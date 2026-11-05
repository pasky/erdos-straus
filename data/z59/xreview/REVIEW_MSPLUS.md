# z59 cross-model hostile review — MSPLUS

Reviewed `side-agent/z59-msplus` at `5e4c3c100f4f376a6b955c7f7a3a1aabb8708cbc`.
**Verdict: ACCEPT-WITH-FIXES.** The leading-mean theorem, half-mean theorem and census survive; the second-order expansion does not. Do not copy the proposed FRONTIER text unchanged. ES, (MS) and the primality-free targets remain OPEN.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| Lemma 2.0, dead d-moduli | CORRECT | A common divisor of d,n divides r and d+1, hence is 1; exactly-one-divisible u,B pairs cannot hit. This concerns d-form moduli, not arbitrary pair moduli 4uB. |
| Theorem 1 | CORRECT | CRT, pair-count error, weighted hyperbola sum and normalization all check; proof details below. Fixed Q is essential. |
| Corollary 1.1 | CORRECT with scope clarification | Same leading coefficient for unit residue classes, not for the subset of square inputs or prime inputs. The dead-factor lower bound is a bound on constants, not a uniform class-mean theorem. |
| Remark 2.1 | CERTIFIED agreement | Independently enumerated every residue for 3^e, e≤4; 5^e, e≤3; 7^e,11^e, e≤2. |
| Remark 2.3, R₈ | CORRECT | Odd local factors unchanged, 2-part expectation 1, normalization changes from 1/4 to 1/8; leading coefficient halves. |
| Proposition 2.2 | WRONG as an expansion of the class mean | Already Q=4 has a different linear coefficient. The committed numbers remain usable as a heuristic covariate, not the asserted asymptotic expansion. |
| Lemma 4.1, twisted T1 | CORRECT-WITH-FIX | Density-zero conclusion is sound. Replace “By Dirichlet, relative density 1/4” with PNT in arithmetic progressions, or use only reciprocal-prime divergence. |
| Lemma 5.1, scaling | CORRECT | Division by b gives the stated bijection; the inverse multiplies u,B by b and divides C by b. |
| k(n)=3 exclusion | CORRECT | n≡2 mod 3 has witness (u,B,C)=(1,(n+1)/3,1). |
| §6, census to 10¹² | CERTIFIED agreement, one full-range engine | All 18 chunks reconcile; independent slice and worst-input check pass. No independent full-range rerun claimed. |
| (MS⁺₁₀₅), (R⁺₄₇), certified ranges | CORRECT | Thresholds/counts agree with the z58 zero file; the adjacent claim for every y<7 is false. |
| Zero law / OOS | EVIDENCE, not theorem | Fits and Poisson tails reproduce. No pre-set pass criterion; explicitly not a passed test. Broad “within 1.5×” and finite-tail language still need scoping. |
| §5.2 roughness argument | CORRECT-WITH-FIX | Fixed-y roughness does not imply gcd(n,u)=1 for arbitrary u; the claimed transfer needs explicit bounds on the primality assumptions used. |
| Headline narrowed / strengthened target choice | ACCEPT-WITH-FIXES | Reasonable assessment, not a new positivity mechanism; no HOT LEAD or ES claim is justified or made. |

## Independent proof audit

For Theorem 1, restrict to 4uB−u−B≤X; since u+B≤uB+1, necessarily uB≤(X+1)/3, giving O(X log X) pairs. CRT gives spacing 4uBQ/g and compatibility a≡−u−B mod g. The O(1) error per pair becomes O_Q(log X) after division by the class population X/Q+O(1).
With f=[compatible]g/4, the remaining normalized main sum is Σ f(u,B)/(uB) times (X−4uB+u+B)⁺/X. Replacing this cutoff by 1_{uB≤X/4} costs O_Q(log X): inside, sum the 4uB/X loss; outside, the multiplicative-width annulus has harmonic mass O(log X). Periodicity then gives (mean(f)/2)log²X+O_Q(log X).
For an odd q, the three contributions (neither/exactly one/both divisible) are (1−1/q)², (2/q)[q∤a], [q|a]/q. Hence σ_q=1+1/q² or 1−1/q+1/q², and their ratio is exactly (q²−q+1)/(q²+1).
At 2, only opposite-parity pairs contribute. Conditional on the even coordinate and m=min(k,2+v₂(uB)), the odd coordinate hits the required odd residue with probability 2^(1−m); weighted expectation is (1/2)2^m 2^(1−m)=1. Thus mean(f)=𝔖/4. For R₈ replace 2+v₂ by 3+v₂ and divide by 8, proving 𝔖/16. Exact enumeration agrees through 2⁶ for both counts.
For Corollary 1.1(iii), each dead factor increases with q, so the worst product uses the smallest odd primes. Mertens gives ≫1/log y; their primorial divides a number ≤n, giving y=O(log n). This justifies the stated constant bound, not uniformity of the theorem in Q.
For Lemma 4.1, s=s₀t² has odd squarefree s₀>1, s₀≡1 mod 4. The nonprincipal characters χ₋₄ and (·/s₀) have coprime conductors and are independent. The specified primes occupy one quarter of the reduced classes modulo 4s₀ (apart from finitely many excluded primes). Each has two roots of sm²≡−1; (1,(sm²+1)/ℓ,(ℓ+1)/4) is a positive witness. CRT gives an upper density bounded by ∏(1−2/ℓ), tending to zero by divergence of Σ1/ℓ in these prime progressions. Thin infinite zero subfamilies are not excluded.

