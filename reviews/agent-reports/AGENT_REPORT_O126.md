# AGENT_REPORT_O126 — arithmetic geometry of ES (checkpoint 1)

Branch `side-agent/geometry-es`; main file `GEOMETRY_ES.md`; scripts `scripts/geo_common.py`,
`geo_models.py`, `geo_fibrations.py`, `geo_genus.py`, `geo_levels.py`, `geo_levelsI.py`.

## Bottom line
I proved no theorem toward ES, conditional or not. The deliverable is a precise, mostly PROVED map of why the
fibration, descent and strong-approximation machinery cannot reach ES, and where the one honest homogeneous
space sits. That space is the hyperboloid `X_d : ef − 4da² = 1` (Type I), resp. O128's level-`dp` space
(Type II). On it the ES condition is a **shrinking target with a point-dependent modulus**, which is
spectral territory.

## Results (labels as in the file)
1. **BL recorded exactly** (§1). For fixed n ≥ 2, "BM is the only obstruction to the integral Hasse principle" is
   literally ES(n), because BL Thm 1.8 says the Brauer set is non-empty. Strong approximation fails for every n
   even with Br (BL Thm 1.9). So aim (A) for fixed n is a restatement of ES, not a reduction.
   (R126 repair: BL Thm 1.8 is false at n = 1. There the Brauer set is empty, so the equivalence holds only for
   n ≥ 2. BL Thm 1.9 concerns rational points `U_n(ℚ)`.)
