# Z53 UPPER — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** The mathematical exceptional-set bounds survive; the novelty/milestone account needs substantial correction. No pointwise HC bound, ES proof, or new general ES exceptional-set record follows.

Reviewed `side-agent/z53-upper` at `920fe3d8716a0bd2fc1b014af1c5a7a197d39114`; comparison repository at `6588d7f1965270c4785fbab1e49353d7fef7f384`. The review covers every PROVED item, with emphasis on §3–4. All executed shell commands had resource limits and timeouts.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| L1.1 (U/T divisors) | CORRECT | U is `v(tc−1)=p+c`; T is `(cu−1)(cv−1)=cp+1`. A divisor −1 mod c forces its complementary T divisor to be −1 too. Positivity is preserved. |
| L1.2 (coordinate bound) | CORRECT | Order u≤v: `v(tu−2)≤p`; tu≥3 gives v≤p, tu=2 gives p+1 or p+2, tu=1 is impossible. Also t≤p+2. None of p,p+1,p+2 lies in C_p. |
| L1.3 (word parametrization) | CORRECT | `m=tu−1≥1`, `e=u`; both divisibilities and the displayed inverse follow directly. No coprimality hypothesis was lost. |
| P2.1 (HC=3/4; p+1) | CORRECT | c=3 uses divisor 2; c=4 uses the equivalence between a divisor 3 mod4 and a prime factor 3 mod4. The p+1 witness is `(1,q+1,(p+q+1)/q)`. Already substantially in the repo. |
| L3.1 (reciprocity) | CORRECT | Both U and T give `(d/p)=(2/p)^a(−c/d′)`. For c=4k, d≡3 mod4 and `(k/d)=1`; for odd c≡−p mod8, `(−c/d′)=(d′/c)=−(2/c)^a`. The paired 2-symbols agree, yielding −1. Jacobi reciprocity works for composite c and d′; c<p ensures the needed coprimality. |
| C3.2 (finite/smooth support) | CORRECT | Every prime dividing 2m is a quadratic residue when p≡1 mod8m, so any product of them has symbol +1. Dirichlet gives infinitely many such p. This excludes fixed-divisor covers, not arbitrary congruence arguments. |
| P3.3 (Linnik) | CORRECT | `M=8∏_{ℓ≤Y}ℓ`; p≡1 modM kills every Y-smooth certificate by L3.1. Linnik gives `log p≤1.02 L₀Y+O(1)`, and p>M→∞ ensures infinitely many distinct p. It is a lower bound on certificate prime support, NOT on HC. |
| L4.1 (BV mass) | CORRECT | Restrict to e≤T^(1/3), 4∣e: BV errors sum to O(T/log²T), while the main term before dividing by 2T is ≥T/6+o(T). Thus each dyadic block contributes ≥1/13 eventually; the top half of the logarithmic blocks gives S(y)≥(log y)/20. |
| L4.2 (symmetric functions) | CORRECT | Expand S^r into ordered tuples; sum the repeated-index tuples over the binomial(r,2) possible equal pairs. Nonnegativity justifies the union bound. |
| T4.1 (power window) | CORRECT | See the constant audit below. The p-relative consequence uses θ/2 and discards p≤2√x; this does not change the stated rate. The ineffective threshold is honestly labelled. The qualitative conclusion and even a stronger rate already follow from repository results. |
| §4.2 Rankin step | CORRECT | Under weights g(d), the d>Q tail/product ratio is ≤exp(−s+(e−1)G); s=(e−1)G+1 leaves ≥1−e^(−1). The uniform square-error bound ≤2.4 is valid, including K=1. |
| T4.2 (fixed K) | CORRECT | q>16K² separates all 1+2τ_K(q) roots; q∣16kk′−1 cannot occur there. Fixed-modulus Mertens gives dimension 1+κ(K). Remove p≤Q before applying the zero-root sieve. K=1 is exactly an existing theorem. |
| T4.3 (polylog window) | CORRECT | BT gives G=O(κ); see the uniformity audit below. The growing-modulus SW error is summable, not K times an uncontrolled constant. The floor in K is harmless since 4K≤(log x)^A. |
| §5.1 / §5.3 exact reformulations | CORRECT | L1.1 gives S_θ and the divisor-subproduct formulation. L1.3 gives the coordinate alternatives, allowing endpoint interchange. S_1 implies ES on large primes; the memo correctly does not assert the converse. |
| §5 stopping/heuristic claims | CORRECT-WITH-FIX | The finite-support obstruction is proved; broad statements about what no pointwise method can do are assessments. The q<p experiment does not alone justify a claim about unrestricted prime divisors; retain its precise cutoff, or supply the boundary argument below. |
| §6 census and prime-level numbers | CORRECT (finite scope) | Full reruns agree byte-for-byte; details below. The HC≤64 census itself is already in LOWERTAIL_ROUND2_FABLE. |

