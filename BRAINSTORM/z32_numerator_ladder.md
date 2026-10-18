# z32 memo 4: a ladder of sibling lotteries that DO fail calibrates the ES model (O262; DISPROOF_AVENUES §4)

Labels as in DISCOVERIES.md. ES is not solved. All numbers EVIDENCE; extrapolations Assessment.

**Idea.** Calibrate the "how far away could a counterexample be" model on lotteries of the same shape that have
real failures: the Type II count of m/p for m = 4…24 (m·abcd = a + b + cp), all primes ≤ 10⁸
(`scripts/z32_ladder.c`, validated against bs_prob_fII and brute force).

**Findings.**
1. Failures (Type II only, p ≤ 10⁸): m = 4, 5 none; m = 6 last 2521; m = 8 last 35 569; m = 12 last 1 998 793;
   m = 16 last 12 895 921; m ≥ 20 still failing near 10⁸.
2. **Universal zero law:** P(f = 0) depends on the cell mean μ only, ≈ exp(−0.535 μ^{0.91}), across all 21 m;
   trained on p < 2²⁰ it predicts the later failures per m within ×1.5 (large counts), ×7 (counts ≤ 5).
3. **Negative-binomial tails are falsified** (predicts 50 failures for m = 6 in [2²⁴, 2²⁶); there are 0).
4. **One-constant crossover:** q_m·(log p_last)³ ∈ [7, 16] for every m = 6…23 (q_m = 10⁻³-quantile of f/L³):
   failures stop once the 0.1 %-hardest primes have ≈ 12 solutions. For m = 4 it predicts the last Type II failure
   ≈ 1.7·10³; there is none (≥ 5).
5. m = 4 floor: min f_II/L³ per dyadic bin is flat (0.012–0.021) over 2¹⁴–2²⁷ while lower quantiles rise.

**Numerator analogy (question (e)).** PW Table 1: full m/n exceptions are finite and small for m ≤ 15 at their
search limits (largest: m = 8: 241; m = 12: 12 241; m = 15: 20 521), and PW Thm 1.1/1.2 prove exceptions
> exp(m^{1/3−ε}) exist for large m (e.g. a prime in (m², 2m²) for m ≥ 6.52·10⁹). So "exceptions exist and are
small for each fixed m, and grow with m" is the proved/observed pattern; k = 4 sits at the bottom of the ladder,
where q₄ = 0.028 is the largest 10⁻³-quantile of all m (q ∝ m^{−1.9}). ES would have to behave like m ≈ 60 to fail
beyond 10¹⁸.

**Barrier screen.** B6: these are averages over p and say nothing at a single p; the claim is only a calibrated
*model*. B3: the main term is (log p)³ — the lottery itself.

**Viability (Assessment).** As a disproof avenue: COLLAPSES (the model gives ≤ 10⁻²⁰ expected failures in
[10⁸, 10¹⁸) and < 10⁻⁸⁸ beyond). As a calibration tool: strong (promise 3/5): it replaces untested NB heuristics
by a law validated out of sample on 21 sibling lotteries.
