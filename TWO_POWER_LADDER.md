# TWO_POWER_LADDER — climbing the 2-power ladder above the BM layer (task O272; relay of O271 SHARP 1 + sparks 1, 3)

Setting (SYNTHESIS_SPARKS9 §2, METAPLECTIC_ES Thm K). n odd, t ≡ 0 (mod 4), N = tn + 1, G_t = (ℤ/t)^×.
ES words of level t: n = tuv − u − v (u, v ≥ 2) ⟺ (tu − 1)(tv − 1) = N; R_t(n) = D⁻_t(N) − β_t(n),
D⁻_t(N) = #{d | N : d ≡ −1 (t)}. Forcing (Prop 2.2 of SPARKS9): ℓ | N ⟺ t ≡ −n⁻¹ (mod ℓ); then (−t/ℓ) = (n/ℓ).
**ES is not solved; nothing below proves an infinite case for primes.**

## 0. Iteration log
* v0: literal question "is ψ(ℓ) a function of n mod ℓ at a fixed level t" is vacuous: at fixed t, ℓ | tn + 1 fixes
  n ≡ −t⁻¹ (mod ℓ). The meaningful question is along the forced progression t ≡ −n⁻¹ (ℓ) with a COHERENT family of
  characters ψ_t (Lemma 1.1).
* v1 (decisive numerics, §2): along t = 4q, q ≡ 1 (mod m), the quadratic part is forced, the quartic/octic parts are
  equidistributed (≈ 1/2, 1/4). Spark 1's predicted obstruction is confirmed.
* v2 (construction: which hypothesis did the obstruction use?): "data = congruence data on t". Violate it: let t carry a
  Gaussian (cyclotomic) lift. Then the m-layer at ℓ is an exact function of the lift mod ℓ (0 clashes) — choosable, not
  forced (§4).

## 1. What "free" can mean

**Lemma 1.1 (fixed level = congruence union; PROVED, trivial).** For fixed t:
{n : D⁻_t(tn + 1) > 0} = ⋃_{a ≥ 1} {n ≡ −a (mod ta − 1)}, and at a prime ℓ | tn + 1 the class ℓ mod t is a function of ℓ alone.
*Proof.* d = ta − 1 | tn + 1 ⟺ ta − 1 | tn + 1 − n(ta − 1) = 1 + na ⟺ ta − 1 | n + a (multiply by t, gcd(t, ta − 1) = 1). ∎
So at a fixed level (in particular at the O(log n) "2-group levels" t = 2^k·F, F | 3·5·17·257·65537) there is nothing for
reciprocity to transport: the event is a union of congruence classes of n (B1 / (J)93). Forcing needs the level to MOVE in
the progression t ≡ −n⁻¹ (mod ℓ), and "ψ is free at ℓ" must mean: for a coherent family (t, ψ_t), ψ_t(ℓ) is constant
(or a known function of n) along the progression.

**Definition.** For t = 4q (q prime, q ≡ 1 mod m) put e_m(ℓ, q) := class of ℓ in F_q^×/F_q^{×m} ≅ ℤ/m (canonical up to
the choice of generator; "e = 0", i.e. ℓ is an m-th power mod q, and e mod 2 are choice-free). The m-layer of the class
lottery at level t is the image of the divisor class in G_t/G_t^m.

## 2. Decisive numerics: the forcing stops at the quadratic layer (EVIDENCE)
`scripts/z41_ladder_test.py` (log `logs/z41_ladder_test.txt`): q < 3·10⁵ prime, q ≡ 1 (m), 4q ≡ −n⁻¹ (ℓ).
* e mod 2 is constant on every progression (all 24 rows) — the forced BM/quadratic layer, (−4q/ℓ) = (n/ℓ).
* Given e even, ℓ is a 4th power for 1086/2165, 1053/2151, 3214/6467, 1611/3228 (≈ 1/2), and an 8th power for
  258/1070, 258/1075, 784/3202, 406/1598 (≈ 1/4), uniformly in n (including n = 9, a square, and n = 131, 241).
* Positive control: [ℓ is a 4th power mod q] is an exact function of (a mod ℓ, b mod ℓ, a mod 8, b mod 8), q = a² + b²,
  π = a + bi primary: 0 clashes in 64–1152 occupied classes for ℓ = 3, 5, 7, 11, 13.
So: forced quadratic layer, free-but-not-forced quartic layer — determined by the Gaussian lift of t, not by t mod ℓ.
