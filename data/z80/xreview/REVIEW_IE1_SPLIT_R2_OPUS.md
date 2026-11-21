<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="529922cd6">
A separate reviewer subagent was asked to review the changes in `git log 529922cd6..`. Its request and review follow.

Request: review changes since 529922cd6 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab second Claude Opus review on notes/z80/IE1_SPLIT.md §§9–10 and revised §0. Verify the new rel. §§1–8 claim independently: nonstandard-valuation Hensel and old PA-representability; uniform coefficient loss under rotations, matrix rank, scalar profiles, sphere order/normality/factor and pole contraction; Dirichlet, coinitial new bad-prime tasks with a moving coefficient and norm-one chart, U1 least-failure control. Are Lag, internal Dirichlet, global Sep/Bézout, cofinal windows, no ES(P), no BCM and no L(Div) really simultaneous? Audit original dependencies if needed and consistency of prospective STATUS scope/falsifiers. Give commit hash, decisive verdict, required fixes. Do not change files. If running any Python respect uv run --offline --no-project python, ulimit -v 6000000, timeout <=1800. No need for numerical calculations.

Commit log:
commit 61871c123d40508c4822e6a6920eb35e1b76f1f6
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:50:29 2026 +0100

    Add Lagrange via thick quaternion rotations, internal Dirichlet and coinitial bad primes

 notes/z80/IE1_SPLIT.md | 75 +++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 71 insertions(+), 4 deletions(-)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I reviewed commit `61871c123d40508c4822e6a6920eb35e1b76f1f6`, which only touches `notes/z80/IE1_SPLIT.md` (§0, new §§9–10). I found no substantive gap in the new claims relative to §§1–8 and their imports, and I checked each step independently rather than for plausibility. This counts as the owed cross-lab hostile review of §§9–10. The fixes below are about labels, scope and wording. I changed no files and ran no code.

## What I re-derived

**§9.1 (sphere edge)**
* **Square-free reduction.** Writing the content as `c=b₀²d₀` gives `w_ℓ(s)∈{0,1}` at every B-prime. This is exactly what the Hensel start and the `e·w(s)≤e` bound need.
* **Targets already in B.** If `s` is C-bounded, invariant 3 forces `s∈Frac C∩R_A⊆B`, so PA's four-square theorem applies.
* **Off `J`.** All such `ℓ` are nonstandard, so the residue characteristic is 0. The rank-4 special fibre is geometrically integral even when `s̄=0`. So Gauss on the monic normal form is multiplicative, and contents are PA gcds of coefficient contents.
* **Factoriality and units.** Over `E(i)` write `UV=s−z²−w²`; the right side is prime when `s≠0`. Then Nagata, Hilbert 90 descent, old primes kept by freeness plus a geometrically integral fibre, and `A'∩E=A` give units `K*`. This matches z75 `BCM4_QR.md` §3.
* **Order.** The scaled angular order of `LOGIC_LAGRANGE_END_TEST.md` §2 transfers to the relative setting. The two facts it needs are that `S` has no relative infinitesimals and that `√s>C`.

**§9.2 (valuations at `ℓ|J` via rotations)**
* **Hensel.** The Newton condition `v(f)>2v(f')` holds in a henselization of any rank. Here `4v_ℓJ>2v_ℓ(2)` holds, including at `ℓ=2`.
* **Newton steps.** For a quadratic, exactly `f(X−f/f')=(f/f')²`. So the error goes `r↦2r−2v(2)`, and a standard number of steps reaches `J^N` uniformly in `ℓ`.
* **Approximability.** It survives the partition by unit-coordinate index, via the §3 trick of multiplying by the denominator part outside the subset.
* **Uniform bound (3).**
  * The rotations `UQ(J^k t)` have unit denominator and move coordinates by at least `k·v_ℓJ`.
  * The inverse substitution `G=Ū x/s` gives a coefficient of value `≤e·w(s)`.
  * The stereographic matrix is a fixed integer matrix, injective because the map is birational.
  * The adjugate bound through a nonzero minor `D_e`, the cost `2ek·v_ℓJ` of scaling, and the tensor-Vandermonde bound on `{0,…,2e}³` all check out.
  * Every loss is a standard constant ≤ `const·v_ℓJ`, so `M=M(e,k)` is uniform over centres and places.
  * The PA "first grid point" selection plus CRT patching keeps the strict inequality, since `t≡g` modulo `ℓ^{M v_ℓ J}`.
* **Freezing.** Choosing `k_{i+1}>M_i` freezes each value. The limit evaluations define a valuation (it is multiplicative because every centre lies exactly on the quadric). The extension is immediate at `ℓ|J`, which is what invariant 2 needs.
* **Contents and the sandwich.** The content is `γ·gcd(b,J^{M})`. Invariant 2 at `C'` holds with precision `J^{1+M}`, since every `d∈C'` divides `J`. The sandwich (2) holds with an `M` that depends on the element; this is harmless because `1/J` is inverted.

