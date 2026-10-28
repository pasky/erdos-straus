# LOWERTAIL_ROUND2_ASTRA — growing alphabets and the precision of a pointwise lower tail

**Status: PARTIAL. ES remains open.** No implication from GRH, Elliott–Halberstam (EH), OAI-003, or a standard prime-distribution conjecture to eventual ES is proved here.

**PROVED, relative to an existing internally reviewed computer-assisted theorem:** the prime-alphabet cutoff in `LOWERTAIL_DEEP_ASTRA` §6.3 is unnecessary on certain non-square genus fibres. For every sufficiently large fixed prime r ≡ 3 (mod 4), **every finite alphabet containing r**, with arbitrary prime-power exponents, has a zero lower envelope on the fibre negative only at r. Its conditional mean is positive. Linnik transfers this to infinitely many actual primes with alphabet extending through c log p, while their least nonresidue stays the fixed r (§2).

**PROVED:** sparse insertion of odd prime squares preserves EH-type estimates, standard-scale AP variance asymptotics, Montgomery-type pointwise AP bounds, and fixed-complexity Hardy–Littlewood counting estimates, in the precisely stated sequence versions below. Yet the inserted members have zero actual two-line certificate count (§4). This is a **black-box stability barrier**, not logical independence from conjectures about the actual primes. Importantly, their BM/genus main terms are zero too: square insertion does **not** refute the relative inequality T ≥ εM, nor the conjunction of prime-distribution estimates and a positive arithmetic main term.

**PROVED:** the exact single-atom threshold for negative-part moments, including the second-order improvement to the z48 order log X / log log X (§5). This gives a slightly weaker nonstandard sufficient hypothesis for eventual ES, with sharpness within this moment-only mechanism. It is not claimed easier than ES.

**Assessment:** the long-modulus attempt produces no one-sided bilinear or Kloosterman estimate. The new envelope theorem excludes arbitrary-alphabet **genus-invariant** minorants on specified fibres, not non-real, coefficient-sensitive analytic estimates (§3). Promise as a route to ES: 1/5.

Labels: PROVED = proof supplied or explicit imported result; CONDITIONAL = named assumption; CERTIFIED = finite exact checks; EVIDENCE = numerical interpretation; Assessment = judgement. All mathematics is internal and unrefereed.

## 1. Counts and scope

**PROVED / inherited definitions.** Use the same counts as `LOWERTAIL_DEEP_ASTRA`:

    R(n) = #{(u,v,C) ≥ 1 : n = 4uvC − u − v},
    B(n) = #{(x,y,C) ≥ 1 : n = 4xyC − 4x − y, y ≥ 3 odd},
    T(n) = R(n) + B(n).

At primes n ≡ 1 (4), the relevant pairs are coprime; R is ordered, B is not doubled. Every hit gives a positive three-unit-fraction identity for 4/n. For B, y ≡ 3 (4) follows from n ≡ 1 (4). Odd squares have R = B = 0 (T1). The two-line union need not count distinct rational solutions; positivity is all we require.

For a multiple Q of 24 define C_Q on units modulo Q, restricted to n ≡ 1 (24), by summing:

* R classes: q = 4uv | Q, gcd(u,v) = 1, u+v odd, a = −u−v mod q;
* B classes: q = 4xy | Q, gcd(x,y) = 1, y ≥ 3, y ≡ 3 (4), a = −4x−y mod q.

All weights initially equal one. Pair subfamilies and arbitrary nonnegative weights are allowed when stated. Each onset is in (0,q); a congruence hit at a positive integer therefore gives a genuine positive-C solution. For n > Q all pairs are inside their height domains, so C_Q(n) ≤ T(n). For smaller n use the height-truncated subfamily, not this last inequality without checking the domain.

Let Ω_Q be a square coset in (Z/QZ)× with its mod-24 component fixed at 1. The optimal genus-invariant minorant of C_Q is

    L_Q(Ω_Q) = min_{a ∈ Ω_Q} C_Q(a),

