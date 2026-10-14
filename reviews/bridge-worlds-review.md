# R216 — hostile review of O211 (BRIDGE_WORLDS.md + BRAINSTORM/y3_*.md)

Reviewer: R216 (side agent). Branch `side-agent/review-bridge-worlds`, merged `side-agent/bridge-worlds` at 7714153a.
**ES is not solved; nothing in O211 claims otherwise, and nothing here changes that.**
From-scratch scripts: `scripts/review_r216_*.{c,py}` (none of the author's `scripts/y3_*` were reused).

## Summary verdicts
(filled in progressively; see sections below)

## Checks, claim by claim

### C1. §1 Lemma 1.1 / Prop 1.2 / Prop 1.3 (scaling collapse, additive bridge) — SOUND (one label understated)
Re-derived. Lemma 1.1: F_h^* = ⟨g^{h+1}⟩ ⊂ ⟨g^m⟩ since m | h + 1. Prop 1.2: x ↦ (λ^{w_i}x_i) preserves each C_{a_i}
(λ^{w_i} ∈ F_h^* ⊂ C_0) and maps F = u to F = λ^e u. Prop 1.3: Φ-free identity (X^c − 1)/(X − 1) at X = 1; then
4cd·c = 4c²d. Stickelberger (BEW Thm 11.6.3 — book not accessible here; statement as recalled: h^t ≡ −1 (mod m),
t minimal, q = h^{2tγ}, g(χ) = (−1)^{γ−1+γ(h^t+1)/m}√q) gives (−1)^j h with t = γ = 1, m = 4cd.
From scratch (`scripts/review_r216_gauss.py 60`, F_{h²} = F_h[i], all h ≡ 3 (4) in [7, 59], all m | h + 1, m ≥ 3):
g(χ) = (−1)^{(h+1)/m} h, ∏_{μ_c∖1}(1 − ζ) = c, and the u-independence of #{x ∈ C_a : x + u ∈ C_b} (u ∈ F_h^*):
0 failures.
**The uniform-cyclotomy residue law is PROVED, not EVIDENCE (two lines; this also settles the report's spark 2).**
With (a,b) = #{x ∈ C_a : 1 + x ∈ C_b} and J'(χ^s, χ^t) = Σ_{x ≠ 0, −1} χ^s(x)χ^t(1 + x),
m²(a,b) = Σ_{s,t mod m} ζ_m^{−as−bt} J'(χ^s, χ^t). Here J'(1,1) = q − 2, J'(χ^s,1) = J'(1,χ^s) = J'(χ^s,χ^{−s}) = −1
(s ≢ 0; uses χ(−1) = 1, true as −1 ∈ F_h^* ⊂ C_0), and for s, t, s + t ≢ 0 the Jacobi sum is g(χ^s)g(χ^t)/g(χ^{s+t})
up to a sign χ^s(−1) = 1, i.e. ±h, since every nontrivial character of order | h + 1 has a pure Gauss sum ±h. With
q = h² ≡ 0: **m²(a,b) ≡ 1 − m(δ_{a,0} + δ_{b,0} + δ_{a,b}) (mod h)**, i.e. 1 − 3m at (0,0), 1 − m when exactly one of
a = 0, b = 0, a = b holds, and 1 otherwise. My script confirms this exact *pattern* (not just the value set) for every
(a,b), m | h + 1, m ≥ 3, h ≤ 59: (0,0)/(0,i)/(i,0)/(i,i)/other = 1 − 3m / 1 − m / 1, 0 exceptions.

### C2. Thm 2.1 (three tiers) and Cor 2.2 — SOUND-AFTER-REPAIRS (minor; the statements are correct but near-tautological)
(a) Hom(ℤ/m, ℤ/(h − 1)) has order gcd(m, h − 1) | gcd(h + 1, h − 1) = 2. Correct.
(b) Correct over ℂ: a symmetric S regular at the point μ_m (some ordering) is regular on the whole S_m-orbit, hence
(invariants of the semilocal ring of a finite quotient) S = A(e)/B(e) with A, B ∈ ℚ[e_1..e_m], B(e(μ_m)) ≠ 0. At μ_m the
e_i are the coefficients of X^m − 1 in ℂ and in F_{h²}, so S(μ_m mod h) ≡ A(ē)/B(ē) = s(m) mod h provided B(ē) ≢ 0
(mod h) and A, B have h-integral coefficients. The author's proof ("S is a rational function of the e_i") skips the
regularity step, and the "good reduction" hypothesis is stated for "the fixed formula" — it must refer to an
A(e)/B(e) representation (a representation P(x)/Q(x) with Q(μ̄_m) ≠ 0 but B(ē) ≡ 0 gives a value that need not be
the residue of s(m), which then has h in its denominator).
Two of the listed examples are not instances of (b) as defined: |μ_c| = c is not a rational function of the
coordinates at all, and ∏_{ζ≠1}(1 − ζ) and Σ csc²(πk/c) are symmetric in μ_c ∖ {1}, not in μ_m (the factor ζ = 1
would vanish). Both are covered by the obvious generalisation "symmetric functions of the roots of a fixed monic
F ∈ ℤ[X] (here (X^c − 1)/(X − 1)) with unit leading coefficient", whose proof is identical. → m1.
(c) Correct: Frob_𝔓|ℚ(ζ_m) = (ζ ↦ ζ^h) = c_∞ (h ≡ −1 mod m), trivial on K = ℚ(ζ_m)⁺; h splits completely in K; a
fixed f ∈ ℚ(X) with f(ζ) = f(ζ^{−1}) in characteristic 0 has f(ζ) ∈ K and its reduction at the place 𝔓 picked out by
ζ ↦ ζ̄ is ρ_𝔥(f(ζ)) if f(ζ) is 𝔥-integral. The quantifier that carries all the content is that **f is fixed
independently of h** (and of p). Without it tier (c) is vacuous: the prime field of F_{h²} is F_h, so every element of
F_h is "built from μ_m by field operations" (e.g. 1 + … + 1). The memo y3_lucas_dickson_trace (Prop G) states this
("independent of h once the characteristic-zero formula is fixed"), but Thm 2.1(c) as written in BRIDGE_WORLDS does
not. → m2. Note also that "a single ζ" is no restriction (μ_m = ⟨ζ⟩).
Cor 2.2: Type II at (c,d,h) ⟺ h | p + 4c²d ⟺ −p ≡ 4c²d ≡ c/j (j·4cd = h + 1). Correct; the author correctly notes
rationality ≠ box membership (3 ∉ {1,2,4} at h = 7: Box(2) = {c/j : cj | 2} = {1, 2, 1/2 = 4} ✓).
Scope/labels: "every useful bridge is archimedean" is labelled Assessment in §2, §7 and the report — correct. But the
§2 heading "Classification of bridges between the two worlds (PROVED)" still reads as a classification; what is proved
is three elementary facts about three hand-picked classes. → m3 (relabel heading).

### C3. §3 / memo y3_frob_infinity (h imitates ∞; Artin-symbol dictionary; cd | 6 genus criterion) — SOUND (minor wording)
Re-derived. h ≡ −1 (mod m) ⟺ σ_h = σ_{−1} = c_∞ in Gal(ℚ(ζ_m)/ℚ) ≅ (ℤ/m)^* — a tautology of the identification.
Type II on (c,d) ⟺ some divisor h > 1 of M = p + 4c²d has h ≡ −1 (mod 4cd) (h ≥ 4cd − 1 is then automatic); with
gcd(M, m) = 1 the Artin symbol is multiplicative, so this is "a sub-product *with multiplicity* (= a divisor) of the
prime factors of M has symbol c_∞"; total symbol σ_M = σ_p as M ≡ p (mod m). Correct.
cd | 6 criterion: m | 24 ⟺ cd | 6, and (ℤ/m)^* is then elementary 2-abelian. In an F_2-vector space the set of
subset sums of a finite family is its span, and −1 ∉ span{σ_q} ⟺ some character (necessarily ±1-valued) kills every σ_q
but not −1, i.e. an odd quadratic character χ mod m with χ(q) = 1 ∀ q | M (⟺ every q | M splits in ℚ(√D), D ∈
{−3, −4, −8, −24} with D | m). This is pure linear duality — so the numerical check can only catch coding errors, and
"genus theory" is a generous name (MINOR, wording). From scratch (`scripts/review_r216_genus.py 100000`, all 9 slices
with cd | 6, all primes 5 ≤ p < 10⁵): 86 310 instances, 45 418 firing, **0 mismatches**; a deliberately wrong criterion
gives 1 948 mismatches on p < 3000 (the check is sensitive). The author's count 86 310 matches exactly.
"Thm 3.1's gcd = 2 is |D_∞|" and "the size conditions are what imitating ∞ costs" are numerology/heuristics and are
labelled as such (Assessment) — fine. Construction (1) (Carlitz D_∞ = F_q^*) is flagged "not checked against
FUNCTIONFIELD_ES" — fine as Assessment.

### C4. CONJECTURE PM-II and the census (§5, memo y3_primemod_census) — SOUND (EVIDENCE confirmed; two minor numerical-statement defects)
From-scratch exhaustive census `scripts/review_r216_census.c` (different algorithm from the author's): parametrise a
certificate (c,d,h), h = 4cdj − 1 | n + 4c²d, by (c,d,t,j) with t = (nj + c)/h; then **n = 4cdt − (c+t)/j with
j | c + t**, a bijection onto all c,d,t ≥ 1, j | c + t (proof in the file header). Enumerating all c,d,t with
4cdt − c − t ≤ N and the divisors j of c + t lists every certificate of every n ≤ N; h-primality by deterministic
64-bit Miller–Rabin. Validated against a naive divisor brute force (`review_r216_census_brute.py`, factor
n + 4c²d over all slices with c(4d − 1) ≤ n + 1): identical (N_II, N_II^pr) for all 454 primes and odd squares ≤ 3000.
Results (data/r216/census_1e6.txt, census_1e7.txt — **complete census to 10⁷**, 10× the brief's floor):
* Primes p ≥ 5, p ≤ 10⁷ with N_II^pr ≤ 1: exactly **13 (1), 193 (1), 3361 (0), 76441 (1)** — as claimed.
* min N_II^pr on [10⁵, 10⁶] = 5 at 152461; mean N_II = 222.85, mean N_II^pr = 45.35 (author 222.9 / 45.4 ✓); all
  dyadic rows of the memo's table reproduced (e.g. [2¹⁶, 2¹⁷]: 5709 primes, 157.2, 35.44, min 1 at 76441 ✓);
  window [10⁷, 10⁷ + 2000]: 121 primes, 401.96 / 70.17, min 34 ✓ (exact match).
* Odd squares ≤ 10⁷: 1580, none with any Type II certificate (T1 control ✓).
* Growth: mean N_II^pr/log²p over full dyadic blocks *decreases monotonically*: 0.289 ([2¹⁰,2¹¹)), 0.271, 0.267, …,
  0.265 ([2¹⁹,2²⁰)), 0.264, 0.264, 0.263 ([2²²,2²³)); mean N_II/log³p: 0.124 → 0.096. The author's "0.10–0.12·log³p
  for 10³ ≤ p ≤ 10⁸" is contradicted by the author's own 10⁷ sample (401.96/log³(10⁷) = 0.096) and by every full
  block above 2²⁰; "(0.27–0.33)·log²p" holds only because of the 54-prime window at 10⁸ (113.1/log² = 0.333), which
  is out of line with the block trend (see the 10⁸ run below). → m4.
(1e8 rerun: see C4b below.)
