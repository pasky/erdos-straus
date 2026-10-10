# AGENT REPORT O129: literature scout on spectral and geometric tools (2026-10-10)

**Deliverable:** `LITERATURE_AUTOMORPHIC.md`.
* About 600 lines and about 70 entries.
* Each entry has exact statements where they could be checked, verified links, and a "relevance to pointwise ES" paragraph ending with an Assessment label.
* Sections: (1) shrinking-target and small-scale equidistribution of Heegner points and closed geodesics, plus roots of quadratic congruences; (2) optimal strong approximation and covering exponents; (3) ternary forms; (4a) Bright–Loughran and its citers; (4b) log K3 / Markoff surfaces / the fibration method; (5) analytic and geometric work on unit fractions; (6) conditional results.
* §0 is an executive summary addressed to O123, O124, O126, O127 and O128.

**PDFs** (`sources/autgeo/`, 6.1 MB): Sardari 1510.00462, Browning–Kumaraswamy–Steiner 1609.06097, Parzanchevski–Sarnak 1704.02106, Rouse 1111.0979, Kane 2010, Harpaz 1511.04876, Ghosh–Sarnak 1706.06712. The Harpaz PDF is also archived in `sources/lit2026/`.

**Method.**
* Two rounds of research subagents drafted the sections; the drafts were then critically spot-checked against primary PDFs.
* Items checked against the primary text, and corrected where wrong:
  * Young Thm 2.1 and Prop 1.2; the scale was corrected to `V ≪ D^{1/24}` for balls.
  * Humphries Thms 1.22, 1.24 and 1.25. Thm 1.22 is Young's theorem over the full class group.
  * Sardari Thm 1.2 and Cor 1.1.
  * Ghosh–Sarnak Thm 1.2. The count was corrected to `√K(log K)^{−1/2}`.
  * Ono–Soundararajan, via Kane.
  * Elsholtz–Tao Props 1.6 and 1.9.
  * The two extra Bright–Loughran citers, Dahan and Xu 2605.23601, found by grepping the archived PDFs.
* All other entries rest on subagent checks of arXiv/publisher pages. Entries that are still unverified are labelled as such in the file (Golubeva, Bourgain–Gamburd–Sarnak and W. Chen links, the Santens/Wilsch/Jahnel–Loughran cluster, Jia's exact theorem).

**Findings (all Assessment-level; nothing new is proved).**
1. **No pointwise ES result.** No work found proves pointwise ES, conditionally (GRH, EH, Hypothesis H, abc) or unconditionally. No work found applies automorphic forms or Kloosterman sums to the *existence* of solutions of `4/n`.
2. **Bright–Loughran citers.** The census finds 6 verified citers: Mitankin–Uhlemann, González-Avilés, Bloom–Elsholtz, Xu 2609.29250, Dahan, Xu 2605.23601. All are contextual. Google Scholar suggests about 2–3 more are unidentified.
3. **Most actionable lead (O123/O128).** Young's Prop. 1.2 shows that spectral methods *do* give single-discriminant existence theorems: small roots of `b² ≡ −D (mod 4a)` in a thin region. The precondition is that the target area exceeds about `D^{−1/12}` unconditionally, or `D^{−1/4}` under Lindelöf. The constants are ineffective (Siegel). O123 should compute the area of the ES Type I target region for fixed `p` and compare.
4. **Sanity check.** Any such route must also pass Elsholtz–Tao's odd-square vanishing `f_I(n) = f_II(n) = 0` for odd squares `n`.
5. **Other benchmarks.**
   * Sardari's optimal lifting gives height `(m/r)^4` for `d ≥ 5` and `(m/r)^6` for `d = 4`, including determinant equations.
   * Harpaz gives existence only, with no real-place approximation.
   * For Markoff surfaces, the "almost all versus every" gap is quantified.

**Open items for the parent.**
* A full hostile check of the subagent-verified (not parent-verified) theorem statements, especially §3 (Blomer's exponents) and the §5 divisor-in-AP exponents.
* Possibly a citation census with Google Scholar access.