2. **Models, PROVED** (§2). All 9 lines are rational. Toric model (Prop 2.1; R126 repair: symbolic proof via
   Cayley's six-point model added): `Ũ_n` is `ℙ²` blown up at one
   point on each side of the triangle, the three points collinear, which produces the node. Positive points:
   primitive `s ∈ ℕ³` with `4s_i | nS`. Prop 2.2 gives the matrix forms. Type I is `SL₂(ℤ)` with `g` even,
   `g | h`, `2h | n+f`. Type II is the same with `det = n` and `2h | f+1`.
3. **No Pell fibres, PROVED** (§3). The plane-conic bundles (F1)–(F3) all have split torus fibres. α restricts to
   `(n(n−4t), −w)` and `(−λ, −nZ)`; this was checked at every place on about 10⁵ points. α is horizontal and
   `Br_vert = Br ℚ`. Thm 3.1 (via BL 3.10): only lines carry infinitely many integral points. Prop 3.2: every
   non-split 1-dim torus maps constantly to `V_n ≅ G_m²`. **Aim (B) is answered negatively for every fibration
   of `U_n`.** (R126 repair: the reason is Thm 3.1 = BL Lemma 3.10, a real-place bound valid for every curve.
   Prop 3.2 covers only curves inside `V_n`: fibres meeting the lines can be punctured non-split tori. So "all
   conic bundles are split" is not claimed. The (F2) restriction of α now has a proof, and the "n²" size bound is
   corrected to `≪ n⁴`.)
4. **Homogeneous spaces** (§4). S-integral reformulations cannot help (PROVED, elementary). On `X_d`
   (Spin(2,1)/T, real place non-compact, integral points are Heegner forms, SA holds), the ES points form an
   affine modification adjoining `κ_p = (f+p)/4da`. Each member of the pencil is a split conic, and the
   condition is a congruence modulo a coordinate of the point (Prop 4.1, PROVED; R126 repair: `c ≠ 0` is needed,
   because without it `Σ^I_{p,d}(ℤ)` is infinite when (−d/p) = +1). Cor 4.2: SA, descent and fibration outputs
   cannot produce it; shrinking-target equidistribution is needed. R126 repair: the PROVED core is now stated
   precisely: for open `W_f ⊂ ∏X_d(ℤ_ℓ)`, the set `X_d(ℤ) ∩ W_f` is empty or infinite, while the ES set is finite.
   The rest, including "collapses into the spectral route", is an Assessment.
5. **The Brauer class is genus theory, PROVED** (§5; checked on all 43812 Type I/II ordered solutions with
   p < 2500).
   * Type I: α is exactly `(−d/p) = −1`, i.e. p is inert in `ℚ(√−d)`.
   * Type II: α is automatic quadratic reciprocity `(f/p) = −(−1/p)`, which is O128's genus lemma.
   * So the Brauer–Manin obstruction rules out exactly the Type I levels with `(−d/p) = +1`, and never a Type II
     level.
   * R126 repair, novelty settled: **not new**. Prop 5.2's `(p/f) = −1` is Yamamoto 1965 Lem. 4 (Mordell's
     `q = 4abd − 1` = ET's f), and BL Appendix A already derives it from α. Prop 5.1 is folklore: the Mordell/ET
     families `n ≡ −f (mod 4ad)` only cover non-residues mod 4d. R126 also added a local form: at level d with
     (−d/p) = +1 the positive adelic Brauer set of the level-d chart is empty.
6. **EVIDENCE** (§5.3). Single fixed levels fail for a few percent of primes `p ≡ 1 (24)`:
   * Type II at d = 1: 73 failures below 1.5·10⁶;
   * Type I at d = 7, 11, 13: 7%, 4% and 14% below 10⁵, with complete searches and brute-force spot checks;
   * exception: "identity levels" such as d = 5, which cover all of `(5/p) = −1` with a = 1;
   * the failures are not square-mimicking.
   * R126 reproduced all counts and level sets exactly with independent code.
7. **Scope table** (§6), machine by machine: SA/BM, fibration method, Harpaz/Swinnerton-Dyer descent (needs
   non-split fibres; R126 repair: (F1)–(F3) are split, and finiteness on every fibre comes from Thm 3.1),
   Markoff orbits, SA on `X_d`, Duke.
   The sufficient target (SHT) is stated; it is **not** a standard conjecture.

## Flags for other agents
* O124/O128: §5.2 dictionary. `q_d = ef − 4da²` is the only non-split quadratic structure, because every
  two-variable slice is split (Prop 3.2). This is consistent with O124.
* O123/O127/O128: the pointwise problem is (SHT), i.e. integral points of `X_d` with `f ≡ −p (mod 4da)`, at
  some level `d ≤ (log p)^K` with `(−d/p) = −1`.

## Weak points a reviewer should check
* Prop 2.1 (toric model) is argued geometrically, with only a consistency check, no symbolic proof. The
  Markoff comparison is from memory.
* The `Br_vert = Br ℚ` argument for (F1) is sketched in the standard residue form.
* The completeness bounds used in §5.3 (`a ≤ √p/2+1` for Type II; ET Lemma 2.8's `a ≤ 3p/4d` for Type I)
  deserve a check. The brute-force cross-checks only cover p < 1100.

## Possible round 2 (parent's choice)
(a) Make (SHT) quantitative: compute the expected count per level and the failure law over many levels.
(b) Classify *all* genus-0 fibrations of `Ũ_n`, not only those coming from lines. Thm 3.1 already makes this
moot arithmetically.
(c) A literature check of the "α = genus character" identification.

## R126 repairs (applied by the reviewer)
D1–D10 and remarks R2–R4 of `reviews/geometry-es-review.md` have been applied in `GEOMETRY_ES.md`, each marked
"(R126 repair)". The repairs are:
* n = 1 is excluded from BL Thm 1.8 and from the §1 equivalence;
* the BL Thm 1.9 quote is corrected;
* a symbolic proof of Prop 2.1 is added;
* the α|F2 restriction now has a proof, and the Br_vert sketch is made precise;
* the scope of Prop 3.2 and the Harpaz/SwD row are corrected (D3);
* the size bound is now `≪ n⁴`;
* §4.2 wording is fixed;
* Prop 4.1 now requires `c ≠ 0`, with a counterexample to the old statement and a finiteness proof;
* Cor 4.2 is restated in a precise provable form;
* Props 5.1/5.2 are attributed to folklore and to Yamamoto Lem. 4 via BL App. A, and the local BM form is added.
