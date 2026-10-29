# Hostile referee report: EXSET_DEPTH_BREAK.md, §§1–6

ES remains open. This review does not establish a depth-breaking exceptional-set estimate.

## Executive verdict

**The advertised arithmetic one-sided PD barrier is not proved.** The LP/mixture construction is substantially correct as an abstract theorem, after clarifying its domain and normalization. Its identification with “all known prime-detection/sieve information,” however, is unsupported and in important respects false. The manuscript repeatedly promotes a limitation of a particular statistic or proof format into a limitation of an entire analytic method.

The elementary reformulations, the CRT Rankin estimate, and the top-band sufficient conditions are useful. The product-form obstruction is repairable. The numerical counts checked here are correct. There is no depth-breaking theorem in §§1–6, and no demonstrated equivalence between the remaining arithmetic problem and the manuscript's proposed high-order or joint-law inputs.

### Verdicts for every §0 row

| Row | Verdict | Reason and concrete repair |
|---|---|---|
| 1 | **MAJOR** | The e/t/m identities and anti-square lemma are sound. The displayed quadratic large sieve is false without squarefree restrictions; “all positive dependence” is not what the cited source proves. Correct N3, separate arithmetic statements from model statements, and qualify the PD distribution ranges. See §1 below. |
| 2a | **SOUND-WITH-MINOR** | The displayed BT upper bound is valid, with harmless small-parameter repairs. The claimed PD cube-root moment ceiling does not follow from it. Keep the proposition and relabel/remove its “Reading.” See §3. |
| 2b | **FATAL** as an arithmetic barrier; **SOUND-WITH-MINOR** as an abstract mixture lemma | I1–I4 define a feasible abstract model, and the mixture checks work. They do not capture all actual PD inputs; exact all-clopen first moments are not available for integers, and important deterministic support information is omitted. Corollary 2.3′ does not remedy this. Restrict the theorem to explicitly specified abstract axioms and withdraw the universal factor-two conclusion. See §2. |
| 2c | **MAJOR** | Cauchy–Schwarz gives the asserted upper bound, not convergence for arbitrary laws. Sharpness holds for suitable constant-density examples, not the arbitrary measurable densities of §2.3. The displayed product needs a Haar integral in the latter setting. State an extremal existence result with its hypotheses. |
| 2d | **MAJOR** | The CRT Rankin inequality is sound. The unrestricted Haar factorial-moment asymptotic and the PD extrapolation are not established. State the range of k, use the actual Haar mean, and supply a separate weighted PD and joint-main-term lemma before asserting an oracle barrier. |
| 3a | **MAJOR**, repairable | The fixed-loss conclusion is supported by the cost estimates. The proof of (b) uses Lemma 3.0(c) outside its range and incorrectly inverts the shift cutoff. “Every shift factor must be exact” is also stronger than the common-loss hypothesis. Repair the ranges and restrict the claim to the defined product format. See §4. |
| 3b | **MAJOR** as packaged; implications **SOUND-WITH-MINOR** | The inclusions and the TB implications are correct, including U failure ⇒ A_N. “CRT-invisible,” “quadratic at level 2 log N,” and the general band citation are inaccurate. Say that one layer suffices, not that every proof needs it. See §5. |
| 3c | **SOUND-WITH-MINOR** | Independently rerun at 10^7; table agrees. The trend is evidence at three sampled scales over two decades, not three decades and not an asymptotic. |
| 3d | **MAJOR** | Largest-prime-factor size laws at two integers are not laws of their residues modulo growing 4e. A full many-shift joint law is sufficient, not proved necessary for TB. Correct the literature comparison and remove “what TB needs” as an exact characterization. See §6. |
| 4 | **MAJOR** | The Haar variance calculation is correct. It only limits direct Chebyshev on the raw count, not every L²/dispersion/large-sieve method, and not arbitrary μ(n). The anatomy discussion is not an impossibility theorem. See §7. |
| 5 | **MAJOR** | The additive-error observation is valid for a direct comparison bound. Neither an unspecified o(1) nor existing fixed-order results prove a universal O(log log N) ceiling for a technology. The asserted necessary moment order/precision is unproved. See §8. |
| 6 | **SOUND-WITH-MINOR** | The 10^7 rerun and independent 20000 brute force agree. Correct the convention excluding 1, identify the controls' moving top threshold, and print the complete histogram/overflow information. See §9. |
| 7 | **MAJOR (incomplete, administrative)** | The manuscript's review section is empty. Incorporate review dispositions rather than implying completed review. |
| 8 | **MAJOR (incomplete, administrative)** | The promised exact-gap section is empty. State the unresolved arithmetic lower-tail input without claiming that all alternatives have been excluded. |

The last two rows are placeholders outside the requested mathematical §§1–6, not refuted mathematical theorems.

## 1. Reformulations, squares, and the non-CRT inputs

### 1.1 What survives

Lemma 1.1(a)–(e) is correct, subject to interpreting (e) on its implicit integer/congruence domain. In particular, m ≡ 3 (4) follows from mℓ = n+4e ≡ 1 (4), since ℓ ≡ 3 (4). The proper-divisor condition is automatic.

