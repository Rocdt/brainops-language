#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, List, Set

ALLOWED_TASK_CLASSES = {"A", "B", "C"}
ALLOWED_CHECK_STATUS = {"pass", "fail", "blocked"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high", "critical"}
ALLOWED_FAILURE_TYPES = {"context_loss", "missing_artifact", "invariant_violation", "overconfidence", "unchecked_assumption"}

def err(msg: str, errors: List[str]) -> None:
    errors.append(msg)

def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def index_artifacts(phases: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    artifacts: Dict[str, Dict[str, Any]] = {}
    for ph in phases:
        for a in ph.get("artifacts", []) or []:
            aid = a.get("id")
            if aid:
                artifacts[aid] = a
    return artifacts

def index_checks(phases: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    checks: Dict[str, Dict[str, Any]] = {}
    for ph in phases:
        for c in ph.get("checks", []) or []:
            cid = c.get("id")
            if cid:
                checks[cid] = c
    return checks

def get_phase(phases: List[Dict[str, Any]], number: int) -> Dict[str, Any]:
    for ph in phases:
        if ph.get("phase") == number:
            return ph
    return {}

def validate(trace: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    for k in ["bol_version", "trace_id", "task", "phases"]:
        if k not in trace:
            err(f"Missing top-level field: {k}", errors)

    task = trace.get("task", {})
    tclass = task.get("class")
    if tclass not in ALLOWED_TASK_CLASSES:
        err(f"Invalid or missing TaskClass: {tclass}", errors)

    phases = trace.get("phases", [])
    if not isinstance(phases, list):
        err("phases must be a list", errors)
        return errors

    expected = [0, 1, 2, 3, 4]
    got = [p.get("phase") for p in phases if isinstance(p, dict)]
    if got != expected:
        err(f"Phases must be exactly [0,1,2,3,4] in order; got {got}", errors)

    p0 = get_phase(phases, 0)
    p1 = get_phase(phases, 1)
    p2 = get_phase(phases, 2)
    p3 = get_phase(phases, 3)
    p4 = get_phase(phases, 4)

    ctx = p0.get("context", {})
    if not ctx:
        err("PHASE 0 must declare Context", errors)
    else:
        for k in ["known", "unknown", "assumptions"]:
            if k not in ctx:
                err(f"Context missing field: {k}", errors)

    hyps = p1.get("hypotheses", [])
    if not hyps or not isinstance(hyps, list):
        err("PHASE 1 must declare at least one Hypothesis", errors)

    artifacts = index_artifacts(phases)
    checks = index_checks(phases)

    blocked_checks: Set[str] = set()
    for cid, c in checks.items():
        st = c.get("status")
        if st not in ALLOWED_CHECK_STATUS:
            err(f"Check {cid} has invalid status: {st}", errors)
        if not c.get("artifacts"):
            err(f"Check {cid} must reference at least one Artifact", errors)
        else:
            for aid in c["artifacts"]:
                if aid not in artifacts:
                    err(f"Check {cid} references missing Artifact id: {aid}", errors)
        if st == "blocked":
            blocked_checks.add(cid)

    failures = p2.get("failures", []) or []
    for f in failures:
        ftype = f.get("type")
        if ftype not in ALLOWED_FAILURE_TYPES:
            err(f"Failure has invalid type: {ftype}", errors)
        if not f.get("correction"):
            err("Failure must include correction", errors)

    risk = p3.get("risk")
    if tclass in {"B", "C"}:
        if not risk:
            err(f"TaskClass {tclass} requires Risk in PHASE 3", errors)
        else:
            rl = risk.get("level")
            if rl not in ALLOWED_RISK_LEVELS:
                err(f"Invalid Risk.level: {rl}", errors)

    gates = p3.get("gates", []) or []
    for g in gates:
        req = g.get("required_artifacts", []) or []
        for aid in req:
            if aid not in artifacts:
                err(f"Gate {g.get('id','<no-id>')} requires missing Artifact id: {aid}", errors)

        if g.get("human_required") is True:
            has_human = any(a.get("type") == "HumanConfirmation" for a in artifacts.values())
            if not has_human:
                err("Human-required Gate requires HumanConfirmation Artifact", errors)

    decision_attempt = p3.get("decision_attempt", {}) or {}
    decision = (decision_attempt.get("decision") or {}) if decision_attempt.get("requested") else {}
    if decision:
        for k in ["owner", "timestamp", "artifacts", "based_on_checks", "result"]:
            if not decision.get(k):
                err(f"Decision missing required field: {k}", errors)

        for aid in decision.get("artifacts", []) or []:
            if aid not in artifacts:
                err(f"Decision references missing Artifact id: {aid}", errors)

        for cid in decision.get("based_on_checks", []) or []:
            if cid not in checks:
                err(f"Decision references missing Check id: {cid}", errors)

        if tclass == "C":
            unknown = (ctx.get("unknown") or []) if isinstance(ctx, dict) else []
            if unknown and decision.get("result") not in {"blocked"}:
                err("TaskClass C with non-empty Context.unknown must block Decision", errors)

        if blocked_checks and decision.get("result") not in {"blocked"}:
            err(f"Blocked checks exist {sorted(blocked_checks)}; Decision must be blocked", errors)

        if failures and decision.get("result") == "approved":
            err("Decision cannot be approved while failures exist (unless explicitly resolved)", errors)

    audit = p4.get("audit", {})
    if not audit:
        err("PHASE 4 must include audit block", errors)
    else:
        if audit.get("conformance") not in {"conformant", "non-conformant"}:
            err("Audit.conformance must be 'conformant' or 'non-conformant'", errors)

    return errors

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: tools/bol_validate.py <trace.json>")
        return 2

    path = sys.argv[1]
    try:
        trace = load_json(path)
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        return 2

    errors = validate(trace)
    if errors:
        print("BOL VALIDATION: FAIL")
        for i, e in enumerate(errors, 1):
            print(f"{i}. {e}")
        return 1

    print("BOL VALIDATION: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
