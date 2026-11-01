# Hostile review of Z53_HCSHIFTS.md

**Overall verdict: UNSOUND as written.** The fixed-window arithmetic theorem W, the argument of W2 for its particular family, W3, and the substantive parts of Lemma C survive. However, the advertised universal growing-window wall does not follow, the model's boundary-scale calculation is wrong, and several empirical claims contradict or exceed the supplied evidence. These are substantive changes to the headline conclusions, not just editorial repairs. Nothing reviewed proves or disproves ES.

Locations below refer to `Z53_HCSHIFTS.md` unless another file is named.

## Issues

### 1. CRITICAL — The fixed-family theorem is promoted to an unproved universal growing-window impossibility

**Locations:** lines 12–16, 137–138, 320–322, 416–419, 429–430, 436–439.

W fixes X and a family. Its spacing argument leaves the least member uncontrolled. When X and the family vary, one exceptional least member per family can form an infinite sequence. Thus the theorem does not establish the stated restriction for an arbitrary family of constructions with X=X(p). There is also no argument that every Hypothesis-H certificate must formally factor every window integer as required in W's explicit hypotheses.

Furthermore, even ignoring these problems, the proved bound is approximately **4 log p**, not **log p/log log p**. It cannot exclude H-type constructions throughout the advertised “dark range.” The latter boundary comes only from a separate BH assessment. The coefficient-one target HC≤log p is also not excluded as a possible target of refutation by a bound permitting X up to 4 log p.

**Fix:** State W as a fixed-window, fixed-factorisation-family result, applying its quantitative bound only to nonleast members. Any growing-family corollary needs an additional uniform argument controlling the selected members. Remove the universal H-type impossibility claims and the assertion that W excludes the whole dark range.

### 2. MAJOR — The model boundary calculation is false; equality A=2 log 2 is wrongly excluded

**Locations:** lines 45, 309, 317–322, 426–430.

For fixed M>0 the cost at X=M exp(2λ log 2) is not O((log M)e^λ). A missing critical-window contribution already has size at least c√λ e^λ.

Indeed, writing W for Poisson(λ), summing the linear part of the hit probability over coordinates x≥2^W gives a constant multiple of

    E[2^W (log X − W log 2)_+]
      = e^λ E[(log M + (2λ−V) log 2)_+],  V ~ Poisson(2λ).

The expectation on the right is asymptotic to (log 2)√(λ/π) for fixed M. Restricting to multiples of four only changes a constant; replacing x by φ(x) cannot remove this lower bound. Since −log(1−hit)≥hit, it is also a lower bound for the actual model cost.

Consequently the model gives a summable upper bound

    P(HC > M(log p)^(2 log 2)) ≤ exp(−c log p √(log log p))

for every fixed M>0. Borel–Cantelli therefore works even at M=1, without independence between primes. The assertion “iff A>2 log 2” is false for the stated model: the boundary exponent also works. The asserted dark range “every X<(log p)^(2 log 2)” is false even internally: take X=½(log p)^(2 log 2).

**Fix:** Correct the boundary calculation and include A=2 log 2. State lower-tail predictions for fixed exponents strictly below 2 log 2, not all functions lying below the boundary. The logarithmic limsup exponent can still be 2 log 2 after specifying the cross-prime model.

### 3. MAJOR — The model specifies within-prime independence, not a joint law across primes

**Locations:** lines 292–295, 314–318; summary lines 43–44.

The marginal probability exp(−(log p)^{g+o(1)}), g<1, establishes an **expected** count P^{1−o(1)}. It does not by itself establish an almost-sure counting function, infinitely many exceedances, or the lower bound for a limsup. Highly dependent cross-prime couplings can have the same marginals and no eventual exceedances.

**Fix:** Explicitly add independent draws across primes, or another sufficient concentration/second-Borel–Cantelli assumption. Under that extension, the subcritical count and the model-internal prediction against every fixed C log p are defensible. “Predicted false in this model” is appropriate; “the old conjecture should be retired” (line 442) is not warranted by these data.

