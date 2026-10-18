# AGENT REPORT O262 — disproof avenues and adversarial search (checkpoint 1)

Main file `DISPROOF_AVENUES.md`; memos `BRAINSTORM/z32_*.md` (6); scripts `scripts/z32_*`; logs `logs/z32_*`.
**ES is not solved; no counterexample is known or claimed.** Compute used ≈ 40 CPU-minutes (≤ 2 cores).

## SHARP
1. **Universal zero law on a ladder of sibling lotteries that really fail (EVIDENCE).** For the Type II count of m/p,
   m = 4…24, all primes ≤ 10⁸ (1.2·10⁸ counts), the failure rate depends only on the cell mean μ:
   P(f = 0) ≈ exp(−0.535 μ^{0.91}), validated out of sample (train p < 2²⁰ → predicts later failures per m within
   ×1.5 for large counts; R274 repair: but up to ×16–20 for small counts, and systematically ×3–5 too few zeros on
   test units with μ ≥ 35 — the extrapolation direction). Negative-binomial tails (B1_LINE §3 style) are falsified (50 predicted, 0 observed).
   And a **one-constant crossover law**: q_m·(log p_last)³ ∈ [7, 16] for all m = 6…23 (q_m = 10⁻³-quantile of f/L³),
   predicting each m's last failure within ×2–4 over 2.5·10³…10⁸. For ES (m = 4) the predicted last Type II failure
   is ≈ 1.7·10³; there is none. (§4.2–4.3, memo z32_numerator_ladder.)
2. **Heavy tails are self-refuting (Assessment).** In the family exp(−a μ^β), μ ∝ L³, every β that puts ≳ 0.1
   expected failures beyond 10¹⁸ puts ≥ 494 below 10¹⁸, where ES is verified. (R274 repair:) A counterexample needs a
   zero law outside this family — non-monotone in p, a floor/mixture (conspiracy class), or polynomial decay in p —
   i.e. a new global mechanism, not a fatter tail of the measured kind. (§4.5)
3. **n = 1 shadow principle (PROVED; existence CONDITIONAL on Dickson/H).** p ≡ 1 (mod Q) with prime slice
   cofactors empties ANY finite set of ET slices (all six pair rows of both types + e-slices): every divisor is ≡ a
   divisor of N_θ(1), and n = 1 has no solution (4 > 3). Archimedean twin of T1 / Thm C; unifies (J)83 Thm 1.3,
   (J)90 Thm 4.2, redteam L1.2.1. Novelty only in uniformity (mechanism = B1_LINE §4). (§3 Prop 3.1)

## Results by goal
* (1a) BL Thm 1.8 (1.4): no BM obstruction to ES at any n ≥ 2 (R274 repair: n = 1 is BM-obstructed); Thm 1.6: Br/Br₀ = ℤ/2 (transcendental); Thm 1.9: strong
  approximation fails beyond BM; Rem 1.10 for m/n. So every counterexample is a non-BM integral failure; such
  failures exist for 8/n, 15/n (PW Table 1) and are small-count accidents. (§1)
* (1b) Markoff (CT–Wei–Xu, Loughran–Mitankin, Dao), Lyczak order 5: known non-BM integral failures are all
  "few orbits/points" phenomena. Verification record 10¹⁸ (Mihnea–Dumitru 2025); nothing newer found. (§2)
* (1c) Prop 3.1 + budget: k ≲ log p/log log p forced slices, killed share O(log L/L), congruence part saturates
  (≈ 0.73); ≍ (log p)³ untouchable, not √p. (§3)
* (1d) Expected f_II-failures (⇒ conservative for ES) in [10⁸, 10¹⁸): ≈ 10⁻³¹ (R274 repair: up to 10⁻⁹ in the
  author's own β = 0.8 variant); beyond 10¹⁸: 10⁻²⁹⁶ … 5·10⁻³⁷, before a model-error factor. Worst case (every prime at the smallest f_II/L³ ever seen ≤ 10⁸): P ≈ e^{−240} at 10¹⁸. (§4.4)
* (1e) PW: full m/n exceptions small for m ≤ 15; PW Thm 1.1 proves large exceptions for large m. On our ladder
  m = 4 has the largest lower quantile (q ∝ m^{−1.9}); ES would have to behave like m ≈ 60. (memo 4)
* (2) Adversarial search 10¹⁸–10²⁵ (86 primes, engine exact on the 1024 cheapest e-slices, validated): hardest
  prime p = 2054098191162848070241, 870 solutions in e ≤ 2047 (0.26 × controls), W = 11; min absolute 612. The
  depression saturates (0.32–0.36) and overstates the true f_II depression (10¹²: S 0.49–0.63 vs exact f_II
  0.80–0.82). (§5)
* (3) Bottom line (Assessment): P(ES false) well under 10⁻³ (R274 repair: a subjective credence; floor/mixture
  laws are not priced), all of it model risk; the only conceivable disproof
  route is a "prime T1" (a global invariant correlating ≍ log³p divisor events); none found. (§6, memo z32_prime_T1)

## Caveats for the reviewer
* The zero law is fitted on μ ≤ 50 and extrapolated to μ ≥ 229 (m = 4 at 10⁸); §4.3's quantile law is the
  cross-check. Pooling by cell mean hides within-cell heterogeneity (`logs/z32_lowdev.txt`, confounded).
* Ladder = Type II only; ES failure needs f_I = f_II = 0, so predictions are conservative for ES but the ladder's
  failures are not PW's (full m/n) failures.
* 10²⁵ primes are BPSW-probable (EVIDENCE-grade); X in the log shows 10000000000000000905969664 for the
  first 1e25 run (float parse; fixed afterwards; cosmetic).
* Prop 3.1's row table was derived here; please re-derive II{a,d}, I{c,d}, I{a,b}.

## Sparks (not pursued)
* Run the ladder with Type I included (full m/p) and test the crossover law against PW Table 1's full exceptions.
* Fit the zero law with a second covariate (truncated L(1, χ_p) or the class-of-one depth) to remove within-cell
  heterogeneity; test whether β stays ≈ 0.9 at fixed local profile.
* Function-field analogue of the ladder (q fixed, numerator m): is the crossover constant the same?
* Search for a non-monotone zero law on some sibling lottery (failures switching on at large p) — the only
  shape that would make a disproof plausible.