## Substantive new issue: the second-order coefficient

Theorem 1 leaves an O(log X) error; Proposition 2.2 cannot discard it when identifying c₁. A direct countercheck is Q=4, a=1. Write L=log(X/4) and γ for Euler's constant. The actual cumulative class mean is

`L²/8 + ((3γ−1)/4)L + O(1)`, whereas the memo's formula gives `L²/8 + (γ/2)L + c₀ + o(1)`.

To derive this, first replace 4uBC−u−B≤X by 4uBC≤X, retaining u+B≡3 mod 4. This changes the total by O(X): order u≤B, sum the B-interval length O(X/(u²C²)+1) over C≤(X+2u)/(4u²), and double. Both sums are O(X).
The pair Dirichlet series is `F(s)=h(s)ζ(s)²+j(s)ζ(s)β(s)`, where `h=2^(−s)−4^(−s)`, `j=2^(−s)−2·4^(−s)`, and β is the Dirichlet beta function. Here h(1)=1/4, h′(1)=0, j(1)=0. Multiplication by ζ(s) for C and summation give the displayed linear coefficient (equivalently apply the elementary ternary-divisor asymptotic to the shifted arguments). The shift error changes only O(1) in the mean.
Numerical check from the exact census, X=10⁶,10⁷,10⁸,10⁹: residuals after the corrected quadratic+linear terms are 0.66935, 0.66913, 0.66899, 0.66897. With the memo's linear term they are −0.64437, −0.88797, −1.13148, −1.37487. This is not merely an unproved remainder.
**Fix:** withdraw the asserted class-mean expansion and call the existing m(n) a reciprocal-progression mean proxy; retain its fitted predictions only as EVIDENCE. Alternatively derive the genuine second-order terms and recompute the model. Leading Jacobi-blindness remains proved, but “Mordell acts only through c₁L” is not proved by Theorem 1.

## Computation and exhaustiveness

Reproduction: archive the reviewed branch to `/tmp/xrev_MSPLUS`; run `scripts/z59_xrev_msplus_audit.py /tmp/xrev_MSPLUS MODE` with MODE=`summary`, `zeros`, `slice`, `fit`, `extras`, using `uv run --with sympy --with numpy --with scipy python`. Every run used `ulimit -v 4000000`, timeout≤1800, single-threaded BLAS, and at most two compute processes. The script streams large files and never allocates a census-sized array.
The independent engine does not reuse the LADDER scan: order u≤B and use n+1≥(K−1)uBC, so min(u,C)≤⌊((n+1)/(K−1))^(1/3)⌋. Split into u≤C (factor n+u) and C<u (factor KCn+1=(KCu−1)(KCB−1)). Exact divisor enumeration counts every witness once up to u↔B. K=4 gives R, K=8 gives R₈. It agrees with direct u,B enumeration on all 499 n≡1 mod 4 in [5,1999].
The original engine is exhaustive: any witness supplies moduli 4uC−1,4BC−1,4uB with minimum cubed ≤64(n+1)²/9. The d-form remainder is u<4uC−1 and the pair-form branch enumerates every divisor of m/4. Positive-witness reconstruction, inclusive integer cap correction, square exclusion, residue loops and 128-bit arithmetic are sound at 10¹². Allocation/divisor overflow would give a nonzero exit, not a silent zero.
All 18 status files have exit=0 and matching inclusive endpoints, without gaps or overlaps. Every chunk's two category counts equal exact residue-class counts minus squares; there are no Z lines. Totals: 1,046,544,177 P + 5,381,870,962 C = 6,428,415,139. Exact raw population is **6,428,571,430**, minus 156,291 squares; the memo's unrounded `6·9·10¹¹/840` equality is not literally correct.
Independent slice [475715100001,475715940000]: **966 P + 5034 C**, every input has a verified witness; original-engine rerun agrees. At the global maximum input 475715523361, the independent complete factorization count gives **R=12, least modulus=1,470,759**, agreeing with the log. This validates the reported extremal input, not an independent global maximum search.
The z58 zero file has 50,499 entries: 49,999 squares and **500 non-squares = 14 P + 486 C**. Recomputed target rows: MS 9/8,813,281; MS⁺ 27/17,401,609; MS⁺₁₀₅ 38/29,210,401; rough11 30/17,401,609; rough43 21/17,401,609; rough47 19/8,813,281 (count/last zero). All four distinct endpoint zeros (8,813,281; 17,401,609; 29,210,401; 9,919,520,121) also independently give R=0. The principal targets are certified to the advertised endpoints, conditional on the underlying census completeness.
All **18 OOS zeros** independently have R=0 and are composite: g105/g15/g21/g3 = **9/4/4/1**. All 12 R₈ screen rows independently reproduce both their positive R and zero R₈ counts. All 460,000 structured-search lines verify, with six square UNK controls and maximum reported witness modulus 211,403; distinct counts match. Twist distribution 668/49/4/2 and q²-overlaps 1/1/0/2/0 reproduce, as do all six closure-example R values.
Fit-cell zero counts agree with the independent z58 list by group/decade. Refits recover κ_A=0.351408, β_A=−0.461247, κ_B=0.288082, β_B=−0.854192 and 261 training zeros. A separate Newton score solve agrees with the pooled fit (score residual <3·10⁻¹²). Poisson upper tails: 18 vs 13 →0.10954; 18 vs 11.53 →0.04668; 4 vs 1.32 →0.04512; 42 vs 28.2 →0.00894. These are plug-in model diagnostics, not theorem probabilities or calibrated parameter-uncertainty intervals.
Commit 85a4fa37 contains all five prediction rows before the OOS result commits. This verifies committed ordering, not that no result had been inspected privately. The absence of a pre-registered pass criterion is now honestly stated. I refitted coefficients and checked reported predictions against artifacts, but did not independently regenerate the full Monte Carlo tail integration.

