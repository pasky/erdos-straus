# BRIDGE_WORLDS — bridging the (h+1)- and (h−1)-worlds (task O211, spark relay Y3)

Status: in progress (O211). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on TORSION_FIRING.md (O207, Thm 3.1 torsion–residue orthogonality), FIXED_MODULUS_SHOTS (Thm 3.1 box),
FF_MUTE ((J)30), FROBENIUS_FIRING ((J)34). Memos `BRAINSTORM/y3_*.md`, scripts `scripts/y3_*`.

Notation. p odd prime; h prime ≡ 3 (mod 4), h ∤ p; k = (h + 1)/4. Type II fires at h iff ∃ c, d, j ≥ 1 with
h = 4cdj − 1 and h | p + 4c²d (⟺ h | pj + c ⟺ −p ≡ c/j mod h, cj | k: the box). Write m = 4cd (so m | h + 1:
h is *semi-primitive* mod m, h ≡ −1). N_II(p) := #{(c, d, h) : 4cd | h + 1, h | p + 4c²d} (all h, prime or not),
N_II^pr(p) the same with h prime.

## 0. Iteration log
(I1) Task (a): semi-primitive (uniform) cyclotomy over F_{h²}. Result: a scaling-collapse proposition (§1) — every
cyclotomic statistic at level m | h + 1 sees p only through F_h^*/F_h^{*e}; the only non-homomorphic bridge is
the additive shift ζ ↦ 1 − ζ, which transports exactly the INTEGER m (cardinality), i.e. the box. Memo
`y3_semiprimitive_collapse`.

## 1. Semi-primitive cyclotomy is p-blind except through the integer m (PROVED)

**Lemma 1.1.** Let h be an odd prime, g a generator of F_{h²}^*, m | h + 1, C_a = g^a⟨g^m⟩. Then F_h^* ⊂ C_0.
*Proof.* F_h^* = ⟨g^{h+1}⟩ and m | h + 1. ∎

**Proposition 1.2 (scaling collapse).** Let F ∈ F_h[x_1..x_n] be weighted-homogeneous: F(λ^{w_1}x_1, …) = λ^e F(x)
for λ ∈ F_h^*. For a ∈ (ℤ/m)^n and u ∈ F_h^* put N_a(u) = #{x ∈ (F_{h²}^*)^n : F(x) = u, x_i ∈ C_{a_i}}. Then
N_a(λ^e u) = N_a(u) for all λ ∈ F_h^*. Hence N_a(p) depends on p only via p mod F_h^{*e}.
*Proof.* x ↦ (λ^{w_i}x_i) is a bijection of the solution sets that preserves each C_{a_i} by Lemma 1.1. ∎
Consequences: (i) shifted cyclotomic numbers #{x ∈ C_a : x + u ∈ C_b} (F = x_2 − x_1, e = 1) are independent of
u ∈ F_h^*; (ii) with e = 2 the only p-information is the Legendre symbol (p/h): the genus layer of Thm 3.1.

**Proposition 1.3 (the additive bridge).** In F_{h²}, ∏_{ζ ∈ μ_c ∖ {1}} (1 − ζ) = c for every c | h + 1. Hence Type
II fires at (c, d, h) iff −p ≡ P(μ_{4cd}) · P(μ_c) (mod h), P(μ) := ∏_{ζ∈μ∖1}(1 − ζ). Pure Gauss sums of order m
equal (−1)^{(h+1)/m} h (Stickelberger; BEW Thm 11.6.3), so g(χ_{4cd}) = (−1)^j h: they carry only the parity of j.
Uniform cyclotomic numbers reduce mod h to integer polynomials in m (EVIDENCE: m²(a,b) ≡ 1, 1 − m, 1 − 3m for m ∈ {4,6,8,10,12,16,20,24}, h ≤ 199).
*Proof.* (X^c − 1)/(X − 1) = ∏(X − ζ) at X = 1. ∎ **Assessment:** the non-homomorphic bridge between the two
worlds that semi-primitivity supplies is cardinality (the integer m read in F_h); it is the box, not new input.

