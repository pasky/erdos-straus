# Hostile internal review of Z53_HYPKLOOST.md

## Verdict

**Major revision required.** There are useful exact identities and two useful **positive-mean** obstructions, but the memo repeatedly turns these into false obstructions to **pointwise positivity**, and then into an unjustified exhaustion of possible analytic methods. One stated part of Theorem B is false, including for a block in the memo's own LP output. The numerical calculations are mostly reproducible; their interpretation as conductor orthogonality is not.

“Narrowed” is defensible only as “these particular estimates do not presently improve the elementary bound.” It is not defensible as “all linear positivity methods need the top spectrum” or “cross-conductor cancellation has been excluded.” ES remains open.

I read the entire memo, HYP §§2–3, LIT_CHECK.md, the conductor/analysis/KF/LP scripts, and the LP/window results. Literature arithmetic below is checked **against the quoted statements**, not independently re-certified against the original PDFs. I did not edit Z53_HYPKLOOST.md.

## Findings

### F01 — CRITICAL — Positive mean is repeatedly confused with pointwise positivity

**Locations:** summary items 2–3 and “What survives”; §5.1 Reading; §5.2(c) and Reading; §§6.3, 8–10 and proposed FRONTIER text.

B(b)'s valid first conclusion is that a certificate with **positive mean** needs H ≥ q_max/2. It does not say a certificate with positive value at a specified prime needs this degree. C(b) similarly obstructs positive mean, not positive value. The memo briefly acknowledges deviations from a negative mean, then excludes precisely that possibility in its conclusions.

There is an explicit counterexample even for a full integer-sided block. Take U=1, V=2, p=19. The pairs are (2,3), (2,4), with q=24,32. Set

    c = cos(2π/32), t = cos(2π·25/32),
    G(x) = (cos(2πx) − c)(cos(2πx) − t)².

This has degree 3 < q_max/2=16. Every nonzero point in T has distance at least 1/32 from an integer, so G≤0 on T; G(0)>0. At p=19 the phases are 1 and 25/32, so ΣG(−F)=G(0)=0.012448824648788116>0. It is a genuine low-frequency positivity certificate. Its mean is nonpositive, as the valid theorem requires.

Likewise for the pair (2,3), q=24,

    f(m) = 1[8|m] + 1[3|m] − 1 ≤ 1[24|m]

has only conductors 1,3,8, not 24; f(24)=1. Set this f for (2,3) and all other pair functions to zero. This is a conductor certificate at p=19 with no primitive conductor at all. Its mean is −13/24, consistent with C(b).

**Fix:** insert “positive-mean” everywhere the degree/top-conductor necessity is used. Explicitly retain low-frequency/low-conductor negative-mean certificates whose oscillatory value is positive at p. Do not claim that only the band q_min≤|h|≤H survives: B does not exclude using the lower nonzero frequencies. Delete the assertion that the displayed high-band sum is “equivalent to the problem”; no such equivalence is established. A max-|S_h| ceiling also does not imply a ceiling for signed weighted frequency sums; HYP §3.6 explicitly warns of this.

### F02 — CRITICAL — Theorem B(b)'s expectation claim is false as stated

**Locations:** §5.1(b), its second proof, the “any finite set” assertion, and all summaries of the H<q_min threshold.

The exact expectation identity

    E Σπ G(−Fπ(n)) = |P|·ĝ(0),  H<q_min

is correct. The inference “q_min≤q_max, hence ĝ(0)≤0 by the first claim” is not: the first claim requires H<q_max/2, not H<q_max.

The memo's own `certificate_lp.txt` gives U=V=2, q_min=36, q_max=64, H=32 and positive mean 0.005311. Thus H<q_min, but the expectation is positive. This is also a rigorous consequence of the repaired Selberg construction in F04, not merely numerical evidence. A singleton pair gives another immediate contradiction: q_min=q_max=q, and positive-mean certificates exist already at H=q/2.

**Fix:** the universally valid nonpositive-expectation range is

    H < min(q_min, q_max/2).

The original H<q_min assertion is valid if one adds q_min≤q_max/2. For integer rectangular blocks this is (U+1)(V+1)≤2UV, and is true in the large balanced regime, not for every block. The verbatim arbitrary-finite-set extension must be corrected accordingly.

### F03 — MAJOR — The Fourier support hypothesis excludes the given example and arbitrary degree-H polynomials

**Location:** opening of §5.1 and the phrase “every linear combination.”

The specified Fejér transform is supported on [−H−1,H+1], not [−H,H]. Moreover a continuous transform supported on [−H,H] vanishes at ±H, so it cannot interpolate a general degree-H polynomial with nonzero endpoint coefficients. For H=0 it can only be zero, excluding even a nonzero constant G.

