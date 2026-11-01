# HCHYP cross-model hostile review

Reviewed `side-agent/z53-hchyp` at `09f10071aaebc66c10efe0433d9b83a561f5a079`.
**Verdict: ACCEPT-WITH-FIXES.** The main model theorem, fixed-window theorem, and quadratic counting lemma survive.
The lane verdict **NARROWED** follows, but only with the model/arithmetic distinction and the fixes below. ES remains open.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| §1 line dictionary; HC and ES₅ equivalences | CORRECT | E: A=tx−1 and v=(p+x)/A; L: d=xu−1, with complementary divisor also −1 mod x. These recover positive words and the cited coordinate criterion. |
| M1 | CORRECT | Distinct nonempty subset products are pairwise independent by exposing a coordinate in their symmetric difference. With t=(2^k−1)/n, EZ²≤t+t² gives P(Z>0)≥t/(1+t); k=0 is separate. |
| M2(i),(ii) | CORRECT | Exponential tilting gives E[2^k 1(k≤t)]=e^λ P(Poi(2λ)≤t). The identity 1−2Q(a/2)−a log 2=−Q(a) and the upper-tail estimate give both stated bounds, including the −1 term. |
| M(a) | CORRECT | Small coordinates cost ≤2Yλ in −log failure; the remaining dyadic sum costs L^{θ−Q(θ/log 2)+o(1)}, L=log p. Both exponents are <1 after choosing η. Failure probability ≥1/p and independence across primes give infinitely many failures by Borel–Cantelli. |
| M(b) | CORRECT | Endpoint success ≥L/(5x) above Y=L^{2 log 2+2δ}; sum over C contributes (3/8)log(X/Y)+O(1). The exponent is −(3/40)(A−2 log 2−2δ)L log L+O(L), summable over primes. |
| M3 | CORRECT | Positive-measure H cannot be contained in null S_θ. HC≪log p lies in S_θ for any fixed 1<θ<2 log 2. This is not an arithmetic non-implication theorem. |
| M4 theorem | CORRECT | Planting empty sequences at one prime in each sufficiently large dyadic block forces infinitely many failures; the coupling preserves any genuinely block-robust H. |
| M4 “Which averaged statements”; H_Kub | CORRECT-WITH-FIX | The claimed slack ≥1 criterion is false for sliding intervals (y,2y], which can meet two fixed dyadic blocks. Moreover, almost-sure slack is not invariance of every member of H. See fix 1. |
| K | CORRECT | The stabilizer H lies inside the divisor-residue set and excludes −1. In G/H the final product, hence every partial product, is aperiodic. Iterated Kneser gives 1+#outside≤|Σ/H|≤[G:H]−1. |
| U | CORRECT, with cited input | Checked Henriot's original definitions and 2014 erratum directly; details below. Index 2 gives precisely 1/2; higher indices give a strict extra saving that absorbs fixed powers of log log y. |
| Proposition 5.1 | CORRECT | For fixed events E_p, a nonnegative count bounded by B(y)→0 vanishes eventually, in both directions. |
| LT is “literally S_A” | CORRECT-WITH-FIX | LT uses (log x)^A for all p∈(x,2x], so its event depends on the block endpoint. Proposition 5.1 does not identify this statement with the stated unit-constant S_A. See fix 2. |
| §5.3 first-draft counterexample | CORRECT | 5 divides every F_j(p)=5jp, so every event fails; there is no odd quadratic character of conductor dividing 5. Its unconditioned model mass nevertheless grows quadratically in log x. |
| §5.3 alignment and character classification | CORRECT | Outside 2·lead(G)·Δ, a prime divides some G(m) iff Δ is a quadratic residue. On modulus lcm(q,cond χ_Δ), Dirichlet forces ψ to be trivial on ker χ_Δ, hence principal or induced by χ_Δ. Exceptional primes must remain excluded. |
| Proposition 5.5 | CORRECT, CONDITIONAL as labelled | Prime m²+1 has m even, so am²+1 is odd and coprime to a. Every prime divisor has χ_{−a}=1, whereas χ_{−a}(−1)=−1 and its conductor divides a. The assumed HL-F lower bound contradicts the proposed exponential-mass bound. |
| N, including small-height aligned mass | CORRECT | Endpoint squarefree kernel divides D; for levels, that of 4α−xD divides rad(4α). Counting square parameters gives the displayed bounds. Summing reciprocal quadratic sequences above Y yields the stated mass bounds; for height L^{0.1}, the larger exponent is 1.1−(log 2)/2<0.76. |
| Remark M / Remark U interpretations | CORRECT-WITH-FIX | Model thresholds and surrogate numbers are useful, but convergence of finite-difference slopes and the precise growing-modulus failure law are not established by M. See fixes 3–4. |
| §6 CERTIFIED / EVIDENCE | AGREEMENT | Full square and one full prime sample rerun; all HC/X* and selected Z-tail summaries independently recomputed; details below. These do not test the proposed deep tail. |

## Decisive citation: Theorem U

