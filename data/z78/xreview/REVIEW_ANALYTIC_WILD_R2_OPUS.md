<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="ed7b5eb5d">
A separate reviewer subagent was asked to review the changes in `git log ed7b5eb5d..`. Its request and review follow.

Request: review changes since ed7b5eb5d carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Fresh independent Claude Opus hostile review of Round 2 (math, not just code). Re-derive the claimed 20/63 exponent and 7/22 intermediate independently. Attack all steps in §§6–10 especially positivity/enlargement, various Cauchys, phase centering and signs, stationary expansion error in Q at quartic endpoint, cap/Abel/tail uniformity, square-frequency multiplicities and all LP checks. Check the exact hypotheses of each external input (Weil, classical stationary phase theorem with smooth parameters, additive large sieve, prime MPZ and Dirichlet GRH). Look for a fatal gap, check comparisons with old records. Only read relevant notes, no edits, never write outside the lane directories. Python via 'ulimit -v 6000000; timeout 180 uv run --offline --no-project python ...'. Return full critique, verdict, required repairs and any provider/auth/quota errors.

Commit log:
commit b4e34a1e90bc64a8ea0b06545058d5e4c99ea33b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:06:39 2026 +0100

    z78 R2: check MPZ residue and moment-depth quantifiers

 notes/z78/ANALYTIC_WILD.md | 8 ++++++++
 1 file changed, 8 insertions(+)

commit 0159f8a345ca2e6bc74566b5dc9659414e6b7728
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:06:01 2026 +0100

    z78 R2: relative relation deletion saves log-three off sparse progressions

 notes/z78/ANALYTIC_WILD.md | 6 ++++++
 1 file changed, 6 insertions(+)

commit 98f458d94b326744da9eda057a8b40e3ae850379
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:04:56 2026 +0100

    z78 R2: fourth moment of quadratic conductor sums reaches 20/63

 data/z78/analytic_r2_lp.txt |  4 ++++
 notes/z78/ANALYTIC_WILD.md  | 12 ++++++++++--
 scripts/z78_analytic_r2.py  | 10 ++++++++++
 3 files changed, 24 insertions(+), 2 deletions(-)

commit 7d711bac7b8f91b07a6c8479bb81339232941957
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:03:20 2026 +0100

    z78 R2: improve pointwise R(n) exponent to 7/22 by positive conductor enlargement

 data/z78/analytic_r2_lp.txt |  4 ++++
 notes/z78/ANALYTIC_WILD.md  | 53 +++++++++++++++++++++++++++++++++++++++++----
 scripts/z78_analytic_r2.py  | 15 +++++++++++++
 3 files changed, 68 insertions(+), 4 deletions(-)

commit d99771725bbf12494d95a0c56da0b76a563e6a6f
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:55:07 2026 +0100

    z78 R2: prove stationary-lift loss for the genuine completed off-diagonal

 notes/z78/ANALYTIC_WILD.md | 22 ++++++++++++++++++++++
 1 file changed, 22 insertions(+)

Review:
**Verdict: accept the mathematics of §§7–8 with minor repairs. I found no fatal gap. Do not promote yet: the §0 Review line is stale and the note mixes PROVED and CONDITIONAL results.**

I checked §§6–10 by hand, re-derived (8) and (9), ran my own threshold search on the LP constraints, and checked the stationary-phase expansion numerically.

## Re-derivation of 7/22 and 20/63 (both confirmed)

**Positivity and enlargement (§7).** This step is valid.
- The shift identity gives Σ_C g z = H⁻¹ Σ_x g(x) Σ_i z(x+iQ). Cauchy with ‖g‖² ≪ (W/Q+1)Q² ≪ WN gives the stated bound.
- The right-hand side Σ_x|Σ_i z_Q(x+iQ)|² is ≥ 0 and depends on Q only through the smooth z_Q.
- So the average over the J ≍ N/log²N prime pairs is at most O(log²) times the average over all integers Q ∈ [N,4N].
- The square sieve only needs the average of S_Q, not the maximum. Triangle in ℓ, then Cauchy in Q, is legitimate.
- The expansion weights (H−h) do not depend on Q, so the absolute value can sit outside the Q-average in E_h.
- Replacing the C-cutoff by ψ(C/W) ≥ 1 on the positive detector only enlarges an upper bound. Mass stays ≪ Vn^ε. No C-endpoint Abel step is needed.

**Phase centring and sign.** I checked each piece:
- z_Q(x+hQ)·z̄_Q(x) has phase nℓh/(4x(x+hQ)) = A/(t²−(hQ/2)²). This is exact.
- When hQ is odd the lattice is ℤ+½, which only contributes a sign (−1)^m. That sign is constant on each parity class of Q.
- By the envelope theorem, ∂(critical value)/∂σ² = (y*²−σ²)⁻² = y₀⁻⁴ at σ=0. Hence ξ_m = (Ah²/4W⁴)(m/2Y)^{4/3}.
- Numerical check (/tmp/z78rev/bproc.py, W=3000, Y=6): the direct sum and the stationary-phase prediction with the exact critical value agree to about 10⁻³ relative. The quadratic-in-σ² expansion degrades only as Tσ⁴ grows. Sign and centring are confirmed.

**Bounds (8) and (9).**
- From (W/(N√T))·√Y·√(N³D₀), with D₀ = (1+Z)(1+Y/(ZN²)), I reproduce all four terms of (8).
- Using r₂(s) ≤ 4τ(s), the large sieve on Σc(s)e(ξs) gives a fourth moment ≪ N^{4+ε}D₀. Hölder over the O(Y) dual frequencies then reproduces all four terms of (9).
- The spacing claim ξ′_m ≍ Z/Y and the arc-multiplicity count are right.
- Abel summation before Cauchy/Hölder is fine, because sup_m|∂w_m| is uniform.
- The large-sieve point multiplicity is handled correctly by colouring.

