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
* v3 (self-review, deep reviewer): 7 MAJOR repaired in place (marked ⟨rep⟩): Thm 3.1 hypotheses ℓ ∤ m, 4 | lcm(M, m),
  conjugacy-invariant formulation, the false Schinzel "iff" replaced by a direct one-direction proof; Prop 4.1 needs q ≡ 1 (m)
  and gains the forced case q ≡ 3 (4); the cofactor claim was false; the cubic Hecke conductor is not | t (R283 sharpened: | 3q); scopes narrowed.
* v4 (hostile review R283: no FATAL/MAJOR): minors D1–D13 applied in place, marked "(R283 repair)".

## 1. What "free" can mean

**Lemma 1.1 (fixed level = congruence union; PROVED, trivial).** For fixed t:
{n : D⁻_t(tn + 1) > 0} = ⋃_{a ≥ 1} {n ≡ −a (mod ta − 1)}, and at a prime ℓ | tn + 1 the class ℓ mod t is a function of ℓ alone.
*Proof.* d = ta − 1 | tn + 1 ⟺ ta − 1 | a(tn + 1) − n(ta − 1) = n + a (gcd(a, ta − 1) = 1; conversely multiply n + a by t: t(n + a) = (tn + 1) + (ta − 1)). ∎
So at a fixed level (in particular at the O(log n) "2-group levels" t = 2^k·F, F | 3·5·17·257·65537) there is nothing for
reciprocity to transport: the event is a union of congruence classes of n (B1 / (J)93). (R283 repair, D7: the lemma is for
D⁻_t > 0, a ≥ 1, boundary d = t − 1 included; the ES word event R_t > 0 is the sub-union a ≥ 2 with n + a ≥ 2(ta − 1) —
still a congruence union above a threshold.) Forcing needs the level to MOVE in
the progression t ≡ −n⁻¹ (mod ℓ), and "ψ is free at ℓ" must mean: for a coherent family (t, ψ_t), ψ_t(ℓ) is constant
(or a known function of n) along the progression.

**Definition.** For t = 4q (q prime, q ≡ 1 mod m) put e_m(ℓ, q) := class of ℓ in F_q^×/F_q^{×m} ≅ ℤ/m (canonical up to
the choice of generator; "e = 0", i.e. ℓ is an m-th power mod q, and e mod 2 are choice-free). The m-layer of the class
lottery at level t is the image of the divisor class in G_t/G_t^m.

## 2. Decisive numerics: the forcing stops at the quadratic layer (EVIDENCE)
`scripts/z41_ladder_test.py` (log `logs/z41_ladder_test.txt`): q < 3·10⁵ prime, q ≡ 1 (m), 4q ≡ −n⁻¹ (ℓ).
* e mod 2 is constant on every progression (all 24 rows) — the forced BM/quadratic layer, (−4q/ℓ) = (n/ℓ).
* Given e even, ℓ is a 4th power for 1086/2165, 1053/2151, 3214/6467, 1611/3228 (≈ 1/2), and an 8th power for
  258/1070, 258/1075, 784/3202, 406/1598 (≈ 1/4), the same for every residue n mod ℓ tested (R283 repair, D10: the forcing depends on n only through n mod ℓ, so e.g.
(241, 7) and (101, 7) are the SAME progression, not independent evidence; n = 9 being a square is not special at the
4th-power layer).
* Positive control: [ℓ is a 4th power mod q] is an exact function of (a mod ℓ, b mod ℓ, a mod 8, b mod 8), q = a² + b²,
  π = a + bi primary: 0 clashes in 64–1152 occupied classes for ℓ = 3, 5, 7, 11, 13.
So: forced quadratic layer, free-but-not-forced quartic layer — determined by the Gaussian lift of t, not by t mod ℓ.

## 3. The ceiling theorem: congruence forcing reaches exactly the quadratic layer (PROVED; scope as stated)