## 2. Classification of bridges between the two worlds (PROVED)

Fix h ≡ 3 (mod 4) prime and m | h + 1, so μ_m ⊂ T(F_h) = ker(N : F_{h²}^* → F_h^*). A "bridge" is a rule that
attaches to μ_m (or to its elements) an element of F_h, where −p lives.

**Theorem 2.1 (three tiers of bridges; scope: the three classes defined below, NOT all conceivable constructions —
R-O211 repair).**
(a) (homomorphic; TORSION_FIRING Thm 3.1) every homomorphism μ_m → F_h^* has image in {±1}.
(b) (symmetric algebraic) if S ∈ ℚ(x_1, …, x_m) is symmetric and defined at μ_m, then S(μ_m ⊂ F_{h²}) ≡ s(m) (mod h)
for the fixed rational number s(m) := S(μ_m ⊂ ℂ), for every h for which S has good reduction at μ_m (h ∤ m and
the denominator of the fixed formula does not vanish mod h). Examples: |μ_c| = c, ∏_{ζ≠1}(1 − ζ) = c,
Σ csc²(πk/c) = (c² − 1)/3 (cot(πk/c) = i(ζ + 1)/(ζ − 1) is rational in ζ). NOT covered by (b): Gauss sums,
cyclotomic numbers and Γ_h-values, which are not rational functions of μ_m; for those the analogous statements are
separate (Stickelberger: g(χ_{4cd}) = (−1)^j h, PROVED, classical; m²(a,b) ≡ 1, 1 − m, 1 − 3m mod h: EVIDENCE,
y3_gauss.py; Gross–Koblitz: the argument 1/m reduces to j, memo y3_gross_koblitz_box).
(c) (Frobenius-invariant algebraic) quantities built from a single ζ ∈ μ_m and fixed by ζ ↦ ζ^h = ζ⁻¹ are values
ρ_𝔥(α), α ∈ K = ℚ(ζ_m)⁺ regular (integral) at 𝔥, at a prime 𝔥 | h (h splits completely in K); here "fixed by
ζ ↦ ζ⁻¹" means the characteristic-zero formula is invariant (invariance only after reduction is not covered). Those
fixed by all of Gal(ℚ(ζ_m)/ℚ) are rational, as in (b).
*Proof.* (a) is Thm 3.1. (b) S is a rational function of the elementary symmetric functions of x_1..x_m; at μ_m these
are the coefficients of X^m − 1 (0 or ±1) both in ℂ and in F_{h²} (h ∤ m). (c) Frob_𝔥 restricted to ℚ(ζ_m) is
ζ ↦ ζ^h = ζ⁻¹ = complex conjugation, trivial on K; reduction from the local ring of K at 𝔥 to O_K/𝔥 = F_h is a ring map. ∎
**Corollary 2.2.** Type II firing on slice (c, d) at h is the case (b) statement −p ≡ s(m) with s = 4c²d (=|μ_{4cd}|·|μ_c|).
Within the three tiers, the only room beyond "the box" is (c) with α ∉ ℚ — which tests p ≡ −α (mod 𝔥), a
*cyclotomic generalisation* of Type II that does not imply ES. Whether every useful bridge must be archimedean is an
Assessment, not a theorem (other constructions — e.g. Gauss sums mixing in characters of F_h^* — are outside the tiers).

