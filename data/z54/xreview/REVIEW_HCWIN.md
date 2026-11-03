# HCWIN cross-model hostile review

Reviewed `side-agent/z54-hcwin` at `d86fe09abab2408fb88f8923aaa4c13ab80c0163`.
**Verdict: ACCEPT-WITH-FIXES.** The main numbered results survive independent derivation.
The advertised NARROWED verdict, with a conditional strengthening, follows; ES remains OPEN.
There are presentation/quantifier fixes, not a new arithmetic mechanism or a refutation of Lot.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Lemma 1.1(a–c) | CORRECT | A class certificate belongs to the negative square coset. Unit groups have exponent at most two exactly for divisors of 24; the allowed x give the listed four values. For squarefree N the subset map onto W has fibres of size 2^ω/|W|, giving the asserted inequality only on live lines. |
| Lemma 1.1(d), including unit-divisor extension | CORRECT | For every odd prime ℓ dividing either square-control line and coprime to x, −x is a nonzero square modulo ℓ (use m or m⁻¹). The character χ₋ₓ is therefore +1 on ℓ. If ℓ=2, x≡7 (8) makes χ₋ₓ(2)=1. The odd character is −1 on −G². Removing nonunit factors also handles gcd(m,x)>1. |
| Lemma 1.2 | CORRECT | Both integers are divisible by 8. Removing powers of 2 from a live divisor leaves dₒ; the four divisors 2ʲdₒ, 0≤j≤3, cover dₒ⟨2⟩, which contains the negative square coset for x=7,15. |
| Local Lemma A1 | CORRECT | For odd q coprime to p each of the three classes modulo 8 intersects one solution class modulo q; CRT and endpoint errors give the stated uniform count. |
| Theorem A1, ω version | CORRECT | Expansion gives |𝒳|μ plus errors O(π(z)²+μπ(z)); z²≤X absorbs those errors. Chebyshev gives O(|𝒳|/t²) exceptions, not a density-one fixed-standard-deviation bound. |
| A1 additive parenthesis; §0 reading | CORRECT-WITH-FIX | Explicitly restrict the parenthesis to strongly additive sums over the indicated primes. For unrestricted additive functions prime-power terms invalidate its RHS. Replace the summary's fixed O(√log log X) “almost all” claim as detailed below. |
| Theorem A2 | CORRECT | There are at most x/2 allowed small odd divisors, so truncation preserves 2aₓ/x. Interchanging sums gives a progression of step 4d starting below 6d. Integrating 1/x and then summing odd d gives (1/2)(1/4)log²X+O(log X). No primality is used. |
| Theorem B(i) | CORRECT | With the verified H bound, min(1,u)≤uˢ and Σ(x/φ(x))φ(x)⁻ˢ≪X¹⁻ˢ(log log X)²/(1−s). Choosing s=log₂κ gives κ−1+κ log 2−κ log κ. This is only an upper bound; the small-θ trivial bound and undecided boundary are correctly separated. |
| Theorem B(ii) | CORRECT | Odd d≤√T/logᴮT, (d,x)=1, combine with p≡1 (8) into a reduced class modulo 8d. BV is uniform in that class and x. Divisor pairing gives a mean ≫(φ(x)/x)log T. The (1+η)-moment removes the truncated tail: its relative exponent is 2(2^η−1)−ηθ₀<0. Dividing by φ(x) and summing 1/x over Y<x≤X, 4∣x, gives log T log log T. |
| Theorem C(a) | CORRECT (model only) | The second moment of n/φ(n) gives N(t)=O(t); hence Σqᵢ=O(log p/K). For qᵢ≤1/2 the failure product is ≥exp(−2Σqᵢ). There are O((log p)^0.7) remaining lines, each failing with probability ≥P(k=0)=1/log p. For each fixed deterministic K(p)→∞ this yields p⁻ᵒ⁽¹⁾; independence across primes gives infinitely many no-big-line events. |
| Theorem C(b), conjunction | CORRECT (model only) | Fix x=4q and k₀. All k₀ generators in ker χ₋₄ force a K-big failure with probability ≍λᵏ⁰/log p. Its prime sum diverges; independent primes give infinitely many failures. This excludes the specified universal per-line conjunction, not all per-line or adaptive arguments. |
| Proposition M′ | CORRECT (model only) | M1 follows from pairwise independent nonempty subset products and the second-moment inequality. Summing x≥2ᵏ and tilting 2ᵏ·Poi(λ) to e^λ·Poi(2λ) leaves a positive-part deficit of order √λ. The k≥3 restriction removes the small-endpoint issue. Thus S≫log p√λ and the miss probabilities are summable. |
| Proposition L(a) | CORRECT (model only) | Conditional on genus images, nonempty target-fibre products are uniform in the target coset and pairwise independent (including nested subsets). The empty product is excluded because −1∉G². At the data-determined first crossing, conditional independence between lines gives p⁻ᶜᐟ²; for Λ use the 1/4 bound and subtract O(log X)=o(log p) from k=0 lines. C>2 or C>4 ensures summability without a union over windows. |
| Proposition L(b) | CORRECT (model only) | A union bound over nonzero genus characters costs ≤2ʳ2⁻ᵏ per line. Multiplying by its Λ mass gives total loss O(Σ2^ω(x)/φ(x))=O((log X)²). M′ supplies mean ≫log p√λ at the boundary; independent bounded summands concentrate with summable error. Below it, Rankin bounds EΛ=o(log p), conditional Jensen gives EΓ≤EΛ, and Markov plus independent primes gives infinitely many failures. |
| Theorem S | CORRECT | Substitute the polylogarithmic window into the matching mass version of Lot, with the stated cap. Only sufficiency is proved. |
| Theorem D | CORRECT, CONDITIONAL | A2 at log X=√(8C log p)+8c₀ reaches C log p; for large p this lies below the specified exp(3√(C log p)) cap and below p. Applying Lot yields the claimed subpower bound, not an unconditional HC estimate. |
| §3.3 literature / scope | CORRECT-WITH-FIX in §9 wording | The cited Li–Yang Δ estimate and Ivić–Zhai mean-square formula are accurate. Their consequences are sufficient ranges, not necessary window sizes. Pointwise inaccessibility and “no known approach” remain assessments, not theorems. |

