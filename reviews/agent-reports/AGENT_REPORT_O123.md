# AGENT REPORT O123 — "flip the average": fixed-p spectral formulation of Type I

Branch `side-agent/spectral-flip`. Main file: `POINTWISE_SPECTRAL.md`. Scripts: `scripts/spec_*.{c,py}`.
Data: `data/spec/*_stats.txt`, `data/spec/target_mean_1e6.txt` (the binary arrays are git-ignored; regenerate them
with `spec_typecount N prefix`).

## Outcome (honest)
This is a **precise negative result**. ES is not proved, and neither is Type I for large p. No conditional theorem
from a standard hypothesis is claimed. I show why none follows by this route, with exact target geometry and
numbers.

## Deliverables
1. **Numerics (EVIDENCE).** `spec_typecount.c` computes exact f_I, f_II for all n ≤ N by sieving the factorisations
   of 4a²d+1. It was validated by brute force (primes ≤ 400, 0 mismatches).
   * For p ≤ 10⁸: f_I(p) ≥ 1 and f_II(p) ≥ 1 for every prime, and the a = 1 slice never fails.
   * min_{[X,2X)} f_I grows (62 at 2²², 105 at 2²⁵) and stays at ≈ 0.16–0.2 × the mean (≈ 0.1 L³).
   * The minimisers are Mordell-hard.
   * The 10⁸ run agrees exactly with the 10⁷ run on n ≤ 10⁷.
2. **Exact fixed-p forms (PROVED, §2).**
   * Lemma 2.1: Type I ⇔ `f | p²+4c²d, f ≡ −p (mod 4cd)`.
   * Lemma 2.2: the SL₂ form with entry p, and the Hecke identity `Q' = Q₋∘[[1,2bd],[0,p]]`. Disc −4dp² solution forms are T_p-translates of level-d disc −4d forms.
   * Lemma 2.3: a = 1 slice = the brief's candidate (c); Type II = `(aq−1)(bq−1) = cqp+1`.
   * Lemma 2.4: the genus condition `χ_{−4d}(−p) = 1`. It fails for all d at odd squares, which is the required n = p² check (ET Prop 1.6).
3. **Targets (PROVED geometry, §3).**
   * Prop 3.1/3.2: point-in-wedge ⇔ Type I, with exact hyperbolic areas `log(2p)/(c√d)` (A) and `log(2p)/(a√d p)` (B).
   * The targets are tubes of width ≍ 1/p.
   * Statement (S) records the Sobolev data.
   * EVIDENCE: the per-target mean is ≈ κ_d L/(cd), with 13–89 % of single targets empty.
4. **Gap (§4, Assessment).** In the best family:
   * relative measure ≈ L²|D'|^{−1/2} and width |D'|^{−1/2}, i.e. Planck × polylog;
   * gaps of p^{5/6} (Young, unconditional, area), p^{1/2} (Lindelöf), p^{8/9} (cusp strips, width);
   * the Ramanujan-only Cauchy–Schwarz Hecke-orbit bound misses by ≈ p (R123 repair: Lindelöf does not enter it).
5. **Step (5) (§5).**
   * Thm 5.1 (PROVED rel. (D)32b): f_I(p) ≤ ψL³ except for a proportion O(1/ψ) of primes.
   * Prop 5.3 (CONDITIONAL on H): infinitely many p ≡ 5 (12) have the target (c,d) = (1,3) empty (expectation ≈ 0.17L; R123 repair: was "≈ 0.5L"). Data: 3630/3630 such p in [10⁶, 3·10⁶).
   * Prop 5.4 (PROVED): thickening the target to width K/p is exactly averaging f_I over |n−p| ≤ K. So the spectral scale V gives only interval averages of length p/V, where short-interval results already exist.
   * Verdict (Assessment): GRH, GLH/Lindelöf (any aspect), Ramanujan, Selberg and twisted Linnik do not suffice. A sufficient statement is a Planck-scale, polylog-accurate, genus-aware aggregate, which is just Type I restated.

## Points for the reviewer
* The "≈ p" Hecke-orbit gap is a Cauchy–Schwarz upper bound that is too weak. It shows the method fails; it is not a lower bound on the truth. The truth at the target scale is Poisson-like (per-target empty rates).
* "No standard hypothesis suffices" is an Assessment about routes through this formulation. It is not a theorem about all possible arguments.
* The Formulation B density factor p and the per-target κ_d are heuristic or local-density statements (EVIDENCE, `spec_target_mean.py`).
* Coordination: O128 (Type II automorphic) can reuse Lemma 2.3(b). Type II has the same structure with p ↦ cp.
