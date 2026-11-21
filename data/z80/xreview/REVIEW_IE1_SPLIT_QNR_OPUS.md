<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="cec147eb6">
A separate reviewer subagent was asked to review the changes in `git log cec147eb6..`. Its request and review follow.

Request: review changes since cec147eb6 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab corollary check (scope deliberately tiny): validate the new paragraph at the start of §10 in notes/z80/IE1_SPLIT.md: equality of R/PR with the geometric localization, regular field extensions across every §9 fibre including target-zero sphere, least QNR exactly 2, independent prime squareclasses, failures of full QR and TS. Check it does not imply any other IE1^- consequence. Return commit hash, verdict and fixes concisely; no edits or computation.

Commit log:
commit 682ca95741413fa44e3b57d97cf91e522577ffd8
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:24:31 2026 +0100

    Identify the least nonresidue and squareclass obstruction at the bad prime

 notes/z80/IE1_SPLIT.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

Review:
**Commit reviewed:** `682ca95741413fa44e3b57d97cf91e522577ffd8` (`682ca9574`). It changes only `notes/z80/IE1_SPLIT.md`: a new first paragraph in §10 and a Review line saying "cross-review owed". I made no edits and ran no computation; this is a reading check against the note's §§3–4, 6 and 9 and z76 `IE1_BREAK.md` §1.

**Verdict: ACCEPT WITH MINOR FIXES.** The mathematics holds. Nothing in the paragraph implies any IE₁⁻ consequence.

**What I checked and found correct**
- **R/PR equals the localized fibre A/PA.**
  - P is a prime of a Bézout domain, so R/PR is a field.
  - By the factor calculus, P divides no nonzero element of B. So B∖{0} maps to units of R/PR, and K embeds in it.
  - P is not a unit in A, so localizing gives R/PR = A/PA. The text's "by localization of this field" is terse but right.
- **Every edge gives a regular extension on the fibre.** The base is K[X]/(1+JX) = K (§4).
  - **Free lines:** floors (§4), Dirichlet lines and the extra bad-prime lines X′ (§9.3) give F[Y], which is purely transcendental.
  - **Rows:** coprimality means p̄ and q̄ are not both zero, so the row fibre is an affine line, which is rational.
  - **Spheres:** Σx² = s̄ in four variables over a field of characteristic 0 is geometrically integral. This includes the cone at s̄ = 0, e.g. s = P. That is exactly the old-prime persistence argument of §9.1.
  - Each stage injects into the next. An algebraic element over K lies in some finite stage, so K is relatively algebraically closed in the union, and squareclasses inject.
- **Least QNR is exactly 2.** 2 is not a square in Frac B by parity of the 2-adic order in PA, and 1 is a square. Standard primes are independent squareclasses by PA factorization. In fact −1 and all B-primes are independent too.
- **QR and TS fail.** Since P ≡ 1 (8) but 2 is a nonsquare, the 2-supplement fails. TS (two squares) fails because P = a²+b² would make −1 a square mod P.
- **No conflict with Lag.** −1 is a sum of three squares in R/PR, which is compatible with K being relatively algebraically closed there.
- **No conflict with the §7 Smith direction.** Its hypothesis ("p is a square mod P") is false for every standard odd p.
- **No IE₁⁻ leakage.** The §9 model fails factorial induction, so it is not an IE₁⁻ model.

**Fixes**
1. **TS misattributed to z76.** "their QR and TS hypotheses cannot be pooled" reads as if the z76 model has TS. It does not claim TS: its base `BCM4_QR.md` §0 says "No claim of simultaneous universal TS". Reword to something like "its full-QR hypotheses (no TS is claimed there) cannot be pooled with §9".
   - Cite Theorem 1′ for "unique exception".
   - State the sharper contrast: in z76 every standard positive integer is a square at P; here every standard prime is a nonsquare.
2. **"Not full QR" understates the failure.**
   - The first supplement also fails: P ≡ 1 (4) but −1 is a nonsquare.
   - The main law fails for every standard odd prime q: (P/q) = +1 because P ≡ 1 (q), while (q/P) = −1.
3. **The label's source is vague.** "the §9 prime-fibre calculation" should name its parts:
   - the base K[X]/(P) = K;
   - the row-chart persistence lemma in §4;
   - floors and the §9.3 lines as free lines;
   - the §9.1 persistence of geometric integrality at target zero.
   - Listing the edge types also makes the "every subsequent edge" claim checkable.
4. **Scope sentence.** Replace "No conclusion about IE₁⁻ proving least QNR at all primes" with: the §9 model fails IE₁⁻ (§6), so nothing here bears on what IE₁⁻ proves about least QNR, QR, the supplements or TS. Also delete "not just with a nonresidue somewhere", which is unclear.
5. **Optional:** "all standard primes" can be strengthened to "−1 and all B-primes".

**Form:** the Review-line "cross-review owed" tag is right, and the commit message is fine. Leaving the Result, Scope and STATUS delta unchanged is appropriate for a scoped corollary.
</code-review>