## Decisive source checks

Read Henriot's actual [arXiv text](https://arxiv.org/pdf/1102.1643), Theorems 5 and 7, and the complete
[2014 erratum](https://doi.org/10.1017/S0305004114000280), pp. 375–377.
The constants are uniform in the polynomial coefficients subject to the displayed norm condition, satisfied by polylogarithmic a.
For Q=aX+1, primes dividing a have no roots; the erratum's a*D* correction introduces no bad Euler factor.
At other primes the linear local factor is 1+(2ˢ−1)/ℓ+Oₛ(ℓ⁻²). Removing primes dividing a can only reduce this bound for s≥0.
For Q=X+a the extra Q(0)/φ(Q(0)) factor is precisely a/φ(a). Thus both specializations used in B are justified.
The erratum's congruence correction is harmless for a single irreducible linear factor; no erroneous lower-bound theorem is being used.
Also read [Li–Yang Theorem 1.2](https://arxiv.org/pdf/2308.14859) and
[Ivić–Zhai Theorem B and (2.3)](https://arxiv.org/pdf/1209.0872).
The latter gives exceptional measure O(T(log T/U+log²T/U²)) at fixed relative tolerance; the memo correctly requires extra savings for primes.

## Numerical audit

All shell executions used timeout and ulimit; the C build also succeeded under `ulimit -v 6000000`.
The scripts inspect one integer/row at a time; the joint recalculation does not load millions of rows into an array.

| Check actually executed | Result |
|---|---|
| Rebuild C program; regenerate all 5,000 square controls, x≤1024 | `.lines` byte-identical; all 3,840,000 lines genus-dead, no successes. Entire per-integer file matches committed gzip. Mean Λ/log n=5.2001296286. |
| Regenerate all 50,000 primes from 10⁹, x≤1024 | `.lines` byte-identical; first 5,000 records identical to committed gzip. Mean Λ(1024)/log p=5.8485651747. |
| Regenerate all 166 hard primes | Entire `hard.txt` byte-identical. |
| Independent SymPy divisors and explicit unit-square residue sets, all 166 hard primes, all lines x≤64 | Every HC, pre-HC Λ/Γ/S, and Γ(16) agrees within the saved rounding. Of 145 with HC≥20, exactly 95 have Γ(16)=0. No shared genus DP or character implementation. |
| Eleven named HC controls, independently enumerated | 7,4,4,15,7,7,7,64,8,39,8, in the memo's order. |
| Independent 21841 calculation | HC=64; pre-HC Λ=29.0300505051, Γ=10.2272727273, S=9.7040843215; Γ/log p=1.0235928007. |
| Independently pool the committed bins at all four prime heights, 64≤x<1024 | Largest endpoint discrepancy is 2.371 points; largest level discrepancy is **3.878 points**, at 10⁹ and log₂m-bin 1.5 (13,921 lines). The “about 3 points” blanket claim misses this unprinted bin. |
| Regenerate 2.5 million-prime joint scan from 10¹²; independently stream its analysis | All displayed counts agree: failures at X=8,12,16,20,24,28 are 1804,535,58,14,1,0; genus-dead counts 1804,535,33,7,0,0. At X=16 class obs/pred=25/27.228216 or 25/17.038801. At X=24 it is 1/0.861520 or 1/0.241197. |

The scan hit its 600-second limit after 2,319,606 complete rows; one incomplete final row was explicitly skipped.
Continuation started at 1000256305585 for 180,394 primes; exactly 2,500,000 increasing records were analyzed, ending at 1000276237817.
I did not regenerate the four-million-prime 10⁹ scan or all high-height 1024-line samples; their aggregate files are not an independent certification here.
Reproduction helpers: `scripts/z54_xrev_hcwin_check.py` and `scripts/z54_xrev_hcwin_joint.py` (usage in docstrings).

## Required fixes, in priority order

1. **A1 scope and summary quantifier.** Specify F(n)=Σ_{ℓ≤z, ℓ∣n}f(ℓ) and its corresponding centering in the parenthesis.
   For a general additive function supported at prime 3, f(3)=0, f(3²)=1, all other prime-power values zero,
   p=41, X=16, z=4 gives F(p+4)=F(45)=1 but the claimed prime-only variance RHS is zero.
   In §0 replace “O(√log log X) for almost all” with “outside O(|𝒳|/t²) exceptions, deviation ≤t√(1+log log X)”.
   Density one follows by allowing t→∞; a fixed number of standard deviations does not follow from Chebyshev.
2. **Per-line numerical precision.** Replace the blanket ≈3-point claim in §§0,7.3,9 by “within about four percentage points in these pooled bins”.
   The 3.878-point omitted level bin is real, reproduced from byte-identical regenerated data, not rounding noise.
3. **Joint summary range.** §0's 0.3–0.9 and 0.7–1.7 ranges describe the 10⁹ scan only and also omit zero-observation bins.
   The 10¹² X=24 row gives ratios 1.161 and 4.146. Retain the low-count caveat and say “no clear systematic excess”, not that every observation lies between the two surrogates.
4. **Assessment wording.** In §9 replace “asymptotic needs X≥p^0.3145” by “the cited Δ-bound supplies a sufficient range X≥p^(θ*+ε)”.
   Call the consecutive-prime samples “samples”, not randomized samples; the code takes consecutive primes in the progression.

## Recording decision

Accept the central mathematics after these local fixes: arithmetic average calibration, the elementary outer bound,
model-only C/M′/L, and the conditional implications S/D. Do not promote the additive parenthesis or density-one summary as written.
“Model-compatible class hypotheses must be joint” remains an assessment about the examined formulation, not a classification theorem.
Lot still postulates the tied divisor outcome; finite data with unspecified p₀ cannot establish or refute it.
NARROWED is justified; the conditional D strengthening is genuine but does not advance an unconditional ES mechanism.
