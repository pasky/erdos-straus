# Hostile review of Z53_LATTICE.md

## Verdict

**No fatal defect found in the quantitative, full-rank theorem actually defined by (E), (S), (V).** Proposition 2.3 and Theorem 2.6 survive the repairs below, with the advertised threshold 1.34·10¹⁶. The fixed-C local bounds and area argument also survive; its displayed inequality needs correction.

**Major revisions are necessary before promoting the conclusions to FRONTIER.** The memo repeatedly substitutes “no exactness cosets,” “factorization needed,” and “no Thue/Minkowski certificate” for substantially narrower statements. Those substitutions are not justified. There are also an incorrect Coppersmith/CHN identification and an incorrect empirical significance claim.

I read the entire memo, checked the proofs, inspected all three requested checking/enumeration programs and the summary program, and performed the bounded reproductions recorded below. No repository source/document was edited.

## MAJOR findings

### M1. The scope does not exclude general Thue/Minkowski arguments

**Locations:** Definition 1.1 and scope remarks, lines 57–70; summary lines 13–15, 28, 41–43; §3.2 reading, lines 244–247; §§7–9, especially lines 345, 359–380.

The equivalence

    K + Λ = R³  ⇔  K meets every real translate of Λ

is correct. Thus (V) is necessary for a theorem guaranteeing intersection with *every real translate*, with the same K and Λ. It is not necessary for intersection with a particular arithmetic coset, with just the cosets satisfying (E), or for a homogeneous Minkowski argument. Merely calling a theorem “translation-uniform” must not silently erase arithmetic restrictions on its translations.

For example, for Λ = MZ × Z and M > 8, the origin-centered disc of radius √(2M) satisfies Minkowski’s volume hypothesis but does not cover R² modulo Λ. Homogeneous lattice-point existence is not a covering theorem.

The classical motivating argument also excludes the origin *after* applying Minkowski. Its exactness region {0 < x²+y² < 2p} is a punctured disc, not a convex disc; the full convex disc fails |x²+y²−p| < p at the origin. Definition 1.1 excludes analogous exceptional-point/sign-selection arguments by construction. The observation about a symmetric body centered at a positive coset point does not exhaust those possibilities.

The quantitative result is nevertheless nonvacuous: its proof actually excludes all (E),(S) convex positive bodies with **vol K ≥ index Λ**, even without covering. State precisely that useful result. Do not identify it with a universal impossibility theorem for geometry of numbers.

Likewise, “no exactness cosets” is literally false: for every D,

    t = (0, −n, 0),  Λ = DZ³

satisfies (E). Its coset also has positive representatives. Theorem 2.6 excludes a compatible sufficiently large convex body, not the coset itself.

Proposition 3.2 has a parallel scope restriction: it imposes divisibility at *all* coset points with C ≥ 1, not just points on the quadric or in a selected exactness body. Its proof does not apply to the latter because the C-shifts leave the quadric.

**Fix:** consistently say “full-rank convex positive-shell volume/covering schemes satisfying (E),(S),(V).” Keep broader assessments explicitly open; do not replace the entire M1b assessment by a general Thue/Minkowski impossibility claim.

### M2. “Every affine-linear encoding” omits the essential rank-three restriction

**Locations:** summary lines 13–15; Theorem 2.6 lines 177–188; §§8–9 lines 351, 371–379.

The stated reduction works for rank-three A. It does not cover lower-rank encodings. The unrestricted wording has explicit counterexamples of arbitrarily large height:

    n = 8m − 3, m ≥ 2;
    Φ(v) = (1, 2, v), Λ = Z, t = 0, D = 8;
    K = [m − 1/2, m + 1/2].

Here G_n(Φ(v)) = 8(v−m), the congruence holds on all integers, Φ(K) is positive, |G_n∘Φ| ≤ 4 < 8, and K+Z = R. This is a rank-one affine-encoded scheme for arbitrarily large odd n.

**Fix:** say “every rank-three integral affine encoding.” Lower-dimensional slices beyond the particular fixed-C treatment remain outside Theorem 2.6.

### M3. The fixed-C gcd bound does not imply being handed a factorization

**Locations:** summary lines 23–26; §3.1 title and reading, lines 201, 229–232; §3.2 reading; §§7–9.

