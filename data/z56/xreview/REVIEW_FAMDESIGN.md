# FAMDESIGN hostile cross-review

Reviewed `side-agent/z56-famdesign` at `132f0557a56dc1a295050e0f6296eb9f55f3c1ad`.
**Verdict: ACCEPT-WITH-FIXES. Theorem V is CORRECT; the high-end H3 numerical certification is not.**
Independent re-derivation below; no reliance on the internal review's verdict. ES remains OPEN.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| §1 region areas and complete-layer containment | CORRECT | Areas G=5/12, K=1/12, G₁/₁₅=29/90. If Q⁴≤Pp, PQ≤p²/³; 64C³≤p gives PQ=(p+P+Q)/(4C)>p²/³, contradiction. |
| Corollary V1 | CORRECT | Thin rectangles satisfy the inherited C1–C3; area ∫₁/₁₅³/₅(3−5a)/4 da=8/45, hence 64/(45π⁴). |
| Lemma 3.1 / Bu8 | CORRECT | Splitting into four odd residue classes modulo 8 reduces to shifted sums for the primitive odd squarefree conductor; f′=1 is separately bounded. |
| Lemma 3.2 | CORRECT | s(4oe)=4·2^{ω(o)+ω(e′)}, φ(4oe)=2^{k+1}φ(o)φ(e′); counting both orders gives 2^{2−k}. All three 2-adic cases check. |
| Lemma 3.3 | CORRECT | Odd-prime projectors cancel the fixed-variable 2^ω; mod-4/mod-8 projectors contribute 1/2 and 1/4. Principal coefficients Tₒ and 2^{−k}/φ(e′) are correct. |
| Proposition 3.4 | CORRECT | Conductor products, non-principality, convolution, and uniform window errors check; details below. |
| Lemma 3.5 | CORRECT | Bad-prime cancellation gives exactly (1−1/p)/(2o), or (1−1/p)/(2e), times 𝓛. Positivity uses no ineffective lower bound. |
| Proposition 3.6(a,b), Burgess | CORRECT | Square diagonal is 6/π²; nonsquares require α₀>τν. The stated C3 provides slack; the even-variable errors sum geometrically, not as O(K). |
| Proposition 3.6(a,b), HB | CORRECT | Both HB variables are odd squarefree after extracting square factors. The coefficients depend on fixed square factors, not on the HB modulus. Small kernels and large square factors are separately controlled. |
| Theorem V / genus corollary | CORRECT | Rectangle density 3/π²; constants 29/(30π²)=0.097943810854 and 5/(4π²)=0.126651479553. Burgess-only effectivity and fixed-p quantifiers are valid. |
| §3.8 T1 audit | CORRECT | At odd squares the p-factor disappears from the primitive conductor and an available second principal product cancels the first pole. No extension of the prime theorem to squares is asserted. |
| §4.1 exhaustive scanner / decider | CORRECT-WITH-FIX | Enumeration partitions solutions correctly; decision fallback is exhaustive. But the claimed exact H3 membership over the supported range has signed-128 overflow (counterexample below). |
| §4.2–4.3 F4/F4L zero counts | CORRECT in audited portions | Stored unions give 38/317; all 38 F4 zeros rerun. Full absence of additional zeros through 10¹⁰ was not independently rescanned. The overflow does not affect arithmetic in that census range. |
| §3.7′ slice evidence | CORRECT in audited portions | All 46 direct slice sums reproduced at stored precision; 42 ratios within 3%. Stored PARI L-value predictions were not recomputed. |
| §4.2, 10¹⁴ H3 sample | WRONG | 75 false H3 memberships at 53/100 primes; mean hits 42.33 must become 41.58. No corrected H3 zero appears. |
| §4.4–4.5 fits, genus depletion, correlations | Assessment/EVIDENCE labels honest | Not independent proofs of last-zero bounds or uniform genus rigidity. Bulk genus/correlation calculations and fits were not rerun. |
| §5 divisor identities / H3 genus bounds | CORRECT | (4Cu−1)(4CB−1)=4Cp+1 gives the complete divisor layer, with ordered count D⁻, not 2D⁻. Strip areas 5/18 and 7/30 give 5/(6π²) and 7/(10π²). The different level-coordinate genus split is explicitly acknowledged. |
| §6–7 verdict and screens | CORRECT-WITH-FIX | “Strengthened” follows for the genus main term only. B2 remains untouched. Reword the proposed FRONTIER sentence that sounds like an unconditional impossibility result. |

## Theorem V: independent derivation and source audit

1. At an allowed odd prime ℓ the convolution factor is
   hℓ(Y)=1+(1+χ(ℓ))Y/(ℓ−1)+χ(ℓ)[1−(1+χ(ℓ))ℓ/(ℓ−1)]Y².
   Thus hℓ(1/ℓ)=1+χ(ℓ)/ℓ². At excluded primes it is (1−Y)(1−χ(ℓ)Y).
   The absolute h-sum at exponent −3/4 converges with only p^{o(1)} losses at excluded primes.
2. Write o=o₁s², g=(d,o₁), d=gd₂. Then f_F f_G≤16d₂²o₁p≤16op; in the mirror slice it is ≤64e′p.
   The surviving p-factor ensures f_G>1 for every projector. A principal F is handled by the separate principal hyperbola lemma, never by nonprincipal Burgess.
   Conductors 4^j·odd-squarefree are cube-free; conductor 8f′ is **not** cube-free, but Bu8 legitimately reduces it to four f′-sums.
