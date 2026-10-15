# z10_pointwise_cap — the minimal cap e*(n) and where it meets the sieve (O234; CAP_INTERPOLATION.md §4)

**ES is not solved here.**

## Idea
Measure the cap pointwise as e*(n) := min{e : ES^{(y,e)}(n)} (ES ⟺ e* = 0). Thm 4.2 of FROBENIUS_FIRING gives
e* < ∞ ineffectively; PHASE_DIAGRAM Thm 5.1 is family-form and bounds e*(n) only by x₀(n)^{o(1)}.

## Result
* Prop 4.1 (PROVED): covering (F_r^*)² at a prime certifying r needs e ≥ (log log p)^{1−o(1)} for infinitely many p
  (Linnik: p ≡ 1 mod 8∏_{q≤R} q forces r > R ≍ log p). Same scale as the almost-all saturation (z10_uniform_cap).
* Thm 4.2 (CONDITIONAL on GRH, citation-level sketch): e*(p) ≤ C_ε(log p)^{2+ε} (k = 1 mute prime, Hooley–Lenstra with
  Lagarias–Odlyzko) and e*(p) ≤ exp(O(√(log₂p log₃p))) (k ≍ √(log₂p/log₃p) mute primes + Minkowski II as in (J)43).
  Min-form only; family-form polylog stays open even under GRH.
* EVIDENCE: the Thm 4.2(a) prime is ≤ 251 for all p < 10⁶, 47/71 for adversarial p ≈ e^{32}.

## Barrier screen
GRH is used only as effective Chebotarev in Kummer fields of small degree — B3 does not apply (no main-term
certificate at a single n; the count is over r). Unconditional version blocked by Siegel (BV at modulus ≈ n).

## Assessment
The conditional pointwise statement is new to the campaign (FROBENIUS Thm 4.4 had existence only). Gap:
(log₂)^{1−o(1)} vs exp(√(log₂ log₃)) under GRH.