**§9.3 (Dirichlet and new bad primes)**
* **Dirichlet line.** The forced first digit is compatible with the §3 dilution. `a+mY` is content-1 at all places, prime by Gauss's lemma over the UFD `A`, and above the bound.
* **Every non-old `y` exceeds some reserve.** Every positive `y∈R∖B` lies above the old reserve of the step that produced it, by the "Changing reserve" paragraph of §4. So each `y>D` and the task is well posed. Also `D<p'<1+2JH∈C_{n−1}<y`.
* **Replay over `K(X')`.** Base change along the pure transcendental extension preserves lines, row charts, gcd-coprimality, the graded domain and contraction. The intersection `A_old[X']∩K(X')=K[X']` holds via a K-basis containing 1. Positivity is checked in the original order, and the clopen positive-ray argument works.
* **Units for `d=p'²−1`.** `d` stays a nonsquare because each edge is geometrically integral. Every generic algebra over `F(√d)`, spheres included, has only scalar units. The descent ends in `K[z,z⁻¹]`, where the norm-one units are `±z^j` with `j` standard.
* **Conditional no-least-failure.** With `B≡ℕ` and ES true in ℕ, every failure is non-old and has a smaller failing `p'`. If ES were false in ℕ, the least failure would be standard, so the condition is necessary.
* **U₁ control.** The complement is E₁ via root/remainder decoding. Members are never old. `t=h^h∈C_{n−1}` with `h>2p'` works.

**Simultaneity: yes.** One dovetailed tower uses only free lines, rows and spheres.
* **Positive properties:**
  * Bézout, (Sep), isolation, floors, Lag and Dirichlet are each delivered by tasks.
  * The windows are E₁ facts that later edges cannot destroy.
  * Cofinality comes from invariant 3.
* **Failures:** each comes from an argument that covers every edge type:
  * ¬ES(P) comes from line, row and graded-sphere descent.
  * ¬PW comes from the scalar units of the sphere.
  * ¬BCM holds because the `X+j` stay independent primes.
  * ¬L(Div) holds because `A*=K*` keeps divisors of B-scalars old.
  * ¬IE₁⁻ follows from the §1 factorial test.

## Required fixes
1. **§10 "Assessment (next fork)" contains a proved lemma.** The statement is: if every element has a content in `K` (invariant 1) and `R` is the pullback of integral-valued elements, then `A*=K*`, so `IE₁⁻` fails by the §1 Corollary. It should get its own **PROVED** label with these exact hypotheses, and an entry in Triage as BARRIER-SCOPED, merged by root cause with the §1 corollary. Keep the repair speculation as Assessment.
2. **§0 Label.** Add `LOGIC_LAGRANGE_END_TEST.md` §2 (the scaled angular order). Name the Hensel form used: Newton/Hensel–Rychlik in a henselian field of arbitrary rank.
3. **STATUS delta.** "Separately from the normal + Lag model" is now ambiguous, because §9 is itself normal + Lag.
   * Phrase it as a row next to the z79 `IE1_BASE` row, which keeps the z78 height windows and §11 data but lacks global (Sep). Better, merge the two rows.
   * Note that Lag + Dirichlet + Bézout + (Sep) + ¬ES already coexist in the z76 PID. The novelty is the combination with cofinal-PA windows and a nonstandard cut.
   * Mark it "cross-lab reviewed (one)" and keep it within the 6-line cap.
4. **§0 Scope/Result.** Mention the unconditional coinitial ES-failing primes outside `B`. Scope the unconditional U₁ control honestly: it is ¬PW repackaged, since the set is empty in `IE₁⁻`, and it carries no independent content.
5. **§9.2 "multiplying … by `J^M`".** Write `J^{M_f}` with the dependence on the element stated, and say it is harmless because `1/J` is inverted.
6. **§9.3.** Cite §4 "Changing reserve" for the parenthetical about "that step's old reserve", and add that every positive non-old `y` lies above some `C_m`, hence above `D`.
7. **§10 table, z79 §4 row.** Carry over the §8 remark with the new reason. `−1` is still not a square mod `P`: `K[X]/(P)≅K`, and each special fibre is geometrically integral, so `K` stays algebraically closed in the residue field. So there is still no clash with conditional two squares. Also say that conditional two squares at other primes is not asserted.
8. **Wording:**
   * "another ES-failing prime" should be "an ES-failing prime".
   * Fix the grammar of the "approximable" definition.
   * In 9.1, say "if `s∈B` use PA" as well as the C-bounded case.
   * Update the Review line to cite this review.

## Points for debate
* **Novelty is incremental.** §9 mainly merges z76 (Lag + Dirichlet + Bézout + Sep), z79 (Lag + windows) and §§2–6 (Bézout + Sep + IW₂). The genuinely new ingredient is the quaternion-rotation construction that keeps the residues at `ℓ|J` immediate on spheres. In STATUS, compress the rows rather than add one.
* **The conditional no-least-failure result is well scoped and worth one line.** It is a statement about the intermediate theory, not about parameter-free induction, as the note says.
* **The new §10 lemma is the most useful structural output.** Any architecture with PA scalar contents is automatically not an `IE₁⁻` model, so it should feed the FRONTIER §4 screen.
</code-review>
