# Hostile referee report, round 2: EXSET_DEPTH_BREAK.md

ES remains open. No depth-breaking exceptional-set estimate is established here.

## Executive verdict

**Substantial repairs succeeded, but the claimed arithmetic interpretation of Theorem 2.3 is still false.** Roughness to the horizon fixes within-shift exclusivity; restricting I2 to THETA level does **not** fix its first-moment interpretation. THETA level is not a bound on the modulus or on its prime factors. An explicit level-zero progression below has identically zero true prime count and positive proposed density.

The abstract LP/activation theorem survives. The new Theorem 2.6 is sound **as the intended class-constant model theorem, conditional on the cited KARY/EK framework**, after minor but necessary corrections: specify its different level convention, refine the word classes, and correct a block constant. Its arithmetic analogue remains open; it does not rescue the arithmetic assertions surrounding Theorem 2.3.

The repaired product-format obstruction, top-band implications, and numerical arithmetic survive. Several residual sentences still promote a particular sufficient input or implementation into a necessary one.

### Verdicts for every §0 row

| Row | Verdict | Concrete disposition |
|---|---|---|
| 1 | **SOUND-WITH-MINOR** | Squarefree large sieve and dependence qualifications are repaired. In N1, replace the false identity for a fixed `E_{ℓ,e}` by an identity for `⋃_ℓ E_{ℓ,e}`. Keep distribution ranges in the candidate variable `N/m`. |
| 2a | **SOUND** | BT bound and the explicitly hypothetical depth reading are now properly separated. |
| 2b | **MAJOR** | Abstract theorem sound; the assertions that I2 matches true level-λ prime data and covers BV/SW arguments remain false. Delete that transfer or supply an actual modulus-bounded test family, correct main terms, and an error ledger. The counterexample in §2.2 is fatal to the present arithmetic transfer, not to the abstract construction. |
| 2c | **SOUND-WITH-MINOR** | Existence/sharpness repair works, but the finite factorial moment is `K₂ μ²(1−1/|𝒥|)`, not exactly `K₂ μ²`. |
| 2d | **SOUND** | Rankin inequality, empty range, and restricted Haar asymptotic are correct. This is not an oracle barrier for arbitrary moment methods. |
| 2e | **SOUND-WITH-MINOR** | Valid for the intended CH model given KARY/EK. Charge all primes above W in `level(S)`, refine W1/W2 classes, replace `2K·4^i+4` by `4K·4^i+4`, and expand the supply/concentration justification. No arithmetic consequence follows. |
| 3a | **SOUND-WITH-MINOR** | Lemma 3.0(d) fixes the large-cutoff case. The proof should retain the inexpensive small-shift contribution in that case. The subsequent `≍ L₂L₃` count of costly shifts is not proved by an upper bound; replace it by `O(L₂L₃)`. |
| 3b | **SOUND-WITH-MINOR** | Inclusions and revised band bounds are correct. Make the ES₅ domain explicit (in particular, exceptional primes for the cited comparison), rather than referring to an unspecified domain. |
| 3c | **SOUND-WITH-MINOR** | Stored new rows reproduce. The §0 range “1.4–1.5” omits the 10⁷ value 1.32; use 1.3–1.5. These are finite-scale observations. |
| 3d | **SOUND-WITH-MINOR** | Literature distinctions are repaired. The “sufficient hypothesis” still needs a target joint law, a norm, and a zero-probability/mass condition; merely specifying a number of residues and a precision is not a hypothesis. |
| 4 | **SOUND-WITH-MINOR** | Haar/raw-Chebyshev statement is correct and properly restricted. The cited numerical variance ratios are for large layers, not the full raw count X; label them accordingly. |
| 5 | **SOUND-WITH-MINOR** | Additive-error lemma and qualitative-rate correction are sound. Restrict the remaining moment-order necessity sentence to the particular central-moment bound displayed, not “moment arguments” generally. |
| 6 | **SOUND** | Stored histograms, overflow repairs, and conventions pass the checks described in §7. This review checks stored high-scale data, not a new high-scale sieve execution. |
| 7–8 | **MAJOR** | Review record is populated, but it overstates completion of the I2 repair. In §8 replace “cannot touch” and “product forms are useless” by the actual quantitative/scoped conclusions; remove the suggestion that above-cap correlations are the only correlation route left. |