**Theorem 3.1 (Kummer–Chebotarev ceiling; PROVED, unconditional; R-self-review repairs marked ⟨rep⟩).** Fix an odd prime ℓ and
m ≥ 3 with **ℓ ∤ m** ⟨rep: without this, e.g. m = 12, ℓ = 3, √3 ∈ ℚ(ζ₁₂) and [L : K] = 6⟩; fix a modulus M with ℓ | M and
**4 | lcm(M, m) if m is even** ⟨rep: for m = 6, M = 7, q mod 4 is free and (ℓ/q) is not fixed⟩, and a class c ∈ (ℤ/M)^× with
c ≡ 1 (mod gcd(M, m)) (else the progression below is empty). Let K = ℚ(ζ_m), L = K(ℓ^{1/m}). For primes q ≡ 1 (m), q ≡ c (M):
* for every e | m, the conjugacy-invariant event "ℓ ∈ F_q^{×e}" has natural density, inside the progression, exactly 1/e if m is
  odd, and exactly 2/e among the q with (ℓ/q) = 1 if m is even and e is even ⟨rep: the earlier "ψ_𝔮(ℓ) equidistributed with 𝔮
  chosen compatibly" was not well defined — Chebotarev distributes conjugacy classes; equivalently, averaged over all pairs (q, 𝔮),
  𝔮 | q, ψ_𝔮(ℓ) := (ℓ/𝔮)_m is equidistributed on μ_m (m odd) resp. on the fibre {ζ : ζ^{m/2} = (ℓ/q)} (m even)⟩;