## 3. Interpretation: h imitates the infinite place (PROVED dictionary; heuristic reading is Assessment)
h ≡ −1 (mod m) ⟺ Frob_h = c_∞ in Gal(ℚ(ζ_m)/ℚ), i.e. D_h = D_∞ = {1, c_∞}; Thm 3.1's gcd = 2 is |D_∞|. With
M = p + 4c²d: Type II on (c, d) ⟺ a sub-product of the prime factors of M has Artin symbol c_∞ (total symbol σ_p).
On the slices with (ℤ/4cd)^* an elementary 2-group (cd | 6) this is genus theory: failure ⟺ some odd quadratic
character χ mod 4cd has χ(q) = 1 for all q | M (hypothesis gcd(p, 4cd) = 1; checked: y3_span.py, 87 405 slice instances with gcd(M, 4cd) = 1, 86 310 of them at
primes p < 10⁵, 0 mismatches).
FF_MUTE works because its mute place is finite with Frobenius in p's group; over ℚ the place with decomposition group
{±1} is ∞, residue field ℝ — heuristically, the size conditions of B2/B3 are what "imitating ∞" costs (memo
y3_frob_infinity; Assessment).

## 4. Type I: the overlap is p-dependent; full overlap only in the trivial case (PROVED)
Type I (fg = p² + 4c²d, f ≡ g ≡ −p mod 4cd): Frobenius at f acts on μ_{4cd} by ζ ↦ ζ^{−p}; the divisor world is
μ_{f+p}, p's world F_f^*, overlap |Hom(μ_{f+p}, F_f^*)| = gcd(p + 1, f − 1). Full overlap at level 4cd ⟺ 4cd | p + 1
⟹ p ≡ 3 (mod 4) (one-way), where g = 1 (f = p² + 4c²d) is a certificate. For p ≡ 1 (4) partial overlaps exist on
the finitely many slices with gcd(cd, p + 1) > 1 (e.g. (p,c,d,f) = (17,1,3,43): overlap 6) — not exploited. The dual
Hasse window (O207 spark 1) consists of the g ∈ {1, 3, 5} certificates (p ≥ 17; complete proof in the memo), i.e.
for p ≡ 1 (4) of g = 3 with f prime: a sub-family of the greedy x = (p + 3)/4 congruence family (B1); the suggested
CM by ℚ(√−d) occurs in none of the 10 737 window certificates p < 20000 (y3_typeI_hasse.py). Memo
y3_typeI_hasse_window.

## 5. Prime-modulus Type II (O207 spark 2): census and CONJECTURE PM-II (EVIDENCE)
Exhaustive census of all Type II certificates (no range cut on h) via (4cdt − p)j = c + t (scripts/y3_census.c):
mean N_II^pr(p) ≈ (0.27–0.33)·log²p and mean N_II ≈ (0.10–0.12)·log³p for 10³ ≤ p ≤ 10⁸ (dyadic blocks to 2¹⁹, full
[10⁵, 10⁶], samples at 10⁷, 10⁸). Primes with N_II^pr ≤ 1: 13, 193, **3361 (0)**, 76441; min over [10⁵, 10⁶] is 5.
All low cases have p − 1 divisible by many small primes (stacked QRs: by reciprocity no small prime h can fire, since
(pd/h) = −1 is necessary). Adversarial p ≡ 1 (mod 4∏_{q≤29} q) up to 1.3·10¹¹ still have 14–20 prime-firing slices
with cd ≤ 200 (y3_adversarial.py). Odd squares: 0 certificates throughout (T1 control).
**CONJECTURE PM-II.** Every prime p ≥ 5 except p = 3361 has a prime-modulus Type II certificate. (Trivial for
p ≡ 3 mod 4.) It is strictly stronger than Type II-ES, so B2/B3/B6 apply verbatim; no sieve handle (memo
y3_primemod_census).