**Fix:** require that ĝ(k)=0 for integer |k|>H, allowing compact support in [−H−1,H+1]. This includes the Fejér pair. Arbitrary coefficients can be interpolated by smooth compactly supported bumps around the integers, with the real-symmetry condition; the inverse transform is rapidly decreasing. The Poisson identity and its signs then remain unchanged.

### F04 — MAJOR — Selberg sharpness proof does not establish G(0)>0

**Location:** last sentence of §5.1(c)'s proof.

Positive integral and nonpositivity off a symmetric arc imply positivity somewhere in the arc, not at its centre. The three listed properties of S⁻ do not justify the asserted centre value. This is a proof gap, not evidence that the sharp positive-mean threshold is wrong.

**Precise repair sufficient for sharpness:** set H₀=q_max/2 and choose

    1/(q_max+2) < δ < 1/q_max.

The Selberg minorant of degree H₀ has positive mean. Since H₀<q_max, quadrature on the full q_max-grid is exact. All its nonzero grid values are ≤0, so

    q_max·mean(S⁻) = Σr S⁻(r/q_max) ≤ S⁻(0).

Thus S⁻(0)>0. This proves existence exactly at H₀; the same polynomial works for every degree allowance H≥H₀. Together with half-shifted quadrature this proves the sharp **positive-mean** threshold for every nonempty finite set of positive-integer pairs.

For the stronger assertion about the particular Selberg minorant for *every* δ and arbitrarily large H, either prove its centre value from the explicit construction or remove that assertion. LP experiments do not fill this analytic gap.

### F05 — MAJOR — Poisson periodization is not a finite-window or information-loss theorem

**Locations:** summary 2(a), §5.1 Reading, ledger §6.3, §8(iii), §§9–10.

Equation (5.1) has an infinite ℓ-sum. The scale q/H and the positive central weight/tail bounds are properties of the Fejér example, not of every admissible signed interpolating g. The weights depend on the pair through qπ, so this is not even a functional of the scalar counts N(n+ℓ) alone. It is a weighted count of **pair-labelled** solutions. No fixed finite window suffices exactly, and the nonuniqueness of interpolation prevents the claimed information-theoretic conclusion. For example integer translates of g have identical integer Fourier samples and identical periodization, but very different real-line localization.

**Fix:** call (5.1) an exact pair-weighted periodization identity. State a localization heuristic, or a separately proved tail-controlled approximation, only for specified kernels. Remove the claim that arbitrary polynomial/nonlinear uses of short-frequency sums have “the same information-theoretic content” as finite window data. Nonlinear/amplified methods are genuinely not covered here.

### F06 — MAJOR — Parseval does not make the measured relative-depth bins orthogonal

**Locations:** §3 “Square-root prediction,” all statements that F1 proves orthogonality, and §§0, 8–10.

Distinct **absolute reduced conductors** have disjoint Fourier support under uniform n mod L. Relative bins k=floor(log₂(qπ/d)) do not: the same conductor d can occur at different relative depths for different pairs. The table and quoted covariance shares use these relative bins. Applying Parseval to conclude Var(N)=Σ_k Var(P_k) for these bins is false even in the stated uniform residue model.

Tiny exact-character check: for U=V=2 and uniform n mod L=576,

    Var(N)                  = 0.1194993007330247
    Σ Var(relative bins)    = 0.1216694396219136
    cross share             = −0.0178363514752151
    Cov(relative bins 3,4)  = −0.0020254629629630.

By contrast the sum of absolute-bin variances is 0.1194993007330248, as Parseval predicts.

There is a second model mismatch: uniform n over all residues is not uniform prime/unit residues, or uniform n≡1 mod 4. Orthogonality of distinct additive characters generally fails under those conditioned measures.

**Fix:** state Parseval only for distinct conductor pieces or disjoint absolute-conductor bins under the **unconditioned** uniform model. Treat relative-bin and prime-sample covariances as empirical quantities with no exact orthogonality prediction unless separately derived.

### F07 — MAJOR — F1/F3 evidence is promoted to a no-cancellation theorem

**Locations:** summary 1 and 4, §3 interpretations, §§8–10.

A small aggregate covariance over a finite prime sample is not an impossibility result at fixed p, is not mutual orthogonality, and need not exclude large cancelling individual covariances. The prime-10¹² aggregate share is +14%, with the stated bootstrap interval excluding zero; “orthogonal” is not literally the measured result. Sample standard deviations of order one are not an asymptotic O(1) theorem.

“The only exact cross-conductor cancellation is T1's” is also too strong even pointwise: 92.4% of the p12 rows have N=0, so their full nonzero conductor contributions sum exactly to zero as well. What distinguishes squares is the universal T1 identity across all such n, not the existence of exact zero totals.