## 1. Disposition of the round-1 repair list in §7

1. **Theorem 2.3: partially repaired.** `B_λ` versus `A^{CRT}_λ`, infimum/finite quotient, compactness, the strict endpoint, and the `10/21` fibre factor are correct. The smooth-cofactor restriction and horizon roughness really give (α) and (β). The I2 restriction does not have the advertised arithmetic effect; see §2.
2. **Corollary 2.3′: substantially repaired.** Lichtman's 3.2290 and Wu's 3.3996 have the stated full-Hardy–Littlewood normalization. The conditional I3 corollary is valid. Replace the remaining “every pair constant in the literature” by “the listed generic twin-prime constants”; no exhaustive literature theorem is established, and these constants do not supply localization to I3.
3. **Proposition 2.4: repaired up to a new finite-size equality error.** The integral and existence formulation are right. Correct the missing diagonal subtraction.
4. **Lemma 2.5: repaired.** The range and the `k=o(μ_N)` qualification are adequate; the unconditional PD/oracle extrapolation is gone.
5. **Lemma 3.0 / Proposition 3.1: repaired at theorem level.** The split at `16E²`, corrected logarithmic inversion, and total-hit bound resolve the former gap. Remaining issues are bookkeeping and the overstrong “Reading.”
6. **§3.2: substantially repaired.** Linear visibility, three-prime degree at `2 log N`, sufficiency rather than necessity, and the literature distinctions are correct. The prose sufficient hypothesis is still underspecified.
7. **§4: repaired.** Constant centering and the anatomy-plan qualification cure the prior major errors. Do not use large-layer data as full-count data.
8. **§5: substantially repaired.** `o(1)` is no longer treated as a numerical rate. A residual sentence still claims a necessity for all moment arguments rather than one bound.
9. **§1.3: repaired.** Both squarefree summation variables are now present, and quadratic-profile dependence is labeled heuristic rather than a theorem.
10. **§6: repaired in the checked files.** The missing high bins are present, totals agree, and the `n=1` and moving-control-threshold conventions are explicit.

Theorem 2.6 is new, not a repair of a round-1 theorem. Its model-only qualification is important and should remain prominent.

## 2. Theorem 2.3: support succeeds, arithmetic first moments do not

### 2.1 (α), (β), and the size of the density

Put `z=e^λ`. On the support of `r_{e,m}`, for each prime `q≤z`,

    v_q(x+4e) = v_q(m).

Indeed, division by m is well-defined on the divisibility cylinder, and the quotient is a q-adic unit. Every prime factor of m is at most z because `4em≤z`. Thus m is exactly the finite z-smooth part of `x+4e`. Two distinct m for the same e have disjoint supports. This works on the profinite space, not only on integers. Consequently I4 really does imply the stated within-shift exclusivity.

Likewise, if `ℓ′≤z` divides `x+4e` on this support, then `ℓ′|m`. This proves (β). No assumption of coprimality between e and m is needed.

The assertion `r_j≤1/C` can be justified uniformly, but the proof should be supplied. For a nonempty class, let

    Q = lcm(8,4e),    h = ℋ(class_j) = 8/(mQ).

Under Haar conditional on this class the candidate is uniform in one reduced class modulo Q. Therefore its roughness probability is

    R = ∏_{p≤z, p∤Q}(1−1/p) ≍ Q/(φ(Q) log z),

since every prime factor of Q is at most z. BT, `mQ≤2z`, and `#I≍N` give

    #E_j/#I ≪ 1/[m φ(Q)(log N−λ−O(1))].

Dividing by `hR` yields

    c_j ≪ λ/(log N−λ−O(1)).

Choose `c_C>0` sufficiently small and N sufficiently large. Empty congruence classes and zero-count events should explicitly be assigned `r_j=0`; their proposed normalization alone does not uniquely define c_j. These details do not obstruct the abstract theorem.

