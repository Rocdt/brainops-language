# Changelog
All notable changes to BrainOps Language (BOL) are documented in this file.

This project follows Semantic Versioning.

---

## Versioning Policy

- **MAJOR** — breaking changes to core primitives or execution semantics
- **MINOR** — backward-compatible extensions or new normative sections
- **PATCH** — clarifications, editorial fixes, or non-normative updates

Versions prior to v1.0 are experimental but authoritative.

---

## [0.1.0] — Foundation Specification
**Release date:** 2025-12-14

### Added
- Core-12 specification (minimal normative core)
- Core Primitives specification
- Execution Semantics (phase-based execution model)
- Failure Model (first-class failure handling)
- Conformance Specification
- Core-12 ↔ Conformance Matrix
- Formal EBNF grammar
- Reference examples (Hello World, blocked execution)

### Defined
- Normative use of MUST / MUST NOT / SHOULD / MAY
- Binary conformance model (conformant / non-conformant)
- Human-in-the-loop as explicit artifact
- Artifact-based verification as mandatory

### Clarified
- Distinction between failure and invalid execution
- Separation of thinking, verification, and decision
- Auditability as a mandatory property

---

## [Unreleased]
### Planned
- Reference Execution Trace (end-to-end example)
- Domain profiles (engineering / medical / legal)
- Extension mechanism without Core-12 breakage
