# R263 — hostile review of O254 (JOINT_BUDGET.md)

Reviewer: R263 side agent (branch side-agent/review-joint-budget). Author branch merged: side-agent/joint-budget.
From-scratch scripts: `scripts/review_r263_*.py` (none of the author's z26 code reused).

**Repairs applied** (author quiet after its final report): D1, D2, D3, D4, D5, D6, D8, D9 and the §6 Type-II-scope note,
directly in JOINT_BUDGET.md, each marked "(R263 repair)". D7 (the report's proposed ledger line) is left to the parent.

**Bottom line:** no FATAL, two MAJOR (framing D1, missing prior art D2 — Prop 3.2/Cor 3.3 are LONGSHOT_PIGEONHOLE
(O135) Prop 1.4/1.4(b)/Lemma 2.1), seven MINOR. Every PROVED statement re-derived and checked by from-scratch code;
no mathematical error found. Full table at the end.

## Per-claim checks

### §1 Theorem A — SOUND (minor wording)
Re-derived. The nine RT2 side numbers listed in §1 match RT2 Lemma 2.1 exactly (I{c,d}, I{a,c}, I{a,e}, I{d,e};
II{c,d}, II{a,c}, II{a,d}, II{a,e}, II{d,e}). Linear rows: N = αX + β with α ∈ {a, e, 4c²d, c, 1}, α ≢ 0 because it is
positive somewhere; after removing g = gcd(α, β) the polynomial is primitive of X-degree 1 over the UFD ℚ[u], hence
irreducible (any factorisation has a factor of X-degree 0, which divides the content). Quadratic row: X² + 4c²d monic;
reducible over ℚ(u) iff −d ∈ ℚ(u)² (c ≢ 0); a square of ℚ(u) is ≥ 0 wherever defined, so d(u₀) > 0 at one real point
already excludes it. Correct. The (·,e)-row numerators eX + 1 and X + e have content 1.
From-scratch check `scripts/review_r263_thmA.py` (sympy factor_list in ℚ[u₁,u₂,X]): 40 random slice tuples × 9 rows
= 360 side numbers, half of them with a deliberately shared polynomial factor among a, c, d, e (to exercise the
content g): 0 violations. Negative controls behave as they must: d = −w² splits X² + 4c²d into two X-factors
(Remark 1.2 confirmed); d = (u₁² − 2)² (≥ 0, zero on a set) stays irreducible; the Remark 1.3 identity
4c²dX + 1 = (4acd − 1)(4bcd − 1) at d = (X + e)/(4ab), e = (a+b)/c holds symbolically.
Hidden hypotheses: none of substance. The "positive on a non-empty open set U" hypothesis is stronger than needed
(positivity of d at one real point suffices for the quadratic row; α ≢ 0 for the linear rows) — harmless.
Content: this is Gauss's lemma plus one sign; the document says "elementary", which is the right label.

### Remark 1.2 — SOUND
(X − 2cw)(X + 2cw) = X² − 4c²w². "The only place Theorem A uses more than Gauss's lemma is d > 0" is correct
(c ≢ 0 is also used but is automatic). The interpretive tail ("matching (J)52's positivity is T1's anchor") is
Assessment, not PROVED; harmless.

### Cor A.1 — SOUND
Divisors of g·N′ in the UFD ℚ[u, X] with N′ irreducible are (const)·g₁ or (const)·g₁N′, g₁ | g. For fixed u, f is
either a fixed integer or g₁(u)N′(u, p); with RT2's R_θ(p) depending on p mod q_θ (and, rows (d,e), on N mod q_θ) the
class condition is periodic in p with a period M(u) (denominators of N′ absorbed into M(u)). Fine.

### Remark 1.3 — SOUND (but see defect D1 on what it means)
A ℚ-polynomial P with D·P ∈ ℤ[X] satisfies P(X + Dt) − P(X) ∈ ℤ, so integrality is periodic; positivity is eventual.
Correct.

### §2 Prop 2.1 — SOUND-AFTER-REPAIRS (wording; (c) is a reduction, as labelled)
(a) |φ(u)| ≤ X ⇒ |u| ≪ X^{1/D} for one-variable φ of degree D: correct; density 0.
(b) Checked against NORMFORM_CUBIC: Thm 1.1′ (Type II, valid at one point, P* prime) and Thm 3.1 with the R259 repair
(Type I, valid at one point, P* irreducible ⇒ gr ℚ[x]/(P) a domain ⇒ only constant units). The ES coordinate
conventions agree: Type II 4abd = p + e, ce = a + b ⇔ 4ABCD = A + B + CP; Type I 4abd = pe + 1 ⇔ 4ABCD = P(A + B) + C.
φ* irreducible ⇒ φ irreducible ((UV)* = U*V*), so P = φ is prime as (J)79 requires. Schinzel (ET §1, polynomial
solutions with positive leading coefficients cannot cover a quadratic-residue class): an ET identity in n valid at
infinitely many n has positive leading coefficients and is integral on a union of classes mod some M (integer-valued
polynomials become ℤ-coefficient after n ↦ M′t + r), so it covers only non-square classes and misses every prime
≡ 1 (mod M). Correct. Typo: "valid at one point (Type II) or at one point (Type I …)" — duplicated phrase.
(c) The case split is complete (r = 1: (a); r ≥ 2: φ* irreducible (b); φ* reducible and degree 1 in some variable (c);
else (d)). But the proof of (c) treats "α a non-zero constant", which the statement of (c) excludes (α ∉ ℚ), and for that
case cites the wrong result: with u_r = (p − ψ(u′))/α the family's coordinates are polynomials in (u′, p), i.e. the slice
parameters DO depend on p, so Theorem A (p-free slices) does not apply — Remark 1.3 does (and sides can split, e.g. the
ET-variety example right below). See defect D3.
(d) Residual correctly stated as "no claim".

### §3 window form — SOUND
Type II with e = m: 4abd = p + m, cm = a + b ⇔ ab | K, m | a + b. Reduction to coprime (a, b): a prime ℓ | gcd(a, b, m)
divides K and m, hence 4K − m = p; excluded by gcd(m, p) = 1, so dividing by gcd(a, b) keeps m | a + b. The
exponent-vector description of Σ_m(K) is then exact. From-scratch brute force (`scripts/review_r263_kneser.py` part 1):
all primes p ≡ 1 (4) < 1200, all windows m ≡ 3 (4), m < 2p, gcd(m, p) = 1 (26 430 windows): "∃ a, b (any gcd) with
ab | K, m | a + b" ⇔ "−1 ∈ Σ_m(K)": 0 mismatches; every hit verified exactly as 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp).

### Lemma 3.1 — SOUND (near-tautological, as the author says)
a + b ≤ ab + 1 ≤ F + 1 < 4F. Correct.

### Prop 3.2 (Kneser threshold) — SOUND
Re-derived. (ℤ/m)^× cyclic; Σ = Σ_s A_s with A_s symmetric progressions; 0 ∈ Σ so H := Stab(Σ) ⊆ Σ ⊆ H₀, and Σ ≠ H₀ ⇒
H ≠ H₀. In G/H the image has trivial stabiliser (Stab(Σ̄) = Stab(Σ)/H), so Kneser for k summands gives
|Σ̄| ≥ Σ|Ā_s| − (k − 1). If ℓ_s ∉ H and Ā_s wrapped around (2b_s + 1 ≥ ord ℓ̄_s), Ā_s is the non-trivial subgroup ⟨ℓ̄_s⟩
and Σ̄ + Ā_s = Σ̄ (Ā_s + Ā_s = Ā_s), contradicting trivial stabiliser; so |Ā_s| = 2b_s + 1 for ℓ_s ∉ H, giving
|Σ̄| ≥ 1 + Σ_{s∉H} 2b_s ≥ [H₀ : H] against |Σ̄| ≤ [H₀ : H] − 1. The Kneser statement used is the standard one
(|A + B| ≥ |A + H| + |B + H| − |H|, H = Stab(A + B), iterated). "(K/m) = −1 ⇒ −1 ∈ H₀": H₀ ⊄ squares ⇒ [G : H₀] odd ⇒
|H₀| even ⇒ −1 ∈ H₀ (unique involution of a cyclic group). Correct.
From-scratch brute force (part 3): 40 000 random (m prime in [5, 110), K with 1–6 primes < 400, exponents ≤ 8, half
biased to primes of small order mod m); (3.1) checked over ALL proper subgroups H < H₀ (via divisors of |H₀|): held in
17 379 cases, Σ_m(K) = H₀ in all 17 379 (6 259 of them with m ≡ 3 (4), −1 ∈ H₀). The author's R-review example
p = 809, m = 31, K = 210 reproduced (Σ_31(K) = (ℤ/31)^× while 2Ω(K) = 8 < 29).

### Cor 3.3 — SOUND; labels correct
PROVED part: 2Ω(K) ≤ 2 log₂ K, so H = {1} in (3.1) with H₀ = G fails once m > 2 log₂ K + 2. Correct.
Assessment part is correctly labelled. Its one checkable numeric claim ("least element of −p mod 4F is ≥ F for a
proportion ≥ 3/4 of admissible p mod 4F") checked for all F < 3000 (`scripts/review_r263_cor33.py`, p ≡ 1 (4),
gcd(p, 4F) = 1): minimum proportion exactly 0.75 (at F = 4). Correct. Small imprecision: "(2^E − 2)/2 − E prime
factors" presumes H₀ = G; if the forced primes generate a small H₀ the need is |H₀|-sized, not m-sized (the
"exponential gap" sentence should say "when H₀ = (ℤ/m)^×"). MINOR.

### §4.1 — SOUND except one misattributed citation (D4)
(J)64 forcing: 4K ≡ p (mod m), so (K/m) = (p/m) = (m/p) for p ≡ 1 (4). K = s prime, v_s = 1: Σ_m(K) = {1, s, s⁻¹}, which
contains −1 iff s ≡ −1; for prime m ≡ 3 (4), m ≥ 7, there are ≥ 3 non-residues so one ≢ −1 exists (m = 3: the only
non-residue is −1 — consistent with the "Mordell's class" exception in 5.2(c)). Correct.
But "Whether such K occur for every bounded set of windows is (J)83 Thm 1.3 (CONDITIONAL on Dickson: yes)" misreads
CAP_BOUNDED Thm 1.3: its Dickson primes have (m/p) = +1 for EVERY window m ≤ M (all ℓ ≤ M + 1 split, R_m a residue), i.e.
no forced window at all; it says nothing about forced windows with K = (prime non-residue). See D4.

### Prop 4.2 — SOUND
Re-derived: 4K ≡ p ≡ cw² (mod m), gcd(w, m) = 1 ⇒ (K/m) = (c/m); Jacobi reciprocity with p ≡ 1 (4) (no sign);
m ≡ cw² (mod p), p ∤ w (else p | m) ⇒ (m/p) = (c/p). m | A² − pB², gcd(B, m) = 1: a prime ℓ | gcd(A, m) would give
ℓ | p, so (p/m) = ((A/B)²/m) = +1. (For CF convergents gcd(Q_k, m) = 1 is automatic since gcd(P_k, Q_k) = 1 and
ℓ | Q_k, ℓ | m ⇒ ℓ | P_k; same for near squares m = w² − p. The hypothesis is harmless but redundant.)
From-scratch check (`scripts/review_r263_sec4.py 42`): all primes p ≡ 1 (4) < 10⁵; windows = 6 next-square windows, ALL
odd divisors m > 1 of the first 30 CF norms |P_k² − pQ_k²|, and prime divisors of 3 random A² − pB² (gcd(B, m) = 1):
335 151 windows, 0 with (p/m) ≠ +1. General c: all p ≡ 1 (4) < 5000, m ≡ 3 (4) < 400, every factorisation
p + m = cw² with gcd(w, m) = 1 (92 665 instances): (K/m) = (c/m) = (c/p) in every case. Example p = 17, m = 7, c = 6
reproduced ((6/17) = (6/7) = −1, (a, b) = (1, 6)).
Reading: "Forced windows are exactly the m with (p/m) = −1" — this is the DEFINITION of Jacobi-forced (via (K/m) = (p/m)),
fine; the "structural reason why near-square primes are hard" sentence is Assessment (unlabelled; MINOR).

### Prop 4.3 — SOUND
Type II: p ≡ −e (mod 4ab); Type I: pe ≡ −1 (mod 4ab); 4ab | p − 1 ⇒ e ≡ −1 ⇒ 4ab ≤ e + 1 ≤ a + b + 1, impossible
(4ab − a − b − 1 ≥ 1). p + 1 case trivial. Checked from scratch on all 6 376 ordered Type II points (= the author's 3 188
unordered) of p ≡ 1 (4) < 3000 and all 3 466 Type I points (a ≤ b, enumerated independently via acd < 3p/4,
e = (4a²d + 1)/(4acd − p), each verified exactly) of p ≡ 1 (4) < 1500: 0 violations.

### Remark 4.4 — SOUND for Type II; the Type I extension used in Thm 5.2(e) is true but unproved in the text (D5)
Proof checked: removing g = gcd(a, b) (p ∤ g since p ∤ ab: p | a forces p | e, then 4abd = p + e ≤ 2(a + b), impossible),
Lemma CT (POINTWISE_SIZE §2, notes Lemma 77.6) gives (ab/p) = −1; p ≡ t² (mod 4ab) ⇒ (p/ℓ) = 1 for odd ℓ | ab and p ≡ 1 (8)
when 2 | ab ⇒ (ab/p) = +1 by reciprocity. Correct; ord_{4ab}(p) odd would make p ≡ (p^{(k+1)/2})² a square, so the order
is even. From-scratch check: 6 376 Type II points p < 3000: p non-square mod 4ab at every one.
Type I: Lemma CT also gives (ab/p) = −1 for Type I in the notes' coordinates (ack, bck, pabc); mapping to RT2 (acd, bcd,
abdp) with g = gcd(a, b) (which divides c, since g² | pe + 1 ⇒ gcd(g, e) = 1 and g | a + b = ce) changes ab by g², so
the same proof works. Numerically: 3 466 Type I points p < 1500, p non-square mod 4ab in every case. But the text of
Remark 4.4 says "every Type II point" only, while Thm 5.2(e) asserts "p is a non-square mod every class modulus" for
(R4), whose class moduli include Type I ones. See D5.
Thm C applicability to bounded cyclotomic menus: checked against POINTWISE_SIZE §1.1 — computing p^j − 1 (j ≤ k₀, P2),
DIVISORS, then c | a + b and the test 4ab | p + e (or pe + 1) are all (P1)–(P8) instructions; plus a final exactness
check it is a correct bounded witness-producing program, so Thm C (H) applies. Correct.

