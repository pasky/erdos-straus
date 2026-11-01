# Hostile review of Z53_HYPSUMPROD

## Issues

No FATAL issue found in Theorem 1. The numerical exponent 74/225 survives independent checking. The following corrections are needed; several concern claims surrounding the theorem rather than its proof.

1. **MAJOR — A grid computation is promoted to a global theorem.** §3.7, Remark (1), line 189: “i.e. R(n) ≪ n^{0.3272}” does not follow from the exponent-map computation. A sampled maximum is not an upper bound on the maximum over the continuous simplex, and the off-cube argument has not been written out. The surrounding labels acknowledge this, but the displayed implication nevertheless asserts a theorem. The “exactly” descriptions of the winning region in §0 and §4.3 likewise exceed the evidence. **Fix:** retain 0.3272 as a numerical candidate, explicitly not proved, and describe the sampled winning region. A global result requires continuous parameter coverage, uniform estimates, and logarithmic/endpoint bookkeeping.

2. **MAJOR — The method-exclusion conclusions are broader than the proved propositions.** §0, lines 32–50; §9, lines 350–352; §11, final sentences. Props B and C concern specific λ-uniform/class-blind majorants. An O(1)-per-fibre upper bound is not a lower bound prohibiting another fibre-based argument from proving that most fibres are empty. Lemma D is a reduction, not such an impossibility theorem. Cor A′ restricts heights certified by a congruence alone; it does not prohibit fixed-congruence counts from certifying solutions. For example, n=5, H=1, (x,y)=(3,7), q=4 certifies (u,B,C)=(1,2,1). **Fix:** restrict the conclusions to the precise majorants/reductions established. Replace “every ... cannot ... certify ES” with the actual finite-height restriction. Also replace “can never feed”/“cannot be a step of” a positivity argument (§3.7 Remark (3), §8.1) by “does not imply positivity by itself”; an upper bound can be an ingredient of an argument using additional prime-specific information.

3. **MINOR — False joint-divisibility identity for composite n.** §4.1, lines 216–217: L₁ ∩ L₂ is not generally {uB | n+u+B}. Take n=18, u=B=2: both individual relations hold, but 4 does not divide 22. This matters in an explicitly integer-uniform memo, although Theorem 1 never uses the identity. **Fix:** write {lcm(u,B) | n+u+B}, and impose gcd(u,B)=1 before replacing lcm by uB.

4. **MINOR — Logarithms are silently removed from proved bounds.** §6, line 298, drops (log T)²; §11, line 373, drops (log n)². Neither stronger estimate is established by the written proof. **Fix:** restore those factors, or use the corresponding exponent +o(1).

5. **MINOR — The cube row conflates a discretized computation with the exact theorem.** §4.2, line 237: the script returns θ=0.320333..., gain 0.013000..., whereas Theorem 1(c) gives θ=8/25=0.320000..., gain 1/75=0.013333.... Thus “+0.0130 (=1/75)” is false. **Fix:** print the exact theorem values, or explicitly distinguish the discretized result from the stronger analytic choice. The other seven table rows reproduce the script's numbers.

6. **MINOR — H=1 bookkeeping is not justified termwise.** §3.6, line 166, substitutes log H for a sum containing its h=1 term. **Fix:** use log(2H), or better retain h^{-1/6} and use Σ_{h≤H}h^{-7/6} ≪ 1. The final bound and exponent are unchanged; the omitted term at H=1 is also absorbable into the first term in the stated parameter range.

7. **MINOR — Unqualified priority claims are not established.** §0, lines 16–17, and the “genuine new” language elsewhere. A brief literature check did not identify this specific argument as already published, but that does not verify “first” in the literature. **Fix:** say “first in this campaign” unless a substantially broader literature review supports priority. The tools themselves—square sieve, quadratic character evaluation, reciprocal-phase discrepancy—are standard; any novelty is their application to this particular restricted equation.