Similarly F3's rms square-root size for b≤16 and these primes is not “the best that any bilinear KF bound could give.” No general lower bound preventing stronger cancellation has been proved.

**Fix:** say “no aggregate variance reduction in these sampled prime bins,” “sample sds are order one,” and “T1 explains an exact zero total throughout the square control.” Keep all extrapolations labelled EVIDENCE/Assessment; explicitly retain possible joint conductor/frequency cancellation and different weights. HYP Thm 5 expressly does not exclude joint summation over conductors.

### F08 — MAJOR — Uniform-residue mean and prime local mean are conflated; certificate normalization is missing

**Location:** §5.1 Reading, especially “M=Σπ1/qπ over admissible pairs” and “this is ≈0.146.”

For N as defined over all pairs, uniform n mod L gives

    E N = Σall pairs 1/qπ = (H₂U−H_U)(H₂V−H_V)/4,

which tends to (log 2)²/4≈0.120113, not 0.146. For U=V=1000 the absolute-bin zero term is about 0.120027. Restricting this 1/q sum to admissible pairs does not produce 0.146 either. HYP's approximately 0.146 is the prime/unit model

    M₀ = Σadmissible pairs 1/φ(qπ),

or the matching low-conductor leading constant. These are different models. Also the defined frequency certificate satisfies ΣG≤G(0)N, not ΣG≤N, unless G is normalized.

**Fix:** separate these means and measures throughout. Normalize G(0)=1, or divide the frequency side by G(0), before comparing its expectation to the mean count. Resonance statements E S_h=Σ_{qπ|h}e(hsπ/qπ) concern the unconditioned uniform model only.

### F09 — MAJOR — lcm/divisor-closed support is not the full class-average projection

**Locations:** §5.2(a) after the exact identity; Reading; ledger and summary formulations of arbitrary conductor truncations.

The identity is valid for the **unweighted full projection onto all d dividing M**. A divisor-closed set with lcm M need not contain every divisor of M: {1,2,3} is divisor-closed with lcm 6 but omits 6. Arbitrary weights likewise need not be the conditional expectation operator.

For a pair with q=24 and m=0, keeping d=1,2,3 gives (1+1+2)/24=1/6, while the M=6 class projection is 6/24=1/4. Both depend only on m mod 6, but they are different functions.

**Fix:** distinguish “depends only on n mod M,” valid for any support with denominators dividing M, from “equals the class average,” valid only for the full unweighted projection. Make this distinction in the summaries as well.

### F10 — MAJOR — HYP Theorem 3 is misapplied to divisors of lcm(1,…,D)

**Location:** last sentence of §5.2(a), repeated “low conductors” class-average Reading.

HYP Thm 3 treats d≤D. The projection onto d|lcm(1,…,D) includes conductors much larger than D (already 6 for D=3). Such conductors can be comparable with the pair moduli, where the required smooth equidistribution estimate does not apply. Smoothness alone does not repair the range error. The hypothesis that n is coprime to every d≤D must also be stated; the preceding identity was for every integer n.

**Fix:** use HYP Thm 3 only for the actual cutoff d≤D, with its smoothness and coprimality hypotheses. Do not assert a superpolynomially constant Λ_lcm(1,…,D) without a new theorem controlling the additional divisors. Alternatively restrict M so that every contributing divisor is within the proven cutoff.

### F11 — MAJOR — General conductor certificates do not have complete Ramanujan primitive components

**Location:** §5.2(c), its Reading, summary 3, and “where the dual has nothing to sum.”

The lemma allows arbitrary real fπ on Z/qπ. Its primitive Fourier component can have unequal coefficients at the primitive frequencies; it need not be a scalar multiple of c_qπ. A complete Ramanujan sum is available for the original unweighted indicator dual, or for the explicitly restricted Ramanujan-weight class, not for every fπ.

Moreover “≤K p^{o(1)} pairs at each conductor” does not bound cancellation across many distinct conductors; that is exactly the distinction HYP Thm 5 makes.

**Fix:** restrict the complete-Ramanujan assertion to Ramanujan-form weights. For general fπ retain its arbitrary primitive Fourier component. Replace “nothing to sum” by the precise fixed-conductor divisor-count bound, under UV≤p, without excluding joint-conductor methods. Retain the positive-mean qualification from F01.

### F12 — MAJOR — O2's claimed formula for N omits the 4-condition

**Location:** §4(O2), bullet “Summed over B this gives … N=…,” and summary 4(a)'s description as an expansion of 4uB divisibility.