not its conditional mean μ_Q(Ω_Q). This is the already proved envelope theorem (`LOWERTAIL_DEEP_ASTRA`, Thm 6.1), not a new lemma. Its mean is exactly the sum of the individual genus projections, because reduction of the global square subgroup onto the square subgroup modulo q | Q is surjective.

**CONDITIONAL on a fixed Dirichlet zero-free strip:** the inherited Thm 5.4 gives M_gen^T(p) ≥ (2/π⁴−o(1)) log²p. OAI-003 means **CONDITIONAL on OAI-003 (quasi-RH 7/8)** throughout. The actual remainder is still T = M_gen^T + X_nr^T. Nothing below silently substitutes the BM term for the full genus term.

## 2. Round one: the growing-alphabet envelope

### 2.1 The older theorem that removes the alphabet restriction

**PROVED / imported, computer-assisted:** `STERILE_LOWER.md`, Thm 6.3, states that for every prime

    r ≥ r₀ := 2^(21.4375)

there is a unit ξ ∈ Z_r with (ξ/r) = −1 such that the profinite unit z has

    z_r = ξ,       z_ℓ = 1 for every prime ℓ ≠ r,

and belongs to **none** of the seven ET Proposition 1.9 certificate classes. This is the r-generic sterile-point theorem. The bound is internally computer-assisted, not a newly certified computation here. Its exact scope and reviewed inputs are recorded in `STERILE_LOWER` §§2,6 and `STERILE_EXPLICIT` §§3.1–3.4; `POINTWISE_MORDELL17` defines the r-generic point. A weaker cutoff 2³² from `STERILE_EXPLICIT` would work identically.

The needed transfer is not “all polynomial identities are ET classes.” We only need two explicit inclusions:

* The R pair (u,v) is ET II1 with (a,b,e) = (u,v,u+v), modulus 4uv and residue −u−v.
* The B pair (x,y) is ET II3 with (a,d,e) = (1,x,y), modulus 4xy and residue −4x−y.

Both parameter conditions are exactly the coprimality conditions in §1. These maps are checked against `scripts/mordell_lib.py`, independently of the new proof. In particular II3 does **not** require e | 4a²d+1; confusing it with II2 would invalidate this transfer.

### Theorem 2.1 — an all-alphabet, non-square zero envelope

**PROVED relative to the imported sterile-point theorem.** Fix any prime r ≥ r₀. For every finite Q divisible by 24r let Ω_Q(r) be the genus fibre specified by

    a ≡ 1 (8),  a ≡ 1 (3),
    (a/r) = −1,  (a/ℓ) = +1 for every odd prime ℓ | Q, ℓ ≠ r.

Then

    L_Q(Ω_Q(r)) = 0.

There is no bound on the largest prime factor of Q, its number of prime factors, or its prime-power exponents. The same conclusion holds for every nonnegative weighting and every subfamily of the R/B classes modulo divisors of Q, including a height-truncated or dyadic-modulus subfamily.

If additionally r ≡ 3 (4), then the unweighted full menu has

    μ_Q(Ω_Q(r)) ≥ 4/(r−1) > 0.

*Proof.* Project the sterile point z to a unit z_Q modulo Q. Every summand of C_Q vanishes there by the two ET inclusions. Its genus signs are those defining Ω_Q(r): at an odd prime power, a unit is a square iff its residue modulo the prime is a square; at 2^e with e ≥ 3, it is a square iff it is 1 modulo 8. Thus z_Q lies in Ω_Q(r), proving the zero minimum. The same point annihilates every weighting/subfamily.

For the positive mean retain the two ordered R pairs (1,2r),(2r,1). Their modulus is 8r | Q, their target is a = −1−2r. Since r ≡ 3 (4), a ≡ 1 (8) and (a/r) = (−1/r) = −1. They are genus-allowed throughout Ω_Q(r), and each contributes 1/|((Z/8rZ)×)²| = 2/(r−1). Their contributions add. ∎

