# z29_nb_tail_model — negative-binomial model of N₁(p) and the finite-failure prediction (O259; B1_LINE §§3.3–3.5)

**Idea.** Build a calibrated random model for N₁(p) that predicts the expected number of failures beyond X, and test it on the
data and on the (★) line.
**Literature.** ET 2013 (mean of f_II ≍ log³ p); Hardy–Littlewood-type independence heuristics; PARITY_AUDIT §2 (lottery
framing); Cohen–Lenstra-style class weighting enters only through the class means (§3.2).
**Result (EVIDENCE + heuristic).** N₁ is overdispersed (var/mean 2–3.6), but the relative spread falls (0.33 → 0.22 from 10⁶
to 10¹⁰). NB(μ = bin mean, D) back-test ≤ 10⁶: 1.2 predicted vs 2 observed zeros. #{N₁ ≤ 2}: 16 predicted vs 33 observed, so
the model is about 2× optimistic in the tail, and equally so for (★) (3.4 vs 7). Extrapolation with μ = (log p)²/8, D = 3.24:
1.1·10⁻⁴ failures expected beyond 10⁸, 1.4·10⁻¹⁰ beyond 10¹¹. With every prime treated as hardest-class (−20 %): 0.013 and
8·10⁻⁷. Conjecture 3.5: exactly three failures. Test of the model on (★): it predicts 1.8 (★) failures beyond 10⁸ (or up to
50 with the depression); see B1_LINE §3.6 for the (★) census to 10¹⁰.
**Barrier screen.** B3 (main term ≍ (log p)² is above p^{o(1)} but the error is unbounded pointwise), B6 (calibrated on
averages). Dickson (Thm 4.2) shows the tail is not Poisson for bounded shift sets. For the full line it changes only lower-order
terms (Assessment).
**Cheap numerics.** `z29_model.py` on the complete counts ≤ 10⁶ and windows at 10⁸, 10¹⁰; census ≤ 10¹¹ (0 failures above 66529).
**Assessment.** CONJECTURE with a calibrated heuristic. Not a proof route. The value is a falsifiable prediction (no failure
anywhere above 66529) and an honest measure of the margin.
