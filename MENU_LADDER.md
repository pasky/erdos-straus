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
