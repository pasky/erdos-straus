# Hostile referee report, round 3: EXSET_DEPTH_BREAK.md

ES remains open. This manuscript proves no depth-breaking exceptional-set bound.

## Executive verdict

**The arithmetic local-density repair in Theorem 2.3 now works.** Bounding the test modulus really removes the round-2 obstruction. After transforming the test into the candidate-prime variable, horizon roughness produces exactly the reduced-residue proportions claimed in (δ). I find no remaining local-support counterexample in this test family. The abstract activation proof remains sound. However, transferring an actual SW/BV estimate requires its candidate-modulus range and an error adjustment for normalization by the *observed* total; merely naming SW/BV does not discharge those obligations.

**Theorem 2.6's requested repairs pass**, conditional on the expressly cited KARY/EK framework. **The TB_pow consequence for exceptional primes also survives**, but write the U count on its stated domain, and explicitly extend/define ES₅ at the other primes rather than silently applying a theorem on the 1 mod 4 line to all primes.

**The new numerical counts pass the checks performed here; the claim that the distribution is “Poisson within sampling error” does not.** The zero probabilities are compatible with the fitted Poisson zero probabilities. The variances are significantly above the Poisson variances, by approximately 7–10 estimated standard errors. These are different claims.

The audit began at `bfc975a8`. During it, the author-side commit `9b054b4b` added the scale stratification. This report includes that addition: it now supports “scale mixing explains most of the excess” at N = 10⁹, not “the distribution is Poisson at fixed scale.” I made no changes to the manuscript or programs and no commits.

## 1. Verdicts for every §0 row

| Row | Verdict | Concrete disposition |
|---|---|---|
| 1 | **SOUND** within its stated elementary/assessment scope | The N1 union identity is repaired. Keep prime-distribution ranges in the candidate variable and include the mod-8 condition. |
| 2a | **SOUND** | The BT upper bound and hypothetical depth interpretation remain properly separated. |
| 2b | **SOUND-WITH-MINOR**, not a universal arithmetic barrier | The abstract theorem and reduced-class formula now pass. Define ϖ explicitly using the induced modulus; restrict the structural-zero equivalence to positive global mass; state the normalized error ledger and candidate-modulus ranges. |
| 2c | **SOUND** | The missing finite-size factor is present, and the constant-density sharpness example is explicitly abstract. |
| 2d | **SOUND** | No new defect in the scoped Rankin statement or its stated range. |
| 2e | **SOUND-WITH-MINOR**, conditional on KARY/EK | The all-prime level, common-coin refinements, Euler factor and block constant pass. Clarify that the LP quotient here retains full relevant prime powers and that the dual is run on the mod-8 fibre. |
| 3a | **SOUND-WITH-MINOR** at theorem level; one false proof sentence remains | An *absolute* E₁′ with hit(e) ≤ 1/2 for all e > E₁′ is not supplied by Lemma 3.0(b) and is false uniformly in N. Use E₁′(N) = O(L₂L₃). The advertised bound survives. |
| 3b | **SOUND-WITH-MINOR** | The inclusion directions are correct. Restrict the intermediate U exceptional-prime count to p ≡ 1 mod 4, define ES₅ outside that domain, and handle p = 2 and p ≡ 3 mod 4 explicitly. |
| 3c | **SOUND-WITH-MINOR** after `9b054b4b` | The all-n rows and new stratification arithmetic reproduce. Say “most of the excess at N = 10⁹ is accounted for by scale stratification,” not an exclusive/asymptotic causal identification. |
| 3d | **MAJOR wording/statistical overclaim; counts SOUND** | Replace “X_top is Poisson within sampling error” by “the zero probability is compatible with exp(−sample mean), despite significant overdispersion.” Replace mean ≈ 0.32 ln N by a measured slope ≈ 0.32 per unit ln N, with a substantial fitted intercept. |
| 3e | **SOUND** as a scoped assessment | The sufficient hypothesis now names a reference law and the required zero-event error. The cited size laws are not presented as residue laws. This round does not independently re-audit the external literature. |
| 4 | **SOUND** within the Haar/raw-count scope | Large-layer numerical ratios are now identified as such; no general L² barrier is asserted. |
| 5 | **SOUND** within its stated scope | Moment order is now tied to the displayed bound, and qualitative errors are not assigned a numerical rate. |
| 6 | **SOUND-WITH-MINOR** for the checked numerical claims | Stored rows reproduce; 12 high-scale sample rows regenerate; 40 independent e-view checks pass. Harden the supplied cross-check's subprocess/length checks and document the candidate program's supported input range. No fresh full high-scale census was run. |