### §5 Theorem 5.2 (JF trichotomy) — SOUND-AFTER-REPAIRS (scope/framing, no false mathematics)
Each item re-traced to its source: (a) = Remark 1.3 + Theorem A; (b) = (J)79 Thm 1.1′/3.1 + Schinzel, Prop 2.1(a),
Prop 2.1(c); (c) = §4.1 + Prop 3.2/Cor 3.3 + CAP_BOUNDED Thm 1.3; (d) = Prop 4.2; (e) = Prop 4.3, Remark 4.4,
POINTWISE_SIZE Thm C. Every PROVED tag is backed, every CONDITIONAL tag names its hypothesis. Problems:
* (a), (b)-last and (d) are reformulations, not impossibility statements: ES itself has the shape "u-indexed union of ET
  classes, firing = moving-modulus event" (u = (a, b, c), class p ≡ −e (mod 4ab)). The theorem therefore excludes no
  proof strategy by itself; its genuine negative content is (b)-Schinzel ((J)79), (c)/(e) conditional on Dickson/H
  ((J)83, Thm C) — all pre-existing. Needs an explicit sentence (D1).
* (e) "p is a non-square mod every class modulus" is proved in the text only for Type II (D5).
* (R3) is defined as a *window* rule; archimedean/ℚ(√p) data used as other coordinates (e.g. a = ⌊√p⌋, d or the class
  modulus 4ab from CF data, Type I windows) are covered by none of (R0)–(R4), yet the "Not covered" list implicitly counts
  "archimedean-ℚ(√p)" auxiliaries as covered (D6).