**Assessment / strengthening and limitation.** This strictly extends the z48 bounded-alphabet barrier on an explicit class of non-square fibres: it allows *all finite alphabets*, not just primes ≤ 19. It does not establish zero envelopes on **every** Mordell-hard fibre, or at a fixed small least nonresidue such as 11 or 17. It is a new corollary connecting existing campaign results, not a new construction of sterile points.

### 2.2 Anchors and the order of quantifiers

**PROVED explicit projection bound.** Write Q = r^e N, gcd(r,N) = 1. If ξ_e is the residue of ξ modulo r^e, the anchor is the least positive representative of

    z_Q = 1 + N · [(ξ_e−1) N^(−1) mod r^e].                 (2.1)

Thus 1 ≤ z_Q ≤ Q. These anchors are compatible under reduction as Q varies and annihilate every q | Q menu. The sterile-point theorem is existential; (2.1) is not an algorithm for finding its unbounded r-adic digit sequence.

**Assessment / extremality.** Zero is the sharp possible envelope because the count is nonnegative. We have not optimized the *height* of an integer anchor. Unlike the z48 finite integer anchors, z_Q need not be one fixed integer that works for every exponent of a fixed alphabet. Compatibility is supplied by a single profinite point instead. This distinction is why an unrestricted alphabet theorem is possible without constructing an integer with T(n)=0 globally.

### Corollary 2.2 — growing alphabets at actual primes

**PROVED relative to the same theorem, PNT, and Linnik.** Fix r ≥ r₀, r ≡ 3 (4). If L₀ is any admissible exponent in Linnik's least-prime theorem, then for every fixed 0 < c < 1/L₀ there are infinitely many primes p ≡ 1 (24), with least quadratic nonresidue exactly r, such that:

> For every finite Q divisible by 24r and supported on primes ≤ c log p, with arbitrary exponents, the genus envelope of the R/B q | Q menu at the genus profile of p is zero.

*Proof.* For Y ≥ r let Q_Y = 8∏_{ℓ≤Y}ℓ. Choose p in the reduced class z mod Q_Y, with p ≤ A Q_Y^L₀ by Linnik. Then p > Y, since every prime ≤ Y divides Q_Y while the chosen class is a unit. Therefore these primes tend to infinity as Y does. The PNT gives log Q_Y = (1+o(1))Y, so c log p ≤ Y eventually. The signs of p at primes ≤ Y are positive except at r, hence r(p)=r by quadratic reciprocity and multiplicativity. Apply Theorem 2.1 to any Q in the assertion; its exponents need not divide Q_Y since equality of genus profiles only uses the prime signs and mod 8. ∎

**Assessment.** This is not an ES counterexample: only the smooth-modulus menu's genus-invariant minorant is zero, not its count at p. Even the actual truncated count can be positive at p. The theorem also does not assert that every p has this sign profile up to c log p. It shows that allowing an alphabet growing logarithmically, *even with a fixed known nonresidue*, cannot universally repair the genus-minorant method.

There is a stronger algebraic statement but a weaker realization statement: Theorem 2.1 allows Y arbitrarily large on abstract fibres; Corollary 2.2 realizes growing Y at actual primes only on the stated scale. No existence of primes with this profile up to p^θ is asserted.

## 3. Round two: long moduli and the non-real remainder

**Assessment / calibration respected.** No polylogarithmic two-endpoint witness bound is proposed. The z49 calibration disfavors such bounds, and the task's near-linear modulus regime q up to p^(1−o(1)) is the regime examined here. A least-QNR bound is not a witness bound.

### Proposition 3.1 — long-modulus completion has no automatic sign

**PROVED, algebraic scope.** Let C be any nonnegative weighted sum of certificate classes modulo divisors of Q and let μ be its conditional mean on Ω_Q(r). If μ > 0, its non-genus part X = C−μ has both signs on that fibre, and at the sterile projection

    X(z_Q) = −μ.                                           (3.1)

