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

## 4. Construction: violate "congruence data on t" — the 2-power layer is CHOOSABLE at one prime, but not forced

Which hypothesis did Thm 3.1 use? That the only information on the level is a congruence. Violate it: choose the level
prime q by its Frobenius in the non-abelian field ℚ(ζ_m, (−ℓ)^{1/m}) (equivalently, by the class of its cyclotomic lift
𝔮 mod ℓ, §2 positive control).

**Proposition 4.1 (PROVED, Chebotarev).** Let n be an odd non-square. (a) There is a prime ℓ ≡ 3 (mod 4) with (n/ℓ) = −1.
(b) For such ℓ and every m = 2^j ≥ 2, the primes q with ℓ | 4qn + 1 and −ℓ ∈ G_{4q}^m (i.e. ψ(−ℓ) = 1 for every character
ψ mod 4q of order dividing m — the BM character included) have positive density. Taking m ≥ 2^{v₂(q−1)}: −ℓ lies in the
odd-order subgroup of G_{4q}; **the whole 2-power ladder at ℓ is satisfied.**
*Proof.* (a) ξ(x) := Jacobi (n/x) on positive odd x coprime to n is a character mod 4n (reciprocity). If ξ(ℓ) = 1 for all primes
ℓ ≡ 3 (4) (ℓ ∤ n), then ξ = 1 on all residues ≡ 3 (4) (Dirichlet), hence on all residues (x ≡ 1 (4) is −1·(−x), and
ξ(−1)·ξ(−x) with both factors ≡ 3 (4) — residues mod 4n), so ξ is principal and n is a square (n odd). (b) −ℓ ≡ 1 (mod 4); the
conditions on q are: q ≡ −(4n)⁻¹ (mod ℓ) and q splits completely in ℚ(ζ_m, (−ℓ)^{1/m}). By Thm 3.1 (with −ℓ in place of ℓ;
same proof) these are compatible iff they agree on ℚ(ζ_m, √−ℓ) ∩ ℚ(ζ_{4ℓ}) = ℚ(i, √−ℓ) (m ≥ 4) resp. ℚ(√−ℓ) (m = 2):
q ≡ 1 (4) and (−ℓ/q) = 1, i.e. (q/ℓ) = 1 — and the forcing gives (q/ℓ) = (−n/ℓ) = (−1/ℓ)(n/ℓ) = 1. ∎
Numerics (`scripts/z41_minus_l.py`, `logs/z41_minus_l.txt`, forced q < 4·10⁵): (n, ℓ) = (13, 7), (7, 11), (101, 7),
(131, 11), (241, 7): m = 2 — all forced q have −ℓ a square (forced layer); m = 4, 8, 16 — fractions 1405/2819, 350/1406,
82/713 (n = 13; the others alike) ≈ 2/m = 1/2, 1/4, 1/8: exactly the Chebotarev density of the extra (chosen) layer.

**Proposition 4.2 (size obstruction — why the ladder at a small prime never reaches the class −1; PROVED, trivial).**
(a) A prime ℓ < t − 1 is never ≡ −1 (mod t); every divisor d ≡ −1 (t) of N has d ≥ t − 1.
(b) If d ≡ −1 (t), d | tn + 1, then t is the least positive residue of −n⁻¹ mod d whenever t < d (always, by (a), unless
d = t − 1), so the pair (d, t) is determined by d: **the ES event at a forced pair has no free parameter left** — it is
"the residue r_d := (−n⁻¹ mod d) divides d + 1 and 4 | r_d" (the ES lottery; heuristic probability ≍ τ(d + 1)/d).
(c) In particular at a 2-group level t = 2^k·F (G_t a 2-group, where "the whole ladder" would mean d ≡ −1 exactly), the event
is a union of congruence classes of n (Lemma 1.1), not a reciprocity consequence.
*Proof.* (a) 1 ≤ ℓ < t − 1. (b) d | tn + 1 ⟺ t ≡ −n⁻¹ (d). (c) Lemma 1.1. ∎
So Prop 4.1 shrinks the lottery FOR THE SMALL PRIME to the odd part of G_t, but the class −1 must be carried by a divisor of
size ≥ t − 1, i.e. by the cofactor (tn + 1)/ℓ, whose prime factors are not touched by any datum of n or of the level
(CLASS_FORCING Thm 5.2 in p-coordinates; Thm 3.1 here). For m odd (the odd part of G_t), Thm 3.2 says the forcing data is
independent of the Dirichlet datum; there is no odd analogue of the BM layer at all.