* (c) "the forced information is the image of ⟨primes of K⟩ in H₀/H₀^ℓ" — what (J)64 gives is one bit, the image of K
  (with multiplicities) in G/G², i.e. (K/m) = −1; "image of ⟨primes of K⟩ in H₀/H₀²" is a different (and not forced)
  object. Imprecise wording (MINOR, D8).
The "Not covered" list is otherwise honest and accurate: (R1) residual, growing k₀, the (J)64/(J)66 regime.

### §6 numerics — SOUND (spot-checked from scratch)
`scripts/review_r263_sec4.py depth …` (own window enumeration, each point verified exactly, sympy n_order):
p = 210 961 (≡ 121 mod 840): 46 ordered Type II points, k* = 72, all orders even — matches. p = 80 809 and 296 041:
k* = 42 — matches. All 53 Mordell-hard primes < 2·10⁴: max k* = 22 (histogram {2:13, 4:6, 6:6, 8:3, 10:11, 12:9, 14:1,
16:2, 22:2}), all orders even — matches the author's "at N = 2·10⁴ the maximum was 22". T1 control: no odd square
t², t < 400, has a Type II point. Labels: EVIDENCE, correctly hedged in JOINT_BUDGET ("growing in range"). But the
report's proposed ledger line says "EVIDENCE: cyclotomic depth unbounded" — overclaim relative to the text (D7).
Note the k* statistic is a min over Type II points only (the report says so; §6 should say so too).

