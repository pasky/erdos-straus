# Hostile cross-model review: I3_DEEP_FABLE (z49)

**Verdict: SOUND-AFTER-REPAIRS.** The principal positive theorems survive. The five advertised exponential-family coverings are correct, and the class-free lower bound has a valid proof with the stated constant. There are, however, major defects in the negative covering-search report and the interpretation of the numerical evidence. This is not a clean SOUND verdict on the document as written.

Reviewed: `side-agent/z49-i3fable`, commit `2c49ebe1`, worktree `erdos-straus-claude-agent-worktree-0044`. Line references below are to that version of `I3_DEEP_FABLE.md`. I read both wave briefs, the relevant FRONTIER/BREADTH and z48 predecessor material, the main document, and the pertinent scripts/data. I did not rerun the entire 10^8 census or rare-event grid. ES and general I3 remain open.

## 1. Fatal findings

**None in the principal positive existence claims or the class-free lower bound.** The issues below can be repaired without withdrawing those results. In particular, finite checks up to exponent 2000 are not the reason I accept Theorem 5.5: I independently checked a complete modular period and the interior-size threshold for each covering.

## 2. Major findings

### M1. The negative exponential-family search silently discards essential pairs; both reported uncovered families are covered

Lines 474–475 report that no covering was found for `3·2^k+1` and `5·2^k−1` with `uv ≤ 12000` and period lcm at most `3·10^6`. The search script discards every pair with `gcd(c,w) != 1`, where `uv = 2^a w`, rather than reducing the congruence

`c·2^k ≡ −(d+u+v) (mod w)`

by `g = gcd(c,w)`. When `g | d+u+v`, the correct modulus is `w/g`, and the coefficient `c/g` is invertible there. These omitted pairs matter decisively.

**Independent counter-certificates, PROVED by complete-period checks:**

* `I3(5·2^k−1) ≥ 1` for every `k ≥ 6`, using just four pairs, with maximum `uv=90` and period **6**:

| Pair | Exponent class |
|---|---|
| (5,6) | k even |
| (3,3) | k ≡ 3 mod 6 |
| (3,6) | k ≡ 1 mod 6 |
| (6,15) | k ≡ 5 mod 6 |

These cover all six classes. The last pair first becomes interior on its class at `k=11`; `k=5` is below the asserted threshold. For each class, division gives an integer `t=(5·2^k−1+u+v)/(uv)`, and its first occurrence at or above 6 has `t≥3`.

* `I3(3·2^k+1) ≥ 1` for every `k ≥ 5`, with maximum `uv=975` and period **360**, using:

| Pair | Exponent class |
|---|---|
| (3,14) | 0 mod 3 |
| (7,8) | 2 mod 3 |
| (3,5) | 1 mod 4 |
| (5,6) | 0 mod 4 |
| (5,27) | 10 mod 12 |
| (6,17) | 7 mod 8 |
| (9,38) | 13 mod 18 |
| (5,5) | 19 mod 20 |
| (4,11) | 1 mod 10 |
| (5,10) | 7 mod 20 |
| (5,15) | 15 mod 20 |
| (5,195) | 43 mod 60 |

The checked union is all of Z/360. I verified divisibility and `t≥3` for every `k=5,…,364`; periodic divisibility and monotonicity of t prove the infinite assertion. These certificates and their independent verifier are in `reviews/z49-i3fable-xcheck.py` and its output.

Strictly speaking, “no covering was found” can truthfully describe an incomplete search. But its unstated restriction makes the advertised numerical search bounds misleading, and the two families should not be retained as negative outcomes. Repair the search, replace these outcomes by positive certificates, and disclose the selected smooth-period menu. For bases other than 2 the script also excludes all moduli sharing a prime with the base; those negative searches are likewise not exhaustive over the stated uv range.

### M2. The H₄ calibration does not imply the asserted large-witness barrier for sign-free I3

Lines 79–81 and §6.1 import the signed H₄ tail into a statement that an I3 proof must, infinitely often, use a word with a very large larger endpoint. H₄ measures **certificate** edges. Small monochromatic interior words do not contribute to H₄ and may coexist with arbitrarily delayed certificates. There is no implication from “all small certificate edges absent” to “all small interior words absent.”

For a concrete illustration of the distinction, `(t,u,v)=(195851,5,9)` is an interior word of `8813281`; none of `t,u,v,tu−1,tv−1` is divisible by 4. The sign-free target accepts it and H₄ does not.

