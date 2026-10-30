# Hostile referee report: EXSET_CHAR_FORCING §§1–4 (Astra, round 1)

Scope: the manuscript as read in this worktree, through §4.3. Sections 5–9 are excluded. I checked the cited local arguments in CAP_POINTWISE, FORCED_WINDOW §8, CAP_BOUNDED §3, EXSET_SIEVE_MASS §4, and the z51 briefs. I also read Henriot's original definitions and the 2014 erratum's New Theorem 5 directly from the supplied PDFs. ES remains open; none of the observations below proves or disproves it.

## 1. Verdict register

| Claim | Verdict | Principal finding |
|---|---|---|
| Observation 1.1(a) | SOUND | Tautological, with the stated eventual quantifiers. |
| Observation 1.1(b) | SOUND-WITH-MINOR | Correct conclusion; the displayed proof does not dispose of small p when A > 4. Dyadic summation repairs it. |
| Observation 1.1(c) | SOUND | Bach's GRH bound applies to the unrestricted least quadratic nonresidue, not to a prescribed residue class of q. |
| Lemma 2.1 | SOUND-WITH-MINOR | Correct for odd p; its standalone wording accidentally includes p = 2, where the unit assertion is false. State the Type II converse explicitly. |
| Lemma 2.2 | SOUND | The full-stabiliser Kneser argument, involution step, and final inequality are valid. Clarify the quotient sharpness example. |
| Corollary 2.3 | SOUND | Necessary anatomy and the stated one-outside-prime sufficient obstruction are valid, for q-coprime integers. |
| Consequences 2(a), 2(b) | SOUND | Forced q = 3 always succeeds; forced q = 7 succeeds on p ≡ 1 (8). Neither assertion says unforced windows always succeed. |
| Consequence 2(c) | SOUND-WITH-MINOR | Correct dominant integer obstruction, but “exactly” and the unqualified probability asymptotic overstate it. |
| Consequence 2(d) | MAJOR | The numerical Ω bound is valid; the claimed general deterministic limit and inference to random-box behaviour do not follow. |
| §2 CERTIFIED checks | SOUND-WITH-MINOR | Small Kneser rerun passes; the script's “sharpness” test does not actually check sharpness at a prescribed nontrivial stabiliser. |
| Theorem 3.1 | SOUND-WITH-MINOR | The fixed-q upper bound and its exponents survive. The Henriot transfer is legitimate, including y tending to zero and even x. Correct the displayed summation domain. |
| Proposition 3.2 | SOUND | The integer lower bound follows from the stated construction and Wirsing. It is not a lower bound for shifted primes. |
| §3.1 “Reading” / “exact exponent” language | MAJOR | Upper bounds become asserted two-sided failure probabilities, contradicting even the manuscript's zero-failure q = 7 case on its main p ≡ 1 (8) population. |
| §3.2 growing-q assessments | MAJOR | Fixed-q estimates are not automatically uniform; the Fourier range can already be improved using the cited lemma; one random-box first-moment asymptotic is wrong even within the proposed model. |
| §3.3 numerical evidence | SOUND-WITH-MINOR | Requested independent subset agrees exactly. No asymptotic exponent or universal ordering follows from finite samples. |
| §3.4 G4 verdict | MAJOR | Useful refinement of fixed-q upper bounds, but no refutation of the parent's growing-q restriction, and no sharp shifted-prime failure law. |
| Proposition 4.1 | SOUND-WITH-MINOR | Fixed-k conclusion is valid; display the primality factor in the Euler product and retain dependence on all fixed shifts. |
| Proposition 4.2 | MAJOR | Arithmetic for multiplying the particular coarse envelopes is substantially correct; a structural 1/3 cap on the Fourier-majorant method is false. A better bound follows immediately from Lemma 8.2. |
| §4.2 “Why … must stop” / RLD identification | MAJOR | Heuristic only; neither a rigorous stopping theorem nor a reduction to the existing RLD conjecture is supplied. |
| §4.3 joint evidence / correlation interpretation | SOUND-WITH-MINOR | Finite-sample observations are evidence, not negative association or a conservative-independence theorem. |

The central algebraic lemma and the fixed-parameter analytic upper bounds are not broken. The main defects concern sharpness, uniformity, and asserted method limitations.

## 2. Observation 1.1: Linnik and Bach

### Linnik conclusion is correct, but the supplied proof loses the advertised exponent