**LP.** I wrote an independent bisection over the same constraint set (/tmp/z78rev/lp.py). The minimal admissible exponent is exactly 7/22 for (8) and exactly 20/63 for (9). 20/63 − 10⁻⁶ fails, and a 60×60 interior grid gives no violations. All constraints are affine, so checking the vertices suffices. The committed script replays identically to `data/z78/analytic_r2_lp.txt`. The two differences, 62/137313 and 205/174762, are correct.

**Quartic endpoint (§8).**
- At vertex 1, 20r−3t = 0, so Tσ⁴ ≪ n^{δ+o(1)}·log^{O(1)}. That only multiplies the Abel total variation by n^δ, which is acceptable.
- Stationary phase was applied to the exact phase first, so its constants are unaffected.
- **Important observation:** the binding term γ/4+d/2+j/2 ≤ γ−j and the quartic condition coincide at vertex 1. Both reduce to 20r ≤ 3t. So 20/63 is the limit of any method that truncates the Q-phase at quadratic order. Higher moments cannot help unless the σ⁴ term is kept, for example as a genuine quartic polynomial in Q with a Vinogradov mean-value estimate. The note should say this.

**Other side conditions hold:**
- 1−2γ > 0 holds at all vertices.
- HQ ≤ W follows from γ > j+2r.
- L ≳ 1 holds, including vertex 2 where r = 0 and P = log³n.
- ℓ-tails are negligible by Schwartz decay, and derivatives of b are uniform for |ℓ| ≤ Ln^δ.
- The stationary-phase error is actually W·T^{-3/2}; the note uses the weaker O(W/T), which is still fine.

**Consistency.**
- The method uses only ‖G‖₂ ≪ Q, so it also applies to the §1 mock rows. That is consistent with §1, whose floor is only below 3/10.
- The result removes the dependence on Trudgian–Yang, Bourgain, Huxley and Sargos; it beats the old 7955/24966 using classical inputs only.

## External inputs (hypotheses checked)
- **Weil:** formula (6) is correct; I re-derived it via Gauss sums, and the (s/p) factors cancel. Kloosterman bound with p∤AB. The cases d = 0, v ≡ 0 and c = 0 are handled explicitly.
- **Stationary phase:** this needs a uniform statement with parameters, such as Hörmander Thm 7.7.5 (or a Blomer–Khan–Young-type lemma): compact parameter family, |φ″| bounded below, fixed compact amplitude support. The note should cite one; it is currently uncited.
- **Large sieve:** Montgomery–Vaughan's (N−1+δ⁻¹), applied to integer frequencies Q² ≤ 16N² (squares 1+Q₁²... sums ≤ 32N² in §8). Correct.
- **MPZ:** Polymath8a Thm 1.1 is quoted accurately: coherent a_p classes, squarefree x^δ-smooth q ≤ x^{1/2+7/300−ε}, uniform in the classes.
- **GRH (§9):** √X·log(RD) = o(X/φ(D)) needs log D ≤ (1/6−ε)u. This holds since log D = O(√u·log u).

## §§6, 9, 10
- **§6:** correct as a majorant lower bound (a method barrier). |g(0)| = 1 needs h primitive, which is assumed. The band of length ≍ MT/W with T/W ≍ U → ∞ gives at least √T·Σ|c_b| ≥ √T. It is low-stakes and correctly scoped.
- **§9:** correct.
  - The bad primes depend only on S and B, so the excluded classes depend on T only.
  - Markov gives the O(e^{-k})φ(D) exceptional classes.
  - The log-cap 2u/(k+1)+O(k) = O(√u) checks out.
  - Scope is honest. It still needs a triage class, and should note that it is weaker than the existing almost-all cap results in EXSET_LINNIK_CAPS.
- **§10:** correct (identity Q_K = C(Z−1,K), Bonferroni gap C(Z,K+1), μ ≪ (ϑλ)^{3/4}). It largely restates `paper/sieve-limits-note.tex` lem:depth and the 3/4-sharpness. The only new parts are the K ≥ 6μ converse and the MPZ check, and the note should say so. Triage: NULL/BARRIER-SCOPED.

## Required repairs (form and scope)
1. **§0 Review line is now misleading.** The archived Opus review predates §§6–10. Mark "§§6–10: cross-review owed" until the hostile review is archived.
2. **Split the note.** AGENTS asks for one note per task and a one-sentence Result. Move §§6–8 to, say, `notes/z78/ANALYTIC_R2.md` with Label "PROVED rel. Weil (via Z53 Lemma W/z76 §2), uniform stationary phase, additive large sieve, r₂ ≤ 4τ". At present the PROVED headline sits under "Label: CONDITIONAL on GRH".
3. **STATUS delta.** It should say the bound drops the Trudgian–Yang, Bourgain, Huxley and Sargos dependence and supersedes both 8/25 and 7955/24966. It should also flag that FRONTIER §3/§7.1 benchmarks need updating at export.
4. **Missing pieces in §§7–8:**
   - cite a specific stationary-phase theorem;
   - add the replay command and output path for `scripts/z78_analytic_r2.py`;
   - state the 20/63 quartic-truncation limit as the next step.
5. **Wording:**
   - "without an exponent-pair conjecture" → "without any exponent-pair input" (Trudgian–Yang's pairs are theorems);
   - "ordered c=1 line" in Scope is undefined; point to the R(n) definition in z76 §0.
6. **§9 and §10** each need a triage class; §9 also needs the EXSET_LINNIK_CAPS comparison above.

No provider, auth or quota errors. Two scratch check scripts are in /tmp/z78rev/ (outside the lane directories, as noted); no repository files were edited.
</code-review>