The theorem supplies a necessary inequality for d = gcd(D,N_C). But **d may equal N_C**, which is explicitly known without factoring anything. Choosing D=N_C automatically satisfies the claimed “large divisor” requirement. Even the exactness coset can be constructed without factoring:

    u ≡ −n (mod N_C), B arbitrary;
    g(−n,B) = −N_C B.

This coset has index N_C. This does not assert a compatible K exists; it shows why the gcd condition is not a factorization obstruction. A large possibly composite divisor also need not supply a divisor in the desired residue class.

**Fix:** retain the quantitative necessary gcd bound, but remove “handed (almost) the factorization,” “the lattice contributes nothing beyond the divisor,” and “factorization needed.” To derive those assertions one needs a separate theorem excluding the trivial divisor N_C and extracting useful arithmetic information.

### M4. The integer-Coppersmith guarantee is not exactly the CHN boundary

**Locations:** summary lines 33–36; §5.1 lines 295–300; §5.2(c), lines 322–324.

I checked Coron's original paper, *Finding Small Roots of Bivariate Integer Polynomial Equations Revisited*, Theorem 2 and §2, at http://www.jscoron.fr/publications/bivariate.pdf. The quoted theorem **does** say XY < W^{2/(3δ)}; this citation and δ=1 are correct. Do not “repair” it by replacing it with the stronger epsilon condition of Coron's own simplified algorithm.

For a positive root in an origin-centered box, however,

    W = 4CXY,   XY < W^{2/3} ⇔ XY < 16C².

Thus an individual root fits such an admissible box iff **uB < 16C²**. Since 4CuB = n+u+B, this is not exactly the CHN test (4C)^4 > 4Cn+1.

Concrete counterexample: n=53 and (u,B,C)=(1,18,1). It is CHN-visible in the C-slice since 256 > 213, but any box containing this root has XY ≥ 18 > 16, so the quoted unshifted bivariate guarantee does not apply. The two regimes have the same leading exponent C ≍ n^{1/3}, not the same exact boundary. Also, failure of a sufficient small-root bound does not prove algorithmic unreachability.

Section 5.2(c) further claims polynomial-in-log-n decisions at the CHN *boundary*, although §5.1 correctly notes degeneration as α↓1/4. Fixed-epsilon CHN guarantees do not justify that uniform runtime. Its √n count of u-slices also requires explanation: by symmetry the smaller coordinate is O(√n), but visibility might occur only in the larger coordinate. For example (1,(n+1)/3,1), with sufficiently large n≡5 mod 6, is visible only in the large B-slice among the three CHN tests. Restricting to the smaller u discards that visible slice.

**Fix:** state the exact box condition, describe the shared asymptotic exponent, and retain fixed epsilon (or provide a separate uniform complexity argument). Do not turn a sufficient guarantee into an “iff reachable” statement.

### M5. Five exceptional-prime angles are small, not six

**Locations:** summary lines 38–40; §6 lines 332–334; checks script lines 19–21.

Both the printed list and a fresh run on all fourteen exceptional primes give exactly **five** b/a < 0.16: p=409, 577, 1134241, 5212561, 8813281. The claimed six is an arithmetic error.

The null probability is p₀=arctan(0.16)/(π/4)=0.2020… . The relevant binomial tail is

    P(Binomial(14,p₀) ≥ 5) = 0.1341898564…,

not 0.046. The latter is the correctly calculated tail for the incorrectly supplied count six. No nominal 5% significance survives, even before selection/multiple-testing caveats.

**Fix:** replace six by five and the tail by 0.134; ideally compute the count from the actual observations rather than hard-coding it.

### M6. Density-model shares and subset-counting do not establish the broader conclusions

**Locations:** summary lines 33–36, 41–43; §3.3 lines 250–257; §5.1 lines 301–304; §8.

The fractions 1/4, 4/9, 9/16, 4/9 and 1/36 are correct for the specified log-triangle density model. They are not proved proportions of actual R(n) for prescribed n or primes. In particular, the 35/36 statement is a model mass share, not a statement that every finite root set has that fraction of Lenstra-visible triples. The summary blurs this distinction.

Likewise #((Λ+t)∩S) ≤ R(n) does not imply that proving this subcount positive is “never easier” than understanding R(n). A structured subset can be much easier to certify than the full count. The volume bound supplies no complexity or logical reduction in that direction. The claim that no geometry-of-numbers route remains is not a consequence.

