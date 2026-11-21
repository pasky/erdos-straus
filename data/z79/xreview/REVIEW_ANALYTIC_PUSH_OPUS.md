<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab review of notes/z79/ANALYTIC_PUSH.md and scripts/z79_analytic_push.py. Check carefully signed order of the two Cauchy/shift inequalities, stationarity, uniformity incl M, LP and boundaries, arithmetic falsifiers and scopes of §§1,3. State model if available. Return full verdict; do not edit files. Python only via ulimit -v 6000000; timeout 180 uv run --offline --no-project python. Do not write to repository.

Commit log:
commit cbc38e871f31ac16b18dddde19f09c6c7bfa9aaf
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:08:57 2026 +0100

    Bound pointwise word counts by 13/41 using a second conductor difference

 data/z79/analytic_push.txt   |  9 +++++
 notes/z79/ANALYTIC_PUSH.md   | 90 ++++++++++++++++++++++++++++++++++++++++++++
 scripts/z79_analytic_push.py | 63 +++++++++++++++++++++++++++++++
 3 files changed, 162 insertions(+)

Review:
**Verdict: ACCEPT the 13/41 theorem in §2, with minor fixes (form only). Accept §1 and §3 as scoped results, but they need triage labels. I found no mathematical gap.**

I am a Claude model (Anthropic); I can't see the exact model version. The note doesn't say which model wrote it. If Claude wrote it, this review doesn't count as the other-lab review the STATUS gate requires.

### Substance of §2, checked step by step

**Order of the two Cauchy/shift steps (signed).**
- **First step (inherited from z78 §7).** The periodic shift plus Cauchy gives a nonnegative right-hand side. Only then is the conductor range enlarged to all Q in [N,4N]. E_h is the absolute value of the *signed* average over Q and x. This order is correct.
- **Second step (new).** The steps go: Poisson in x, triangle in m, Cauchy in m (O(Y) terms), then van der Corput in Q within one parity class (shift 2k, K ≤ N, weights 1−k/K). For each m the right-hand side is real and nonnegative. Summing these real correlations over m and only then putting absolute values on the (Q,k) sums is legitimate.
- **Normalisation.** (W/(N√T))·√Y·(N²YD)^{1/2} = √(WY)·D^{1/2}. This matches the note.
- **Why it works.** The parity sign e(mhQ/2) depends only on m within a parity class. No smoothness in Q is needed. The shift only makes sense because the conductor range was enlarged; I agree with the note on this point.

**Stationarity.**
- By the envelope theorem G_u = y* and G_s = (y²−s)^{-2}.
- At s=0, G_uus = 2^{2/3}u^{-2/3}/9 > 0. This equals the note's (4/9)·2^{-4/3}u^{-2/3}.
- I confirmed this with mpmath at 40 digits. At s = 0.01 and 0.05 it stays positive and moves smoothly.
- The exact phase difference gives F″ ≍ ZNk/Y² > 0. A 60-digit finite-difference check of the exact F″ agreed with the formula to a ratio of 0.99991–0.99999.
- No quartic expansion is used, so the bounded-residual condition really is dropped.

**Derivative test and the bound (4).**
- The second-derivative test (Titchmarsh Thm 5.9) is applied correctly. The u-range is compact, so the comparability constant is fixed. Short subintervals are handled by AM–GM, and the weights by partial summation (variation O(1) in m).
- The resulting bound on D is correct.
- I recomputed K₀ = (Y²/(ZN))^{1/3} and all five terms of (4), including both clipping cases:
  - K₀ < 1: √(WY) is at most the first term, since (ZN/Y²)^{1/6} > 1.
  - K₀ > N: the middle term is absorbed.
- At the binding vertex K₀ ≍ N^{3/4} (exponents 3/41 against 4/41). So λ ≤ 1 throughout, and the "Round 2" remark is consistent.