## Mandatory falsifier table audit

| Screen | Result / required clarification |
|---|---|
| F1 squares | Correct obstruction and explicit non-square domain. Say “same Q=840 leading residue-class coefficient/proxy,” not an actual square-subpopulation mean; primes ≥11 dividing a square alter finer-Q constants. |
| F2 C-even | All 12 rows verify; exactly four are in 𝔐. Identical odd dead factors do not transfer the zero law to R₈. The ≈5× rate comparison remains a rough model assessment, not a calibrated test. |
| F3 285 composites | The table's “sit in” four groups is not literally true: g3/g15/g21/g105 contain 91/51/41/31 =214; g5/g7/g35 contain 26/15/10; **20 are coprime to 105 (15 in 𝔐)**. Replace with “predominantly.” Dead factors explain a correlation, not every zero. |
| F4 14 star / 38 G* | The memo never explicitly disposes of G*. All 14 star zeros are in the 38; the remaining **24 have R>0**, independently witnessed. They obstruct the restricted G* family, not these R-targets. Add this distinction instead of implying the R-zero model models all 38. |

## Required fixes, priority order

1. **Major:** withdraw/correct Proposition 2.2 as above; separate the empirical proxy from a proved local-mean expansion throughout §2, §7 and proposed FRONTIER text.
2. **Logical scope:** §5.2 must not identify fixed-y roughness with gcd(n,u)=1 for all witnesses. Counterexample above the proposed threshold: n=9,553,913=1093·8741 is 47-rough and has witness (1093,2186,1), with gcd(n,u)=1093. A proof transfer is valid only if every primality use follows from non-squareness and the explicitly specified fixed-y exclusion; a requirement y(n)→∞ is not (R⁺₄₇).
3. **Screens and numerical statement:** make F3/F4 explicit as above. Correct §1 “for y<7 zeros continue to 9.9·10⁹”: for **3≤y<7 the last zero is 7,479,950,569**, not 9,919,520,121; the latter is divisible by 3. The main y≥47 conjecture is unaffected. Use the exact integer raw census count.
4. **Statistical scope:** “within ≈1.5×” applies approximately to the four large *training* groups (worst listed ratio ≈1.63), not all later rows; OOS g21 is 3.03×, and held-out g7 is ≈17×. Do not compress this into “composite zeros are quantitatively a dead-moduli phenomenon.” Keep m, log n and Jacobi depth as separate empirical covariates.
5. **Labels:** in the bottom line, change “tail is long but finite” to “the extrapolated model predicts a finite tail”; negligible expected tail is not exhaustion. The summability implication is valid under the stated uniform exponential-model assumption, not a proof about deterministic zeros. Cite PNT-AP or reciprocal-prime divergence in Lemma 4.1. Remove any unqualified claim that all second-order Mordell dependence is established.

After these fixes the defensible result is: exact leading local factors and R₈ half-mean, density-zero twisted obstructions, a one-engine MS⁺ census through 10¹² with independent spot checks, and useful but imperfect empirical target selection. No pointwise positivity mechanism, general prime-reduction impossibility, or resolution of ES follows.