### 2.2 Explicit counterexample to the repaired I2 interpretation

The manuscript says that for **every class S of level ≤λ**, the Haar integral vanishes exactly when the true count does and otherwise has the true SW/BV main term. This is false.

Take `z=100`, `j=(e,m)=(1,3)`, and

    S = {x ≡ 905 (mod 2424)},       2424 = 8·3·101.

Then `S⊆1+8Ẑ` and `S⊆class_j` (`905≡5 mod12`). The candidate on S is

    (x+4)/3 = 303 + 808t.

It is divisible by 101 and is 3 modulo 4. It can never be prime: the only possible prime divisible by 101 would be 101 itself, which is 1 modulo 4. Thus the true PD count on S is identically zero, for every N.

But S meets the roughness support in positive Haar measure. For example,

    x=32417 ∈ S,       (x+4)/3 = 10807 = 101·107,

which has no prime factor at most 100. A sufficiently fine cylinder about this x retains all the finitely many required nondivisibilities. Also c_j is positive for large N: candidate 103 gives the PD event `n=305`.

Finally **S has level zero under the manuscript's definition**: 3 is in Q₀ and 101 is a non-slice prime (`101≡1 mod4`). THETA §1 charges only the slice primes, not all prime factors of the test modulus. Thus

    ℋ(1_S r_j)>0,       true count(E_j∩S)=0,

at an allowed level. The small numerical horizon is inessential: for any sufficiently large horizon choose a prime `q≡1 mod4`, `q>z`, and impose the corresponding candidate-divisibility condition. The same construction works, with positive rough support supplied by CRT (or by a second large prime in the required class).

There are two additional, independent scope defects:

* A bound on radical/slice level never bounds prime powers. Classes modulo `q^a` can have bounded level and modulus much larger than N. No SW/BV theorem evaluates all these classes at the claimed accuracy.
* Even for ordinary small moduli, **positive local main term is not equivalent to positive finite count**. The correct structural zero statement is about local inadmissibility; analytic errors and interval endpoints must remain in the statement. BV is an averaged distribution theorem, not a uniform positive-count theorem for every reduced progression.

For appropriate modulus-bounded tests, with all relevant candidate-divisibility primes at most z, the roughness law does give the familiar relative local factors. That useful restricted fact is not the claim written here. The induced modulus in the candidate-prime variable must include the class condition, the mod-8 condition, and the test after `n=mp−4e`; it is not automatically bounded just because S has low THETA level.

**Required repair:** delete “vanishes exactly when the true count does,” and delete the blanket “integers satisfy I2 up to BV/SW errors / BV-type arguments are covered” assertion. Either retain a purely abstract theorem, or define a genuine arithmetic test collection and its main-term/error vector, then show that the comparison law satisfies that vector. An exact fake identity only implies error inequalities around the **same correct main term**, not around a different prime-counting main term.

### 2.3 Finite quotient, duality, and the mixture

These parts pass.

For B_λ, condition a candidate majorant on the finite quotient consisting of Q₀ and the first digits at the relevant slice primes. Conditional averaging preserves the majorization, nonnegativity, mean, and allowed slice supports. Thus the optimum reduces to a finite-dimensional LP. Arbitrary powers and uncharged coordinates do not invalidate this reduction, because B_λ ignores them.

For each finite class collection containing the trivial class, duality gives a probability law with the prescribed Haar marginals and B_λ-mass at least β_λ. Compactness/FIP then supplies a single law for all permitted classes. Alternatively, the finite-quotient optimizer can be extended by independent uniform finer digits and irrelevant coordinates. The normalization is correct.

The small-prime avoidance factor on `1+8Ẑ` is

    (1−1/3)(1−2/7) = 10/21,

not `10/168`. For the remaining primes, `w(ℓ)<ℓ/4`, the weighted supply is `O(1/α)`, and the truncated mass is `O(λ)`. THETA Proposition 2.4/Theorem 2.5 therefore give the displayed `exp(−O(√λ)−O(log²(2+λ)))` bound. Take λ₀ large enough to include the small primes, or adjust the bounded factor.

