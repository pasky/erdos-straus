# Non-ANT literature lane (L7, z52)

## §0 Summary
- **New since 2026-09-28:** research pending; no claims yet.
- **Transferable structural features:** pending source verification.
- **Campaign verdict changes:** none identified yet.

## §1 Verified entries

1. **AI/Lean-assisted Erdős-problem resolution (related divisibility problem, not ES).** Nat Sothanaphan, “Resolution of Erdős Problem #728: a writeup of Aristotle’s Lean proof,” arXiv:2601.07421v5 (26 Jan 2026), accessed 30 Oct 2026. Theorem 1 proves: for any 0 < C₁ < C₂ and 0 < ε < 1/2, infinitely many triples (a,b,n) satisfy εn ≤ a,b ≤ (1−ε)n, a!b! | n!(a+b−n)!, and C₁ log n < a+b−n < C₂ log n. The proof reduces to binomial divisibility, then uses Kummer carries and a scale-by-scale counting/union-bound argument to choose carry-rich but spike-free integers m; the Lean proof is described in §6. **Status:** arXiv preprint, formal proof reported; no journal publication verified here. Its own Appendix “beyond this proof” explicitly notes a similar Pomerance argument and reports close/similar results, so the AI provenance does not establish a novel mathematical method. **Relation:** existing `BRAINSTORM/logic_complexity.md` and `BRAINSTORM/z45_program_synthesis.md`; this is a fresh specific case, but no ES verdict changes. Decisive excerpt: `sources/z52/nonant/erdos728.txt`.

2. **SAT-certified finite extremal theorem.** Marijn J.H. Heule, “Schur Number Five,” arXiv:1711.08076v1 (submitted 21 Nov 2017), accessed 30 Oct 2026. Abstract states the maximal n for a 5-coloring of {1,…,n} without monochromatic a+b=c is 160; it was encoded in propositional logic, solved by massively parallel SAT, and the two-petabyte proof certified by a formally verified checker. **Status:** published at AAAI 2018 (arXiv page says accepted); finite extremal computation. **Relation:** `BRAINSTORM/logic_complexity.md`, `BRAINSTORM/z32_adversarial_search.md`; the finite-domain boundary is exactly why this is not an infinite ES certificate. Excerpt: `sources/z52/nonant/schur5.txt`.

## §2 Structural-feature table

| Problem | Structural feature making it solvable | Does ES share it? | Transfer verdict |
|---|---|---|---|

## §3 NEW candidates

None identified yet; source and prior-work screening pending.

## §4 Not accessed / could not verify / incorrect leads

Research pending.