### 4. MAJOR — L1's advertised accuracy is contradicted by the data, and the conditioning variable is misstated

**Locations:** lines 269–275, summary lines 36–37, proposed FRONTIER line 424.

The engine bins by **floor(log₂ τ)**, not by τ=2^b. The bins contain all τ in [2^b,2^{b+1}). The current files do not even store the sum of τ needed for a true mean-τ comparison.

Examples satisfying the claimed 2^b≥φ(x)/4 condition:

- x=23, level, b=3: observed 0/12,263 at 10⁹ and 0/8,542 at 10¹³, versus model 0.1662.
- x=23, level, b=4: 7,281/43,448=0.1676 at 10⁹, versus 0.3049.
- x=31, level, b=4: approximately 0.0832, versus 0.2341.

These are not “within a few %.” Even at 2^b≥φ(x), the claimed mean-count ratio 0.9–1.2 is unsupported: for x=31, level, b=5 at 10⁹, sumcert/count divided by 2^b/φ(x) is 0.7376. The true mean τ in that bin is at least 2^b, so using it only decreases this ratio.

Scale stability of the discrepancies is real, but stability is not accuracy or evidence that τ is the only relevant anatomy variable. The “fires only if τ≳φ(x)” language (lines 48–49, 328–330) is also not a necessary condition: the model itself gives a positive firing probability below that threshold. A dominant large-deviation contribution is not a requirement on every certificate or every proof.

**Fix:** Describe a rough, scale-stable occupancy comparison with substantial systematic exceptions. Use exact-τ bins or record sum τ; remove the universal accuracy and “only through τ” claims.

### 5. MAJOR — L2 does not establish conditional independence or independent private anatomy

**Locations:** lines 38–39, 277–284, 292–295, 339–341, 425.

Both independence scripts first OR the endpoint and level masks. They test products of **coordinate miss events**, not independence of both integer types used in model M. They compare one nested all-miss statistic with fitted products; they do not test the full joint distribution or the factor anatomy. At M=15015 there are 5760 reduced residue classes, averaging only about 104 observations per class, with the same observations used to fit and evaluate the product.

The recorded ratios reproduce, but do not justify “lines are independent” or “the private parts act independently.” Nor do positive correlations at the sampled thresholds prove that all relevant extreme joint-tail probabilities dominate an independent model. Pairwise positive correlation alone would not imply that either.

**Fix:** Say that small-prime conditioning substantially reduces the observed all-miss excess for these coordinates and sample sizes. Add held-out/uncertainty analysis and a separate endpoint-versus-level test before making stronger empirical claims. Keep cross-line/private-factor independence as an explicit model assumption.

### 6. MAJOR — The universal BH upper-limit assessment assumes an unjustified singular-series bound

**Location:** lines 171–175.

The algebra yielding 4/3 is correct **if** k∼3X/4, the parameterisation has density 1/Q, and log SINGULAR_SERIES=O(k log log X). But the assertion SINGULAR_SERIES≤(C log X)^k for **any** Dickson family is not established and is not generally true with unrestricted coefficients. Refining a family into a progression modulo a new large primorial can make the local factors, hence the singular series, arbitrarily large at fixed X. The increased progression modulus must be accounted for jointly.

Also, an expected count below one is a typical-first-occurrence heuristic, not a statement that members “exist only if” the inequality holds; searching over families requires further accounting.

**Fix:** Restrict this calculation to the displayed family or a precisely bounded class of parameterisations, and call 4/3 a typical first-hit threshold. Do not use it as a universal exclusion theorem.

### 7. MAJOR — Remark 3.1's PROVED label covers an unproved methodological universal

**Locations:** lines 32, 221–234, 431–432, 443–444.