Repair: attribute any proposed I3 witness-growth law to **this document's own I3 simulator**, as a separate heuristic requiring its own extrapolation. Do not say the parent's H₄ calibration establishes it, even heuristically by implication. Fixed-H Schinzel/Dickson barriers remain valid and are unaffected.

### M3. The numerical agreement and tail-bias diagnosis are overstated

The headline at line 39 says agreement within 2–7% at every X≤1024; line 276 says every X≤512. The displayed table itself contradicts this:

* even non-squares at X=128: `.0018` versus `.0016` is a 12.5% excess;
* even non-squares at X=256: `.00025` versus `.0003` is a 16.7% deficit;
* even squares at X=512: `.0120` versus `.011` is a 9.1% excess.

At X=512 the even-square census contains only about 50 survivors; its relative binomial standard error is about 14%, not a few percent. Compatibility within uncertainty is plausible; uniform 2–7% relative accuracy is not the result shown.

The statements at lines 319–321 that overprediction is “beyond Poisson noise,” **hence systematic**, and is **located in P₂**, are also too strong. The Poisson p-values are conditional on an extra independence/count-model assumption, not a consequence of the CRT simulator. Moreover, the P₁ comparison itself predicts about 45/30/13 even-non-square survivors against 32/22/10 observed, and 5/3 square survivors against 3/2 in the first two windows. Those discrepancies do not isolate the error to P₂. The few square survivors cannot support that localization.

Repair: state the observed ratios, the conditional Poisson diagnostic, and that the source of the mismatch is **undetermined**. “Nominal-size treatment of the tail” is a possible explanation, not a located defect. Keep the already-honest factor-2-to-8 replicate spread and all extrapolation caveats.

## 3. Minor repairs and scope issues

1. **Thm 2.2(c), line 172:** the claim about “any class modulo 8t coprime to 2k₁” also needs coprimality to t. For example, k=3, t=5 and A′≡5 mod 40, excluding multiples of 3, satisfy the stated coprimality to 6, but `(-15/A′)=0`, never ±1. Actual word divisors automatically have `gcd(A′,t)=1`, so the intended application is sound. Say “admissible unit class modulo 8t, restricted to gcd(A′,k₁)=1.”
2. **The near-square summary still overstates the repaired theorem.** Lines 29 and 194 say depletion is confined to `k|2t` and is no more than `1/(2k)`. Theorem 2.2(c) explicitly retains 2-adic exclusions elsewhere. Even the displayed first-order model gives depletion approximately `2/(3k)`, not `1/(2k)`, for even k≥6. Separate the character-constant levels, the 2-adic restrictions, and the heuristic averaged factors.
3. **Lemma 5.2's numerical implication:** `T>n/9` alone does not imply `T>(n+3)/8`. Use the immediate stronger bound `T=tt′n+t+t′≥n+2`. The conclusion is correct. An exact interior bound is `T≤(n+6)/9`; the document's looser `(n+3)/8` is also valid.
4. **Prop 4.4's expectation wording:** class-free and class-restricted sums have the same leading density scale, not literally identical finite Haar expectations. With the size cutoff frozen at N=21, only u=3,A=8 occurs: the class-free contribution has expectation `1/24`, the interior-word contribution `1/8`. Replace “same expectation” by a stated first-order/asymptotic comparison. This does not affect the lower-bound proof.
5. **Theorem 5.5 exceptions:** for `7·2^k−1`, k=6,7 are failures of the **listed pair menu**, not failures of I3. The archived check itself gives I3=4 and 8 there. Keep that qualifier in the prose “exactly the exceptional k.”
6. **Small endpoint hypotheses in §5.1:** explicitly assume u≥3 in the `u|n` interior-word criterion; the displayed A bound alone does not make u=1,2 interior. Likewise “k! has an interior word (t,k−2,k−2) whenever k−2 is prime” needs k≥5. At k=4 the proposed endpoints are 2 and are free. The Wilson calculation in its stated p>k/2 range is correct.
7. **CERTIFIED is not a code-correctness proof.** It can label a reproduced finite enumeration, not the entire simulator or its asymptotic accuracy. The general use of EVIDENCE/Assessment for predictions is appropriate, subject to M3. The search-negative part of Thm 5.5 should not inherit the theorem's PROVED label without its algorithmic scope.
8. Corollaries 2.1a/2.2a impose a first-order averaging/conditional-sign model. Their factors are not theorems about I3(n), nor proved uniform asymptotics over k and n. The local square conditions and the elementary Haar integral are exact; the calibrated expectation should remain explicitly separate. Pólya–Vinogradov for an unrestricted progression does not by itself equidistribute the actual divisors of `tn+1`.

