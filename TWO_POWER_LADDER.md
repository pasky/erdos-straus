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

## 3. The ceiling theorem: congruence forcing reaches exactly the quadratic layer, for every m (PROVED)

**Theorem 3.1 (Chebotarev–Schinzel ceiling; PROVED, unconditional).** Fix an odd prime ℓ, m ≥ 3, a modulus M with
ℓ | M, and a class c ∈ (ℤ/M)^×. For primes q ≡ 1 (m), let 𝔮 | q be a prime of K = ℚ(ζ_m) and ψ_𝔮(x) := (x/𝔮)_m (a Dirichlet
character of exact order m mod q; the choice of 𝔮 is the choice of ψ). As q runs over primes ≡ 1 (m), ≡ c (M), with 𝔮 chosen
compatibly (Frobenius in a fixed lift), the value ψ_𝔮(ℓ) is equidistributed on
* μ_m, if m is odd;
* the fibre {ζ ∈ μ_m : ζ^{m/2} = (ℓ/q)} (m/2 values), if m is even;
and (ℓ/q) is itself a function of q mod 4ℓ. In level coordinates (t = 4q·(anything coprime fixed), M ⊇ the forcing modulus ℓ
and any further congruence one wishes to impose on t): **no congruence condition on the level — in particular not the
forcing t ≡ −n⁻¹ (mod ℓ), for any n or any family of n — determines the m-layer of a forced prime beyond its quadratic part.**
*Proof.* Frob_𝔮 in L = K(ℓ^{1/m}) is ψ_𝔮(ℓ) under Kummer (Gal(L/K) ≅ μ_m; [L : K] = m since ℓ is unramified in K and
v_λ(ℓ) = 1 at any λ | ℓ, so ℓ ∉ K^{×p} for p | m). The pair (q mod M, Frob_q|L) is equidistributed in Gal(Lℚ(ζ_M)/ℚ), the fibre
product over F := L ∩ ℚ(ζ_{lcm(M,m)}) (Chebotarev; as in CLASS_FORCING Thm 2.1(b)). F ⊂ L^{ab}. The intermediate fields of the
cyclic Kummer extension L/K are K(ℓ^{1/d}), d | m; K(ℓ^{1/d})/ℚ is abelian iff ℓ^{1−χ(σ)} ∈ K^{×d} for all σ ∈ Gal(K/ℚ)
(χ = cyclotomic character mod d); σ = complex conjugation gives ℓ² ∈ K^{×d}; comparing λ-adic valuations, d | 2 (Schinzel,
*Abelian binomials…*, Acta Arith. 32 (1977), in this special case). Conversely K(√ℓ) ⊂ ℚ(ζ_{4ℓ}) ⊂ ℚ(ζ_{lcm(M,m)}) when m is even
(4 | m). So F = K for m odd, F = K(√ℓ) for m even, and conditioning on q mod M fixes Frob only on F: nothing (m odd) or
ψ_𝔮(ℓ)^{m/2} = (ℓ/q) (m even). ∎
*Scope.* t = 4q with one prime q carrying the order-m character; for composite t the character is a product over the prime
factors of t and the theorem applies factor by factor (each factor's Frobenius is independent of all congruence data). This is
CLASS_FORCING Thm 2.1(c)(i)(ii) / z33_kummer_shadow ((J)93) transported from p-coordinates to level coordinates — the roles of
"fixed datum" and "moving prime" are swapped (there p moves, here the level prime q moves); not new as mathematics.

**Theorem 3.2 (Stickelberger dictionary: what exactly the forcing sees; PROVED for m = 3, 4; identity re-checked numerically for m = 3).**
Let ℓ ≡ 1 (mod m) split as ℓ = ∏_{a∈(ℤ/m)^×} σ_a(λ) in K, with K a PID (m = 3, 4), λ primary, and put
x_a := (σ_aλ/𝔮)_m ∈ μ_m (the Frobenius vector of ℓ at the level prime). Then
* the ES (Dirichlet) datum is the **norm component** D := ψ_𝔮(ℓ) = ∏_a x_a;
* the forcing datum (all m-th power information in q mod ℓ, i.e. in t mod ℓ) is the **Stickelberger component**
  S := (q/λ)_m = ± ∏_a x_a^{a⁻¹} (sign a fixed function of q, ℓ mod 8 for m = 4; no sign for m = 3), and (q/σ_bλ)_m = S^b
  carries nothing more;
* D/S = ± ∏_a x_a^{1−a⁻¹}. The exponents 1 − a⁻¹ generate the ideal gcd(2, m)·ℤ/m (a = 2 for m odd; all even for m even).
Hence D is determined by S exactly modulo μ_m^{gcd(2,m)}: for m odd S says nothing about D; for m = 4, D² = S² (the quadratic
layer, = quadratic reciprocity) and D/S = ±x₃² is a free sign (Burde's correction: x₃ depends on the Gaussian lift of q mod ℓ).
*Proof.* (q/λ)_m = ∏_c (σ_c𝔮/λ)_m (q = ∏σ_c𝔮 up to a unit, which contributes a fixed root of unity absorbed in the sign) =
∏_c (λ/σ_c𝔮)_m·(sign) (cubic reciprocity for primary elements, m = 3; biquadratic reciprocity, m = 4, sign
(−1)^{((Nλ−1)/4)((Nσ_c𝔮−1)/4)}) and (λ/σ_c𝔮)_m = σ_c((σ_c⁻¹λ/𝔮)_m) = x_{c⁻¹}^{c}. Reindex a = c⁻¹. For b: apply σ_b. The
exponent ideal: for m odd, a = 2 is a unit and 1 − 2⁻¹ = 2⁻¹ is a unit; for m even, a odd ⇒ a⁻¹ odd ⇒ 1 − a⁻¹ even, and
a = −1 gives 2. ∎
*Reading.* For m = 2 the two components coincide (K = ℚ, one coordinate): that is the whole reason the BM layer is free
(SPARKS9 Prop 2.2) and the whole reason T1 exists. For m ≥ 3 the level prime's Frobenius vector has φ(m) coordinates; the
forcing measures one Galois-twisted linear form, ES needs the untwisted one. The general-m form of the identity needs Eisenstein
reciprocity (m odd prime) with ideal-theoretic symbols; we only use m = 3, 4, and Thm 3.1 covers all m without it.

Checks (`scripts/z41_stickelberger.py`, `logs/z41_stickelberger.txt`): (q/λ)₃ = x₁x₂² on all 882 pairs ℓ < 60, q < 2000
(primes ≡ 1 mod 3, primary generators): 0 failures. Along forced progressions (q < 2·10⁵) S is constant for each (n, ℓ), while
"ℓ is a cube mod q" occurs at 491/1492, 257/759, 255/741, 174/508 (≈ 1/3) for n = 27, 125, 343, 729 (cubes) and identically
for squares and generic n (9, 25, 7, 131, 241). The m = 4 analogue is §2 (Gaussian-lift functionality, 0 clashes).
