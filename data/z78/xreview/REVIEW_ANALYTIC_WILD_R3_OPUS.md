<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="203dfee1d">
A separate reviewer subagent was asked to review the changes in `git log 203dfee1d..`. Its request and review follow.

Request: review changes since 203dfee1d carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Fresh independent Claude Opus hostile review of R3 §§11–13 of notes/z78/ANALYTIC_WILD.md. Independently re-derive the rational LP (1472/4637, 286/901, 272/857) and uniform M dependence; attack inverse phase spacing and Titchmarsh 5.13 *exact range*, small Z, Δ, ET frequency sums and boundary arcs, local J reduction, quartic coefficient −1/3, exact stationary error and Abel, fourth moment for frozen complex weights. Verify no overtransfer to fII, ES5, N2. Check and state any reviewer provider/auth/quota errors. No file writes, no commits, no /tmp scratch code; all checks in memory via 'ulimit -v 6000000; timeout 180 uv run --offline --no-project python ...'. Return full verdict, defects and required repairs. Round 2 proof is reviewed separately; examine dependencies necessary for R3.

Commit log:
commit ea376720c4e68dc3cc4c811a0f198c9ba93c587e
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:35:58 2026 +0100

    z78 R3: quantify numerator dependence and exact scope of Type II and ES5 transfers

 data/z78/analytic_r3_lp.txt |  6 ++++++
 notes/z78/ANALYTIC_WILD.md  | 18 +++++++++++++++++-
 scripts/z78_analytic_r3.py  | 13 +++++++++++++
 3 files changed, 36 insertions(+), 1 deletion(-)

commit 7be0f5bb56a1ee02fcd687a0cef840395d35f6f0
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:33:07 2026 +0100

    z78 R3: a localized inverse fourth derivative keeps the quartic phase, reaching 272/857

 data/z78/analytic_r3_lp.txt |  8 ++++++++
 notes/z78/ANALYTIC_WILD.md  | 26 ++++++++++++++++++++++++--
 scripts/z78_analytic_r3.py  | 14 ++++++++++++++
 3 files changed, 46 insertions(+), 2 deletions(-)

commit 57aea294cd843fabda96bb64aaae66265c9fbe70
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:30:31 2026 +0100

    z78 R3: inverse-phase spacing beats 20/63 at the binding block

 data/z78/analytic_r3_lp.txt |  4 ++++
 notes/z78/ANALYTIC_WILD.md  | 10 ++++++++++
 scripts/z78_analytic_r3.py  | 13 +++++++++++++
 3 files changed, 27 insertions(+)

Review:
**Verdict: ACCEPT with minor repairs.** I found no mathematical gap that breaks §§11–13. The headline `R(n) ≪_ε n^{272/857+ε}` follows from §12 together with §§7–8 as written. Round 2 (§§7–8) was taken as given. The improvement over 20/63 is tiny: 4/53991 ≈ 7.4·10⁻⁵, so the new exponent is ≈ 0.317386. Every defect below is about form or exposition, not substance.

**Reviewer errors:** none. I used no subagents and no external models, so there were no provider, auth or quota errors. All checks ran in memory under `ulimit -v 6000000; timeout 180 uv run --offline --no-project python`. I wrote no files.

## What I re-derived and checked

- **The three LP exponents.**
  - The R3 script output is byte-identical to `data/z78/analytic_r3_lp.txt`.
  - My own re-implementation finds 1472/4637, 286/901 and 272/857 each feasible, and each infeasible at t − 10⁻⁹. So each is the exact threshold for its stated parametrisation.
  - The vertex-1 algebra checks out by hand:
    - §11: 19v/60 + 38/15 + 20 − 3v ≤ v − 2 gives v = 1472/221.
    - Intermediate: v ≥ 286/43.
    - §12: 41v/60 ≥ 68/15 gives v = 272/41.
    - At v = 272/41 the penalty K is 4/857 > 0, so the subdivision into J subintervals really is needed.
    - The new fifth term has slack 33/23996, and the sextic and localisation conditions are strict.
- **Checking only the vertices is valid.** r, j and d are affine. K = max(0, affine) is convex, so "goal − max of terms" is concave and the strict conditions are convex.
- **Uniform dependence on M.** The region over μ ∈ [0, 1/3] is the convex hull of the six endpoint vertices, since each vertex is affine in μ. A 31 × 231 grid over μ and the triangle gave no failure; the minimum slack is 0, at the binding vertex. The exponent bookkeeping is right: 1 − 4θ = −231/857, and the two bounds in (12) cross at M = n^{1/4}.
- **Quartic coefficient −1/3.**
  - The implicit derivative is y′ = (2/3)y₀⁻¹ ✓.
  - The second derivative of the critical value is −(2/3)y₀⁻⁶, so the coefficient is −1/3 ✓.
  - Newton iteration at μ = 2, 1, 0.7 gives −0.33333…
  - The note's unexplained "1 − 8/3 + 4/3" is the three Taylor contributions, ½φ_ss + φ_ys·y′ + ½φ_yy·y′².
  - ζ_m ∝ m² exactly, which is the only property the argument uses.
- **Inverse phase spacing.** Each step checks:
  - f′ ≍ Y/Z gives the window Δ = Y/(ZN²), and each v contributes O(1) when Δ ≪ 1.
  - A²(1/2,1/2) = (1/14, 11/14).
  - Choosing B = (Z⁴/Y)^{1/15} balances to Z^{11/15}Y^{1/15}, which matches the trivial O(Z) exactly when Z⁴ ≤ Y.
  - The new exponent W^{19/60}Y^{27/60}h^{11/30} is correct.
