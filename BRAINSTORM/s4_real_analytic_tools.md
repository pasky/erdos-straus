# s4_real_analytic_tools — theta positivity on iℝ, IVT/degree on real points, SOS certificates, Hodge-index/Hasse positivity: what each gives at a single n (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. One screen per tool from O218 goal (2), against the frame
of s4_three_bits_meta (ES-five(n) ⟺ X_n(ℤ) ∩ (D × Ω₂) ≠ ∅; D the positive component).

## 1. Θ > 0 on iℝ (Jacobi triple product)
θ_L(iy) = Σ_{x∈L} e^{−πy Q(x)} > 0 for definite L. *At a single n* it gives non-emptiness of genera and the Siegel–Weil
main term r(gen L, T) > 0 whenever T is locally represented ((J)13, (J)45 §5). On the χ = +1 side the genus of ℤ³ is
one class (TWO_FIBRES Thm A), so θ-positivity is exact there and says "non-certificates exist when the local
conditions allow" — the wrong side. On the χ = −1 side it gives the genus average, whose positivity is the
local/genus layer, true at odd squares' neighbours and blind to path bases (B2: the path basis is a thin
extraction, p^{o(1)} words on average — R219 D10e: the earlier "≪ p^{1/3+o(1)}" was unsupported; pointwise only Elsholtz–Tao f_II ≪ p^{2/5+o(1)} — of ≍ p classes). The modular transformation θ(−1/τ) — the archimedean proof of quadratic
reciprocity (Hecke) — *is* the product formula ε_∞ε₂ε_n = 1; so θ supplies T1, not existence. **Verdict:
COLLAPSES (B6 + B2); positivity of θ is the genus layer.** Harness: numerator-blind (θ never sees 4 vs 8).

## 2. Intermediate value / topological degree on real points
D ≅ ℝ²_{>0} (L2), so real points in D always exist and are connected; a degree/IVT argument proves only real (or
2-adic-and-real, by weak approximation) points. Integrality of t = (n + u + v)/(uv) is the exact divisibility uv | n +
u + v (B2). On the Markoff-type S_{n,D} (GROWING_MUTE) the real locus is a conic bundle with all fibres real for
C ≫ 0; IVT gives a real point in every fibre and nothing integral. Brouwer/Lefschetz fixed points of the Vieta
involutions: one integral involution only ((J)36), fixed loci are real curves with no forced integral point.
**Verdict: COLLAPSES — real topology holds at odd squares too (D is the same at n = m²).**

## 3. Sum-of-squares / Positivstellensatz certificates
SOS certificates prove *real* infeasibility or real positivity; ES failures at odd squares are not real-infeasible
(D is non-empty at m²), so no real certificate can encode T1, and conversely a real-algebraic argument proving a
point exists proves it at m² too. Integer SOS (e.g. ℤ-Positivstellensatz) is undecidable in general; the relevant
decidable piece is the lattice one (s4_selling_voronoi_wall), i.e. reduction theory. **Verdict: COLLAPSES (T1 is
not real).**

## 4. Hodge index / Hasse–Weil positivity (Arakelov flavour)
The Hasse bound |a| ≤ 2√p (Hodge index on E × E) plus Deuring (every a in the window occurs: H(4p − a²) > 0, itself
an L(1, χ_odd) > 0 / class-number positivity) is a genuinely deterministic positivity theorem at a single p. Its ES
use: Type II j = 1 tickets are curves of trace 1 − c with a subgroup of order ≡ −1 (mod 4c), i.e. "p + c has a
divisor ≡ −1 (mod 4c)" (TORSION_FIRING Props 4.2/4.3; R206 D7: the curve plays no role). Bogomolov/Zhang successive
minima give small *algebraic* points, not integral rational ones. **Verdict: COLLAPSES to B2 (TORSION_FIRING
(J)44).** Remark: the positivity here (class numbers > 0) is the same archimedean input that gives the provable
relaxations their Dirichlet prime g ≡ −1 (mod M) (L(1, χ) ≠ 0 for odd real χ is the class-number formula) — so the
proved T1-bearing variants ((J)23, (J)41) already use the archimedean place, at a fixed modulus.

## Cheap numerics
None new: each verdict reduces to an already-certified statement (L1/L2 in `scripts/s4_signed_nadic.py`;
TORSION_FIRING §4 numbers). Odd-square control is structural (D, θ, real topology are identical at m²).

## Assessment
All four "real-analytic positivity" tools act on the *real* or *genus* layer, which is identical at odd squares and
primes; they cannot encode T1, hence cannot prove ES (meta-statement of s4_three_bits_meta). The archimedean input
that does matter is ε_∞ = −1 inside a global product formula; analytic positivity (θ, class numbers) re-proves that
product formula, it does not go beyond it. Promise 0/5.
