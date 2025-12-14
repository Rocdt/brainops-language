# BrainOps Language (BOL)

BrainOps Language (BOL) is a **normative specification** for constraining, recording, and auditing thinking in systems where error has a non-trivial cost.

BOL is **not**:
- a programming language
- a prompt style
- a UI or workflow framework
- a model training method

BOL **is**:
- a language of admissible thinking
- a framework for evidence-based verification (Artifacts)
- a phase-based execution model (0→4)
- a binary conformance standard (conformant / non-conformant)

This repository is the **canonical source of truth** for BOL.

---

## Authorship
- Author: Rocdt
- First public release: 2025-12-14
- Canonical repository: https://github.com/Rocdt/brainops-language

---

## Specification

BOL is defined as a set of normative documents:

- Scope and applicability: `spec/00-scope.md`
- Fundamental principles: `spec/01-principles.md`
- Core-12 (one-page minimal core): `spec/01-core-12.md`
- Core primitives: `spec/02-core-primitives.md`
- Execution semantics (phases): `spec/03-execution-semantics.md`
- Failure model: `spec/04-failure-model.md`
- Conformance specification: `spec/05-conformance.md`
- Core-12 ↔ Conformance matrix: `spec/06-core12-conformance-matrix.md`
- Grammar (EBNF): `spec/grammar/bol.ebnf`
- Reference execution trace (end-to-end): `spec/07-reference-execution-trace.md`

Normative keywords MUST / MUST NOT / SHOULD / MAY are used consistently.

---

## Machine-readable Artifacts (Reference Implementation Layer)

This repo also includes:
- JSON reference traces in `traces/`
- A reference validator in `tools/`

These files allow automated conformance checks.

---

## Versioning

BOL follows Semantic Versioning:
- MAJOR: breaking changes to primitives or semantics
- MINOR: backward-compatible extensions
- PATCH: clarifications and editorial fixes

See `CHANGELOG.md`.

---

## License
See `LICENSE`.
EOF

---

## Authorship
- Author: Rocdt
- GitHub: https://github.com/Rocdt
- Authors file: AUTHORS.md
- First public release: 2025-12-14