Equation (4.1) correctly detects the two relations u|p+B and B|p+u, hence uB|p+u+B for coprime pairs. It does not enforce 4|(p+u+B)/(uB). For p=17, U=V=2, the pairs (3,4),(4,3) satisfy both relations and contribute 2 to the displayed sum; N=0 because the quotient is 2, not a multiple of 4. HYP §2(E4) already gives this counterexample.

**Fix:** call that sum the two-relation count, or retain the factor 1[4|(p+u+B)/(uB)] on the integer-quotient locus. If expanding that factor, display the resulting additional phases. State the coprime-pair restriction explicitly in the summation; noncoprime pairs have zero contribution to N for prime p, but do not make omitted conditions redundant.

### F13 — MAJOR — O3 mixes the full-pair main term with a coprime-only oscillatory expansion

**Location:** §4(O3), its noncoprime-pair sentence, and its use to motivate K(b).

The inverse ū exists only on coprime pairs. The correct coprime KF expansion has zero term Σ_(u,B)=1 1/B, not Σall pairs 1/B. “Up to non-coprime pairs” must specify the correction, which is of main-term size and is not merely their solution count.

For U=V=2,p=17, all N₁ solutions are coprime and N₁=2. The full zero term is 7/6, the coprime zero term 7/12, and the written RHS equals 2+7/12, not 2. In large balanced boxes the coprime zero term is asymptotically (6/π²)U log 2≈0.421U, not ≥U/2. Thus the exact factor 1/2 in the ordinary-additive zero-mode argument is not automatically the KF zero-mode factor.

Noncoprime reduction also requires g=gcd(u,B) to divide p; otherwise B|p+u is impossible. If g|p, reduce the numerator to p/g as well as u,B. Merely replacing u,B by u/g,B/g is not the same detector.

**Fix:** write the coprime zero mode and add the actual noncoprime solution count separately, or use the ordinary additive detector throughout. Keep K(b)'s proved ≥U/2 statement explicitly attached to that full additive detector. An order-U obstruction for the coprime implementation needs its own correctly normalized argument/hypotheses.

### F14 — MAJOR — K(b)'s one-relation ceiling is expanded beyond the proved implementation

**Locations:** K(b)'s third bullet, K(c)'s conclusion, summary 4(b), ledger, §§8–10 and proposed FRONTIER text.

The proved ceiling applies to bounds of the form

    full-additive zero mode + a nonnegative absolute error allowance.

It does not apply to all evaluations of N₁: the proof itself gives only N₁≥U/2−V, useful in the strongly skew regime, and explicitly lacks a useful balanced deterministic bound. For example U=V=2,p=19 gives N₁=0, strictly below min(U,V)/2=1. It therefore does not establish “any one-relation bound is ≥min(U,V)/2.” Nor does nonfactorability of the second indicator prove that every bilinear/trilinear method can see only one relation: decomposition of a coupling into separable pieces, further averaging, or weighted joint estimates would require analysis of their cost, not dismissal by reciprocity alone.

**Fix:** state the ceiling only for this positive-main-plus-absolute-error implementation, and distinguish exact evaluation and genuinely coupled estimates. Keep the factor-of-two comparison separate from HYP's p^{o(1)} upper-bound notation. Present the broader failure of alternative KF organizations as Assessment, not PROVED.

### F15 — MAJOR — Q's “needs varying nebentypus” and exhaustive Kuznetsov conclusion are not proved

**Location:** §6.2(iii), its title/Reading, and summaries saying “in every normalisation.”

The double-coset and conjugation bookkeeping is correct. The claim that detecting d≡−1 “needs nebentypus” is false: additive orthogonality gives

    1[d≡−1 (c)] = (1/c) Σ_{k mod c} e(k(d+1)/c),

and therefore inserts a combination of ordinary sums S(m,n+k;c), with varying indices rather than mandatory nebentypus. This may be analytically unhelpful, but it is not the asserted necessity.

Likewise a representation number for cp+1 is not the standard fixed-index Kuznetsov coefficient presented here, but the identity does not rule out Fourier/generating-function descriptions or all reorganizations across c. “One integer per level” is bookkeeping, not a theorem excluding a spectral estimate jointly in that level and integer.

**Fix:** retain Q(i),(ii) and the explicit two orientations as PROVED. Replace the nebentypus necessity by a list of possible detectors and their varying parameters. Scope the Assessment to “no direct standard fixed-index Kuznetsov application is exhibited.” Remove universal claims about every normalization or every Kuznetsov method.

### F16 — MAJOR — The determinant calculation is an upper-bound calculation, not a lower bound or exclusion of the method

**Locations:** summary 6, §7 HB row and following prose, proposed FRONTIER addition, bottom line.

From the quoted theorem one obtains

    k ≪_ε V^{2/(3√3)+ε}(log ||F||)^5,

