# z58 DISPROOF — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** The negative sampled search and both new R₈-zeros survive independent verification. The elementary lemmas are sound; a T1 application drops their hypothesis. “Narrowed, not a HOT LEAD” is justified as an empirical/model assessment, not an exclusion theorem. ES and (MS) remain open.

Reviewed `side-agent/z58-disproof` at `59c09dc3f655cd7b057dba05cbd76c4ccc1b2a4b`, including `Z58_DISPROOF.md`, the engine, archived runs, cells/fit/tail scripts and all four screens. No reliance on the memo's internal-review verdict. Every command used `ulimit -v 4000000`, timeout ≤1500 s, and at most two concurrent compute processes.

## Per-claim findings

| Claim | Classification | Independent finding |
|---|---|---|
| Lemma 2.1, pair congruences | CORRECT | Solving each congruence gives an integer third coordinate; positivity follows from n≥1. |
| Lemma 2.2, square-class shadow | CORRECT | Fixed-pair lifting to a sufficiently large square is valid for each of the three moduli. The square obstruction is independently derived below. |
| Lemma 2.3, sterile u-line | CORRECT; application needs fix | The stated gcd hypothesis suffices. But “n=m² is the case every u, c=u, t=1” does not satisfy it for u sharing a factor with m. |
| Proposition 2.4(i) | CORRECT | c divides k, and mapping (c,t) to u=ct²−k gives the displayed upper bound; duplicates only help. |
| Proposition 2.4(ii), fixed-offset mass | CORRECT as Assessment | For fixed k the reciprocal sum converges; O_k(L) follows from the assumed line-mass bound, not from the arithmetic lemma alone. |
| §4.2 smooth square exclusion | CORRECT, one-way | For the relevant odd primes p>y≥2, square roots lift at odd prime powers, and p≡1 mod 8 handles powers of 2. Independence of remaining solutions is a separate model assumption. |
| Engine exact/decision modes | CORRECT in recorded range | Exhaustive partition, parity multiplicities and early exits are sound. Both modes match independent enumeration on 375 inputs. No false R/G* zero decision found. |
| 868,562 distinct primes, no R/G* zero | CORRECT-WITH-FIX | Count and positivity verified for every prime; the sample includes 90,589 primes outside 𝔐, and its exact maximum exceeds the literal stated upper endpoint. |
| Two new R₈-zeros | CORRECT | Exhaustive independent counts: 20,840,951,041 → (R,R₈,R_G*)=(24,0,24); 23,296,553,281 → (36,0,32). |
| §5.1 log L_D∼2D/3 | CORRECT | Odd primes 3 mod 4 occur through D, primes 1 mod 4 through D/3; higher powers contribute o(D). The CRT-construction scope is correctly qualified. |
| §6.1 fitted zero law | REPRODUCED EVIDENCE | Cell census matches byte-for-byte; fit and profile likelihood agree. Plug-in means and extrapolation do not establish a universal zero law. |
| §§6.2–6.3 tail, “none reaches 10¹⁷” | ACCEPTABLE Assessment with disclosure fix | Tail output reproduces byte-for-byte. Frozen mean, ×6 factor, non-independent calibration and slow mixtures are honestly disclosed. A second truncation—only 120 nonresidue slices—is not disclosed. |
| §7.3 “fully accounted for” near-square depression | OVERSTATED EVIDENCE | Approximate line weights, neglected overlaps and gcd exceptions cannot establish full attribution or absence of a real-proximity effect. |

## Proof audit and exhaustiveness

For d≡3 mod 4 and positive r dividing (d+1)/4, gcd(r,d)=1 and (r/d)=1: for every odd prime q dividing r, quadratic reciprocity and d≡−1 mod 4q give (q/d)=1; if r is even, d≡7 mod 8 gives (2/d)=1. Thus (−r/d)=−1. Every solution supplies d=4uC−1 and n≡−u mod d with u dividing (d+1)/4. A square n cannot have Jacobi symbol −1. This proves the square obstruction needed in Lemma 2.2 without assuming the cited result.