The statement applies when all retained moduli lie in a prescribed long dyadic interval. Such nonempty positive-mean intervals exist at unbounded scales: for r ≡ 3 (4) use the ordered pairs (1,2r^k),(2r^k,1) with odd k, at modulus 8r^k.

*Proof.* Theorem 2.1 gives C(z_Q)=0. The conditional average of X is zero, and C is positive somewhere if μ>0, so X must also be positive somewhere. For the indicated pairs the target −1−2r^k is 1 modulo 8 and a nonresidue modulo r. The square-image size modulo 8r^k is φ(r^k)/2, so their total conditional mean is 4/φ(r^k)>0. ∎

**Scope.** This rules out an identity-level claim that multiplicative pairing, completion, or nonnegative regrouping gives X ≥ 0 on each genus fibre, even at long moduli. It does **not** rule out X(p) ≥ −(1−ε)M_gen(p) specifically at primes in their height domains. Nor does it prove that every BFI/dispersion device must be two-sided. That universal barrier is not established.

**PROVED bookkeeping / attempted bilinear route.** For an R pair write q=4uv, gcd(u,v)=1, a=−u−v. Its indicator has the exact expansion

    1[p ≡ a (q)] = q^(−1) Σ_{h mod q} exp(2πi h(p+u+v)/q).

In a block q ≍ p^θ, C ≍ p^(1−θ) away from endpoint-boundary effects. Reindexing by u,C instead gives the exact divisibility condition

    4uC−1 | p+u.

Thus completion either keeps a modulus varying with u,v or keeps a class target depending on the multiplicative height. It does not create a free interval of integer arguments around the prescribed p. The multiplicative character expansion has the analogous exact separation into genus and non-real frequencies.

**Assessment / three attempts and their stopping points.**

1. **Linnik dispersion / BFI:** prime-in-AP statements sum over the prime argument before estimating the congruence discrepancy, even when coefficients over moduli are bilinear or well-factorable. Applying them after summing p produces an averaged estimate. Section 4 makes precise why estimates at their standard errors cannot alone remove an isolated member. No fixed-p version with error o(log²p) is obtained.
2. **Kloosterman completion and Weil:** completion is exact and Weil controls absolute values. Both are compatible with (3.1). An absolute bound *smaller than μ* would of course suffice; nothing here proves it impossible at the exact ES coefficient vector. The missing result is cancellation of the full height-dependent combination, not the usual bound for one complete sum. A proof claiming that square-root bounds alone suffice must actually sum their coefficients and show an error below log²p; no such estimate is supplied.
3. **A positive bilinear expression:** nonnegative sums of certificate indicators and their genus averages still have the zero (3.1). Positive-square compression retains the pedestal problem proved in z48. A new inequality would need a prime/height-specific strict excess above the pedestal, not nonnegativity of the completed expression.

**Exact result of this round:** an arbitrary-alphabet, unbounded-modulus sign counterexample on abstract fibres; no analytic one-sided estimate at the given p. Coefficient-sensitive non-real estimates remain open.

## 4. Round three: which standard-type statistical inputs survive bad members?

### 4.1 A general perturbation lemma

For a set A of positive integers put

    θ_A(x;q,a) = Σ_{n≤x, n∈A, n≡a (q)} log n,
    E_A(x;q,a) = θ_A(x;q,a) − x/φ(q),  gcd(a,q)=1.

Using Li(x) and unweighted counts gives parallel statements. This is a definition for arbitrary sets, not an assertion that A has an Euler product.

### Theorem 4.1 — sparse-set stability