not k≍V^{2/(3√3)} and not a statement that the method must produce that many curves. The V^ε factor is omitted in the displayed output. A weak covering upper bound does not prove that fewer curves cannot be used or that another determinant-method argument cannot improve the result.

The application should also check its hypotheses: B_i≥1, primitive projective representatives (automatic for (x,y,z,1)), and irreducibility over Q. Here irreducibility is easy: as a polynomial in z, the coefficients 4xy and −w²(x+y+pw) are coprime, so Gauss's lemma and degree one in z apply.

**Fix:** state the quoted upper bound with ε and height dependence, and say “this direct black-box application does not yield the target saving.” Do not say the determinant method necessarily produces more curves than the target or excludes a better argument. The exponent calculation itself is correct.

### F17 — MAJOR — Literature-search scope and “only ES-specific structure” are overstated

**Locations:** §§0, 7–10, especially proposed FRONTIER wording and final survivor sentence.

LIT_CHECK explicitly says the search is not exhaustive and a negative literature conclusion is not proved. “No known theorem gives one” and “no known theorem, determinant method included” are broader than the verification performed. The dimension-growth comparison is a useful benchmark, not a lower bound for this surface, nor a proof that any better result must use ES-specific structure. “The three implementations … exactly … the literature offers” is likewise an unsupported exhaustion claim.

**Fix:** say “none of the checked theorems, applied in the displayed way, gives the saving; the literature search found no such result.” Keep the dimension-growth analogy labelled Assessment. Preserve all methods not ruled out by a specific inequality, including signed weighted sums, negative-mean positivity certificates, joint-conductor arguments, and alternative spectral/determinant reorganizations. This is necessary to make the verdict “narrowed” honest.

### F18 — MINOR — E(c)'s equality criterion ignores the third coordinate

**Location:** last sentence of §5.3(c).

The Fejér inequalities E(a),(b) are valid for any finite phase multiset, and the square-root max-bound comparison is valid for an appropriate containing box. But “equals the trivial bound … exactly when the two coordinate sides are comparable” is false when the omitted third side is much smaller. For example u and B can both have scale p^{1/2} while C has scale 1: (UB)^{1/2} is p^{1/2}, while min(U,V,C̄+1) is O(1).

**Fix:** equality with the three-coordinate elementary scale additionally requires the third side not to be smaller in order. Define the containing C-box and its number of integer entries explicitly, using O(C̄+1) rather than treating an arbitrary real interval length as exactly an integer box size. Scope the ceiling to the Fejér/max-Δ implementation, as in HYP.

### F19 — MINOR — LP output is numerical evidence for a bounded-coefficient problem, not exact optimization certification

**Location:** §5.1 LP check and `scripts/z53_hypkloost_certificate_lp.py`.

The LP silently imposes −10≤c_h≤10 in addition to the stated constraints. The saved H=64, U=V=2 optimum c₀=10 visibly hits that artificial bound. Floating-point feasibility and optimality are not an exact proof of the unrestricted maximum, and the permitted G(0)=0 boundary is not a certificate as defined. These issues do not refute the reported low-degree feasibility observations or the independently repairable sharpness theorem.

**Fix:** label the LP check EVIDENCE, disclose the coefficient bounds and tolerances, and avoid calling its output the unrestricted exact maximum. If a CERTIFIED claim is wanted, supply rigorous primal/dual witnesses and check the strict G(0)>0 condition. No new numerical test is needed for sharpness once F04's proof is supplied.

### F20 — MINOR — A few numerical statements and uncertainty labels need correction

**Locations:** §3 F3, summary 4, K(b), covariance table, reproduction §11.

1. “N∈{0,2,4}” does not describe all three KF data sets: balanced KF has {0,2}; both skew files have {0,1,2}. The larger balanced conductor samples can have 4. State the sample to which the claim applies.
2. “N₁=main±17” is a standard-deviation description, not an interval bound. In `kf_bal12.tsv`, deviations run from −42.8972 to +37.1028, sd 16.8468. Write “sd≈17” consistently.
3. The stated 400-resample bootstrap CI endpoints are not reproduced by the saved analysis script; it contains no bootstrap, and neither resampling seed nor implementation is saved. Independently recomputed intervals are compatible but not identical (table below). Consecutive-prime rows also do not supply an established iid sampling model. Label these as empirical/bootstrap uncertainty estimates, not certified frequentist coverage.
4. Printed total-check columns equal N at nine decimals. Sums of the separately rounded printed bins can differ by up to 9.21·10⁻¹⁰, so the <5·10⁻¹⁰ assertion must refer to the internally accumulated total, not every reconstructed TSV-bin sum. It is floating-point evidence, not a rigorous error certification.
5. The input generators and bootstrap code are absent from the reproduction script; it describes a generator “inlined in the session.” The existing gzipped n columns preserve the actual inputs, but ranges/seeds alone are not a complete reproduction recipe. The analysis script expects uncompressed c_*.tsv, not the stored .gz names.

