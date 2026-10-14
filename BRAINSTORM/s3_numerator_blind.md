# s3_numerator_blind — (J)23/(J)28 relaxations × (J)31/(J)32 numerator data: the relaxations cannot see failures

**Combines:** (J)23 ES^{(S)}, (J)28 ES^□, (J)31 (8/n fails at 131, 241: Pomerance–Weingartner; no BM obstruction:
Bright–Loughran Rem 1.10), (J)32 (complete failure lists for M ≤ 24; m = 4 unique χ-fibre). Deep version:
SYNTHESIS_SPARKS3.md §1–§2.

## Idea
Replace 4 by M ≡ 0 (mod 4) in the shot identity. If the relaxed variant M^□ / M^{(S)} still holds at primes where
the exact M-problem fails, then relaxed certificates carry no information about the success of the finite search,
and every transport (E1) or finite mechanism (E2) must use an input that is false for M = 8.

## Result
* Lemma 1.0 (PROVED): g | n + MQ², g ≡ −1 (mod M) ⇒ M/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, den z | Q².
* **Thm 1.1 (PROVED, Dirichlet only): for every M ≡ 0 (mod 4), M^□(n) holds at every odd non-square n prime to M; at
  odd squares no M-shot exists (T1 for the shot mechanism — not for all M^□ solutions: 4/9 = 1/3 + 1/18 + 1/18).** Key fact: (−M/g) = −1 for every odd g ≡ −1 (mod M).
* Example: **8/131 = 1/20 + 1/131 + 9/2620**, while 8/131 has no unit-fraction solution.
* Cor 2.1: any family of implications "R_M(p) ⇒ M/p" (R_M = M^□ or M^{(S)}) is false at M = 8.

## Literature
Pomerance–Weingartner (8/n failures), Bright–Loughran (BM for m/n surfaces, Rem 1.10); the shot identity is
UNIT_ORBIT_ES Prop 2.1. No source found that states the □/mute relaxation for general numerators (campaign-internal
search only).

## Barrier screen
It IS a barrier (relativisation-type). B1–B6 untouched; the relaxation's shot mechanism keeps T1 (Thm 1.1(b)), so
it is "T1-correct as a mechanism and still blind". It does not bar numerator-free targets (SQ₅/(S), (J)15/(J)32).

## Cheap numerics
`scripts/s3_numerator_blind.py 60` (< 1 s): all 278 failing pairs (M, p), M ∈ {8,12,16,20,24}, p ≤ 10⁸, have exact M^□
certificates (g ≤ 239); T1 control 0 shots at odd squares. `scripts/s3_mute_S.py 100000`: same with fixed S = {3,5,7,11}
for the 264 pairs with p ∉ S, Q ≤ 385.

## Assessment
PROVED barrier with exact scope (the formal content is R₈(131) ∧ ¬(8/131)); SHARP (strategic): both exits need some
numerator-4-specific input; the cleanest known one is the numerator-free χ-fibre (SQ₅). Promise as a route: 0; as steering: high.