## Analytic details that could have failed, but do not

T4.1: `Σ(τ*(q)/q)² ≤ (16/9)ζ(2)^4/ζ(4) = 12.0258137079 < 12.1`.
With Λ=(θ log x)/20 and r=⌊√Λ/2⌋, S≥Λ/r gives S²/r²≥16, so the repeated-index loss is <S^r/2.
Consequently `L≥4^r/2≥exp((log2)√Λ)/8`, and `(log2)/√20=0.1549924214>0.15`.
The large sieve contributes ≤2x/L. Passing to p^θ loses √2 in the exponent, still leaving >0.1.

T4.3: put H=16K². For m=4k and t≥H, BT gives π(t;m,−1)≤4t/(φ(m)log t), hence the displayed G≤4+16κ and s=O(log K).
The asserted κ≤2H_K is valid but deserves a justification: `κ=Σ_{k≤K}1/φ(2k)≤H_K∏_{ℓ odd prime}(1+1/(ℓ(ℓ−1)))<2H_K`.
It does NOT follow from the false termwise inequality φ(4k)≥k.
Start SW at `y₁(m)=max(H,exp(m^(1/N)))`, N=⌈2A/ε⌉. Partial summation bounds its reciprocal-prime error by `O_N(exp(−c_N m^(1/(2N))/2))`.
Its sum over all k is finite for fixed N. Meanwhile `log log y₁≤(ε/2)log log x+O(1)` uniformly in k≤K, and `log log z=log log x−O(log log log x)`.
Thus the Euler-product exponent is ≥`(1−ε/2−o(1))A(log log x)²`; the ε margin absorbs all losses. Also z>y₁ and the discarded √x primes are negligible.
No GRH, EH, or effective Siegel constant is silently used.

## Novelty audit — required correction

1. **T4.1 is not a new repository milestone.** `I3_DEEP_ASTRA.md §3.4` already transfers its square-root-log prime-modulus sieve to 4-divisible levels. More decisively, `EXSET_I3.md §7.3` already proves the U/ES₅ bound `N exp(−c(log N)^(2/3)/(log log N)^(1/3))`, using the atoms of `I3_DEEP_ASTRA.md Lemma 8.7 / Thm 8.8` with 4∣u.
Those atoms have `u≤X^(1/6)`, where `log X=O((log N log log N)^(1/3))`. Thus HC≤N^o(1), not merely HC<∞, outside that stronger exceptional set. Discarding p≤√N gives HC(p)≤p^θ for every fixed θ>0 with the stronger rate. This is an implication of the existing internal theorem/proof, not a fresh external-literature claim.
2. `LOWERTAIL_ROUND2_FABLE.md §§1.2,3.1–3.3` already contains the two coordinate-line conditions, HC=3/4 characterization, HC≤64 census, and `#{HC>4}≪x/log²x`. T4.2 at K=1 repeats its Theorem 3.2. General fixed K and T4.3 are useful explicit window refinements not found verbatim in the searched repo.
3. `FOREST_DEEP_FABLE.md Prop 3.1` already writes the forced nonresidue condition on the certificate modulus; Prop 3.2 already gives the finite-cover/Linnik logarithmic obstruction. L3.1 is a clean direct formulation; P3.3 extends the presentation to arbitrary smooth support. Do not sell either as a new reciprocity mechanism.
4. `notes.md §§12.1–12.3` already uses growing-dimensional root sieves and Siegel–Walfisz to get a log-log-squared exponent for ES exceptions. T4.3's contribution is the precise HC window and coefficient, not a new sieve technique or general exceptional-set exponent. No external novelty is established by this audit.
5. Vaughan's stronger ES rate alone is not a bound for this HC statistic. `I3_DEEP_ASTRA.md §8.7` explicitly diagnoses the ratio-family witness as a word of bn, not n. Retain the memo's caution about that transfer; add the direct U/ES₅ comparison above rather than infer HC from unrestricted ES results.

## Computation and scope