Sections 7 and 8 have no separate rows in the current table. Their residual overclaims and repairs are listed in §7 below.

## 2. Theorem 2.3: arithmetic transfer

### 2.1 The correct candidate-variable calculation

Fix j = (e,m), with m ≡ 3 mod 4 and 4em ≤ z. Put Q = lcm(8,4e). If class_j is nonempty, its two conditions are equivalent, under x = mp−4e, to a single **reduced** candidate class

    p ≡ a (mod Q),
    a ≡ −1 (mod 4e),   ma−4e ≡ 1 (mod 8).

Here m is odd, so it is invertible modulo 8. The compatibility condition may fail; those are the empty classes already assigned zero density. For a compatible class, a is coprime to Q, and

    ℋ(class_j) = 8/(mQ).

This includes the mod-8 condition; replacing Q by 4e without checking it would be wrong.

Now let S = {x ≡ b mod d}, d ≤ z, and put

    g = gcd(m,d),   D = d/g.

The test is the linear congruence mp ≡ b+4e mod d. It is impossible if g does not divide b+4e. Otherwise it is equivalent to

    p ≡ c (mod D),
    c = (m/g)⁻¹ ((b+4e)/g) mod D.

Thus the minimal combined candidate modulus is L₀ = lcm(Q,D), not generally d or lcm(Q,d). The manuscript's larger L = lcm(Q,d) is nevertheless a **valid common refinement**, so its use does not invalidate (δ).

Define explicitly

    R = {a′ mod L : a′ ≡ a mod Q, gcd(a′,L)=1},
    R_S = {a′ ∈ R : ma′−4e ≡ b mod d},
    ϖ_j(S) = |R_S|/|R|.

There are |R| = φ(L)/φ(Q) reduced extensions. Every prime dividing L is at most z: this is true for Q because 4em ≤ z (with λ₀ large enough for 2), and for d because d ≤ z. Conditional on the base candidate class, Haar gives equal mass to its extensions modulo L. Roughness kills all non-reduced extensions. On each reduced extension its remaining probability is the same factor

    ∏_{q≤z, q∤L}(1−1/q).

