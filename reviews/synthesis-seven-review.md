# R256 — hostile review of O247 Synthesis VII (SYNTHESIS_SPARKS7.md, BRAINSTORM/s7_*.md)

Reviewer: R256 (side agent, branch side-agent/review-synthesis-seven). Author files merged from side-agent/synthesis-seven
at a8269442. From-scratch scripts: `scripts/review_r256_bf_search.py` (polynomial-family search), `scripts/review_r256_m0.py`
(m₀, brute-force validation, Type-II-free non-squares), `scripts/review_r256_dickson.py` (Dickson classes),
`scripts/review_r256_parity.py` (r-generic window parity). Data in `data/review_r256/`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Thm 1.1 (Type II, one valid point ⇒ A, B, C, D ∈ ℚ[Q]) | SOUND (minor wording) |
| Thm 1.2 (Type I on a cone ⇒ ℚ[Q]) | SOUND-AFTER-REPAIRS (minor: sign dilation; positivity of κ) |
| Cor 1.3 / consequences (POINTWISE_BINARYFORM §5–6, Prop 5.2, (J)76 hatch) | (in progress) |

## 1. Theorems 1.1 and 1.2 — re-derivation

Conventions checked: with (x, y, z) = (abd, acdn, bcdn) the equation 4/n = Σ1/· is 4abcd = a + b + cn (Type II); with
(abdn, acd, bcd) it is 4abcd = n(a + b) + c (Type I). Both match POINTWISE_BINARYFORM §1 / ET §2 (ET p. 3: Type II = n | y, z,
x coprime to n). The theorems only assume A, B, C, D polynomial (not e, f), so they are formally stronger than
POINTWISE_BINARYFORM's six-coordinate hypothesis.

**Thm 1.1, re-derived line by line.** s = α+β+γ+δ = deg LHS (product of nonzero polynomials). RHS degree ≤ max(α, β, γ+2).
Case split s ≤ α / s ≤ β / s > α, β is exhaustive. (a): s ≥ α forces β = γ = δ = 0; 4BCD = 1 ⇒ B + CQ = 0 impossible; else
A ∈ ℚ[Q]. ✓ (b): A + B has degree < s, so if γ + 2 > s the RHS would have degree γ + 2 ≠ s; hence γ + 2 = s, α + β + δ = 2 and
4A_top B_top D_top = Q. Q irreducible ⇒ not a product of two rational linear forms ⇒ one top quadratic, two constants. ✓
(b1) C(4ABD − Q) = A + B ≠ 0 constant ⇒ C constant ⇒ D ∈ ℚ[Q]. ✓ (b2) E = 4BDA − Q has deg ≤ 1, E ≠ 0, deg(A+B) = 2 = γ + deg E,
γ ≥ 1. γ = 1: Q + 4B²D = E(4BDC − 1) — I recomputed this: (Q + E)/(4BD) + B = CE ⇔ Q + E + 4B²D = 4BDCE ✓; degree-2 parts
give Q = 4BD·E_lin·C_lin, a rational factorisation ✗. γ = 2: E constant, A, C ∈ ℚ[Q]. ✓ Symmetric B-case ✓.
Validity is used only for A + B ≠ 0 in (b1); the Remark's degenerate family (A = −B = κ, D = −Q/(4κ²)) satisfies the identity
(checked by hand: 4·(−κ²)·C·(−Q/4κ²) = CQ). **SOUND.**

**Thm 1.2, re-derived line by line.** (a) γ > μ+2: s = γ ⇒ α = β = δ = 0, C(4ABD − 1) = Q(A + B) of degree 2 < γ ✗. ✓
(b) γ = μ + 2: top of Q(A+B) + C is Q·(A+B)_top + C_top, nonzero on the arc by positivity ✓; forces μ = 0, γ = 2, C ∈ ℚ[Q] ✓.
(c) top identity 4A_top B_top C_top D_top = Q(A+B)_top ✓.
 (c1) B quadratic: A(4BCD − Q) = QB + C ✓; α = 4 ✓; α = 3: I recomputed 4CD·A·E = Q(Q + E) + 4C²D ✓ (from A·E = Q(Q+E)/(4CD) + C).
 On the rational affine line E = 0 the polynomial Q has degree exactly 2 because an irreducible binary form has no rational
 isotropic vector ✓ (this needs E of exact degree 1, which holds). C quadratic: 4ABD(Q/(4BD) + E) = AQ + 4ABDE, so
 4ABD·E = κQ + E with κ = B + 1/(4BD) ✓. D quadratic ✓.
 (c2) μ = 0 ((2,0) is actually case (b), harmless redundancy), (0,2), (1,1) ✓; μ = 1: Q prime in the UFD ℚ[u, v] cannot
 divide a product of linear forms ✓; μ = 2: I re-expanded 4CD(κQ + E_A)(κ'Q + E_B) − Q(κQ + E_A + κ'Q + E_B) − C: degree-4
 part gives 4CDκκ' = κ + κ', remainder Q·G = C − 4CD·E_A E_B with G exactly as stated ✓; G ≠ 0 ⇒ G constant (deg(QG) ≤ 2) ⇒
 Q ∝ product of linear parts ✗; G = 0 ⇒ E_A E_B = 1/(4D) ⇒ both constant ✓.
Exhaustiveness: (c1)/(c2) × the 3 resp. 3 sub-cases cover β+γ+δ = 2 resp. μ+γ+δ = 2 completely ✓.
Positivity is used exactly in: (A+B)_top ≠ 0 when α = β; no cancellation in Q(A+B)_top + C_top; κ ≠ 0 (needs 4B²D ≠ −1,
true as D > 0); A + B ≠ 0. **SOUND-AFTER-REPAIRS** (defects D1, D2 below are editorial).