**Fix:** correct the sample labels and sd wording; save or fully specify bootstrap/input procedures, or document extracting the preserved n columns and decompressing the files. Retain EVIDENCE labels for floating calculations.

### F21 — MINOR — Missing integer/nonempty-set hypotheses in B and counting formulas

**Locations:** §1 notation, B's arbitrary-set extension, E and K box counts.

The exact formulas q_min=4(U+1)(V+1), q_max=16UV, |B|=UV and the harmonic sums require positive integer U,V. HYP also uses U=1/2 or V=1/2 to cover coordinate 1; those formulas do not all extend verbatim. An arbitrary finite set must be nonempty for q_min,q_max to exist, and must consist of positive-integer pairs for q to be a positive multiple of four.

**Fix:** state integer U,V≥1 in these results, treating the singleton-coordinate blocks separately or using actual minima/maxima and cardinalities. State nonempty positive-integer pair sets in B. For “all pairs of R(p),” specify a finite *candidate* set, rather than an unknown solution set; the natural feasible set 4uB≤p+u+B has q_max≈4p/3, whereas arbitrary solution subsets need not attain that asymptotic maximum.

## Proof steps and claims verified as correct (with scope)

### Exact algebra and elementary estimates

- The unweighted conductor expansion (1.1) is the ordinary additive-character identity, and grouping each pair's divisors returns its divisibility indicator.
- Ramanujan prime-power values in §3 and the C implementation are correct. The program's integer q/d bin index implements floor(log₂(q/d)) correctly.
- The O4 progression count and the O5 trial-form bijection are correct, with the 4-condition retained. In O5, m=4uC−1, u=(−p mod m)>0, and 4u|m+1 determine C and B uniquely; the inverse identity (4C)u≡1 mod m is correct.
- For positive integer U,V, q_max is attained at (2U,2V); q_min is attained at (U+1,V+1). All pair moduli are multiples of four, so q_max/2 is an integer.

### Theorem B

- The Poisson sign is correct: the transform of t↦g(t−F) is e(−ξF)ĝ(ξ). The substitution ℓ=kq−n−s gives exactly q|n+ℓ+s and weight g(ℓ/q). Periodization also proves the identity under the given decay/continuity assumptions, after correcting support as in F03.
- The half-shifted q₀/2-grid consists of (2k+1)/q₀. No point is integral, every point belongs to the q₀-grid in T, and every Fourier mode 0<|h|≤H<q₀/2 averages to zero. Thus the **positive-mean** lower-degree obstruction is rigorously correct.
- Uniform n mod q gives E G(−F)=Σ_j ĝ(jq). The H<q_min reduction to ĝ(0) is correct; only the subsequent sign inference is wrong without the extra threshold.
- The Fejér lower bound 4(H+1)/π² on |ℓ|≤q/(2H+2), and upper bound q²/[π²(H+1)ℓ²] for ℓ≠0, follow respectively from sin x≥2x/π on [0,π/2] and |sin x|≤1. They include the continuous value at zero.
- The sharp **positive-mean** threshold q_max/2 is provable for every nonempty finite positive-integer pair set by F04. The finite-set extension of Poisson and half-shifted quadrature is valid; the expectation-sign extension as written is not.

### Theorem C

- The exact full-projection identity uses Σ_{d|g}c_d(m)=g·1[g|m], g=gcd(q,M), and CRT gives conditional probability (g/q)·1[g|n+s]. Both are correct.
- The primitive-conductor lemma is sound for every q≥2, including prime powers. Each nonprimitive character is invariant under at least one subgroup H_i of order ℓ_i; assigning each Fourier term to one such subgroup gives the required decomposition. Realness can be retained by assigning conjugate characters together, though only the final sum needs to be real.
- Under CRT the chosen a_i=ℓ_i^{e_i−1} has order ℓ_i and lies in H_i. In ν=u+(−1)^{k+1}q⁻¹⊗(δ_{a_i}−δ_0), the 2^k support points are distinct; signed masses are ±1/q; ν(0)=0; all masses are 0,1/q,2/q; total mass is 1. Integration of an H_i-invariant function kills the signed tensor in its i-th coordinate. Consequently mean(f)=∫f dν≤ν(0)=0. No gap found.
- For the Ramanujan-form subclass, absence of primitive Fourier coefficients is exactly λ(q)=0.
- For q=ℓ₁ℓ₂ with **distinct primes**, the four stated constraints and objective a+b/ℓ₁+c/ℓ₂ give maximum zero. More generally the linear-program value is max(0,1/ℓ₁+1/ℓ₂−1) in the indicated two-coordinate setup. The Bonferroni point has negative objective for distinct primes, so the zero function is the actual maximizer in this case. Calling the feasible polyhedron a “cone” is imprecise (the last bound is 1), but does not affect the calculation.