Taking the ratio of the integrals over S and over the whole class proves exactly

    E_ℋ[1_S r_j] = ( #E_j^{PD}/#I ) ϖ_j(S).

Prime powers cause no hidden defect. A condition modulo q^a is uniform in the higher q-adic digits after restricting to units, and the division by m induces D = d/g rather than an unaccounted larger modulus. Indeed, bounding all prime factors of L by z is sufficient for this *local identity*; bounding d itself additionally controls the allowed arithmetic test family.

Example checking the gcd issue: for e = 1, m = 3, z ≥ 12, the base class is p ≡ 7 mod 8. For tests x ≡ b mod 9, the weights at b = 2 and b = 8 are each 1/2; at b = 5 the weight is zero, because it forces 3 | p. It would be incorrect to count these tests as single unrestricted reduced classes modulo 9 in the p variable.

**Verdict on (δ): the local identity is correct.** The old large-uncharged-prime counterexample is disallowed. A permissible test cannot force a candidate divisor q > z through these congruences. I find no replacement counterexample.

One literal qualification remains: if #E_j^{PD} = 0, the chosen r_j is identically zero even for locally admissible S. Therefore write “ϖ_j(S) vanishes exactly on locally inadmissible tests”; transfer that assertion to E_ℋ[1_Sr_j] only when the global mass is positive. This is a normalization qualification, not a revived round-2 obstruction.

### 2.2 Check of (γ)

For a nonempty base class, its conditional roughness probability is

    R_Q = ∏_{q≤z, q∤Q}(1−1/q) ≍ Q/[φ(Q) log z].

All primes dividing Q are in the horizon, justifying the displayed Mertens factor. Put X_j = (N+4e)/m. Since mQ ≤ 2z, BT on the single reduced class modulo Q gives, for N sufficiently large in the stated range,

    #E_j^{PD}/#I ≪ 1/[m φ(Q)(log N−λ)].

More precisely the logarithm can first be written log N−λ−log 2; it is comparable to log N−λ once λ ≤ c log N with fixed c < 1. Dividing by (8/(mQ))R_Q gives

    c_j ≪ λ/(log N−λ).

Hence r_j ≤ 1/C after choosing c_C sufficiently small and N sufficiently large. Empty classes/events are harmless. No missing m-factor or mod-8 factor remains.

### 2.3 SW/BV errors and the “covered / not covered” paragraph

For a genuine counting theorem, distinguish the conventional analytic main term from the observed-total normalization. Write, in count units,

    A_j = #E_j^{PD},    A_j(S) = # (E_j^{PD} ∩ S),
    M_j = [Li(X_j)−Li(z)]/φ(Q).

For compatible reduced tests, the conventional main term is ϖ_j(S)M_j. If

    A_j = M_j + R_j,
    A_j(S) = ϖ_j(S)M_j + R_j(S),

then the exact error around the manuscript's center is

    A_j(S) − ϖ_j(S)A_j = R_j(S) − ϖ_j(S)R_j.

Thus an available absolute-error bound yields

    |A_j(S)−ϖ_j(S)A_j| ≤ |R_j(S)| + ϖ_j(S)|R_j|.

For averaged bounds, sum this ledger with the actual weights and multiplicities. Do not reuse an unchanged conventional error vector without checking this extra term. Divide by #I when comparing with I2.

Likewise, the distribution theorem is applied at **L₀ in the candidate variable X_j ≈ N/m**, including Q, not automatically at d. Although d ≤ z, one only has the crude bound L₀ ≤ Qd ≤ 2z²/m. SW requires the appropriate logarithmic candidate-modulus range; BV supplies an averaged estimate in its X_j-dependent range, not uniform asymptotics at every d ≤ z and every j. Repeated induced moduli and summation over j need their own accounting.

With these qualifications the answer to the user's specific question is **yes**: an exact fake first-moment identity satisfies every allowed error inequality centered at the **same normalized main term**. The repaired local density is no longer a different prime-counting main term. However, the sentence “the integers satisfy it up to SW/BV error terms” is still too compressed if read as a theorem covering the whole test family without the above ranges and ledger. Replace it by the explicit conditional statement.

The surrounding exclusions are substantially honest now: higher-order two-sided arithmetic information, omitted first-moment tests, archimedean constraints, identities beyond first moments, and extra exact zero correlations are not covered. I3 remains an assumption of a very specific localized form, not something implied just by quoting a global sieve constant.

Finally, retain the distinction between the formal model event B_λ ∩ {π=0} and A_N. The modeled family need not contain every arithmetic event. All omitted bits may be set to zero **only because the stated information set constrains none of them**. Say “all events outside 𝒥,” not just “cofactors m > z”: events with m ≤ z but 4em > z are omitted too. Inclusion of A_N in the larger formal zero event alone is not a lower bound for arithmetic A_N.

## 3. Corollary 3.3: the exceptional-prime implication

On p ≡ 1 mod 8, the chain is

    {ES₅(p) fails} ⊆ {U(p) fails} ⊆ A_N ⊆ {X_top(p)=0}.

The first inclusion is the contrapositive of U ⇒ ES₅, on its stated prime domain. The second is the contrapositive of a prime-pivot U certificate; the third is the top-band subfamily inclusion. Primes are not squares, so TB_pow bounds the last set at primes by its non-square integer bound. No reversal of inclusion occurs.

On p ≡ 5 mod 8, U holds for p > 5: the endpoint v = 3 and divisor A = 8 satisfy 1 < 8 < p+3, A | p+3 and A ≡ −1 mod 3. This is `EXSET_SIEVE_MASS.md:45–48`. Thus there is at most the fixed U exception p = 5 on this line; an ES₅ exception there is not forced by U's failure. It is harmless in the big-O bound.

The source-domain issue is real but repairable. `FOREST_DEEP_FABLE.md:43–55` works with p ≡ 1 mod 4, and `EXSET_SIEVE_MASS.md:47–60` defines its U exceptional set and ES₅ class family on that domain. Its Theorem 3.5(a) suppresses that distinction in its display; citing the display alone does not define ES₅ or U on other primes.

There **is** an explicit wider definition elsewhere in the repository: `EXSET_BEYOND_CRT.md:103–108` defines ES₅(n) by a positive word with a slot divisible by 4, and its Theorem 3.1 (`:343–353`) separately handles p ≡ 3 mod 4 and p = 2. Under that definition, ES₅ is automatic at p ≡ 3 mod 4. For example the word

    (t,u,v) = (2,1,p+1),   tuv−u−v = p,

has 4 | v and distinct endpoints. This also avoids any ambiguity about using the equal-endpoint word (p+2,1,1) printed in the source. At p = 2 the word (1,2,4) has the required slot.

**Recommended display:** explicitly adopt this global word/slot definition, and write

    #{p≤N : ES₅(p) fails}
      = #{p≤N : p≡1 (4), ES₅(p) fails}
      ≤ #{p≤N : p≡1 (4), U(p) fails}
      ≪ N^{1−c}.

Alternatively restrict all ES₅ counts to the original p ≡ 1 mod 4 domain. The unrestricted U count in the current corollary is unnecessary unless U is also explicitly extended. The all-prime ES₅ conclusion is valid after this small domain repair.

For the all-integer U conclusion, use the established odd-square obstruction in addition to the displayed inclusion: squares account for the asserted main set, non-square failures on the 1 mod 8 line are bounded by TB_pow, and the 5 mod 8 line contributes O(1). The corollary's proof should name that square obstruction when asserting the equality with the square count.

## 4. Theorem 2.6 repairs

I checked the key source definitions and assembly formulas directly, and reviewed an independent deep-mode audit of this part. No new arithmetic assertion follows from this model theorem.

1. **Level convention:** charging all primes p > W is now explicit, and agrees with `EXSET_SIEVE_MASS.md:292–296`. Arbitrary prime powers and W-smooth parts remain allowed. For T = S ∩ ⋂ class_j, its radical level is at most level(S)+Σs_j, exactly what step (5) needs.
2. **Refinement:** the W2 example is correct: (5 mod 12) ∩ (1 mod 8) is (17 mod 48) ∪ (41 mod 48). General refinement changes only powers of 2. For W2, Γ is unchanged because 2 already divides 4em, and the total refined Γ(G)/G weight does not exceed the original. For W1, the fibre fixes the other endpoint mod 8; Γ(8ℓ)/(8ℓ) = Γ(ℓ)/ℓ because γ′(2)=8. These are genuine classes of the refined universe in `EXSET_SIEVE_MASS.md:50–68`.
3. **Common coins:** all refinements of one original event correctly share its coin. For concentration, group their weights into a_j(y) ≤ Γ(4em)/(4em) ≤ 2. The independent summands are κ_j a_j(y), not separate refined-class coins. Their variance is O(E𝔐(y)), so Bernstein and the dyadic-log union bound are legitimate.
4. **Euler factor:** writing a=v_p(e), b=v_p(m), the a=0,b>0 contribution is γ′(p)/(p−1); the a>0,b≥0 contribution, including e/φ(e), is γ′(p)p²/(p−1)³. Thus the printed odd-prime factor is exactly right. For p>W it is 1+2/p+O(p^{−3/2}), yielding the (log y)² smooth sum. Since λ≤log N/2 and log y≤λ, dividing by log N−λ gives O(log y). Supply is constant beyond e^λ. Small-prime factors are bounded for fixed W.
5. **Square base and cofactor sums:** the relevant hypothesis is no *unit* square, not no square at all. The revised proof uses the right source theorem. Cofactor bounds are inherited by subfamilies, with the W-uniform leak control in the cited framework.
6. **Block constant:** d=floor(λ/s)≥λ/(2s) in the relevant blocks, so (EM+4d)/d ≤ 4Ks²/λ+4 = 4K·4^i+4. This is the β=1 specialization of `EXSET_BEYOND_CRT.md:243–249`. The resulting sum is O(√λ), and O(log²λ) is absorbable.
7. **Dual/monomial argument:** conditional on every selected family, the law gives T its Haar mass; averaging its indicator of J being selected gives exactly ℋ(T)∏ρ_j. Dependence of x on the selected family does not spoil this step.

Two exposition repairs remain. Unlike the prime-local B_λ quotient in Theorem 2.3, the realized W2 avoider may depend on higher prime powers: its finite quotient must retain those full digits. Also state that the dual is run on the 1 mod 8 fibre, or explain conditioning the full-Haar dual, paying only a constant factor. Both are available without changing the result.

## 5. Numerical implementation audit

### 5.1 Candidate enumeration is correct in the recorded range

The program enumerates k | (n+m)/4, k ≡ −1 mod m, then sets

    e = (n+m)/(4k),   t = (k+1)/m,   p = 4et−1.

This is precisely Lemma 1.1(e), using k rather than e as the enumerated divisor. All quantities are integral and positive, and pm−4e=n. Each pair (m,e) is enumerated once. Multiple e with the same p should be counted separately, since X_top counts shifts; there is no erroneous deduplication.

The code's Mmax is a padded **global** bound, not the n-dependent bound stated in the prose. This is safe: even for composite candidates, m≥3 and p≥4e−1 give e≤(n+3)/8. Hence a candidate above √(2N) necessarily has

    m = (n+4e)/p < (3n+3)/(2√(2N)).

The global Mmax exceeds this for all sampled n≤N. Overscanning larger m creates no extra accepted top-band candidates, because the same inequality rules them out after the p filter.

The segmented factorization covers all required offsets n+m. It sieves through floor(√(2N+Mmax))+2, more than enough to cover √(n+Mmax) in these runs. After stripping the listed primes, any remaining factor of (n+m)/4 is prime: two factors above that cutoff cannot fit. Although the code computes `rem`, the factor extraction subsequently recomputes divisions from x using `fp`; that is redundant, not incorrect.

The identity check is present. The top cutoff is numerically safe at the recorded N; an integer comparison p²>2N in widened arithmetic would be better for a general-purpose executable.

The Miller–Rabin bases are the first twelve primes 2 through 37. This is a valid deterministic set for unsigned 64-bit inputs; it is not the insufficient first-seven-prime set. `unsigned __int128` modular multiplication avoids product overflow. This does **not** make the entire candidate executable safe on arbitrary 64-bit input: its surrounding signed arithmetic, floating cutoffs, allocation sizes and fixed divisor buffer are more restrictive.

For the actual files N≤10¹¹, the allocations are modest and arithmetic is safe. I independently enumerated ordered exponent patterns to bound τ(x) for x≤25,000,100,000, above every x=(n+m)/4 used in these runs: the maximum is 2880, attained at 24,443,218,800. This is well below the 16384-entry divisor buffer. The fixed distinct-prime storage is also ample in this range. The source should nevertheless validate its accepted range and allocations rather than advertise unrestricted input robustness.

The sampling rule rounds a uniformly drawn integer downward to 1 mod 8 and rejects squares. It is almost, but not exactly, uniform on [N/2,N]∩I: endpoint cells have unequal lengths and one endpoint cell can fall below N/2. This is negligible here (O(1/N)), and every stored observation was in range, congruent to 1 mod 8 and a non-square. Sampling the progression index directly would remove the issue. The seed/command provenance should be stored with future datasets.

Compilation with `gcc -O2 -Wall -Wextra` succeeds with a misleading-indentation warning at the two adjacent `if` statements on line 53. This is not a logic error.

### 5.2 Independent arithmetic checks actually executed

All executions used `ulimit -v 8000000` and explicit timeouts. Scratch is `/tmp/dbreak_review_0046/`. Python ran through `uv`. No dense Cartesian-product allocation was used; the independent SPF table goes only to 400000.

* Compiled the current candidate source to `candidates_r3`.
* Regenerated the first, middle and last recorded n from each of the four data files: **all 12 rows match**, including C_top, X_top and the printed inverse-log weight sum.
* Wrote a different implementation: factor n+4e directly using an SPF table, for all 1≤e≤floor((n+3)/8), and test each distinct prime factor by p²>2N and 4e | p+1. At fixed N=200000 it agrees on **all 40 tested n**, consisting of controls and seeded random samples, spread across the full interval.

Selected independent checks (the full event lists are in `audit_r3.out`):

| n | C_top from candidate program | X_top from both methods | Direct events (e,p) |
|---:|---:|---:|---|
| 5393 | 6 | 1 | (19,1823) |
| 95129 | 11 | 2 | (2,13591), (390,3119) |
| 115945 | 7 | 4 | (1,2467), (5,859), (7,811), (101,38783) |
| 59441 | 10 | 3 | (16,3967), (193,20071), (2477,9907) |
| 180329 | 16 | 6 | (1,6679), (3,25763), (14,839), (17,25771), (1503,6011), (3468,27743) |

The last event at n=59441 tests the extreme t=1 boundary p=4e−1. Squares and several hard-prime controls also give the expected zero counts at this fixed threshold.

I did **not** independently regenerate all 330000 high-scale sample rows or rerun the full 10⁹/4·10⁹ census. Do not describe these checks as doing so.

The supplied `scripts/z51_dbreak_xcheck_top.py` has a reproducibility weakness: it hard-codes `/tmp/dbreak_0046/cand`, does not request `check=True`, and zips expected n with subprocess output without asserting its length. A truncated run can therefore check fewer than the claimed 150 observations. My independent check asserts successful exit and exact output length. Harden that harness; this is not evidence of an actual mismatch in the stored data.

### 5.3 Recomputed fixed-scale rows

Both rerunning `scripts/z51_dbreak_cand_analyze.py` and an independent integer-total calculation reproduce the table.

| N | samples | ΣC | ΣX | ΣX² | zero count |
|---:|---:|---:|---:|---:|---:|
| 10⁸ | 100000 | 2577442 | 466834 | 2662770 | 985 |
| 10⁹ | 100000 | 3347921 | 541809 | 3503427 | 454 |
| 10¹⁰ | 100000 | 4213694 | 615500 | 4436258 | 187 |
| 10¹¹ | 30000 | 1556389 | 206099 | 1639569 | 35 |

| N | E C_top | E X_top | variance/mean | P₀ | s.e.(P₀) | exp(−mean) | ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10⁸ | 25.77442 | 4.668340 | 1.035550 | .0098500 | .00031230 | .00938784 | 1.049230 |
| 10⁹ | 33.47921 | 5.418090 | 1.048076 | .0045400 | .00021259 | .00443561 | 1.023534 |
| 10¹⁰ | 42.13694 | 6.155000 | 1.052568 | .0018700 | .00013662 | .00212284 | .880895 |
| 10¹¹ | 51.87963 | 6.869967 | 1.085283 | .0011667 | .00019709 | .00103851 | 1.123403 |

The printed lower-tail proportions P(C_top≤20) are also correct: .29468, .09673, .02112, .00330. The analyzer fits c=E X/E W rather than estimating a universal local primality probability; its values are approximately 2.438, 2.458, 2.471, 2.469. Describe “2.46/log p” as this aggregate fitted weighting, not a calibrated conditional probability for each candidate. Its own decile table demonstrates the failure of that stronger interpretation.

### 5.4 Recomputed all-n rows

Streaming the complete histogram files gives:

| N | mean | P₀ | exp(−mean) | ratio | P₀ given small avoidance |
|---:|---:|---:|---:|---:|---:|
| 10⁷ | 3.533968 | .03843902 | .02918886 | 1.316907 | .08414384 |
| 10⁸ | 4.251019 | .01974582 | .01424971 | 1.385700 | .04607804 |
| 10⁹ | 4.988812 | .00980839 | .00681375 | 1.439500 | .02363734 |
| 2·10⁹ | 5.208960 | .00794804 | .00546736 | 1.453726 | .01926654 |
| 4·10⁹ | 5.429370 | .00643782 | .00438586 | 1.467860 | .01580346 |

These agree with §3.3. This is a stored-output arithmetic check, not another large sieve run.

## 6. What the data do and do not show

### 6.1 Zero probabilities are not full Poisson laws

The zero-probability statement is defensible at these sample sizes. Accounting also for uncertainty in the fitted mean and its covariance with the zero fraction gives approximate standardized differences for P₀−exp(−mean) of

    1.51, 0.50, −1.86, 0.65.

Thus “zero probabilities agree within approximately two estimated standard errors” is accurate.

But the Poisson identity Var X = E X fails much more decisively. For an iid Monte Carlo interpretation, estimate the standard error of Var X−E X from the influence variable

    (X−sample_mean)² − X,

centered by its sample average. The standardized excesses are approximately

    7.21, 9.68, 9.83, 8.66.

These calculations use empirical higher moments, not an assumed Poisson fourth moment. They are diagnostic sampling-error estimates, not a theorem about the PRNG. On the same sampling interpretation used by the manuscript's zero-count error bars, “X_top is Poisson within sampling error” is false. A near-Poisson zero mass can coexist with significant overdispersion elsewhere in the distribution.

The interval [N/2,N] itself still mixes scales. However, stratifying each sample into 20 equal-width n-bins accounts for only about .016–.019 of variance, whereas the excess Var X−E X is .166, .260, .324, .586 respectively. This coarse diagnostic does not prove a causal decomposition, but it certainly does not rescue the blanket claim that all deviations disappear at fixed scale.

There is also a slope-versus-level confusion. The measured mean increases by about .74 per decade, so its slope against ln N is about .32. The actual mean/ln N ratios are approximately .253, .261, .267, .271, not .32. A description such as

    “over these scales, mean ≈ .319 ln N − 1.20”

or simply “measured slope ≈ .32 against ln N” fits the observations. No asymptotic slope, intercept, independence statement or exponent c=.3 is proved.

### 6.2 The new scale-mixture evidence

Before `9b054b4b`, the claim that scale mixing explains the all-n excess was asserted from the upper-half comparison, not quantitatively established. The new stratification is a substantive improvement.

I checked the added `SCALE` loop: it groups non-squares by floor(log₂n), and records count B_b, hit sum T_b and zero count Z_b. It uses the same existing hit marks, not an independent event generator. The saved bins sum to

    ΣB_b = 124984189,
    ΣT_b = 623522683,
    ΣZ_b = 1225894.

Their mixed-Poisson prediction is

    Σ B_b exp(−T_b/B_b) = 1156445.665830,

compared with the homogeneous prediction 851611.154629. Actual/mixed is 1.060053. Thus this stratification accounts numerically for about 81.4% of the original excess zero count, leaving 69448 more zeros than the stratified Poisson prediction.

For b=24,…,29 the means are 3.338932, 3.761227, 4.183505, 4.605941, 5.031308, 5.430328; actual/Poisson ratios are 1.097450, 1.088365, 1.068644, 1.058937, 1.039626, 1.020763. The added manuscript numbers reproduce.

**Accept:** “At N=10⁹, dyadic scale stratification explains most of the all-n excess relative to a homogeneous Poisson zero prediction.”

**Do not accept:** “The excess is entirely scale mixing,” “each conditional distribution is Poisson,” or an asymptotic identification from this single-scale decomposition. The residual in this exhaustive census is not sampling noise. Narrower bins and other arithmetic features remain possible explanations; the data do not identify which is responsible.

## 7. Remaining repairs in §§0, 7, 8 and adjacent prose

1. **Poisson wording:** change the §0 lead, row 3d, §3 verdict, §3.3 ending and §8 lead to the zero-probability statement. Significant overdispersion is already in their own table. Independent-event behavior is a heuristic, not what the marginal zero data establish.
2. **Scale-mixture wording:** update row 3c to the qualified result now supported by `9b054b4b`: most of the observed excess at N=10⁹, not a complete or all-scales explanation.
3. **Mean slope:** do not identify the finite-scale slope .32 with the actual mean divided by ln N. Keep the c≈.3 extrapolation explicitly conjectural.
4. **Review record:** the modulus repair genuinely cures the previous local counterexample, but §7 should not imply that every SW/BV error vector or modulus range has been transferred without the ledger in §2.3 of this report. Incorporate this round's statistical objection rather than recording all issues as accepted repairs.
5. **Raw Chebyshev:** §8's abbreviated “Raw Chebyshev stops at N/μ” should retain the Haar/Poisson-scale variance and constant-centering qualification of Proposition 4.1.
6. **Product format:** the §3 opening still calls common-loss product bounds “useless” without specifying a fixed C>1 or inadequate accuracy. Exact/common sufficiently small losses are explicitly outside that verdict later. Use the quantitative Proposition 3.1 conclusion instead.
7. **False absolute cutoff in Proposition 3.1(b):** replace “Fix an absolute E₁′ with hit(e)≤1/2 for e>E₁′” by “Choose E₁′(N)=O(L₂L₃) so that hit(e)≤1/2 for e>E₁′(N).” Lemma 3.0(b) supplies the latter. In fact for every fixed e, hit(e) tends to 1 as N→∞: avoid any finite collection of primes ℓ≡−1 mod 4e, take the interval limit by CRT, then let that collection grow; its reciprocal-prime sum diverges. Thus the absolute-cutoff sentence is genuinely false, not merely unproved. The moving cutoff adds only the already budgeted O(L₂²L₃) small-shift cost. Round 2 also missed this point.
8. **Exact remaining gap:** TB_pow is a sufficient zero-event upper bound, not itself an assertion of a full Poisson law. “Beyond any two-shift technology” should mean “not supplied by the cited two-shift theorems,” not an exclusion of every possible amplification using two-shift inputs.
9. **Omitted events/model scope:** keep the theorem about the stated information set. Its fake law does not establish a barrier for arbitrary arithmetic PD methods, nor a lower bound on actual A_N. The present exclusions are much better than in rounds 1–2; do not enlarge them again in the summary.

## Recommended disposition

Accept the repaired local arithmetic calculation and the conditional CH-model theorem, with the explicit normalizations and domains above. Retain the top-band reduction and the checked numerical counts. Repair the absolute-cutoff proof sentence. Downgrade the full Poisson-law language to the supported zero-probability observation, and describe scale mixing as a substantial but incomplete finite-scale explanation. No depth-breaking bound, universal arithmetic barrier, or asymptotic Poisson law is established.
