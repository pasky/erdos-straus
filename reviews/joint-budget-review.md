# R263 — hostile review of O254 (JOINT_BUDGET.md)

Reviewer: R263 side agent (branch side-agent/review-joint-budget). Author branch merged: side-agent/joint-budget.
From-scratch scripts: `scripts/review_r263_*.py` (none of the author's z26 code reused).

## Verdict summary
(in progress)

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