**PROVED.** Suppose A and A′ differ at at most K(x) integers ≤ x, and put D(x)=K(x)log x. Write δ(q,a)=θ_A′(x;q,a)−θ_A(x;q,a). Then, uniformly in x,Q,

    Σ_{q≤Q} max_{(a,q)=1} sup_{y≤x}|δ_y(q,a)| ≤ Q D(x),     (4.1)
    Σ_{q≤Q} Σ_{(a,q)=1}|δ(q,a)|² ≤ Q D(x)².                (4.2)

Consequently, if V_A=Σ_{q≤Q}Σ_a* |E_A|², then

    |√V_A′ − √V_A| ≤ √Q D(x).                              (4.3)

Also |δ(q,a)|≤D(x) separately for each q,a.

*Proof.* For each modulus, the sum over all residue classes of the absolute perturbations is at most D(x), including for every y≤x. Hence its maximum is at most D(x), and its sum of squares is at most D(x)². Sum over q. Equation (4.3) is the reverse triangle inequality in the finite Euclidean space of (q,a). ∎

### Corollary 4.2 — standard-scale hypotheses cannot detect sparse insertions

**PROVED implications for sequence versions of the displayed hypotheses.** If K(x) is bounded by a fixed power of log x:

* **EH(ϑ), every fixed ϑ<1:** bounds (4.1) with RHS O_A(x/log^A x) remain valid, for every fixed A, if they held for A before the modification. The extra error x^ϑ D(x) is smaller than x/log^A x for every A. The same argument covers bounded or polylog-bounded weights on moduli, including restricted well-factorable tests.
* **Hooley/Montgomery-type AP variance:** an asymptotic V_A(x,Q) ∼ V₀(x,Q) transfers uniformly wherever QD(x)²=o(V₀). In particular it transfers when V₀ ≍ xQ log x. This explicitly stated variance scale is what is used; no claim is made for arbitrarily microscopic error terms or every variant bearing those names.
* **Montgomery-type pointwise AP bound:** bounds |E_A| ≪_ε (x/q)^(1/2) x^ε, q≤x, remain valid for every fixed ε>0. The perturbation is polylogarithmic while the RHS is at least x^ε.

The corresponding main term, total counting asymptotic, and fixed-progression PNT also survive. A sharp variance remainder transfers only when its specified error tolerates the perturbation bound; an asymptotic and an arbitrary error term are not interchangeable.

### 4.2 Actual arithmetic bad members, rather than invented zero counts

**PROVED construction.** Choose odd primes s_j so fast that s_(j+1)>s_j², and set

    S = {s_j² : j≥1},       A′ = P ∪ S.

Then K(x)=O(log log x). Every new member is 1 modulo 8, has T(s_j²)=0 by T1, and has no small prime factor below its square root. By Corollary 4.2, **if** the primes satisfy any combination of its displayed distribution hypotheses, A′ satisfies their sequence versions too, with the same main terms and variance asymptotics. But “T(n)>0 for every sufficiently large n∈A′” is false. In particular H⁻mom at its sufficient growing order fails on A′: one square contributes the full deficit moment.

**Important limitation (PROVED bookkeeping).** M_BM(s_j²)=M_gen(s_j²)=0. Therefore the inserted squares do not violate T ≥ εM. They also violate the independently supplied prime-only theorem M_gen ≫ log²n. This construction proves that the AP estimates *alone*, treated as properties of a sequence, cannot yield positive actual counts at every sequence member or H⁻mom centered at c log²X. It does not disprove an implication using those estimates **plus primality or the positive main-term theorem**. Nor does it prove that EH cannot logically imply ES for genuine primes.

No example satisfying both an arithmetic M_gen ≫ log²n and infinitely many actual two-line zeros is constructed. Producing one would be a substantially harder arithmetic result, not a legitimate free modification of the prime labels.

### 4.3 Hardy–Littlewood: explicit uniformity and its limit

### Proposition 4.3 — tuple-statistic stability

