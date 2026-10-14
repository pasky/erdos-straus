# R216 — hostile review of O211 (BRIDGE_WORLDS.md + BRAINSTORM/y3_*.md)

**Repairs applied (R216, author quiet since 19:51):** M1, M2, m1–m8 applied in place in BRIDGE_WORLDS.md, memos
y3_ordinary_bridge / y3_semiprimitive_collapse / y3_primemod_census, and AGENT_REPORT_O211.md, each marked "(R216 repair)";
m9 (wording only) not applied.

Reviewer: R216 (side agent). Branch `side-agent/review-bridge-worlds`, merged `side-agent/bridge-worlds` at 7714153a.
**ES is not solved; nothing in O211 claims otherwise, and nothing here changes that.**
From-scratch scripts: `scripts/review_r216_*.{c,py}` (none of the author's `scripts/y3_*` were reused).

## Summary verdicts
| claim | verdict |
|---|---|
| §1 Lemma 1.1, Prop 1.2 (scaling collapse), Prop 1.3 (additive bridge), Stickelberger sign (−1)^j | SOUND |
| Uniform-cyclotomy residue law m²(a,b) ≡ 1, 1 − m, 1 − 3m (labelled EVIDENCE) | SOUND, and in fact PROVED (two-line Jacobi-sum proof, C1) — relabel |
| Thm 2.1 (a)/(b)/(c), Cor 2.2 | SOUND-AFTER-REPAIRS (minor: (b) regularity step & examples outside the definition; (c) "fixed formula" quantifier missing; heading overclaims "classification") |
| "every useful bridge is archimedean" | correctly labelled Assessment everywhere ✓ |
| §3 / y3_frob_infinity dictionary + cd \| 6 criterion (0 mismatches in 86 310) | SOUND (re-checked from scratch: 86 310 / 0 mismatches; it is linear duality) |
| §4 Type I overlap + dual Hasse window (g ∈ {1,3,5}, CM refuted) | SOUND |
| §5 CONJECTURE PM-II + census | SOUND as EVIDENCE (independent complete census to 10⁸, C4/C4b: exceptions 13, 193, 3361 (0), 76441 exactly); minor: growth constants, adversarial numbers |
| Prop 6.1 | SOUND |
| Prop 6.2 (T1 kept; (p/h) = −1 ⟺ firing at good h; numerics) | SOUND-AFTER-REPAIRS (MAJOR: the variant is never defined, and the natural reading "E⁺ of K_{4cd}" FAILS T1 by the author's own ℚ(√3) example; provability is GRH/Artin-type, not unconditional; novelty = (J)23 mechanism at rank 1) |
| §8 / y3_ordinary_bridge (1): \|Hom(E(F_h),F_h^*)\| ≤ gcd(a_h − 2, h − 1) | GAP — false as stated (counterexamples), true for the image of a single homomorphism; repair trivial, conclusions unaffected |
| §8 (2)–(4), Mazur, trace-a equation | SOUND |
| memos Salié / Gross–Koblitz / Euclid–Schur / Lucas–Dickson | SOUND |
| Labels overall | no FATAL overclaim; ES and "no infinite case" disclaimers present throughout |

No FATAL defect. Two MAJOR (M1, M2), nine MINOR.

## Checks, claim by claim

### C1. §1 Lemma 1.1 / Prop 1.2 / Prop 1.3 (scaling collapse, additive bridge) — SOUND (one label understated)
Re-derived. Lemma 1.1: F_h^* = ⟨g^{h+1}⟩ ⊂ ⟨g^m⟩ since m | h + 1. Prop 1.2: x ↦ (λ^{w_i}x_i) preserves each C_{a_i}
(λ^{w_i} ∈ F_h^* ⊂ C_0) and maps F = u to F = λ^e u. Prop 1.3: the identity ∏_{ζ≠1}(X − ζ) = (X^c − 1)/(X − 1) at X = 1; then
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

### C5. §6 Prop 6.1 / 6.2 (unit twists) — SOUND-AFTER-REPAIRS (definition must be stated; provability label/novelty to be sharpened)
**The variant is never defined as a named statement.** Reading Prop 6.2 and the numerics, it is:
> **Fire⁺(n, h)** (h prime ≡ 7 mod 8): ∃ c, d ≥ 1 with **cd even** and 4cd | h + 1, ∃ k ∈ ℤ, with
> h | N_{ℚ(√2)/ℚ}(n + 4c²d·ε₀^{2k}) (ε₀ = 1 + √2), equivalently −n/(4c²d) ∈ U_h := ⟨ρ_𝔥(3 + 2√2)⟩ ⊂ F_h^*.
> n is "E⁺-solvable" iff Fire⁺(n, h) for some h.
U_h does not depend on 𝔥 | h ((3 + 2s)(3 − 2s) = 1). Note this predicate is *not* a superset of Type II (slices with
cd odd are excluded; ES Type II on cd-even slices is the k = 0 sub-case), and it is a firing predicate, not an
Egyptian-fraction equation; "ES-cousin" should be read in that sense. → M2 (define it).
Prop 6.1: ring-homomorphism + norm facts, correct (h | N(α) ⟺ some 𝔮 | h divides α — no splitting hypothesis needed).
The triviality repair (ε = −1 ⇒ h = 3, c = d = 1 fires for every p ≠ 3; p = 3 fires genuinely at h = 7) is correct.
Prop 6.2(i): re-derived. h ≡ −1 (mod 4d₀), h ≡ 3 (mod 4): (d₀/h) = (h/d₀)(−1)^{(d₀−1)/2} = (−1/d₀)(−1)^{(d₀−1)/2} = 1;
if 2 | d then 8 | h + 1 and (2/h) = 1; hence (−d/h) = −1. U_h ⊂ F_h^{*2}; for n = r², h ∤ n, −n/(4c²d) has symbol
(−d/h) = −1 ∉ squares; for h | n the target is 0. **T1 kept: PROVED** (this is the classical Mordell/Yamamoto
step, used exactly as in (J)23 Cor 1.2).
Prop 6.2(ii): (−pd/h) = (p/h)(−d/h), so U_h-membership needs (p/h) = −1; at h ≡ 7 (8), |F_h^{*2}| = (h − 1)/2 is odd,
so if [F_h^* : ⟨ρ(ε₀)⟩] ≤ 2 then ⟨ρ(ε₀)²⟩ = F_h^{*2} and any slice (e.g. (1,2), always admissible) fires. Correct.
Numerics from scratch (`scripts/review_r216_units.py`): 2399 primes h ≡ 7 (8) below 10⁵, index of 1 + √2: 1 → 891,
2 → 909 (good: 1800 ✓); every prime 5 ≤ p < 10⁵ fires at some h < 2000 ✓; least firing h: 7 → 4812, 23 → 2415,
31 → 1198, 47 → 609 ✓; (p/h) = −1 necessity: 0 violations; good h with (p/h) = −1 but no firing: 0; genuine
Type II at the least firing h: 7705/9590 ✓; odd squares r² (r < 317) at all h < 2000: 0 firings ✓; h = 103: index 3,
|U_h| = 17, (5/103) = −1, p = 5 fires on none of the six admissible slices ✓.
**Novelty / provability (the brief's question).** The mechanism is *literally* that of (J)23 Thm 2.4: there, a prime
r ≡ 3 (4) with (n/r) = −1 and [F_r^* : ⟨S⟩] ≤ 2 gives −n/4 ≡ Q² with Q ∈ ⟨S⟩; here the role of ⟨S⟩ ⊂ ℚ^* is played
by ⟨ρ_𝔥(ε₀)⟩, with the extra Chebotarev condition h ≡ 7 (8). The difference is the rank: (J)23 is unconditional
because |S| ≥ 4 permits Gupta–Murty/Heath-Brown; here the group is generated by ONE element, so "every p is
E⁺-solvable" reduces to an Artin-type statement for the single unit 1 + √2 on a Chebotarev set (good h ≡ 7 (8) with
(p/h) = −1), which is known only under GRH (Hooley/Lenstra-type; the Kummer fields ℚ(√2, ε₀^{1/ℓ}) are unramified
outside 2ℓ, so no entanglement with (p/·) — plausible, NOT checked here, as the author also says). That makes it a
GRH-type cousin like (J)21 (V_φ, rank-1 mute unit), **not a new unconditional ES-cousin**. Nothing in O211 claims
unconditionality; but the §6 sentence "whose provability for every p is an Artin-type statement … (GRH à la Hooley …)"
should carry an explicit label: CONJECTURE (unconditional) / CONDITIONAL on GRH only after a written Lenstra-type
density argument; at present Assessment. → m5. On the higher-rank spark: for ℚ(ζ_{2^k})⁺ every totally positive
unit is a square (Weber's units of independent signs — recalled, not checked here), so the T1 argument of (i)
would survive on 2-power slices; this is the natural repair of the ℚ(√3) failure the author notes and worth a line in
the spark list (no claim made).

### C6. §8 / memo y3_ordinary_bridge — GAP (finding (1) is FALSE as stated; the intended statement is true)
(1) claims **|Hom(E(F_h), F_h^*)| ≤ gcd(a_h − 2, h − 1)**. The proof bounds the *image of one homomorphism*
(cyclic, order | exp E(F_h) and h − 1), not the number of homomorphisms. With E(F_h) ≅ ℤ/n₁ × ℤ/n₂ (n₁ | n₂,
n₁ | h − 1), |Hom| = gcd(n₁, h − 1)·gcd(n₂, h − 1) = n₁·gcd(n₂, h − 1). Counterexamples (from scratch,
`scripts/review_r216_misc.py`, brute-force group structure): y² = x³ − x over F_7 (supersingular): E ≅ ℤ/2 × ℤ/4,
|Hom| = 4 > gcd(−2, 6) = 2; y² = x³ + 1 over F_7 (ordinary, a = −4): ℤ/2 × ℤ/6, |Hom| = 12 > gcd(−6, 6) = 6;
38 counterexamples for h ≤ 13 alone. The image bound gcd(n₂, h − 1) ≤ gcd(a_h − 2, h − 1) held in every case
(asserted for all curves, h < 60). → M1. Repair: "every homomorphism E(F_h) → F_h^* has image of order
≤ gcd(n₂, h − 1) ≤ gcd(a_h − 2, h − 1)"; and |Hom| = n₁·gcd(n₂, h − 1) ≤ gcd(a_h − 2, h − 1)² (n₁ | gcd(N, h − 1)).
The downstream conclusions (Hasse-bounded images unless a_h = 2) are unaffected — they only use the image bound.
(2) correct (gcd(m, h − 1) | 2). (3) Mazur: E(ℚ)_tors is ℤ/n (n ≤ 10, 12) or ℤ/2 × ℤ/2n (n ≤ 4); a point Q has order
≤ 12, so t_n(Q, ·) has image ⊂ μ_{ord Q}, ≤ 12 elements. Correct (also needs μ_{ord Q} ⊂ F_h, i.e. ord Q | h − 1, else
the reduced pairing lands in an extension — harmless). Lang–Trotter attributions: a_h = 2 density zero unconditionally
is Serre 1981 (correct as recalled; not re-read). (4) re-derived: 4cdj = h + 1 − a ⇒ 4c²dj ≡ (1 − a)c, so
h | p + 4c²d ⟺ h | pj + (1 − a)c (gcd(j, h) = 1). Correct. "Type I is the imaginary-quadratic tier (c)":
N(p + 2c√−d) = p² + 4c²d — correct as an identity; the analogy is Assessment.
Numerics: the author's example y² = x³ + x + 1 at h = 127 has E ≅ ℤ/126 (cyclic) ✓.

### C7. §4 / memo y3_typeI_hasse_window (Type I overlap, dual Hasse window) — SOUND
Re-derived the window proof line by line: with f + p = 4cd·a, g + p = 4cd·b, fg = p² + 4c²d ⟺ c(4abd − 1) = p(a + b);
cd ≤ p(a+b)/(4ab − 1) ≤ 2p/3 (uses d(4ab − 1) ≤ 4abd − 1), c ≤ 2p/3, so c²d ≤ 4p²/9, g ≤ (100/9)p²/(p − 1)² < 13 for
p ≥ 17 (12.54 at p = 17); g odd; g ∈ {7, 9, 11} excluded via c²d ≤ (cd)² ≤ ((p+g)/4)² (g = 7: p² − 14p − 21 ≤ 0 ⟹
p ≤ 15.4). g = 3 ⟹ p ≡ 1 (4), 3 ∤ c, d ≡ 2 (3); f ≡ −p (mod 4cd) automatic from fg ≡ p², g ≡ −p. Correct.
From scratch (Type I window certificates with f prime, 17 ≤ p < 3000): 1621 certificates, g ∈ {1: 1251, 3: 320, 5: 50},
none outside {1,3,5}; CM field ℚ(√((p − 1)² − 4f)) = ℚ(√−d) in 0 cases ✓ (smaller range than the author's 20000).
Overlap: Frob_f acts on μ_{4cd} ⊂ μ_{f+p} by ζ ↦ ζ^f = ζ^{−p}; |Hom(μ_{f+p}, F_f^*)| = gcd(f + p, f − 1) =
gcd(p + 1, f − 1); 4cd | f − 1 ⟺ 4cd | p + 1 ⟹ p ≡ 3 (4); then g = 1, f = p² + 4c²d ≡ −p ✓. Example (17,1,3,43,7):
301 = 7·43, 43 ≡ 7 ≡ −17 (mod 12), gcd(18, 42) = 6 ✓. Minor: the report's "partial overlaps exist for p ≡ 1 (4) on
finitely many slices" — for fixed p there are finitely many slices anyway; the phrase adds nothing (m6).

### C8. Memos y3_salie_angle, y3_gross_koblitz_box, y3_euclid_schur_forcing, y3_lucas_dickson_trace — SOUND (minor)
Salié: S(a,b;h) = i√h (b/h) Σ_{y² ≡ ab} e(2y/h) for h ≡ 3 (4) — verified from scratch on 6522 cases (h < 200, a ∈
{1,2,5}, all b), 0 failures. Dictionary re-derived: y₀ = 2cd, y₀² = 4c²d² ≡ −pd, 2y₀j = h + 1; converse needs h ∤ d
(automatic). Correct; "plausibly new in this form" is a fair Assessment.
Gross–Koblitz: a/(q−1) = i/m; ⟨h·i/m⟩ = 1 − i/m (h·i/m = ij − i/m); π^{h−1} = −h; reflection
Γ_h(x)Γ_h(1 − x) = (−1)^{ℓ(x)}, ℓ(x) ∈ {1..h}, x ≡ ℓ (mod h): checked by hand at x = 1 (Γ(1)Γ(0) = −1·1) and x = 2
(Γ_7(2) = 1, Γ_7(−1) = Γ_7(0) = 1 from Γ(x + 1) = −xΓ(x)); so g = (−1)^{ℓ(i/m)}h, ℓ(1/m) = j ✓ consistent with
Stickelberger. Robert/GK texts not accessed; sign conventions for the Teichmüller exponent were not re-derived (they
only swap i ↔ m − i; for i = m − 1, ℓ((m−1)/m) = h + 1 − j and (−1)^{h+1−j} = (−1)^j since h + 1 is even ✓).
Euclid–Schur: Prop E1 correct (a subgroup of index 2 or more has ≤ |G|/2 < |G| − 1 elements when |G| ≥ 3); E2
correct; Remark E3 correct (7 | p + 8 for p ≡ 6 (7), 7 ≡ −1 (8)). Schur/Murty statement (Euclidean proof exists iff
a² ≡ 1) recalled correctly; sources not accessed.
Lucas/Dickson (Prop G): D_c'(2) = c² ✓ (T_c'(1) = c², D_c(x) = 2T_c(x/2)); Σ_{k<c} csc²(πk/c) = (c² − 1)/3 ✓
(classical) — note this is an identity in ℤ[1/3] ⊂ F_h only for h ≠ 3 (fine, h ≥ 7). "Primitive prime divisors of
U_{4cd} with (D/h) = −1 are ≡ −1 (mod 4cd)" ✓ (rank of apparition = 4cd divides h − (D/h) = h + 1).

### C4a. Adversarial stacked-QR primes (§5 / memo) — numbers inconsistent between documents
From scratch (`scripts/review_r216_adversarial.py`, first 4 primes p ≡ 1 (mod 4∏_{q≤Q} q) for Q = 13, …, 29, up to
1.8·10¹¹; slices cd ≤ 200 with a prime h ≡ −1 (mod 4cd) dividing p + 4c²d): Q = 13: 11, **4 (p = 600601)**, 13, 11;
Q = 17: 18, 11, 8, 11; Q = 19: 18, 14, 15, 19; Q = 23: 19, 12, 16, 16; Q = 29: 20, 14, 14, 14. The memo's "4–20 (min 4
at p = 600601)" is right; BRIDGE_WORLDS §5 ("still have 14–20 prime-firing slices") and the report ("≥ 14") are
wrong. → m7.

## Defects
**M1 (MAJOR; BRIDGE_WORLDS §8(i), memo y3_ordinary_bridge Finding (1), report SHARP 5).** "|Hom(E(F_h), F_h^*)| ≤
gcd(a_h − 2, h − 1)" is false (y² = x³ − x / F_7: 4 > 2; y² = x³ + 1 / F_7: 12 > 6). Repair: state the bound for the
image of any one homomorphism (≤ gcd(n₂, h − 1) ≤ gcd(a_h − 2, h − 1)); if a count is wanted, |Hom| = n₁·gcd(n₂, h − 1)
≤ gcd(a_h − 2, h − 1)².
**M2 (MAJOR; §6 Prop 6.1/6.2, §7 table, report SHARP 4).** The E⁺-twisted variant is never defined, and the text
suggests the general repair "allow only totally positive units E⁺" of K_{4cd} = ℚ(ζ_{4cd})⁺. Under that reading T1
FAILS: at the slice (c,d) = (1,3), K_12 = ℚ(√3), E⁺ = ⟨2 + √3⟩, n = 9 fires at h = 11 (the author's own example). The
proved statements hold only for the restricted predicate Fire⁺ (C5): units ⟨ε₀²⟩ ⊂ ℚ(√2) on slices with cd even.
Repair: insert the definition of Fire⁺ (C5) before Prop 6.2, say explicitly that it is neither weaker nor stronger
than Type II (cd-odd slices excluded) and is a firing predicate (not an Egyptian-fraction equation), and that the
K_{4cd}-wide E⁺ variant is NOT T1-keeping (n = 9, h = 11).
**m1 (Thm 2.1(b)).** Add the regularity step (S regular at μ_m ⟹ S = A(e)/B(e), B(e(μ_m)) ≠ 0) and define "good
reduction" via that representation; reword the examples: |μ_c| is not a rational function, ∏(1 − ζ) and Σ csc² are
symmetric in μ_c ∖ {1} (cover them by "symmetric functions of the roots of a fixed monic F ∈ ℤ[X]").
**m2 (Thm 2.1(c)).** Add "for a characteristic-zero formula fixed independently of h (and p)"; without it the tier
is vacuous (the prime field of F_{h²} is F_h). Prop G in y3_lucas_dickson_trace already says this.
**m3 (§2 heading).** "Classification of bridges … (PROVED)" → "Three elementary bridge tiers (PROVED; scope: these
classes only)".
**m4 (§5, memo census, report).** Growth constants: over full dyadic blocks mean N_II^pr/log²p decreases 0.289 → 0.263
and mean N_II/log³p 0.124 → 0.096 (to 2²³); "(0.10–0.12)·log³p for 10³ ≤ p ≤ 10⁸" is contradicted by the author's own
10⁷ window (0.096). Repair: quote the block values and say the normalised means drift slowly downward (the growth
law is not established; Assessment).
**m5 (§6 provability sentence).** Label it: Assessment (E⁺-solvability of every p is an Artin-type statement for the
single unit 1 + √2 on a Chebotarev set; expected under GRH via a Lenstra-type density argument not written out; not
unconditional — rank 1, unlike (J)23's |S| ≥ 4).
**m6 (report "Other results").** "partial overlaps exist for p ≡ 1 (4) on finitely many slices" — vacuous qualifier;
say "on slices with gcd(cd, (p+1)/2) > 1".
**m7 (§5, report SHARP 3).** Adversarial counts: "14–20" / "≥ 14" → "4–20 (min 4 at p = 600601)", as in the memo.
**m8 (§1, §7, report).** Uniform-cyclotomy residue law: EVIDENCE → PROVED, with the two-line proof of C1 (the pattern
is 1 − m(δ_{a0} + δ_{b0} + δ_{ab})); spark 2 is thereby closed.
**m9 (§3 / memo / report).** The cd | 6 criterion is F_2-linear duality (subset sums = span); "genus theory" is
acceptable as a name but the 86 310-instance check is only a coding check — say so.

### C4b. Census to 10⁸ (complete, from scratch; data/r216/census_1e8.txt, ~35 min, 1 core)
Complete census of all Type II certificates for all n ≤ 10⁸ + 1000: the primes with N_II^pr ≤ 1 are exactly
**13, 193, 3361 (0), 76441** — independently confirming the author's tf_primemod rerun and extending the full census
(N_II and N_II^pr for every p, not just existence) from 10⁶ to 10⁸. Odd squares ≤ 10⁸: 4999, none with a Type II
certificate. Full-block minima keep growing (min N_II^pr = 16 on [2²⁵, 2²⁶), at 40238641). Normalised block means
continue to drift down: N_II^pr/log²p = 0.262, 0.262, 0.261 and N_II/log³p = 0.094, 0.094, 0.093 on the blocks
[2²³, 2²⁶). The author's window [10⁸, 10⁸ + 1000] is reproduced exactly (54 primes, 680.83 / 113.06, min 38), but it is
an outlier against the block trend (expected ≈ 0.261·log²(10⁸) ≈ 88.5 vs 113.06), so the "0.33" upper end of the
quoted range comes from one short window (m4).
