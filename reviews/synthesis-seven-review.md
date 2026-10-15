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
| Cor 1.3 / consequences (POINTWISE_BINARYFORM §5–6, Prop 5.2, (J)76 hatch) | SOUND-AFTER-REPAIRS (scope wording: O145's one-variable questions are not settled) |
| Prop 2.1 (Mordell ⟺ m₀ ∈ {3, 7} off six classes mod 840) | SOUND (re-proved; checked to 10⁷) |
| m₀ records ≤ 107 for p ≤ 10⁷, histogram | SOUND (recomputed exactly; histogram label slip D5) |
| Permutation test (EVIDENCE) | SOUND as EVIDENCE for B = 47; wording repairs (D7) |
| Dickson all-fail classes (CONDITIONAL) | SOUND (5 representatives re-verified, admissibility checked) |
| Parity law on r-generic lines (Lemma 2) | SOUND (re-proved; brute-forced r = 17, 19, 23; analogy wording D9) |
| (ii) certified caps, Lemma 1 per class; Haar ≈ 0.93–0.96 | SOUND (per class: e*(p) ≤ e, not ES); densities replicated; "Haar-almost all" overstated (D8) |
| (iii) no finite certificate / level-1 survivors | SOUND (survivor sets reproduced with an independent test) |
| (iv) FF thin menus (Baire), lifted digit identities | SOUND as Assessment |
| (v) Type II window bound Lemma 1; 103 Type-II-free non-squares ≤ 2·10⁵; 3985 | SOUND (recomputed: 103, list identical; 3985 unique ≤ 10⁶) |

Overall: **no FATAL, no MAJOR defect.** Nine MINOR defects (D1–D9), all editorial/scope.

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

**Permutation test (EVIDENCE).** Independent re-implementation (`review_r256_shuffle.py`; groups = (block of 2000 primes, m,
R mod m, bit length of R), windows m ≤ 51). Actual tails at N = 10⁶ reproduce the memo exactly (4540, 989, 405, 161, 57, 20, 7).
Shuffled, 40 permutations each:
* B = 47, N = 10⁶: mean (sd) 4542.8 (9.2), 985.3 (11.1), 408.7 (8.2), 160.4 (7.2), 51.0 (4.2), 14.4 (2.4), 4.2 (1.4). Fits for
  M ≤ 19; the deep tail is above the model at M = 35 (actual 20, 0/40 shuffles ≥ 20) and M = 27 (6/40).
* B = 47, **N = 4·10⁶** (30 permutations; `shuffle_4e6_B47_30.txt`): every tail fits (M = 27: 146 vs 152.9 ± 9.8; M = 35: 48
  vs 48.5 ± 5.8; M = 47: 11 vs 9.3 ± 1.8). So the 10⁶ deep-tail excess is a fluctuation, and the EVIDENCE claim survives.
* B = 13, N = 10⁶: the model **does not fit**: M = 11: actual 405 vs 436.7 ± 13.5 (40/40 shuffles ≥ actual), M = 19: 161 vs
  189.3 ± 11.8 (39/40). The memo's own B = 13 ranges (427–456, 175–200) already exclude the actual values; the text does
  not say so (D7).
* Control "m-only" shuffle (R mod m not preserved): tails collapse (M = 19: 14–15 vs 161), so preserving R mod m is essential,
  as the memo's design assumes.
Verdict: **SOUND as EVIDENCE for B = 47**, with wording repairs (D7).

## 3. Parity law and r-generic windows (s7_sibling_certificate Lemmas 1–2)

Re-derived. At the r-generic point K_m ≡ 1/4 (mod m), v_ℓ(K_m) = v_ℓ((1+m)/4) for ℓ ≠ r, v_r(K_m) = v_r(u+m) ✓. For odd
ℓ | (1+m)/4: (m/ℓ) = (−1/ℓ) and Jacobi reciprocity with (m−1)/2 odd gives (ℓ/m) = (−1/ℓ)(m/ℓ) = 1 ✓; ℓ = 2 needs 8 | 1+m,
(2/m) = 1 ✓. χ(−1/4) = −1 ✓. If c ≥ 1 then r | u + m with (u/r) = −1, so (−m/r) = −1 and (r/m) = (−1/r)(m/r) = (−m/r) = −1 ✓;
hence χ(r)^c = −1 ⇒ c odd. For c = 0 the same character computation is already contradictory (χ(δ) = 1 ≠ −1), so the T1
remark is not needed (D9). The law holds for **every** admissible c, not only the least.
From scratch (`review_r256_parity.py`): r = 17, m ≤ 2·10⁵, c ≤ 16: 464 firing windows, every admissible c odd, every
firing window has (−m/17) = −1; same for r = 19, 23 (m ≤ 5·10⁴). m = 11 at r = 17: admissible c ∈ {3, 5, 7, 13, 15}, least
c = 3 ✓ (the P-datum example). Level-1 windows at r = 17: {3, 7, 23, 39} ✓ (cells 14, 10, 11, 12 ✓).
Level-1 survivors with the full fixed-divisor test (`review_r256_level1.py`, m ≤ 3·10⁵, windows + mirrors): r = 13 {2, 5, 7, 8},
r = 17 {3, 5, 6, 7}, r = 19 {2, 3, 10, 13}, r = 23 {5, 14} — identical to the memo's ratio-test sets, and the r = 19, 23 sets
equal STERILE_LOWER Comp 4.1 (read on main) ✓. **SOUND** (Lemma 1, Lemma 2 PROVED; numerics EVIDENCE).
"Exact ℤ-twin of (J)67's root-product law" is an analogy (both are μ₂/quadratic-character obstructions on exponents), not a
proved correspondence: should read "analogue" (D9). Frobenius criticality (3^k(N+1) − 1 levels, ball contains 1 iff N = 0)
re-checked: ✓ given (J)72 Prop 5.1.

## 4. Certified caps on lnr = 17 (s7_certified_caps Lemma 1)

Re-derived from CAP_DOWN Lemma 1.1 (read on main): for d = K·s^g·∏_{ℓ∈F} ℓ^{j_ℓ}, c_ℓ = b_ℓ + j_ℓ ∈ [0, 2b_ℓ] since b_ℓ ≥ 1
(also for ℓ = 2, giving condition (ii)); c_s = b_s + g ≤ 2b_s for g ∈ {−1, 0, 1}; g = 2e′+1 with b_s odd gives c_s even and
c_s/2 − b_s = (2e′+1−b_s)/2 ≤ e′; all other primes of K have c = b. d ≡ −K (mod q) ⟺ s^g∏ℓ^j ≡ −1 since gcd(K, q) = 1 ✓.
Existence of s: (K/q) = (p/q) = (q/p) = −1 (p ≡ 1 (4)), and 2 is never the forced non-residue because p ≡ 1 (8) makes K odd
for q ≡ 3 (8) and (2/q) = 1 for q ≡ 7 (8) ✓. The hypothesis depends on p mod 8·q·∏_{ℓ≤L}ℓ ✓.
**What is PROVED per class:** for every prime p in a certified class, e*(p) ≤ e, i.e. an ES^{(y,e)}(p) solution (CAP_DOWN
normalisation) exists — not ES itself unless e = 0. The 0.93–0.96 figure is a Monte Carlo Haar measure (EVIDENCE); as Haar
measure of a finite union of congruence classes it equals the relative prime density on the line (Dirichlet), so "explicit
positive-density classes with cap ≤ 1" is correct as stated.
From scratch (`review_r256_capdensity.py`, Haar sampler: p ≡ 1 (8), QR mod 3…13, NR mod 17, uniform above; forced windows =
primes q ≡ 3 (4), 19 ≤ q ≤ Q, (p/q) = −1): Q = 200: cap 0 / ≤ 1 / ≤ 2 = 0.764 / 0.922 / 0.938 (author 0.770 / 0.928 / —);
Q = 400: 0.873 / 0.954 / 0.964 (author 0.875 / 0.959) ✓. Forced + F-only (all windows m ≡ 3 (4) ≤ Q, composite and < 19
included): cap 0 = 0.999 (Q = 200), 1.000 (Q = 400) — a bit higher than the author's 0.982 / 0.997, presumably a different
unforced-window set (unspecified in the memo; D8). Count check: 4 945 primes p ≡ 1 (4), p ≤ 2·10⁷ with lnr = 17 ✓.
**SOUND** for Lemma 1 and the per-class statement; "cap 0 on Haar-almost all of the line" is an overstatement (D8).

## 5. (iv) Function-field menus (s7_ff_nonlinear) — Assessment

Lemma 1 is elementary (finite union of closed nowhere-dense sets is closed nowhere dense; "Baire" only needed for countable
unions, fine in the compact Hausdorff Â). Lemma 2 proof ✓ (a basic open set mod M, CRT at ℓ ∤ M with φ mod ℓ not surjective
gives an open set missing φ(F_q[T])); for φ = X⁴ + 1 (char 3) non-surjectivity holds at every ℓ, because x ↦ x⁴ is never
injective on F_{3^k}^* (2 | 3^k − 1), so the Sophie-Germain example satisfies the hypothesis ✓.
Lemma 3 re-derived: π^p = Σ θ^{ip}U_i(θ^p)^p = Σ T^i U_i^p = P ✓; 4^p = 4 in F_p ✓; π ↦ P^{σ⁻¹} under θ ↦ T ✓.
Application caveat: "U ⊆ C ∪ ⋃T_i ⇒ U ⊆ C" must be applied with T_i = closures of thin images and with the covered target
dense in U ∖ C (all polynomials; for primes, Dirichlet for F_q[T] on unit cylinders). Implicit; harmless. **SOUND as
Assessment** (labels appropriate: PROVED lemmas, Assessment conclusion).

## 6. (v) Enlarged T1 control set (s7_typeII_free_controls)

Lemma 1 re-derived: m/x = 1/Y + 1/Z ≤ 2 ⇒ x ≤ n/2 ⇒ m ≤ n ✓ (ET's Type II requires gcd(x, n) = 1 — ET p. 3, checked in the
PDF — matching the memo). From scratch (`review_r256_m0.py free 200000`): **103** non-square n ≡ 1 (4) ≤ 2·10⁵ with
f_II(n) = 0; the list is identical to the memo's displayed members (21, 57, 93, 105, …, 1705, 3985, 4585, …); 101/103 are
divisible by 3 or 7 (exceptions 1705, 3985) ✓. `review_r256_free1mod4.py 10⁶`: 3985 is the **only** Type-II-free non-square
≤ 10⁶ with all prime factors ≡ 1 (4) ✓. **SOUND.**

## 7. Consequences of Thms 1.1/1.2 (Cor 1.3, (I6), memo Assessment)

* **Removes the hypotheses of POINTWISE_BINARYFORM Prop 5.2** (positive definite Q, A_F ≠ ∅): correct. Prop 5.2's forms are
  definite, hence irreducible; Thm 1.1 needs only irreducibility and one valid point, and does not use O145 Prop 3.2. Only
  gap: Prop 5.2 concludes F ∈ ℚ[n]⁶ (six coordinates); Thm 1.1 gives a, b, c, d — add e, f (D4). ✓
* **Answers POINTWISE_BINARYFORM §5–6 negatively on cones**: correct for the question as posed there ("genuinely two-variable
  Type I families with non-constant level" for a form Q, polynomial ET coordinates, valid on a cone). For definite Q it extends
  to "valid at a positive proportion of prime points of a class" via Thm 3.2(c)/Lemma 3.1 + Hecke (as Cor 1.3's scope says). ✓
  But **O145's own open items are NOT settled**: ident_form_families §6 (on main) lists (a) one-variable Type I families with
  non-constant level c(t), d(t) on P = t² + k, (b) quadratic P with t-dependent leading coefficient, (c) "whether some 2-variable
  identity on a binary form exists". Thm 1.2 answers (c) on cones only. (a), (b) are one-variable, non-homogeneous problems to
  which neither the top-form argument nor the cone hypothesis applies — and one-variable Type I families outside ℚ[P] do exist
  there (O145 Prop 3.4, k = 21, 37). Likewise POINTWISE_BINARYFORM §7's "Open: Type I analogue of O145 Prop 3.2" (a statement on
  lines) is bypassed, not proved. (I6)'s parenthesis "(Type I families with non-constant level; O145)" overclaims (D3).
* **"Closes the degree-2 norm-form hatch of (J)76"**: SYNTHESIS does not use these words; what it states (Cor 1.3: the M₂ rung
  collapses to rung 0 on every congruence class) is correct *for polynomial ET-coordinate families* of a binary quadratic form,
  Type I on cones, and its "Remaining scope" list is accurate and complete as far as I can see (cusps of indefinite forms, non-
  polynomial ET coordinates of (x, y, z)-families off square classes, rational families, degree ≥ 3, plus §2's "factor-selection
  procedures that are not polynomial ET families"). MENU_LADDER's "norm-form data remain" (an Assessment) also covers
  procedures that use (u, v) non-polynomially (floor/factorisation in (u, v): POINTWISE_BINARYFORM §4.4(i); unbounded families
  of forms: §4.2); these are untouched. Recommend Cor 1.3 list §4.4(i) and §4.2 explicitly in its remaining scope (D3).
  One more check: the collapse to "rung 0" is meaningful on non-square classes: ℚ[Q]-families are one-variable ET identities
  whose integrality set is a union of residue classes of n, i.e. Mordell/ET classes ✓.
* T1/105 control remark ("predicts nothing at odd squares beyond ET Prop 1.6") ✓ — a negative theorem.

**Verdict Cor 1.3: SOUND-AFTER-REPAIRS (scope wording D3, D4).**

## 8. Not re-checked
Spearman(m₀, L(1, χ_p)-proxy) = 0.35 / 0.20 (s7_lvalue_proxy), the Gaussian-window cap-0 rate 1.0·10⁻⁴ (only the identity
p + m = (A+B+1)² for m = 2AB+2A+2B+1, p = A²+B², and m ≡ 3 (4), checked by hand ✓), the union mass 0.31857/0.31888, and the
actual-prime cap percentages 79.4 / 93.8 / 95.2 %. All are labelled EVIDENCE and none is load-bearing.

## 9. Defects

No FATAL, no MAJOR defect found. All MINOR:

* **D1 (MINOR) Thm 1.2 proof, "Positivity on the cone".** Valid points may carry the sign pattern (A, B, C) < 0 < D (ET
  dilation; POINTWISE_BINARYFORM §1 and its R159 repair to Thm 3.2). Repair: "On an arc I avoiding the zero directions, the sign
  of each coordinate at far valid points equals that of its top part, constant on I; replacing (A, B, C) by −(A, B, C) (which
  preserves the Type I identity and the conclusion) we may assume A_top, B_top, C_top, D_top > 0 on I."
* **D2 (MINOR) Thm 1.2 (c1) C-quadratic and (c2).** "κ = B + 1/(4BD) > 0" needs B > 0 (D1); only κ ≠ 0 is used, and
  κ = (4B²D + 1)/(4BD) ≠ 0 because D > 0. In (c2) μ = 0 the sub-case γ = 2 is case (b) (γ = μ + 2), not (c): drop it or mark it
  redundant.
* **D3 (MINOR, scope) (I6), s7_normform_collapse Assessment, Cor 1.3.** "settle the open question … (Type I families with
  non-constant level; O145)": O145's open items (ident_form_families §6: one-variable non-constant-level Type I on t² + k;
  t-dependent leading coefficient) are not addressed, and the line-version "Type I analogue of O145 Prop 3.2"
  (POINTWISE_BINARYFORM §7) is bypassed, not proved. Repair: "settles, on cones, the two-variable question of
  POINTWISE_BINARYFORM §5–6 (and the last clause of ident_form_families §6); O145's one-variable questions remain open." Add
  POINTWISE_BINARYFORM §4.4(i) (floor/factorisation in (u, v)) and §4.2 (unbounded families of forms) to Cor 1.3's remaining scope.
* **D4 (MINOR) Thm 1.1/1.2 vs Prop 5.2.** Prop 5.2 concludes F ∈ ℚ[n]⁶; add one line: f = 4acd − 1 (Type II) resp. the Type I
  e, f are then rational functions of Q that are polynomials, and ℚ(Q) ∩ ℚ[u, v] = ℚ[Q] (if h(Q) | g(Q) with gcd(g, h) = 1 in
  ℚ[t], a root ρ of h gives Q − ρ | g(Q), whence g(ρ) = 0).
* **D5 (MINOR) s7_window_lottery histogram / records.** "…; 31: 33; larger: 32" omits m₀ = 27 (8 primes); ≥ 35 has 24. Repair:
  "27: 8; 31: 33; ≥ 35: 24". "m₀/log²p ≈ 0.4–0.5 at the records": the records give 0.28–0.49 (e.g. 35/log²67369 = 0.28,
  71/log²1430641 = 0.35); say "0.3–0.5".
* **D6 (MINOR) "So m₀ is unbounded under Dickson".** The script exhibits all-fail classes for M ∈ {11, 27, 47, 63, 99} only.
  Repair: "m₀ > 99 for infinitely many p under Dickson; unbounded under H by redteam-automorphic-2 Thm 2.2(iii)".
* **D7 (MINOR) Permutation-test wording (s7_window_lottery, SYNTHESIS §2).** (a) The B = 13 shuffles reported in the memo exclude
  the actual tail at M = 7, 11, 19 (989 vs 1008–1056, 405 vs 427–456, 161 vs 175–200; my 40 shuffles: 405 vs 436.7 ± 13.5).
  "Agree within noise" holds for B = 47 only; say so, and conclude that primes 17–47 carry part of the dependence. (b) "Shared small
  prime factors" is inaccurate for ℓ > 11: K_m − K_{m′} = (m − m′)/4 ≤ 12 for windows ≤ 51, so no prime > 11 divides two windows'
  K; the dependence is carried by the *joint congruence of p* modulo primes ≤ 47 (e.g. mutual exclusivity of ℓ | K_m). (c) Four
  shuffles cannot resolve the deep tail M ≥ 27; cite a larger run (mine: N = 4·10⁶, 30 shuffles, all tails within 1 sd).
* **D8 (MINOR) "cap 0 on Haar-almost all of the line" (I3; §3(ii) by implication; s7_certified_caps).** For any finite window
  set the cap-0 measure is < 1 (the memo's own B1 screen). Repair: "cap 0 on Haar measure ≈ 0.98–1.00 for windows ≤ 200–800
  (EVIDENCE)"; and specify which unforced windows enter the F-only count (prime q only? composites? q < 19?).
* **D9 (MINOR) s7_sibling_certificate Lemma 2.** "(−m/r) = −1 gives χ(r) = −1" is valid for c ≥ 1 (r | u + m); c = 0 is excluded
  by the same character computation (χ(δ) = 1 ≠ −1), so the T1 parenthesis is unnecessary. State that every admissible c (not
  only c_m) is odd. "Exact ℤ-twin of (J)67" → "ℤ-analogue" (no proved correspondence).

## 10. Repairs applied
None yet (author's branch has no commits after a8269442 at time of writing; repairs left to the author / parent).