* (ℓ/q) is a function of q mod 4ℓ, hence of q mod lcm(M, m).
In level coordinates (t = 4q, the forcing t ≡ −n⁻¹ (mod ℓ) being one such congruence, plus any further congruences on q):
**for fixed (n, ℓ) and one varying level prime, the forcing determines the m-layer of ℓ at the level prime only through its
quadratic part** ⟨rep: scope narrowed — this says nothing about joint restrictions on varying prime factors of tn + 1⟩.
*Proof.* [L : K] = m: ℓ is unramified in K (ℓ ∤ m) and v_λ(ℓ) = 1 at each λ | ℓ, so ℓ ∉ K^{×p} for every prime p | m. Frob of a
prime 𝔮 | q (q ≡ 1 (m), degree 1) in Gal(L/K) ≅ μ_m is ψ_𝔮(ℓ); its Gal(L/ℚ)-conjugacy class is the orbit {ψ_𝔮(ℓ)^a}, which fixes
exactly the order of ψ_𝔮(ℓ), i.e. the events "ℓ ∈ F_q^{×e}". Chebotarev in the compositum Lℚ(ζ_{M′}), M′ := lcm(M, m): the pair
(q mod M′, Frob_q|L) is equidistributed in the fibre product Gal(L/ℚ) ×_{Gal(F/ℚ)} Gal(ℚ(ζ_{M′})/ℚ), F := L ∩ ℚ(ζ_{M′}).
F/ℚ is abelian, and F ⊇ K. Intermediate fields of the cyclic L/K are K(ℓ^{1/d}), d | m. *Claim: K(ℓ^{1/d})/ℚ abelian ⟹ d | 2.*
⟨rep: the earlier "iff" criterion (via Schinzel) is false in general — central extensions need not be abelian; only this
direction is used, proved directly:⟩ let α = ℓ^{1/d}, τ ∈ Gal(K(α)/K) with τα = ζ_dα, and σ̃ a lift of complex conjugation, so
σ̃α = ζ′α for some ζ′ ∈ μ_d and σ̃(ζ_d) = ζ_d⁻¹. Then σ̃τ(α) = ζ_d⁻¹ζ′α and τσ̃(α) = ζ′ζ_dα; commutativity forces ζ_d² = 1. ∎(claim)
So F = K (m odd) or F ⊆ K(√ℓ) (m even); and K(√ℓ) ⊆ ℚ(ζ_{4ℓ}, ζ_m) ⊆ ℚ(ζ_{M′}) as ℓ | M and 4 | M′, so F = K(√ℓ) (m even).
Conditioning on q mod M′ (which includes q ≡ 1 (m)) therefore fixes Frob_q|L only through Frob on K(√ℓ), i.e. through (ℓ/q).
Within a fibre the Haar measure on the coset of Gal(L/K(√ℓ)) ≅ μ_{m/2} (m even), resp. on Gal(L/K) ≅ μ_m (m odd), gives the
stated densities (here ℓ ∈ F_q^{×e} ⟺ ψ_𝔮(ℓ)^{m/e} = 1). (R283 repair, D8: for m even and e odd the density is 1/e
unconditionally on (ℓ/q), since μ_{m/e} meets each fibre in the same proportion; reviewer numerics (ℓ, m) = (7, 6), e = 3: 0.334.) ∎
*Scope.* t = 4q with one prime q carrying the order-m character; for composite t the character is a product over the prime
factors of t. (R283 repair, D9: for t = 4q₁q₂ the forcing is the COUPLED condition q₁q₂ ≡ c (mod ℓ), a condition on pairs.
Pair count: for q₁, q₂ ≤ X, split by the class a of q₁ mod ℓ (then q₂ ≡ c/a); for each a, Chebotarev applies to q₁ in its
class and to q₂ in its class separately, giving densities that factor; summing over the φ(ℓ) classes a, the joint
distribution of (ψ₁(ℓ), ψ₂(ℓ)) beyond the quadratic parts is still uniform. Same conclusion; a two-line argument, not "the
same" one.) This is CLASS_FORCING Thm 2.1(c)(i)(ii) / z33_kummer_shadow ((J)93) transported from p-coordinates to level
coordinates — fixed datum and moving prime swapped; not new as mathematics.

**Theorem 3.2 (Stickelberger dictionary: what exactly the forcing sees; PROVED for m = 3, 4; identity re-checked numerically for m = 3).**
Let ℓ ≡ 1 (mod m) split as ℓ = ∏_{a∈(ℤ/m)^×} σ_a(λ) in K, with K a PID (m = 3, 4), λ primary, and put
x_a := (σ_aλ/𝔮)_m ∈ μ_m (the Frobenius vector of ℓ at the level prime; (R283 repair, D2) the x_a depend on the primary
normalisation of the element λ — λ ↦ uλ multiplies ∏x_a^{a⁻¹} by (uū²/𝔮)₃ resp. (u²/𝔮)₄ — while S and D do not). Then
* the ES (Dirichlet) datum is the **norm component** D := ψ_𝔮(ℓ) = ∏_a x_a;
* the forcing datum (all m-th power information in q mod ℓ, i.e. in t mod ℓ) is the **Stickelberger component**
  S := (q/λ)_m = ∏_a x_a^{a⁻¹} (exactly, no sign, for m = 3 and m = 4 ⟨rep: for m = 4 the two biquadratic reciprocity signs
  cancel; reviewer re-checked 1 892 quartic pairs < 500, 0 failures⟩), and (q/σ_bλ)_m = S^b
  carries nothing more;
* D/S = ∏_a x_a^{1−a⁻¹}. For m = 3 the exponents (0, 1 − 2⁻¹ = 2) generate ℤ/3; for m = 4 they are (0, 2), generating 2ℤ/4.
Hence (m = 3, 4 only; R283 repair, D1) D is determined by S exactly modulo μ_m^{gcd(2,m)}: for m = 3, D/S = x₂⁻¹ is free and S
says nothing about D; for m = 4, D² = S² (the quadratic
layer, = quadratic reciprocity) and D/S = x₃² is a free sign (Burde's correction: x₃ depends on the Gaussian lift of q mod ℓ).
*Proof.* With π a primary generator of 𝔮, q = ∏_c σ_c(π) exactly (for m = 3: ππ̄ = q; m = 4: ππ̄ = q), so (q/λ)_m = ∏_c (σ_cπ/λ)_m =
∏_c (λ/σ_cπ)_m (cubic reciprocity for primary elements, m = 3; biquadratic reciprocity, m = 4, whose sign
(−1)^{((Nλ−1)/4)((q−1)/4)} is the same for c = 1, 3 and cancels in the product) and (λ/σ_c𝔮)_m = σ_c((σ_c⁻¹λ/𝔮)_m) = x_{c⁻¹}^{c}. Reindex a = c⁻¹. For b: apply σ_b. The
exponent ideal: m = 3: a = 2, 1 − 2⁻¹ = −1 is a unit; m = 4: a = 3, 1 − 3⁻¹ = −2. *Realisability* ⟨rep⟩: the σ_aλ are distinct primes, hence multiplicatively independent modulo K^{×m},
so [K((σ_aλ)^{1/m} : a) : K] = m^{φ(m)} and by Chebotarev every vector (x_a) ∈ μ_m^{φ(m)} occurs for a positive density of
degree-1 primes 𝔮; inside a progression q mod ℓ all vectors with the prescribed S occur. (R283 repair, D3: for cyclic H = Gal(K/ℚ) (m = 3, 4),
K(β^{1/m})/ℚ is abelian IFF σ_cβ ≡ β^c (mod K^{×m}) for all c — necessity by the commutator argument of Thm 3.1, sufficiency
because the extension is then central with cyclic quotient H, hence abelian. Writing β = ∏(σ_aλ)^{i_a} (B = ⟨σ_aλ⟩ is free over
ℤ/m by valuations) the condition is i_{c⁻¹a} ≡ c·i_a, i.e. i_a = a⁻¹i₁: the maximal abelian-over-ℚ subfield is K(β₀^{1/m}),
β₀ = ∏(σ_aλ)^{a⁻¹}, whose Frobenius at 𝔮 is exactly S; Chebotarev then gives every vector with prescribed S equal density.) "S determines D exactly modulo μ_m^{gcd(2,m)}" is sharp. ∎
*Reading (Assessment, not part of the PROVED statement; R283 repair, D4).* For m = 2 the two components coincide (K = ℚ, one coordinate): in our reading that is the whole reason the BM layer is free
(SPARKS9 Prop 2.2) and the whole reason T1 exists. For m ≥ 3 the level prime's Frobenius vector has φ(m) coordinates; the
forcing measures one Galois-twisted linear form, ES needs the untwisted one. The general-m form of the identity needs Eisenstein
reciprocity (m odd prime) with ideal-theoretic symbols and is NOT proved here; for general odd m only the conjugacy-invariant
consequence (Thm 3.1: congruence data on q says nothing about ℓ's m-layer) is available.

Checks (`scripts/z41_stickelberger.py`, `logs/z41_stickelberger.txt`): (q/λ)₃ = x₁x₂² on all 882 pairs ℓ < 60, q < 2000
(primes ≡ 1 mod 3, primary generators): 0 failures. Along forced progressions (q < 2·10⁵) S is constant for each (n, ℓ) (R283 repair, D12: automatic for EVERY n — S is a function of
q mod ℓ, which the forcing fixes — so this constancy is not evidence of anything cube-specific), while
"ℓ is a cube mod q" occurs at 491/1492 (n = 27 and 125, ℓ = 7), 257/759 (343, ℓ = 13), 255/741 (27, ℓ = 13), 174/508 (729, ℓ = 19) (≈ 1/3; cubes) and identically
for squares and generic n (9, 25, 7, 131, 241). The m = 4 analogue is §2 (Gaussian-lift functionality, 0 clashes).

## 4. Construction: violate "congruence data on t" — the 2-power layer is CHOOSABLE at one prime, but not forced

Which hypothesis did Thm 3.1 use? That the only information on the level is a congruence. Violate it: choose the level
prime q by its Frobenius in the non-abelian field ℚ(ζ_m, (−ℓ)^{1/m}) (equivalently, by the class of its cyclotomic lift
𝔮 mod ℓ, §2 positive control).

**Proposition 4.1 (PROVED, Chebotarev).** Let n be an odd non-square. (a) There is a prime ℓ ≡ 3 (mod 4) with (n/ℓ) = −1.
(b) For such ℓ and every m = 2^j ≥ 2, the primes q ≡ 1 (mod m) with ℓ | 4qn + 1 and −ℓ ∈ G_{4q}^m (i.e. ψ(−ℓ) = 1 for every
character ψ mod 4q of order dividing m — the BM character included) have positive density; inside the forced progression
∩ {q ≡ 1 (m)} their relative density is 2/m ⟨rep: the condition q ≡ 1 (m) is essential — over ALL forced q the fractions are
0.748, 0.686, 0.670 for m = 4, 8, 16 (reviewer rerun, (13, 7)), since for q ≢ 1 (m) the m-th powers are a larger subgroup⟩.
(b′) ⟨rep: the "take m ≥ 2^{v₂(q−1)} afterwards" step was not justified as stated; fixed by adding q ≡ 1 + 2^j (mod 2^{j+1})⟩
For every j ≥ 1, the primes q with v₂(q − 1) = j exactly, ℓ | 4qn + 1 and −ℓ in the odd-order subgroup of G_{4q} have positive
density (relative density 2^{1−j} among forced q with v₂(q − 1) = j): **the whole 2-part of the class of −ℓ is trivial.**
(c) ⟨rep, reviewer's observation⟩ For j = 1 (q ≡ 3 mod 4) this is FORCED, not chosen: every forced q ≡ 3 (4) has −ℓ in the
odd-order subgroup of G_{4q} (the 2-Sylow of G_{4q} is then (ℤ/2)², its characters are χ_{−4} and χ_{−4q} = χ_{−t}, settled by
ℓ ≡ 3 (4) and by the BM forcing (−t/ℓ) = (n/ℓ) = −1).
*Proof.* (a) ξ(x) := Jacobi (n/x) on positive odd x coprime to n is a character mod 4n (reciprocity). If ξ(ℓ) = 1 for all primes
ℓ ≡ 3 (4) (ℓ ∤ n), then ξ = 1 on all residues ≡ 3 (4) (Dirichlet), hence on all residues (x ≡ 1 (4) is −1·(−x), and
ξ(−1)·ξ(−x) with both factors ≡ 3 (4) — residues mod 4n), so ξ is principal and n is a square (n odd). (b) −ℓ ≡ 1 (mod 4); the
conditions on q are: q ≡ −(4n)⁻¹ (mod ℓ) and q splits completely in ℚ(ζ_m, (−ℓ)^{1/m}). By Thm 3.1 (with −ℓ in place of ℓ;
same proof) these are compatible iff they agree on ℚ(ζ_m, √−ℓ) ∩ ℚ(ζ_{4ℓ}) = ℚ(i, √−ℓ) (m ≥ 4) resp. ℚ(√−ℓ) (m = 2):
q ≡ 1 (4) and (−ℓ/q) = 1, i.e. (q/ℓ) = 1 — and the forcing gives (q/ℓ) = (−n/ℓ) = (−1/ℓ)(n/ℓ) = 1. Chebotarev; the ℓ ∤ m
hypothesis of Thm 3.1 holds (ℓ odd, m = 2^j). (b′) For j ≥ 2: same, with the additional abelian condition q ≡ 1 + 2^j (2^{j+1}) and
m = 2^j: then F_q^{×m} is the odd-order subgroup. (R283 repair, D11: Thm 3.1 needs m ≥ 3; the case j = 1 is (c).) (c) For q ≡ 3 (4): (−ℓ/q) = −(ℓ/q) = (q/ℓ) (ℓ, q ≡ 3 (4)) = (−n/ℓ) = 1, and
−ℓ ≡ 1 (4). ∎
Numerics (`scripts/z41_minus_l.py`, `logs/z41_minus_l.txt`, forced q < 4·10⁵): (n, ℓ) = (13, 7), (7, 11), (101, 7),
(131, 11), (241, 7): m = 2 — all forced q have −ℓ a square (forced layer); m = 4, 8, 16 — fractions 1405/2819, 350/1406,
82/713 (n = 13; the others alike; (241, 7) is the same progression as (101, 7) — identical rows, not independent, R283 D10) ≈ 2/m = 1/2, 1/4, 1/8: exactly the Chebotarev density of the extra (chosen) layer.

**Proposition 4.2 (size obstruction — why the ladder at a small prime never reaches the class −1; PROVED, trivial).**
(a) A prime ℓ < t − 1 is never ≡ −1 (mod t); every divisor d ≡ −1 (t) of N has d ≥ t − 1.
(b) If d ≡ −1 (t), d | tn + 1, then t is the least positive residue of −n⁻¹ mod d whenever t < d (always, by (a), except the
boundary divisor d = t − 1, which β_t removes from R_t anyway), so the pair (d, t) is determined by d: **the ES event at a forced pair has no free parameter left** — it is
"the residue r_d := (−n⁻¹ mod d) divides d + 1 and 4 | r_d" (the ES lottery; heuristic probability ≍ τ(d + 1)/d).
(c) In particular at a 2-group level t = 2^k·F (F a product of known Fermat primes; G_t a 2-group, where "the whole ladder" would mean d ≡ −1 exactly), the event
is a union of congruence classes of n (Lemma 1.1), not a reciprocity consequence.
*Proof.* (a) 1 ≤ ℓ < t − 1. (b) d | tn + 1 ⟺ t ≡ −n⁻¹ (d). (c) Lemma 1.1. ∎
So Prop 4.1 shrinks the lottery FOR THE SMALL PRIME to the odd part of G_t — and at q ≡ 3 (4) it does so for free (4.1(c)):
**the brief's "lottery shrinks to the odd part" holds, trivially, at every level 4q, q ≡ 3 (4)** — but that odd part is
(q − 1)/2 classes, i.e. almost everything. The class −1 must be carried by a divisor of size ≥ t − 1. ⟨rep: the earlier "i.e. by
the cofactor (tn + 1)/ℓ" was false: N ≡ 1 (t) gives [N/ℓ] = [ℓ]⁻¹ ≠ −1 too.⟩ Such a divisor combines ℓ with SOME other prime
factors, or avoids ℓ; the total class of the cofactor is constrained by ℓ ([N/ℓ] = [ℓ]⁻¹), but the classes of its individual
prime factors are not determined by any datum of n or of the level (CLASS_FORCING Thm 5.2 in p-coordinates; Thm 3.1 here for
fixed small primes only — Chebotarev with fixed ℓ says nothing about the varying large factors). For m odd (the odd part of G_t), Thm 3.2 says the forcing data is
independent of the Dirichlet datum; there is no odd analogue of the BM layer at all.

**What the brief hoped for, and the exact catch ((J)93 screen).** "A forced divisor class at a single level for ALL n" would
be a covering of the non-squares by the classes −a (mod ta − 1) (Lemma 1.1) — B1. Reciprocity cannot produce it because the
only datum it can transport is t mod ℓ (Thm 3.1), and the full class of a divisor needs the non-abelian Frobenius of the level
prime (choosable, Prop 4.1, but then it is a choice of level, i.e. the lottery itself, Prop 4.2(b)).

## 5. 2-group levels do not suffice (EVIDENCE + a PROVED partial obstruction)

`scripts/z41_two_group.py`, `logs/z41_two_group.txt`: T2 = {2^k F : k ≥ 2, F | 3·5·17·257·65537}, 169 levels ≤ 10⁶; words
n = tuv − u − v (u, v ≥ 2) (the (★) line in level form).
* odd non-squares 3 ≤ n ≤ 10⁶ with no T2 word: **20 325** (of 499 500 odd non-squares; R283 D6: the prime census below starts at
  p = 5, and 3 has no T2 word either); baseline over ALL 4 | t levels: 1 939.
* primes 5 ≤ p ≤ 10⁶ with no T2 word: **1 298** (largest 999 979); of these 1 180 have a (★) word at some 4 | t level
  (baseline all-level (★) failures: 118 primes). Failure rate by decade: 0.217, 0.069, 0.029, 0.0136, and 0.0069 on (10⁶, 10⁷] (`scripts/z41_two_group_1e7.py`: 237 levels, 5 320 failing primes ≤ 10⁷, largest 9 994 727; 0 squares hit) — decreasing, as the
  expected number of T2 hits grows like c·log n, but with infinitely many failures expected (Assessment).
* T1: 0 odd squares have a T2 word (also 0 at all levels). Numerator 8: 131, 241 have no word at any 8 | t level (241 has
  none at any 4 | t level either; 131 has one at t = 4). Every hit is generated as n = (tu − 1)v − u, i.e. it IS the certificate (tu − 1)(tv − 1) = tn + 1 (no separate re-verification pass; the identity is algebraic).

**Lemma 5.1 (twisted squares kill the levels divisible by the twist; PROVED, elementary).** Let D be odd, n = D·m², and
4D | t. Then D⁻_t(tn + 1) = 0.
*Proof.* For ℓ | tDm² + 1: −tD ≡ m⁻² (mod ℓ), so 1 = (−tD/ℓ) = (−t/D / ℓ) (D² is a square, ℓ ∤ D). Hence
χ_{−t/D}(d) = 1 for every d | N; χ_{−t/D} is a character mod t (4 | t/D) and odd, so χ_{−t/D}(−1) = −1 and no d ≡ −1 (t). ∎
Check (`scripts/z41_twisted_levels.py`): D = 3, 5, 15, 17, m < 200 odd: 0 words at levels 4D | t. So n = F·m² is
obstructed at every T2 level 2^k·F′ with F | F′ — the genus layer of the 2-group levels is a finite family of fixed-conductor
real characters, and each of them has its own "twisted T1". (By this BL-character mechanism only n = m² kills all levels,
SPARKS9 Prop 2.2; non-squares failing all levels exist, but for other reasons — the class layer.)

## 6. Spark 3: can a structured family bias the cubic (odd) layer at the forced primes? (PROVED negative, in scope)

**Corollary 6.1 (no odd-order "T1"; PROVED).** Let 𝒩 be ANY set of odd n (a polynomial family, n = r³, n = D r^k, …), ℓ ≡ 1 (3)
a prime, and t = 4q·w (w fixed) with q ≡ 1 (3) the level prime. Conditional on ℓ | tn + 1 — whatever n ∈ 𝒩 is — the cubic
character of ℓ mod q is equidistributed on μ₃ as q varies over the forced progression (and any further congruence on q).
*Proof.* The only information n gives about q at ℓ is q mod ℓ (ℓ | tn + 1 ⟺ q ≡ −(4wn)⁻¹ (ℓ)); Thm 3.1 with m = 3. ∎
*What a cube DOES force (Thm 3.2).* For n = r³ the forcing gives S = (q/λ)₃ = (−4w/λ)₃⁻¹ — the Stickelberger (anti-cyclotomic)
component x₁x₂² of the Frobenius vector of ℓ. (R283 repair, D12: constancy of S along a progression holds for every n; what
cubes add is that the pinned value (−4w/λ)₃⁻¹ does not depend on r. At w = 2 (t = 8q; −8 = (−2)³) **S = 1 at every forced split
ℓ, for every cube n — the literal cubic analogue of T1**, while the Dirichlet datum D = x₁x₂ stays uniform (491/1492 cubes,
n = 27; 174/508, n = 729; reviewer's w = 2 rows likewise).) So a cube biases a cubic HECKE character of ℚ(ω),
α ↦ (q/α)₃, of conductor dividing 3q (R283 repair, D13: sharper than the earlier "9t"; by cubic reciprocity α ≡ 1 (3) is primary
up to the cube −1; checked trivial on all primes α ≡ 1 (3q) for q = 7, 13, 19, 31, and NOT of conductor dividing q in general —
e.g. q = 7, α = 1 + 28ω, N(α) = 757, (7/(α))₃ ≠ 1 — except q = 19 ≡ 1 (9), where the conductor is q) — not a Dirichlet character mod t, hence invisible to the ES event "d ≡ −1 (t)". For m = 2 the two components
coincide (K = ℚ) and the bias becomes T1. **Squares are the only power family whose forced bias is Dirichlet-visible**; more
precisely the forced part of the m-layer is μ_m/μ_m^{gcd(2,m)} (Thm 3.2).
*Scope (⟨rep: narrowed⟩).* Cor 6.1 excludes cubic bias transported by the forcing congruence, for fixed (n, ℓ) and a varying
level prime. It does NOT exclude joint restrictions on the varying prime factors of tn + 1, correlated composite-level
families, or other algebraic constructions (Chebotarev with fixed ℓ cannot be applied to the varying factors). So spark 3 is
closed only in the form "no family of n biases the cubic Dirichlet layer through the forcing congruence".

## 7. Summary (honest labels)
* **Goal 1 (decisive): spark 1's obstruction is real.** Along the forced progression the quadratic part of a forced prime's
  class is fixed, the 4th/8th/16th-power parts are equidistributed with exactly the Chebotarev fractions 1/2, 1/4, 1/8 (EVIDENCE),
  and Thm 3.1 (PROVED) shows this for every m with ℓ ∤ m and every congruence family of one varying level prime: a
  commutator argument (K(ℓ^{1/d})/ℚ abelian ⟹ d | 2) caps congruence forcing at the quadratic layer. This is (J)93 in level coordinates.
* **Thm 3.2 (PROVED, m = 3, 4): the Stickelberger dictionary.** Forcing reads S = ∏x_a^{a⁻¹}, ES reads D = ∏x_a; they agree
  exactly modulo μ_m^{gcd(2,m)} (proved for m = 3, 4 only; R283 D1). The BM layer and T1 are the m = 2 coincidence S = D; there is no odd-order BM layer and no
  odd-order T1 transported by the forcing (Cor 6.1: cubes bias only an anti-cyclotomic Hecke character; spark 3 closed in
  that narrow form only).
* **Construction (§4).** Choosing the level prime by its non-abelian Frobenius makes the entire 2-part of ℓ's class choosable
  (Prop 4.1, relative density 2/m per rung among q ≡ 1 (m)); at q ≡ 3 (4) it is even forced (4.1(c)) — the brief's "shrink to
  the odd part" holds trivially there, and the odd part is (q − 1)/2 classes. A prime < t − 1 is never ≡ −1 (t) and a fixed
  divisor determines its level (Prop 4.2): the class −1 needs a divisor ≥ t − 1 built from prime factors whose individual
  classes nothing controls — the B2 lottery, now localised in the odd part.
* **Goal 3: 2-group levels do not suffice** (EVIDENCE: 1 298 primes ≤ 10⁶, 5 320 ≤ 10⁷ with no word at any 2-group level; decade
  ratios ÷3.2, ÷2.3, ÷2.2, ÷2.0 — roughly halving in the last decades (R283 D5); "infinitely many failures" is Assessment); twisted squares Dm² are dead at levels 4D | t (Lemma 5.1, PROVED). Controls: squares 0 hits; 131, 241 no
  8 | t word; every hit an explicit certificate.
* No route. **ES is not solved; no infinite case for primes is claimed.** The ladder above the BM layer is not forced; the
  quadratic layer is the unique reciprocity-free layer, for a structural reason (Thm 3.2).