**What the brief hoped for, and the exact catch ((J)93 screen).** "A forced divisor class at a single level for ALL n" would
be a covering of the non-squares by the classes −a (mod ta − 1) (Lemma 1.1) — B1. Reciprocity cannot produce it because the
only datum it can transport is t mod ℓ (Thm 3.1), and the full class of a divisor needs the non-abelian Frobenius of the level
prime (choosable, Prop 4.1, but then it is a choice of level, i.e. the lottery itself, Prop 4.2(b)).

## 5. 2-group levels do not suffice (EVIDENCE + a PROVED partial obstruction)

`scripts/z41_two_group.py`, `logs/z41_two_group.txt`: T2 = {2^k F : k ≥ 2, F | 3·5·17·257·65537}, 169 levels ≤ 10⁶; words
n = tuv − u − v (u, v ≥ 2) (the (★) line in level form).
* odd non-squares n ≤ 10⁶ with no T2 word: **20 325** (of 499 500); baseline over ALL 4 | t levels: 1 939.
* primes 5 ≤ p ≤ 10⁶ with no T2 word: **1 298** (largest 999 979); of these 1 180 have a (★) word at some 4 | t level
  (baseline all-level (★) failures: 118 primes). Failure rate by decade: 0.217, 0.069, 0.029, 0.0136, and 0.0069 on (10⁶, 10⁷] (`scripts/z41_two_group_1e7.py`: 237 levels, 5 320 failing primes ≤ 10⁷, largest 9 994 727; 0 squares hit) — decreasing, as the
  expected number of T2 hits grows like c·log n, but with infinitely many failures expected (Assessment).
* T1: 0 odd squares have a T2 word (also 0 at all levels). Numerator 8: 131, 241 have no word at any 8 | t level (241 has
  none at any 4 | t level either; 131 has one at t = 4). Every hit is an explicit (t, u, v) with (tu − 1)(tv − 1) = tn + 1.

**Lemma 5.1 (twisted squares kill the levels divisible by the twist; PROVED, elementary).** Let D be odd, n = D·m², and
4D | t. Then D⁻_t(tn + 1) = 0.
*Proof.* For ℓ | tDm² + 1: −tD ≡ m⁻² (mod ℓ), so 1 = (−tD/ℓ) = (−t/D / ℓ) (D² is a square, ℓ ∤ D). Hence
χ_{−t/D}(d) = 1 for every d | N; χ_{−t/D} is a character mod t (4 | t/D) and odd, so χ_{−t/D}(−1) = −1 and no d ≡ −1 (t). ∎
Check (`scripts/z41_twisted_levels.py`): D = 3, 5, 15, 17, m < 200 odd: 0 words at levels 4D | t. So n = F·m² is
obstructed at every T2 level 2^k·F′ with F | F′ — the genus layer of the 2-group levels is a finite family of fixed-conductor
real characters, and each of them has its own "twisted T1". (Only n = m² kills all levels; Prop 2.2 of SPARKS9.)

## 6. Spark 3: can a structured family bias the cubic (odd) layer at the forced primes? (PROVED negative, in scope)

