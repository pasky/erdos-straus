# AGENT_REPORT_O219 — FF class-divisor machinery over ℤ: explicit sterile Mordell points (STERILE_EXPLICIT.md)

Status: interim checkpoint 1 (work continues on the rigorous certificate, §3). Nothing here proves ES or a case of it.

**SHARP:**
1. **Exact dictionary (PROVED, trivial but useful):** O216's FF Case B tuples (m', g', w, C, v), m'wC = T^s + v, w + C = g'v,
   are literally the ℤ P-data of M17 (4d·a·b = N + e, a + b = c·e, N = r^K) under (m', g', w, C, v) ↔ (4d, c, a, b, e);
   E ↔ f = 4acd − 1, O216 Lemma 1.1(i) ↔ ef = N + 4a²d. Every O216 route has a ℤ twin (STERILE_EXPLICIT Table 2).
2. **Coppersmith interpolation (Cor 1.4, PROVED, elementary via Minkowski):** divisors of n of size n^β in a unit class mod
   n^ρ number ≤ n^{max(0, β(1−β) − ρ) + o(1)}, with explicit lattice constants — by cutting the size window into pieces.
   It removes the τ-loss *below* the Coppersmith threshold, which is exactly where O216 got stuck at q = 27.
3. **With it, the P-count exponent is ET's 2/5 with no divisor-function loss except τ₃ of the single integers (N + e)/4,
   tolerated up to τ₃(m) ≤ C₃(0.3)m^{0.3}** (grid EVIDENCE). ET's own argument tolerates only ≈ 1/18 — that is why (J)26's r₀
   is a tower. The surviving τ-corner is e = N^{o(1)}, a ≈ b ≈ d ≈ N^{1/3}: balanced triple factorisations of N + e.
4. Prototype box sums (non-rigorous) predict an **explicit r₀ ≈ 10⁸–10⁹** for (J)26 Thm 3.1. r = 13, 17 stay out of reach of
   any union bound of this type (M17D §1 quantified why; the prototype's bound/√N ≈ 7·10² near N ≈ 10¹⁵ confirms it).

## Done so far
* §0 iteration log (I1)–(I3); §1 Lemmas 1.1–1.3, Cor 1.4 (proofs written; Cor 1.4 brute-checked, 200 cases, 0 violations);
  §2 route table + continuum exponents (P: 2/5; Q: ≈ 0.65 with no divisor bound).
* Level-1 term (brief): at r = 13 all six non-residue cells are covered at level 1 (POINTWISE_MORDELL §1), so no 13-generic
  sterile point exists at all; at r = 17 two cells survive. For a theorem uniform in r the level-1 term is ≈ 2F(r)/r and is
  harmless for r ≳ 10⁶; it is not what limits r₀ — the constants of the K-tail are.

## Next
§3: fail-closed certificate (C, outward-rounded) of F_P(j) ≥ D_P(N) for N ∈ [2^j, 2^{j+1}), same for Q, plus a normalised
tail for large j; then the explicit r₀.

## Sparks
* Coppersmith interpolation in F_q[T] (O216 §3 end): at q = 27 the binding point is a below-threshold class count — the
  FF version of Cor 1.4 may close r = 3 (q = 27) of O216 directly.