The argument on p ∈ (X^{1/2}, X] gives X^{2/A+o(1)}. Adding the trivial X^{1/2} bound for the remainder proves only

    E(X) ≤ X^{2/A+o(1)} + X^{1/2}.

For A > 4 that is not the claimed result. Apply the same argument separately on dyadic intervals (Z, 2Z], with y = (log Z)^A and N of order Z². Products of distinct primes ≤ y already give the sufficient lower bound

    |A ∩ [1,N]| ≥ N^{1−1/A−o(1)}.

Each interval costs Z^{2/A+o(1)}, and summation gives X^{2/A+o(1)} for every fixed A > 2. Alternatively iterate the square-root decomposition instead of stopping after one step. The finitely many primes below the threshold in the eventual hypothesis cost O(1).

No exact smooth-number asymptotic is necessary. The lower bound used in CAP_BOUNDED suffices, with all small primes allowed here. On each sufficiently large interval p > y, so none of these generators vanishes modulo p.

### GRH statement and scope

Under GRH for Dirichlet L-functions, Bach's proper-subgroup bound supplies a positive integer outside the quadratic-residue subgroup below 2(log p)². The least such integer is prime: a composite least nonresidue would have a smaller prime nonresidue factor. Thus the formulation with the least prime quadratic nonresidue is valid. For p ≡ 1 (8) it is odd, since 2 is a residue.

This says nothing about restricting that prime to q ≡ 3 (4), still less q ≡ 3 (8). Observation 1.1 uses F(R) for **all** primes q in the reach. The window theorems in §§2–4 use only q ≡ 3 (4). They do not by themselves supply that F(R). Preserve this distinction explicitly when drawing conclusions about G3.

The exact logical equivalence is F(R) ⇔ eventual ES on the primes with n₂(p) ≤ R(p); on the complementary primes the implication in F(R) is vacuous. If R is merely bounded below by (log p)^A, this implies ES outside that Linnik set, but the converse from ES only outside that smaller set need not give F(R) at the larger reach.

## 3. Lemmas 2.1–2.2 and Corollary 2.3

### Window criterion and Type II correspondence

For odd p and p ∤ x,

    gcd(x,4x−p) = 1,     gcd(p,4x−p) = 1.

Consequently the divisor ratios are indeed units. The elementary two-unit-fraction criterion is valid: writing y = g y₁, z = g z₁ with gcd(y₁,z₁)=1 gives

    a g y₁z₁ = b(y₁+z₁),

hence y₁z₁ | b, and d₁=b/z₁, d₂=b/y₁ have d₁+d₂=ag. The converse formulas are integral because both d_i divide b and a divides their sum.

Since v_p(px)=1, the p-exponent in a divisor ratio is exactly one of −1,0,1, giving

    R(px) = R(x) ∪ p R(x) ∪ p^{-1} R(x).

The Type II assertion is an equivalence, not just a sufficient construction: if y=pa and z=pb, then m/x=1/a+1/b, so the same criterion produces divisors of x. Conversely such divisors give both y,z divisible by p. With a mixed pair d₁=pa, d₂=b, p ∤ ab, the constructed denominator y is prime to p and z is divisible by p, since pa+b is prime to p. Common p factors in the pair may be cancelled first. These sets can overlap; the union is not a disjoint classification of residue values.

Finally an ES solution cannot have p dividing all three denominators: after multiplication by p that would express 4 as three positive unit fractions, whose sum is at most 3. Permuting a denominator prime to p into the x position proves the final existence criterion.

Minor scope repair: write “odd prime p” (or repeat p ≡ 1 (8)). With the literal standalone hypothesis “p prime,” p=2, x=1 gives m=2 and the divisor 2 of px is not a unit modulo m. The ratio formulation is then unavailable.

### Kneser proof, line by line