**PROVED.** Let L_i(t)=a_i t+b_i, 1≤i≤k, be distinct nonconstant integer affine forms, and restrict to integer t in any interval I on which 1≤L_i(t)≤Z. The unweighted counts with all L_i(t) in A or in A′ differ by at most

    k K(Z).                                                 (4.4)

For counts weighted by ∏_i log L_i(t), the difference is at most

    k K(Z) (log Z)^k.                                        (4.5)

*Proof.* A changed tuple has some L_i(t) in A Δ A′. For each i and each changed value there is at most one t because a_i≠0. A union bound gives (4.4), and the maximum weight gives (4.5). ∎

**CONDITIONAL transfer / precise comparison.** Any uniform Hardy–Littlewood hypothesis whose error allowance dominates (4.4), or (4.5) in the weighted convention, survives the insertion. This includes fixed k and bounded coefficients with any fixed power-saving error X^(1−δ), 0<δ<1, when Z≪X^B and K is polylogarithmic. Main terms/singular series refer to the same forms; no new singular series is invented for A′.

For k growing, the actual boundary matters: if log Z≍log X and K is polylogarithmic, (4.5) is X^(a+o(1)) when k=(a+o(1))log X/log log X. A weighted error X^(1−δ) still tolerates all fixed a<1−δ. This is a transfer statement, not a derivation of H⁻mom from high-order HL. An HL assertion for bounded-complexity prime tuples counts a different correlation from a growing family of divisor congruences at the *same* integer.

**Assessment / open stronger possibility.** Uniform correlation estimates at growing complexity with errors small enough to exclude one arithmetic atom could in principle supply the missing tail. “Uniform Hardy–Littlewood” without its complexity range and absolute error does not specify such a hypothesis. No implication from a standard precise version is established here.

### 4.4 GRH, pair correlation, Cramér and Granville

**Assessment / analytic scope.** The sparse-insertion construction is not a new system of Dirichlet L-functions. It does not retain their functional equations, character periodicity, or analytic zero correlations. Therefore it is **not** a countermodel to GRH, GRH plus pair correlation, or OAI-003. GRH plus a zero pair-correlation conjecture can imply particular AP second moments, but replacing the full analytic hypothesis by those consequences loses information. Only the latter are covered by Theorem 4.1. No logical non-implication from the full analytic hypotheses is claimed.

The exact missing analytic input remains a signed correlation of zeros/characters with the ES coefficients at p. Neither an ordinary unweighted pair-correlation statement nor its AP-variance consequence explicitly supplies it; no derivation is known in this work.

**PROVED in the elementary Cramér model.** If each integer n≥3 is selected independently with probability 1/log n, infinitely many odd squares are selected almost surely, since Σ_{m odd}1/log(m²)=∞ and the events are independent. Every selected square has T=0. Thus the literal “every sufficiently large model prime has T>0” statement is false in this model.

**PROVED in a specified presieved variant, not all Granville models.** Deterministically exclude integers with a prime factor ≤ z(n), where z(n)<√n eventually, then select the surviving integers independently with probabilities at least c/log n. Every sufficiently large odd prime square s² survives, and Σ_{s prime}1/log(s²)=∞ (e.g. by PNT). Hence infinitely many are selected almost surely. For a randomized sieve or another Granville model, the independence and survival claims would have to be checked anew.

**Assessment.** These models can still be useful heuristics for the genuine primes after additional arithmetic conditioning. They are not pointwise transfer theorems. The square-exact main term is essential, not a dispensable correction.

## 5. Round four: the sharp negative-moment precision

The earlier H⁻mom uses k=⌈log X/log log X⌉. We retain its one-sided nature, but identify the exact one-atom obstruction, rather than stopping at its leading order.

### Theorem 5.1 — exact moment-only threshold

**PROVED.** Let I be a finite index set of size N, F:I→Z_≥0, m>0, C>0, and k a positive integer. Suppose

    Σ_{i∈I} (m−F(i))_+^(2k) ≤ N(Ckm)^k.                     (5.1)

