# BrainOps Language (BOL)
## Conformance Specification

This document defines the **normative requirements** for BrainOps Language (BOL) conformance.

The keywords **MUST**, **MUST NOT**, **SHOULD**, **MAY** are to be interpreted as described in RFC 2119.

---

## 1. Definition of Conformance

An implementation is considered **BOL-conformant** if and only if it satisfies **all mandatory requirements** defined in this document.

Any deviation MUST be explicitly documented as a non-conformant behavior.

---

## 2. Levels of Conformance

BOL defines a single conformance level.

There are **no partial or informal compliance levels**.

An implementation is either:
- **BOL-conformant**
- **Non-conformant**

Experimental extensions MUST NOT alter core semantics.

---

## 3. Mandatory Structural Requirements

A BOL-conformant implementation MUST support the following primitives:

- CognitiveUnit
- Task
- TaskClass
- Context
- Invariant
- Constraint
- Artifact
- Check
- Decision
- Risk
- Gate
- IntuitionSignal
- Failure

Omission of any core primitive constitutes **non-conformance**.

---

## 4. Phase Enforcement Requirements

A BOL-conformant implementation MUST enforce the execution phases in the following order:

1. Context Fixation
2. Hypothesis Formation
3. Verification
4. Decision
5. Audit

### Phase Rules

- Phases MUST NOT be skipped.
- Forward jumps between phases are forbidden.
- Backward transitions are allowed.
- A Decision MUST NOT be produced outside PHASE 3.

Violation of phase order constitutes an **execution error**.

---

## 5. Context Requirements

- All knowledge used in reasoning MUST be explicitly declared in Context.
- Any information outside Context MUST be treated as unknown.
- Assumptions MUST NOT influence Decision without Check.

For TaskClass C:
- Non-empty `Context.unknown` MUST block Decision.

---

## 6. Artifact Requirements

- Every Check MUST reference at least one Artifact.
- Artifacts MUST be identifiable and auditable.
- Missing required Artifacts MUST block Decision.

An implementation MUST treat absence of required Artifacts as **invalid execution**, not as a warning.

---

## 7. Check and Decision Requirements

- Every Decision MUST be based on completed Checks.
- Checks MUST have an explicit status: pass, fail, or blocked.
- A Decision based on failed or blocked Checks MUST be marked invalid.

Decision without owner attribution is invalid.

---

## 8. TaskClass Enforcement

An implementation MUST enforce TaskClass rules:

### TaskClass A
- Human intervention MAY be omitted.
- Risk MAY be omitted.

### TaskClass B
- Risk MUST be declared.
- Human intervention MAY be required depending on Gate conditions.

### TaskClass C
- Risk MUST be declared.
- Human intervention MUST be explicitly confirmed.
- Decision MUST be blocked without human confirmation Artifact.

Failure to enforce TaskClass rules constitutes **critical non-conformance**.

---

## 9. Invariant and Constraint Enforcement

- Invariants MUST have absolute priority over Task progress.
- Violation of any Invariant MUST block Decision immediately.
- Forbidden actions in Constraint MUST override Allowed actions.

Invariant or Constraint violations MUST be recorded as Failure events.

---

## 10. Gate Enforcement

- Gate conditions MUST be evaluated before phase transitions.
- Unmet Gate conditions MUST block execution.
- Human-required Gates MUST NOT be auto-resolved.

Gate bypassing is strictly forbidden.

---

## 11. Risk Handling Requirements

- Risk MUST be declared for TaskClass B and C.
- Risk level MUST influence verification depth.
- Critical risk MUST trigger explicit Audit phase entry.

Ignoring Risk constitutes a semantic violation.

---

## 12. IntuitionSignal Handling

- IntuitionSignal MUST NOT directly produce Decision.
- IntuitionSignal MAY only influence Hypothesis formation.
- IntuitionSignal MUST be recorded explicitly if used.

Implicit intuition is forbidden.

---

## 13. Failure Handling Requirements

- Failure MUST be treated as a first-class entity.
- Failure MUST include a correction strategy.
- Failure MUST be auditable.

Failure MUST NOT be silently ignored.

---

## 14. Auditability Requirements

A BOL-conformant implementation MUST:

- Preserve execution trace
- Preserve artifact references
- Preserve phase transitions
- Preserve failures and corrections

Loss of audit trail constitutes non-conformance.

---

## 15. Declaration of Conformance

An implementation claiming BOL compliance MUST provide a declaration including:

- BOL version supported
- Deviations, if any
- Supported extensions
- Known limitations

Implicit or assumed compliance is invalid.

---

## 16. Non-Goals of Conformance

Conformance does NOT require:
- A specific syntax
- A specific storage format
- A specific UI
- Automation

Conformance applies to **semantics and enforcement**, not presentation.

---

## 17. Final Conformance Rule

If an implementation allows a Decision to be made:
- without artifacts
- without enforced phases
- without risk consideration
- without required human intervention

then it is **not BOL-conformant**.
