# AGENT REPORT O137 — verify.py blocks for DISCOVERIES (I)9–(I)10

Branch `side-agent/verify-longshots`. Two new blocks, (fa) and (fb), go after (ez) at the end of `verify.py`, and
the header docstring is updated. They follow the style of (es)–(ez) (O133). Each block runs the REVIEWERS'
from-scratch scripts as subprocesses, asserts exact outputs and prints one summary line. No author code is run. The
author's stored outputs in `data/lsb/` are used only as comparands. Neither block needs gcc, so there is nothing to
degrade. Both use ≤ 2 cores and ran under `ulimit -v 8000000`. Timings are from a standalone run.

| block | ledger | reviewer scripts | what is checked | s |
|---|---|---|---|---|
| (fa) | (I)9 LONGSHOT_PIGEONHOLE (R135) | review_r135_slices 110, _genus_kneser, _covers 2000 3529 5569 21169 110881, _constants | **Lemma 1.1**, two checks. First, for all 27 primes 5 ≤ p < 110, the solution counts split into Type I and Type II only, and equal 3 × the coprime fibre counts. Without gcd = 1 there is excess at 18 of 27 primes (p = 71: 171 vs 210). Second, ES(p) by a direct solver ⟺ the slice criterion, for all p < 2000: 0 mismatches. **Lemma 1.2**: 96524 tests, 0 failures. **Lemma 1.3**: 0 failures. **Prop 1.4** (Kneser, e < 64): 0 violations, criterion silent on 5280 configurations. **§5 instances** (e = 3, 7, p < 2·10⁵): 0 failures. **§3 covers**: the four lines equal R135's table exactly. The exceptions 3529 and 110881 have no P20 cover for e ≤ 2000 (max covered 12). **(b2) constants**: 33, 19, and the ratio 0.0713 → 0.0627 | 44 |
| (fb) | (I)10 LONGSHOT_FIBRED (R136) | review_lsb_et16, _pell, _f4growth, _spinor 50000, _genus, _typeII_genus | **ET Prop 1.6**: no Type I/II solution at the odd squares 9…225 (incl. 9, 25, 49). **F2 Pell identity**: holds on all 3303 Type II quadruples (p < 1500), no unit power recurs, max log(2T)/log p = 1.812. **F4 counts**: 152, 300, 602, 1206 at H = 250…2000. Also, R136's count function at H = 3000 gives 1800, the author's stored count for the orbit (n = 29, A = 3). At n = 9, 25, 49, 4n+1 is prime ≡ 1 (4), so there are 4 genus-full orbits and 0 ES orbits; this matches the stored table. **F5/§5.2 spinor exceptions**: up to 5·10⁴ they are exactly the 29 numbers in M₃², and there are none the other way. **Prop 5.3 / 𝔊⁻_d**: the table equals `data/lsb/genus_minus.out` line for line, with h⁻ = h/2 at all 40 prime pairs, 0 at all 40 square pairs, and F_d(p) = 0 in 19/40. **D5**: output = `data/review_lsb_typeII_genus.out`, with the f-form χ = −1 always and the e-form χ = −(d/p) | 44 |

Scope notes (what is NOT covered):
* (I)9: the Lemma 1.1 count check stops at p < 110 (R135's run). The ES ⟺ slice check is hard-coded in R135's script to
  p < 2000, which runs in about 3 s. Covers are checked at 4 of R135's 6 primes. The two 10⁸ primes need E = 5000 and
  were left out for time. CONJECTURE PH (all hard primes to 3.7·10⁷) is not re-run.
* (I)10: the F4 orbit counts at the squares 9, 25, 49 (3230, 1918, 1382) are author-only EVIDENCE. R136 did not
  recount them. The reviewer's `count` uses the box |a|, |c| ≤ √H + 2, which is not guaranteed to cover the orbits of
  `[1,2,10]`-type bases, so I did not reuse it there. The block checks the structural facts instead (4 orbits, 0 ES
  orbits, 4n+1 prime ≡ 1 (4)) together with ET Prop 1.6. For Q = [3,4,11] the box is provably big enough
  (λ_min ≈ 2.53), and there the reviewer's count reproduces the author's 1800 exactly. The citation-only parts
  (EM/EMS/BR/CTX, Thm 3.1, Thm 5.4) have no numerical content.

Full `verify.py` run: see below.
Full `verify.py` run (`(ulimit -v 8000000; OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 3000 uv run --with scipy
--with mpmath python verify.py)`, nohup, about 15.5 min wall time): **`all checks passed`, exit 0**. There are 157 section
headers, and no block was SKIPPED. Seconds in the full run: fa 46.2, fb 46.5.