- **Titchmarsh 5.13 with k = 4.** With K = 8 the bound is M·λ^{1/14} + M^{3/4}·λ^{−1/14}. It needs only an interval length b − a ≥ 1 and |f⁽⁴⁾| between fixed multiples of λ. There is no restriction on the size of λ, and the implied constant is absolute.
  - Here f⁽⁴⁾ < 0, so conjugating is fine.
  - The comparability ratio (c₂/c₁)^{13/4} is absolute.
  - Summing over the J subintervals and over frequencies l ≤ B gives exactly the displayed bracket and (11): Z(BY/Z⁴)^{1/14} = Z^{11/15}Y^{1/15}, and the second term is J^{1/4}Z^{29/28}Y^{−1/14}.
  - Subintervals shorter than 1 cost O(1) each, which is the J term.
- **J absorbed into Z/B.** J ≍ 1 + T(hN/W)⁴ equals 1 + Z(hN²/W)² identically. The localisation condition plus B ≤ Z^{4/15} (using Y ≫ 1) gives J ≪ 1 + Z/B, and the LP checks this strictly.
- **Small Z and large Δ.** Both are covered by the integer count (J + Z)(1 + Δ).
- **Fourth moment with frozen complex weights.** The squared coefficients satisfy |b_s| ≤ r₂(s) ≤ 4τ(s) and Σ|b_s| ≤ 9N². The large sieve is applied per subinterval I, with D_I as its spacing count. Hölder over all O(Y) dual indices gives W^{1/2}Y^{1/4}(Σ D_I)^{1/4} ✓.
- **Stationary phase and Abel summation.** The family is compact in (σ, m/Y) independently of T. The O(W/T) error per (m, Q), summed over m, is O(1). After freezing, the residual is (ζ_m − ζ_{m_I})Q⁴ plus a T·σ⁶ term, and it has bounded variation in Q under the sextic condition. In §11 the full variation T(hN/W)⁴ is charged instead. Abel summation uses a common Q endpoint for all m ✓.
- **Higher moments remark.** The normalised 2s-th moment is ≪ N^{o(1)}Σ D_I, and Σ D_I ≤ Y, so s = 2 is best in this black box ✓.
- **Numerator M (§13).** I checked against z76 §2:
  - The detector becomes (Mdk − n)² − 4k, with discriminant 16(Mdn + 1).
  - When p | M the local polynomial is n² − 4k, linear in k: its DC term is 0 and its other Fourier coefficients are Gauss sums of modulus √p, so Σ|G|² ≤ Q².
  - The Poisson length is L = MNW/V and the phase is −ℓX/(Qd).
  - The zero frequency costs V/(MQ) + V/(MW).
  - The new Y exponent is d_* = d + μ.
  - The elementary identities b(Mad − 1) = n + a and (Mda − 1)(Mdb − 1) = Mdn + 1 hold, and the ratio bound ≥ 1/6 holds.

## No overtransfer

- **f_II:** the note is correctly scoped. The direction R₄(p) ≤ f_II(p) is right. The c-slices 4abcd = a + b + nc match the repo's Type II form, and summing over c costs exponent θ + (2 − 3θ)/5 ≈ 0.527 > 2/5.
- **ES₅:** the bound is an upper bound on the number of words only; there is no lower or positivity claim.
- **N₂:** the bound min(U, n^θ) = U is explicitly vacuous.

## Defects and required repairs

1. **(Form, required)** The §0 Review line still lists only the §§1–5 and §§6–10 reviews, while Result, Label and STATUS delta already carry 272/857. Add "§§11–13: cross-review owed" (or point to the archived file once one exists). Under AGENTS §3 the record cannot be promoted until then.
2. **(Form, required)** The §0 Scope line is stale. Add the uniform bound (12) for R_M, the ES₅ word-count upper bound, and the explicit non-transfers to f_II and N₂.
3. **(Exposition)** §11's exponent-pair citation ("A process and second derivative test; equivalently translate any fixed shift…") is vague and does not quote the definition's range conditions. Better: derive (10) as the J = 1 case of (11) via Titchmarsh 5.13, which also keeps the second Titchmarsh term. I checked that 1472/4637 still holds with that extra term (slack 57/32459). The headline does not depend on §11.
4. **(Notation)** Three clashes:
   - J means the number of prime pairs in §§6–7 but the number of subintervals in §12.
   - Δ means the large-sieve spacing in §7 but Y/(ZN²) in §§11–12.
   - The script and data file use "m"/"R_m" for the numerator, against §13's own M convention.
5. **(Exposition)** Spell out "1 − 8/3 + 4/3" as the three Taylor terms listed above.
6. **(Minor)** §13's "entire triangle without β ≥ α" is harmless but superfluous: the detector strip normalises by the larger of U and V, and the a ↔ b symmetry gives U ≤ V anyway. Say so.
7. **(Pointers)** The precise slot-test statement is in `EXSET_I3.md` §4.6, and §7.1 defines ES₅ only on n ≡ 1 (mod 4). The bound is fine for all n, but cite accurately.
8. **(Pointers)** The f_II bullet's "binding scales of ET Prop 1.7" is not verified anywhere in the repo. Cite it or mark it as an illustration.
9. **(Replay)** Add a replay command for the R3 script to §12, and a header to the data file, as §8 has for R2.
10. **(Presentation)** In the STATUS row, give the decimal (0.317386) and the size of the gain, so a gain of 7·10⁻⁵ over 20/63 is not read as a large jump.
</code-review>