## 6. Construction iteration on tier (c): unit twists give an FF_MUTE mechanism inside K = ℚ(ζ_m)⁺ (PROVED + Assessment)
Hypothesis of Thm 2.1(b) to violate: "defined over ℚ". In tier (c) the reduction ρ_𝔥 : O_K → F_h is a ring map, so
it maps the unit group E_K (cyclotomic units, rank φ(m)/2 − 1) *homomorphically into F_h^*, the world where p lives*
— exactly FF_MUTE's "⟨s mod f⟩ lives in the same group as p", and not excluded by Thm 3.1 (E_K is not of exponent
dividing h + 1).
**Prop 6.1 (unit-twisted firing; PROVED, elementary).** Put Fire^E(p, h) :⟺ ∃ c, d with 4cd | h + 1 and ε ∈ E_{K_{4cd}}
with 𝔥 | p + 4c²d·ε for some 𝔥 | h. Then Fire^E(p, h) ⟺ −p ∈ ⋃_{(c,d)} 4c²d · ρ_𝔥(E): at fixed h the firing set is a
union of cosets of the subgroup ρ_𝔥(E) ⊂ F_h^* (large for most h under Artin-type heuristics for units, cf. Roskam,
Exp. Math. 2002; EVIDENCE for m = 8, K = ℚ(√2): over the 2399 primes h ≡ 7 (mod 8) below 10⁵ the index
[F_h^* : ⟨ρ_𝔥(1 + √2)⟩] is 1 for 891 and 2 for 909 — scripts/y3_unit_index.py). Taking norms, Fire^E ⟺ h | p² + t·p·X + N(ε)X² (X = 4c²d, t = Tr ε when K is quadratic; for
ε = 1 this is (p + X)², the Type II number squared). ES-firing is the sub-case ρ_𝔥(ε) = 1.
*Proof.* ρ_𝔥 is a ring homomorphism; the norm identity is (p + Xε)(p + Xε′) for K quadratic. ∎
**Assessment.** The unit-twisted variant is an FF_MUTE/ES^{(S)}-type statement inside K (large-coset firing sets,
Chebotarev-countable), and its gap to ES is the condition ε ≡ 1 (mod 𝔥) — a Wieferich/exponent-cap condition, the
same wall as EXPONENT_CAP ((J)34). No transport back to ε = 1 is known; the Galois-invariant (rational) section is
exactly where the archimedean condition sits. Not pursued beyond the index check (spark).

## 7. Barrier table and verdict (O211 checkpoint 1)
| object | bridge tier | what reaches p's world | barrier |
|---|---|---|---|
| Thm 3.1 (O207): torsion, torus, Weil pairing | homomorphic | ±1 (genus layer, = |D_∞|) | B3 (2τ₃ ceiling) |
| pure Gauss sums, uniform cyclotomy (§1) | symmetric algebraic | parity of j; rationals in m | B2 (box) |
| Lucas / Dickson / Cayley / ∏(1 − ζ) (§2) | symmetric algebraic | the integers c, m (box) | B2 |
| Salié angle (memo) | root of ν² ≡ −pd at 1/(2j) | exact Planck-scale hit | H-A / B3 |
| Gross–Koblitz (memo) | Γ_h(1/m) ≡ residue j | box | B2 |
| mixed torus Gauss sums (memo) | genuinely two-world | Weil-bounded character sum | B3 |
| Euclid–Schur forcing (memo) | residue forcing | only |G| = 2 (trivial slice) | B1/B4 |
| tier (c) + units (§6) | ring map O_K → F_h | large subgroup (mute-type) | exponent cap ((J)34) |
| Type I overlap (§4) | gcd(p + 1, f − 1) | trivial case p ≡ 3 (4) | B1 |
**Verdict.** ES is not solved; no infinite case. The bridge question has a precise negative answer for every algebraic
mechanism (Thm 2.1): homomorphic bridges see ±1, Galois-invariant algebraic bridges see fixed rationals (the box), and
the only bridges with large image (units of ℚ(ζ_m)⁺ via tier (c)) produce a mute-type variant separated from ES by an
exponent-cap condition. Semi-primitivity = "Frob_h = Frob_∞" explains why the remaining content is archimedean.
Positive by-products: PM-II (EVIDENCE), the uniform-cyclotomy residue law (EVIDENCE), the 2-group slice genus criterion
(PROVED, folklore-level), refutation of O207 spark 1's CM claim.