**Fix:** label the shares “proved density-model integrals; actual-root asymptotics not established.” Retain the non-convex observations as limited assessments, without an exhaustive no-go conclusion.

## MINOR findings and concrete repairs

### m1. Incorrect extraction at 2, but the final local estimate survives

**Location:** Proposition 2.3, line 106.

From s=±1 one gets 2Q≡0 and **2(L+T)≡0**, together with L+Q+T≡0. One does not generally get L+T≡0 at the original modulus.

Counterexample within the actual setting: modulo 8, take n=7, t=(0,1,0), h=(1,7,1). The entire cyclic coset t+⟨h⟩ is exact, but

    L(h)=−8, Q(h)=4, T(h)=28, L(h)+T(h)≡4 (mod 8).

The s=2 equation still gives 2L+8T≡0, and subtracting 2L+2T≡0 gives 6T≡0. Hence Q,T,L all vanish modulo 2^{f−1}, exactly as needed later. At odd primes the stronger extraction is valid.

**Fix:** change the first extraction to 2(L+T)≡0 and derive 6T by that subtraction.

### m2. False displayed comparison in Theorem 3.1

**Location:** line 206, “Cn/114 > N_C/456.”

In fact Cn/114=(N_C−1)/456 < N_C/456. Fortunately the desired final constant is valid. Keep n′=n+1/(4C), rather than weakening it to n, in the area bound. The same comparison yields

    d ≥ 9Cn′/1024 = 9N_C/4096 > N_C/456.

It also yields d ≥ 9Cn/1024 > Cn/114. State these as separate consequences, not the false chain.

### m3. Numerical cutoff parenthesis and volume quotations

**Locations:** Theorem 2.6 lines 185–186; lines 191, 195–197, 361, 368, 378.

Recomputed values:

    c₀ = 276.91191749902237;
    thin-case limiting n = 253522375.1111108…;
    root for coefficient c₀/4 = 7.83485231274335·10¹⁴;
    root for the rounded coefficient 69.23 = 7.83567339041654·10¹⁴.

Therefore the claim that the rounded-coefficient function is positive everywhere beyond 7.835·10¹⁴ is false. The asserted safe bound D<7.84·10¹⁴ and n<1.34·10¹⁶ remains valid. A clean proof checks positivity at 7.84·10¹⁴ and monotonicity of D^{1/3}/log²(9D) for D>e⁶/9.

Lemma 2.4 proves a coefficient 136/9=15.111… (rounded upward to 15.12), **under D≤n/17**. Later quotations silently replace this by 15 and omit the regime. Those are not the bound established in the memo. Quote “15.12 D²/n for D≤n/17,” and retain the separate thick-case bound.

The suggestion of lowering the threshold using an “observed” index bound must be conditional on proving that bound, not on finite experiments.

### m4. Several brute-force descriptions overstate or misreport their coverage

**Locations:** summary lines 18–20; cross-check lines 135–150; lines 191, 197, 377–378; data/z53/lattice/cosets_q27.txt.

* At q=9, |H|max=27 only when 3|n; for 3∤n it is 9, giving minimal index 81, not 27. The table is valid as a maximum over n, but the summary needs this qualification.
* “D′≥D^{3/2} in every computed case” is false already at D=2,4,8,16, where the recorded indices are 2,4,8,32. Limit any empirical conjecture to the appropriate odd moduli.
* The saved q=27 file stops at n=20 and has no SUMMARY; it is not the claimed exhaustive run through all residues. The saved small file omits q=6, despite the summary range {2,…,9}. My q=6 rerun gives |H|max=12 and index 18.

There is an efficient rigorous repair for the q=27 coverage: for a unit a modulo q, (u,B,C)↦(au,aB,a⁻¹C) sends V_n to V_{an} and preserves subgroup sizes. Representatives of each valuation class suffice; n=0,1,3,9 are already recorded. The same observation extends the q=16 odd-n computations to all odd residues. State and use that symmetry rather than claiming unperformed exhaustive coverage.

### m5. Small presentation/proof qualifications

