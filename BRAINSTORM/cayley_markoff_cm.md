# Cayley cubic, Markoff dynamics and the CM tetrahedron (O143, memo 1 of the cubic/Markoff cluster)

Labels as in DISCOVERIES.md. Script: `scripts/bs_cubic_cayley.py` (sympy identities (A),(B); exhaustive check (C) on
all 2256 positive solutions of 4/p, 5 ≤ p < 400; orbit demo (D)). Notation: S = projective ES surface,
U_n = its affine ES chart (GEOMETRY_ES §1), V_k: X²+Y²+Z²−XYZ = k (Markoff type).

## 1. Idea

The projective ES surface is the 4-nodal (Cayley) cubic, and the Markoff surface V_4 is another affine chart of
the same cubic. Questions: (i) is there an integral correspondence between the two charts? (ii) Do the Markoff
(Vieta) moves act on ES solutions? (iii) Can their orbits be used to reach every prime? Answers: (i) no; (ii) yes,
with positivity preserved, via the compact SU(2) component; (iii) no, by orbit sparsity, and the orbits fix an
imaginary quadratic field, which is exactly the campaign's Type I/II CM field. The by-product is a clean geometric
origin of the Heegner discriminants −4d / −4dp.

## 2. Exact statements (all PROVED, elementary; identities machine-checked)

**P1 (symmetric Cayley form).** 4/n = 1/u₁+1/u₂+1/u₃ ⟺ y = (4u₁, 4u₂, 4u₃, −n) solves
`C : 1/y₀+1/y₁+1/y₂+1/y₃ = 0`, i.e. e₃(y) = 0. So S ≅ C over ℚ (divide by x₀x₁x₂x₃; y₃ = −n x₀/4). The nodes
are the coordinate points, Aut = S₄ permuting the y_i. **ES(n) ⟺ C has an integral point with y₃ = −n and
y₀, y₁, y₂ positive multiples of 4.** Without the "≡ 0 (mod 4)" level structure every n is trivial
(1/(3n)·3 = 1/n): the whole problem lives in the level-4 integral model, not in the surface.

**P2 (Markoff coordinates).** With e₁ = Σy_i,
`X = 2(y₀+y₁−y₂−y₃)/e₁, Y = 2(y₀−y₁+y₂−y₃)/e₁, Z = 2(y₀−y₁−y₂+y₃)/e₁`
one has `X²+Y²+Z²−XYZ−4 = −64 e₃(y)/e₁³` (check (A)). The nodes go to (2,2,2), (2,−2,−2), (−2,2,−2),
(−2,−2,2). The boundary of V_4 is the **Sylvester plane** e₁ = 0, which contains the three non-edge lines
{y_i+y_j = 0 = y_k+y_l}. The boundary of U_n is a **face** y₃ = 0 of the node tetrahedron.
* (i) U_n ≇ V_4, even over ℂ: U_n has one singular point, V_4 has four. The two log Calabi–Yau pairs are
  different: the ES boundary triangle passes through three nodes, the Markoff one through none.
* (ii) Positive ES points land in the **open compact component**. For y₀, y₁, y₂ > 0 > y₃ with each 4u_i > n,
  we have e₁ > 0 and |X|, |Y|, |Z| < 2 (X < 2 ⟺ 4u₃ > n, X > −2 ⟺ u₁+u₂ > 0). This holds in all 2256 cases of (C).
  The compact component is the closed curved tetrahedron spanned by the four nodes (the SU(2) character variety
  of ℤ²). Its four open faces are exactly the four sign patterns of y with one negative entry, permuted by S₄. So
  **every rational point on an open face is a positive ES point for some n** (permute so that y₃ < 0, then scale).
* (iii) The integral points of V_4 inside the open tetrahedron are the four points
  (1,1,−1) (and permutations) and (−1,−1,−1). Each is the face centre y ∝ (3,3,3,−1), i.e. the trivial
  point 4/n = 3·(4/(3n)), integral iff 4 | n. Integral structures do not correspond:
  V_4(ℤ) (traces of commuting SL₂(ℤ) matrices, Pell units, |X| ≥ 2) lies on the non-compact components, while
  the positive ES points lie in the compact one.

