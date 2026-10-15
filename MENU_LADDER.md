# MENU_LADDER — the genus ladder for root menus at unit-square points (task O245, spark relay Z12)

Status: O245 work in progress (unreviewed). **ES is not solved here; no infinite case of ES for primes is claimed.**
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

## 1. The descent class at μ = 0 is purely 2-adic, and is trivial only for D = 1

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
P₀ = (0, √k) at 2". It survives 2-cover descent iff the x − θ descent images of P₁ and P₀ agree in A ⊗ ℚ₂ — i.e. (D odd)
iff the divisor class [P₁ − P₀] lies in 2J(ℚ₂) for the Jacobian of the hyperelliptic curve w² = φ(Y). For D = 1, A = ℚ,
θ = −k/c₀ and θ(θ − 1) = k·4^J/c₀² is a square in ℚ₂ (k ≡ 1 mod 8): Schinzel / EXPONENT_COVERING Cor 1.5 recovered.

**Computation 1.2 (CERTIFIED by PARI `nfislocalpower`; `scripts/z18_descent2.py c₀ k 10`).** For (c₀, k) ∈ {(3,1),
(15,1), (63,1), (7,9), (31,33), (7,57)} and 2 ≤ D ≤ 10, θ(θ − 1) is a NON-square at some prime of A above 2 in every
case (at D = 9 one component is a square, others are not; for (63,1) and (31,33), (7,57) at D = 4 one component is a
square). So **Y* ∉ Ster(φ) for all D ≥ 2**: Theorem A certifies no sterility of the unit-square point for any root
menu of degree ≥ 2. Heuristic: J(ℚ₂)/2J(ℚ₂) has order ≈ 2^{g + #J[2](ℚ₂)}, so a "random" class lies in 2J(ℚ₂) with
probability ≈ 2^{−g}·… — the genus ladder predicts rarity of descent-sterility, and in the data it is already absent at g = 0
(D = 2), where A ⊗ ℚ₂ is a quadratic algebra and the test is a single Hilbert symbol.

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
with t − t′ of the wrong sign — direct check); (ii) the CRT shape "a constant, m linear" (`scripts/z18_quad.py`) never passes
positivity (0 of 5041–33489 grid points, every tested D and (c₀, k)): for D = 4 directly, b = Y² + pY + q and the cofactor
Y² − pY + p² − q cannot both have real roots (would need 3p² < 4q < p²).

## 3. Witness localisation at μ = 0

**Proposition 3.1 (PROVED).** Let k = 1, c₀ odd squarefree, D ≥ 1, φ = c₀Y^D + 1, β := θ(θ − 1). For a root family through
μ = 0 with witness polynomial f (Type II: f = 4acd − 1; Type I: −d), α := f(θ) must satisfy
  W(f) := Π_{v|2}(α, β)_v = −1, equivalently Π_{v odd, v ∤ c₀} ((β mod v)/v)^{v(α)} = −1.
*Proof.* The first form is MENU_STERILITY Theorem A's computation at μ = 0 (u ≡ 1 at odd S-places where ρ − θ = 1 − θ is
an S-unit, u → 0 at 2; MENU_STERILITY §4.2). Product formula Π_v(α, β)_v = 1: real places of A are the negative real root
(D odd), where β > 0 ⇒ symbol 1. At q | c₀: 1/θ is a root of x^D + c₀, Eisenstein at q, so q is totally ramified with
uniformiser ϖ = 1/θ and β = ϖ^{−2}(1 − ϖ); the tame symbol (α, β)_𝔮 = ((−1)^{v(α)v(β)} α^{v(β)} β^{−v(α)} mod 𝔮 / 𝔮) has
v(β) = −2, so it equals ((1 − ϖ)^{−v(α)} mod 𝔮 / 𝔮) = 1. At the remaining odd v, β is a unit (N(θ − 1) = ±16/c₀) and the
symbol is ((β mod v)/v)^{v(α)}. ∎
`scripts/z18_witness2.py` evaluates W(f) with PARI `nfhilbert`; O240 Theorem B's witness gives W = −1 (2-part −1,
c₀-part +1, other odd −1), its sign-flipped constant gives +1. **Reading:** the witness condition is a coin-flip parity over
the primes of Res(f, φ); it does not obstruct anything structurally (consistent with §1).

## 4. The first two rungs: D = 1 and D = 2 are sterile at μ = 0 (Type II)

**Theorem 4.1 (PROVED).** Let c₀, k > 0, k ≡ 1 (mod 8), c₀ + k = 4^J, n = c₀Y² + k. Every Type II polynomial family on n
(a, b, c, d ∈ ℚ[Y] with positive leading coefficients, cn = 4abcd − a − b) is *non-escaping*: its witness f = 4acd − 1 is
≡ a rational constant f₀ (mod n) in ℚ[Y]. Consequently no Type II root family of degree D = 2 (Y = 2^{s/2}, i.e. the
family c₀·4^t + k with Y = 2^t) contains μ = 0 in the closure of its class.
*Proof.* m := 4abd − n = (a + b)/c ∈ ℚ[Y] has positive leading coefficient. If deg(abd) > 2 then deg m = deg(abd) ≤
max(deg a, deg b), forcing (say) a, c, d constant and b ∝ n + const of degree 2 — contradiction; if deg(abd) < 2 then
lc(m) = −c₀ < 0. So deg(abd) = 2, deg m ≤ 1. Shapes (deg a, deg b, deg d), up to a ↔ b:
(0,0,2): m | a + b constant ⇒ m, c constant; f = c(n + m)/b − 1 ≡ cm/b − 1 (mod n).
(2,0,0): m constant ⇒ a = (n + m)/(4bd), c = (a + b)/m ≡ (m/(4bd) + b)/m (mod n) is ≡ a constant, so f = c(n + m)/b − 1 ≡ const. m linear with root Y₀: a(Y₀) = −b and
4a(Y₀)bd = n(Y₀) give −4b²d = n(Y₀) > 0, impossible (b, d positive constants).
(1,1,0): m constant: at the root of a, n + m = 0, impossible (n, m > 0). m linear with root Y₀: n(Y₀) = 4a(Y₀)b(Y₀)d =
−4d·a(Y₀)² ≤ 0, impossible.
(1,0,1): at the root Y_a of a, m(Y_a) = −n(Y_a) < 0; but m is a positive constant, or linear with c = (a + b)/m constant
and m(Y_a) = b/c > 0. Impossible.
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
| 3, ≥ 5 odd | genus ≥ 1 | finitely many (Siegel) | silent | (15,1): no family found (EVIDENCE §5) |
| 4 | genus 1 | finitely many | silent | yes for (3,1), (7,9), (23,41), (39,25) (SG, O239/O240); no z14 window for (15,1), (31,33), (7,57), (63,1), (47,17), (55,9) (O239 Cor 2.8) |
So the ladder's first two rungs are sterile for structural reasons (Schinzel at D = 1, positivity at D = 2), and the
rung where escapes appear (D = 4) is the first where BOTH the integer T1 points become finite AND a factorisation supply
(Sophie Germain) exists in base 2 (Aurifeuille: only 4X⁴ + 1 among binomials, Capelli).