For a target 0≤η<1 put d=m−⌊ηm⌋ and

    A = d²/(Cm),       E = N(k/A)^k.

Then the number of indices with F(i)≤ηm is at most E. In particular E<1 excludes every such index. Conversely, if E≥1, there exists a nonnegative integer-valued F satisfying (5.1) and having one such index.

*Proof.* Every bad index has deficit at least d. Divide (5.1) by d^(2k). For the converse set F=⌊ηm⌋ at one index and F=⌈m⌉ elsewhere. Its moment is d^(2k), which is allowed exactly when E≥1. ∎

**Scope.** This is an information-theoretic sharpness statement for the one displayed moment. The constructed F is not asserted to be an ES count. For η=0 it is exactly the threshold for excluding a zero, without a rounding error.

### Corollary 5.2 — the second-order critical order

**PROVED asymptotic calculation.** Write t=log N and suppose A/t→∞. The smaller positive real root of

    k log(A/k) = t

is

    k_* = −t / W_−1(−t/A),                                  (5.2)

where W_−1 is the negative real Lambert-W branch. Equivalently, if h=log(A/t),

    t/k_* = h + log h + O(log h/h).                           (5.3)

On the increasing branch 0<k<A/e, any integer k>k_* gives E<1; k≤k_* permits a bad atom. More generally E<1 exactly when k lies strictly between the two positive roots.

*Proof.* Set y=t/k. Then y−log y=log(A/t), with the large solution y>1, giving (5.2). Substitution of y=h+log h+O(log h/h) gives (5.3). The derivative of k log(A/k) is log(A/k)−1, proving monotonicity and the two-root description. ∎

For N≍X/log X, m=c(log X)² and fixed η,C, let L=log X. Then

    k_* = L / [log L + log log L + log((1−η)²c/C) + o(1)].     (5.4)

The replacement of t by L and integer rounding of ηm change the denominator by o(1). Thus the z48 k=L/log L is safely above the critical value; it can be lowered by a second-order amount of order L log log L/(log L)².

### Hypothesis H⁻crit(c,C,η,δ)

**CONJECTURE / nonstandard.** Fix c,C,δ>0 and 0<η<1. For every sufficiently large dyadic block (X,2X], let I_X be its primes ≡1 (4), N_X=|I_X|, m_X=c(log X)², and

    k_X = ceil{ L / [log L + log log L
                     + log((1−η)²c/C) − δ] }.

Assume (5.1) for F(p)=T(p), I=I_X, m=m_X and k=k_X.

### Theorem 5.3 — sufficient hypothesis with a sharp mechanism boundary

**CONDITIONAL on H⁻crit; PROVED implication.** All sufficiently large primes p≡1 (4) satisfy T(p)>ηc(log p)²(1−o(1)), hence T(p)≥εM_BM(p) for some ε>0 and ES(p).

*Proof.* By PNT in the fixed class, N_X≍X/log X. Equation (5.4) and δ>0 put k_X strictly above k_* and below A/e for large X. Therefore Theorem 5.1 excludes every bad prime in every sufficiently large dyadic block. The inherited unconditional upper bound M_BM(p)≪log²p converts this to the relative lower bound. No zero-free-strip assumption is needed for this implication. ∎

**PROVED sharpness within the same information.** Replacing −δ by +δ in the denominator puts k below k_* and permits a bad atom in every sufficiently large block in the abstract moment problem. For η=0 those atoms are zeros. Taking only a sparse subsequence of blocks and taking F(p)=⌈c(log p)²⌉ elsewhere realizes infinitely many permitted zeros; no arithmetic ES interpretation of this F is claimed. This strengthens the z48 leading-constant sharpness a<1 to the second-order boundary. At the exact root, constants and integer rounding matter, so the strict δ margin is intentional.