An additional elementary bound should be stated explicitly. From ℓ ≥ 4e−1 and m ≥ 3,

    n+4e = mℓ ≥ 3(4e−1), so e ≤ (n+3)/8,
    ℓ ≤ (n+4e)/3 ≤ (n+1)/2.

Thus all possible hits at n ≤ N have ℓ ≤ N automatically (apart from irrelevant tiny endpoints); the unrestricted e in the definition of X_top causes no actual infinite-family problem. This also justifies the brute-force cutoff.

Lemma 1.2 is sound. Since e < ℓ, there is no missing zero Legendre-symbol case. Reciprocity gives (e/ℓ)=1 and hence (−4e/ℓ)=−1. Every odd square avoids every event. The baseline CRT upper bound transfers from the 4ℤ subfamily used in SIEVE_MASS Proposition 2.3.

### 1.2 False or overstated parts of §1

* **N3 omits the essential squarefree condition.** Heath-Brown's quadratic large sieve has squarefree summation variables, not the unrestricted sum displayed here. For example, take a_ℓ=1 at odd primes ℓ≤L and L comparable to N. On odd squares n≤N, almost all (n/ℓ) equal 1. Their contribution is of size √N·(L/log L)^2, exceeding (NL)^ε(N+L)L/log L for sufficiently small fixed ε. Even deleting squares is not the same as imposing squarefreeness: n=17b² gives repeated characters on the n≡1 (8) line. Repair by writing the squarefree theorem and separately treating square parts, with their actual loss.
* **The cited shift theorem does not show that the quadratic profile carries all positive dependence.** EXSET_SHIFT_DIVISORS §3.1 proves conditional negative dependence in a finite CRT model after conditioning on the full capped small-prime-power fibre. Remark 3.1(3) explicitly says that this does not imply negative association given only the quadratic profile. The same document says the explanation on integers is evidence, not a theorem. Correct §1.3 and the causal language accompanying the histograms.
* PD indicators for a fixed finite interval can always be represented on that interval by classes modulo a sufficiently large polynomial modulus. What is unavailable is the same **global periodic majorant/evaluation architecture**, not a literal inability to represent a finite-interval function. THETA itself warns about this distinction.
* “CRT can only certify blocks up to exp(c√λ)” is an optimal-saving statement, not a visibility cutoff. Individual primes up to exp(λ) are visible. This distinction matters again in §§3–4.

## 2. Theorem 2.3: abstract proof versus arithmetic scope

### 2.1 The LP and weak-* argument are not the main failure

First replace the notation A^CRT_λ⊆I by a separate profinite cylinder, say

    B_λ = {x∈1+8Ẑ: x avoids the finitely many event classes at ℓ≤min(N,e^λ)}.

The literal finite set A^CRT_λ⊆[1,N] is not clopen in 1+8Ẑ. The intended cylinder B_λ is clopen. The finite-quotient LP is then feasible: ν=1 is primal feasible and Haar measure is dual feasible. Including the trivial class normalizes the dual mass to one. Coefficients are unrestricted real numbers and the pointwise inequality ν≥1_B imposes both nonnegativity and majorization, as required.

For a finite collection of classes, its optimum is at least the infimum over all allowable finite combinations. The dual produces the required ρ_C. The sets of probability measures with the prescribed class masses and ρ(B_λ)≥β_λ are weak-* closed. They are a directed family with the finite-intersection property, rather than necessarily a single decreasing sequence. Compactness gives ρ. This is legitimate.

Use **inf**, or justify **min**: conditional averaging onto the finite quotient consisting of Q₀ and the squarefree slice primes in B_λ removes finer digits and irrelevant primes and preserves the allowed slice supports. The optimization can therefore be reduced to a finite-dimensional LP. This also explains why unrestricted prime powers and uncharged non-slice primes do not invalidate the abstract duality.

### 2.2 Correct THETA bookkeeping

THETA charges each distinct slice prime once, not log d. Powers of slice primes, the Q₀-primary part, and non-slice primes can occur in the test moduli. Fix the slice-prime set explicitly; do not switch silently between this level and an ordinary modulus bound.

Take Q₀=168 and move 3 and 7 into it. For the 4ℤ family, w(3)=1 and w(7)=2. Within the fibre x≡1 (8), the allowable proportion at these two primes is

    (1−1/3)(1−2/7) = 10/21.

Equivalently, R has 10 residues modulo 168; full-integer Haar density is 10/168, whereas Haar probability on 1+8Ẑ is 10/21. The constant saving is log(21/10), not log(168/10), after fibre normalization. When one of these primes is not in the horizon, impose only the relevant avoidance conditions; this changes only the bounded factor.

For ℓ≥11, write a=(ℓ+1)/4≥3. Since τ(a)≤a−1,

    w(ℓ)=τ(a)≤a−1<ℓ/4.