**Brute force (from scratch, `review_r256_bf_search.py`, python-flint exact division).** For each Q, solve the identity for
one coordinate given the other three from boxes S1 = {deg ≤ 1, coefficients in {−1,0,1,2}} (63 polys) and
S2 = {deg ≤ 2, coefficients in {−1,0,1}} (728 polys): Type II solved for A (B, C ∈ S1, D ∈ S2) and for D (A ∈ S2, B, C ∈ S1);
Type I solved for A (two placements of S2) and for D (A, B ∈ S1, C ∈ S2); ≈ 2.9M divisions per (Q, mode). Each family is
tested for membership in ℚ[Q] (top-down peeling of c·Q^k), for an integral valid point (|u|, |v| ≤ 12, Type II) and for an
open arc of directions with all top parts positive (Type I, 720 directions; sign dilation allowed). Results
(`data/review_r256/bf_irred.txt`, `bf_red.txt`):
* Irreducible Q ∈ {u²+v², u²+uv+v², u²−2v² (indefinite), u²+5v²}: Type II: every family outside ℚ[Q] (120 per Q) has
  A + B = 0 — exactly the Remark's degenerate family, never valid. Type I: 840 families outside ℚ[Q] per Q, **none** positive on
  an arc and none with an integral valid point (|u|, |v| ≤ 10, checked for u²+v²); 720 of them have A + B = 0. Consistent with
  both theorems; also shows the cone/positivity hypothesis of Thm 1.2 is doing real work (identity-level solutions abound).
* **Positive control, reducible Q** ∈ {uv, u²−v², u², u²+uv}: Type I families outside ℚ[Q] that are positive on an arc and
  integrally valid are found (32 for uv, 28 for u²−v², 16 for u²), e.g. Q = uv: (A, B, C, D) = (2v+1, 2, u, (v+1)/8), valid at
  (u, v) = (1, 7) (n = 7, (A,B,C,D) = (15, 2, 1, 1)); classical "n = u(4k−1)"-type families. So the search can see escapes, and
  irreducibility is genuinely needed in Thm 1.2.
* Type II with reducible Q: no valid escape in the box. By hand, the (b)-case shapes with two linear tops (A_top·B_top or
  A_top·D_top ∝ L₁L₂) and (b2) with γ = 1 (needs Q + 4B²D, D > 0, to factor) also fail for Q = uv. So for Type II the
  irreducibility hypothesis may be partly superfluous — not a defect, just an observation (no claim is made either way).

## 2. Window lottery, m₀(p), Mordell form, Dickson classes (§2, s7_window_lottery)

**Definition / criterion re-derived.** Type II (ET: n | y, z, gcd(x, n) = 1), y = nY, z = nZ, m = 4x − n: m/x = 1/Y + 1/Z ⟺
(mY − x)(mZ − x) = x² ⟺ ∃ d | x², d ≡ −x (mod m) (gcd(x, m) = gcd(x, n) = 1 makes the second congruence automatic). With
x = K_m this is the memo's e-slice form ✓. `review_r256_m0.py brute` validates this criterion against direct enumeration of
(x, Y) for all primes p ≡ 1 (4) < 3000 (least window) and all n ≡ 1 (4) < 3000 (existence): 0 mismatches.

**Prop 2.1 (Mordell in window form).** Re-derived every case (a)–(e) by hand: residues, the divisors d ∈ {1, K/2, 5, 5, 10,
20, 1, 4, 2} and d | K² all check; the residual set is p ≡ 1 (24), p ≡ ±1 (5), (p/7) = 1, i.e. 1·2·3 = 6 classes mod 840 =
{1, 121, 169, 289, 361, 529} ✓. From scratch to **10⁷** (all 332 180 primes p ≡ 1 (4)): 0 primes off the six classes with
m₀ ≥ 11 (`data/review_r256/m0_1e7.txt`). **SOUND.**

**Records / histogram (EVIDENCE).** Recomputed exactly: records (5,3), (73,7), (1129,11), (1201,23), (21169,31), (67369,35),
(87481,63), (1430641,71), (8803369,107) — identical to the memo; histogram ≤ 10⁶ identical (3: 34 635, 7: 3 551, 11: 584,
15: 131, 19: 113, 23: 96, 27: 8, 31: 33, ≥ 35: 24). **SOUND**; see D5 for the histogram's mislabelled "larger: 32".

**Dickson all-fail classes (CONDITIONAL).** Re-derived the construction: with L = 4·∏_{ℓ≤M} ℓ^{max v_ℓ(K_m)+1}·∏m the forms
f₀(t) = Lt + r, f_m(t) = (Lt + r + m)/(4S_m) are integral, keep the M-smooth part S_m exactly and R_m (mod m) constant (since
gcd(K_m, m) = 1, L/(4S_m) ≡ 0 mod m and mod every ℓ ≤ M). `review_r256_dickson.py` recomputes, for the author's
representatives (M = 11: 1000000000129, 1000000000441; M = 27: 1000000004089; M = 47: 1000000030969; M = 99: 1000000434889),
that no window m ≤ M fires when each rough part is prime (divisor residues of S_m²·{1, R, R²}), and that the system is
admissible at every prime ≤ 500 (above that #forms ≤ 26 < ℓ). Negative control r = 10¹² + 1: windows 3, 7 fire. **SOUND**
(CONDITIONAL on Dickson, as labelled). Minor: "m₀ is unbounded under Dickson" needs a class for every M, which the script
only exhibits for five M; cite redteam-automorphic-2 Thm 2.2(iii) for the general statement (D6).