1. B contains 1. Its stabiliser H is a subgroup, H ⊆ B, and −1 ∉ H. In a cyclic group of order 2u with u odd, every even-order subgroup contains the unique involution. Hence |H| is odd and H ≤ U. Correct.
2. Each g_j belongs to B. If g_j ∈ −H, H-invariance of B gives −1 ∈ B. Correct.
3. The multisummand Kneser inequality with the stabiliser of the **full** sumset is legitimate. One way to see this is to pass to G/H: the full sumset is aperiodic, and any period of a partial sumset would persist in the full sumset. Applying the aperiodic Kneser inequality successively in the quotient gives the stated formula.
4. For g_j ∉ H, the three quotient classes are distinct unless g_j² ∈ H. Since H has odd order, the image of −1 is the unique involution of G/H. Thus g_j² ∈ H, g_j ∉ H really does imply g_j ∈ −H. This is not true in arbitrary noncyclic groups; it is true under the stated hypotheses.
5. Therefore |B| ≥ (1+2n_out)|H|. Missing −1 and being H-periodic means missing the entire coset −H, so |B| ≤ (2[U:H]−1)|H|. Division gives n_out ≤ [U:H]−1. No sign or factor-of-two error.

Sharpness in C_{2d} is correct: d−1 copies of a generator give every residue except the involution, and the complement singleton makes the stabiliser trivial. To claim sharpness for a specified H in the original C_{2u}, take that quotient construction and add enough generators **inside H** that their box covers H. The full box is then the inverse image of the quotient box, with stabiliser exactly H and n_out=d−1.

The supplied script does not perform that last test. Its sharpness loop uses d−1 copies of 1 in C_{2u} and only asserts that u is missing; it neither verifies the advertised H nor equality in n_out ≤ [U:H]−1. For d<u those copies alone generally have trivial stabiliser and do not attain equality for the proposed H. This weakens the script's certification wording, not the mathematical quotient example.

I ran `scripts/z51_forcing_kneser.py 9 3`: 1,975 multisets, 908 failing boxes, no violations of (i)–(iii). Identity generators and the empty multiset are not enumerated by that script, but they reduce immediately to the checked/nonempty case or a trivial case.

### Corollary and consequences

The factorisation box equals the product of v_s(x) copies of {s^{-1},1,s}, so multiplicities are handled correctly. Forcing implies at least one prime factor outside U, hence outside H. If H=U, Lemma 2.2(iii) would allow no outside factors, a contradiction. Thus d>1 and Ω_out≥1. The one-outside-prime converse is valid because the three H-cosets cannot include −H unless s∈−H. Keep q ∤ x implicit in this group notation or state it explicitly in the converse.

For q=3, u=1 makes failure impossible. For q=7 on p≡1 (8), 2|x and 2 has logarithm ±2 in C₆. A nonresidue prime has logarithm 1,3,or5. Logarithm 3 succeeds alone; logarithm ±1 combines with one copy of ±2 to hit 3. Repetition or higher valuations cause no difficulty. The conclusion is **forced-window** success; unforced q=7 failures occur in the checked data.

Consequence (c) should say that forcing removes the dominant index-two obstruction, not “exactly” that failure event. It also removes even-parity failures with nonresidue prime factors. A concrete example is p=353, q=11, x=91=7·13: both prime factors are nonresidues modulo 11, x is a residue, and R(x)={1,2,…,9} misses −1. Thus this is an unforced failing window outside the all-factors-in-U event, also excluded by forcing. The Landau probability ≍(log X)^{-1/2} is justified for the integer semigroup event. A matching shifted-prime asymptotic is not furnished by the cited upper-bound arguments.

For (d), Ω(x)≤log₂x does make the displayed **numerical necessary inequality** automatic when q>2log₂x+3. It does not erase the separate “no prime factor in −H” restriction, turn the necessary condition into a failure criterion, or establish a random-box model. The threshold d−1<a_d log log X, a_d=1−1/(2d), is the optimisation threshold for one relaxed Rankin bound. It is not a theorem excluding all further uses of Kneser, forced parity, the factor 2, or additional structure. Rename this a limitation of the particular relaxed upper bound, not a deterministic limit on window information.

## 4. Theorem 3.1 and Proposition 3.2

### The Henriot transfer works for fixed q

Let f_y(s^a)=y for s outside H_d, s∤2q, and f_y(s^a)=1 otherwise. For 0<y≤1 this is multiplicative, takes values in [0,1], and satisfies, under cross-coprimality,

    F(a₁b₁,a₂b₂) ≤ F(b₁,b₂),
    F(n₁,n₂)=f_y(n₁) 1[P⁻(n₂)>√M].

Thus F belongs to Henriot's M₂(1,1,ε) uniformly in y. New Theorem 5 has no positive lower-bound hypothesis on F; the additional hypothesis in New Theorem 6 is irrelevant. In particular choosing y≈1/log log X does not make its implicit constant blow up.