The classes are distinct: distinct divisors e of a cannot differ by a multiple of ℓ. Thus the local hypothesis is satisfied. BT/divisor pairing gives the weighted profile O(1/α); the truncated mass is O(λ), and s_* = log 11 is fixed. THETA's remainder is consequently O(log²(2+λ)). Optimizing gives the intended exp(−O(√λ)−O(log²(2+λ))) lower bound, including the constant 10/21. There is no uncontrolled large R-term here.

### 2.3 The mixture checks do work

For any fixed Borel r_j∈[0,1/C], define the inactive component with x∼ρ and all bits zero, and the active component of probability 1/C with x∼Haar and independent Bernoulli(Cr_j(x)) bits. Then for every clopen S,

    P(π_j=1,x∈S)=∫_S r_j dH,
    P(all π_j=1 for j∈J,x∈S)=C^{|J|−1}∫_S ∏_{j∈J}r_j dH.

I1 and I4 also follow exactly. There is no hidden error in these identities, and feasibility of these abstract axioms is proved by the construction itself.

The formal lower bound excludes universal bounds **strictly below** (1−1/C)β_λ. A model with probability ≥b does not, by itself, refute the weak inequality probability≤b. Change the corresponding “cannot prove ≤” to “cannot prove <” or formulate an infimum ceiling. This is a minor logical endpoint issue.

### 2.4 Why the claimed arithmetic theorem fails

**(i) Actual integer data are not these exact all-clopen data.** A finite empirical integer law is atomic, while r_j dH is nonatomic. Equality of their restrictions on every clopen set would imply equality of the measures. More concretely, a modulus larger than N isolates any particular n≤N. There is no SW/BV/EH theorem with exact r_j dH values on every such class.

Calling these data an unrealistically strong oracle is permissible, but then one must prove that the actual inputs being ruled out are consequences of this oracle, with specified errors. No such implication is given. “Up to their error terms” has no content without a test family, an error norm, and a quantitative allowance at the desired exceptional-set scale.

**(ii) The suggested roughness r_j is not a density for exact first moments on every clopen S.** Choose a prime q>w below the PD horizon and condition on the candidate (x+4e)/m being divisible by q. For a concrete instance, take e=1, m=3, w=5, horizon 100, and S={x≡17 (2520)}: the candidate (x+4)/3 is divisible by 7, is 3 mod 4, and is coprime to 2·3·5. On an admissible positive-measure progression the displayed r_j remains positive, while a true candidate prime above the horizon cannot be divisible by q. This is already a first-moment obstruction; it is not an unresolved high-order correlation. Local densities for fixed tests can be approximated as a roughness cutoff tends to infinity, but there is no single finite-cutoff density giving uniform all-clopen prime data. Also, r_j≤1/C and positivity of log(N/m_j) require a candidate-size range; they are not automatic for the complete PD indexing set.

**(iii) Known deterministic relations go beyond I4.** The sentence “None is known” in §2.3(d) is false. For a fixed shift e there is at most one prime divisor above √(2N). Distinct PD cofactor bits for that shift are mutually exclusive in the top band. More generally, two different representations sharing the same candidate prime or the same shifted integer satisfy divisibility and size constraints. The roughness support only excludes small factors; it does not encode all these relations. For example, coprime cofactors m,m′≡3 (4), both w-rough, have compatible congruence classes; on suitable rough fibres the model can assign both bits 1, whereas simultaneous primality forces the candidates to equal the opposite cofactors and fixes n+4e=mm′. Taking mm′<e^λ excludes this completely for above-horizon events. These are elementary relations, not a new theorem about ES.

The authors may intentionally omit these inputs, but the conclusion must then be: **arguments using only I1–I4 fail**, not “PD information fails.” Adding deterministic exclusions may require a different joint law in the active component and a new feasibility proof.

**(iv) Prime detection uses more than unweighted first moments plus tuple upper bounds.** Weighted Type I/II identities, signed cancellation, switching, interval restrictions, sums over parameters, and exact zero correlations are not classified by the stated axioms. BV and BFI should not be declared harmless for every nonlinear use merely because one application counts primes in an AP.

In §2.1, the prime range is x≈N/m. A BV range is governed by x^{1/2} (with its logarithmic losses), not N^{1/2} uniformly in m. Siegel–Walfisz concerns small logarithmic moduli and appropriate x-ranges. The simultaneous mod-8 condition and any test S also change the relevant modulus. Correct these before assigning arithmetic meaning to I2.

### 2.5 Constants and Corollary 2.3′

The comparison with 2 is plausible for specified classical generic upper sieves, but the universal wording and the claimed 3.39 floor are false.