* **Line 64:** use t∈K+Λ, not −t, to obtain K∩(Λ+t)≠∅. The covering implication itself is correct.
* **Prop. 3.2, lines 238–242:** the apparent exception “unless all … X=−1” cannot occur for a full-rank coset: shifting X by the index immediately contradicts it. The result can simply say no such full-rank coset exists, within its stated all-points scope.
* **Lemma 4.1/Cor. 4.2, lines 265–274:** say “pairwise intersecting” or “triangle-free intersection graph,” not “pairwise concurrent.” For n=0 explicitly invoke the two distinct remaining lines rather than the five-cycle.
* **§7 numerator row, line 344:** the general-k extension needs its own bad-prime argument; the present proof is not literally only smoothness/irreducibility/Hessian, since the 2-adic argument uses the coefficient 4 and odd n. It may be extendable with k-dependent constants, but is not proved by merely saying constants change.

## Proof audit: steps that pass

### Proposition 2.3

* **CRT:** the quotients Z³/(Λ+ℓ^fZ³) are ℓ-primary quotients of Z³/Λ. The joint map is surjective: CRT can simultaneously realize arbitrary representatives modulo the different ℓ^f. Their orders multiply, giving the claimed index lower bound.
* **Facts 2.1–2.2:** smoothness holds (indeed the gradient argument does not require G(t)=0). The primitive degree-one-in-C argument proves irreducibility over every field of characteristic other than 2, including n=0. A plane would give a linear factor.
* **Odd-prime extraction:** after m1’s correction, L,Q,T vanish modulo ℓ^f for ℓ≥5. At 3, Q vanishes modulo 3^f and L,T modulo 3^{f−1}; the loss is correctly one power of 3.
* **Smith basis and coefficients:** H⊆W≅(Z/ℓ^f)² admits the stated elementary-divisor basis. Quadratic coefficients are extracted by (1,0),(0,1),(1,1). Cubic endpoints plus (1,1),(1,−1) extract both mixed coefficients using only division by 2, including at ℓ=3.
* **Nonvanishing on W:** if both restricted homogeneous forms vanished as polynomials modulo ℓ, t+W would be a plane in V_n. Irreducibility rules this out. This is polynomial nonvanishing, not an invalid inference from finite-field point counts.
* **Cases:** a unit quadratic coefficient gives a+b≥f/2; a unit cubic coefficient gives at least a+b≥f/3. The stronger τ₂₁ inequality a+b≥2f/3 is also correct. Thus |H|≤ℓ^{5f/3}.
* **At 3:** the reduction kernel has size 27, giving index ≥3^{(4f−4)/3}; f=1 is the trivial g=0 case.
* **At 2:** H̄ really is contained in W_g: L vanishes modulo 2^{f−1}, hence modulo 2^{f−3}. In the stated coordinates the cross coefficient reduces to u+B≡1, so it really is odd. The polar determinant is odd; perfect duality gives |H̄||H̄⊥|=2^{2g}, hence |H̄|≤2^g. The ambient reduction kernel has order 2⁹, giving |H|≤2^{f+6}. The f≤3 cases are trivial for the advertised weaker bound. The final constant 2⁶·3^{4/3} is correct.

### Lemmas 2.4–2.5 and Theorem 2.6

The midpoint inequalities, convexity of the reciprocal terms, identity

    R=(1+αβ)/((1−α²)(1−β²)),

and the printed algebra proving R−1≥(α²+β²)/2 all check out. So do the log-coordinate rectangle estimate, fibre integration, σ≤1/2 at D≤n/17, and coefficient 136/9. Lemma 2.5 correctly uses u+B≤2uB for u,B≥1 and the log-triangle integral (1/2)log²((n+D)/2).

Both cases of Theorem 2.6 then work with the numerical correction m3. The rank-three affine projection preserves congruence, convexity, positivity, the size bound, and covering. AΛ has finite index (as usual for a full-rank source lattice; alternatively its covering of R³ by a bounded projected shell forces rank three). The displayed threshold is safe.

### Theorem 3.1

For ℓ∤4C, the hyperbolic polar form is unimodular, giving |H|≤ℓ^f. When f>e=vℓ(N_C), the valuation identity i+j=e is valid. A projection image ℓ^a has at most ℓ^i points per fibre; the two cases j+a<f and j+a≥f both give 2a+j−i≥f. Thus |H|≤ℓ^{(f+e)/2}, including the zero-image case a=f.

