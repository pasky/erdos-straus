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
1. **BL recorded exactly** (§1). For fixed n, "BM is the only obstruction to the integral Hasse principle" is
   literally ES(n), because BL Thm 1.8 says the Brauer set is non-empty. Strong approximation fails for every n
   even with Br (BL Thm 1.9). So aim (A) for fixed n is a restatement of ES, not a reduction.
2. **Models, PROVED** (§2). All 9 lines are rational. Toric model (Prop 2.1): `Ũ_n` is `ℙ²` blown up at one
   point on each side of the triangle, the three points collinear, which produces the node. Positive points:
   primitive `s ∈ ℕ³` with `4s_i | nS`. Prop 2.2 gives the matrix forms. Type I is `SL₂(ℤ)` with `g` even,
   `g | h`, `2h | n+f`. Type II is the same with `det = n` and `2h | f+1`.
3. **No Pell fibres, PROVED** (§3). The conic bundles (F1)–(F3) all have split torus fibres. α restricts to
   `(n(n−4t), −w)` and `(−λ, −nZ)`; this was checked at every place on about 10⁵ points. α is horizontal and
   `Br_vert = Br ℚ`. Thm 3.1 (via BL 3.10): only lines carry infinitely many integral points. Prop 3.2: every
   non-split 1-dim torus maps constantly to `V_n ≅ G_m²`. **Aim (B) is answered negatively for every fibration
   of `U_n`.**
4. **Homogeneous spaces** (§4). S-integral reformulations cannot help (PROVED, elementary). On `X_d`
   (Spin(2,1)/T, real place non-compact, integral points are Heegner forms, SA holds), the ES points form an
   affine modification adjoining `κ_p = (f+p)/4da`. Each member of the pencil is a split conic, and the
   condition is a congruence modulo a coordinate of the point (Prop 4.1, PROVED). Cor 4.2: SA, descent and
   fibration outputs cannot produce it; shrinking-target equidistribution is needed. The sentence "collapses
   into the spectral route" is an Assessment.
5. **The Brauer class is genus theory, PROVED** (§5; checked on all 43812 Type I/II ordered solutions with
   p < 2500).
   * Type I: α is exactly `(−d/p) = −1`, i.e. p is inert in `ℚ(√−d)`.
   * Type II: α is automatic quadratic reciprocity `(f/p) = −(−1/p)`, which is O128's genus lemma.
   * So the Brauer–Manin obstruction rules out exactly the Type I levels with `(−d/p) = +1`, and never a Type II
     level.
   * This identification of BL's α is probably folklore-adjacent (Yamamoto). **Novelty unchecked.**
6. **EVIDENCE** (§5.3). Single fixed levels fail for a few percent of primes `p ≡ 1 (24)`:
   * Type II at d = 1: 73 failures below 1.5·10⁶;
   * Type I at d = 7, 11, 13: 7%, 4% and 14% below 10⁵, with complete searches and brute-force spot checks;
   * exception: "identity levels" such as d = 5, which cover all of `(5/p) = −1` with a = 1;
   * the failures are not square-mimicking.
7. **Scope table** (§6), machine by machine: SA/BM, fibration method, Harpaz/Swinnerton-Dyer descent (needs
   non-split fibres, and here everything is split), Markoff orbits, SA on `X_d`, Duke.
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
