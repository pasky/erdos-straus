# Z69 MINE — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** Accept the census, Lemma 4.3, and a narrowly descriptive non-rejection result; do not record that the hard-prime pointing problem, or all CF effects, has been resolved. **ES remains OPEN.**

Reviewed `side-agent/z69-mine` at `e149a0ba8be550313a47f6a3f66ed17c66908088`, including `Z69_MINE.md`, its engines, fit/sampling/analyser code, committed raw records, Z60 Lemma 7, Z68_U7F/U7O, and the actual z58 screens. No provider/auth/quota error occurred.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Exhaustive census: all 1,439,970 primes p ≡ 1 (8), p ≤ 10⁸ have W ≥ 1; W = 1 only at 2521 | CORRECT / reproduced | Recompiled and reran the complete census. A separate literal f-loop agrees for all 2,384 such primes ≤ 10⁵ and 16 named hard primes, including 2521. All 165,976 committed census rows ≤ 10⁷ agree with the rerun. |
| Only non-square zeros n ≡ 1 (8), n ≤ 10⁸ are Z₇ | CORRECT / reproduced | Full census gives exactly {105,1465,3865,4545,10305,12145,39361,67425}. Independent literal scan of all 12,500 n ≡ 1 (8), n ≤ 10⁵ gives the same eight and no prime zero. |
| Lemma 4.3, all anti-alignment cases | CORRECT | Re-derived below; no hidden primality/composite-modulus exception found. The exclusions concern f dividing a coordinate, not coordinate divisors used as letters. |
| Local model R²(w) ≈ .434, Poisson share .308, Pearson variance 1.85 | CORRECT as descriptive EVIDENCE | Regenerated from the fresh census: .4337, .3081, 1.850. Cross-fit assignment uses no held-out W in training. |
| Local + shifts explains ≈ .44, noise ≈ .35 | CORRECT-WITH-FIX | Regenerated τ data and fit: R²(log w) = .4384; printed benchmark .352. This is not an identified variance decomposition; its noise estimator is mean(1/W)/Var(log w), not a Poisson simulation using the fitted mean. |
| Heavy fitted lower tail | CORRECT as model-specific EVIDENCE | Local+shifts NB rerun: 180 vs 122.1 at 10⁻³ and 31 vs 11.3 at 10⁻⁴; inflation 1.581. Does not exclude better local interactions or establish nonlocal causation. |
| Phantom numerical ratios / window and identity implementation | CORRECT / audited | Independently recomputed pooled ratios and cluster intervals from all five raw runs; agreement to printed precision. All phantom primes, congruences, same-size windows, canonical xz words, and q ≠ p checks pass. Raw PARI feature values were not all independently regenerated. |
| Hard-set matching “resolves” quadratic/Pell/class-number effects | CORRECT-WITH-FIX | Differences disappear for these pooled tests, but exchangeability and size robustness are not established. Same sampler is not sufficient to justify difference-in-differences; see controls below. |
| CFk/CFh excess is “explained/resolved by period length” | GAP in the stronger wording | The original diagnostic only computes CFk, not CFh, and uses multiplicities rather than the original any-hit statistic. Independent CFk/CFh diagnostics retain small residuals; replace “explained” with “mostly tracks period length.” |
| No candidate passed K4; tested n_p/nq₇/divisor-union rules fail | CORRECT, narrowly | A displayed failure suffices to fail all-H coverage. This does not kill other non-residue, class-group, CF, or letter-generation rules. |
| “No relation family showed a p-specific enrichment” / blind-search assessment | CORRECT-WITH-FIX | No replicated, adequately controlled enrichment was established. That is weaker: QS/CFpA/H-z are unresolved, several target primes are omitted, and pooled non-rejection does not test one successful candidate per prime. |

## Proof re-derivation

For r | f+1, gcd(r,f)=1, hence gcd(p,f)=1 directly from p ≡ −r (f); the memo's bound-based argument is also valid. Write r=2ᵉs with s odd. Since f ≡ −1 (s) and f ≡ 3 (4), reciprocity gives (s/f)=1; (2/f)=1 because f ≡ 7 (8). Thus (r/f)=1 and **(p/f)=−1**. In particular an odd square can never be witnessed.
For f | a or b, p becomes a unit square modulo f. For f | c or d, it becomes twice a unit square or a unit square; (2/f)=1. For f | g or v it becomes a unit square. If f | u, 3 | f would force p=3; otherwise (p/f)=(3/f), so only (3/f)=−1 is possible.
For a complete-quotient norm Q_i, h²−pk²=±Q_i with gcd(h,k)=1. If f | Q_i, every prime dividing gcd(k,f) also divides h, impossible; therefore p is a square modulo f.
For Pell, f | U would make −1 a square modulo f, contradicting (−1/f)=−1. If f | T, pU²≡1; if f | T±1, pU²≡2. In both cases U is invertible modulo f, contradicting (p/f)=−1. No prime-modulus assumption was used.
The exception e is genuine: p=41, e=7, g=2, f=7 gives (x,y,z)=(1,8,6). Jacobi +1 is not the assertion “square modulo composite f”; the memo's final bottom-line shorthand should retain that distinction.

