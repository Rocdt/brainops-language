# BrainOps Language (BOL)
## Failure Model (Normative)

Failure is a **first-class concept** in BOL.
Failure is expected, explicit, and auditable.

---

## 1. Definition of Failure

A **Failure** represents a detected breakdown in thinking execution.

Failure {
  type
  correction
}

Failure is NOT an exception.
Failure is part of correct execution.

---

## 2. Failure Types

### context_loss
Loss or corruption of Context integrity.

### missing_artifact
Required Artifact not provided.

### invariant_violation
Invariant breached.

### overconfidence
Decision pressure without sufficient verification.

### unchecked_assumption
Assumption used without Check.

---

## 3. Failure Handling Rules

- Failure MUST be explicitly recorded.
- Failure MUST include correction strategy.
- Failure MUST block Decision unless resolved.

---

## 4. Recovery

- Recovery MAY involve backtracking phases.
- Recovery MUST preserve audit trail.
- Silent recovery is forbidden.

---

## 5. Failure vs Invalid Execution

- Failure: recoverable with correction.
- Invalid execution: non-conformant and rejected.

---

## 6. Audit Requirements

- All Failures MUST be auditable.
- Failure history MUST be preserved.
