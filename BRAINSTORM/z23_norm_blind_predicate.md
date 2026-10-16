# z23 — the ES predicate on slice ideals depends only on the norm (O251)

## Idea
Hoped: a class-group walk 𝔤 → 𝔤𝔩 in Cl(−4p) carries a Claude point (2k, Y) to smaller |Y| keeping k | h. Found:
LATTICE_MEETING Thm 1.4 — at a slice g, the Type II solutions with y = p(g+1)/4 are in bijection with the k | h such that
d_k := (−4k²p mod g) divides k (the line's height class satisfies Y_k² ≡ d_k; formally the point (2k, √d)). d_k does not
depend on the root ρ, hence (Cor 1.5) E(𝔤) is a function of N𝔤 alone: ∃ k | (g+1)/4, d | k with g | 4k²p + d.
## Literature
ET Prop 1.3; WINDMILL_REDUCTION Prop 10.3 (form classes see only the genus shadow of m ≡ −1 mod t); ASTRA_BRIDGE Prop 3.2.
## Barrier screen
Sharpens Prop 10.3 in these coordinates: not "the class sees only the genus" but "the predicate does not involve the
class". B2 verbatim (divisor of 4k²p + d in the class −1 mod 4k). B5/T1: at n = c² no slice g ≡ 3 (4) carries a root of −n with gcd(g, 2c) = 1 and g ≡ −1 (4k) meeting the
criterion (Type II is empty at odd squares, ET Prop 1.6), consistent with the criterion.
## Cheap numerics
`scripts/z23_alld.py 6000 3000`: 89 117 slices, the k-criterion reproduced the brute-force Type II solution set at every
slice (0 set mismatches; 5894 ES slices).
## Assessment
PROVED (repackaging of ET Prop 1.3). SHARP as a steering fact: any mechanism whose state is an ideal class (or a form
up to equivalence) is blind to ES by construction; the state must carry the factorisation of (g+1)/4 and p mod g.