Use Q₁(n)=n, Q₂(n)=4n−q, on a dyadic range of n. The original FORCED_WINDOW argument applies, not merely by citation but with the same local computations:

* Away from 2q there are two distinct roots; the auxiliary Euler factor is 1+f_y(s)/s+1[s>√M]/s.
* The product of root-avoidance factors contributes (log M)^{-2}; the f_y Euler product returns one power of log M minus the desired deficiency.
* At 2, Q₂ is odd. With f_y(2^a)=1, the local sum is bounded by 1+Σ_{a≥1}2^{-a}=2. Even x for q≡7 (8) is not a problem. Discarding the information carried by 2 only weakens the upper bound.
* The q factor is bounded as in Lemma 8.3. The polynomial-size condition is automatic for fixed q on sufficiently large dyadic ranges.
* Dropping the Legendre condition and any extra mod-8 condition enlarges the nonnegative sum. One must retain p≡1 (4), since otherwise (p+q)/4 is not an integer. The displayed sum over “p≤X” without this condition is not defined as written.

Fixed-q Mertens in progressions gives

    Σ_{s≤X, s∤2q, s∉H_d} 1/s = a_d log log X + O_q(1).

The error remains bounded uniformly in y because it is multiplied by 1−y. Thus the d contribution is

    ≪_q (X/log X) y^{−r} exp(−(1−y)a_d log log X),  r=d−1.

For sufficiently large X, y=r/(a_d log log X) lies in (0,1). Substitution gives

    ≪_q (X/log X)(log X)^{−a_d}(log log X)^r.

The constants include (e a_d/r)^r, harmless for fixed q. For d>ℓ_q the ratio of this bound to the ℓ_q term tends to zero: the strict power of log X wins over the fixed power of log log X. Dyadic summation preserves the claimed order; initial small ranges cost O_q(1). Full-window failure is a subset of Type II failure, so its asserted upper bound is also valid.

This verifies the theorem's exponent 2−1/(2ℓ_q) on the total count, or 1−1/(2ℓ_q) relative to a population of order X/log X. It does **not** give a matching lower bound for primes.

### Wirsing construction

Write δ=1/(2d), d=ℓ_q. The indicator that h has every prime factor in H is a nonnegative multiplicative function with prime density δ; Wirsing gives

    #{h≤Z: all prime factors in H} ∼ C_q Z(log Z)^{δ−1},  C_q>0.

There are nonresidue classes outside −H, of density (d−1)/(2d)>0 among all nonzero classes. For s≤√Y in those classes, log(Y/s) is comparable to log Y, and Mertens gives a reciprocal-prime sum of order log log Y. The representation n=s h is unique because s is the sole outside prime factor and occurs once. Its quadratic character is −1, and the coset obstruction proves failure. The claimed integer lower bound follows.

“Sharp exponent for integers” is fair, disregarding powers of log log. “Exact failure law for shifted primes” is not. The paragraph acknowledging that no shifted-prime lower bound is proved must govern all later prose. On the main p≡1 (8) population q=7 has identically zero forced failure, so a universal asserted equality `(log X)^{-a_q+o(1)}` is demonstrably wrong there.

## 5. Growing q, G4, and a concrete break in the 1/3 cap

### Uniformity is not supplied by the Rankin optimiser

The condition d−1<a_d log log X says when the idealised displayed function of y has a minimiser below 1. It does not by itself make the proof uniform in q. The Mertens remainder, the sum over divisors of u, the d-dependent optimisation constants, and the domination of the ℓ_q term must all be controlled anew. Fixed-q domination especially cannot simply be reused when d and ℓ_q grow. Uniform estimates on some small growing range may well be provable, but the manuscript has not supplied them.

### The same Fourier majorant already beats the alleged 1/3 range

This is the most concrete objection to Proposition 4.2 as a method cap. FORCED_WINDOW Lemma 8.2 proves two different estimates:

    mean(g_χ) ≤ 2/3                    for the quadratic character;
    mean(g_χ) ≤ 1/√3                  for every nonreal character.

For prime q there is exactly **one** nontrivial real character, and q−3 nonreal characters. Apply the same Henriot/Siegel–Walfisz argument separately to these two groups instead of bounding all q−2 characters by the worst real-character estimate. With L=log X and

    a = 1−1/√3 = 0.4226497308…,

