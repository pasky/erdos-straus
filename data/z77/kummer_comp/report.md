Result: Every one of 23,325,118 primes in six square-offset families above the z76 floor has R₈, R and Type A witnesses; 1,881,841 forced-composite panel entries all have R and U₇ witnesses. Label: CERTIFIED (specified finite panels); EVIDENCE (interpretation).
Scope: p=m²+c, 1≤m≤10⁸, c=1,4,16,36,64,100, p>1,590,284,203,561; composites are separately selected. No new zero, unrestricted threshold, or change to ES.
Review: cross-model (Opus audit and responses: `data/z77/kummer_review.md`).
Triage: DATA
STATUS delta: none

# Track 3: does the square-shift deficit produce a zero?

**No in these panels.** The offset-1 search includes **92,596 Mordell primes**, 62,097 above 10¹⁵. Of the 49,679 with no R₈ word through modulus 1,000, the ascending discovery scan sent 196 to fallback after modulus 2,000,000; all 196 admit independently checked R₈ triples. This re-enumerates inputs above the current floor (including the overlap with z76), rather than adding 92,596 new primes to z76. All six Mordell residue classes are tested; for offset 1 only 1 and 121 mod 840 occur. For c=4,36,100 and an odd prime p above the floor, m is odd and p≡5 (8), so **none** belongs to 𝔐. Nevertheless all their primes at these heights enter the all-residue test.

| c | all primes | first R₈ f>1000 | f>2·10⁶ (single engine) | Mordell primes | Mordell f>1000 | Mordell f>2·10⁶ (single engine) |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 3,887,239 | 1,722,199 (44.3%) | 4,082 | 92,596 | 49,679 | 196 |
| 4 | 3,886,506 | 217,423 (5.6%) | 125 | — | — | — |
| 16 | 3,888,355 | 416,953 (10.7%) | 172 | 185,008 | 31,566 | 18 |
| 36 | 2,594,334 | 593,130 (22.9%) | 377 | — | — | — |
| 64 | 3,886,730 | 174,683 (4.5%) | 61 | 184,584 | 14,136 | 2 |
| 100 | 5,181,954 | 333,279 (6.4%) | 140 | — | — | — |

The rows are disjoint: throughout this range consecutive squares differ by more than 100. Of the 23,325,118 primes, 462,188 are Mordell and 15,685,610 exceed 10¹⁵ (310,296 of those Mordell). **4,957** R₈ exact fallbacks, all positive. Absence of a word through 2·10⁶ for those fallbacks is single-engine EVIDENCE, not needed to certify existence. Absence through 1000 was independently checked. For example, at p=9,999,176,016,974,401, `(u,B,C)=(12,83,1254916668797)` gives `p=8uBC−u−B`. Every prime had both an R and a Type A word by f≤2·10⁶. Thus no higher R₈-zero floor, no 15th prime R-zero and no 4th Type A-zero here. This says nothing about primes not represented in the six ranges.

**Losing a shot need not lower the mean number of hits.** In `p=m²+c`, the R₈ word with `f=8uC−1` requires `m²≡−(c+u) mod f`. At `u=c=a²`, the target is **−2a²**, not −a². Since (a,f)=1, f≡7 mod 8, the Jacobi symbol is (−2/f)=−1, so this shot is indeed impossible. The conjectured broad cheap-hit suppression does not follow. `local.txt` evaluates each of the 623 shots with f≤1000: take m uniform mod f conditioned on gcd(m²+c,f)=1, count *all* root residues for the shot, sum its probability. In offset order the means are **0.824, 3.084, 2.361, 1.484, 3.445, 3.354**, versus **2.891** at uniform units p mod f. Root multiplicity of surviving shots matters. This calculation is for **all classes**, not an exact CRT-matched Mordell control, and is not an independence model for the probability of being late or of being a zero. The preceding table counts actual no-hit events. Neither the table nor these marginals establish a prime zero rate. For the matched offset-1 analysis see `notes/z76/DISPROOF_COMP.md` §2.

## Composite stacks: which are possible?

