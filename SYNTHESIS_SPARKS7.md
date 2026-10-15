# SYNTHESIS_SPARKS7 — cross-combinations of wave Z, second half ((J)64–(J)77) (task O247, synthesis VII)

Status: O247 checkpoint 1 (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.** Labels as
in DISCOVERIES.md. Memos `BRAINSTORM/s7_*.md`; scripts `scripts/s7_*`.

## 0. Iteration log
(I1) Mandatory (i), forced budgets × primes. Made exact: the least cap-0 window is m₀(p) = 4·x_min(p) − p (x_min the least
first denominator of any ES decomposition; Type I has 4x − p ≥ 3p). Construction attempt 1: force the budget by congruences
(ℓ | K_m ⟺ p ≡ −m (ℓ)) — gives ET classes (B1). Attempt 2: force it algebraically at positive density through norm forms
(p = a² + b²). The Gaussian window m = 2AB + 2A + 2B + 1 has K_m = ((A + B + 1)/2)², a square, at every p ≡ 1 (4): a
positive-density forced budget does exist — but at windows of size ≍ p, where cap 0 is a 1/m residue lottery (B3), and it
fires at the same rate as random windows of that size (s7_gaussian_square_windows). Attempt 3: small windows with algebraic
structure in the binary-form coordinates — killed completely by Theorem 1.1 below (the norm-form rung collapses).
(I2) Statistics of m₀: a conditional permutation test shows the inter-window correlations are exactly the shared small-prime
(congruence) data; rough parts behave as independent draws (§2). Mordell's theorem is "m₀ ∈ {3, 7} off the six classes".
(I3) Mandatory (ii): forced witness + forced small primes certify caps on congruence classes (Lemma in s7_certified_caps);
cap ≤ 1 on Haar ≈ 0.93–0.96 of the first undecided line lnr = 17, but the same window data already give cap 0 on Haar-almost
all of the line; the forced mechanism is blind exactly at the r-generic (sterile-candidate) points, where no window is forced.
(I4) Mandatory (iii): fixed windows on the r-generic line are M17's U/U⁻¹ boxes, with a reciprocity parity law (the ℤ-twin of
(J)67); level-1 survivor sets reproduce STERILE_LOWER Comp 4.1 exactly at r = 19, 23. No finite certificate: deep levels
reduce to ES solutions of 4/17^c (M17D wall), and the only self-map (char-3 Frobenius) is exactly critical.
(I5) Mandatory (iv): over F_q[T] the Sophie-Germain/Carlitz idea cannot help with an open target (Baire), and the inseparable
"Frobenius digit" menu collapses to Galois conjugation (s7_ff_nonlinear).
(I6) Own (v): while screening norm-form windows, the degree argument of §1 turned out to settle the open question left by
POINTWISE_BINARYFORM §5 (Type I families with non-constant level; O145) and to remove the cone/definiteness hypotheses
of its Prop 5.2 for Type II. → deep item 1.

## 1. Deep item 1: the binary-form rung collapses (PROVED)

Setting. Q ∈ ℚ[u, v] a binary quadratic form that is irreducible over ℚ (non-square discriminant; definite or indefinite).
A *polynomial Type II (resp. Type I) family for Q* is a quadruple A, B, C, D ∈ ℚ[u, v] ∖ {0} with
  (II) 4ABCD = A + B + C·Q,      resp.      (I) 4ABCD = Q·(A + B) + C