3. I rechecked the inherited L-tail and both hyperbola arguments: the window difference cancels L(1,F)L(1,G), or γL+L′.
   With c≤p^ε, the stated y lower bounds leave positive exponent slack; c>p^ε contributes p^{−ε/4+o(1)}.
   All projector/divisor multiplicities and the final weighted outer sums cost only p^{o(1)}.
4. Euler cancellation gives HₒL(1,χ)/φ(o)=(1−1/p)𝓛/(2o).
   After truncating at N=p^ν, ν=τ(1+α₁)+3ε, square indices n=s² contribute
   (1/2)log(O₁/O₀)·Σ_{s odd}(φ(s)/s)β(s²)/s²
   = (1/2)log(O₁/O₀)·∏_{ℓ odd}(1+ℓ⁻²) = (6/π²)log(O₁/O₀).
   The local sum is 1+(1−ℓ⁻²)Σ_{j≥1}ℓ^{−2j}=1+ℓ⁻², not 1/(1−ℓ⁻²).
   Multiplication by the slice's 1/2 gives **3/π²**, including both orders exactly once.
5. Burgess bounds the nonsquare average by p^{θν−κα₀+o(1)}; α₀>τν suffices.
   With τ→1/4, thin rectangles require α>1/15. The even-variable shifts cost at most ε and are absorbed by fixed margins.
6. For HB, write n=n₁m² and o=o₂t². The t>p^{λ/4} tail is p^{−λ/4} times logarithms.
   For n₁≤p^{λ/8}, periodicity plus the squarefree sieve gives O(τ(2m)n₁√T), hence a saving above T≥p^{λ/2}.
   For larger n₁, Cauchy–Schwarz and HB give p^{o(1)}(N₁^{−1/2}+O′^{−1/2}) per dyadic block.
   Both variables exceed fixed powers of p; m⁻² and t⁻² are summable, and divisor weights fit the available slack. No averaging over p occurs.
7. Tiling with finitely many fixed rectangles precedes p→∞. Compact rectangles crossing the two slice regions can be finitely subdivided using their positive margins.
   Nonnegative weights yield the global lower bound, not a global asymptotic. Letting fixed λ↓0 gives 5/(4π²), and division by 3/(2π²) gives 5/6.

Sources actually inspected: [Burgess restatement and explicit Theorems 1.1–1.2](https://arxiv.org/html/2511.17778v2), including the all-r cube-free condition and removal of the N restriction;
[Heath-Brown 1995 original paper](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf), Theorem 1, printed p.237: exactly the positive odd squarefree quadratic large sieve used here.
No Siegel estimate or unverified effectivity of HB is needed for the Burgess-only effective statement.

## Required fixes, in priority order

1. **Fix H3 overflow in both `z56_famdesign_scan.c` and the full-count fallback of `z56_famdesign_decide.c`.**
   The first unsafe C is 1,385,297,844,440. A sampled counterexample is (p,o,e,C)=(100000000000097,1,6,4166666666671).
   It satisfies p=4oeC−o−e, but 64C³=4629629629644074074074089096296296301504 exceeds signed-128 capacity.
   The compiled classifier nevertheless records H3=1; UBSan diagnoses signed integer overflow. This pair belongs to K, not H3.
   Use the overflow-free positive-integer test `C <= n / 64 / C / C`, or an integer cube-root cutoff with verified bounds.
   Regenerate the 10¹⁴ H3 column and all dependent statistics; retract the blanket “exact integer tests” certification until repaired.
   Auditing all overflow-capable pairs gives 4,233→4,158 sample hits and mean R_H3/log²p **0.08002525**, not the published rounded 0.081.
2. In proposed FRONTIER text, replace “cross terms cannot be averaged unconditionally” with “are not controlled by this argument.” No impossibility or optimality theorem was proved.
3. Minor editorial cleanup: §4.1 first states the HC tie guard as 10⁻⁹, then correctly describes its replacement by 10⁻¹². State the current value consistently.

## Reproduction and limits

Audit script: `scripts/z56_xrev_famdesign_check.py`; branch files exported under `/tmp/xrev_FAMDESIGN`, C engines built with gcc -O2.
Every execution used timeout and memory/CPU limits (`ulimit -v 6000000`; longest audit timeout 300s); peak slice SPF allocation is about 500 MB.
Results: 2,604 direct unit-square/rational-weight comparisons; all 12 scanner columns versus independent pair enumeration at 1,498 odd n≤3000; no mismatches.
The full scanner through 10⁶ visits 39,175 primes and reproduces 758 stored zero rows; the decider agrees on its 361 zero rows in [1000,10⁶].
Stored F4/F4L unions reproduce 38 (last 564661441) / 317 (last 6122428657); rescanning every F4 zero confirms the four above 10⁷ each have one solution in K.
All 46 slice sums agree within 5.6·10⁻⁶ of the displayed values; ratios to stored predictions are 0.909032–1.044870, with 42 within 3% (rounding explains the lower endpoint).
The H3 audit enumerates every potentially overflowing solution in the 100-prime sample using oe≤p/(4C_min−2), then invokes the actual source classifier and UBSan; no large full rescan is needed.
I do not independently certify the absence of unlisted zeros throughout (10⁶,10¹⁰], the bulk higher windows, or the fitted last-zero scales.
**Bottom line:** record Theorem V as a valid unconditional genus result; repair the numerical certification and wording before accepting the memo unchanged. Nothing here proves positivity of R or resolves ES.
