# Referee report R86 — `paper/es-coverings-note.tex` (coverings note, O86)

Reviewer: hostile referee side agent (branch `side-agent/referee-coverings`).
Status: IN PROGRESS.

## Working notes (§2, first pass)

- Lemma 2.4: correct, but "Σ⊂Ẑ^× clopen, defined modulo M (a union of reduced classes modulo M)"
  is literally inconsistent: a union of classes mod M in Ẑ is not contained in Ẑ^× (Ẑ^× is closed,
  *not* open in Ẑ). Must read Σ = (union of reduced classes mod M) ∩ Ẑ^×, clopen *relative to* Ẑ^×.
  The proof works with that reading (first half places 𝒫(Σ)' inside Ẑ^×).
- Prop 2.5(a),(b): re-derived; argument correct (details below).