identically (ET's Σ^{II}_n, Σ^{I}_n at n = Q(u, v); POINTWISE_MORDELL17 §2), the ET coordinates (a, b, c, d) of a solution
x, y, z of 4/n (POINTWISE_BINARYFORM §1). Notation: α, β, γ, δ = total degrees of A, B, C, D; X_top = top-degree part;
s = α + β + γ + δ = deg(4ABCD).

**Theorem 1.1 (Type II; PROVED, elementary).** For every polynomial Type II family for Q that is valid (A, B, C, D > 0) at
one point, A, B, C, D ∈ ℚ[Q]. Hence x = abd, y = acdn, z = bcdn are polynomials in n: the family is an ET identity in n.
*Proof.* deg(A + B + CQ) ≤ max(α, β, γ + 2), so s ≤ max(α, β, γ + 2).
(a) s ≤ α. Then β = γ = δ = 0 and A(4BCD − 1) = B + CQ. If 4BCD = 1 then B + CQ = 0, impossible (C ≠ 0, Q non-constant).
So A = (B + CQ)/(4BCD − 1) ∈ ℚ[Q]. (s ≤ β is symmetric.)
(b) s > α, β. Then A, B do not reach degree s, so the degree-s part of A + B + CQ is that of CQ; as the left side has exact
degree s, γ + 2 = s, i.e. α + β + δ = 2, and 4A_top B_top D_top = Q (top parts). Q is irreducible over ℚ, so exactly one of
A_top, B_top, D_top has degree 2 and the others are constants.
 (b1) D quadratic, A, B constant: C(4ABD − Q) = A + B, and A + B > 0 by validity, so C is a constant and
 D = (Q + (A + B)/C)/(4AB) ∈ ℚ[Q].
 (b2) A quadratic, B, D constant (γ ≥ 1 since s > α = 2): C(4BDA − Q) = A + B. E := 4BDA − Q has degree ≤ 1 (tops cancel)
 and E ≠ 0 (else A + B = 0). deg(A + B) = 2 = γ + deg E. If γ = 1, E is linear and Q + 4B²D = E(4BDC − 1), so Q (the
 degree-2 part) would be a product of two rational linear forms: impossible. So γ = 2, E is a constant, A = (Q + E)/(4BD) and
 C = (A + B)/E lie in ℚ[Q]. (B quadratic: symmetric.) ∎
*Remark.* Positivity is used only in (b1) (A + B ≠ 0); without it there is the degenerate family A = −B = κ, D = −Q/(4κ²), C
arbitrary, which is never valid. This removes both the cone and the definiteness hypotheses of POINTWISE_BINARYFORM Prop 5.2
and avoids O145 Prop 3.2.

**Theorem 1.2 (Type I, any level; PROVED, elementary).** Let a polynomial Type I family for Q be valid at all points of a
lattice coset lying in an open cone Γ (outside a bounded set), as in POINTWISE_BINARYFORM Thm 3.2 (A_F ≠ ∅). Then
A, B, C, D ∈ ℚ[Q]: the family is an ET identity in n.
*Proof.* Positivity on the cone: for directions θ in a non-empty open arc I ⊂ Γ (avoiding the finitely many zero directions
of the top parts involved and of Q), A_top(θ), B_top(θ), C_top(θ), D_top(θ), Q(θ) > 0 (each coordinate is ~ |P|^{deg}·X_top(θ)
along valid points P → ∞ in direction θ, and Q(P) = n > 0). Consequently no top-degree cancellation occurs in A + B or in
Q(A + B) + C. Put μ = max(α, β), so deg(A + B) = μ and s = deg(Q(A + B) + C) = max(μ + 2, γ).
(a) γ > μ + 2. Then s = γ, so α = β = δ = 0, μ = 0, and C(4ABD − 1) = Q(A + B) has degree 2 < γ (or 4ABD = 1 and
Q(A + B) = 0): impossible.
(b) γ = μ + 2 = s. Then α + β + δ = 2 − γ + … gives α + β + δ = μ, so (α ≥ β, wlog α = μ) β = δ = 0 and α + 0 + 0 = μ: then
s = μ + β + γ + δ = γ forces μ + 2 = γ = s = α + γ, so α = 0, γ = 2: A, B, D constants and C = Q(A + B)/(4ABD − 1) ∈ ℚ[Q].
(c) γ < μ + 2 = s. Wlog α = μ. Then β + γ + δ = 2 and 4A_top B_top C_top D_top = Q·(A + B)_top.
 (c1) α > β: (A + B)_top = A_top, so 4B_top C_top D_top = Q; one of B, C, D is quadratic with top ∝ Q, the others constants.
  • B quadratic (α ≥ 3): A·E = QB + C with E := 4BCD − Q of degree ≤ 1, E ≠ 0 (else QB + C = 0). deg(QB + C) = 4 = α + deg E.
    α = 4: E constant, B = (Q + E)/(4CD), A = (QB + C)/E ∈ ℚ[Q]. α = 3: E linear and E | Q² + 4C²D·(…) — precisely
    4CD·A·E = Q(Q + E) + 4C²D, so Q² + 4C²D vanishes on the rational line {E = 0}; Q restricted to that line has degree
    exactly 2 (Q has no rational zero direction), so (Q|_E)² + 4C²D ≢ 0: impossible.
  • C quadratic: C = Q/(4BD) + E, deg E ≤ 1, and 4BD·A·E = κQ + E with κ = B + 1/(4BD) > 0. E = 0 is impossible (κ ≠ 0).
    α + deg E = 2: α = 2, E constant ⟹ A, C ∈ ℚ[Q]; α = 1, E linear ⟹ κQ = E(4BDA − 1), a product of linear forms: impossible.
  • D quadratic: D = Q/(4BC) + E, deg E ≤ 1, and 4ABC·E = QB + C (≠ 0). α = 2, E constant ⟹ A, D ∈ ℚ[Q]; α = 1, E linear
    ⟹ QB + C = 4BC·A·E: impossible as before.
 (c2) α = β = μ (then (A + B)_top = A_top + B_top ≠ 0 by positivity) and 2μ + γ + δ = μ + 2, so μ + γ + δ = 2.
  • μ = 0: C(4ABD − 1) = Q(A + B). γ = 2, δ = 0: C ∈ ℚ[Q]. γ = 0, δ = 2: D = (Q(A + B)/C + 1)/(4AB) ∈ ℚ[Q].
    γ = δ = 1: Q(A + B) = 4AB·C_top·D_top + …, a product of linear forms at top degree: impossible.
  • μ = 1: Q divides 4A_top B_top C_top D_top, a product of linear forms (γ + δ = 1): impossible (Q is prime in ℚ[u, v]).
  • μ = 2, γ = δ = 0: Q | A_top B_top, so (Q prime) A_top = κQ and then B_top(4CDκ − 1) = κQ, B_top = κ'Q. Write
    A = κQ + E_A, B = κ'Q + E_B (deg E ≤ 1). The Q²-coefficient gives 4CDκκ' = κ + κ', and the rest of the identity reads
    Q·G = C − 4CD·E_A E_B with G := (4CDκ − 1)E_B + (4CDκ' − 1)E_A (deg ≤ 1). If G ≠ 0, comparing degrees forces G constant and
    Q = (C − 4CD E_A E_B)/G, a product of linear forms up to constants: impossible. So G = 0 and E_A E_B = 1/(4D) is a nonzero
    constant, hence E_A, E_B are constants and A, B ∈ ℚ[Q]. ∎
(The case (b) bookkeeping: if γ = μ + 2 then s = γ = α + β + γ + δ, so α = β = δ = 0 and μ = 0.)

**Corollary 1.3 (PROVED).** Combining Theorems 1.1/1.2 with POINTWISE_BINARYFORM Thm 3.2/3.2′, Prop 5.1: every polynomial
Type I family valid on a cone, and every polynomial Type II family at all, in the coordinates of an irreducible binary
quadratic representation n = Q(u, v), is an ET polynomial identity in n. So the binary-form (norm-form, degree 2) rung of
the menu ladder ((J)76 Prop 7.1, MENU_STERILITY §5 table row M₂) collapses to rung 0, on every congruence class — not only on
square classes. The open question "genuinely two-variable Type I families with non-constant level" (POINTWISE_BINARYFORM
§5–6, O145) has a negative answer on cones. Remaining scope: Type I families valid only near finitely many directions (density
zero of prime points by Hecke, POINTWISE_BINARYFORM Cor 3.4-type argument), (x, y, z)-families whose ET coordinates are not
polynomial (§8 there handles square classes only), rational-function families (Lemma 3.3 there: density zero), norm forms of
degree ≥ 3 (the top-part step "Q prime and of degree 2" fails: lower-order terms of degree ≥ 2 need not lie in ℚ[N]).
*Numerical consistency (EVIDENCE, not a test of the proof):* POINTWISE_BINARYFORM §6 found 0 genuinely two-variable Type I
families for u² + v² with constant or linear levels (65 × 728 level pairs), as Theorem 1.2 predicts.
*T1/105 control:* the theorem is a negative statement; it predicts nothing at odd squares beyond ET Prop 1.6.

## 2. Deep item 2: the window lottery at primes (EVIDENCE + PROVED pieces)

* **Exact invariant.** m₀(p) = min{4x − p : ES solution with p ∤ x} = least m ≡ 3 (4) with −K_m ∈ {d mod m : d | K_m²},
  K_m = (p + m)/4 — the e-slice form, with consecutive integers K₃, K₃ + 1, … as the windows' K. Type II solutions have
  x ≤ n/2, so m₀ ≤ n whenever f_II(n) > 0 (s7_typeII_free_controls Lemma 1).
* **Prop 2.1 (Mordell's theorem in window form; PROVED).** m₀(p) ∈ {3, 7} for primes p ≡ 1 (4) outside 1, 121, 169, 289,
  361, 529 (mod 840) (explicit witnesses in s7_window_lottery). Checked: no p ≤ 10⁷ outside these classes has m₀ ≥ 11.
* **What a proof would need (B2 for windows, precise).** ES(p) at Type II ⟺ some K among the ⌈p/4⌉-shifted consecutive
  integers K = ⌈p/4⌉, …, ⌊p/2⌋ has a divisor ratio ≡ −1 modulo 4K − p. For any finite window set W this fails on infinitely
  many primes under Schinzel H (redteam-automorphic-2 Thm 2.2(iii)); explicit all-fail residue classes for W = {m ≤ M},
  M = 11, 27, 47, 63, 99, are produced by `s7_dickson_classes.py` (CONDITIONAL on Dickson's conjecture, admissible since every
  prime ≤ M divides the modulus). So a proof must let the window grow with p and control the joint factorisation of the
  K_m — a statement about the multiplicative structure of consecutive integers near p/4 in residue classes of their own
  shift, which is B2 in its purest form.
* **The lottery is congruence × independent rough parts (EVIDENCE).** Conditional permutation test (rough parts permuted
  within block, window, residue mod m and bit length): tail counts #(m₀ > M) for M = 3 … 47 (primes ≤ 10⁶) agree with the
  shuffled model within noise (e.g. M = 19: actual 161, shuffled 149–167 with B = 47), while a model conditioning only on
  Legendre symbols under-predicts by 3–9×. Records: m₀ ≤ 107 for p ≤ 10⁷ (p = 8 803 369), m₀/log²p ≈ 0.4–0.5 at records.
  Spearman(m₀, L(1, χ_p)-proxy) = 0.20 (0.23 inside Mordell-hard classes): hardness = QR-richness on small primes.
* **Positive-density forcing exists only at the wrong scale** (s7_gaussian_square_windows): K = S² at windows m ≍ p, cap-0 rate
  1.0·10⁻⁴, identical to random windows of that size. With Theorem 1.1/1.2 (small windows have no binary-form structure beyond
  ET identities), the forced-budget route at primes is closed at both ends.

## 3. Answers to the mandatory items
(i) No positive-density mechanism forces the cap-0 budget at a window of sub-p size: congruence forcing = ET classes (B1),
binary-form forcing collapses to identities in n (Thm 1.1/1.2), Gaussian forcing exists only at m ≍ p (B3). m₀(p) is a
congruence-modulated lottery, with no residual correlation (shuffle test); records grow like a small power of log p.
(ii) Cap ≤ 1 holds on explicit congruence classes of Haar measure ≈ 0.93–0.96 of the first undecided line lnr = 17
(PROVED per class, density EVIDENCE); the forced witness is blind on the r-generic points that carry sterility.
(iii) No finite certificate for r = 17: fixed windows give U/U⁻¹ boxes with a parity law; deep levels are ES solutions of
4/17^c; Frobenius over F₃ is exactly critical; Conj 4.2 remains the B2-type input.
(iv) No: separable thin families are nowhere dense (Baire) and cannot touch an open covering problem; the inseparable digit
menu is Galois conjugation.
(v) Theorem 1.1/1.2 (binary-form rung collapse); window parity law; enlarged T1 control set (non-squares with f_II = 0, e.g.
3985); L-value dictionary.

## 4. Sparks (not pursued)
* Norm forms of degree 3 (p = N_{K/ℚ}(x) for a cubic field, Heath-Brown-type representations): does the top-part argument of
  Theorem 1.2 extend when the lower-order terms of the parameters are allowed degree ≥ 2? The first case where the rung
  might not collapse.
* Theorem 1.2 for Type I families valid only near finitely many directions (cusp-like regions of indefinite forms).
* m₀ records versus extreme values of L(1, χ_p).
