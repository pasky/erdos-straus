# AGENT_REPORT_O10: window statistic a_min(p), unconditional Ω-results (checkpoint 1)

Branch `side-agent/window-omega`. Deliverable: `POINTWISE_WINDOW.md`
(§0 lists the results). Scripts: `scripts/window_w1.py` and
`scripts/window_joint.py`. Data: `data/pointwise_window/`. Sources archived
in `sources/sieve/`: Teräväinen arXiv:1611.08585 and FHRSS arXiv:2504.20289.

## Results

1. **Goal 1. Prop 11.4 is now Theorem W1, PROVED modulo cited sieve
   theorems.** The statement:
   `#{p≤x : p≡1 (840), (p+3)/4 has no prime factor ≡2 (3)} ≫ x/(log x)^{3/2}`.
   All such p are hard and have `a_min≥7`, and the order is sharp.
   * **Inputs.** The semi-linear sieve (β=1) at BV level gives
     `z=x^{1/2−ε}`. Parity of the bad count (Lemma 1.2) leaves 0 or 2
     large bad primes. A uniform prime-pair upper sieve bounds the
     two-prime configurations by `ε^{3/2}`, against a main term `ε^{1/2}`.
   * **Gaps.** None found in the sketch.
   * **Cross-check.** FHRSS 2025 Thm 1.1(2), with `f=x²+xy+y²`, `B=4`,
     `A=−3`, `m=35`, implies W1 directly (hypotheses checked).
2. **Goal 2. Largest unconditional K is 7.**
   * **Theorem W2 (CONDITIONAL on EH):** `a_min≥11` for `≫x/(log x)^2` hard
     p. It is the same skeleton with the linear sieve near `s=2`. The key
     step keeps the other window inside the dimension-5/2 upper bound, so
     the two-prime terms cost `ε^{3/2}` against a main term ε.
   * **Lemma 6.1 (PROVED).** Every failing window forces the prime factors
     of `n_q` into a subgroup `K∌−1`, up to `<qφ(q)` exceptions. So each
     window costs sieve density `≥1/2`.
   * Congruence classes on p cannot lower this. The brief's idea "kill
     windows by congruences" is impossible (Lemma 11.3) and saves no
     dimension.
3. **Goal 3. `a_min→∞` unconditionally is not reached (Assessment).**
   * **Single window.** There is *no* Selberg parity barrier: the parity
     of the bad count is a congruence datum, and it is an input to W1.
   * **Two windows.** The problem sits exactly at the linear-sieve parity
     threshold. Prop 7.2: the generic one-step Buchstab route has margin
     *identically 0* at level x, and is negative at BV level.
   * **J≥3 windows.** The sift-to-√x route needs `β_{J/2}≤2ϑ≤2`. This
     fails at every level of distribution if `β^{opt}_{3/2}>2`, which is
     expected but not proved here.
   * **Unboundedly many windows.** The obstruction is dimension growth
     against `z≤x^{1/2}`, not formal genericity.
4. **EVIDENCE.**
   * `N_3(x)/(x/(log x)^{3/2})` is flat at 0.0123–0.0126 for
     `10^6…10^11`.
   * Joint F1-clean counts for J≤8 windows are flat at the scale
     `x/(log x)^{1+J/2}`.
   * 5731 primes `p<10^11` with `p≡1 (840)` have `a_min≥35` by F1 alone.

## Self-review

A deep reviewer subagent ran over the whole branch. All points are
addressed in the commits "Review fixes 1/2" and "Script fixes".

* **Restored file.** Earlier commits had raced an in-flight edit; a
  restore commit fixes this.
* **W2.** The remainder now needs `(log x)^{−3}` from EH.
* **Wording.** Claims of "needs ϑ≥1" are now scoped to the analysed
  routes. A fixed level `1−ε_0` suffices for W2.
* **Lemma 6.1.** Its counting consequence is downgraded to Assessment,
  because the exceptional primes vary with x.
* **Citations.**
  * The semi-linear and linear lower-bound statements are standard. The
    archived secondary source shows only their application; this is now
    stated.
  * The missing `gcd(l,m)=1` hypothesis is added to the FHRSS
    statement.
* **Small fixes.** A false claim "`n_7/2` odd" is removed. The W1 final
  constant is corrected, and `g_q` is now used in Prop 7.2.
* **Scripts.** Fixed the duplicate edge row, the filename collisions and
  the unbounded memory (reservoir sample). Data regenerated.

The reviewer independently reproduced the joint counts at `10^6`
(395/244/160/52/28/9/4/2/1). It found W1 sound, with ε-independent
constants.

## Suggested ledger entry (parent to merge into DISCOVERIES (H))

* (H) `a_min(p)≥7` for `≫x/(log x)^{3/2}` hard p (POINTWISE_WINDOW Thm W1).
  PROVED modulo cited semi-linear sieve, upper sieve and BV.
* `a_min≥11` for `≫x/(log x)^2` hard p (Thm W2). CONDITIONAL on EH.
* Unconditional K=11 and `a_min→∞` are not reached (Assessment §7).

## Open for the parent

* Is W2 worth pushing to an unconditional K=11 via Chen-type switching
  at BV level? Prop 7.2 suggests the margin is genuinely negative without
  new input. My recommendation: no, unless a BFI-type level `>1/2` for
  varying residue classes becomes available.
* Optional: write out the almost-prime sum that would upgrade Lemma 6.1's
  consequence to PROVED.