### Theorem K

- B B̄+u ū≡1 modulo uB, and B+u≤B B̄+u ū<2uB with B+u>1; hence the sum is exactly 1+uB. The representative choices matter and are correctly given.
- Multiplying by ap gives the stated reciprocity of exponentials. Expanding the two coprime divisibility indicators, substituting b=a+c mod B, and collecting the linear phases yields (4.1) with exactly the displayed signs and normalization 1/(uB). This is not the 4-condition, as noted in F12.
- For the full ordinary-additive one-relation detector, Σπ1/B=U(H₂V−H_V)≥U/2. Counting a residue class inside U consecutive integers yields N₁≥Σ_B floor(U/B)≥U/2−V, and U≥4V implies N₁≥U/4. The symmetric statements are correct.
- Against the **quoted** DFI 1 expression, (U+V)min(U,V)≥UV and the (1+a/UV) factor give no saving over the norm-based trivial bound. This calculation is conditional on LIT_CHECK's transcription.
- Against quoted DFI 2, dropping ε factors gives p^{3/8}(UV)^{11/96} versus (UV)^{1/2}, hence the necessary threshold UV≳p^{36/37}, or C̄≲p^{1/37}. It is necessary, not sufficient, and power savings require slack for ε.
- Against quoted BC, the first summand alone gives ratio ≳(4C̄)^{1/2}A^{7/20}(UV)^{−1/40}. Thus 4C̄≲(UV)^{1/20}, and the weaker necessary statement C̄≲p^{1/20} is valid for nonempty hit blocks. In fact substituting UV=p/(4C̄) sharpens this to C̄≲p^{1/21}; this is an optional improvement, not a refutation of the stated weaker necessary threshold. The omitted second BC summand can only impose more restrictions.
- The numerator bp≥p is correct. In a hit block UV≲p (indeed use 4uB≤p+u+B and u+B≤2uB), so the product comparison needed for these necessary thresholds is valid. These are limitations of these displayed upper bounds, not lower bounds on KF sums themselves.

### Theorem E, Proposition Q, determinant calculation

- E(a) follows from the Fejér majorant; the sum of the nonzero weights is H, giving exactly N≤|P|/(H+1)+HΔ_H/(H+1).
- E(b)'s positive-kernel diagonal argument is independent of the phase: weighted second moment≥(H+1)|P|; subtract |P|² and use 2H terms to get Δ_H≥sqrt(|P|)/2 when H+1≥2|P|. The extension to all three displayed phase functions is valid. Dropping the third-coordinate restriction increases the count, as required for an upper bound.
- Q(i)'s determinant identity is (cu−1)(cB−1)−cp=1, equivalent to cuB−u−B=p. For c positive and divisible by four, the positivity and congruence constraints give the claimed bijection.
- At fixed positive c the standard double cosets are indexed by units d mod c, with a≡d⁻¹ mod c. Selecting d≡−1 selects the term e(−(m+n)/c). Upper-unipotent translations produce the displayed lattice of representatives.
- With w=[[0,−1],[1,0]], wγw⁻¹=[[d,−c],[−p,a]], so the lower-left entry is indeed −p. This proves the claimed orientation change, not exclusivity of all other spectral strategies.
- For F=4xyz−xw²−yw²−pw³, B₄=1 and B_i≥1, the monomial weights are B₁B₂B₃,B₁,B₂,1. Coefficient magnitude p does **not** enter T. Thus T=V=B₁B₂B₃; n=4,d=3 give (V³/T)^{1/3^{3/2}}=V^{2/(3√3)}, with 2/(3√3)=0.3849001795. The height factor is (log p)^5. With coordinate scales in a block containing a hit, V≍p. The upper-bound exponent arithmetic is correct, with F16's qualifications.
- The quoted ET and Elsholtz–Planitzer 3/5 and Type-II 2/5 bounds are transcribed consistently in the memo. They do not by themselves answer the restricted-family 1/3 question.

## Independent numerical checks

All jobs were small and memory bounded (ulimit -v 6000000), Python through `uv run --with numpy python`, with shell timeouts ≤180 seconds. The largest input array was only 3000×83 numbers. Bootstrap resampling was one draw at a time, not a giant Cartesian allocation.