## Decisive independent computations

Literal exhaustive f ≤ 2n+1 counts `(p: W, least f)`:
`2521:1,87; 3361:2,679; 9601:2,111; 14177:9,87; 21841:4,575; 66529:6,39; 76441:4,279; 225289:4,287; 712321:4,23; 1095481:4,1119; 1381969:4,1351; 2031121:4,21383; 3613009:8,3415; 4149601:5,911; 45553561:7,1175; 96049801:10,159`.

Independent pooled real/phantom ratios (±2 cluster SE): same-size controls divf **1.005±.035**, divq **1.008±.008**, divxy **1.011±.016**; xz controls divz **1.011±.016**; matched H **1.041±.076**, **1.003±.010**, **.983±.016**, respectively. These confirm the arithmetic, not the null model.
Independent period-normalised multiplicity ratios `(real rate)/(phantom rate)` on H: CFk **1.0315**, diagnostic 2-SE interval **[1.0071,1.0565]**; CFh **1.0272**, **[1.0013,1.0538]**. Controls: **.9831** and **.9872**. H CFk totals 62,546/38,056 reproduce exactly. These modest residuals are not a replicated ≥4σ discovery; neither are they evidence of complete explanation. Uniform L/f is only a diagnostic model.

## Controls, leakage, and power

* **Actual sample differs from the stated cutoff accounting.** H has 849 primes. Eighteen are below 10⁴, including **2521, 3361, 9601**; nine exceed 2·10¹⁰. Thus the analysed population is **822**, not 840; the joint cutoff skips **27**, not nine. Controls: 2,547 → 2,468. The 840/2,520 denominators apply to the older upper-cutoff-only union test.
* H and CTRL are disjoint. `sets.py` draws roughly three nearby controls per H prime, using an approximately ±26% linear window followed by next-prime selection; this is **not log-uniform sampling**, and primes receive gap-dependent weights. Median p is 19,201,081 vs 18,995,369: reasonable approximate size matching, not exact matching.
* **No direct self-leakage found:** q never equals its real p, and the code computes the phantom dictionary from q, not p. Sharing f and x,y (or x,z) deliberately conditions on a witness; it is not a witness-independent rule-generation experiment. H membership itself is selected using W/other witness properties. Matching a few residue symbols does not remove every consequence of that selection.
* Phantom reuse is small but nonzero: same-size H has 7,822 phantom occurrences / 7,779 distinct q, controls 7,764 / 7,707; 39 and 54 occurrences belong to H∪CTRL. Prime-only clustering ignores those links. Use disjoint phantom pools or a dependency-aware resampling sensitivity check before interpreting precise significance; this is not evidence of a large current error.
* Same-size H covers **4,197/6,409** sampled records; controls **4,129/7,404**. No f>p/16 record can be covered. Sampling caps and record weighting do not test whether every prime has one useful, possibly rare/large-f, witness. There is no held-out replication of the unresolved H signals.
* **Matched size robustness is asserted too broadly.** Median q/p is 740 on H and 1,239 on controls. In 2,053/3,098 H records, f>3√(2p), so every G2 linear value is smaller than f: real G2:divf is structurally impossible, not in a “modulus ≪ values” regime. The analogous C2 bound excludes 2,104 records, one of which has a phantom C2:divf hit. These examples do not show a large pooled bias, but disprove the blanket justification. divq can also involve large factors; divxy is explicitly size-sensitive.
* Difference-in-differences requires comparable size/modulus/profile-induced bias, not merely identical sampling code. H/control witness distributions differ by construction. Report strata/reweighting by log p, f/√p, factor sizes, letter sizes, and local profile, and retain uncertainty about unbalanced regions. Exposures must stay symmetric at the Pell cutoff, as the current analyser correctly enforces.

## Strongest open / under-powered families: concrete next tests