For the activation mixture, for any clopen S,

    P(π_j=1,x∈S) = ∫_S r_j dℋ,
    P(π_J≡1,x∈S) = C^{|J|−1}∫_S ∏_J r_j dℋ.

I1 follows from the two components' low-level marginals; I4 and exclusivity follow from support. The inactive component gives the claimed lower bound. The strict endpoint `<` is now correct.

State the formal target as the model event `B_λ∩{π≡0}`. Since the represented family is capped by `4em≤z`, whereas the arithmetic identity for A_N uses all cofactors, explain that omitted bits are unconstrained and may be adjoined identically zero in this abstract information set. No assertion about their actual first moments or other deterministic relations is then being made.

### 2.4 Constants, sharpness, and the remaining scope language

The **conditional** Corollary 2.3′ is correct: if precisely I3 bounds with `K_k≥2^{k−1}` are the inputs and `r_j≤1/2`, use C=2. The listed numerical constants exceed 2. Lichtman, arXiv:2309.08522 Theorem 1.1, gives 3.2290; Wu's local source `sources/window3/0705.1652.txt`, Theorem 3, gives 3.3996, with `Π(x)=2∏_{p>2}(1−1/(p−1)²)x/log²x`. Tao's sieve notes give both `2^k k!` and `4^{k−1}(k−1)!`; the latter satisfies the needed comparison for every k≥2.

Keep the manuscript's disclaimer that global tuple estimates are not automatically localized I3 estimates. A pair estimate alone also says nothing about every higher K_k. Replace the universal literature wording with the enumerated comparison.

For Proposition 2.4, with `J=|𝒥|` constant densities,

    E R(R−1) = K₂ J(J−1)r² = K₂ μ²(1−1/J).

The inequality and limiting sharpness remain correct. Its constant-density example is an abstract example, not one of the prescribed roughness-supported arithmetic densities.

“What escapes Theorem 2.3 (each item excludes the mixture)” is too categorical. A smaller K_k only contradicts this mixture if an applicable k-tuple has positive product integral; a smaller one-sided upper constant is not itself “two-sided” information. Most importantly, genuine first-moment local obstructions omitted from I2 already escape the proposed arithmetic identification. Above-cap correlations are not the only unexcluded route.

## 3. Theorem 2.6: audit of all five steps

I checked the cited assembly and word-family definitions directly. An independent deep-mode audit reached the same model-level conclusion; the decisive supply and refinement calculations were checked again here.

### 3.1 State the level convention explicitly

Here the intended level is

    level(b mod d) = Σ_{p|d, p>W} log p,

charging **all** primes above W. This differs from I1's slice-prime level. The displayed s_j suggests the right convention, but `level(S)` must explicitly use it too. The cited word-family sieve-limit theorem does not give matching for all tests under the earlier, more generous non-slice-free convention.