For an odd prime q≡3 (4), `q | m²+a²` forces q|a,m: otherwise −1 would be square mod q. Thus for the five small even-square offsets, the proposed stack 11·13·17·19 is **impossible** (11 and 19), as is 105 (at least 7); these are empty conditions, not empirical nulls. We use split factors for the small offsets, and enforce common factors for the original stacks by changing d in `a=2d`.

* For each `a=2,4,6,8,10` require **13·17·29·37 | n**. For `a=418,836` (`d=209,418`) require **11·13·17·19 | n**. These panels take every odd m≤10⁸ above the same n-floor with `n` in 𝔐 if `n≡1 (8)`, and `n+420` in 𝔐 if `n≡5 (8)` (membership means the six residues mod 840). The latter is a comparison class, **not** 𝔐; both classes are 1 mod 4 and coprime to 105. Counts in a order: **96,96,189,96,379; 123,120**. All are nonsquares satisfying the (MS⁺₁₀₅) hypotheses; all have R and U₇ certificates.
* For `a=42,84` (`d=21,42`) take **all odd m≤10⁸** above the same floor with **105 | n**; 940,371 per offset. These two panels are **outside (MS⁺₁₀₅)**; they test U₇, hence U_II and CONV-II via `U₇ ⊂ U_II ⊂ Type II` (see `Z60_LOPEZ.md` and `FRONTIER.md` §2). Every row has a U₇ witness. The additional R scan needed 8 and 1 exact rescues respectively; all nine are positive. A factor q|n kills words with q|f since u|f+1, but it does not kill all words.

All selected n lie strictly between m² and (m+1)², checked rowwise. `summary.txt` gives panel sizes, caps and maxima for the bounded composite detectors. The CRT restrictions do not define a consecutive composite census. R₈ here always refers to the C-even half of (★), not the full numerator-8 equation. The square, numerator and averaging screens in `FRONTIER.md` §4 rule out extrapolating from this finite hunt to ES or pointwise positivity.

## Certificate and replay

From the repository root run `bash scripts/z77_kummer_replay.sh`. This runs serially with `ulimit -v 6000000`, timeouts ≤1800 s and offline uv Python. The regenerable ~0.5 GiB witness sheets are identified by `sha256.txt`, not checked in. `fallback.txt` **does** retain every hard triple (`k n u B C`); `checks.txt`, `summary.txt`, `local.txt` supply the other expected outputs.

1. `z77_kummer_prime.cpp` enumerates m by residue mod 840 in the prime families; rejection by gcd with 210 is safe above the floor. It uses deterministic 64-bit Miller–Rabin (first 12 prime bases); its primality/coverage claims do **not** stand on that routine alone. It tries R, R₈ via `u=−n mod f`, `u | (f+1)/k`. For Type A it uses `4 | u`, `u | f+1`, or lifts u=1 to u′=f+1; then n=4abc−4a−b with a=u′/4 (or u/4). U₇ needs `f≡7 (8)`, `u | f+1`. The upper scan cap is not a decision of nonexistence.
2. `z77_kummer_check.cpp` independently sieves by every possible least prime factor q≤10⁸. For a fixed square offset a² and the parity giving odd p, the m roots are 0 for q|a, ±a√−1 for q≡1 (4) with q∤a, and none otherwise (odd q). Cross these progressions; p in range exceeds every sieving q. The checker consumes every prime row exactly once from its survivors and requires none left. It reimplements the composite-panel population filter by separate factor tests. For every capped hit it reconstructs the defining integer identity; for every reported late R₈ row at 1000 it checks all cheap (u,C) residue shots independently. Hard counts at 2·10⁶ use the ascending discovery scan; positive rescues do not depend on its minimality.
3. `z77_kummer_factors.cpp` directly uses `B(kuC−1)=n+u`, with u≤B by symmetry, hence `ku²−2u≤n`. It factors contiguous blocks of n+u by a prime sieve and tries every divisor in the possible size range, stopping at the first positive witness. Every one of the 4,966 jobs returned a positive, checked by standalone Python with exact integers. **There is no zero claim** and no unresolved capped row.
