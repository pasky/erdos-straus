<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="2d42c3e6e">
A separate reviewer subagent was asked to review the changes in `git log 2d42c3e6e..`. Its request and review follow.

Request: review changes since 2d42c3e6e carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Independent Claude Opus hostile review, round 4. Attack §§14–15 of notes/z78/ANALYTIC_WILD.md and exact 46/145 LP in scripts/z78_analytic_r4.py. Re-derive common quartic coefficient relation, freezing across h with weights and absolute values, arc occupancy on fixed v/bin by third derivative including all small/boundary cases, all five terms and binding equations, sextic slack, numerator generalization. Audit the multiple-alphabet and small-nonresidue fallback at q|R and the exact CRT/GRH compatibility obstruction, quantify what is not shown. Check cited theorems' hypotheses; report any defects including numerical typos and any provider/auth/quota errors. Only read relevant sections and dependencies. No edits, scratch files or commits; all python checks in memory with ulimit -v 6000000; timeout 180 uv run --offline --no-project python ... . Return full review.

Commit log:
commit 31ba3ad61593ec661cd2b90eca6d8881f4b0efcb
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 22:04:48 2026 +0100

    z78 R4: characterize obstructions to the disjoint cap menus and planted-carrier fallback

 notes/z78/ANALYTIC_WILD.md | 24 +++++++++++++++++++++---
 1 file changed, 21 insertions(+), 3 deletions(-)

commit 50dcf54cd245edd22ccdd43892c60b9506a1121b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:58:35 2026 +0100

    z78 R4: pool shifts in common quartic bands to reach 46/145

 data/z78/analytic_r4_lp.txt |  7 +++++++
 notes/z78/ANALYTIC_WILD.md  | 32 ++++++++++++++++++++++++++++++++
 scripts/z78_analytic_r4.py  | 13 +++++++++++++
 3 files changed, 52 insertions(+)

Review:
# Hostile review, round 4 (Claude Opus): `ANALYTIC_WILD.md` §§14–15 and `z78_analytic_r4.py` (commits 50dcf54, 31ba3ad)

## Verdict

- **§14 holds.** The bound R(n) ≪ n^{46/145+ε}, and θ = 46/145 in (12), survived every attack I made. I found no gap in the substance. There are a few form and consistency defects (§E).
- **§15 is correct as scoped.** Its obstruction is genuine and the note states its limits honestly. One paragraph treats a case that cannot occur, a parity fact is cited rather than stated, and one label is imprecise.
- **This is one review.** RECORD promotion still needs the other-lab gate and a priority check. Who wrote the note is not stated, so whether this Opus review counts as cross-lab depends on the author.

## A. Shared quartic coefficient relation (re-derived, then checked numerically)

- **Phase.** In the midpoint coordinate the phase is A/(t²−(hQ/2)²), with A = nℓh/4, Y = A/W³ ∝ h and T = A/W² ∝ h.
- **Second-order term.** The σ² term is T·y0⁻⁴σ², which gives ξ = c·h^{5/3}m^{4/3}. The σ⁴ coefficient is (1 − 8/3 + 4/3)·y0⁻⁶ = −y0⁻⁶/3. Numerically, Newton on the critical point plus a finite-difference fit matched −y0⁻⁶/3 to 8 digits.
- **Quartic coefficient.** |ζ| = m²h³/(48nℓ) exactly. The constant does not depend on h, m or even W.
- **Relation.** |ζ| = c′c^{−3/2}·h^{1/2}·ξ^{3/2}. I checked this numerically at two values of h.
- **Sign and parity.** The sign of ζ is fixed once ℓ > 0. Splitting Q by parity for every h is harmless, including even h.

## B. Freezing across h, weights and absolute values (13)

- **Order of operations.** The order Σ_h E_h ≤ Σ_h Σ_m |Σ_Q …| is legitimate.
- **Bins.** Width-one bins in |ζ|N⁴ give a residual |Δζ|Q⁴ ≤ 128 with Q-derivative O(1/N). The sextic term T(SN/W)⁶ ≪ 1 is checked.
- **Bin count.** The number of bins is J = 1 + YS⁴N⁴/W³ = 1 + Z(SN²/W)², as stated.
- **Varying weights.** Abel summation per pair, with a common endpoint u, followed by Hölder on all O(SY) pairs, is valid. The weights w_{h,m} and W/√T_h are bounded on the dyadic block.
- **Fourth moment.** It has coefficients c_s with |c_s| ≤ r₂(s), so the bin bound N^{4+ε}D_i holds. D_i ≥ 1 for nonempty bins, and the coloring argument needs exactly D_i.
- **Prefactor.** W/(N√T) · (SY)^{3/4} · N · (ΣD_i)^{1/4} = W^{1/2}Y^{1/4}(S⁻¹ΣD_i)^{1/4}, as claimed.