The family need not satisfy `4em≤e^λ`: arbitrary powers and arbitrary W-smooth parts are allowed. This is not an error. It means the supply proof must sum smooth numbers rather than invoke Proposition 2.2. Declare `0≤ρ_j≤1` as well as the displayed upper bound, and fix C₀ as an absolute constant (otherwise the conclusion's constants depend on it).

### 3.2 Steps (1)–(2): random subfamily and supply

Independent selection with probabilities ρ_j correctly represents CH. The key smooth sum is valid. Dropping `m≡3 mod4` and other restrictions only enlarges it. Its odd-prime Euler factor is

    1 + γ′(p) [1/(p−1) + p²/(p−1)³].

The first summand inside brackets comes from `v_p(e)=0, v_p(m)>0`; the second from `v_p(e)>0`, including `4e/φ(4e)`. For `p>W`, this factor is `1+2/p+O(p^{−3/2})`. The 2-factor and the finitely many factors up to W are bounded constants for fixed W. Hence

    Σ_{P(em)≤y} Γ(4em)(4e/φ(4e))/(4em) ≪_W (log y)².

Consequently

    E𝔐(y) ≪ (log y)²/(log N−λ) ≪ log y

for `y≤e^λ` and `λ≤(log N)/2`. Every prime above W dividing an indexed modulus is at most `e^λ`, so the random supply is constant beyond the horizon (take λ₀≥log W).

The concentration argument is legitimate but compressed. The unrefined weight `Γ(4em)/(4em)` is uniformly bounded: the factor at 2 is at most 2, and each odd-prime factor is at most 1 for W sufficiently large. Thus, writing `t=log y`, the variance is `O(E𝔐(e^t))=O(t)`. Bernstein gives a tail `≤exp(−cKt)` for threshold Kt once K is a sufficiently large fixed constant. Sum these bounds at `t=2^i`; the failure probability is less than 1/2 after fixing constants. Monotonicity fills the gaps, with another factor 2 in K. No union over every prime or every subfamily is needed.

### 3.3 Step (3): W1/W2 membership and inherited estimates

The **literal membership statement needs refinement**. EXSET_SIEVE_MASS §1.1 defines 𝔘 using refined W1/W2 classes intersected with the mod-8 fibre, not the raw class modulo 4em.

For example `(e,m)=(1,3)` has raw class `5 mod12`; on the fibre it is

    17 mod24 = (17 mod48) ∪ (41 mod48).

The two classes on the right are refined W2 classes for `(u,v)=(4,3)`. In general split by the compatible values of t modulo 4 and intersect with `n≡1 mod8`. These are genuine members of 𝔘, with endpoint `u=4e∈S`. Similarly refine the prime-local W1 classes by the compatible value of the other endpoint modulo 8.

This operation preserves the fibre avoider set and changes moduli only by powers of 2. The sum of the refined `Γ(G)/G` weights is no larger than the corresponding unrefined weight. For concentration, retain **one common selection coin for all refinements of an original j**; independence of the refined classes is neither true nor needed.

The square-base condition then follows from SIEVE_MASS §1.1. The excluded mod-8 residues need only avoid **unit squares**; do not invoke BEYOND_CRT's stronger literal “no perfect square” hypothesis for them. SIEVE_MASS Theorem 3.2 expressly handles this distinction.

Cofactor sums (iii) are nonnegative and inherited by subfamilies of the refined universe. SIEVE_MASS Theorem 3.2's W1/W2 calculation and BEYOND_CRT Lemma 2.4 supply them, including the W-uniform control needed to choose the fixed W. This is a legitimate use of the cited framework, not a new arithmetic conjecture about PD.

### 3.4 Assembly with supply exponent one

The rerun is legitimate after correcting the constant. Put `s₁=√λ`, `s=2^i s₁`, `d=floor(λ/s)`. Then

    EM_{V_i} ≤ 2Ks,
    (EM_{V_i}+4d)/d ≤ 4K s²/λ + 4 = 4K·4^i+4.

The printed `2K·4^i+4` neglects the floor loss. The corrected inequality is exactly the β=1 case of BEYOND_CRT's assembly formula. Singleton cost is `O(√λ)`, and block costs sum to

    O(√λ Σ_{i≥0} 2^{−i}(1+i)) = O(√λ).

Keep the linear block, square-base term, leak bound, and `O(log²λ)` remainder from the cited proof. For large λ that remainder is absorbable into `C√λ`; finite λ can be absorbed by increasing C. Thus the claimed exponent follows under the stated KARY/EK proviso.

### 3.5 Steps (4)–(5): fake laws and mixed monomials

For each realized finite subfamily, the avoider set is clopen. The majorant lower bound therefore gives, by finite LP duality and compactness, a law matching Haar on every permitted class and assigning the avoider at least the claimed mass. Starting from full Haar and imposing the excluded mod-8 residues causes only a constant normalization; equivalently run the dual problem directly on the fibre.

For a permitted monomial set

    T = S ∩ ⋂_{j∈J} class_j.

If S is a class, T is a class or empty; for more general permitted indicators, expand linearly. Its all-prime radical level is at most `level(S)+Σ_J s_j≤λ`. Conditional on **every** selected subfamily, its x-probability is ℋ(T), including on bad subfamilies where the chosen law is Haar. Therefore averaging over the independent selection coins gives exactly

    E[1_S∏_{j∈J}π_j] = ℋ(T)∏_{j∈J}ρ_j.

The dependence of x on the selected subfamily does not break this calculation. On good subfamilies the avoider event forces both B_λ and all bits zero; the good-subfamily probability ≥1/2 yields the stated lower bound, after absorbing fixed constants.

### 3.6 Arithmetic scope

The paragraph saying CH ignores roughness and does not match true PD statistics is accurate. Even a first-order test forcing a small candidate divisor can distinguish CH from the arithmetic law. Roughness-refined intersections are generally expensive unions of classes, so the present monomial calculation cannot simply be reused for them. The proposed prime-law/unit-group rerun remains unproved in the cited sources.

This also requires correcting the subsequent “Blocking statement”: **two-sided true PD information below the cap is not excluded**. Only class-constant CH information below the cap is covered by Theorem 2.6. Keep the two assertions separate.

## 4. Lemma 3.0 and Proposition 3.1

The repaired estimates work.

* (a) The fixed mod-8 PNT interval supplies `≫N/log N` shifts whose shifted number is prime and hence cannot contain an event prime, giving `cost(e)≤L₂+O(1)`.
* (b) Splitting at `q²`, treating an empty upper interval as empty, and including the `O(1/N)` progression errors gives the stated estimate. BT at `2N` bounds the aggregate rounding contribution by `O(1/φ(q))`.
* (c) `16E²` makes the high-range BT hypothesis valid simultaneously for e≤E. Divisor pairing bounds the low range by `O(log(2E))`, and summing reciprocals of φ bounds the upper range and rounding as claimed.
* (d) The sum of shift-hit probabilities is bounded by the mean number of event pairs. Divisor pairing/BT gives `Σ_{ℓ≤N}w(ℓ)/ℓ≪log N` and `Σ_{ℓ≤N}w(ℓ)≪N`, so the displayed total-hit estimate follows.

There is no endpoint gap in applying these bounds to relevant shifts: if `n=8k+1`, then `e≤floor((n+3)/8)=k`, so `4e≤(N−1)/2`.

For Proposition 3.1(b), first choose an absolute E₁ such that `e>E₁` implies `hit(e)≤1/2`. The small shifts cost `O(L₂²L₃)`. A contributing large shift has

    ε/2 < cost(e) ≤ 2 hit(e),

so the standard totient lower bound yields an upper cutoff satisfying

    log E₀ ≤ a + O(log(2+a+L₂)).

If this cutoff exceeds `N^{1/3}`, then

    (log N)/3 < a + O(log(2+a+L₂)),

which forces `a≫log N`. Now use (d) on the large shifts, obtaining `O(log N)`, and add the small-shift `O(L₂²L₃)=o(log N)` contribution. This proves the claimed bound. The text's “whole contribution” skips this addition but does not change the result.

The final necessity for a **common** loss follows in the stated regime `M≫L₂²L₃`. It says nothing comparable about heterogeneous losses or non-product estimates.

The “Reading” still asserts a two-sided asymptotic per-shift cost and `≍L₂L₃` costly shifts without a proof. The proposition supplies only an upper bound of the latter order. Delete those asymptotic claims or mark them as separate heuristics. Likewise, a particular NT/Henriot implementation is capped only after verifying periodic nonnegative majorization, level, and CRT-mean evaluation; a name alone does not place it inside G1.

## 5. Corollary 3.3, band statements, and literature

### 5.1 Top-band arithmetic and CRT visibility

The event bounds from Lemma 1.1(d) justify the finite shift range and prime cutoff. Any contributing shifted integer is at most `(3n+3)/2≤2N` apart from harmless tiny cases, so a divisor above `√(2N)` is unique and is its largest prime factor. The inclusions

    U-failure on I ⊆ A_N ⊆ {X_top=0}

are correct. Combining with U on `n≡5 mod8`, and the odd-square obstruction for U, gives the stated power-saving consequence (finite exceptions can be absorbed, or written `+O(1)`). For ES₅, cite the actual prime-domain comparison explicitly; the z50 theorem does not identify all squares as ES₅ failures.

The revised band accounting is correct. At level `log N`, two primes above `√(2N)` cannot occur in one term. Boolean conditional averaging reduces the pure-band problem to a linear majorant, giving saving at most `−log(1−max p_ℓ)=o(1)`; `max p_ℓ→0` follows from the divisor bound. At `2 log N`, three can fit but four cannot.

For a fixed logarithmic-width band and polynomial level, THETA Proposition 2.4 has `s_*≍log N`, only O(1) groups, and remainder `O(log(2+μ))`. Choosing the Rankin parameter accordingly proves the claimed band upper bound, including the remainder. These are statements about sieving that band; adding smaller-prime information can of course supply its own saving.

### 5.2 Literature verification and remaining wording

I checked the actual statements in the following sources:

* [Teräväinen, arXiv:1710.01195](https://arxiv.org/html/1710.01195), Theorems 1.11 and 1.14: the asserted two-shift large-prime-factor count law and Dickman law in logarithmic density are correctly described.
* [Tao–Teräväinen, arXiv:2512.01739v2](https://arxiv.org/html/2512.01739v2), Theorem 1.8: for x in a set whose complement has logarithmic measure `O(log^{−c}X)`, the consecutive smooth-number formula holds with error `O(log^{−c}x)`, uniformly in `u,v≥1`. The revision correctly distinguishes this from an all-scales qualitative result.
* OpenAI item 012: the local `introduction.tex` explicitly claims ordinary natural-density independence for fixed parameters at all scales, and explicitly disclaims the quantitative error/growing-parameter uniformity. “Claims,” “unrefereed,” and “no rate” are appropriate. This review does not certify that manuscript's proof or formalization.

None of these is a growing-modulus residue law for `P⁺(n+4e) mod4e`. Gallagher's fixed-λ conditional Poisson comparison is now correctly distinguished from a growing-λ exponentially small zero tail. The RH/Selberg bound has the stated dependence on H, but write its usual short-interval regime (for example a dyadic x-range, `1≤H≤X`); for `H=λ log X` with fixed λ it is not nontrivial, whereas for `H=X^θ`, `0<θ<1`, it gives a power saving. This is an analogy, not a reduction or a technology barrier.

The sentence “TB_δ would follow from joint control ... at precision ...” is not yet a precise sufficient hypothesis. It must specify the reference law and its zero probability, and include the size cutoff or use the actual top-band hit indicators. A valid formulation is: on a selected shift family, a comparison law Q has `Q(all hits zero)≪e^{−M}`, and the actual law differs on that event (or in total variation) by `O(e^{−M})`; then TB follows with constant factors. Counting `exp(M)` coordinates and naming a precision alone does not establish these premises. The claim about `≍(log N)²` candidates is likewise heuristic unless separately proved.

## 6. Remaining overclaims outside the main proofs

1. **N1 identity:** for fixed ℓ, `E_{ℓ,e}∩I` is not the union over all PD cofactors for that e. That union also contains other pivot primes. For example n=17 lies in the e=1, m=3 PD event (candidate 7), but not in `E_{11,1}`. Put `⋃_ℓ` on the left.
2. **Raw-count evidence:** §4.1 and row 4 cite `Var/mean=1.05–1.12` for X, but §6.2 measures `X_{ℓ>Y}`. State the actual statistic. At the new 4·10⁹ top-band row the ratio is about 1.1259, so even a claimed exhaustive rounded range needs adjustment.
3. **Moment necessity:** §5's calculation is valid for the displayed Poisson-scale central-moment bound, with `μ≍log N`, `0<δ<1/2`, and the appropriate moment range. Replace “a requirement of moment arguments” by “the order needed when using this particular bound.” Other weighted or structured moment estimates have not been classified.
4. **§8 “cannot touch”:** the top band is visible and yields bounded/polylogarithmic savings at polynomial level. Say “cannot supply the required exponential-in-mass saving,” not that CRT cannot touch it.
5. **§8 “product forms are useless”:** Proposition 3.1 concerns a common fixed loss, or a specified common small loss. It does not rule out exact factors (`C_e=1`), sufficiently accurate common factors, heterogeneous losses, or other estimates. Qualify the sentence.
6. **Remaining PD gap:** ordinary local support tests already defeat the claimed arithmetic I2 model, and Theorem 2.6 explicitly omits roughness. Do not assert that a successful PD method must use correlations above `log N`. Genuine below-cap arithmetic correlations, correctly normalized first moments, signed aggregate information, and other deterministic relations remain outside the established conclusions.
7. **Full-family transfer:** upper bounds transfer by the stated inclusion. The CRT fake-law and CH constructions plausibly extend to the full refined U-family with adjusted supply constants, as labeled Assessment. The exact roughness/cofactor parameterization and arithmetic first-moment transfer require their own proof; replacing w(ℓ) alone does not prove them.

## 7. Numerical audit without rerunning the large sieve

All computation used `ulimit -v 8000000` and explicit timeouts. Scratch files are in `/tmp/dbreak_review_0046/`. I did **not** run the 4·10⁹ sieve (or any new high-scale sieve). The independent script `check_r2.py` streams the stored histogram lines, computes integer totals and first/second sums, and checks the first-moment counterexample. It runs with `timeout 30s uv run ...`; no array proportional to N is allocated.

For `data/z51_dbreak/sieve4_top_N4000000000.txt`:

| Quantity | Recomputed value |
|---|---:|
| Sum of all non-square histogram bins | 499,968,377 |
| Sum of small-layer-avoiding bins | 2,000,321 |
| First sum `Σ r h_r` | 2,714,513,504 |
| Second sum `Σ r² h_r` | 17,794,379,152 |
| Top-band zero count | 3,218,708 |
| Mean | 5.429370393960 |
| Zero probability | 0.006437823167 |
| `exp(−mean)` | 0.004385856295 |
| Poisson ratio | 1.467860033088 |
| Variance/mean | 1.125903369010 |
| Conditional zero probability | 31,612 / 2,000,321 = 0.015803463544 |
| Maximum / number at least 40 | 41 / 5 |

These reproduce the manuscript's rounded row. The total is also exactly `500,000,000−1−31,622`, accounting for n=1 and the other odd squares. The four observations in bin 40 and one in bin 41 match the five printed BIG records.

The 2·10⁹ row independently gives mean **5.208959882208**, zero probability **0.007948038904**, Poisson ratio **1.453725864924**, and conditional zero probability **0.019266544486**. Its histogram totals are **249,977,639** and **1,231,513**. The endpoint log-log slope from 10⁹ to 4·10⁹ is **−0.303721891880**, agreeing with −0.304.

I also checked the repaired `sieve4_N1e9_Y1000.txt`: its full histogram now sums to **124,984,189**, with maximum 42 and exactly one observation at least 40. The previous missing observation is restored. Its mean is **7.173274677167**, and variance/mean **1.049062865169**. The checked files have no saturated bin-255 observations, so saturation does not alter these moments. The script still saturates at 255 generally; future runs must continue checking that bin.

The high-scale calculations certify arithmetic consistency of the saved outputs, not independent regeneration of their event marks. The round-1 independent low-scale sieve/brute-force checks remain the implementation evidence. Finite-range Poisson resemblance does not certify an asymptotic lower tail or its proposed causal mechanism.

## Recommended disposition

Retain the elementary results, numerical section, product-format theorem, abstract activation theorem, and explicitly conditional CH theorem. Correct the minor equalities/refinements and remove the false I2 arithmetic-transfer paragraph. The revised manuscript is much closer to an honest inventory of scoped results, but it still does **not** prove a barrier for actual one-sided PD information, much less a depth-breaking estimate. Its honest unresolved target remains an arithmetic lower-tail estimate beyond the particular model and proof-format limitations established here.
