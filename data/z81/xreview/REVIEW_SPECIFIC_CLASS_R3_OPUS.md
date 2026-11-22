<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="b57c615a4">
A separate reviewer subagent was asked to review the changes in `git log b57c615a4..`. Its request and review follow.

Request: review changes since b57c615a4 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Final narrow hostile Claude Opus check of the new fixed-tilt and endpoint-tilt fixed-band calibration in notes/z81/SPECIFIC_CLASS.md, including that the integer square floor gives only a lower bound on the certificate void and the claimed conditional exponent is correct. Check closure of R2 changes. Do not write files. No compute needed; please distinguish audited from unresolved claims. No priority claim is intended.

Commit log:
commit b3a81b26c37f699d2cad04a7a2f386b30b8a8dc6
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:29:48 2026 +0100

    z81: calibrate the physical diagonal at fixed tilt and the square floor

 data/z81/xreview/REVIEW_SPECIFIC_CLASS_R2_OPUS.md | 83 +++++++++++++++++++++++
 notes/z81/SPECIFIC_CLASS.md                       | 28 +++++---
 2 files changed, 101 insertions(+), 10 deletions(-)

Review:
**Verdict: ACCEPT with minor fixes.** I re-derived the new fixed-tilt and endpoint-tilt calibration and found no mathematical defect. The conditional exponent is correct. The square floor is used correctly: it is a lower bound on the certificate void, never on E(N). All the substantive R2 points are closed. No proof of ES is claimed, and nothing needs flagging to the user.

## Audited and correct

**Fixed tilt, z=2.**
- m_q = 1 + L^{−I_*+o(1)}, so Σlog m_q = o(J). This needs only W's upper bound on the marginal.
- If K ≤ e^{ρJ}, then the failures are ≪ L + X·e^{ρJ+o(J)}·2^{−J}. That matches the note.
- J ~ L/(2l), so the saving exp(−cL/l) beats exp(−L^θ) for every θ<1, but it is not a power saving. Correct.
- K ≤ 2^J = X^{o(1)} holds trivially. So "K = X^{o(1)} is useless" is right, and ρ < log 2 is the first non-trivial condition.

**Endpoint tilt, band AL<q≤2AL with z = L^{I_*}.**
- J ~ AL/(2l), so z^J = X^{AI_*/2+o(1)}.
- log m_q ≤ log(1+L^{o(1)}) = o(l), so Σ log m_q = o(L) and ∏m_q = X^{o(1)}. Only the upper marginal is needed, and both displayed inequalities use only that.
- Failures ≪_A L + X^{1−AI_*/2+o(1)}K_A. Correct; the wrap cost is O(AL).
- The squares give K_A ≥ X^{−1}·≍X^{1/2}·z^J/∏m_q = X^{AI_*/2−1/2+o(1)}. Here F1 makes every window in the band miss −1, including the cases q|s and 2|m, which hold for any q ≡ 3 mod 4.
- I_* = 0.004155, so A = 1/I_* ≈ 240.7. Then K_A = X^{o(1)} gives a dyadic count of X^{1/2+o(1)}, and dyadic summation gives E(N) ≤ N^{1/2+o(1)}. This is exactly where the hypothesis stops contradicting the squares. For A > 1/I_* the conclusion stays at 1/2. So "does not beat the square floor" is correct.
- **Square floor scope.** It bounds the *untrimmed* certificate void from below. Odd squares are not ES exceptions. The actual void may be larger, and a functional that trims out the squares is not covered. The wording "of this certificate family" and the §5 table ("No untrimmed … exponent below 1/2") are consistent with this.
- **Saturation, unstated but supporting the claim.** z/m_q ≤ 1/𝔼F_q = L^{I_*−o(1)}, so no z beats AI_*/2 at width A. Taking z = L^{I_*} is optimal up to X^{o(1)}. This also reconciles the calibration with R2's "ratio increases with σ" remark: the ratio increases but saturates.
- **W/S at fixed A.** The only new input is log M = l + O_A(1) in j_0. The conditions R > q and the Siegel–Walfisz range still hold. In S the L^{−β} factor becomes 1/q ≍ 1/(AL). I audited this as a sketch.

**R2 closure.** Checked against the diff:
1. The §0 label now lists PNT mod 4, BM §2.2 (Thm 2.2 checked in FRONTIER) and Rankin, and the K_mix heading is fixed. ✓
2. The triage is split, with proposed §6 and §7 lines for the exporter. The §6 direction matches P. ✓
3. The (DR) Assessment is renamed to f = 4ac−1. The algebra checks: c^{−1} ≡ 4a mod f, so −ac^{−1} = −4a², and the cofactor is b. ✓
4. The CERTIFIED disclaimer is added. ✓
5. Priority: an R.R. Hall reference was added, and the note keeps "no priority claim". Only partially closed (see below).

R2's challenge that the H⁻_BM arrow is only a strength comparison is now stated plainly. The WP "dominated by 3/4" sentence is added. ✓

## Critique and fixes owed

1. **The hypotheses are strictly stronger than the conclusions they give.**
   - K ≤ e^{ρJ} is an exponential-moment bound on the number of holes. Its all-holes face *is* the void bound, and partial-hole rows add to it.
   - K_A = X^{o(1)} is stronger than simply assuming "void in [AL,2AL] ≤ X^{1/2+o(1)}". That simpler assumption gives the same E(N) bound with no tensor at all.
   - The only extra value of the tensor form is the Fourier route (4). The real new content of the calibration is heuristic: independence predicts a void of X^{1−AI_*/2}, which meets the square floor at A = 1/I_*.
   - The note should say this. Otherwise "how strong a new input would be needed" undersells how strong it is.
2. **"Exact exponent accounting"** reads like K_A ≍ …. It is one upper bound and one lower bound. Say "explicit", and add the saturation remark above.
3. **Label.** "PROVED rel. S and PNT" covers a one-sentence uniformity claim. W as stated (fixed β ∈ [0.9, log 3), q ∈ [L^β, 2L^β]) does not literally cover A > 2 or A < 1. Relabel as "rel. the uniform-in-band version of W/S".
4. **Trybushnyi sentence.** It is an unlabelled comparison inside a PROVED paragraph, with no pointer. `notes/z81/LIT.md` is not in this worktree; it exists on the z81-lit branch (983637e4e, §0.5). That source is consistent with the sentence ("fixed level improves constants, not exponent"). Mark it Assessment and point to LIT §0.5.
5. **§0 Review line.** It cites R2 as incorporated, but the calibration paragraphs came after R2. They should be marked as covered only by this narrow R3.
6. **Wording.** "Conjectural subpolynomial restriction" should be "hypothesised". Do not promote it as a TARGET: it sits exactly on the F1 boundary, with K_A ≥ X^{o(1)} forced.
7. **Overlap.** The fixed-tilt paragraph overlaps the existing θ>3/4 subpower sentence in §3. That is harmless; a cross-reference would do.

## Unresolved (not audited here)
- The content of the Hall paper behind the link (not fetched), and priority for the variant with divisors of m² and ratios. The priority search is still owed.
- Trybushnyi's §11 comparison (relayed via LIT.md only).
- A full write-up of W/S uniform in A; only the sketch is audited.
- (DR), K_A = X^{o(1)}, K ≤ e^{ρJ} and K_mix themselves: all open by design.
- Whether any ES-soluble family other than squares gives a larger certificate void. I found none with a uniform reciprocity obstruction, e.g. among k·s² for k ≠ □, but did not check exhaustively.
</code-review>
