# anal_euler_product_law — is f(p) an L(1,χ_p)-type Euler-product statistic? (O151, angle (c), own idea)

Labels as in DISCOVERIES.md. χ_p(q) = (p/q) (Legendre). L_Y(p) = Π_{3≤q≤Y} (1 − χ_p(q)/q)^{−1}, a truncated
L(1,χ)-proxy (for p ≡ 1 (4), χ_p is the character of ℚ(√p) at odd q). g(p) = f(p)/log³p. ES is not solved here.

## 1. Idea

The hard primes for ES are the "square-mimicking" ones (p a square modulo many small q: Mordell's classes mod 840,
POINTWISE_SIZE X5). The natural analytic statistic measuring square-mimicking with 1/q weights is L(1,χ_p): it is
large exactly when χ_p(q) = +1 for many small q. Exotic hope (an Erdős–Wintner / Chowla–Erdős picture for ES):
(E1) `g(p) ≈ G·L(1,χ_p)^{−β}` with a fixed β > 0, so the lower tail of f is the upper tail of L(1,χ_p), which is
completely understood (Granville–Soundararajan: L(1,χ) ≤ e^γ log log + O(1) except on a doubly-exponentially rare set;
under GRH L(1,χ) ≤ (2e^γ + o(1)) log log p, Littlewood). A pointwise version `f(p) ≥ c log³p·L(1,χ_p)^{−β}` would
give ES under GRH and "ES with an explicit doubly-exponentially thin structured exceptional set" unconditionally.
(E2) T1 analogy: at n = m² (odd), χ_n is principal off m and L(s,χ_n) has the pole of ζ at s = 1, so (E1)
"predicts" f(m²) = 0 — the square obstruction would be the limit of the Euler-product law.

## 2. Literature anchor

Chowla–Erdős (1951), Elliott, Granville–Soundararajan (GAFA 2003) on the distribution of L(1,χ_d); Littlewood (1928)
GRH bounds — all from memory, unverified details. No ES source relates f(p) to L(1,χ_p) (campaign files searched:
only the least non-residue n_p is used, POINTWISE_TYPEI/OMEGA, for the *minimal* witness). Novelty of the
observation: Assessment; not literature-searched online.

## 3. Barrier screen

* **B1 (decisive).** E[f(p) | χ_p(q), q ≤ Y] is a Haar/CRT conditional mean, i.e. a CRT majorant/minorant on the
  residue of p mod Π q. POINTWISE_SIZE Prop A / Thm F: such data cannot prove ES; a pointwise form of (E1) would
  have to control the residual, which is the lottery (B2). COLLAPSES.
* **The law is lower order (EVIDENCE §4).** Within p ≡ 1 (mod 8) the fitted β decreases like 1/log p
  (β·log p ≈ 6.2 for f_I, ≈ 4.5 for f_II over three decades). So the true shape is
  `log f(p) ≈ log(κ log³p) − (A/log p)·log L(1,χ_p)`, i.e. `f(p) ≈ κ log³p − κA log²p·log L(1,χ_p)`: local data
  move the *conditional mean* by a relative `O(log log p/log p)` (unconditionally, L(1,χ) ≪ log p) or
  `O(log₃p/log p)` under GRH. Square-mimicking can never make the conditional mean small. This is the CRT picture of
  CEILINGS_UNIFIED (mass ≍ 𝓛³ over all scales; small moduli carry a vanishing fraction) made quantitative.
* **B5/T1.** (E2) is spurious. Along primes that are squares mod every q ≤ Y the model predicts only a relative
  depression `(A/log p)·log log Y`, never 0; and at m² the zero is the global reciprocity identity of EXF Prop 2.1
  (−4d is an odd character evaluated at X ≡ −1), not a small-prime effect. The step of (E1) that is false at m² is
  "the residual (non-local) part is ≥ 0 on average-sized scale": at m² the *global* Jacobi constraint kills every
  block simultaneously, which no Euler product over small q sees.
* **B2/B3/B6.** The residual after local data is the shift-factorisation lottery (anal_moments_structured §3.3);
  any lower bound for it at a single p is H-A/H-B. Proving (E1) even on average over p ≡ r (mod Q) (an asymptotic
  for Σ_{p≡r(Q)} f(p) with explicit local factor) would be a new averaged theorem (beyond ET's ≍), irrelevant pointwise.
* **B4.** Not a pigeonhole construction. **T5**: on the X5 fibre (log Q ≍ 𝓛⁴) the model predicts the same
  log³p mass minus a log²p·O(𝓛)-size correction — consistent with X5 (only small-modulus solutions are removed).

## 4. Experiments (scripts/bs_anal_lfun_corr.py, scripts/bs_anal_euler_profile.py; counts from spec_typecount to 4·10⁶)

Single-regressor fit `log g = a + β log L_{1000}(p)` within p ≡ 1 (mod 8):

| window | n | β (f_I) | R² | β·log p | β (f_II) | R² | β·log p |
|---|---|---|---|---|---|---|---|
| [2·10⁴, 4·10⁴] | 473 | −0.60 | 0.56 | 6.2 | −0.46 | 0.42 | 4.7 |
| [2·10⁵, 4·10⁵] | 3938 | −0.49 | 0.57 | 6.2 | −0.35 | 0.34 | 4.4 |
| [2·10⁶, 4·10⁶] | 33579 | −0.42 | 0.54 | 6.3 | −0.30 | 0.31 | 4.5 |

In the other classes mod 8 the dependence is weak (|β| ≤ 0.13 for p ≡ 3, 5; ≈ 0.3 for p ≡ 7 (8), R² < 0.1): those
classes are dominated by covering families. Per-prime profile (p ≡ 1 (8), [10⁶, 4·10⁶], 51143 primes; multiple
regression on χ_p(q), q ≤ 61): q·coef_q for f_I lies in [−0.60, −0.13] for every q ≤ 61 (mean ≈ −0.35; SE of
q·coef ≈ 0.001q), i.e. a genuine 1/q-weighted Euler-product law; f_II is noisier (−0.72 … +0.12, mean ≈ −0.25).
Mean g by square depth s(p) (least odd q with χ_p(q) = −1), p ≡ 1 (8): f_I 0.070 (s=3), 0.060, 0.050, 0.044, 0.040,
0.037, 0.034, 0.033 (s=23), 0.031 (s>23, 124 primes); f_II 0.029 → 0.015 — steady decline, of the size the fitted
β predicts (Σ_{3≤q≤23} 2β/q ≈ 0.6–0.8 in log; observed 0.81 for f_I, 0.66 for f_II).

## 5. Viability Assessment

**COLLAPSES to B1** (local data = CRT conditional mean; Prop A), and the T1 analogy (E2) is spurious (global Jacobi
identity, not a local limit). By-products (EVIDENCE + Assessment, new as far as the campaign files show):
(i) for p ≡ 1 (8), `log(f(p)/log³p)` depends on the Legendre symbols through `−(A/log p)·Σ_q χ_p(q)/q`, a clean
1/q-weighted Euler-product law with A ≈ 6.2 (f_I), 4.5 (f_II), stable over three decades;
(ii) consequence: square-mimicking depresses the conditional mean of f by only a relative O(log log p/log p);
the risk of sterility is entirely in the non-local lottery. CONJECTURE (averaged, not pursued):
`Σ_{p≤N, p≡r (Q)} f(p)` has an asymptotic with an explicit local factor whose log is
`−(A/log N)Σ_{q|Q} χ_r(q)/q + …`.