it gives, uniformly in any fixed polylogarithmic q range,

    E[Σ_{χ≠1}G_χ(x)] ≪ L^{-1/3+ε} + q L^{-a+ε}.

The expectation here is the prime-population normalised average on the applicable mod-4/mod-8 progression; using the larger weight with the factor at 2 omitted handles even x as above. This is the **same Fourier L¹ majorant**, with no new arithmetic input.

It is nontrivial for q up to L^{a−2ε}, not merely L^{1/3−ε}. Under the manuscript's hypothetical loss-free product model, choose T a sufficiently small constant multiple of L^{a−ε}. For q≤T each resulting envelope is bounded away from 1 for large X. The product over admissible primes then gives a formal saving exp(−cT/log T). Thus the claimed universal 1/3 limitation on arguments multiplying these Fourier majorants is false on the manuscript's own inputs.

This does not establish the growing-k joint bound, nor does it reach Vaughan's 2/3 exponent. It does establish that “1/3” is a property of an unnecessarily coarse scalar envelope, not a cap inherent in the majorant family. One can retain an exact calculation for that explicitly frozen envelope; one cannot promote it to a barrier theorem.

### Random-box heuristic: one correct number and one incorrect asymptotic

The value 0.205 is consistent with the proposed small-ω heuristic: solving Q(α)=1/2 and multiplying α by log 3 gives 0.2050914786…. It remains a heuristic about the divisor box, not a theorem about primes or uniform residue distribution.

However, success ≈E[3^ω]/q≈L²/q for every β>2, q=L^β, does not follow even in the random-box model. Success is bounded by 1, so the relevant average is approximately

    E[min(1,3^ω/q)],

not E[3^ω]/q. In the same Poisson/Sathe–Selberg model, the untruncated first moment is dominated by ω≈3 log log X. It can be used without this saturation problem only beyond β=3 log 3≈3.29584, not just beyond 2. For log 3<β<3 log 3 the model instead has logarithmic exponent −Q(β/log 3) for success. At minimum replace the L²/q assertion by a first-moment upper heuristic and discuss truncation. Likewise |R(x)| is at most τ(x²), not literally 3^{ω(x)}; prime-power multiplicities and residue collisions require assumptions when replacing one by the other.

### G4 verdict

The fixed-q forced upper bound is genuinely stronger than the parent's coarse square-root-log estimate. This is a refinement, not a refutation of “only for q≤(log X)^ε”: fixed q belongs to that range for every positive ε. There is no proved matching shifted-prime failure probability, and the stated growing-q threshold is heuristic. Replace “Refined, partly refuted” by a precise distinction between a stronger fixed-q upper bound, an unproved growing-q heuristic, and the remaining joint problem. The subsequent “confirmed in its consequence” depends on the overbroad cap and must be weakened too.

## 6. Propositions 4.1–4.2 and the many-window interpretation

### Fixed k: valid after making the local factor explicit

For fixed distinct q_i, the k+1 primitive linear forms are pairwise nonproportional. The product of the f_i weights and the roughness indicator for Q₀ belongs uniformly in the y_i to M_{k+1}(1,1,ε). Choose Henriot's ε small enough for degree k+1. All polynomial-size thresholds and bad-prime factors can depend on the fixed tuple.

At a good prime s≤√M, multiplying the avoidance product and auxiliary Euler factor gives

    (1−(k+1)/s)(1+Σ_{i=1}^k f_i(s)/s)
      = 1−[1+Σ_{i=1}^k(1−f_i(s))]/s + O_k(s^{-2}).

The extra 1 in brackets is primality and yields the outside 1/log X. If the manuscript's displayed local factor is meant **after** extracting the prime-density factor, say so; otherwise it omits this term. Primes above √M change the product by a fixed-k bounded factor. Primes dividing 2, the q_i, or differences q_i−q_j are finitely many; their local sums converge and cost O_{k,q}(1). Small primes covering all residue classes of the product cause no obstruction to New Theorem 5, which omits primes ≤degree from its avoidance product. Individual forms remain primitive.

Independent optimisation and the finite sum over d_i then prove the stated fixed-k upper bound. This does not give uniformity as k or the q_i grow.

### What the product arithmetic actually proves

For the coarse Fourier envelope b_q=min(1,Cq/T), with C enlarged to be at least 1, one indeed has b_q≥q/T for q≤T. Hence

    ∏_{q≤T} b_q ≥ exp(−Σ_{q≤T}log(T/q)).