8. **NIT — State the discrete conventions in Prop C.** §4.1, lines 211–215, uses exactly UV pairs and X shifts, so U,V,X should be integers, or actual interval cardinalities should replace them. Its deduction of the coefficient log 2−o(1) from the displayed average also needs V→∞ and X/V→∞. **Fix:** specify these conventions/limits. This does not affect the unrestricted shift-uniform obstruction intended there.

## Theorem 1 audit

**Ranges and detection (§§3.1–3.2).** The bound on M follows because 4T^{2−2η}−2 ≥ 2T^{2−2η}. The interval for s covers all integral sums, including the lower boundary. The converse square-detection statement correctly gives positive integral roots: s²−r²=4k implies equal parity and s>r. Nonzero squares have precisely two ordered preimages in the unrestricted strip; imposing the near-cube restrictions can only remove preimages. Zero discriminant gives at most τ(n) triples because u | n and C is then determined. There is no missing factor of two and no requirement that the converse preserve all near-cube inequalities.

**Square sieve (§3.3).** Correct. For m²≤2^{P₀}, ω(m)≤log₂m≤P₀/2. Negative nonsquares are harmless because the added weight times the square of the real character sum is nonnegative. No assumption that f is nonzero modulo each sieve prime is needed: prime divisibility of an actual square is exactly what the ω(m) argument controls. The value f=0 is separately removed and its characters vanish. Since 2+4η≤2.2<3, P₀≥3log₂T suffices. For sufficiently large T, the chosen prime set satisfies this; finitely many smaller n are absorbed in the implied constant.

**Complete sums (§3.4).** Correct: the discriminant is 16(4cn+1). If q | c, the polynomial is n²−4k modulo q, nonconstant because q is odd, and its character sum is zero. Otherwise the leading coefficient is a nonzero square, giving −1 or q−1. If q | n the exceptional c-class is empty. CRT gives the stated product even for nonunit c and for zero character values.

**Main term (§3.5).** Correct. The half-open interval count follows exactly from floor β−floor α with ψ(x)={x}−1/2, also at integral endpoints. Its length contribution is independent of k₀. The monotone-AP inequality has the required single J_max boundary loss. Expanding |K(C)| gives

    Q^{-1}[4Σ_J+(q+q′+Q)J_max] ≤ 4Σ_J/Q+3J_max.

The exceptional intersections are either empty or one class modulo Q; no coprimality condition on c₀ is missing.