Extracted the reviewed scripts/data with git archive into `/tmp/xrev_UPPER`; inspected their allocation bounds first (the largest prime-certificate allocations total about 600 MB, below the imposed 6 GB ceiling).
Compiled both C programs with `gcc -O2 -Wall -Wextra`; both builds succeeded without warnings.
`timeout 1200s /tmp/xrev_UPPER/hc 100000000 24 20000000` (CPU limit 1100 s) exited 0 and its entire stdout matched `hc_1e8.txt` exactly.
This reproduces 2,880,504 primes, the complete HC histogram, record 64 at 21841, 45,499,504 reciprocity checks with zero violations, and every printed sieve-containment count.
`timeout 600s /tmp/xrev_UPPER/primecert 100000000 100000000` (CPU limit 550 s) exited 0; stdout and failure-list stderr matched both archived files exactly: Q₄ failures 760, Q_C failures 4, including all histogram bins and record values.
A SymPy spot-check independently returned `(HC,word)` = `(7,(7,5,99))`, `(8,(8,5,1706))`, `(15,(5,15,14804))`, `(15,(167,15,34211))`, `(64,(64,9,38))` at the four Q_C failures and 21841 respectively.
These are finite certifications, not numerical tests of the ineffective asymptotic bounds.

The prime-certificate executable stops at q≥p despite printing “no q≤QM”; correct that output label and preserve q<p in every quotation.
For the stronger all-q conclusion at the four failures, an available missing argument is: a prime q=tu−1>p forces the opposite endpoint v=1. Indeed v≥2 and u≤p+2 would give `q=(p+u)/v≤p+1`, leaving only the even nonprime p+1. Thus `(t−1)u=p+1`.
Here p+1 factors respectively as `2·41²`, `2·5·6653`, `2·547741`, `2·5·2693·3181`; all odd primes are 1 mod4. Every divisor u is consequently 1 or 2 mod4, and neither u nor `t=1+(p+1)/u` belongs to C_p. Thus q>p cannot rescue these four examples, but this justification is absent from the memo.
In general, distinguish “some primes need composite certificates” from “every pointwise proof must explicitly exploit a particular subproduct method”; the latter remains an assessment.

## External-input checks

- BV: [Kedlaya, Theorem 17.1](https://kskedlaya.org/ant/chap-bombieri.html#T-bv), inspected with its modulus range; the required T^(1/3) lies strictly inside the permitted range. Partial summation supplies π from ψ. The stronger maximal formulation in the memo is standard and unnecessary for its two endpoints.
- SW: [Teräväinen, Theorem 7 and proof](https://jonismathnotes.blogspot.com/2015/01/the-siegel-walfisz-theorem.html), inspected: the exact `π=Li/φ+O(x exp(−C_M√log x))` uniformity for q≤log^M x used here. The proof chooses Siegel's ε=1/(2M), explaining the ineffective constant.
- Linnik 5.5: Heath-Brown (1992), DOI `10.1112/plms/s3-64.2.265`; original publisher access hit a security page. The attribution and uniform bound were corroborated in the [introduction of arXiv:0912.0147v3](https://arxiv.org/html/0912.0147v3), not falsely recorded as a primary-paper recheck. Any admissible Linnik exponent suffices. The 1.02 Chebyshev margin can also be obtained for sufficiently large Y directly from PNT, so no all-small-Y numerical claim is load-bearing.
- Vaughan benchmark: [Pomerance–Weingartner, introduction and §4](https://arxiv.org/html/2511.16817v2), inspected, confirms the 1970 exponent 2/3 and that its residue family is larger than the memo's divisor shadow. This is not a verification of an HC witness map.

## Required fixes, in priority order

1. Rewrite §0's milestone/novelty comparison using the stronger pre-existing HC consequence above; explicitly identify the repeated HC census and K=1 theorem. Retain T4.1 as an elementary reproof with explicit constants.
2. Keep the finite q<p scope in §5.2.3 and the data labels, or include the boundary exclusion before claiming unrestricted prime certificates are insufficient. Label universal methodological judgments as Assessment.
3. Make p≡1 mod4 explicit in T4.2/T4.3, and add the short reciprocal-totient upper-bound justification. These are exposition fixes, not losses in the bounds.

**Final assessment:** ACCEPT-WITH-FIXES as a correct bounded-window sieve memo with useful refinements; not an advance on the existing power-window exceptional-set rate and not progress on the pointwise target. ES remains open.