The following are recomputed from the gzipped TSVs using population variances. The table values in §3 agree to the displayed rounding. The covariance decomposition is an algebraic identity; its interpretation as orthogonality is the issue.

| set | rows | Σ Var(relative bins) | Var(N) | cross share |
|---|---:|---:|---:|---:|
| p12 | 3000 | 0.2758661233 | 0.3150360000 | +0.1419887164 |
| rn12 | 1500 | 0.2567953081 | 0.2432906667 | −0.0525891284 |
| ns12 | 600 | 0.2687880709 | 0.2964888889 | +0.1030582119 |
| sq12 | 600 | 0.1750474879 | 0 | −1 |
| p10 | 3000 | 0.2605492101 | 0.2698648889 | +0.0357540088 |
| rn10 | 1500 | 0.2610353189 | 0.2712515556 | +0.0391373729 |
| sq10 | 600 | 0.1976105417 | 0 | −1 |

Total rows: 10,800, as claimed. All saved total-check columns equal the integer count at the printed nine decimals. Maximum reconstructed relative-bin rounding residual is 9.2111·10⁻¹⁰; maximum absolute-bin residual is 8.7081·10⁻¹⁰.

For p12:

- sds k=0,1,2,3: 0.30352348, 0.27397019, 0.21566105, 0.16672466;
- cumulative capture correlations k=0,…,4: 0.61467386, 0.75640286, 0.88055583, 0.93708663, 0.96634752;
- maximum sd among absolute bins j<10: 0.00286506;
- rn12 absolute-bin j=1 sd: 0.01892160;
- fraction N=0: 0.924 (consistent with the loose “≈93%” description).

An independent 400-resample percentile bootstrap, NumPy default_rng(53), processing sets in the table order, gives intervals: p12 [0.0134,0.2633], rn12 [−0.2288,0.1036], ns12 [−0.1194,0.3368], p10 [−0.0856,0.1398], rn10 [−0.2127,0.2801]. These are compatible with the memo's rough uncertainty ranges, but cannot validate its exact endpoints without its seed/procedure.

KF recomputation used columns 6 onward divided rowwise by sqrt(column 5), with zero-based indexing, and sd of column 2 minus column 4:

| file | rows | rms magnitude / sqrt(ncop) | maximum | sd(N₁−main₁) | observed N |
|---|---:|---:|---:|---:|---|
| kf_bal12 | 200 | 0.56654012 | 1.66362441 | 16.84683279 | 0,2 |
| kf_unb12 | 100 | 0.98800157 | 2.86146470 | 11.40799719 | 0,1,2 |
| kf_unb12b | 100 | 0.78602373 | 2.18652358 | 4.43016930 | 0,1,2 |

The quoted rms, maxima and sd values are correct. The balanced full-additive main is 692.8972; the two skew mains are 69.3122 and 6906.5343.

I compiled `scripts/z53_hypkloost_conductor.c` and checked U=2,V=3 at n=5,17,25,41,89,101,121,1009. An independent Python computation used the defining sum

    c_d(m) = Σ_{0≤a<d, gcd(a,d)=1} cos(2πam/d),

rounded to its integer value, rather than reusing the multiplicative code. Every divisor and both bin families were compared. Counts were 0,0,0,1,1,0,0,0; maximum printed-bin discrepancy was 4.45·10⁻¹¹. This checks the implementation on both hits and misses, but is not an exhaustive certification of every large-n run.

The saved LP numbers at H=q_max/2 (0.005311,0.001727,0.000712) agree with the memo's rounding, and visibly contradict its unconditional H<q_min expectation claim for U=V=2. The saved window-check residuals/tail bounds are consistent with the summary; they are numerical checks of the Fejér specialization, not evidence for universal finite-window information claims.

## Recommended status after repair

- **PROVED:** exact conductor/full-class projection identities; correctly formulated Poisson periodization; positive-mean half-shifted quadrature threshold with the repaired sharpness proof; primitive-conductor lemma; reciprocity (4.1) for two relations; the stated full-additive one-relation inequalities; Fejér/max-input ceiling; the two explicit SL₂ orientations.
- **CONDITIONAL on quoted literature statements:** exponent comparisons for DFI/BC and the direct HB covering upper bound, with ε losses and all hypotheses retained.
- **EVIDENCE:** data-table moments, limited-frequency KF sizes, LP/window checks and empirical bootstrap intervals.
- **Assessment only:** broader methodological limitations and negative literature-search conclusions.
- **Not established / in places false:** pointwise certificate spectrum necessities, exact orthogonality of relative bins or prime samples, exhaustion of analytic implementations, and the claim that only top-spectrum primality-dependent methods survive.

Do not paste §9 into FRONTIER before these corrections.