* **A concrete counterexample to “every published upper bound has K₂≥3.39”:** Lichtman, [arXiv:2309.08522, Theorem 1.1](https://arxiv.org/html/2309.08522), proves π₂(x)≤(3.2290+o(1))Π₂(x), with Π₂ explicitly the Hardy–Littlewood prediction in (1.1). I verified the theorem and normalization in the source; it is also recorded in `sources/lit2026f/lichtman-2309.08522-excerpt.txt`. This still exceeds 2, so it does not alone defeat the abstract C=2 comparison, but it directly falsifies the literature assertion.
* Constants must be relative to the full Hardy–Littlewood singular-series main term, not to a differently normalized twin-prime constant. I checked the local source `sources/window3/0705.1652.txt`: Wu defines Π(x)=2∏_{p>2}(1−1/(p−1)²)x/log²x and proves π₂(x)≤3.3996Π(x), Theorem 3. “3.39” is not a valid rounding-down upper bound. Chen's historical figure in that source corresponds to 7.8342/2=3.9171. The rough historical comparison still puts these constants above 2.
* `sources/lit2026/audit-tao-254a-notes4-sieve-theory.md`, equations (39) and Exercise 36, gives 2^k k! and the alternative 4^{k−1}(k−1)!, with 2^{k−1}(k−1)! under EH. These do satisfy the relevant ≥2^{k−1} comparison. They do not establish a universal lower bound on every published tuple estimate, nor uniformity for growing coefficients, k, and all clopen S.
* Inadmissible or algebraically incompatible pairs have exact upper bound zero. Averaged tuple problems can have substantially better information than the worst individual tuple constant. Neither is captured by replacing every actual estimate with a generic large K_k.
* A global singular-series upper bound does not automatically imply I3 localized to every S with the proposed finite-roughness product density. That is a separate, false-as-stated transfer.

Repair: formulate a corollary for an explicitly chosen collection of generic upper bounds **provided they have precisely the I3 form and the specified errors**, and keep the factor two confined to that abstract information set. Delete “every published” and “all sieve upper-bound information.”

### 2.6 Sharpness and novelty

Proposition 2.4's Cauchy–Schwarz inequality is correct. For variable r_j(x), however, the mixture gives

    P(R=0)=1−1/C+(1/C)∫∏_j(1−Cr_j(x))dH(x),

not the unintegrated product in the manuscript. Divergence of ∑∫r_j does not force the integral to vanish. For example r_j=(1/C)1_B on a fixed Haar-half set gives μ→∞ but retains an additional 1/(2C) zero mass. Nor does I3 imply the scalar bound E R(R−1)≤K₂μ² without control of ∫(∑r_j)².

Sharpness is easily salvaged as an **existence statement**: take constant small r_j with ∑r_j→∞ and C=K₂. To satisfy every higher-order axiom with that C also requires K_k≥K₂^{k−1}; the original general sequence of K_k need not satisfy this. In general the activation parameter is limited by all orders, not just the pair constant.

Novelty is limited but not zero. G1/THETA already supplies the CRT comparison law; EXSET_ARITH_JANSON_OPUS §3 already explains LP duality and the collapse of pointwise-certified chains. DISCOVERIES (D)22 concerns prime-supported CRT majorants under unit-measure evaluation, not these additional arbitrary bits. The zero-inflated mixture is therefore a distinct elementary abstract extension, not literally the same theorem. But it does **not** establish a strictly larger arithmetic barrier than z50 until its arithmetic inputs and support are justified. The claimed campaign advance presently rests on that unproved identification.

## 3. Exchange rate and factorial moments

### 3.1 Proposition 2.2

The BT proof of the displayed upper bound is essentially correct. Under 4em≤e^λ≤N/e, one has q=4e<x=(N+4e)/m and x≤2N/m. Dropping the mod-8 restriction and lower prime cutoff only increases the count. Summing 1/(mφ(4e)) over the triangular range is O((1+λ)²). The claimed bound follows for λ≥1 and sufficiently large N.

The comparison “CRT mass ≫λ” is an asymptotic statement, not literally uniform starting at λ=1: e^1<3, so the CRT mass is zero there. Require λ≥λ₀ or use an appropriate additive constant.

This proves an **upper bound** for available PD first-moment mass, not a two-sided exchange rate and not a theorem about all moment methods.

### 3.2 The cube-root statement needs a different lemma

A heuristic derivation is possible: if a weighted PD profile is O(1/(α² log N)), and compatible k-tuples have product-law main terms, then Rankin and 1/k! give, at α≈k/log N,

    F_k^PD ≲ (C log N/k³)^k.

This explains the cube-root scale. Proposition 2.2 alone does not provide these premises. It bounds cumulative mass by λ²/(log N−λ), which degenerates near log N; it does not directly give the asserted global Laplace-transform bound with denominator log N. One can split at, say, λ=(log N)/2, use the proposition below it, and separately bound the tail, but the manuscript does not do so. The PD profile also depends on its horizon, whereas a clean Rankin calculation should fix the event family first and then vary the cost cutoff.

Most importantly, actual intersections are not products of their marginal densities. Singular factors, common congruence factors, repeated candidate primes, incompatible tuples, and least-common-multiple rather than product moduli require attention. A numerical first-moment cost calculation cannot be a universal ceiling for Bonferroni, a weighted sieve, or an HL oracle.

### 3.3 Lemma 2.5's CRT core

For distinct slice primes the coefficient of degree k in ∏_ℓ(1+w(ℓ)ℓ^{−1−α}z) is at most (∑w(ℓ)ℓ^{−1−α})^k/k!. Rankin therefore proves exactly the first display. At α=k/L, for the nonempty range k≤L/log 3, Stirling's elementary lower bound yields

    F_k(L)≤(Ce²L/k²)^k.

Above the nonempty range F_k=0. This supplies the omitted α≤1 check and proves the exponential smallness for k≥C′√L.

The Haar factorial moment should be written in terms of μ_N=∑_{ℓ≤N}w(ℓ)/ℓ. An approximation μ_N^k/k! requires a range, for example k=o(μ_N), in which repeated-prime collisions are negligible; it is certainly false for arbitrary k, since the elementary symmetric polynomial eventually vanishes. The manuscript's empirical C₄ should not silently become a proved asymptotic constant without a citation or derivation.

Finally, small level-N content of these particular moments does not classify every possible PD oracle argument. The sentences “even an exact HL oracle ... leaves the exponent at 1/2” and “the needed objects are the full factorial moments” are unsupported. Also the moment order needed to obtain saving M is not universally ≍M: with mean μ≫M, central-moment bounds of the form (Ck/μ)^{k/2} can save M with k of order M/log(μ/M). For fixed δ>0 this still exceeds √log N when M=(log N)^{1/2+δ}, but it refutes the sharper necessity language.

## 4. Lemma 3.0 and Proposition 3.1

### 4.1 Cost estimates

(a) is correct. Primes n+4e in the fixed odd class 1+4e mod 8 cannot be event primes since they are 1 mod 4. PNT in the two fixed classes 1,5 mod 8 gives ≫N/log N primes in (4e,N+4e], uniformly for 4e≤N/2. For instance the common subinterval (N/2,N] is available. Thus cost(e)≤log log N+O(1).

(b) has the right conclusion. The elementary progression count is ≤1/ℓ+O(1/N). For q≤ℓ≤q² the harmonic progression sum is O((1+log q)/q); beyond q², BT and partial summation give O((1+log log N)/φ(q)). If q²>2N, the second piece is empty, not a negative logarithmic difference. The rounding sum is O(1/φ(q)) since q≤N/2 and BT at 2N has log(2N/q) bounded below.

(c) is repairable as written. Split at **16E²**, not E², so that ℓ>(4e)² really holds for every e≤E. The low piece is O(log(2E)) by divisor pairing and BT for ∑τ((ℓ+1)/4)/ℓ. The high piece contributes O((1+log log N)∑_{e≤E}1/φ(4e)). Include the rounding contribution from (b), which is O(log(2E)). This proves the claimed bound for E≤N^{1/3}, with minor endpoint adjustments.

### 4.2 Fixed loss

For any fixed C>1, a contributing shift must have hit probability >1−1/C. The standard lower bound φ(q)≫q/log log(3q) confines these shifts to e≪_C L₂L₃ (a loose bound is enough). Each has cost O(L₂), giving O_C(L₂²L₃). All relevant shifts satisfy e≤(N+3)/8 by §1, so the stated range covers them except for a bounded harmless endpoint. This conclusion is correct for the **defined** product format.

It does not follow that every Nair–Tenenbaum/Henriot/Shiu application has that format. The manuscript gives no theorem translating their global constants and local singular factors into factors C_e≥C>1 multiplying the actual marginal probabilities. Likewise the blanket claim that every such proof becomes a capped CRT majorant after its first step requires a theorem, not a description of one common implementation.

### 4.3 Small common loss

Assume 0<ε≤1 and put a=log(1/ε). The cutoff inversion in the proof is inaccurate. A bound resembling

    e≲ε^{-1}(log e+L₂)log log(3e)

gives log E₀≤a+O(log(a+L₂)+log log(a+L₂)), not a+O(L₃+log L₂) uniformly in ε. Furthermore E₀ need not be ≤N^{1/3}, the stated domain of Lemma 3.0(c).

These gaps can be repaired without changing the order of the final bound. Apply (c) up to N^{1/3}; for the remaining e, Lemma 3.0(b) makes every individual hit probability o(1), so cost(e)≤2·hit(e). Summing hits over all e is the mean total event count, O(log N). One elementary proof of this latter bound swaps back to primes and uses

    ∑_{ℓ≤N}w(ℓ)(1/ℓ+O(1/N))=O(log N).

If the cutoff extends past N^{1/3}, its defining inequality forces a of order log N (up to lower-order logarithms), and this total O(log N) is already absorbed by O(L₂a). In the remaining range the extra logarithms in the correct cutoff inversion are absorbed by O(L₂a+L₂²L₃). Supply these details.

Consequently a saving M≫L₂²L₃ under a **common** factor 1+ε requires a≳M/L₂, as asserted up to constants. It does not mean that every actual shift estimate must have that accuracy: heterogeneous losses, selected shifts, conditioning, and non-product estimates are outside the proposition. Change “every shift factor must be exact” accordingly.

## 5. Top-band reduction and CRT visibility

Lemma 3.2's inclusion and Hölder inequality are correct. They prove that **one sufficiently strong layer is sufficient**. They do not prove that an arbitrary successful argument must find such a layer; combined information can be stronger than every individual layer. Even a full Mertens-product upper bound need not logically require near-independence of all layers if some other input proves a stronger estimate.

Corollary 3.3 is correct after spelling out the finite-family bounds from §1. A hit counted by X_top has e≤(n+3)/8 and ℓ≤(n+1)/2≤N, so it really is an A_N event. Conversely, every event prime >√(2N) is the unique large prime factor of its shifted integer, since n+4e≤(3n+3)/2≤2N for n≥3.

A U-failure at n≡1 (8) cannot lie in any of these valid prime-pivot U certificates; thus it lies in A_N. This is the correct inclusion direction even though A_N is larger than the full-family avoider set. The n≡5 (8) input, with its finite exceptions, then gives

    #U-failures = #odd squares + O(N^{1−c}) + O(1)

under TB_pow. The claimed ES₅ consequence follows in the domain of the cited E_ES₅≤E_U comparison. Specify that domain (in particular if E_ES₅ counts primes), rather than suggesting squares must be ES₅ failures.

The CRT-band language needs correction:

* With ℓ>√(2N) and level λ=log N, an allowed term contains at most one band prime. The band is **linear**, not invisible. SIEVE_MASS 2.2(c)(iii) gives a bounded saving, tending to zero if its max p_ℓ tends to zero.
* At λ=2 log N, up to **three** such primes can fit; four cannot. It is not a quadratic polynomial class. The cited source itself explicitly says “up to three.” The name quadratic band refers to the associated Selberg-square scale, not an assertion of degree two for every nonnegative majorant.
* For a general band beginning at N^{1/4}, level log N already permits up to three primes, and level 2 log N up to seven. The stated “linear ... quadratic” sentence is false for that general band.
* SIEVE_MASS's displayed band bound contains E(λ). One cannot simply discard it in a quotation. For a fixed-width logarithmic band one can redo THETA's Boolean argument with s_* comparable to log N, giving O(1) groups and E=O(log(2+μ)); or partition into a bounded number of bands. That proves the intended O(log(2+μ)) order, but must be written.

Use “too expensive for exponential-in-mass CRT savings at polynomial level,” not “CRT-invisible.”

## 6. Literature and the claimed requirements of TB

I checked the actual local OpenAI manuscript rather than relying on its title. The source is

`/home/pasky/projects/math/oai-math/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/sections/introduction.tex`.

Its main theorem claims ordinary natural-density independence of the normalized **sizes** of P⁺(n),P⁺(n+1) for fixed thresholds a,b∈(0,1). Its introduction explicitly disclaims a quantitative error and growing-parameter uniformity. Calling this an unrefereed release and describing its iterated-limit character is appropriate; it should not be treated as independently certified by this review.

Teräväinen, [arXiv:1710.01195, Theorems 1.11 and 1.14](https://arxiv.org/html/1710.01195), does prove the corresponding logarithmic-density statement. That attribution is correct.

There are two Tao–Teräväinen results to distinguish. The 2019 almost-all-scales work gives the qualitative ordinary-average comparison outside an exceptional set. The relevant genuinely quantitative source is [arXiv:2512.01739v2, Theorem 1.8](https://arxiv.org/html/2512.01739v2), *Quantitative correlations and some problems on prime factors of consecutive integers*. Its statement gives the consecutive smooth-number law, uniformly in u,v≥1, with a power-of-log error outside a small exceptional set of scales. Cite this explicitly. The manuscript's phrase about exceptional scales is correct, but “known only with o(1) errors” understates the quantitative result unless it means uniformity at **all** scales.

None of these results is a law of

    P⁺(n+4e) modulo 4e

uniformly over a growing family of e. Size thresholds do not determine these residues. Thus the cited two-shift results are useful analogies, not k=2 cases of the exact TB input asserted here.

The claim that TB “needs” the full joint law at exp(M) shifts with precision exp(−M) is not proved. A direct bound for the zero event, a suitable exponential moment, a weighted witness, or an aggregate signed moment estimate could suffice without reconstructing that joint law. The number of shifts needed to collect mass in a particular selection strategy is not the number of coordinates whose entire joint distribution must be evaluated. Replace this claim by a clearly stated **sufficient hypothesis**, or leave it as a research heuristic.

The short-interval comparison needs its limiting regimes:

* Gallagher's Poisson conclusion is conditional on a suitable Hardy–Littlewood tuple hypothesis and is classically for fixed λ in H=λ log X. Uniformity for λ→∞ and for exponentially small zero probabilities is additional; it does not follow from the fixed-λ statement.
* The quoted RH/Selberg exceptional-interval bound O(X log²X/H) is a standard weak form in the appropriate short-interval regime. It is only a polylogarithmic saving when H is polylogarithmic. For H=X^θ the same formula is a power saving. At H=λ log X with fixed λ it is not even nontrivial. State the range rather than attaching “only polylogarithmic” to the bound universally.
* No reduction from TB to a prime-gap theorem is proved. “Beyond RH-type technology” must remain analogy, not a barrier.

## 7. Proposition 4.1 and anatomy

For constant centering μ=E_H X, the variance formula is correct. At a given prime at most one of the forbidden classes is hit, so the prime's contribution is Bernoulli(p_ℓ), and different primes are independent under Haar. Here p_ℓ≤1/2 even at 3 and 7. Therefore

    Var_H X = ∑p_ℓ(1−p_ℓ) ≥ μ/2.

The **numerical RHS obtained by applying raw Chebyshev to this X** is consequently at least a constant times N/μ. This does not establish a lower bound on the actual number of zeros, and it does not limit all L² methods. One may apply L² to a weighted count, a sieve weight, a nonlinear transform, a localized or conditioned family, or a bilinear error term whose cancellation is stronger than raw variance control. Such methods are not classified here.

The displayed generalization to arbitrary μ(n) is false. On any finite sample with integer X, taking μ(n)=max(1,X(n)) makes the numerator count exactly the zeros, with denominator one if a zero exists. The resulting RHS can be much smaller than N Var(X)/(EX)². This is not an effective proof method by itself, but it disproves the asserted universal inequality. Restrict the proposition to constant centering or impose and prove the necessary restrictions on the predictor.

Also, exact averaged binary information Var X≈μ already gives a 1/μ bound. It cannot then be replaced without explanation by the C=2 mixture, whose second factorial moment is of order 2μ². The last sentence of §4.1 conflates exact second moments with the weaker one-sided tuple inputs of Theorem 2.3.

The bilinear identity is right, but its PD notation must be consistent: §2.1's events include only primes above e^λ, whereas §4 sums to the full X. Either remove that cutoff there or add back the CRT contribution.

The anatomy split

    P(X=0)≤P(C≤K)+P(X=0,C>K)

is a tautologically valid research plan. A large candidate count plus a prime probability heuristic is not a lower-tail theorem. Conversely, failure of the crude split to prove the target is not a barrier to anatomy, and Theorem 2.3 cannot be applied to the selected set {C>K} without representing that selection and its correlations in the model. “CRT sees only words with moduli≤T” again confuses optimal collective saving with literal visibility. Relabel the entire blocking discussion as a limitation of this particular implementation, not an exact theorem about the approach.

## 8. Entropy decrement and additive errors

Lemma 5.1 is correct if “certifies” means using only the direct upper bound

    P(X_B=0) ≤ P_model(X_B=0)+η.

The RHS is at least η, so it cannot itself yield a saving greater than log(1/η). It is not a lower bound on the true probability, and it does not preclude combining this comparison with other information.

An unspecified o(1) says nothing about log(1/η): exp(−√log N), for example, is o(1). For a specific theorem with η=(log N)^{−c}, direct substitution indeed gives O(log log N); a qualitative theorem gives no explicit rate. List the actual error available in each proposed application rather than turning the notation o(1) into a quantitative obstruction.

Existing bounded-order MRT/entropy estimates do not directly yield the required many-parameter lower tail. That is a reasonable literature assessment. It is not a proof that all refinements, amplification schemes, or averages of this type have that ceiling. The recent Tao–Teräväinen paper itself illustrates a growing-dimensional sieve and nontrivial manipulation of bounded-order information, albeit for a different problem; “all treat bounded k” needs to be confined to the specific correlation theorem being cited.

The final “exact blocking statement” is not exact: neither the full exp(M)-shift law nor per-moment relative precision exp(−M) has been shown necessary. Bonferroni needs control of a particular weighted alternating error, not necessarily uniform relative accuracy of each term. Delete the necessity language.

## 9. Independent computation and table audit

All shell runs used `ulimit -v 8000000` and explicit `timeout`; scratch files are in `/tmp/dbreak_review_0046/`. No large Cartesian-product allocation was used. The C rerun at 10^7 uses roughly tens of MB, not GB. The independent Python check uses a smallest-prime-factor array only through 40000 and streams the (n,e) loop.

### 9.1 Decisive reproduction

Compiled with:

    gcc -O2 -Wall -Wextra scripts/z51_dbreak_sieve4.c -lm \
        -o /tmp/dbreak_review_0046/sieve4

Ran with a 120-second timeout:

    /tmp/dbreak_review_0046/sieve4 10000000 4472

Here 4472=floor(√(2·10^7)). The complete stdout is **byte-for-byte identical** to `data/z51_dbreak/sieve4_top_N10000000.txt`; stderr is empty. In particular:

| Quantity | Recomputed value |
|---|---:|
| non-squares sampled | 1,248,419 |
| all-family non-square avoiders | 2,457 |
| odd square avoiders, excluding 1 | 1,580 |
| top-band zero count, non-squares | 47,988 |
| mean top-band hits | 3.533968163 |
| top-band zero probability | 0.038439018 |
| exp(−mean) | 0.029188860 |
| ratio | 1.316907142 |
| zero probability given small-layer avoidance | 2457/29200 = 0.084143836 |
| top-band variance/mean | 1.104832863 |

### 9.2 Independent arithmetic implementation

I wrote `/tmp/dbreak_review_0046/check.py` independently of the supplied event-generation code. It factors every n+4e for n=9,17,…≤20000 and 1≤e≤(n+3)/8, retaining prime factors satisfying 4e | ℓ+1. It finds exactly **160 avoiders, including 70 squares**, and the entire avoider list agrees with the stored cross-check file.

With the fixed top cutoff √40000=200, the independent non-square histogram is

    r:      0    1    2    3    4   5   6  7
    count: 483  771  601  347  165  50  11  1.

A separate C run at N=20000,Y=200 gives exactly this histogram and 90 non-square all-family avoiders. This cross-check tests multiplicities and the top band, not just the final avoider set.

### 9.3 Higher-scale table arithmetic

Recalculation from the stored histograms gives:

| N | mean top | P(top zero) | Poisson ratio | var/mean | P(top zero given small avoidance) |
|---:|---:|---:|---:|---:|---:|
| 10^7 | 3.533968 | 0.0384390 | 1.31691 | 1.10483 | 0.0841438 |
| 10^8 | 4.251019 | 0.0197458 | 1.38570 | 1.11665 | 0.0460780 |
| 10^9 | 4.988812 | 0.00980839 | 1.43950 | 1.12330 | 0.0236373 |

These support the printed rounded tables. I did not independently rerun the 10^8 or 10^9 sieve. The quoted endpoint log-log slope is approximately −0.297. The range 10^7–10^9 spans **two** decades, sampled at three scales.

The control JSON agrees with the manuscript's tabulated stored values. Note that the controls script defines “top” using √(2n), while the census uses √(2N) at a fixed global N. Label this distinction; those control counts cannot be compared directly with a fixed-N top-band count.

### 9.4 Certification qualifications

1. The scripts exclude n=1. Thus the literal A_N defined with positive n≤N has 161 avoiders at N=20000, including 71 odd squares; the stated 160/70 counts are for n>1. At 10^9 there are 15,811 odd squares including 1, not 15,810. Non-square counts are unaffected. Make the convention global or restore 1 in square/total counts.
2. `cntL` saturates at 255 and the printed histogram stops at r=39. This is harmless for the checked small/top-band runs but should be certified, not assumed. In `sieve4_N1e9_Y1000.txt`, the printed histogram sums to **124,984,188**, one less than the reported 124,984,189 non-squares. At least one observation is omitted from the histogram. Its effect on the rounded variance is negligible if modest, but the saved histogram is not a complete exact distribution. Print all bins, overflow count, maximum, and exact first/second sums.
3. The squares script checks selected odd squares; the large sieve loop checks every square in its run. Distinguish those statements.
4. A variance/mean near one and a visually Poisson-like histogram do not certify an exponentially small lower tail at future scales. The observed excess and its proposed quadratic-profile cause remain evidence/assessment.
5. Sections 4–6 contain literal escaped strings such as `\u00b2` and `\u03bc`; render the actual mathematical characters before circulation.

## 10. Is there an obvious missed depth-breaking route?

**I do not have an unconditional route giving exponent >1/2 for #(A_N minus squares).** Nothing in this report supplies one. In particular, a strong result for the larger U certificate family does not automatically bound this larger 4ℤ-prime avoider set; that would reverse an inclusion.

There are, however, obvious routes **not excluded by this manuscript**, and its conclusions should leave them open:

* Encode elementary prime-factor exclusivity and size constraints before applying a PD moment/dual argument. A correct barrier would need a comparison law preserving these constraints and the actual arithmetic test family, not independent active bits.
* Work with an optimized weighted incidence count W(n), with W(n)=0 on A_N, rather than the raw X(n). To prove the target it would suffice to obtain an appropriately strong lower-tail or exponential-moment bound for W; raw Var(X)≈EX is not an obstruction to that. An actual construction and estimate remain missing.
* Seek a signed aggregate moment estimate or direct zero-event majorant. Such an input could be weaker than uniform HL at every tuple and weaker than a full joint law of all largest-prime-factor residues. The existing rank-one mixture does not classify all such arithmetic information.
* Use quadratic characters only with the correct squarefree/square-part treatment, and prove an ES-specific forcing or confinement statement. The displayed quadratic large sieve cannot substitute for that missing implication; it does not turn avoiding the sparse forbidden classes into quadratic-residue confinement.

These are concrete gaps in the claimed exclusions, not proposed proofs. The honest repaired conclusion is: the elementary CRT/product and raw-moment implementations examined here do not beat the known exponent; top-band lower-tail control is a sufficient open target; the scope of more general PD, weighted dispersion, and arithmetic amplification remains unresolved.

## Recommended disposition

Retain the verified numerical section, elementary event identities, repaired product-format obstruction, and abstract LP/activation lemma. Withdraw Corollary 2.3′ as a universal arithmetic claim, restrict the L² proposition, and change the “exact blocking” statements to scoped assessments. Only after specifying genuine arithmetic inputs, error budgets, and deterministic support should the document claim a new barrier beyond z50.