The divisor-count identity, the congruence descriptions of individual small-divisor events, and the stated smooth-product upper bound are sound. They do not prove that **every** forced structure/divisibility of a shifted family is congruence data, or rule out all other deterministic joint-factorisation mechanisms. Likewise, “congruence data cannot force a firing line at sub-power windows” needs a defined class of certificates and a specified window scale; the cited results do not establish that unrestricted formulation.

The H4 imports must also specify the allowed κ: e.g. any fixed 0<κ<1/12 for the ordinary-PNT route, or the separately qualified <1/6 route. They are not statements for arbitrary κ.

**Fix:** Retain PROVED on the explicit identities and scoped consequences of H4/W3. Label the methodological interpretation Assessment and say “the structures examined here,” not “every forced structure.”

### 8. MAJOR — “Private-type” is conflated with actual shift privacy and with the type of a reported certificate

**Locations:** lines 27–30, 55–56, 78–89, 350–363; `scripts/z53_hcshifts_hc.c:72–76`.

Two different problems:

1. W3 splits the (X+1)-rough part. This does **not** ensure primes private to the combined endpoint/level window; that requires >X². Explicitly, X=8, Q_X=529200, p=2646001 is prime and p≡1 mod Q_X. The prime 31 divides both p+4 and 8p+1. Moreover d=31 is a private-type endpoint-4 certificate in the memo's terminology. Thus the conclusion about primes “private to one shift” does not follow from W3.
2. The C engine's type flags are existential: C means **some** certificate at HC is congruence-type, and P means **all** certificates there are private-type. They are not the type of the displayed divisor or the fraction of individual certificates. For example p=1003553329, HC=23, displayed d=1049742 is private-type relative to y=23, but the output flag is C because another divisor is congruence-type. My independent enumeration reproduces this.

**Fix:** Use “rough-splitting” for W3 unless the privacy threshold is actually X². Relabel the tables as the fraction of primes for which **every** HC-certificate is private-type, or compute a specified representative/per-certificate statistic. For the “y-smooth modulus determines d mod x” explanation, require at least that every prime factor of x is ≤y.

### 9. MINOR — Stale independence data and two incorrect numerical/generalisation sentences

**Locations:** `data/z53/hcshifts/indep_product_of_marginals.txt`, lines 360–362 of the memo.

- The committed raw-independence file's 10¹³ block contains **413432**, not 600000, observations. Rerunning on the final sample gives ratios 3.02, 3.65, 4.46, 18.43, 14.09 at X=7,8,12,15,16; the committed partial block has 3.07,3.71,4.17,16.06,8.19. Regenerate it.
- “Falls steadily ... at every HC≥8” is contradicted even by the displayed bins: the ≥20 congruence share rises from 0.964 to 0.971 between 10⁹ and 10¹⁰. Replace with a qualified trend and acknowledge small counts.
- The explanation of 100% private-type at HC=8 invokes an 8-smooth part that is a power of 2. Both integers at x=8 are odd. For p=66529, their 8-smooth parts are 3². The observed statistic survives, but this explanation does not. A repair uses HC>7 to exclude factors 5 and 7 in the x=8 integers, leaving powers of 3, whose residues generate {1,3} modulo 8, not −1.

### 10. MINOR — Domain and hypothesis qualifications are missing

**Locations:** lines 66–67, 104–110, 142–148, 224, 236–246.

- The definition ranges over all x∈C, so “p>x” is not automatic and p+x need not be coprime to x. State X<p, or gcd(p,x)=1, wherever the unit-group reasoning is used. In the level small-divisor sentence, the right condition is gcd(d,p)=1, not merely d∤p, unless X<p is assumed.
- W should explicitly say the irreducible factors and constants have the integral interpretation used in the proof, with nonzero integer C_i. Theorem M supplies this for these integer window polynomials. Its conclusion should not be extended to formal runs lacking the window-factorisation hypotheses.
- UBH should explicitly require distinct nonproportional primitive forms and positive integer s. If repeated forms are allowed, its displayed singular series diverges, so the literal universal formulation is not meaningful.
- Lemma C(b) gives a necessary compatibility condition on the total product, not sufficient confinement of the actual prime factors. The summary's “exactly” and the reading “non-square-ness ... only through unconfinable lines” overstate what is proved, especially for composite odd coordinates. Say “the total-product obstruction to confinement.”