1. **Q-set letters and CFpA, first priority.** QS divxy remains strongly anomalous after set-size normalisation; QS eqxyf and CFpA divxy/vdivz are unanalysed. Stream the **full** period (not its first 4,000 positions), retain index/orientation information, and test individual candidate letters/divisors plus simple gcd/ratio relations. Split by prime before choosing relations. Compare within size/local-profile/Q-set-size strata; report truncation sensitivity and per-prime witness coverage, not only pooled any-hit counts.
2. **H z-relations and large-f witnesses.** Run the xz design on H, including all small hard primes, with full witness lists and prime weighting. Require matched local profiles and report where simultaneous matching is impossible. Generate candidate outer letters z from norm coordinates, class data and CFpA without consulting witnesses; test x | p+z and the U₇ congruence afterward. This directly targets the blind region of fixed-f phantoms.
3. **CF convergent positions / Pell letter rules.** Compare CFk and CFh indicators and multiplicities with period-length-matched controls and an f-dependent exposure model; stratify early/middle/late positions and test cross-fitted residuals. Pell in the phantom code is tested only for divf/divq: test residues of T,U,T±cU and small shifts modulo candidate x,y,z, not just modulo f. Lemma 4.3 does not exclude these letter rules.
4. **Class-number / class-group and non-residue structure.** Phantom CL contains h(−4p), h/4, n_p, nq₇, not h(p), h(−8p), class-group structure or representation-ideal orders. Test these separately, rather than OR-pooling CL, and their gcd/quotient relations with norm/CF letters. Matching small Legendre symbols can nearly fix n_p itself: a null conditional contrast cannot kill rules using it jointly with other data. The exact tested n_p-menu failures remain valid.
5. **Joint norm data and adaptive combinations.** Mixed Gaussian/C₂/Pell coordinates, small affine shifts, ratios/gcds, factor cofactors and adaptive coefficients are mostly absent; separate same-form linear/quadratic dictionaries do not test them. Pre-register bounded-complexity candidate generators, factor only their generated values, then score verified witnesses on untouched H subgroups and new size bands. No witnesses may enter candidate generation or feature selection for the held-out primes.

For all five: report per-family effect intervals and injection-based detection power, especially for **one informative witness per hard prime**. Use all H (or explicitly list exclusions), subgroup results for H-low/np/u8/deep, and a genuinely disjoint replication. “Enough power for broad pooled deviations on covered records” is not “enough power to reject a constructive relation.” None of these tests is required to claim that no successful rule was obtained; they are required before declaring the corresponding avenues exhausted.

## Mandatory falsifiers

| Screen | Checked outcome / memo repair |
|---|---|
| F1 odd squares | Full census: zero exceptions ≤10⁸; independent literal scan confirms all odd squares ≤10⁵. The proof above covers every odd square. |
| F2 actual 12 R₈-zeros | All 12 directly re-witnessed; least f, in file order: **7,7,2239,87,1559,143,7,143,15,7,39,31**. Restore this outcome in the final table: the additional 38 U⁽⁸⁾ zeros are not a substitute. No mechanism was tested. |
| F3 all 285 composite zeros | Independent direct search: **277 U₇-positive, exactly the eight Z₇ negative** (negative cases exhaustive). State the 277/285 split, not just Z₇. |
| F4 14 (★)- and 38 𝔊*-zeros | All directly re-witnessed. The final table's restricted p ≡ 1 (8), p ≤10⁸ census is not by itself the justification for the full supplied screen. |

## Required fixes, priority order

1. Restrict §4.4/§6–9 and proposed FRONTIER language to observed, non-replicated, sampler-specific non-rejections; explicitly leave CF residuals, QS, CFpA, H-z and untested letter/class-group rules open. No general “blind search” conclusion follows.
2. Correct the 27 excluded H primes and non-log-uniform controls; disclose structural size exclusions even for divf/divq, and make the matched/DiD conclusion conditional on unverified exchangeability. Do not interpret pooled intervals as limits on per-prime rule coverage.
3. Replace “CFk/CFh explained” by “most multiplicity excess tracks period length”; add the missing CFh diagnostic and residual uncertainty, or withdraw that part. Use the same estimand when comparing pre/post-normalisation effects.
4. Label .352 as the observed-count plug-in Poisson/delta-method benchmark; do not present .44 + .35 as separate established components of variance. Keep log w and w, and their different sample ranges, distinct.
5. Restore the full F2/F3/F4 outcomes and fix the bottom-line Jacobi-versus-square shorthand. Preserve the elementary theorem and finite census without promoting empirical assessments to PROVED.

## Reproduction / scope

Review scripts: `scripts/z69_xrev_mine_direct.c`, `scripts/z69_xrev_mine_audit.py`, `scripts/z69_xrev_mine_period.py`. Extract the reviewed branch into `/tmp/xrev_MINE`, compile its `z69_mine_W.c`, and save `W 100000000 100000000` as `census.txt`; compile the review direct checker there. Run the audit with arguments `/tmp/xrev_MINE /tmp/xrev_MINE/census.txt /tmp/xrev_MINE/direct`; run the period script on `raw_ph3_{H,C}.jsonl.gz`.
All runs used **ulimit -v 6000000**, command timeouts ≤1,050 seconds, ≤2 simultaneous compute jobs, and `uv` for Python. Fit reruns used fresh census/τ intermediates with temporary path substitutions; BLAS threads were capped at one. The review independently checks the decisive census subrange/hard primes/screens and raw-record statistics, not every descriptive morphology/Euler-sum/scale-correlation result. No files on the reviewed branch were changed.