**Corollary 6.1 (no odd-order "T1"; PROVED).** Let 𝒩 be ANY set of odd n (a polynomial family, n = r³, n = D r^k, …), ℓ ≡ 1 (3)
a prime, and t = 4q·w (w fixed) with q ≡ 1 (3) the level prime. Conditional on ℓ | tn + 1 — whatever n ∈ 𝒩 is — the cubic
character of ℓ mod q is equidistributed on μ₃ as q varies over the forced progression (and any further congruence on q).
*Proof.* The only information n gives about q at ℓ is q mod ℓ (ℓ | tn + 1 ⟺ q ≡ −(4wn)⁻¹ (ℓ)); Thm 3.1 with m = 3. ∎
*What a cube DOES force (Thm 3.2).* For n = r³ the forcing gives S = (q/λ)₃ = (−4w/λ)₃⁻¹ — the Stickelberger (anti-cyclotomic)
component x₁x₂² of the Frobenius vector of ℓ, constant along the progression (logged S-values), while the Dirichlet datum
x₁x₂ stays uniform (491/1492 cubes, n = 27; 174/508, n = 729). So a cube biases a cubic HECKE character of ℚ(ω) of conductor
dividing t — not a Dirichlet character mod t, hence invisible to the ES event "d ≡ −1 (t)". For m = 2 the two components
coincide (K = ℚ) and the bias becomes T1. **Squares are the only power family whose forced bias is Dirichlet-visible**; more
precisely the forced part of the m-layer is μ_m/μ_m^{gcd(2,m)} (Thm 3.2).
*Scope.* A disproof family biasing cubic characters at all levels would need control of the non-abelian Frobenius of the
level primes of every level simultaneously — i.e. of the factorisation pattern of every tn + 1 in ℚ(ζ₃, ℓ^{1/3}) — which is
not a property of n mod anything (CLASS_FORCING Thm 5.2 is the p-side version). Not excluded in general (a disproof would be
a non-congruence family), but no algebraic (congruence or power-type) family does it.

## 7. Summary (honest labels)
* **Goal 1 (decisive): spark 1's obstruction is real.** Along the forced progression the quadratic part of a forced prime's
  class is fixed, the 4th/8th/16th-power parts are equidistributed with exactly the Chebotarev fractions 1/2, 1/4, 1/8 (EVIDENCE),
  and Thm 3.1 (PROVED) shows this for every m and every congruence family of levels: Schinzel's abelian criterion caps congruence
  forcing at d | 2. This is (J)93 in level coordinates.
* **Thm 3.2 (PROVED, m = 3, 4): the Stickelberger dictionary.** Forcing reads S = ∏x_a^{a⁻¹}, ES reads D = ∏x_a; they agree
  exactly modulo μ_m^{gcd(2,m)}. The BM layer and T1 are the m = 2 coincidence S = D; there is no odd-order BM layer and no
  odd-order T1 (Cor 6.1: cubes bias only an anti-cyclotomic Hecke character — spark 3 closed for algebraic families).
* **Construction (§4).** Choosing the level prime by its non-abelian Frobenius makes the entire 2-part of ℓ's class choosable
  (Prop 4.1, density 2/m per rung), but a prime < t − 1 is never ≡ −1 (t) and a fixed divisor determines its level (Prop 4.2):
  the class −1 must be carried by an uncontrolled cofactor — the B2 lottery, now localised in the odd part and the cofactor.
* **Goal 3: 2-group levels do not suffice** (EVIDENCE: 1 298 primes ≤ 10⁶, 5 320 ≤ 10⁷ with no word at any 2-group level; rate
  halving per decade); twisted squares Dm² are dead at levels 4D | t (Lemma 5.1, PROVED). Controls: squares 0 hits; 131, 241 no
  8 | t word; every hit an explicit certificate.
* No route. **ES is not solved; no infinite case for primes is claimed.** The ladder above the BM layer is not forced; the
  quadratic layer is the unique reciprocity-free layer, for a structural reason (Thm 3.2).