Primary sources inspected: [Henriot 2012, §2 and Theorem 5](https://arxiv.org/pdf/1102.1643) and
[2014 erratum, pp. 375–377, New Theorem 5](https://doi.org/10.1017/S0305004114000280).
The erratum requires primitive Q_i and F∈M_k(A,B,ε); its upper bound does **not** require F bounded below.
Here F=1[P⁻(Q₀)>√M]∏s_i^{ω_{H_i}(Q_i)} is multiplicative, bounded by 1, and belongs uniformly to M_{k+1}(1,1,ε), even at s_i=0.
The displayed normalized forms are primitive and pairwise non-proportional; their product may have fixed prime divisors, which New Theorem 5 permits.
At good primes ℓ≤√M, its avoidance factor and divisor sum give 1−[1+Σ_i(1−f_i(ℓ))]/ℓ+O_X(ℓ⁻²).
Above √M the extra reciprocal-prime sum is O(1); leading-coefficient/resultant primes cost O_X(1), including the corrected erratum factors.
Mertens in fixed progressions gives density 1−1/r_i. Taking s_i=0 for r_i=2 and 1/log log y otherwise gives U after finitely many subgroup choices and dyadic summation.
No uniformity in X, lower-bound sieve, or arithmetic obstruction to such uniformity is proved.

## Numerical reproduction

All shell runs used `ulimit -v 6000000`, a CPU limit, and explicit `timeout`; no large Cartesian-product allocations.
Extracted the reviewed scripts/data to `/tmp/xrev_HCHYP`; compiled its C program with `gcc -O2 -Wall -Wextra` (style/unused-variable warnings only).
- Full `sq 10001 5000 2048`: both output files byte-identical to stored data; **0 successes in 7,680,000 tests**.
- Full `stat 100000000 20000 2048`: both output files byte-identical; **30,720,000 line tests**.
- Independently enumerated actual divisors for all 1,056 C control bits at x≤128; no mismatches. HC values: **7,4,4,15,7,7,7,64,8,39,8**, in the memo's order.
- Independent aggregation of all ten stored samples verifies HC maxima, censoring, HC tails, cumulative failures, X*, and consistency of Z sums with per-coordinate counts.
- Five prime X* values: **63,79,95,111,124**; X*/log(mean p): **3.4187,3.4309,3.4382,3.4433,3.4516**.
- At X=2048, prime variance/mean at 10⁸,10¹²,4·10¹⁵: **2.1846,1.5580,1.3020**; minima **22,49,68**. Deep-tail non-observation is correctly labelled uninformative.
- Near m²+24: conductor computation gives **55 aligned / 40 zero-success E-lines**, **27 / 12 L-lines**; every observed zero-success line is aligned, not conversely.
- Poisson-tilting formula plus an independent 65,536-entry totient sieve reproduces all sixteen U and U/2 surrogate X* values; endpoint ratios **2.55435→4.33250**, **7.39130→17.81938**.
- Original cyclic Monte Carlo rerun reproduces **0.118,0.332,0.687,1.093,1.418** at the five quoted coordinates and log p=27.63; this remains a surrogate, not the unit-group model.
- The independence ratios reproduce the table **using P(E_x∨L_x)**, not treating the two lines at each x independently; explicitly define P_x this way in the memo.

Independent reproduction script: `scripts/z53_xrev_hchyp_check.py` (argument `/tmp/xrev_HCHYP`; requires the C control output `hc_controls.txt`).
Stored-data aggregation is not an independent re-factorization of the other eight samples; the older full ≤10⁸ census was not rerun.

## Required fixes, in priority order

1. **Repair the M4 application, not its theorem.** A sliding interval can contain two newly planted failures, one on either side of a dyadic boundary. An original count 0 with B=1 has slack 1 yet can become 2 infinitely often. Use a proven stability statement (typically an asymptotic error scale ≫1), or an almost-sure coupling argument with sufficient sliding-window slack; do not call almost-sure slack invariance of H. Narrow H_Kub accordingly: actual standard conjectures have not been encoded as such H.
2. **Fix LT's quantifiers and range.** Specify c>0 and A>2 log 2 so its bound tends to zero. For literal equivalence to S_A, define failure using HC(p)>(log p)^A inside the count. As written, evaluating x=p/2 forces HC(p)≤(log(p/2))^A eventually, which is stronger than S_A. This is a real logical distinction: abstract HC values chosen as the largest element of C below (log p)^A satisfy S_A but violate the stronger bound for A>1. The current LT still suffices for S_A; only the asserted equivalence fails.
3. **Keep model incompatibility separate from arithmetic impossibility.** Rename “why the Landau saving cannot be uniform” to say “would be model-null”; M3 cannot rule out an arithmetic uniform estimate. In Remark U, Q(a)<1/2 means a is **above** approximately 0.187, not below. The ω-deficit yields a failure lower bound; domination/equivalence and a precise transition at L^{0.13} need an additional matching argument or explicitly heuristic wording, also in §5.1.
4. **Weaken the surrogate slope assertion.** The estimates behind M bound the mass-crossing scale between L^{2 log 2−ε} and L^{2 log 2+ε}; they do not alone imply convergence of the displayed finite-difference slopes. State the logarithmic exponent limit, or supply further regularity/asymptotic analysis. Define the paired-coordinate independence benchmark as noted above.

## Final assessment

Accept the scoped theorems after these fixes; do not promote the hypothesis catalogue into a non-implication theorem for GRH/EH/Chowla/HL.
The CONDITIONAL label on Proposition 5.5 and the absence of a counterexample-free GLT are honest. The finite controls support calibration, not a far-tail theorem.
**NARROWED** is justified: no standard-conjecture route to ES emerges, while M, U, and N provide genuine, explicitly limited information.