### 11. MINOR — Computation coverage and engine limits need accurate descriptions

**Locations:** lines 51, 346; `scripts/z53_hcshifts_hc.c:48–49,79,89–91`; `scripts/z53_hcshifts_linnik.py`.

- Range/list mode usually stops at x=128 once all auxiliary minima are found. It does not evaluate all lines to 256 for every sampled prime. The HC values remain valid; say “cap 256, masks through 128, with early termination.” The separate lines mode does evaluate to 256.
- The 65536-divisor buffer has no bounds check. It is safe for the actual sample and hard-prime ranges: independent exhaustive exponent enumeration bounds τ by 32256 and 64512 respectively. It is not justified as a general size bound at the advertised ~10¹⁵ input range: integers below 256·10¹⁵ can have 80640 divisors. Add a guard/dynamic storage and validate XCAP (the aggregate arrays have length 260).
- The W3 script checks (i) only on C-coordinates, although its header promises all 1≤x≤X. I independently checked the missing coordinates too; all 440 line instances pass. Extend the checker to match its advertised scope.

## Proof audit: what survives

**W, fixed-family statement:** The proof works. The ℓ−1 multiples 4,8,...,4(ℓ−1) cover every nonzero class mod odd ℓ, so the counting is correct. After selecting one sufficiently large admissible q, divisibility comes from a fixed c or C_i and therefore forces the same residue for **every** admissible q′, including the discarded ones. Thus the proof actually gives one class for the entire family and “all but the least” for every such polynomial family, not just linear ones. The spacing bound and θ(⌊X/4⌋+1)=(1/4+o(1))X are correct. This sharpening does not remove issue 1's growing-family exception.

**W2, displayed family:** With UBH clarified, each step checks: distinct linear forms, admissibility from s=0, k=1+2|C_X|≤3X/4+3, Q|24·lcm(1,...,X+1), log Q≤(1+o(1))X, and coefficients ≤XQ. The small-prime singular-series product is ≥exp(−θ(2k)); the large-prime estimate gives log loss O(k/log k). Taking log S=C₂X log X with C₂≥2C₁ sufficiently large satisfies UBH and makes the lower bound grow, rather than merely become positive. The inversion yields X≥(1/C₂−o(1))log p/log log p; p≥Q+1→∞ establishes distinctness. The unconditional mathematical deduction from this explicitly nonstandard hypothesis is sound.

**W3:** Q_X, its exponents, log Q_X=θ(X+1)+ψ(X+1), the smooth-part equality, r≡1 mod x, and the proper-splitting argument all check. The latter correctly uses x−1|(x+1)⇒x≤3. The least primes tend to infinity since p≥Q_X+1. The constants 1/(2L) and 1/4 follow correctly.