**P3 (degenerate Vieta).** In the general family `xyz + Q(x,y,z) + L + c = 0` (Markoff type, triangle xyz = 0 at
infinity), the involution in x exists iff the x² coefficient of Q is ≠ 0: the second root of the quadratic in x
is −(coefficient of x)/(coefficient of x²) − x. ES (4u₁u₂u₃ − n e₂ = 0) is the member with **no square terms**.
Geometrically, the line {u₂, u₃ fixed} passes through the node Q₁ at infinity, which absorbs two of its three
intersections, so at most one affine point remains. In GEOMETRY_ES Prop 2.1 terms: the two blow-up points on
each side of the toric triangle (Markoff) have merged into one point plus a vertex, and the vertex becomes a node
at infinity. So U_n has no Vieta involution of its own. By BL Lemma 3.10 every automorphism of the integral model
permutes the finite set U_n(ℤ) \ (lines): there is no infinite orbit and no "fundamental domain" reduction. In
Ghosh–Sarnak's language the whole solution set is its own fundamental set.

**P4 (CM tetrahedron).** Write a point of the open compact component as X = 2cos 2A, Y = 2cos 2B, ±Z = 2cos 2(A±B).
For a rational point, `K_P = ℚ(√(X²−4)) = ℚ(√−D)` with D > 0. For an ES point,
`X²−4 = −16(y₀+y₁)(y₂+y₃)/e₁²`, and the ES equation gives **D ≡ n·u₁u₂u₃ (mod squares)**, a symmetric
expression. Put α = x+y√−D, β = x'+y'√−D (tan A = y√D/x, tan B = y'√D/x'). Then, up to a common factor
(check (B), (B')):
```
y₀ = x x' (xx'−Dyy'),   y₁ = D x y'(xy'+x'y),   y₂ = D x' y (xy'+x'y),   y₃ = −D y y'(xx'−Dyy'),
```
that is, `y ∝ (Re α·Re β·Re αβ, D·Re α·Im β·Im αβ, D·Im α·Re β·Im αβ, −D·Im α·Im β·Re αβ)` with
Im(x+y√−D) := y. All positive ES points of all n are obtained this way, with D, x, y, x', y' > 0 and
xx' > Dyy'. With ET's maps π^I = (abdn, acd, bcd) and π^II = (abd, acdn, bcdn) (CONDITIONAL_ES.md l.78–80):
* Type I: n u₁u₂u₃ = (abcd)²·d·n², so **D ≡ d**;
* Type II: n u₁u₂u₃ = (abcdn)²·d·n, so **D ≡ dn**.

These are exactly the CM discriminants −4d (Type I) and −4dp (Type II) of POINTWISE_SPECTRAL / TYPEII_SPECTRAL.
Check (C) confirms, for all 2256 solutions, that p ∤ D for Type I with (−D/p) = −1 (BL's Brauer class,
GEOMETRY_ES Prop 5.1), and that p | D for Type II. So the Heegner fields of the campaign are the CM fields of the
SU(2) character points: the ES-positive face is a union over D of images of `T_K¹(ℚ) × T_K¹(ℚ)`, where
T_K¹ = R¹_{K/ℚ}𝔾_m and T_K¹(ℚ) = {α/ᾱ}.

**P5 (Markoff moves on ES solutions; Assessment-level orbit count).** Vieta X ↦ YZ−X etc. act on (2A, 2B) by
GL₂(ℤ) (here (a,b) ↦ (−a−2b, b)), i.e. on (α, β) ∈ (K^×/ℚ^×)² by monomial maps with conjugations. Hence they
**preserve the compact component and K_P**, and map positive ES points of 4/n to positive ES points of 4/n'.
Demo (D): 4/5 = 1/2+1/4+1/20 ↦ 4/32 = 1/16+1/17+1/272 ↦ 4/64 ↦ 4/4471 ↦ 4/164190848 ↦ …, all with D = 2.
Heights grow like H^{‖γ‖}, so an orbit contains ≪ (log N)² points with n ≤ N (Assessment: it needs the standard
fact that the Weil height on a rank-2 subgroup of T_K¹(ℚ) is comparable to a norm; not written out).

## 3. Literature anchor
* Ghosh–Sarnak, *Integral points on Markoff type cubic surfaces*, Invent. Math. 2022, arXiv:1706.06712v3
  (abstract and §§1, 8 read). Thm 1.1: Markoff descent to a compact fundamental set. (1.6):
  Σ_{|k|≤K} h(k) ∼ C K(log K)². Thm 1.2: infinitely many Hasse failures (≥ K^{1/2}(log K)^{−1/2}), and almost all
  k satisfy HP. The failures (Prop 8.1) are k = 4 ± 2ν² etc., built from the factorisation
  (2x₃−x₁x₂)² − (x₁²−4)(x₂²−4) = 4(k−4) "connected to the singular Cayley cubic V_4", plus quadratic reciprocity.
  Numerically the failures number ≈ K^{0.89}. Remark 1.3: LM20/CTWX20 explain the Prop 8.1(i),(ii) failures by
  integral BM; (iii) uses Markoff descent and is not BM.
* Loughran–Mitankin (IMRN 2021) and Colliot-Thélène–Wei–Xu (Ann. SNS Pisa 2020): Brauer groups of Markoff
  surfaces, as quoted by GS Remark 1.3. Not re-read here.
* Bright–Loughran (as in GEOMETRY_ES §1) for the ES side. That the Cayley cubic is the SU(2)/SL₂ character
  variety of ℤ² with the trigonometric parametrisation is classical (from memory, e.g. Goldman's surveys;
  unverified citation). The CM parametrisation P4 is presumably equivalent to classical parametrisations of
  Σ1/y_i = 0. We found no source connecting it to ET's Type I/II levels (not searched exhaustively).

## 4. Barrier screen
* **B1 / T6.** Markoff orbits are algebraic recipes. At bounded word length they are polynomial families of
  bounded complexity, and LONGSHOT_FIBRED Cor 2.4 / POINTWISE_SIZE Thm C apply. At unbounded word length,
  P5 gives ≪ (log N)² points per orbit, so ≫ N/(log N)³ orbits are needed for the primes ≤ N. An orbit does not
  compress the solution set (Σ_{n≤N} f(n) ≍ N log³N, so orbits are mostly singletons below N).
* **B2.** Fix K and β (the "level" and one torus coordinate). Then p | Re(αβ) (Type I) or p | D (Type II), and the
  remaining requirement (the common factor g must be absorbed, 4 | y_i) is a divisor problem in α. This is the CM
  torus slice of EXACT_FORMULA Thm 5.2, i.e. divisor-class reduction (I)8.
* **B3.** No main term is produced. The only "count" is the Markoff orbit count, which is polylog.
* **B5 / T1.** Every step of P1–P5 holds for every n, including odd squares (ES(m²) points exist via ES(m); their
  D is that of the m-solution). Odd squares are excluded only after one insists on Type I/II, i.e. on the p-adic
  position of the face point. P4 merely relabels that condition (p ∤ D with (−D/p) = −1). No step creates a
  solution, so nothing is false at m², and therefore nothing proves ES.
* **B6 / T7.** GS's "almost all k" (Thm 1.2(ii)) is a variance argument over k: an average leak. Its ES analogue
  ("almost all n") is classical.
* **T8.** The coarse invariant is K_P (and the GL₂(ℤ)-class of ⟨α,β⟩). Lifting to n = p is the divisor problem
  of B2.

## 5. Experiment
`scripts/bs_cubic_cayley.py` (runs in seconds): (A), (B), (B') identities are 0. (C): 0 failures out of 2256.
(D): the orbit shown above.

## 6. Viability Assessment
**PARTIAL / COLLAPSES to B2 at the fixed-(K, β) step.** There is no integral correspondence with Markoff V_4 (P2).
U_n has no Vieta involutions (P3). The Markoff dynamics does act on ES points across n, through the compact
SU(2) component (P5), but its orbits are polylog-sparse and fix K, so they neither compress nor create
solutions. By-products:
* (PROVED) the symmetric level-4 Cayley formulation P1;
* (PROVED) positivity ⟺ the open faces of the compact tetrahedron (P2(ii));
* (PROVED) the CM dictionary P4, D ≡ n u₁u₂u₃, which explains geometrically why Type I lives on disc −4d and
  Type II on disc −4dp: they are the CM fields of SU(2)-character points of ℤ².

**Comparison with GS** (lesson for H-F; a short memo follows in `BRAINSTORM/markoff_hasse_failures_vs_es.md`):
Markoff local densities depend on k at every prime, while ES local densities at ℓ ∤ 2n do not depend on n at all.
