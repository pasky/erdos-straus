# BRAINSTORM O153 / W2 — a hardness law: f_II(p) versus χ_p and congruence data; the Siegel-zero dichotomy

**Verdict: PARTIAL (as a law: new EVIDENCE) / COLLAPSES to B2 (as a route; the dichotomy has no fixed-p
mechanism in either world).** No case of ES is claimed.

## 1. Idea

(a) *Law.* The campaign records that the hardest primes lie in the square classes mod 840 ((I)4 EVIDENCE). The aim
here is to quantify that: how much of the size of `r(p) := f_II(p)/log³p` is predicted by the small-prime profile
of `χ_p` (equivalently, by a truncated Euler product for L(1, χ_p)) and by p modulo small moduli, and how much is
a per-p "lottery"? A sharp law predicts how close to sterile a prime can get through structure alone.
(b) *Route.* The classical illusory-world dichotomy runs: either no exceptional zeros (GRH-like world), or an
exceptional character χ_D, whose Deuring–Heilbronn repulsion gives strong sieve/equidistribution inputs
(Heath-Brown's "Siegel zeros imply infinitely many twin primes"). If both worlds gave ES(p), ES would follow.

## 2. Literature anchor

* Heath-Brown, *Prime twins and Siegel zeros*, Proc. LMS (3) 47 (1983) 193–224 *(from memory, unverified)*.
* Extremes of L(1, χ): Littlewood (under GRH), Granville–Soundararajan, GAFA 13 (2003) *(from memory,
  unverified)*. `log L(1,χ_p)` is at most `log log log p + O(1)` above typical under GRH.
* Least non-residue: Graham–Ringrose (`n_p ≫ log p · log₃ p` infinitely often, unconditional); Montgomery
  (`≫ log p log₂ p` under GRH) *(from memory; the Graham–Ringrose transfer is in the campaign's novelty audit)*.
* Campaign: ET heuristic (f ≈ log³p); POINTWISE_SIZE Thm C (square-mimicking primes need witness moduli
  `> exp(c(log p)^{1/4})`); CONDITIONAL_ES ((I)2: nothing known under GRH).

## 3. Experiment (EVIDENCE)

Data: f_II(p) from the R128b from-scratch counter (`scripts/review_r128b_count.c`, dump mode) for all 148 863
primes p ≡ 1 (24) in [10⁶, 2·10⁷]. Analysis: `scripts/bs_wild_hardness.py` (`logs/bs_wild_hardness.txt`, 30 s).
Over this range, mean r = 0.0465 and min r = 0.0117 (p = 2031121, f_II = 36). The sd of log r is 0.210.

**(i) χ_p profile.** Put `log L_y(p) = −Σ_{q≤y} log(1 − χ_p(q)/q)`, with χ_p(2) = χ_p(3) = 1 on this class.

| y | corr(log L_y, log r) | slope κ | R² |
|---|---|---|---|
| 10 | −0.455 | −0.386 | 0.21 |
| 50 | −0.521 | −0.370 | 0.27 |
| 300 | −0.523 | −0.366 | 0.27 |
| 3000 | −0.520 | −0.366 | 0.27 |

* **r ∝ L_y(p)^{−0.37}**, and the effect saturates by y ≈ 50.
* Deciles of log L₃₀₀ run from mean r = 0.0529 down to 0.0358, a factor of ≈ 1.5 between the extreme deciles.
* By least non-residue prime n_p = 5, 7, 11, …, 29, mean r = 0.0496, 0.0471, 0.0422, 0.0386, 0.0364, 0.0354,
  0.0344, 0.0315.

**(ii) Congruence share.** Fit an additive one-hot model `log r ~ Σ_q [p mod q]`, trained on half the primes and
evaluated out of sample on the other half:

| moduli | R² | resid sd |
|---|---|---|
| {5, 7} | 0.23 | 0.184 |
| {5, 7, 11, 13} | 0.32 | 0.174 |
| up to 23 (with 9, 16) | 0.40 | 0.163 |
| all prime powers ≤ 97 | 0.51 | 0.148 |

**(iii) Lottery floor.** The mean unordered count is ≈ 95. If the count were Poisson, the per-p sd of log f
would be ≈ 0.106 (rms of `1/√(f_II/2)`). The residual 0.148 is only modestly above that floor.

**Reading (Assessment).** Write `f_II(p) ≈ S(p mod Q) · log³p · (near-Poisson noise)`.
* About half of the log-variance is congruence data at moduli ≤ 100. The χ_p profile alone explains a quarter.
* The rest is close to Poisson noise of the solution count.
* Structure alone costs at most a factor `L(1,χ_p)^{0.37}`. Even at Littlewood/Granville–Soundararajan extremes
  (log L ≈ log log log p + O(1)) that is only `(log log p)^{O(1)}`, against a mean of ≍ log³p.
* So by this law, "near-sterility" can come only from the lottery or from congruence structure at moduli far beyond
  100, i.e. the Thm C regime (moduli up to `exp(c(log p)^{1/4})`). Together with POINTWISE_SIZE Thm C, this is a
  quantitative form of "the danger is not χ_p".

## 4. The Siegel-zero dichotomy: screen

* **GRH world.** Nothing is known to give ES(p) ((I)2, CONDITIONAL_ES Props 2.3, 9.1: termwise GRH misses by
  `p^{1−o(1)}`). The first horn is already empty.
* **Siegel world, exceptional χ_D with D unrelated to p.** χ_D(q) = −1 for most q in a range. Heath-Brown's
  mechanism makes Λ resemble a divisor-type convolution, so primes in thin sequences can be counted. It needs
  long averages over the sequence's variable (twin primes: over n). At fixed p, the ES event concerns the prime
  factors of ≍ 𝓛³ specific integers N_θ(p), and their residues against χ_p, not χ_D. The exceptional character is
  orthogonal to the event. **Collapses (B2/B6).**
* **Siegel world with D = p or −4p** (χ_p itself exceptional). Most small q are then non-residues mod p, which is
  exactly the *easy* regime by the law above (small L(1,χ_p) ⇒ large r). The primes ES worries about
  (square-mimicking, large L(1,χ_p)) are the opposite extreme. Even there the slice event is the H-A lottery.
* **T1.** At n = m², χ_n is principal, so neither world says anything. The step that fails at squares is the
  slice event, as always.

## 5. Barrier screen summary

* B1: about half of the variation is congruence data, consistent with Prop A (Haar/CRT majorants).
* B2: the rest is the slice lottery.
* B3: no main term beyond log³p is involved.
* B6: the law is a statistical statement over p, so it says nothing at a single p (EVIDENCE only).
* B5: the χ-structure is trivial at squares.

## 6. Viability Assessment

**PARTIAL (EVIDENCE law) / COLLAPSES as a route** (to B2 at "the exceptional character decides the slice", and
to (I)2 for the GRH horn).

By-product (EVIDENCE, p ≡ 1 (24), 10⁶–2·10⁷):
* `log r = −0.37 log L₅₀(p) + O(1) + noise`, with R² = 0.27;
* moduli ≤ 100 explain 51% of the log-variance out of sample;
* the residual sd is 0.148, against a Poisson floor of 0.106.

Suggested follow-up (cheap): repeat at 10⁸ with f_I as well, and test whether the residual is Poisson after adding
moduli up to 10³. If it is, then "f(p) = congruence factor × Poisson" is a sharp, falsifiable form of the ET heuristic.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-A.md (per-memo paragraph and
"Overclaims / mis-scopes" list). No computational counterexample is involved (scope/label corrections).

* **Fixed-exponent extrapolation is pessimistic.** The fit r ∝ L₅₀(p)^{−0.37} (p ≡ 1 (24), 10⁶–2·10⁷) conflicts with
  anal_euler_product_law, which finds the same exponent decaying like 1/log p (β·log p ≈ 4.5 for f_II, predicting
  β ≈ 0.29 at log p ≈ 15.5). The structural cost is likely a relative O(log log p/log p), not L^{0.37}; the conclusion
  "the danger is not χ_p" only gets stronger.
* Overdispersion figures reconcile: ≈ 2× Poisson here (after one-hot moduli ≤ 97) vs 9–23× in
  anal_moments_structured (coarser fit); the shift-τ₃ effect is mostly small-prime congruence data. EVIDENCE only.