### Novelty / prior art — MAJOR attribution gap (D2)
* Theorem A: Gauss's lemma + a sign; new as a stated lemma, elementary.
* §3 window form, Prop 3.2, Cor 3.3: **already in LONGSHOT_PIGEONHOLE.md (O135, reviewed R135, DISCOVERIES item 9)**:
  Lemma 1.1 there is the window form (−1 ∈ Σ_e(N)); Prop 1.4 there is the Kneser covering criterion in a strictly more
  general form (any target t₀, condition over all H ∌ t₀ with min(2v_i + 1, o_H(g_i)), sharpness example 1.4(c)), and
  1.4(b) is Cor 3.3's PROVED part (Ω(N) ≥ (φ(e) − 1)/2); its §2.1 Lemma 2.1 (CRT forcing costs e^{(1+o(1))k log k}
  against 3^{k+1}) is precisely the "exponential budget gap" that Cor 3.3 states only as Assessment — there it is
  PROVED. JOINT_BUDGET cites none of this; the report credits only the Cauchy–Davenport remark of SPARKS7 s6.
  Prop 3.2 is the special case t₀ = −1 ∈ H₀, H ranging over subgroups of H₀ (equivalent after restricting to H₀).
* Prop 4.2: elementary and, as far as I can find in DISCOVERIES/STATUS, new as stated; related to (J)61 (near-square
  signs as Artin symbols) and (J)53/(J)55 — should be cross-referenced.