## 4. Result-by-result mathematical audit and novelty grade

Grades concern **campaign-level mathematical novelty**, not verified international priority: **0** = restatement/standard identity; **1** = routine refinement or extension; **2** = useful modest new campaign theorem; **3** = substantial new method or general existence progress. No result here earns 3. I performed no literature-wide priority search.

| Result | Mathematical verdict | Novelty |
|---|---|---|
| Lemma 2.0 | Correct norm congruence. The explicit root after division by g² is `g t₁ k₁ m` modulo A. | 0: elementary source identity. |
| Thm 2.1 | Correct exact **cell-level** table: 12 even-square cells, 16 odd-square cells. The reciprocity derivation and separate even-A analysis check out. Every listed cell has a witness by m≤240. This is not sufficiency for each individual t,u,m. | 1: useful refinement of z48's empty levels and endpoint obstruction, not a new reciprocity mechanism. |
| Cor 2.1b | Correct for all even squares. Independent enumeration of all 21 pair residue classes proves the global assertion, not merely a census statement. | 1: finite elementary consequence. |
| Thm 2.2 | The norm identity, cases (a)/(b), and the 2m² table are correct. Case (c) is correct on the admissible unit classes after minor repair 1. When k₁=2 in the actual squarefree decomposition, t₁ is necessarily odd; the even-t₁ calculations are redundant extensions, not additional cases that occur. | 1: routine squarefree generalization. |
| Cor 2.1a/2.2a | Accept as **first-order model computations only**, with minor repairs 2/8. They do not prove finite-count depletion factors. | 0 as an arithmetic theorem; 1 as calibration. |
| Prop 2.3, S_div | Correct Haar integral: mass at a=0 is `1−(ℓ−1)/ℓ²`; for unit n the a≥1 contribution totals 1/ℓ. Euler product is correct. Replace the inner P by an indicator/explicit conditional probability to avoid ambiguity with fixed n,t,u. | 1: elementary local-density calculation. |
| Prop 4.1, including 2m² and m²+1 | Correct CONDITIONAL result. Integer coefficients, negative discriminants, non-association, and absence of a fixed prime divisor all check. F_u(0)=1 establishes joint admissibility. The small exceptional endpoint divisors yield only free words. | 1: genuine extension to new families, but a direct Schinzel-H quadratic lift of the z48 Dickson construction. |
| Lemma 4.2 | Correct: `0<u+v−1<uv` for u,v≥2. | 0: one-line finite-cover obstruction. |
| Prop 4.3 | Correct W2/MP equivalences and boundary-piece conditions; {27} is necessary. The families claimed Dickson-infinite can be parameterized by admissible linear pairs, including p=3s+2 for the 3P branch. | 0: explicit bookkeeping from the free lines. |
| Prop 4.4 / C̃ lower bound | Correct unconditional lower bound from the stated classical divisor-problem input; details below. The Haar comparison needs minor repair 4. | **2: useful pointwise class-free theorem**, still no class-selection progress. |
| §5.1, u dividing n | Correct divisor reduction for u≥3, with the stated A lower bound; the factorial congruence is correct in its stated Wilson range. | 0: elementary rearrangement. |
| Lemma 5.2 | Correct identity and gcd privacy statement; repair the insufficient displayed inequality. | 0: already present in substance in z48/FRONTIER. |
| Lemma 5.3 | Correct for odd prime factors/odd A by multiplicativity and (2.1). It does **not** prove that I3 failure forces this norm condition, and the document appropriately avoids that converse as a theorem. | 0–1: repackaging the square reciprocity obstruction. |
| Lemma 5.4 | Correct **partial** involution on the domain u divides v+1, not a map defined at every endpoint-u word. Both stated free-to-interior families and their inequalities/congruences check. | 0: factor swapping and bookkeeping. |
| Thm 5.5(a)/(b) | Correct five infinite-family results, independently period-certified. Part (c) requires M1. | **2 for explicit campaign-family certificates; 0 for novelty of the covering method.** “Non-congruence family” describes the parameterized set, not a non-congruence proof mechanism. |
| Polynomial identity nonexistence for x, x²±1 | Correct under the stated integer-valued-on-all-Z and eventual positivity hypotheses. The degree/irreducibility cases exhaust the possibilities. Do not generalize the closing residue-class remark to arbitrary polynomial f. | 0–1: elementary classification, not a new barrier method. |
| Lemma 7.1 | Correct. In fact gcd(A,n)=1 follows automatically from A dividing tn+1. Reciprocity gives the Jacobi identity exactly. The odd-A certificate count is the familiar sign projection. | 0: z48 sign law extended to Jacobi notation. |
| CRT simulator / zero-tail model | Useful computational calibration, not a proof step. Local detector checked independently on actual integer residues; asymptotic predictions remain model-dependent. M3 needs repair. | 1: new numerical evidence; 0 as a general existence theorem. |