**Assessment / weakest-hypothesis verdict.** H⁻crit is the weakest precision located here **within this sub-Gaussian negative-moment architecture**, not an absolutely weakest hypothesis implying ES. It is quantitative and not literally ES by definition, but it is much stronger than existence and no easier proof is supplied. Absolute moments remain unusable because of the inherited Linnik positive spikes. Theorems 4.1–4.3 explain why conventional averaged error allowances do not furnish these critical one-atom moments as sequence-only black boxes; they do not rule out using additional arithmetic structure of genuine primes.

## 6. Controls, verification, and exact remaining gap

**CERTIFIED checks:** `scripts/z49_ltastra2_check.py` checks 1,080 R/B-to-ET identities against the existing independent ET class engine; enumerates 12 small finite fibres to check the mean/envelope split and makes 96 prime-power genus-permission checks; checks 243 finite moment problems with exhaustive integer vectors; and checks perturbation inequalities against explicitly modified sequences. The finite-fibre means are independently recomputed from square-image projectors. For example Q=23,064, r=31 has mean 2/5 and minimum zero; Q=1,176, r=7 has mean 2 and minimum 1, correctly preventing an all-r overclaim. These small r are illustrations, not instances of the imported large-r theorem. Arrays are bounded and no large CRT residue space is allocated.

**CERTIFIED controls:** the established count engines are reused for the hard primes 193,409,577,2521,3361,5569,9601,66529,8813281, all 14 R-zeros, seven odd squares, and numerator 8 at 17,241. All 14 R-zeros recur; B vanishes at 193,2521,66529 but R is positive there; T is positive at every tested prime. Both counts vanish at all seven squares and on the numerator-8 controls. `control_counts.txt` records columns n, B, R/2, and an auxiliary large-window B count (the latter is unused). These are controls on actual counts and identities, not numerical evidence for an infinite moment hypothesis. The full sterile-point theorem is imported rather than claimed re-certified by a few finite tests.

**T1:** neither a positive genus term nor eventual positivity is asserted at squares. Their zero counts supply the stability counterexample; the zero main term explicitly limits that counterexample.

**Numerator 8:** the harmonic-analysis and perturbation lemmas are numerator-blind barriers, not positive mechanisms. H⁻crit is an unproved numerator-4 count hypothesis, eventually quantified, and does not assert 8/17 or 8/241. The R/B identity maps used in §2 are explicitly numerator 4.

**Exact remaining gap:** prove a one-sided estimate for the *non-real, target-dependent* remainder at a fixed genuine prime, or prove negative-part moments beyond the critical single-atom threshold. The inherited positive main term is not transferred to an actual count. Growing alphabets alone cannot rescue genus-invariant minorants on the fibres in Theorem 2.1; non-real, height-sensitive kernels remain outside that theorem. Standard AP statistics, bounded-complexity tuple asymptotics, and naive random-prime models do not supply the missing inference in their sequence-only forms. No claim of logical independence from GRH/EH or of a universal bilinear-method impossibility is made.

**Reproduction:**

```sh
ulimit -v 8000000
timeout 180 uv run python scripts/z49_ltastra2_check.py
cc -O3 -Wall -Wextra -o /tmp/z49_ltastra2_count scripts/z29_census.c -lm
timeout 180 /tmp/z49_ltastra2_count countlist 9000000 \
  < data/z49_ltastra2/control_inputs.txt > data/z49_ltastra2/control_counts.txt
```

**Hostile review (completed):** a fresh deep-mode subagent read the complete note, checked the ET inclusions, sterile-point dependency and Linnik quantifiers, perturbation scopes, and the moment/Lambert-W calculation. Verdict: SOUND relative to the explicitly imported sterile-point theorem; no fatal or major defect. It independently reran all check functions under the memory/time limits and reproduced `checks.json`. The review emphasized retaining two scope distinctions already explicit here: square insertion is not a counterexample to T≥εM, and a subthreshold atom for η>0 need not be a zero (the zero sharpness statement uses η=0). Neither distinction was weakened. No merge or upstream-file change is made.
