# z35_free_quartic_bit — every b = 1 certificate carries a canonical quartic bit; is it forced ("quartic T1")? (O265)

## Idea
Witnesses w have (w/p) = −1 forced (the T1 sign). For p ≡ 5 (8), 2 is a non-residue, so β(w) := (2w/p)_4 = ±1 is a canonical
(π ↔ π̄-invariant) bit; for any p, (w₁w₂/p)_4 = ±1 for two witnesses. If the certificate equations forced β, there would be a
quartic analogue of T1 (a new obstruction law, and a new invariant to steer by).

## Literature
MODP_RECIPROCITY Prop 1.2(b): β(w) = (d/p)_4 (g/p)_4⁻¹ · const, a function of (a, b) modulo the parameters.

## Barrier screen
If forced, it would be visible at bounded parameters as a congruence in (a, b) — the Gaussian refinement of B1; T1-type: at
squares β is undefined (no certificates).

## Cheap numerics
`scripts/z35_quartic_independence.py` (p < 2·10⁶, d ≤ 40): β = +1: 281 437, β = −1: 282 747 (49.9/50.1 %). A pilot over
p < 10⁵ gave pair bits (w₀w/p)_4 balanced to within within-p correlation (54/46 % for p ≡ 1 (8), not a law).

## Assessment
EVIDENCE (negative): the quartic bit is balanced at d ≤ 40; there is no quartic T1. (R275 repair: not free in general — w·m = cp + 1 gives β(w) = ((2/m)/p)_4, equal to the Legendre symbol (k/p) on windows m = 2k²; over all witnesses, p ≤ 2·10⁵, 51.8/48.2 %.) Spark: the bit is a well-defined ±1-valued
function on the certificate set of p ≡ 5 (8) — could it be the sign of an involution or a Brauer–Manin pairing (quartic
Hilbert symbol) on the ES surface? Not pursued.