* Prop 4.3 / Remark 4.4: immediate corollaries of Lemma CT (notes Lemma 77.6); new as stated, small.
* Thm 5.2: synthesis (the report says so honestly).

## Numbered defects (no FATAL)
**D1 (MAJOR, framing; §1 "Reading", §5 title/closing, §7, ledger line).** Cor A.1 / Remark 1.3 / Thm 5.2(a),(b)-last,(d)
conclude "u-indexed union of ET classes; firing is the moving-modulus event". ES itself has exactly this shape
(u = (a, b, c), class p ≡ −e mod 4ab), so these items exclude no strategy; they say only that the auxiliary contributes no
*algebraic* factor. Calling §5 "the obstruction theorem" and the ledger's "no algebraic budget at a general prime"
invite over-reading. *Repair:* add after Thm 5.2: "(a), (b)-last and (d) are reformulations, not impossibility
statements — the full ET parametrisation is itself of shape (a); the genuine negative content is (b)-Schinzel and the
conditional parts of (c), (e), all from (J)79, (J)83, Thm C." (R263 repair applied.)
**D2 (MAJOR, attribution; §3, report).** Window form, Prop 3.2 and Cor 3.3 (incl. the "exponential gap", there PROVED)
are LONGSHOT_PIGEONHOLE (O135) Lemma 1.1, Prop 1.4 (more general), 1.4(b) and Lemma 2.1. *Repair:* cite O135 at §3,
state Prop 3.2 as "the t₀ = −1 ∈ H₀ case of O135 Prop 1.4", and replace the Assessment gap sentence by a citation of
O135 Lemma 2.1 (PROVED there). (R263 repair applied.)
**D3 (MINOR; Prop 2.1(c) proof).** Statement assumes α ∉ ℚ, proof treats α constant; for α constant the coordinates are
polynomials in (u′, p) and the right reference is Remark 1.3, not Theorem A (p-dependent slices may split — the ET-variety
example just below). Also the duplicated "valid at one point (Type II) or at one point (Type I…)" in (b). *Repair:* say
"(If α is a non-zero constant … Remark 1.3 applies with u′ auxiliary)". (R263 repair applied.)
**D4 (MINOR; §4.1).** "Whether such K occur for every bounded set of windows is (J)83 Thm 1.3 (CONDITIONAL on Dickson:
yes)" — CAP_BOUNDED Thm 1.3 builds primes with NO forced window ≤ M ((m/p) = +1 for all m ≤ M); it does not produce forced
windows with K = (prime non-residue). *Repair:* "That bounded window sets fail infinitely often (with all windows ≤ M
unforced) is (J)83 Thm 1.3 (CONDITIONAL on Dickson); whether forced windows with K = s occur at every bounded window set
is not claimed." (R263 repair applied.) Thm 5.2(c)'s use of Thm 1.3 is fine as worded.
**D5 (MINOR; Remark 4.4 vs Thm 5.2(e)).** Remark 4.4 is stated/proved for Type II only, 5.2(e) asserts it for every class
modulus. The Type I case follows the same way (Lemma CT gives (ab/p) = −1 for Type I too; g = gcd(a, b) divides c).
*Repair:* extend Remark 4.4 to both types with that sentence. (R263 repair applied; numerically confirmed on 3 466 Type I
points p < 1500.)
**D6 (MINOR, scope; Def 5.1 (R3), "Not covered").** (R3) covers only windows built from ℤ[√p]; archimedean data used as
other coordinates (a = ⌊√p⌋, 4ab from CF data, Type I windows, non-window slices) are covered by no relation type, and the
§0 (V5) "candidate (i), CF/Pell part, closed" overstates. *Repair:* add these to "Not covered" and restrict the (V5)
sentence to Type II windows. (R263 repair applied.)
**D7 (MINOR; report ledger line).** "EVIDENCE: cyclotomic depth unbounded" → "EVIDENCE: cyclotomic depth k* (Type II)
even, growing in range (max 72 ≤ 3·10⁵)". (Reported here; the report is the author's — parent should fix the ledger line.)
**D8 (MINOR; Thm 5.2(c), §4.1).** "the image of ⟨primes of K⟩ in H₀/H₀^ℓ" → "the image of K in G/G^ℓ (one residue-symbol
value per ℓ)". (R263 repair applied.)
**D9 (MINOR; Cor 3.3 Assessment).** The "(2^E − 2)/2 − E" need presumes H₀ = (ℤ/m)^×; add "when the primes of K generate
(ℤ/m)^×". Theorem A hypothesis "positive on an open set" can be weakened to d(u₀) > 0 at one real point (cosmetic, no
repair needed).

## Verdict summary
| claim | verdict |
|---|---|
| Theorem A | SOUND (elementary: Gauss + sign) |
| Remark 1.2 | SOUND |
| Cor A.1, Remark 1.3 | SOUND (framing D1) |
| Prop 2.1 | SOUND-AFTER-REPAIRS (D3) |
| Lemma 3.1 | SOUND |
| Prop 3.2 | SOUND (not new: O135 Prop 1.4, D2) |
| Cor 3.3 | SOUND; labels right (D2, D9) |
| §4.1 | SOUND-AFTER-REPAIRS (D4, D8) |
| Prop 4.2 | SOUND |
| Prop 4.3 | SOUND |
| Remark 4.4 | SOUND (Type II); Type I extension needed for 5.2(e) (D5) |
| Theorem 5.2 | SOUND-AFTER-REPAIRS (D1, D5, D6, D8) |
| §6 EVIDENCE | SOUND (reproduced k* = 72, 42, 42; max 22 below 2·10⁴); ledger wording D7 |
No FATAL defect; no mathematical error found in any PROVED statement.
