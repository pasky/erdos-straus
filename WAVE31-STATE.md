# Wave 31 — PAUSED MID-WAVE (2026-08-30). Resume here.

Coordinator state file; DELETE at wave-31 merge. Session paused externally
(credits) right after the three parallel units landed, BEFORE hostile review.
**Nothing from wave 31 is merged or reviewed yet. Base = 373a095 (Outcome 34).**

## Unit branches (fetched from /tmp clones; clones disposable)

- `wave31-unitA` = 4f061a7 — notes §73 "block reduction" + verify (bt).
  Unit summary: proved F1/CF3/BLK mechanism trichotomy; self-contained,
  effective dimension-uniform Brun fundamental lemma; UNCONDITIONAL no-block
  stacking for every fixed 0<θ<1 with tail exponent (1−θ)L^θ/(4θ); full
  a₁-tail reduced to named open joint hypothesis H_BLK(θ). Unit's honest
  corrections vs coordinator sketch: literal H_FAIL NOT proved (elementary
  truncation leaves polylog losses); CF3 needs multiple maximal subgroups;
  the (1−θ) loss unavoidable in this method; NO "almost every deep prime is
  block-driven" claim (needs a lower bound we don't have).
- `wave31-unitB` = 0e71d6b — notes §74 F3 stratification + verify (bu).
  Unit summary: exact stratification of F3 by generated subgroup K (per-
  stratum bounds H(log H)^{d/(2n)−1}(loglog H)^{B_{a,K}}); HEADLINE: global
  target-transversal bound #F3_a(H) ≪_a H(loglog H)^{K_a+1}/(log H)^{3/4+1/(4n)}
  for every fixed prime a≡3(4) — beats Theorem 70.7 for all a≥7; applies to
  ALL of F3, not just the K=G stratum. F1-dominance rate upgraded. Correction:
  for n=(a−1)/2 PRIME (e.g. a=23) the d=1 stratum is empty ⇒ all F3 is
  full-group there. Census fingerprint: structurally consistent, quantitative
  finite-scale prediction honestly declined ((loglog)^K factors).
- `wave31-unitC` = 4b710ff — paper v17 (151→177pp), §70–§72 absorbed as
  Sections 32–34; pdflatex clean; 3 declared judgment calls (missing row
  terminator fix in table (71.24), \resizebox on wide tables, reference
  mapping) — reviewer must check these.

## Mandatory next steps (house norms — do NOT skip)

1. Hostile adversarial review of §73 (fresh deep subagent, clone of
   wave31-unitA), MAX severity: the dimension-uniform Brun lemma's explicit
   constants + level condition z^{2r}≤N^{1/2} at κ~L^θ; the Siegel/exceptional-
   zero one-sided Mertens argument; the 3^J entropy bookkeeping; H_BLK's
   exact form; every quantifier in the stacking theorem. Reviewer replays
   (bt) numerics from scratch.
2. Hostile review of §74 likewise (clone of wave31-unitB): the pair-exclusion
   quantifier chain (self-paired class c₀=t^{(n+1)/2}, multiplicity caps,
   distinct-primes bookkeeping, union over g and side-choices); the within-K
   budget rigidity transfer; stratum exhaustiveness; independent from-scratch
   replay of (bu) (headline is record-class within its scope ⇒ full protocol).
3. Repair rounds until SOUND; then merge A then B into main via the
   append-append tail-reassembly protocol (git show branch:file + Python
   line surgery; ast.parse verify.py; grep -c '<<<<<<<\|>>>>>>>' on notes.md,
   verify.py, paper/espaper.tex — NOTE grep -c exits 1 on zero matches, no
   && after it; control-byte check; grep "^## " for all section headers).
4. Full `uv run --with sympy,numpy,scipy python verify.py` (timeout 700+,
   ~220s+, foreground) green BEFORE and AFTER every merge.
5. Paper v17 FAITHFUL review (deep subagent) against notes §70–§72; repairs;
   merge wave31-unitC (espaper.tex has no overlap with A/B — merge after A/B
   so README/paper mentions can be reconciled once).
6. PROJECT.md Outcome 35 + delete this file + commit. Then wave 32
   (candidate leads: H_BLK structure at growing a — the isolated wall;
   §74's recursion-into-C_n remark; H_XW/H_EQ; paper v18 = §73–§74).

## Standing orders from pasky (preserve verbatim in any future handoff notes)

(a) Run LONGER than the predecessor session — many waves, no check-ins; do
not stop until the conjecture is proven or you are stopped. Honest failure
logs and new obstruction theorems are acceptable byproducts; overclaiming is
the ONE forbidden outcome.
(b) The wave-31+ priorities below are SUGGESTIONS only — you, the new
session, pick a maximally ambitious SHORTEST PATH to a final E-S proof, and
you may replace or reorder freely.
(c) You have permission to use the session handoff tool AUTONOMOUSLY when
your context nears its limit (just not too often) — the chain
self-perpetuates; each handoff must carry these standing orders forward.
(d) gl hf, ad astra.
