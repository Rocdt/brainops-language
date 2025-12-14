# BrainOps Language (BOL)
## Execution Semantics (Normative)

This document defines how thinking is executed over time in BOL.

Execution semantics are mandatory and enforceable.
Violation constitutes a **spec violation**.

---

## 1. Execution Model

BOL enforces **sequential, auditable execution** of thinking.
Uncontrolled flow of thought is forbidden.

---

## 2. Execution Phases

### PHASE 0 — Context Fixation
- Context MUST be fully declared.
- Unknowns MUST be identified.
- Assumptions MUST be explicit.

Exit condition:
- Context declared and stable.

---

### PHASE 1 — Hypothesis Formation
- Hypotheses MAY be generated.
- IntuitionSignal MAY be recorded.
- No verification occurs.

Exit condition:
- Hypotheses explicitly declared.

---

### PHASE 2 — Verification
- Checks MUST be executed.
- Artifacts MUST be collected.
- Failures MAY occur.

Exit condition:
- All relevant Checks completed or blocked.

---

### PHASE 3 — Decision
- Decision MAY be produced.
- Gates MUST be evaluated.
- Human confirmation enforced if required.

Exit condition:
- Decision accepted or blocked.

---

### PHASE 4 — Audit
- Execution trace reviewed.
- Failures recorded.
- Compliance verified.

Exit condition:
- Audit completed.

---

## 3. Phase Transition Rules

- Phases MUST NOT be skipped.
- Forward jumps are forbidden.
- Backward transitions are allowed.
- Transition without required Artifacts is invalid.

---

## 4. Gate Enforcement

- Gates MUST be evaluated before phase transitions.
- Unmet Gates block execution.
- Human-required Gates MUST halt automation.

---

## 5. Human-in-the-Loop

- Humans are responsibility holders, not truth sources.
- Human confirmation MUST be explicit.
- Human confirmation MUST be recorded as Artifact.

---

## 6. Invalid Execution

Execution is invalid if:
- Phases are skipped
- Gates are bypassed
- Artifacts are missing
- Decisions are premature
