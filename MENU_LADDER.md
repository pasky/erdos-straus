# MENU_LADDER — the genus ladder for root menus at unit-square points (task O245, spark relay Z12)

Status: O245; hostile review R255 (reviews/menu-ladder-review.md), repairs marked '(R255 repair)'. **ES is not solved here; no infinite case of ES for primes is claimed.**
Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z18_*.md`; scripts `scripts/z18_*`.
Builds on MENU_STERILITY (O240: Theorem A witness reciprocity, Props 4.1, 4.3, 5.1), EXP_105 (O239: Prop 2.4–2.8,
ES for all 7·4^s + 9), EXPONENT_COVERING ((J)22 Thm 1.4, Cor 1.5), NEAR_SQUARE ((J)55 Thm 2.2, 3.3, 3.4).

## 0. Iteration log
(I1) Setting. n_s = c₀·2^s + k with c₀ + k = 4^J (k ≡ 1 mod 8) has the profinite unit-square point μ = 0 (s → 0 in Ẑ:
n → 4^J at odd places, n → k at 2). A *root menu of degree D* is the set of identities polynomial in Y = 2^{s/D}
(n = c₀Y^D + k, valid for s ≡ 0 mod some L with D | L). Every exponential identity (parameters Σ q_i 2^{a_i s/L}) at μ = 0
is in some root menu, and root menus increase along divisibility of D. Near μ = 0: **Y → 1 at every odd place, Y → 0 at 2.**
(I2) First test of the brief's prediction ("for D ≥ 5 the Theorem-A descent obstruction disappears"): it disappears
already at **D = 2** for every family tested (§1). So the genus ladder is NOT what blocks 15·2^s + 1: the descent
obstruction lives only at D = 1. Steering consequence: the gap between Theorem A (⊇) and actual sterility must be
explained by something else — degree/shape constraints of polynomial ES families (ET Lemma 2.8, NEAR_SQUARE Thm 2.2) and
the finiteness of factorisation supply (Capelli). §2–§3 set up an exact normal form and a search for D ≥ 3.

## 1. The descent class at μ = 0 is purely 2-adic, and (tested D ≤ 10) obstructs only at D = 1

**Proposition 1.1 (PROVED).** Let φ(Y) = c₀Y^D + k (c₀, k > 0, c₀ + k = 4^J, k ≡ 1 mod 8), A = ℚ[Y]/(φ), θ = class of Y,
and let Y* ∈ Ẑ be the point Y* = 1 in ℤ_ℓ (ℓ odd), Y* = 0 in ℤ₂. Then Y* ∈ Ster(φ) (MENU_STERILITY Theorem A) iff
θ(θ − 1) ∈ (A ⊗ ℚ₂)^{×2}.
*Proof.* φ(Y*) = 4^J at odd ℓ and = k ≡ 1 (8) at 2: condition (i) holds. (ii): if γ(Y* − θ) = γ(1 − θ) is a square in
A ⊗ ℚ_ℓ for every odd ℓ, then γ(1 − θ) is a global square in every component field of A (an element of a number field that
is a local square at all but finitely many places is a square: Chebotarev applied to K(√·)/K; no Grunwald–Wang exception for
exponent 2). So γ ∈ (1 − θ)·A^{×2}; it is totally positive because the real roots of φ are negative (D odd) or absent
(D even) and 1 − θ > 0 there. Condition (ii) at ℓ = 2 then reads (1 − θ)(0 − θ) ∈ (A ⊗ ℚ₂)^{×2}. Conversely
γ := 1 − θ works if that holds. ∎
*Reading.* Y* is the glued adelic point "rational point P₁ = (1, 2^J) of w² = φ(Y) at odd places, rational point
P₀ = (0, √k) at 2" (P₀ is ℚ₂-rational; ℚ-rational iff k is a square). It survives 2-cover descent iff the x − θ descent images of P₁ and P₀ agree in A ⊗ ℚ₂ — i.e. (D odd)
iff the divisor class [P₁ − P₀] lies in 2J(ℚ₂) for the Jacobian of the hyperelliptic curve w² = φ(Y). For D = 1, A = ℚ,
θ = −k/c₀ and θ(θ − 1) = k·4^J/c₀² is a square in ℚ₂ (k ≡ 1 mod 8): Schinzel / EXPONENT_COVERING Cor 1.5 recovered.

**Computation 1.2 (CERTIFIED by PARI `nfislocalpower`; `scripts/z18_descent2.py c₀ k 10`).** For (c₀, k) ∈ {(3,1),
(15,1), (63,1), (7,9), (31,33), (7,57)} and 2 ≤ D ≤ 10, θ(θ − 1) is a NON-square at some prime of A above 2 in every
case (at D = 9 one component is a square, others are not; for (63,1) and (31,33), (7,57) at D = 4 one component is a
square). So **Y* ∉ Ster(φ) for every tested (c₀, k) and 2 ≤ D ≤ 10** (CERTIFIED; all D ≥ 2: CONJECTURE, R-O245 repair):
Theorem A certifies no sterility of the unit-square point for these root menus. Heuristic (D odd): J(ℚ₂)/2J(ℚ₂) has order #J(ℚ₂)[2]·2^g (R255 repair: formula corrected), so a "random" class lies in 2J(ℚ₂) with
probability ≈ 2^{−g}·… — the genus ladder predicts rarity of descent-sterility, and in the data it is already absent at g = 0
(D = 2), where A ⊗ ℚ₂ is a quadratic algebra.

*Hand check (D = 2, c₀ = 15).* θ = ±σ/15 with σ = √−15 ∈ ℤ₂ (−15 ≡ 1 mod 16), σ ≡ −7 (mod 32) for one root; then
θ(θ − 1) = −(1 ± σ)/15 has v₂ = v₂(1 + σ) = 1 resp. v₂(1 − σ) = 3 in the two components — odd, so a non-square in both ✓.

*Consequence (steering).* O239's Prop 2.7 (no z14 window at μ = 0 for (15,1), …) and NEAR_SQUARE-type degree arguments are
**finer** than descent: they use the specific shape of the menu, not the adelic point. The genus ladder therefore has to
be climbed by *shapes*, not by descent.

## 2. Exact normal form and the specialisation lemma

**Lemma 2.1 (specialisation; PROVED).** Let R ∈ ℚ[Y]. For Y = 2^{s/D}, R(Y) ∈ ℤ for every s in some clopen neighbourhood
of μ = 0 (s ≡ 0 mod L, s ≥ s₀) iff R(1) ∈ ℤ[1/2] and R(0) ∈ ℤ_(2).
*Proof.* Write R = R₁/N, R₁ ∈ ℤ[Y]. For odd ℓ^e ∥ N, Y ≡ 1 (mod ℓ^e) once ord_{ℓ^e}(2) | s/D, so R₁(Y) ≡ R₁(1); for 2^e ∥ N,
Y ≡ 0 (mod 2^e) once s ≥ eD, so R₁(Y) ≡ R₁(0). Conversely the clopen set contains such s, and R₁(Y) ≡ R₁(1) resp. R₁(0)
there. ∎ So a polynomial family is valid near μ = 0 iff its parameters are positive for large Y and their values at the two
*specialisations* Y = 1 (the member s = 0, n = c₀ + k = 4^J) and Y = 0 (the 2-adic limit, n = k) are ℤ[1/2]- resp.
ℤ_(2)-integral. The specialisations are rational "solutions" for n = 4^J (with 2-power denominators allowed) and n = k (with
odd denominators allowed): **no local obstruction exists at either specialisation**; any obstruction is global-algebraic.

**Lemma 2.2 (normal form of Type II families; PROVED, algebra).** Every Type II family x = abd, y = acdn, z = bcdn
(polynomials, 4abcd − a − b = cn) satisfies n + m = 4abd, a + b = cm with m := 4x − n ∈ ℚ[Y]. If a = λ is constant, put
σ := c/λ, T := 4λ²d, T′ := m: then
   **n = σ·T·T′ − T − T′**, b = λ(σT′ − 1), witness f = 4acd − 1 = σT − 1, f′ = σT′ − 1,
and conversely every polynomial solution (σ, T, T′) of this equation with positive leading coefficients gives a family.
(Check: 4abd = (σT′ − 1)T = n + T′.) Windows (Lemma 1.1, z14, Theorem B) are the case T′ = m constant.

**Lemma 2.3 (real-place constraint; PROVED).** In Lemma 2.2, at a real root t of T, n(t) = −T′(t); at a real root t′ of T′,
n(t′) = −T(t′). Hence if D is even (n > 0 on ℝ), T and T′ have no common-sign escape: let t* be the largest real root of TT′,
say of T; then T′(t*) ≥ 0 (positive leading coefficient, t* ≥ its real roots), so n(t*) ≤ 0 — impossible. **For even D,
T and T′ have no real roots.** For odd D all real roots of TT′ are ≤ the real root of n.
Consequences: (i) T, T′ both linear is impossible for every D (for odd D the two roots force opposite signs of n(t), n(t′)
with t − t′ of the wrong sign — direct check; (R255 repair) a common root t = t′ would be the real root −(k/c₀)^{1/D} of n,
rational only if k = gu^D, c₀ = gv^D, and then g(u^D + v^D) = 4^J with g, u, v odd, D odd forces u + v = 2^{2J}/g with odd
cofactor 1, so u = v = 1, 2g = 4^J — impossible); (ii) (R255 repair: label split — PROVED for even D, since m linear has a
real root; EVIDENCE for odd D) the CRT shape "a constant, m linear" (`scripts/z18_quad.py`) never passes
positivity (0 of 5041–33489 grid points, every tested D and (c₀, k); R255: the positivity counter is not in the committed script, numbers not reproducible as committed): for D = 4 directly, b = Y² + pY + q and the cofactor
Y² − pY + p² − q cannot both have real roots (would need 3p² < 4q < p²).

## 3. Witness localisation at μ = 0

**Proposition 3.1 (PROVED).** Let k = 1, c₀ odd squarefree, D ≥ 1, φ = c₀Y^D + 1, β := θ(θ − 1). For a root family through
μ = 0 with witness polynomial f (Type II: f = 4acd − 1; Type I: −d), α := f(θ) must satisfy
  W(f) := Π_{v|2}(α, β)_v = −1, equivalently Π_{v odd, v ∤ c₀} ((β mod v)/v)^{v(α)} = −1.
*Proof.* The first form is MENU_STERILITY Theorem A's computation at μ = 0 (u ≡ 1 at odd S-places where ρ − θ = 1 − θ is
an S-unit, u → 0 at 2; MENU_STERILITY §4.2). Product formula Π_v(α, β)_v = 1: real places of A are the negative real root
(D odd), where β > 0 ⇒ symbol 1. At q | c₀: 1/θ is a root of x^D + c₀, Eisenstein at q, so q is totally ramified with
uniformiser ϖ = 1/θ and β = ϖ^{−2}(1 − ϖ); the tame symbol (α, β)_𝔮 = ((−1)^{v(α)v(β)} α^{v(β)} β^{−v(α)} mod 𝔮 / 𝔮) has
v(β) = −2, so it equals ((1 − ϖ)^{−v(α)} mod 𝔮 / 𝔮) = 1. At the remaining odd v, β is a unit (N(θ − 1) = ±4^J/c₀, standing hypothesis c₀ + 1 = 4^J) and the
symbol is ((β mod v)/v)^{v(α)}. ∎
`scripts/z18_witness2.py` evaluates W(f) with PARI `nfhilbert`; O240 Theorem B's witness gives W = −1 (2-part −1,
c₀-part +1, other odd −1), its sign-flipped constant gives +1. **Reading:** the witness condition is a coin-flip parity over
the primes of Res(f, φ); for unconstrained f it is not an obstruction (heuristic reading: within constrained shapes it may
still bite).

## 4. The first two rungs: D = 1 and D = 2 are sterile at μ = 0 (Type II)

**Theorem 4.1 (PROVED).** Let c₀, k > 0, k ≡ 1 (mod 8), c₀ + k = 4^J, n = c₀Y² + k. Every Type II polynomial family on n
(a, b, c, d ∈ ℚ[Y] with positive leading coefficients, cn = 4abcd − a − b) is *non-escaping*: its witness f = 4acd − 1 is
≡ a rational constant f₀ (mod n) in ℚ[Y]. Consequently no Type II root family of degree D = 2 (Y = 2^{s/2}, i.e. the
family c₀·4^t + k with Y = 2^t) contains μ = 0 in the closure of its class.
*Proof.* m := 4abd − n = (a + b)/c ∈ ℚ[Y] has positive leading coefficient. If deg(abd) > 2 then deg m = deg(abd) ≤
max(deg a, deg b), forcing (say) a, c, d constant and b ∝ n + const of degree 2 — contradiction; if deg(abd) < 2 then
lc(m) = −c₀ < 0. So deg(abd) = 2 and deg m ≤ 2. (R-O245 repair: deg m = 2 occurs, e.g. a = (n + 1)/3, b = c = d = 1. Then
m | a + b forces a or b quadratic, so the shape is (2,0,0) and c is constant; (4bcd − 1)a = cn + b gives a ≡ b/(4bcd − 1),
hence f = 4acd − 1 ≡ const (mod n); 4bcd − 1 ≠ 0 since else cn + b = 0.) For deg m ≤ 1, the four shapes up to a ↔ b:
(0,0,2): m | a + b constant ⇒ m, c constant; f = c(n + m)/b − 1 ≡ cm/b − 1 (mod n).
(2,0,0): m constant ⇒ a = (n + m)/(4bd), c = (a + b)/m ≡ (m/(4bd) + b)/m (mod n) is ≡ a constant, so f = c(n + m)/b − 1 ≡ const. m linear with root Y₀: a(Y₀) = −b and
4a(Y₀)bd = n(Y₀) give −4b²d = n(Y₀) > 0, impossible (b, d positive constants).
(1,1,0): m constant: at the root of a, n + m = 0, impossible (n, m > 0). m linear with root Y₀: n(Y₀) = 4a(Y₀)b(Y₀)d =
−4d·a(Y₀)² ≤ 0, impossible.
(1,0,1): at the root Y_a of a, m(Y_a) = −n(Y_a) < 0; but m is a positive constant, or linear with c = (a + b)/m constant
and m(Y_a) = b/c > 0. Impossible.
(R255 repair) The reduction "up to a ↔ b" is legitimate because (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1
≡ 1 (mod n): f ≡ const iff 4bcd − 1 ≡ const, and f₀ ≠ 0.
So f ≡ f₀ ∈ ℚ (mod n) whenever a family exists. Then (f(Y)/n(Y)) = (f₀′/n(Y)) (f₀′ = numerator·denominator of f₀) is a
Kronecker character of n(Y); near μ = 0, n(Y) → 4^J at odd places and → k ≡ 1 (8) at 2, a profinite unit square, so the
symbol is +1, contradicting the Type II witness lemma (NEAR_SQUARE Lemma 1.3: = −1). ∎
*Scope.* Type II only; the Type I analogue (NEAR_SQUARE Thm 2.2's (0,0,2)/(1,0,1)/(0,1,1) analysis transplanted to
c₀Y² + k) is not written — (0,0,2) goes through verbatim, (1,0,1) needs NEAR_SQUARE's Λ-argument redone: open.
*Not T1.* The rung-2 obstruction is archimedean (positivity), not integral-point: Y* is NOT in the profinite closure of the
Pell points 15Y² + 1 = w² (Y_j ≡ 1 mod 17 forces j odd, hence Y_j odd; `scripts/z18_pell.py`), and Y* ∉ Ster (§1).

**Corollary 4.2 (the ladder at unit-square points; PROVED/EVIDENCE as marked).**
| D | curve w² = c₀Y^D + k | integer T1 points | descent at μ = 0 | root menu reaches μ = 0? |
|---|---|---|---|---|
| 1 | line | dense (Schinzel) | obstructs (Prop 1.1) | no (PROVED, Cor 1.5) |
| 2 | conic (Pell) | infinitely many, not dense at Y* (c₀ = 15) | silent | no for Type II (Thm 4.1) |
| 3, ≥ 5 | genus ≥ 1 | finitely many (Siegel) | silent for tested D ≤ 10 (CERTIFIED) | (15,1): no family found at D = 3, 5, 6, 8 (EVIDENCE §5) |
| 4 | genus 1 | finitely many | silent | yes for (3,1), (7,9), (23,41), (39,25) (SG, O239/O240); no z14 window for (15,1), (31,33), (7,57), (63,1), (47,17), (55,9) (O239 Cor 2.8, base 4, unsplit SG pieces, pending review; R255 repair: base-4 non-existence implies base-2 non-existence near μ = 0 for the corresponding sub-menu via s ↦ 2s) |
So the ladder's first two rungs are sterile for structural reasons (Schinzel at D = 1, positivity at D = 2 — Type II only), and the
rung where escapes appear (D = 4) is the first where BOTH the integer T1 points become finite AND a factorisation supply
(Sophie Germain) exists in base 2 (Aurifeuille: only 4X⁴ + 1 among binomials, Capelli).

## 5. Searching the higher rungs for 15·2^s + 1 (EVIDENCE, negative)
Coverage caveats (R-O245): `z18_tt.py` skips underdetermined and zero-resultant systems; `z18_crt.py` uses the reduced
residue m = −n mod a₁b₁ only (no added multiples of a₁b₁). All searches test exactly Lemma 2.1 (+ positivity), so a hit would be a valid family near μ = 0; every hit would then be
re-verified on actual s. Sanity: `z18_crt.py 3 1 4 0 2 3 <r-list>` recovers O240 Theorem B (b₁ = Y² + 2Y + 2, r = 1/6, λ = 3)
and its mirror (b₁ = Y² − 2Y + 2, λ = 5).
* `z18_crt.py` (Type I and II; a₁, b₁ primitive with |coeff| ≤ 3, deg a₁ ≤ 1, deg b₁ ≤ 4, m = −n mod a₁b₁ resp.
  e = −n⁻¹ mod a₁b₁ forced, ratio r forced or from {p/q ≤ 16}): (15,1), D ∈ {3,4,5,6,8}: **0 hits** (up to 211 230 pairs per D).
* `z18_quad.py` (a constant, b quadratic with rational (p, q) of height ≤ 12, m linear): 0 hits for (3,1), (7,9), (15,1),
  D = 3…7 — explained by Lemma 2.3 (positivity never holds; R255: proved for even D, EVIDENCE for odd D).
* `z18_tt.py` (exact normal form n = σTT′ − T − T′, T′ = S·T₁, T = r + U·T₁, (U, S) solved by resultants; also Type I
  nT′ + 1 = T(σT′ − 1); T₁ quadratic |coeff| ≤ 4–6, also with Y ↦ 2^{±1}Y, 2^{−2}Y rescaling): (15,1) D = 4: 110–148
  exact algebraic families, **0 integral at μ = 0** (failures mostly at the 2-adic specialisation Y = 0); D = 5, 8: no
  algebraic solutions in range; D = 6: 4 algebraic, 0 integral; T₁ cubic, D = 6, 8: none. The D = 4 constant-σ solutions
  with σ = 4/11 are the Sophie-Germain Type II in disguise (a = 11, c = 4: cn + a = 15(4Y⁴ + 1)); their failure is the
  O239 Cor 2.8 magnitude obstruction (worked: κ ≡ −1 mod 16·11 with κ | 75 has no solution).
**Status of 15·2^s + 1: NOT decided.** Rungs 1, 2 are PROVED sterile at μ = 0 (Type II for rung 2); the window part of
rung 4 is PROVED sterile (O239); everything else searched is empty at the stated heights (EVIDENCE only).

## 6. Goal (2): the exponential analogue of Theorem 1.4

Setting: n_s = c₀b^s + k, Λ ⊂ Ẑ the closure of the exponents, divisor classes D_q as in EXPONENT_COVERING. A *root class*
F of degree D on s ≡ r (mod L) (D | L) is a polynomial Type I/II family in Y = b^{(s−r)/D}. For μ ∈ Ẑ with μ ≡ r (L) let
Y*(μ) ∈ Ẑ be Y*_ℓ = b^{(μ−r)/D} (ℓ ∤ b), Y*_ℓ = 0 (ℓ | b).
**Lemma 6.1 (PROVED; Lemma 2.1 verbatim).** F is integral at all large s near μ iff all its parameters are integral at Y*(μ);
the set V_F of such μ is clopen.
**Theorem 6.2 (PROVED; compactness, as Thm 1.4).** For some sufficiently large s₀ (R-O245 repair), {n_s : s ≥ s₀} has a finite covering by ET, divisor and root classes iff
every μ ∈ Λ lies in some D_q or some V_F with F positive.
**Proposition 6.3 (PROVED; Theorem A).** V_F ∩ S_D = ∅ for every degree-D root class, where S_D := {μ : Y*(μ) ∈ Ster(φ_D)}.
(R255 repair: Theorem A is stated for residue classes of u; if μ ∈ V_F then every parameter is integral on the full class
u ≡ Y*(μ) mod N (N clearing denominators), positive for large u, whose closure contains Y*(μ); S_D = S_{D,r} uses
φ_{D,r} = c₀b^r Y^D + k.) Hence Λ ∩ (∩_D S_D) \ ∪_q D_q ≠ ∅ ⟹ no covering. (Note ∩_D S_D ⊆ S_1 = Sq^×-points.)
**The pointwise converse fails for natural sub-menus (PROVED; R-O245 repair: scope narrowed).** O240 spark 6 / O238 spark 2
asked whether a covering exists iff Λ avoids ∩_D S_D. Pointwise version: "every μ ∉ ∩_D S_D ∪ ∪_q D_q lies in some V_F".
For the menu "ET + divisor + z14 windows" this is FALSE: for 15·4^s + 1, μ = 0 ∉ S_2, S_4 (Computation 1.2), μ = 0 is in no
D_q (n → 16 at odd q), yet O239 Cor 2.8 (unsplit SG pieces; branch side-agent/exp-105, pending review) proves no z14 window
reaches μ = 0. (R255 repair: the former clause "this also refutes the finite-cover equivalence for that menu" is withdrawn —
it would need that no μ ≠ 0 of Λ lies in ∩_D S_D \ ∪_q D_q, e.g. that μ = 0 is the only profinite unit-square point of
15·4^μ + 1; EVIDENCE only: the primes of 4^60 − 1 force μ ≡ 0 mod 60, `scripts/review_r255_s1points.py`.) For the *Type II part* of the degree-2 rung the pointwise per-rung statement
(reachable iff ∉ S_2) is FALSE at μ = 0 (Theorem 4.1); for the full rung 2 (Types I and II) it is open (Type I half of
Thm 4.1 missing). The global version for all root classes is open; at μ = 0 of (15,1) it is CONJECTURE 6.4's negation.
So per-rung sterile sets *contain* S_D together with positivity-forced points (Thm 4.1, Lemma 2.3) and, for finite
sub-menus, magnitude-forced points (O239 Cor 2.8, MENU_STERILITY Prop 4.3); no classification is claimed.
**CONJECTURE 6.4 (ladder-sterility of (15,1); Assessment, weak).** μ = 0 of 15·2^s + 1 is not reached by any root class
of any degree. Evidence: §5 (empty searches), the failure of every SG window (O239), and the 2-adic failure pattern of all
D = 4 algebraic families. Counter-evidence: no structural obstruction is known for D ≥ 3 (descent silent, T1 finite, witness
parity a coin flip). If true, 15·2^s + 1 would be the first family proved immune to every exponential-polynomial covering;
proving it needs a positivity/size theorem for all shapes, which this file only has at D ≤ 2.

## 7. Goal (3): where the ladder stops for primes

**Proposition 7.1 (valuation slices collapse to ET; PROVED, elementary; R-O245 repair: scope narrowed).** Let
g(n) = 2^{v₂(n−1)} (defined at every odd n; the exponential families c₀2^s + 1 are the slices u := (n − 1)/g(n) = c₀) and let
F be a Type I/II identity polynomial in (n, g) with positive values. Suppose F is valid on a set containing, for some
e ≥ 3, the FULL slice progression P_e = {n ≡ 1 + 2^e u₀ (mod 2^e M), v₂(n − 1) = e} (u₀ odd). Then F restricted to P_e is a
polynomial-in-n identity on an arithmetic progression, so P_e must contain no odd square coprime to its modulus (R255
repair: primitivity needed — n ≡ 0 mod 3 ∋ 9 is polynomially solvable) (Schinzel/Mordell, ET p. 7–8;
Type I/II solutions do not exist at squares, ET Prop 1.6). Near a profinite unit-square point (u₀ ≡ c₀, e ≡ 0 mod
ord_M(2)·L) P_e does contain odd squares (1 + 2^e c₀ ≡ 4^J mod odd M; ≡ 1 mod 8 at 2), contradiction. ∎
So (n, g)-polynomial families whose valid sets contain full slice progressions cannot reach unit-square points; the
exponential families escape precisely because their valid set meets each slice in a single n (u frozen).
**Answer to (3) (Assessment; R-O245: downgraded from PROVED).** Prop 7.1 + MENU_STERILITY Prop 5.1 (finitely many thin
items miss a positive density of primes near (J)54 points) suggest that the ladder stops at the first rung that must see a
positive-density prime set: a Y-type parameter decouples the 2-adic and odd specialisations only while the rest of n is
frozen or thin. This is not a classification: arbitrary auxiliary functions g (fibres not progressions) are not covered,
and the claim that only divisor data (B2) or norm-form data ((J)3, T1 on square-compatible classes) remain is a reading,
not a theorem.

## 8. Spark explored: s-deformation
Exponential-polynomial parameters P(s, 2^{s/D}) with P ∈ ℚ[s, Y]: by Lemma 2.1 integrality near μ = 0 depends only on
P(0, 1), P(0, 0), while positivity is decided at s → ∞ — so s-dependence *decouples integrality from positivity*.
*Rung 2 stays closed (PROVED, Type II; R-O245 reviewer argument).* Theorem 4.1 applied for each fixed large s shows the
remainders f mod n = F(s) and (4bcd − 1) mod n = G(s) are constant in Y; they lie in ℚ[s] (division by n = c₀Y² + k, which is
s-free, creates no s-denominators), and f·(4bcd − 1) = 4c²dn + 1 ≡ 1 gives F·G = 1 in ℚ[s], so F, G are constants and the
fixed-character contradiction of Thm 4.1 applies. *Higher rungs:* for windows polynomiality in s forces m(s) | (a + b)
coefficientwise in Y (impossible for SG pieces Q±(s, Y), t(s)); for the a-constant SG Type II, d = (κQ + 1)/(4ac) is polynomial
in s only if ac is constant, which freezes t. Assessment: no gain found; a polynomial-curve statement on the D ≥ 3 shape
varieties is open (spark).
