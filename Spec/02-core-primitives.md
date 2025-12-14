# BrainOps Language (BOL)
## Core Primitives Specification (Normative)

This document defines the **minimal vocabulary** of BrainOps Language (BOL).
All primitives defined here are **normative**.

Any implementation claiming BOL compliance MUST support **all** primitives
defined in this document without weakening their semantics.

Keywords **MUST**, **MUST NOT**, **SHOULD**, **MAY** are normative.

---

## 1. CognitiveUnit

### Definition
A **CognitiveUnit** is the minimal atomic unit of formalized thinking.

### Types
CognitiveUnit ::= Task | Hypothesis | Check | Decision

### Rules
- Only defined CognitiveUnit types MAY exist.
- A Decision MUST NOT exist without at least one completed Check.
- CognitiveUnits MUST be explicitly declared.

---

## 2. Task

### Definition
A **Task** is a formalized objective with verifiable completion.

### Structure
Task {
  id
  goal
  class
}

### Rules
- Task MUST have a unique id.
- Task MUST declare a TaskClass.
- Task without TaskClass is invalid.
- Task MAY NOT directly produce a Decision.

---

## 3. TaskClass

### Definition
TaskClass defines the **risk profile** of a Task.

### Types
TaskClass ::= A | B | C

- A: low risk, no mandatory human check
- B: medium risk, conditional human check
- C: high stakes, mandatory human check

### Rules
- TaskClass determines verification depth.
- TaskClass determines human involvement.
- TaskClass rules MUST be strictly enforced.

---

## 4. Context

### Definition
**Context** is the only admissible container of knowledge.

### Structure
Context {
  known
  unknown
  assumptions
}

### Rules
- Anything outside Context is treated as unknown.
- assumptions MUST NOT influence Decision without Check.
- For TaskClass C, non-empty unknown MUST block Decision.

---

## 5. Hypothesis

### Definition
A **Hypothesis** is a testable assumption derived from Context.

### Rules
- Hypothesis MUST be explicitly declared.
- Hypothesis MUST be verifiable or explicitly rejected.
- Hypothesis MUST NOT directly produce Decision.

---

## 6. Check

### Definition
A **Check** is a verification procedure.

### Structure
Check {
  target
  artifacts
  status
}

status ::= pass | fail | blocked

### Rules
- Check MUST reference at least one Artifact.
- Check without Artifacts is incomplete.
- Check status MUST be explicit.

---

## 7. Artifact

### Definition
An **Artifact** is verifiable evidence of reasoning.

### Structure
Artifact {
  type
  source
  validates
}

### Rules
- Artifacts MUST be auditable.
- Missing required Artifacts MUST block Decision.
- Artifacts MAY be human or machine generated.

---

## 8. Invariant

### Definition
An **Invariant** is a non-negotiable rule.

### Structure
Invariant {
  id
  description
}

### Rules
- Invariant violation blocks Decision immediately.
- Invariants have priority over Task progress.

---

## 9. Constraint

### Definition
A **Constraint** limits allowed actions.

### Structure
Constraint {
  scope
  forbidden
  allowed
}

### Rules
- Forbidden overrides Allowed.
- Constraint violation MUST trigger a Gate.

---

## 10. Risk

### Definition
**Risk** represents cognitive risk assessment.

### Structure
Risk {
  level
  reason
  mitigation
}

level ::= low | medium | high | critical

### Rules
- Risk is mandatory for TaskClass B and C.
- Critical risk MUST trigger Audit phase.

---

## 11. Gate

### Definition
A **Gate** is a forced stopping point.

### Structure
Gate {
  condition
  required_artifacts
  human_required
}

### Rules
- Unmet Gate blocks phase transition.
- Human-required Gates MUST NOT be auto-resolved.

---

## 12. Decision

### Definition
A **Decision** is the finalized outcome of thinking.

### Structure
Decision {
  based_on
  artifacts
  owner
  timestamp
}

### Rules
- Decision MUST reference completed Checks.
- Decision MUST reference Artifacts.
- Decision MUST have an owner.
- Decision without audit trail is invalid.
