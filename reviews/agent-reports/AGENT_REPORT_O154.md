# AGENT REPORT O154: adversarial hard-prime construction (brainstorm)

Branch `side-agent/bs-adversarial`. Memos: `BRAINSTORM/adv_stacked_primes.md`, `BRAINSTORM/adv_new_drivers.md`.
Scripts: `scripts/bs_adv_*`. Small logs: `logs/bs_adv_*`. ES is not solved, and nothing here proves any case of it.

**adv_stacked_primes.md (O154(a)). Verdict: COLLAPSES as a disproof direction; the lottery model passes the stress
test (finding β, no H-A/H-E signal).**
* *Tool.* A new exact single-prime `f_II` counter (`bs_adv_count.c`). It uses segmented-sieve slices for e ≤ E
  and a small-witness loop for e > E, which is exact by `f < 2p/E + 1`. It agrees with the 10⁸ dump on 400
  random primes with random splits, and it runs to 10¹⁶.
* *Data.* 351 constructed and selected primes at 10⁸–10¹⁶, all solved, each with an exactly verified solution.
  * The stacked designs combine the class of one mod `24·∏_{ℓ≤37}ℓ`, prime shifts, QR to 61, and selection of
    empty small slices among about 7000 candidates.
  * These reach only ≈ 0.65× the random `p ≡ 1 (24)` mean of `f_II/log³p`. The hardest prime found is
    `p = 1180607468041`, with `f_II = 538 = 0.025 log³p` and slices e < 47 empty.
* *Strongest reason.* `f/log³p` is scale-invariant to within ±3% from 2.6·10⁵ to 10¹⁶ in every design.
  * 0.046 for `p ≡ 1 (24)`.
  * 0.034 for the class of one, the same as the mod-120120 value at 10⁸, so the local factor is saturated.
  * The small-slice share decays like `L^{−1.1}`, and the CV shrinks.

  So the predicted count of the best constructible adversary is `≈ 0.03 L³` (≈ 1500 at 10¹⁷). It never drops
  below 1. Bringing the expected number of sterile primes to order 1 would need a depression `c ≲ 3/L²`, about 15×
  beyond anything constructible at 10¹⁷ and widening. Even idealised square-mimicking up to the Burgess range
  removes ≲ 15% of the log-mass in the model.
* *By-products (EVIDENCE).*
  * The scale invariance above, and the confirmed saturation of the local factor.
  * The heavy small-e tail of O142 is a lower-order effect, so the almost-all asymptotic `f_II ~ 𝔖_loc(p) log³p`
    (CONJECTURE) is consistent with the data.
  * W(p) is the only quantity the adversary moves; it scales linearly with y.

**adv_new_drivers.md (O154(b)). Verdict: COLLAPSES to B1 + B2. No global driver.**
* *Setup.* 20 000 primes `p ≡ 1 (24)` in [5·10⁷, 10⁸]. Regressors: cells mod 120120, local features (smooth part
  of `p − 1`, `v₂(p−1)`, the truncated `L(1, χ_p)`, the least non-residue) and shifted-divisor features
  (`τ((p+e)/4)`, `τ(cp+a)`).
* *Strongest reason.* These explain R² = 0.56, against a compound-Poisson noise floor of ≈ 32% of the variance.
  The genuinely global invariants add nothing: the exact `h(−4p)` tail beyond its Euler-product head, the CF period
  of √p and the regulator have |partial corr| ≤ 0.01 (s.e. 0.007).
* *Ranking.* The largest driver beyond O142's baseline is the square class at primes 17…2·10⁴ (partial −0.14).
  That is congruence-type with growing moduli.
* *Correction to O142 §3.6.* Its "weakly positive" `L(1, χ_p)` correlation is a Simpson's-paradox aggregate over
  the mod-24 classes. Within `p ≡ 1 (24)` it is −0.51; it is positive only in the `p ≡ 3 (mod 4)` classes.
* *Structural remark* (PROVED, elementary; the known {a,c} row): `f = 4acd−1 | p + 4a²d ⟺ cp + a = b·f`. So
  O142's dead-modulus `p − 1` driver is the signed slice `(a,c) = (−1, 1)`.

**Not done.** `f_I` for the adversaries (existence was already certified via Type II; `corr(f_I, f_II) = 0.85`
within cells per O142). Adversaries at 10¹⁸ (the counter needs `p < 2⁶²` and ≈ 1 h per prime; not attempted).
