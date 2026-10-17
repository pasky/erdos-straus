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