## C. Arc occupancy (14), including small and boundary cases

**h-interval at fixed v.** The value N⁴c″h^{1/2}(v+η)^{3/2} has h-derivative ≍ (J−1)/S and ξ-derivative ≍ J/Z.
- The error from replacing ξ by v+η is O(J/(ZN²)) = O(1/N²), because J ≪ 1+Z. This gives |I| = O(S/J).
- When J−1 ≍ 1 or J−1 ≪ 1, the whole block works.
- Integer rounding is what produces the JZ/S term. That is why J ≪ S is needed in the trivial Δ ≫ 1 branch, and it holds.

**m-tolerance.** m lies within Δ = Y/(ZN²) of f(h) = c^{−3/4}(v+η)^{3/4}h^{−5/4}.

**Case checks.**
- **Z ≪ 1:** J ≤ 1+Z gives O(1) bins, and the §7 count gives 1+Δ.
- **Δ ≫ 1:** the bound is Z(1+Δ)(1+J/S) ≍ Y/N².
- **Y ≥ S³:** Z ≤ Z(Y/S³)^{1/7}.

**Erdős–Turán plus third-derivative test.**
- f‴ has constant sign and |f‴| ≍ Y/S³ with ratio 2^{17/4} on [S/2, S].
- λ = lY/S³ ≤ (Y/S³)^{6/7} ≤ 1 for l ≤ B.
- Summing with weights 1/l gives D·B^{1/6}(Y/S³)^{1/6} plus D^{1/2}(Y/S³)^{−1/6}·log B.
- Over O(JZ) intervals with D ≤ S/J, this reproduces exactly JZ/S + ZΔ + Z/B + Z(BY/S³)^{1/6} + J^{1/2}ZY^{−1/6}.
- B = (S³/Y)^{1/7} balances the third and fourth terms. JZ/S ≤ Z/B follows from (J−1)B ≪ S together with B ≤ S^{3/7}.

**Cited theorem.** I checked Titchmarsh Thm 5.11 verbatim against the repo's `data/z53/sqsieve/LIT_CHECK.md` §4. Its hypotheses are λ₃ ≤ ±f‴ ≤ hλ₃ and b−a ≥ 1, with bound O(h^{1/2}(b−a)λ^{1/6}) + O((b−a)^{1/2}λ^{−1/6}). They are met. The "+1" the note adds is harmless.

## D. The five terms, the binding equation, sextic slack and the LP

**Term exponents.** I re-derived all five exponents:
- γ/2 + d/4
- 3γ/4 + d/4 − j/2 − r. After substituting Y_S = Y_max·S/H, the S-power is S^{3/4}H^{−5/4}, so the maximum is at S = H.
- (γ+d)/2 − r
- γ/4 + 15d/28 + 11j/28
- γ/4 + 11d/24 + j/2 + K/8, with K the exponent of J−1.

**Side conditions.**
- SN²/W ≪ 1 is j + 4r < γ.
- In the B > 1 branch, (J−1)B/S ≪ 1 is 6d/7 + 24j/7 + 8r − 3γ < 0.
- In the B = 1 branch it is d + 3j + 8r − 3γ < 0.
- The sextic condition is d + 6j + 12r − 5γ < 0.
- Each side quantity is increasing in S, so testing at S = H suffices.

**Binding equation.** t/4 + (41/14)r = t − 2r gives t/r = 46/7. With r = 1 − 3t this gives t = 46/145.

**Arithmetic.** These all check:
- fifth-term slack 1/348;
- sextic exponent −34/145;
- 272/857 − 46/145 = 18/124265;
- 1 − 4θ = −39/145.

**Replay.** The script output matches `data/z78/analytic_r4_lp.txt` byte for byte.

**Independent in-memory check.** I recomputed the bound block by block in rational arithmetic, maximizing over log S ∈ [0, j] with every regime branch of (14):
- Vertex 1 has slack exactly 0, binding at S = H in the Erdős–Turán regime.
- Vertex 2 has min slack 9/290 and vertex 3 has 39/580; both match the script.
- 300 random interior points have min slack about 0.0093.
- μ ∈ {1/12, 1/6, 1/4} at all vertices have nonnegative slack, and every side condition is negative.
- At t = 46/145 − 10⁻⁴, vertex 1 fails. So 46/145 is the exact optimum of this estimate.