For all primes the sum is (1+o(1))T/log T. For admissible q≡3 (4), it is (1/2+o(1))T/log T; using all primes is a permissible weaker bound, but specify which set the equality refers to. Constants in C shift the effective endpoint and the leading constant, not the exponent. This is a lower bound on a **particular numerical upper-bound product**, not a lower bound on the actual exceptional set or on the mean of every possible failure majorant.

The analogous coarse Kneser budget has at most O(log log X/log₃X) windows in its proposed usable range, and no individual displayed Rankin envelope saves more than a power (log X)^1. This gives the stated O((log log X)²/log₃X) bound on the total logarithmic saving. “Each saving (log X)^{5/6}” is not the correct argument for an upper limit on saving: 5/6 is the smallest fixed-q exponent, not the largest. Use the bound 1 instead.

Further scope repairs are necessary:

* Uniformity in k with constant C^k does not control the q_i-dependence of Proposition 4.1. The hypothesis must be uniform in both the tuple and the parameters used at the growing scale.
* A loss-free version of the Kneser proposition does not itself assert a joint Fourier-weight product estimate. State a separate hypothetical factorisation/upper bound for the weights being multiplied.
* Proposition 4.1 counts primes for which **every chosen window is forced and fails**. The actual event “every forced window fails” allows some or all of the chosen windows to be unforced. A proof of a joint exceptional-set estimate must partition or otherwise control these character profiles. Multiplying all-window failure rates is only an optimistic budget calculation until that issue is addressed.
* Exact successful windows, especially forced q=3 and forced q=7 on p≡1 (8), can yield zero factors for some profiles. A positive universal product lower bound cannot cover arbitrary strengthened majorants; it must be restricted to the specific generic scalar envelopes being studied.

Most importantly, the real/nonreal split in §5 of this report invalidates the proposed 1/3 cap for the Fourier family itself. Its qualitative comparison with much stronger known exceptional-set bounds may still be retained, with carefully specified assumptions and a corrected exponent, not as a theorem ruling out every use of these mechanisms.

### “Why the per-window majorants must stop” is not a proof

Cardinality of a divisor-ratio box alone does not bound the probability of hitting the **specific** target −1. A tiny box may always contain that target on an arithmetically constrained family. The implication “typical box size ≪q ⇒ success probability tends to zero” needs a random-target/equidistribution hypothesis. Likewise a mean lower bound on a failure majorant says nothing by itself about products over very many weak events; individually tiny savings can accumulate.

The asserted collective intensity uses typical box sizes where an annealed first moment may be dominated by atypically factor-rich shifts. It suppresses forcing and residue-class constants and the dependence among the different shifts. These may be acceptable modelling choices if explicitly labelled, but they are not a derivation of a joint failure law. A heuristic exp(−L^{1.1−o(1)}) would imply an expected exceptional count tending to zero, so it is particularly important not to phrase this as a proved saving.

“Janson/RLD-type lower tail” is a sensible research description. It is not an established reduction to z50's RLD-U statement: the event family, ambient probability space, forcing conditions, overlaps, and requisite uniformity differ. Classical Janson does not become applicable just by naming many rare divisor events. State the proposed lower-tail conjecture precisely, or call this an analogy. “It is not a sieve statement, and G2 applies to every sieve route” also exceeds the scope of the audited architectures; no proof here classifies all possible sieves or all uses of non-CRT information.

Finally, §4.3's smaller observed variance and selected lower-tail probabilities do not prove pairwise negative correlations, negative association, or stochastic domination by an independence model. At most they show a thinner tested lower tail and reduced aggregate variance in these samples. The two-prime and one-prime tail counts should not support a universal conservative-independence claim.

## 7. Independent numerical audit

I wrote `reviews/z51-forcing-r1-astra-check.py`, importing no campaign mathematics code. It independently sieves primes through 1,030,000, factors each x=(p+q)/4 by trial division, enumerates its integer divisors, and forms all divisor ratios modulo q. It independently forms the divisors of px as D(x)∪pD(x) and recomputes their ratio set; it does not use the manuscript's p^{±1}R(x) formula for the test. Forcing is computed by Euler's criterion modulo p and cross-checked modulo q.

Command:

    ulimit -v 8000000; timeout 120s uv run --no-project reviews/z51-forcing-r1-astra-check.py

