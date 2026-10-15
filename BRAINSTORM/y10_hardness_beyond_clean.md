# y10_hardness_beyond_clean — an archimedean gradient that survives removing all clean levels (O221)

## Idea
Test "hardness = adelic clean-level pattern + polynomial clean levels" on N₋/N within adelic cells (p mod 8, (r/p) for
r ≤ 31, lnr) over all primes p ≡ 1 (4) in (10⁵, 10⁶).

## Findings (EVIDENCE; NEAR_SQUARE §5)
* φ_cl (exact fraction of words on clean levels) explains most variance (corr −0.57); T1-type adds nothing given φ_cl.
* A monotone archimedean gradient in K0 = p − ⌊√p⌋²: −0.05 (K0 < 17) … −0.007 ([100, 300)) … +0.0035 (≥ 300);
  K0 = 24: −0.15.
* About half survives on UNclean levels: N₋/(N − N_cl) residual −0.0093 ± 0.0014 ([30, 100)), −0.0045 ± 0.0008
  ([100, 300)) — near-squares are depleted of χ = −1 words also where no prime is forced.

## Literature
R224 (reviews/three-squares-review.md) for the k = 4, 16 deficit; THREE_SQUARES §2 coin model.

## Barrier screen
B6/B3: averages over p; nothing at a single p. The beyond-clean part is an unexplained correlation (spark S2).

## Cheap numerics
`scripts/ns_census.c`, `scripts/ns_hardness.py census 31`.

## Assessment
EVIDENCE (≈ 5–11σ). The unexplained beyond-clean depletion is the most interesting loose end: some structure of
tp + 1 = c² + t·m² − (c² − 1 − tK0) for small K0 biases χ on unclean levels.
