# BrainOps Language (BOL)
## Core-12 ↔ Conformance Matrix (Normative)

This document defines the **explicit mapping** between the Core-12 elements
and the mandatory conformance requirements defined in `spec/05-conformance.md`.

This matrix is normative.
Any implementation claiming BOL compliance MUST satisfy all mappings.

---

## Purpose of This Matrix

The goal of this document is to eliminate ambiguity.

- Core-12 defines **what exists**
- Conformance defines **what must be enforced**
- This matrix defines **what must be checked**

If a Core element is present but its conformance rules are not enforced,
the implementation is **non-conformant**.

---

## Matrix Overview

Each Core element is mapped to:
- Mandatory enforcement rules
- Relevant conformance sections
- Failure conditions

---

## Core-12 Conformance Mapping

### 1. Task
**Core Definition:** `spec/01-core-12.md#1-task`

**Conformance Requirements:**
- Task MUST have id, goal, and class
- TaskClass MUST be enforced

**Referenced Sections:**
- Conformance §3 (Structural Requirements)
- Conformance §8 (TaskClass Enforcement)

**Failure Conditions:**
- Missing TaskClass
- Task producing Decision without verification

---

### 2. TaskClass
**Core Definition:** `spec/01-core-12.md#2-taskclass`

**Conformance Requirements:**
- TaskClass rules MUST be enforced exactly
- Human-check MUST be enforced for TaskClass C

**Referenced Sections:**
- Conformance §8 (TaskClass Enforcement)

**Failure Conditions:**
- Human-check bypassed
- Risk omitted for TaskClass B or C

---

### 3. Context
**Core Definition:** `spec/01-core-12.md#3-context`

**Conformance Requirements:**
- All knowledge MUST be declared in Context
- Unknown MUST block Decision for TaskClass C

**Referenced Sections:**
- Conformance §5 (Context Requirements)

**Failure Conditions:**
- Implicit knowledge used
- Decision made with unresolved unknowns

---

### 4. CognitiveUnit
**Core Definition:** `spec/01-core-12.md#4-cognitiveunit`

**Conformance Requirements:**
- Only defined CognitiveUnit types MAY exist
- Decision MUST depend on Check

**Referenced Sections:**
- Conformance §3 (Structural Requirements)
- Conformance §7 (Check and Decision)

**Failure Conditions:**
- Decision without Check
- Undefined unit types introduced

---

### 5. Hypothesis
**Core Definition:** `spec/01-core-12.md#5-hypothesis`

**Conformance Requirements:**
- Hypothesis MUST be verifiable or rejected
- Hypothesis MUST NOT directly produce Decision

**Referenced Sections:**
- Conformance §7 (Check and Decision)

**Failure Conditions:**
- Untested hypothesis influencing Decision

---

### 6. Check
**Core Definition:** `spec/01-core-12.md#6-check`

**Conformance Requirements:**
- Check MUST reference Artifacts
- Check MUST have explicit status

**Referenced Sections:**
- Conformance §6 (Artifact Requirements)
- Conformance §7 (Check and Decision)

**Failure Conditions:**
- Check without Artifacts
- Ambiguous Check status

---

### 7. Artifact
**Core Definition:** `spec/01-core-12.md#7-artifact`

**Conformance Requirements:**
- Artifacts MUST be auditable
- Required Artifacts MUST block Decision if missing

**Referenced Sections:**
- Conformance §6 (Artifact Requirements)
- Conformance §14 (Auditability)

**Failure Conditions:**
- Missing or unverifiable Artifacts

---

### 8. Invariant
**Core Definition:** `spec/01-core-12.md#8-invariant`

**Conformance Requirements:**
- Invariants MUST override Task progress
- Invariant violation MUST block Decision

**Referenced Sections:**
- Conformance §9 (Invariant Enforcement)

**Failure Conditions:**
- Decision made after invariant violation

---

### 9. Constraint
**Core Definition:** `spec/01-core-12.md#9-constraint`

**Conformance Requirements:**
- Forbidden MUST override Allowed
- Constraint violation MUST trigger Gate

**Referenced Sections:**
- Conformance §9 (Invariant and Constraint Enforcement)

**Failure Conditions:**
- Forbidden action executed

---

### 10. Risk
**Core Definition:** `spec/01-core-12.md#10-risk`

**Conformance Requirements:**
- Risk MUST be declared for TaskClass B and C
- Risk level MUST influence verification depth

**Referenced Sections:**
- Conformance §11 (Risk Handling)

**Failure Conditions:**
- Risk omitted
- Critical risk ignored

---

### 11. Gate
**Core Definition:** `spec/01-core-12.md#11-gate`

**Conformance Requirements:**
- Gate conditions MUST be enforced
- Human-required Gates MUST NOT be auto-resolved

**Referenced Sections:**
- Conformance §10 (Gate Enforcement)

**Failure Conditions:**
- Gate bypassed
- Human-check faked or implicit

---

### 12. Decision
**Core Definition:** `spec/01-core-12.md#12-decision`

**Conformance Requirements:**
- Decision MUST reference Checks and Artifacts
- Decision MUST have owner and timestamp

**Referenced Sections:**
- Conformance §7 (Check and Decision)
- Conformance §14 (Auditability)

**Failure Conditions:**
- Anonymous Decision
- Decision without audit trail

---

## Global Non-Conformance Rule

If any Core-12 element:
- exists without its enforcement rules
- is partially enforced
- is treated as advisory

then the implementation is **not BrainOps Language conformant**.

---

## Final Note

This matrix is intentionally strict.

BOL compliance is binary:
- enforced
- or invalid