For ℓ|4C, reduce the linear relation modulo ℓ^{f−ν}. For each h_u there are at most ℓ^ν choices of h_B; the unit relation implies h_u²≡0 modulo ℓ^{f−c−ν}. This gives the stated local index bound ℓ^{(3f−c−3ν)/2}; negative exponents impose only trivial constraints. Multiplication gives

    D′ ≥ D^{3/2}/(√gcd(D,N_C) · 2^{3/2}√(4C)).

The fixed-C midpoint estimate α²<2D/(n′+D), the integrated area estimate, and the thick-case coefficient 8 are correct. Constants 114 and 456 are valid after m2’s repair. The thick-case implication D≤n² for all sufficiently large n follows from growth of D/log²(2(n+D+1)); thereafter the coefficient 225 and O(log²n) cofactor bound are valid as eventual bounds.

### Proposition 3.2 and §4

Proposition 3.2’s vertical-shift proof is valid in its stated all-points scope. Lemma 4.1 correctly classifies polynomial maps satisfying G_n=0 as a polynomial identity: the nonzero-product degree comparison forces C and one other coordinate constant; the zero-product case yields L₁,L₂,L₃. All five listed intersection points and the five-cycle are correct for n≠0. For n=0 the two distinct lines are handled separately as noted above.

Corollary 4.2 follows by restricting to source lines and excluding a triangle in the target intersection graph. Theorem 4.3 correctly uses total degree ≤3δ<ℓ to turn vanishing on F_ℓ^d into a polynomial identity, then extends to the algebraic closure. All five resulting divisibility conditions, including Y=0 on L₄ and X=0 on L₅, are correct. This is a structural classification, not an exclusion of nonlinear schemes or a direct application of B4’s additional covering hypotheses.

### §5 density calculations

The triangle areas give exactly 1/4, 4/9, 9/16, and 4/9. The Lenstra-invisible triangle has legs 1/6, area 1/72, hence normalized share 1/36. These are valid model calculations.

The stronger pointwise claim that every positive triple is CHN-visible in some slice is also true, although the memo’s explanation suppresses constants. If both u and B are CHN-invisible and m=max(u,B), then n+m≥256m⁴. If C were Lenstra-invisible, 16C²≤n+1/(4C)<4CuB, so 4C<uB≤m², whence n+m=4CuB−min(u,B)<m⁴, a contradiction. Thus in this case C is even Lenstra-visible.

The conditional-root nature of Howgrave-Graham/Coppersmith is correctly described. What is excluded is existence deduced from those uniform bounds alone, not a combined argument with additional arithmetic input distinguishing nonsquares/primes.

## Bounded reproductions

All shell commands had timeout wrappers; Python/compiled jobs ran with a 6,000,000-KiB virtual-memory limit.

* `z53_lattice_checks.py` reproduced grid minimum 0 on the 1999² grid, c₀, and the safe thin/thick numerical thresholds. Its binomial calculation checks the wrong observed count, as explained in M5.
* Recompiled `z53_lattice_cosets.c`; exhaustively reran q=2,3,4,5,6,7,8,9,11. Global maxima |H| were respectively **4,3,16,5,12,7,64,27,11**. The saved per-n small-q rows agree. The DFS is valid: every subgroup of (Z/q)³ has at most three generators, every valid generator passes the cyclic test, and the closure check does not prune any valid subgroup. I did not rerun q=16,25,27; saved outputs and their coverage were inspected.
* Independently enumerated all subgroups of (Z/q)² and all relevant basepoints for q=3,5,8,9, C=1,…,q. Both fixed-C local bounds passed, including the refined f>e bound and bad-prime bound.
* Recompiled `z53_lattice_regimes.c`; reran first/middle/last rows of each of the four saved regime files. All twelve rows matched exactly. Reran all fourteen exceptional primes (all R=0), and 193,2521,66529,3361,5101441 (R=4,2,8,2,10, all any-CHN-visible).
* Reaggregated all saved regime files. Every displayed measured-table entry and the reported prime-sample correlations agrees after rounding: mean R=37.54 and 62.38 for the prime samples, 33.14 for near-squares; all 200 odd squares have R=0. The summary emits an innocuous NaN-correlation warning for the constant-zero square sample.

**Recommendation:** retain the quantitative lemmas and the narrowly stated full-rank volume/covering no-go. Repair the arithmetic and data statements, and substantially narrow the FRONTIER proposal. The present memo does not prove that factorization is necessary, that exactness cosets do not exist, or that all Thue/Minkowski/geometry-of-numbers existence mechanisms are exhausted.