I visited [LLS, §1.2 and Corollary 1.2](https://arxiv.org/html/1309.3595): it explicitly cites Xylouris's admissible L=5.2 and states, under GRH for q>3, P(a,q)≤(φ(q)log q)². [Tao's constants page](https://teorth.github.io/optimizationproblems/constants/65a.html) also supports the dissertation attribution of L=5. No attribution error in those claims.

**Lemma C:** (a) and (b) are elementary subgroup facts; (c) is correct on the stated unit domain; (c′) correctly uses q−1=2m with m odd. In (d), −x is a negative discriminant for both allowed kinds of x, so the Kronecker character really is an odd Dirichlet character modulo x, possibly imprimitive. The missing prime-2 sentence is easy: for 4|x both integers are odd; for x≡7 mod 8, χ_{−x}(2)=1. For odd prime factors the displayed square arguments give character +1. Thus (d), with its coprimality hypothesis, is sound. In (e), a≥3 and the three actual divisors 2^j m, j=0,1,2, sweep the nonsquare coset modulo 7; the proof is correct.

**Subcritical model calculation:** For fixed 1<κ<2 the Poisson rate Q(κ)=κ log κ−κ+1, the truncated exponential-moment calculation, and g(κ)=κ(1+log 2−log κ)−1 are correct. g′(κ)=log(2/κ)>0, g(1)=log 2, g(2)=1. At X=log p, g=0.9139286679440657. The numerical script reproduces 0.804,0.924,0.990 at λ=160. Do not extrapolate this g-formula to κ<1 or κ>2; the summaries should retain its stated domain. The boundary and cross-prime conclusions need issues 2–3 repaired.

## Numerical and implementation verification

I read the memo fully and audited all named scripts. Commands used timeouts and Python/compiled jobs had a 6 GB virtual-memory cap. No repository file was edited and nothing was committed.

- Reran `z53_hcshifts_linnik.py`: exit 0 and output identical to the committed report. All ten primes, X/log p ratios, HC=4, and certificate counts **42,28,14; 60,28,100; 92,98; 104,64** reproduce. Independently checked smooth parts at all coordinates, not just C.
- Regenerated sample summaries from all **3,000,000 raw rows**: every histogram, tail, maximum, and reported existential type fraction matches. Thus the five main numerical table rows are transcribed correctly, subject to issue 8's statistic interpretation.
- Regenerated fire-law summaries, confinement reports, and hard-prime anatomy reports: all nonheader output matches the committed files. Independently recomputed the stratified products by streaming aggregation; all ratios match. The raw-independence partial-sample discrepancy is issue 9.
- Recompiled the C engine and reran all **166 hard primes**: byte-identical output. Independently used PARI factorisations/divisor enumeration for all 166 through coordinate 256 and another **500 systematic sample primes** through 128: zero discrepancies in HC, masks, divisors, certificate counts, existential flags, and the applicable auxiliary minima. The listed z49 values, 14 (★)-zeros, and six Dickson-instance HC values all match.
- Raw controls reproduce **5000/5000 sterile squares** and 2000 near-square primes for each k. Exact HC>4 rates for k=1,8,9,16,17,24 are **0.0355,0,0.1065,0.048,0,0.063**; maxima are **16,4,12,8,4,23**. The k=8,17 modulo-3 explanation is correct.
- The hard-anatomy table matches **3.15/3.11/3.21 versus 3.80/3.99/4.14**, hit sums **22.07/22.85/30.57 versus 43.39/52.10/60.85**, and the stated residue/Legendre counts. The confinement table matches throughout.
- Reran the forced-prime calculation: X=4096 gives contiguous maximum **1033** and log-product/X **0.2537**. The other quoted approximations agree, with the precise range over 64...4096 being **0.2379–0.2845**.

The C engine implements the HC divisor criterion correctly. Its trial division, deterministic Miller–Rabin bases in the used range, Brent/Pollard-rho splitting, divisor enumeration, and rough-part gcd test pass inspection and independent checks. Not resetting rho's accumulated product at every block is not a correctness error: previous products are units while their gcd is one, and the gcd=n fallback retraces the current block. uint128 modular multiplication prevents product overflow; the actual largest hard-window integer is **88,359,330,802,176,257**, well within uint64. The main engine issues are output semantics and unchecked general limits, not corrupted HC values.

**Disposition:** Keep the scoped arithmetic results and corrected finite evidence. Rewrite the headline wall, empirical “laws,” model boundary, and proposed FRONTIER text before circulation. The defensible outcome is a useful fixed-family obstruction and rough-splitting construction, plus a speculative subcritical extreme-value model—not the current universal no-go or definitive recalibration of the conjecture.
