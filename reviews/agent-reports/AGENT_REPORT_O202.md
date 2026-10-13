# AGENT_REPORT_O202 — ES variants on Markoff-type cubic surfaces (spark relay W)

Main file: MARKOFF_ES.md. Scripts: scripts/mk_fixedD.py, mk_genus.py, mk_depth.py, mk_depth3.py, mk_fibreHP.py.
ES is not solved; ES^{[2]}/ES^{(y,1)} for all non-squares remain OPEN.

## SHARP:
1. **ES is "depth 3" of a continued fraction (Thm 4.2–4.3, PROVED).** ES^{[2]}(n) ⟺ ∃ μ: some odd-index CF
   denominator Q_k of √(4μ² − 4n) is odd, prime to n and divides μ. For μ = t + nj > 2n one has Q₁ = 4μ − 1 − 4n,
   Q₂ = 4n, Q₃ = 4tj − 1, and the depth-3 condition Q₃ | μ is exactly the classical shot family
   "n + 4t² has a divisor ≡ −1 (mod 4t)" with B = 1; every overflow solution (B > 1) is at depth k ≥ 5.
   (R202 repair M1/m7: this holds for μ > 2n; for μ ≤ 2n the ES points (A = 2, j = 1) are at depth 1, and the
   ι_B-partners B = 4μj − 1 of ES points are B > 1 points at depth 3.)
   Parallel to DEDEKIND (J)9 (ES = HJ length-3 words). Checked against brute force (no misses).
2. **On a single admissible fibre D, a locally admissible λ is globally solvable ≈ 45–80 % of the time (EVIDENCE,
   16 non-square n incl. 105, three D each, λ to 3·10⁴, spot checks at 10⁵; T1 controls give 0).** So ES^{[2]}(n) has
   a polynomially large heuristic main term (≍ Λ/√log Λ λ's per fibre) — B3/B6 do not bite — and reduces to a
   Cohen–Lenstra/Gauss-type statement: "for some genus-admissible λ the ideal above D is principal in
   ℤ[2√(λ²D² − n)]". The Richaud–Degert subfamily (n | λ), where class groups are controllable, is exactly the one
   killed by reciprocity.
3. **T1 = fibrewise LOCAL obstruction; family BM via (−1, D) on V_n, unramified iff n is a square (Prop 3.3); for
   non-square n every admissible fibre has empty BM obstruction, killed by the same prime ℓ ≡ 3 (4) ∥_odd D that
   T1 uses at squares (Prop 3.4).**

## Results (labels as in the file)
* §1 literature verified from arXiv full texts (GS Thm 1.1/1.2, (1.8), App. A; LM Thms 1.1–1.5, Prop 2.4; CTWX
  Thm 1.1; Dao Thm 1.3). Erratum for LITERATURE_AUTOMORPHIC.md: the author of 2202.07142 is Quang-Duc Dao.
  GS-type counting does not transfer: F_n = ABC − nA² − B² represents every level trivially (line A = B = 1); the
  ES content is "level divides a coordinate" (2D | C) = B2.
* Prop 2.1 (PROVED): S_{n,D} smooth, closure has one A₂ point, conic bundle over the C-line; both Vieta involutions
  fix C (no Markoff mixing, no compact fundamental set). Prop 2.2 (PROVED modulo standard facts):
  Pic Ū = ℤ(χ_{−D}) ⊕ ℤ(χ_{−nD}), Br/Br ℚ = (ℤ/2)² = ⟨(A, −D), (B, −nD)⟩, no transcendental classes.
* Lemma 3.1 (PROVED): admissible D ⟺ D ≡ 3 (4), gcd(D, n) = 1, all ℓ | D have (−n/ℓ) = 1. Cor 3.2, Props 3.3, 3.4.
* Thm 4.1 (norm form), 4.2 (CF), 4.3 (depth 3) PROVED. Thm 5.1 (PROVED): no polynomial families (A, B, λ)(s) at
  fixed D for non-square n (unit-group/norm-sign argument).
* §6 EVIDENCE table + Prop 6.1 (Assessment): barrier reading of the λ-direction.
* Prop 7.1 (PROVED): B = 1 locus is Siegel-finite per fibre, each Pell orbit meets it at most once (μ > 2n);
  composition gives wrong sign (two factors) or deeper points (three) — O201 spark 3 does not reach ES.

## Honest caveats for the reviewer
* §4 "Reading" (Euclid pattern of (n, t) beyond depth 3, branching mod constant Q's) is computed only for the
  first steps; labelled Assessment.
* Prop 6.1(a) cites the half-dimensional sieve for the local layer without re-derivation.
* Prop 2.2(c) transcendental argument: check the residue computation (sign conventions) independently.
* Equivalence in Thm 4.2 excludes μ ≤ √(4n/3) (finitely many Pell equations, not handled).

## Sparks (not pursued)
1. Prove the depth-structure theorem: for fixed n, each CF depth contributes finitely many μ (depth 3 = ES finite;
   is depth ≤ K finite for every K?). Then ES^{[2]} = ∪_K (finite searches), ES = K = 3.
2. Connect Thm 4.3 with DEDEKIND (J)9 / bsA_fricke F3 (Zagier cycles of length 3): is there a single CF/geodesic
   object in which both "length 3" statements are the same?
3. Class-group input: does any known result on real quadratic orders in families (e.g. Fouvry–Klüners-type 4-rank
   control, Davenport–Heilbronn 3-parts restricted to polynomial families) give "ideal above D principal for some
   λ" for the family 4(λ²D² − n)? Even a conditional (GRH + Cohen–Lenstra-type) theorem would be a clean target.
4. Two-parameter freedom: vary (λ, D) jointly with D | μ for μ highly composite (Davenport-constant pigeonhole in
   Cl⁺(O_μ), target the order-2 narrow class τ); quantify when h⁺(O_μ) is small enough.
5. ES^{(y,1)}: B squarefree is not preserved by Pell orbits (R201 M3); in the CF picture it is a condition on
   μq_{k−1} − p_{k−1}; check whether squarefree B occurs with positive frequency among deep hits (expected: 6/π²·c).