For Lemma 2.2, when m_i divides M, N=(s+t m_i)² preserves the relevant pair congruence and is positive for large t. Its resulting positive third coordinate contradicts that square obstruction. No coprimality of s and M is needed.

For Lemma 2.3, a putative d=4uC−1 divides m²+ct² and is coprime to c. Any prime dividing both d and t divides m, contradicting gcd(m,t)=1. Hence t is invertible modulo d and −c≡(m/t)² mod d. Since c is a unit modulo d, its Jacobi symbol must be +1, contradicting the preceding −1 calculation with r=c. In fact **gcd(m,t)=1 suffices**; the extra gcd(m,c)=1 is unnecessary. This strengthening repairs the claimed k=0 specialization for every u.

In `full()`, put P=min(u,B), Q=max(u,B). The loops partition all solutions into P≤Q≤C, P≤C<Q, and C<P≤Q, with disjoint boundary conventions. Their monotone stopping inequalities are exactly the necessary size bounds. Odd n forces P+Q odd, so P≠Q and the multiplicity two is correct. `gtest()` uses sufficient integer width in the archived range.

Every positive early flag comes from an actual complete level. Skipping an already-found parity cannot lose an H3 decision: if K<cmax and H3 is still absent, both parity flags are initially absent; if K≥cmax, all H3 levels were already scanned. An unresolved flag triggers full enumeration; a missing H3 flag already reflects exhaustive H3 levels. No timed-out, unfinished prime is emitted as a zero.

H3 really implies G*: if Q⁴≤Pn, then n=4PQC−P−Q<4PQC implies Q³<4P²C≤4Q²C, hence Q<4C and n<64C³, contradicting H3. Thus it is sound not to enumerate G* after an H3 witness.

`divides()` concludes with integer equality; in these runs its operands/products are safely representable and an exactly divisible quotient cannot be lost to double rounding. This is a range-specific audit, not approval of unrestricted `list` inputs.

## Independent numerical verification

The committed `scripts/z58_xrev_disproof_check.py` uses segmented integer factorization of n+u for **every** 1≤u≤floor((1+sqrt(1+4n))/4). It enumerates every divisor d≡−1 mod 4u with B=(n+u)/d≥u, recovering C=(d+1)/(4u). This is independent of the reviewed three-loop/float-division implementation.

- New zeros: u=1…72,182 and 1…76,316 exhausted respectively; 12 and 18 unordered witnesses, all C odd. Independent deterministic 64-bit primality checks pass; H3 counts are 20 and 28.
- All 18 archived files parsed and deduplicated: runA 465,132, runB 99,187, exact union 563,728; runC 305,386; overlap of exact union with runC 552; total **868,562**.
- Every distinct archived input independently passes deterministic primality. Its stored d_min reconstructs r=(−p mod d), C=(d+1)/(4r), B=(p+r)/d. Exact integer checks verify 4rBC−r−B=p and max(r,B)⁴>min(r,B)p **for all 868,562 primes**. Thus the main R/G* positivity result is certified independently of both engine modes, not merely inferred from logged flags.
- Exact sample range: **[10,000,000,033, 7,307,828,669,535,601]**; 777,973 primes in 𝔐 and 90,589 outside it. Distinct R₈-zeros are precisely the two listed above; the shared D1b/D1c zero accounts for the third zero row.
- Engine `EXACT=0` and `EXACT=1` each match all counts/flags applicable to 375 independently enumerated inputs: primes 1 mod 4 through 5000, every prime screen input, and the two new zeros.
- Rebuilt and reran `cells 200000000`: byte-identical to `cells_2e8.txt` (about 624 MB including aggregate storage, below the imposed limit).
- Refit: 5,538,137 primes, 68,554 cells; R₈ a=0.3979, β=1.0137, 1,339 zeros; R a=0.4027, β=0.9720, 10 zeros. Fixed β=.7/.5 costs 223.77/617.00 log-likelihood units. R₈-law predicts 4.08 R-zeros, not 10: the disclosed mismatch remains important.
- Reran `tail.py 20000 4`: byte-identical to `tail.txt`; fitted six-class truncated expectation is 2.627·10⁻²⁴ in [10¹⁷,10³¹). This validates implementation reproducibility, not calibration at 10¹⁷.

