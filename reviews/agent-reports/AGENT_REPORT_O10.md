# AGENT_REPORT_O10: window statistic a_min(p), unconditional Ω-results (checkpoint 2)

Branch `side-agent/window-omega`. Deliverable: `POINTWISE_WINDOW.md`
(§0 lists the results). Scripts: `scripts/window_w1.py` and
`scripts/window_joint.py`. Data: `data/pointwise_window/`. Sources archived
in `sources/sieve/`: Teräväinen arXiv:1611.08585 and FHRSS arXiv:2504.20289.

Checkpoint 2 applies all defects D1–D8 of the hostile review
`reviews/pointwise-window-review.md` (branch side-agent/review-window).

## Results

1. **Goal 1. Prop 11.4 is now Theorem W1, PROVED modulo cited sieve
   theorems S1–S3** (semi-linear lower sieve, Selberg upper sieve, BV).
   * **Statement.**
     `#{p≤x : p≡1 (840), (p+3)/4 has no prime factor ≡2 (3)} ≫ x/(log x)^{3/2}`.
     All such p are hard, `a_min≥7`, and the order is sharp.
   * **Gaps.** None found in the sketch. The review re-derived every step.
   * **Cross-check.** FHRSS 2025 Thm 1.1(2) implies W1 directly. Its
     hypotheses were checked literally; it is an arXiv preprint.
2. **Goal 2. The largest unconditional K is 7.**
   * **Theorem W2 (CONDITIONAL on EH; a fixed level `x^{1−ε_0}` suffices):**
     `a_min≥11` for `≫x/(log x)^2` hard p.
   * **Precedent (D1).** W2 is a theorem of the type of Friedlander–Iwaniec,
     *Hyperbolic PNT*, Acta Math 202 (2009) (FI09). FI09 treats two
     half-dimensional absence conditions on shifted primes, p±2 both sums
     of two squares. Its lower bound needs a level close to 1, and the
     unconditional case is still open. So unconditional K=11 is the window
     analogue of a known open problem. The earlier claim "no such result
     known" is removed.
   * **Lemma 6.1 (PROVED).** When a window fails, the prime factors of
     `n_q` lie in a subgroup `K∌−1`, apart from fewer than `qφ(q)`
     exceptions.
   * **The "dimension ≥1/2 per window" consequence is an Assessment (D2).**
     For a single window it is already PROVED (notes Thm 70.9, D6). The
     joint and J-uniform versions are not proved.
   * **Congruence classes.** For a fixed modulus they leave the sifting
     density unchanged (PROVED).
3. **Goal 3. `a_min→∞` unconditionally is not reached (Assessment).**
   * **Single window.** There is no parity barrier, *given* the
     congruence parity of the bad count (Lemma 1.2).
   * **Two windows.** These sit at the linear-sieve parity threshold:
     * Prop 7.2: the generic one-step Buchstab route has margin exactly 0
       at level x.
     * At BV level the route is negative. This is an Assessment, not
       computed (D4).
     * Both routes use parity (D3). Route A wins at level `x^{1−ε_0}`
       through the switched dimension-5/2 upper bound on the two-prime
       configurations.
   * **J≥3.** The sift-to-√x route fails at every level if
     `β^{opt}_{3/2}>2`.
   * **Unboundedly many windows.** The obstruction is dimension growth.
     The exception budget of Lemma 6.1 grows like `≍J^3`, so the
     J-uniform statement is not available.
4. **EVIDENCE.** All results were reproduced by the reviewer.
   * `N_3(x)/(x/(log x)^{3/2})` stays in 0.0123–0.0126 for
     `10^6…10^11`, drifting −2.5%.
   * Joint F1-clean counts are about flat at the scale `x/(log x)^{1+J/2}`
     for J≤8. Columns 7 and 8 settle only from `10^9`.

## Fix log (checkpoint 2)

* **D1.** FI09 is cited in §0, §4.2 (precedent paragraph), §7.3 and §8.
  The novelty wording is recast.
* **D2.** The §0 table splits the label (Lemma 6.1 PROVED / dimension
  consequence Assessment), and §6 drops "rigorous form".
* **D3.** §7.2 now says route B's Bonferroni step already uses parity.
  The gain is the switched `T^{(q)}` bound. Matching rewording in §7.3
  and §8.
* **D4.** "Negative at `x^{1/2}`" is labelled Assessment (not computed).
* **D5.** FHRSS uses [BF12] to pass from genus to form; this is vacuous
  for D=−3. Preprint status noted.
* **D6.** Notes Thm 70.9 / DISCOVERIES #23 cross-reference added. The
  "congruences" label is narrowed, and the J-uniformity caveat is added.
* **D7.** S1 now cites both Opera de Cribro Thm 11.13 and ch. 14, with the
  primary-not-read caveat.
* **D8.** §2.3 is moved before §3, the status line updated, "flat" made
  precise, and the J=7,8 caveat added. Also the β threshold nit for the
  J≥3 row.

## Suggested ledger entry (parent to merge into DISCOVERIES (H))

* (H) `a_min(p)≥7` for `≫x/(log x)^{3/2}` hard p (POINTWISE_WINDOW Thm W1).
  PROVED modulo cited semi-linear sieve, upper sieve and BV.
* `a_min≥11` for `≫x/(log x)^2` hard p (Thm W2; FI09-type). CONDITIONAL on
  EH, or on a fixed level `1−ε_0`.
* Unconditional K=11 is the window analogue of FI09's open unconditional
  case, and `a_min→∞` is not reached (Assessment §7).

## Process note

Three commits on this branch (5de4a2c, 837be82, and one in checkpoint 2)
raced an in-flight edit and committed an empty or partial file. Each was
followed immediately by a restoring commit, and HEAD is complete (verified
by line count). Do not cherry-pick individual commits from this branch.