All executed shell checks used the requested memory limit and timeouts. The prime sieve occupies about one megabyte; ratio sets contain at most q−1 residues, and no large Cartesian-product array is stored.

Results for the inclusive interval [1,000,000,1,030,000]:

    primes p≡1 (8): 571
    admissible q≤100: 13
    window pairs: 7,423
    stored-pattern mismatches: 0
    S=2170, f=423, F=1148, u=1333, .=2349
    all full-window successes: 4361
    unforced full-window successes: 1768

The stored file covers exactly these 571 primes, with no missing, extra, or duplicated prime in this interval.

| q | Forced | Forced Type II successes | Forced full successes | Unforced | Unforced Type II successes |
|---|---:|---:|---:|---:|---:|
| 3 | 285 | 285 | 285 | 286 | 164 |
| 7 | 290 | 290 | 290 | 281 | 214 |
| 11 | 286 | 205 | 222 | 285 | 103 |
| 19 | 280 | 148 | 191 | 291 | 99 |
| 23 | 289 | 246 | 269 | 282 | 146 |
| 31 | 280 | 210 | 231 | 291 | 147 |
| 43 | 279 | 82 | 141 | 292 | 69 |
| 47 | 297 | 188 | 231 | 274 | 118 |
| 59 | 282 | 81 | 117 | 289 | 31 |
| 67 | 282 | 52 | 101 | 289 | 37 |
| 71 | 284 | 165 | 200 | 287 | 84 |
| 79 | 300 | 155 | 210 | 271 | 91 |
| 83 | 307 | 63 | 105 | 264 | 30 |

For forced pairs, all three quantities—forcing, Type II success, and full success—are compared against the stored character. For unforced pairs the format records only Type II success (`u` or `.`), not full success. I computed the latter independently but cannot claim to have compared an unrecorded bit. In particular `.` is not a stored assertion of full-window failure.

This validates the requested subset, not the entire four-scale tables or the joint-tail scripts. It confirms the forced q=3,7 conclusions and the distinction between Type II and full certificates.

## Overall verdict

**MAJOR revisions required, but no fatal flaw found in the central fixed-parameter results.** Lemma 2.2, Corollary 2.3, the fixed-q upper bound of Theorem 3.1, the integer construction in Proposition 3.2, and the fixed-k bound of Proposition 4.1 survive hostile checking. The numerical subset matches exactly. The manuscript is not yet reliable as a barrier or sharp-failure-law document: it repeatedly promotes upper bounds to asymptotics, fixed-parameter arguments to uniform ones, and random-box assumptions to method limitations. In particular its advertised Fourier 1/3 cap is defeated by separating the unique quadratic character from the nonreal characters using its own cited lemma. The publishable internal contribution is presently a sound subgroup anatomy and fixed-parameter upper-bound analysis, with explicitly speculative growing-window conclusions—not a new confinement theorem or a proved classification of all many-window routes.

## Required repairs

1. Repair Observation 1.1(b) by dyadic summation; distinguish unrestricted least nonresidues from q≡3 (4) windows, and state the exact reach-dependent equivalence.
2. Restrict Lemma 2.1 to odd p, make the Type II converse explicit, and clarify quotient versus lifted sharpness in Lemma 2.2 and its certification script.
3. Replace “exactly removes,” unqualified Landau probabilities over shifted primes, and the general “deterministic limit” by statements with the proved scope.
4. Retain Theorem 3.1 as a fixed-q upper bound, restore p≡1 (4) in its summation, and remove every asserted matching shifted-prime failure asymptotic, especially on the q=7 main population.
5. Prove any claimed growing-q uniformity separately; do not infer it from the Rankin optimiser or fixed-q dominance of the least-divisor term.
6. Incorporate the real/nonreal Fourier split, withdraw the structural 1/3 cap, and restrict any retained product-budget calculation to explicitly specified scalar envelopes and uniform joint hypotheses.
7. Correct the random-box first-moment truncation and weaken the G4 verdict: stronger fixed-q bounds do not refute the parent's growing-q restriction.
8. Display Proposition 4.1's primality Euler factor; for growing windows address q_i-dependence, character profiles, exact-success windows, and the separate joint estimate needed for Fourier weights.
9. Label the collective-window/Janson/RLD discussion as a conjectural analogy unless an explicit implication is proved; weaken the finite-sample negative-correlation and conservative-independence language accordingly.