### Why the class-free constant is valid

For dyadic U between `n^(1/3+2ε)` and `n^(1/2−ε)`, the divisor summatory estimate gives

`Σ_{U<u≤2U} τ(n+u) = U log n + O(U)`.

For sufficiently large n, `12U²<n`. Each divisor exceeding `n/(6U)` has a complementary divisor at most 6U, and the number of divisors at most 6U over the interval is at most `U log(6U)+O(U)`. Thus subtracting twice this small-divisor count leaves at least

`U log(n/(36U²)) − O(U)`

admissible class-free pairs. Weighting by at least 1/(2U) and summing disjoint dyadic blocks gives

`liminf C̃(n)/log²n ≥ (1/(2 log 2)) ∫_(1/3)^(1/2) (1−2θ)dθ = 1/(72 log 2)`.

The inequalities are all in the safe direction, and ε can be sent to zero after the liminf. Neither divisor-class equidistribution nor an illegitimate average over the target n is used. This is the cleanest theorem in the document. The primorial-shift warning against a uniform upper bound is also correct.

## 5. Independent verification record

All numerical runs used `ulimit -v 8000000` and explicit timeouts. Python ran through uv. The checks use bounded loops and small arrays, not dense Cartesian-product allocations.

Committed verifier and output: `reviews/z49-i3fable-xcheck.py`, `reviews/z49-i3fable-xcheck.txt`.

* Independent divisor-of-n+u enumerator: all positive square/2-square words through m=240; the 12/16 and 16/16 cell counts are confirmed.
* All 21 `3≤u≤v≤8` congruences tested against the complete even-square residue set modulo uv: no intersection.
* W2/MP equivalences, the Vieta identity/involution, the odd-A reciprocity exclusion and Lemma 7.1: all n=3,…,1000.
* Norm congruence and Thm 2.2(a): k in {1,2,3,5,6,7,10,14,15}, m≤30.
* Exact finite Haar sums for ℓ=2,3,5, including both ℓ|n and ℓ∤n, with the analytic omitted tail ℓ^(−J).
* Five original covering periods **36,18,12,2,60**, with their thresholds **6,6,6,5,8**. All pass. Two additional coverings in M1 also pass.
* Recompiled the author's C census engine and ran it through 2,500,000: 112 zeros, byte-for-byte identical zero list to the archived 10^8 list. Compared counts to my independent enumerator at 1,010 targets, including 1225, 19600, 36078 and 2433600.
* A small C harness included the CRT detector and fed it the consistent residues of every actual n=3,…,20000. Its v-pass plus tail existence decision agrees with the exact count engine at every n. This tests the deterministic detector, not the rare-event estimator's precision or the extrapolation law.

Reproduction of the main verifier:

```sh
ulimit -v 8000000
timeout 120s uv run python reviews/z49-i3fable-xcheck.py
```

The optional census comparison activates when `/tmp/z49-i3-xcount_i3.u16` exists. That file was generated with the original C engine at N=2500000. The extra CRT harness is retained as `reviews/z49-i3fable-crt-xcheck.c` and expects that same file.

## 6. Final assessment

Retain the class-free theorem, the exact cell refinements, the properly conditional Schinzel construction, and the positive exponent coverings. Correct the incomplete negative search (which actually yields two additional positive families), remove the H₄-to-I3 inference, and tone down the statistical diagnosis. The document then becomes sound as a collection of modest structural results and evidence. Its own “no general I3/ES mechanism” conclusion is correct. The zero-tail extrapolation, including the approximate 10^−3 model-internal failure probability, is not a calibrated probability that the mathematical conjecture is false.