**LP, uniformity in M, and boundaries.**
- The exponents of all four terms are correct. Bounding Y by its maximum is a valid upper bound even though Y grows with h.
- Vertex 1 gives exactly t/r ≥ 13/2, i.e. t ≥ 13/41. Just below 13/41 the vertex fails, so the threshold is sharp for this estimate.
- The side conditions are right:
  - γ > j+2r reduces to 6t > 4β+γ; the tightest case needs t > 4/13.
  - 1 > 2γ holds.
  - L ≫ 1 is weak only at vertex 3 (r = 0), where the log³ in P rescues it, as in z78.
- The region is convex: each slice in μ is a triangle whose vertices move affinely. So checking the vertices at μ = 0 and μ = 1/3 is enough.
- I added an independent check of 20,000 random exact-rational points with random μ: no failures.
- The zero slacks at μ = 1/3 and at vertex 1 are weak inequalities. They only cost X^{O(δ)}, which is acceptable.
- 46/145 − 13/41 = 1/5945 ✓. The M-exponent −11/41 ✓. The handover to the fibre bound at M > X^{1/3} ✓.

**Positive point.** 13/41 depends only on z78 §§7 and 13, both of which have two reviews. It does not use §§11–14. That makes its base sturdier than 46/145's, and the STATUS delta should say so.

### §1, §3 and the falsifiers

- **§1** is correct. It is the classical Selberg-denominator calculation:
  - orthonormal centred products, with ∑∏ p/(1−p) equal to ∏(1−p)^{-1} when every subset is allowed;
  - the bound e_j ≤ a^j/j!;
  - the s-trick giving λ^{d/(d+1)}(1+log z)/z.

  It should be triaged BARRIER-SCOPED, not STATUS material. "Sums of squares with total evaluation one" should say ∑|P_j(0)|² = 1; with ∑P_j(0) = 1 the claim is false.
- **§3** is correct as a port of z78 §4 to the z75 Gallagher argument:
  - The character-coefficient signs check out: χ₋₄ and χ_R are harmless, and only χ₋₄χ_R is harmful.
  - The Gallagher error is weighted by coefficients of size μ_i, so a fixed A suffices.
  - The constants 2 and 2√3 are right (minimise 2/b + b/2 and 2/b + 3b/2).
  - It doesn't change the cap scale, which the note says. The constant 2 is in units of u = A·log R with A unspecified, so it says nothing in R-units. Triage: NULL.
- **Falsifiers.** The replay reproduces `data/z79/analytic_push.txt` exactly, within the memory and time limits.
  - I checked `has_word` by hand: the a ≤ b bound, the necessity of both loop conditions, and that b ≥ a holds automatically. The `has_u7` cutoff 2n+1 is correct.
  - The trillion-scale control in `pycheck.txt` does show R₈ = 0 and R₄ > 0.
  - All these checks are one-sided and compatible with an upper bound.

### Form issues (required before export)

1. **§0 covers only §2.** §§1 and 3 have their own labels but no triage class, and the commit message doesn't mention them. Add per-section triage (§1 BARRIER-SCOPED, §3 NULL) or split them into separate notes.
2. **The STATUS delta is incomplete.** It should also:
   - supersede θ in z78 (12)/§14 (the R_M bound becomes 13/41 and M^{-11/41});
   - update the ES₅ and N₂ transfer bullets in z78 §13 and FRONTIER lines 497 and 1741;
   - record that the result no longer depends on the once-reviewed §14;
   - keep "cross-review owed" until a review from the other lab exists.
3. **Undefined term.** U₇ is not defined in the note; point to FRONTIER §365 / `Z60_LOPEZ.md`.

**Minor:**
- Symbols are reused: s (z78 uses b(y,s) with s = Q/N), D (correlation quantity, interval length D₀, and §3's D_i), and N.
- `has_word` has leftover contradictory comments.
- The data file has no header giving the command that produced it.
- The Round-2 paragraph should be labelled clearly as "not an estimate". It nearly is already.

**Debate point.** The improvement is tiny (1/5945), but it's real, and the method is simpler than §§11–14. The only binding constraint is the first term of (4) at vertex 1, and every other constraint has slack. A B-process in m that keeps the signs, as the note suggests, is the natural next lever. Nothing here moves the exponent toward 3/10 beyond this.
</code-review>