**Discrepancy (§3.6).** Apart from issue 6, the argument works. Direct differentiation gives

    (hg)''' = −(3/2)h(n+S)Q²/C⁴.

On W<C≤2W its magnitude lies between λ_h and 16λ_h with the stated λ_h=(3/32)h(n+S)Q²/W⁴. Also n≤n+S≤2n. For sufficiently large T, Q≤T^{1/2} implies Q≤W, so the number of j-values is O(W/Q), including truncated pieces. Neither residue class introduces an extra derivative term.

Vaaler's stated inequality follows from its Fourier polynomial and nonnegative error kernel; I checked the cited Ma–Sun Lemma 2.1. The third-derivative estimate is the standard consequence of differencing followed by the second-derivative test: with differencing length about λ^{-1/3}, its squared bound is O(N²λ^{1/3}+Nλ^{-1/3}); the extreme parameter ranges follow from the trivial estimate. Here the derivative ratio is the absolute constant 16.

Independent exponent calculation gives the two exponential-sum terms

    h^{1/6} T^{1/2} W^{1/3} Q^{-2/3},
    h^{-1/6} T^{-1/2} W^{7/6} Q^{-5/6}.

For H=ceil(T^{1/7}Q^{-2/7}), the first Vaaler term is at most T^{6/7+2η}Q^{-5/7}; the positive-h term is at most T^{6/7+2η/3}Q^{-5/7}, hence also the claimed weaker bound. Multiplication by Q² gives precisely Q^{9/7} and Q^{7/6} in Lemma 1.4. The endpoint and dyadic losses are covered by (log T)².

**Assembly (§3.7).** With P=T^{1/25}, the three T-exponents, before the η contributions, are

    1−1/25 = 24/25,
    6/7+(18/7)/25 = 24/25,
    2/3+(7/3)/25 = 19/25.

The last becomes at most 263/300=0.876666... when η≤1/20; even its log² factor is asymptotically absorbed by T^{0.88}. The omitted main-term contributions and τ(n) are smaller. At η=1/75,

    24/25+2η = 1−η = 74/75,
    (74/75)/3 = 74/225 = 1/3−1/225.

**Shiu in part (b).** Valid, including the growing modulus. I read Theorem 1 on printed page 163 of `sources/shiu-1980.pdf`. Put Y=T^{1−η}. For the ordinary short interval use x=n+Y, y=Y and the standard modulus-one case. For the C-sum use x=4nY+1, y=4nY, k=4n, a=1. Shiu's fixed parameters can be α=1/5, β=1/4: k<y^{4/5} and x^{1/4}<y≤x hold for large n throughout the stated η-range. The function τ satisfies his multiplicative-function hypotheses. Uniformly, since every prime divisor of k is below x,

    exp(Σ_{ℓ≤x, ℓ∤k}2/ℓ) ≪ (log x)²(φ(k)/k)².

Indeed the error between −2/ℓ and 2log(1−1/ℓ) is summable. Shiu therefore gives O(Y(φ(k)/k)log x), at most O(Ylog n), not an unwanted k/φ(k) loss. Thus the explicit log² theorem is justified. Part (c) uses C≍T and s≍T with fixed comparison constants; η=0 in these size estimates gives T^{24/25}=n^{8/25}. No circularity or dependence on primality was found.

## Other results, computations, and novelty

Props B and C have the claimed averaging proofs under the discrete conventions above. Lemma A and Cor A′ are correct; the latter's t=1 counterexample proves necessity even though the permitted factorization may depend on x. Lemma D is a genuine bijection: equivalently, its divisor variable is d=(n+B)/u=4BC−1, with d≡−1 mod 4B. None of these proves the broader impossibility conclusions flagged in issue 2.

Independent verification performed:

- Exhaustive square-detection comparison for every 2≤n≤300: 604 unordered points, including diagonal cases; all matched.
- 8,253 complete prime-sum cases for odd primes through 43, plus CRT checks for six prime pairs and all c-classes with 0≤n<12: all matched.
- Exact rational checks of half-open interval identities, including negative/integral endpoints, and the monotone-AP bound: all passed.
- Recompiled and reran the full enumeration through 500,000,000: output is byte-for-byte identical to `rmax_5e8.txt`. This reproduces max Q=22 at 199582860, prime-class max Q=16 at 9405457, max R=439 at 480134654, and the reported top-range means.
- Recompiled and reran all eight square-detection examples and all four large controls: every comparison and every printed table statistic reproduced. The claimed prime and square identities checked out.
- Recomputed all eight exponent-map rows. The stored fine-grid maximum is 0.327166666... at (0.328,0.344,0.328), consistent with its numerical description but not a continuous-domain proof.

All shell commands were timeout-bounded; Python/C jobs used the requested 6,000,000-KB virtual-memory cap and Python ran through uv. The large enumeration uses about 3.5 GB of explicitly bounded arrays.

The brief novelty search found Elsholtz–Tao, *Counting the number of solutions to the Erdős–Straus equation on unit fractions* (https://arxiv.org/abs/1107.1010), with the known full Type-II 2/5 bound, not this restricted square-sieve estimate. Searches for the equation/square-sieve combination did not reveal an obvious prior occurrence. This supports neither a plagiarism objection nor a literature-priority certification. The memo does not claim ES is proved; its principal overclaiming is about method exclusions and the unproved exponent-map refinement.

## Overall verdict on Theorem 1: CORRECT WITH FIXES

The stated bound R(n) ≪ n^{74/225}(log n)² and the cube-block exponent 8/25 are supported by the argument, uniformly in n. Repair the H=1 bookkeeping and the inaccurate downstream restatements. Do not promote the 0.3272 grid calculation or the broad method-exclusion language to proved results.