**Convexity.** The vertex reduction is valid. The region is the convex hull of the three μ=0 vertices and the μ=1/3 apex, and the constraints are max-affine.

**μ = 1/3.** Two terms have zero slack there. This is harmless, since only n^{O(δ)} is lost and the "≪ 1" side conditions are strict.

**Numerator generalization.** It holds. A = X|ℓ|h only changes c and c′.

## E. Defects in §14 and §0 (form level; none changes the theorem)

1. **§0 Label** drops "fourth derivative test", but the Scope still cites §§11–12 (1472/4637 and 272/857), which use Titchmarsh Thm 5.13. It should list both tests.
2. **Misattributed condition.** The sentence "j+4r<γ and 6d/7+… sufficient for (J−1)B/S≪1" pairs them wrongly. j + 4r < γ is the SN²/W ≪ 1 condition; only the 6d/7 inequality is the (J−1)B/S condition.
3. **Stale exponents in §13.** The ES₅ and N₂ bullets still say 272/857, while §0 now claims 46/145 for ES₅ word multiplicity. This is correct but weaker, and inconsistent.
4. **Citation.** §14 cites "Thm 5.11" without the edition or page (2nd ed., p. 106), unlike §12.
5. **Script.** It asserts `g+2*r<=2*t` without explanation, a constraint inherited from r3 and documented in neither note nor script. The data file prints the coalesced μ = 1/3 vertex three times (cosmetic).
6. **"A longer shift is not free"** is an Assessment. It is consistent with the exponents, since the fourth term's j-coefficient is 26/28 > 0 at a fixed target.

## F. §15 audit

**Correct:**
- log D_i ≤ (c+o(1))u, s ≍ y/(k log y), and D_i·√X·log(RD_i)/X ≍ e^{(c−1/6)u}, because log T = e^{u/3}.
- B_i and the cap log, 2u/(k+1) + O(k + log u), carry no log D_i.
- |E_i| ≤ Ce^{−k}φ(D_i).
- The small-nonresidue test works: K ≡ v (mod v²) and (v/q) = −(−1/v)² = −1. The class is reduced because v ∤ R, and q ≠ v. A = K(1+v^e)/q has v_v(A) = 1, so z = RA/v^e.
- (a/v) = −1 on S_i.
- The CRT proportion ∏ 2|F_i|/φ(D_i) is exact: φ(D_i/4) = φ(D_i)/2 and F_i injects mod D_i/4.
- Realization: R ≡ 1 mod 8 and mod unused v makes every (v/R) = 1. log P_* ≍ y = (log T)^{o(1)}, so the GRH count in (T, 2T] is positive.

**Defects:**
1. **The q | R qualification is vacuous.** For hard radicals every prime of R is 1 mod 8, while q ≡ 3 mod 4, so q ∤ R. The paragraph is algebraically correct, but the forward pointer "see qualification below for q|R" suggests a live case.
2. **A needed parity fact is only cited.** Since q ≡ 3 mod 4, e = ord_q(v)/2 is odd. Hence the overflow exponent e−1 is even and the cap is (e−1)/2 ≤ (q−3)/4. The note relies on "as in z75 §1" for this; it should be stated.
3. **Label imprecision.** The header says only prime realization is GRH-conditional. But the forward direction, "some F_i empty ⇒ O(√u) guarantee", also needs GRH supply (§9).
4. **Possibly unconditional (low confidence, not checked).** The realization step might be made unconditional via a strong Linnik/Gallagher lower bound for moduli T^{o(1)}. Keeping GRH is the conservative choice.

**Quantified gaps:**
- Nothing shows any F_i empty, or nonempty, at any T.
- Counting cannot decide this: |E_i| ≲ e^{−k}φ(D_i), which is ≫ 1 in absolute size and below the 2^{−k} share of candidate classes.
- There is no bound on max b_i over the restricted classes.
- The survivor proportion exp(−c₀ y/log y) is only a fraction of residue classes, not a count of radicals R (composites are not equidistributed mod exp(O(y))).
- The obstruction covers only this fixed menu: disjoint alphabets in (y/2, y] plus nonresidues ≤ y. It says nothing about adaptive alphabets, overlapping alphabets or alphabets built from K's factors.
- There is no lower bound on the true cap.
- Scope omits §15, though the Label includes it.

## G. Errors

I hit no provider, auth or quota errors. One Jina web search returned HTTP 422 on a quoted query; the retry without quotes worked.
</code-review>