## Mandatory falsifiers

| Screen | Independent check and effect on the idea |
|---|---|
| F1 odd squares | Jacobi proof above establishes R=0. The generator genuinely imitates a square obstruction; the probability law is explicitly not a model for squares. Fix the Lemma 2.3 specialization, not Lemma 2.2. |
| F2 C-even / numerator 8 | All 12 supplied zeros exhaustively re-enumerated with matching full R counts; 11/12 are 1 mod 8, 4/12 square mod 840, 6/12 have sd=3. Both new zeros also verified. Mean-only sibling calibration is evidence, not a structural distinction proving R positive. |
| F3 composite zeros | All 285 exhaustively re-enumerated: R=0; 285 are 1 mod 8, 203 square mod 840, 214 divisible by 3. The stated obstruction to a common prime factor of n and m₂/m₃ is correct. No positivity claim is made here. |
| F4 known prime zeros | All 14 R-zeros and all 38 G*-zeros independently verified, not just the four G* examples in the memo. Square-mod-840 counts 9/14 and 20/38 agree. Probability-model and G*-calibration limitations are honestly stated. |

## Required fixes, in priority order

1. **Scope of the headline:** write “868,562 sampled design **and control** primes (777,973 in 𝔐)” rather than claiming the entire total lies in designed progressions in 𝔐. Give the exact upper endpoint or a containing rounded endpoint such as 7.31·10¹⁵; 7.3·10¹⁵ is strictly too small. This is a sampled search, never an interval census.
2. **Model truncation and meaning:** disclose `odd_np[:120]` as well as the 10³¹ cutoff, and call the number a Monte-Carlo/decade-quadrature scenario estimate. The omitted slice supply is 2⁻¹²⁰; using the script's own prime-supply model, its worst-case contribution through 10³¹ is ≤3.294·10⁻⁹ even if all omitted primes are zeros. Thus omission cannot overturn “<1” on this finite interval under that supply assumption, but it is not a demonstrated error below 2.627·10⁻²⁴. Do not present the latter as an upper bound or an infinite tail.
3. **T1 specialization:** strengthen Lemma 2.3 to gcd(m,t)=1 (proof above), or explicitly restrict its k=0 application to gcd(m,u)=1 and leave general T1 to Lemma 2.2. As written, m=3,u=3 already violates the claimed specialization's hypothesis.
4. **Export wording:** replace “fully accounted for” with “rough line-kill estimates are consistent with the measured depressions”; restrict “no real-proximity effect” to “no additional effect established in these controls.” “No tested family reaches 10¹⁷” must remain a finite-interval assessment inside the stated common fitted scenario, not a family-uniform bound. Slow mixtures and other unresolved families remain possible.
5. **Engine reuse, lower priority:** centralize the range guard in `process()` so `list` cannot bypass it. Correct the primality comment: the 3.3·10²⁴ bound is not the bound for these twelve bases through 37. Neither issue affects the independently certified archived inputs.

Reproduction: extract the reviewed branch into `/tmp/xrev_DISPROOF`; run the checker modes `enumerate`, `archive /tmp/xrev_DISPROOF`, `screens /tmp/xrev_DISPROOF`, and `engine /tmp/xrev_DISPROOF /tmp/xrev_DISPROOF/engine` with `uv run python`, memory limit and timeout. Compile the reviewed engine/cells with `gcc -O2 ... -lm`; fit with `uv run --with numpy --with scipy` (BLAS threads=1), tail with `uv run --with sympy`. No six-process batch launcher was used.

**Bottom line:** no disproof found and no engine failure undermines the search. Accept the certified computations and elementary results after the stated fixes; retain the model only as labelled, non-exclusionary Assessment.
