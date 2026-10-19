# PRIMITIVE_INTERSECTION — exact orders, prescribed factors, and trace selection

## 0. Summary

**Assessment.** The primitive-divisor analogy survives as an exact dictionary, not an existence argument. This follow-up makes its loss explicit: unrestricted trace choice is exactly the **prime-divisor subfamily** of (★), and fails at **94 primes below 10⁶**, even with unlimited traces and the complete level range; 2521 and 66529 are among the composite-only losses. Two useful refinements are proved: an exact CRT product formula for trace occupancy at fixed p, and a cyclotomic elimination polynomial whose prime factors contain every possible intersection for a fixed trace and level. Rational-function identities coupling the *exact* index t to tp+1 are impossible for 4|t>4; the exceptional index 4 admits identities but does not force inertness. A complete scan of the 2370 Mordell-hard primes below 10⁶, t≤256 and odd P≤63, finds 2075 trace-list successes versus 2280 primes possessing an eligible prime factor. The observed trace incidences are slightly below the conditional random-trace expectation, not enhanced. Pell traces supply no forcing and have a precise extra 2-adic selection rule. ES remains open.

**Verdict: PARTIAL — missing implication: eventual nonemptiness of the prescribed-factor/exact-order intersection at one prime. Promise: 1/5.** **R-z46 repair (scope):** the regular rational-trace exact-index identity construction COLLAPSES; the general growing-level intersection question does not.

## 1. Setup, predecessors, and scope

**PROVED / existing dictionary.** Write t=4C, N=tp+1. A divisor d|N with d≡−1 (mod t) gives

    u=(d+1)/t, B=(N/d+1)/t,
    p=tuB−u−B,
    4/p=1/(uBC)+1/(pBC)+1/(puC).                         (1)

Conversely (1) gives (tu−1)(tB−1)=tp+1. This is precisely FRONTIER §2's c=1 line (★), not all Type II and not all ES. Its ordered count is R(p). Necessarily t≤p+2, because tuB−u−B≥t−2 for u,B≥1. Moreover any certificate divisor, prime or not, satisfies

    t−1 ≤ d ≤ (tp+1)/(t−1) ≤ (4p+1)/3.                  (2)

The last inequality holds for t≥4. Thus the relevant prime divisors are O(p), although the side integers can be O(p²).

**PROVED / setup.** Throughout the discriminant-p integral family, p≡1 (4) is prime, P is odd, p∤P, and

    Q=(P²−p)/4, α=(P+√p)/2, β=(P−√p)/2,
    U_r=(α^r−β^r)/(α−β), V_r=α^r+β^r.

These are legitimate Lucas pairs: Q≠0, gcd(P,Q)=1, and the real ratio α/β is neither 1 nor −1, hence not a root of unity. For an odd prime ℓ∤Qp, its rank r_ℓ is ord(α/β) in the relevant finite field. Frobenius gives

    r_ℓ | ℓ−(p/ℓ).

For such ℓ, rank exactly t is equivalent to being a primitive prime divisor of U_t (the discriminant and all earlier terms are excluded). The target condition is

    ℓ | tp+1, r_ℓ=t, (p/ℓ)=−1.                         (PI)

**Assessment / novelty audit.** The order analogy and the missing coupling already occur in `TORSION_FIRING.md` Proposition 3.5 and `BRAINSTORM/y3_lucas_dickson_trace.md`; the exact φ(t) trace count is in `BRAINSTORM/z45_recent_pointwise_tools.md` §3.2, checked in `reviews/z45-breadth-review.md` §9. `BREADTH_Z45.md` recommends this follow-up. Prior unit experiments are in `BRAINSTORM/canonical_invariants.md`, and the three prime-modulus dictionaries are in `FIXED_MODULUS_SHOTS.md` Lemma 1.1. FRONTIER §§2–4,6–7 and the brainstorm index were read; repository searches for Lucas/resultants, trace multiplicities, cotangents, and unit/rank combinations found the preceding order and identity barriers, but not the particular elimination tables or joint trace formula below. No priority claim is made for the elementary finite-field, CRT, or resultant mathematics.

## 2. Precise questions and the complete dictionary

### 2.1 Exactly which certificates are represented?

**PROVED, Theorem 1 (single-prime correspondence; the local count is the z45 lemma).** For fixed p, t=4C and prime ℓ|tp+1, the following are equivalent:

1. ℓ≡−1 (mod t).
2. Some admissible integral trace P makes (PI) hold.

When they hold, exactly φ(t) residues P mod ℓ work. Among admissible positive traces P≤H their number is

    (1−1/p) H φ(t)/(2ℓ) + O(φ(t)),                      (3)

with an absolute implied constant. In particular the density among odd traces prime to p is φ(t)/ℓ. Modulo 2pℓ there are exactly (p−1)φ(t) admissible successful classes.

*Proof.* The forward implication from (PI) to the class follows from t|ℓ+1. Conversely, ℓ≡−1 (mod 4C) implies (C/ℓ)=1. For every odd prime q|C, reciprocity gives (q/ℓ)=(−1/q)(−1)^((q−1)/2)=1; if 2|C, then ℓ≡7 (8) and (2/ℓ)=1. Since p≡−(4C)⁻¹ (mod ℓ), (p/ℓ)=−1.

Choose s²=p in F_{ℓ²}. The Cayley map

    P ↦ z=(P+s)/(P−s),   P=s(z+1)/(z−1)

bijects F_ℓ with the norm-one torus minus 1. Its inverse is fixed by Frobenius, and the torus is cyclic of order ℓ+1. Exactly φ(t) elements have order t; none has P=0, which gives order 2. Neither root vanishes because p is inert. CRT supplies odd lifts avoiding p. Counting an arithmetic progression modulo 2ℓ and subtracting its multiples of p proves (3), separately for each good residue. ∎

**PROVED / scope.** Thus (PI) is equivalent to **prime-divisor (★)** after existentially quantifying P, not to general (★). A composite certificate d does not become a primitive *prime* divisor. Rank modulo a composite modulus involves CRT/lcm data, and requiring each prime factor to have inert rank t is a strictly different condition. For example at p=3361, t=20, the (★) factors are 99 and 679; neither is prime, and none of their prime factors is −1 mod 20. No trace recovers this certificate through (PI).

**PROVED / full Type-II prime-modulus dictionary.** Use the cube coordinates (c,d,j) of `FIXED_MODULUS_SHOTS.md`, not the identically named ET coordinates. Every Type-II solution is represented by

    h=4cdj−1, h | pj+c,
    h | pj+c ⇔ h | p+4c²d ⇔ h | 4dj²p+1.               (4)

For prime h=ℓ, each row below is an exact prime-modulus certificate dictionary after adding inert rank t for the discriminant-p Lucas family:

| fixed coordinates | prescribed integer | exact rank t |
|---|---|---:|
| c,d | p+4c²d | 4cd |
| c,j | jp+c | 4cj |
| d,j | 4dj²p+1 | 4dj |

In each row ℓ≡−1 (mod t) makes every prime factor of the fixed coordinate product a square modulo ℓ, by the reciprocity argument above. Substitution from the divisibility gives (p/ℓ)=−1. The same Cayley proof then gives exactly φ(t) successful traces mod ℓ. Conversely, inert rank t and the stated divisibility give (4), hence a positive Type-II solution by the cube lemma. The original (PI) is the third row with j=1, d=C. **It is not the entire PM-II detector.** In particular the known PM-II exception 3361 is unavoidable, but failures of our narrower detector at 2521 and 66529 say nothing against PM-II there.

### 2.2 Quantifier reversal and exact independence

**PROVED, Theorem 2 (joint trace law).** Put

    E_p(T)={(t,ℓ): 4|t≤min(T,p+2), ℓ prime,
                      ℓ|tp+1, ℓ≡−1 (mod t)},
    ρ_(t,ℓ)=φ(t)/ℓ, M=∏_(t,ℓ)∈E_p(T) ℓ.

The primes ℓ appearing in E_p(T) are all distinct. For a uniform admissible trace modulo 2pM, the rank-t events at the pairs of E_p(T) are **independent**, with probabilities ρ_(t,ℓ). Consequently

    Prob_P(at least one PI hit) = 1−∏_(t,ℓ)∈E_p(T)(1−ρ_(t,ℓ)),       (5)
    E_P(number of hits) = Σ_(t,ℓ)∈E_p(T) ρ_(t,ℓ).                    (6)

There is also a single admissible P simultaneously realizing every pair, with density ∏ρ_(t,ℓ) among admissible traces.

*Proof.* If ℓ appears at t and t′, then ℓ|t−t′; also 4|t−t′, whereas both t,t′≤ℓ+1 because they divide ℓ+1. Thus 4ℓ|t−t′ and |t−t′|<4ℓ, forcing equality. The CRT coordinates modulo these distinct primes are independent, even after independently imposing oddness and p∤P. Apply Theorem 1 coordinatewise. ∎

**Assessment.** This is stronger than assuming independent ranks, but does not force E_p(T)≠∅. If that set is empty, every product in (5) is 1, and the probability is zero. A simultaneous CRT trace can be taken below 2pM, which is not a short-trace bound. The independence concerns a complete residue ensemble in P, not consecutive small P and not averages over p. It does not conflict with the correlated lower tail of R(p).

**CONJECTURE (eventual prime intersection, PI∞; a target, not an endorsed eventual prediction).** There exists p₀ such that every prime p≡1 (24), p>p₀, has (PI) at some 4|t≤p+2 and some admissible P. By Theorem 1 this is exactly eventual prime-divisor (★), stronger than eventual (★), not a consequence of BHV. Its threshold must exceed all known (★) failures, including 8813281.

**CONJECTURE-shaped stronger target (PI-short; not established or strongly supported).** For some A,p₀, the same assertion holds with P≤(log p)^A. A theorem selecting P from CF/unit data independently of an already discovered certificate would be another strengthening of PI∞. The threshold-free versions are false by §3.4.

## 3. Attempts, proofs, and computations

### 3.1 Cyclotomic elimination: the prescribed gcd is a finite congruence menu

**PROVED, Theorem 3 (elimination polynomial).** For 4|t define the symmetric cyclotomic polynomial

    Ψ_t(X,D)=Φ_t((X+√D)/2,(X−√D)/2) ∈ Z[1/2][X,D].

It has degree φ(t) in X. Clear denominators in Ψ_t(X,−1/t), without removing content, to obtain F_t(X)∈Z[X]. The clearing denominator has prime factors only in 2t. If ℓ|tp+1 and ℓ≡−1 (mod t), then for every admissible trace P,

    (PI) ⇔ ℓ | F_t(P).                                  (7)

In particular every possible intersection at fixed (t,P) lies in the explicitly finite set

    S_t(P)={ℓ prime: ℓ|F_t(P), ℓ≡−1 (mod t)}.            (8)

For such ℓ the additional condition on p is exactly p≡−t⁻¹ (mod ℓ).

*Proof.* Cyclotomic symmetry under swapping α,β gives Ψ_t∈Z[P,Q], hence the displayed dyadic polynomial on substituting Q=(X²−D)/4. Reducing ℓ|tp+1 replaces D=p by −1/t. The prime ℓ cannot divide t. At an inert ℓ, Q is nonzero, and Φ_t(α,β)=0 is equivalent to α/β having exact order t, since characteristic ℓ does not divide t. Clearing the allowed denominators preserves zeros. Nonvanishing of F_t(P) for integral P follows from Theorem 4 below, including its t=4 exception. ∎

**CERTIFIED / exact symbolic examples.** Denominators shown are those in Ψ_t(X,−1/t)=F_t(X)/b_t:

| t | F_t(X) | b_t |
|---:|---|---:|
| 4 | 4X²−1 | 8 |
| 8 | 64X⁴−48X²+1 | 512 |
| 12 | 144X⁴−168X²+1 | 2304 |
| 16 | 65536X⁸−114688X⁶+17920X⁴−448X²+1 | 8388608 |

**PROVED / examples of (7).** P=1,t=4 permits only ℓ=3, hence p≡2 (3); P=3,t=4 permits only ℓ=7, hence p≡5 (7). P=1,t=8 has F_8(1)=17 and **no inert target prime whatsoever**, for any p. P=1,t=12 has F_12(1)=−23 and permits only ℓ=23, hence p≡21 (23). These are exact congruence families, not chance discoveries of large Lucas divisors. They also explain why a fixed trace performs poorly on congruence-hard primes.

**Assessment.** The elimination does not prove failure for growing t. It identifies exactly where the p-dependence resides: a growing menu of congruences indexed by prime factors of F_t(P). BHV controls Φ_t at D=p, not this independently specialized F_t. No improvement to B2 follows by factoring the latter first.

### 3.2 Exhausting rational-function identities at a fixed index

**PROVED, Theorem 4 (exact-index identity obstruction; specialization of TORSION_FIRING Proposition 3.5).** Let 4|t and let A(Z)∈Q(Z) be regular at Z=−1/t. Then

    Ψ_t(A(Z),Z) vanishes at Z=−1/t

if and only if t=4 and A(−1/4)=±1/2. In particular no fixed odd integral trace P yields a polynomial divisibility identity by tZ+1, for any 4|t; no rational-function trace can do so for exact index t>4.

*Proof.* At Z₀=−1/t, the two roots lie in Q(√(−1/t)), have nonzero product (A(Z₀)²+1/t)/4, and are distinct. Vanishing means their ratio is a primitive t-th root of unity. Its degree is at most 2, so φ(t)≤2. Among multiples of 4 only t=4 remains. Here Ψ_4(X,D)=(X²+D)/2, giving X=±1/2. ∎

**PROVED / the actual exceptional identity.** For P=2p+1,

    Φ_4(α,β)=(P²+p)/2=(4p+1)(p+1)/2.                   (9)

Every prime factor of 4p+1 therefore has rank 4, but may be split: p=13 gives 4p+1=53≡1 (4). Identity (9) supplies no inert factor and no new ES guarantee. It is more directly matched to discriminant p than the prior identity U_4(1,−2Cp)=1+4Cp, but remains a rank-4/sign-only construction.

**PROVED / U and V warnings.** Divisibility of U_t need not mean exact rank t. For example a trace A(Z) with A(−1/t)=0 forces rank 2 at the specialization, so U_t vanishes for every even t without giving the target order. More generally the specialized ratio is a root of unity in a quadratic field, and its order lies in {1,2,3,4,6}. This is the complete obstruction to exact large index, not to every lower-rank U_t identity. A V_t identity at 4|t is impossible for a rational specialized trace: V_t=0 requires ζ^t=−1, and none of those possible orders has this property when 4|t. Poles at the specialization, singular degenerations, growing-degree algebraic traces, and nonidentical prime-factor intersections are not covered by the theorem. **R-z46 repair (no-go calibration):** this excludes an identity making the entire linear polynomial `tZ+1` divide the specialized exact-index expression. It does not prove that rational identities cannot force some common prime factor, or that no other arithmetic argument can force support at `t>4`. The degree-of-roots-of-unity obstruction is already TORSION_FIRING Proposition 3.5; the new content here is its exact specialization and the trace/support accounting, not a new general identity barrier.

**CERTIFIED / systematic identity search.** `z46_primitive_intersection_algebra.py` constructs Ψ_t(X,−1/t) exactly for all 32 multiples of 4 through 128, using the binomial formula for U_d and exact cyclotomic division. Rational-root enumeration finds only ±1/2 at t=4. It tests 2880 specializations A(Z)=aZ+b, even −8≤a≤8, odd −9≤b≤9. The only zeros are t=4 and (a,b)=(−6,−1),(−2,−1),(2,1),(6,1), exactly the condition 4b−a=±2. It also factors F_t(P) for every 4|t≤32 and odd P≤15 and checks the exact rank of every eligible prime factor. The all-t theorem, not the search bound, excludes further rational exact-index identities.

### 3.3 Fundamental units and continued fractions: an extra constraint, not coupling

**PROVED / normalization caution.** A unit ε=X+Y√p of norm q=±1 naturally supplies the Lucas pair with trace 2X, norm q and discriminant 4pY². Its ratio is represented in the discriminant-p Cayley coordinates by the **rational trace** P=X/Y. Simply inserting the integral numerator X (or the numerator of a half-integral fundamental unit) into Q=(P²−p)/4 does not preserve the unit. At primes ℓ∤2pY, the normalized rational trace and the actual integral unit pair have the same rank and quadratic character. Thus this is a legitimate extension of the local dictionary, not necessarily a member of the original odd-integral-P family.

**PROVED, Lemma 5 (unit 2-part selection).** For a target ℓ≡−1 (mod t), let k=(ℓ+1)/t. If the unit ratio has exact order t, then

    norm ε=+1 ⇒ k is even,
    norm ε=−1 ⇒ k is odd.                              (10)

*Proof.* Frobenius exchanges ε and ε′ and εε′=q. For z=ε/ε′,

    z^((ℓ+1)/2)=q^((1−ℓ)/2)=(q/ℓ).

Since 4|t and ℓ≡3 (4), this right side is +1 for q=1 and −1 for q=−1. Exact order t makes the left side (z^(t/2))^k=(−1)^k. ∎

**Assessment.** Powers of a unit do not bypass (10): squaring gives norm +1 and squares the ratio, possibly losing the desired 2-part of its order. These constraints supply no divisibility by tp+1. Existing CF/norm-window no-go statements in FRONTIER concern other uses of unit data; we do not apply them indiscriminately to this rank experiment.

**CERTIFIED / unit experiment.** For each scanned prime, use the first continued-fraction convergent X/Y of √p with X²−pY²=±1, i.e. a canonical unit of Z[√p] (not a claim to compute the fundamental unit of the maximal order). Every one of the 2370 Mordell-hard cases has norm −1; the largest X has 3902 bits. The unit fires at 1087 levels, covering 874 primes; its square fires at 530 levels, covering 463 primes. Among the 9234 eligible (t,ℓ) pairs, 5113 have odd k and 4121 even k; every actual unit hit satisfies (10). At p=193 neither unit nor its square realizes the sole prime certificate (8,103), whereas P=9 does. No canonical-unit forcing appears.

### 3.4 Census, conditional random model, and controls

**CERTIFIED / methods and bounds.** The scan fixes T=256 and odd P≤63 for **all 2370** primes p<10⁶ in the six Mordell square classes mod 840. It also uses a deterministic, evenly spaced 256-prime baseline from p≡1 (4) outside those classes, and separately exhausts every 4|t≤p+2 at the eight requested test primes. It factors tp+1, checks reconstructed factorizations and primality, and computes order by binary powering in F_ℓ[s]/(s²−p), never by constructing U_t. The symbolic script independently checks the selected full-range results through h|p+u, h≡−1 (mod 4u), 1≤u≤(p+1)/3, and checks stored rank witnesses with the Lucas recurrence. Working memory is bounded: small factorizations, O(log t) field powering, per-prime rows, ≤128-degree polynomials, and a roughly 1.34-million-entry integer sieve for the full-support check below. Both scripts ran with a 2 GB address-space cap and 300/120-second timeouts. Data total less than 1 MB.

**CERTIFIED / coverage, common T=256.** Entries are numbers of primes with at least one hit:

| detector | Mordell-hard / 2370 | non-Mordell baseline / 256 |
|---|---:|---:|
| unrestricted trace / eligible prime factor | 2280 | 253 |
| P=1 | 321 | 151 |
| P=3 | 706 | 148 |
| odd P≤15 | 1740 | 241 |
| odd P≤63 | 2075 | 249 |
| odd P≤63, t>30 | 1296 | 145 |
| canonical CF unit | 874 | 195 |
| squared CF unit | 463 | 93 |

**EVIDENCE / reading.** Mordell-hard primes remain harder: short-trace success is 87.6%, versus 97.3% in the baseline; the disparity for P=1 is larger (13.5% versus 59.0%). The baseline is a deterministic comparison sample, not a claim of unbiased inference or a limiting density. Of 13 Mordell-hard primes with |p−m²|≤4, 11 have an eligible factor and all 11 are hit by P≤63; the two misses are 3361 and 9601. This tiny subgroup cannot establish a near-square law.

**PROVED / the appropriate conditional model.** Conditional on an actual pair in E_p(T), a uniform trace has probability ρ=φ(t)/ℓ, with no extra factor 1/2 for inertness: inertness is already forced. For a list of H traces each having uniform marginal residue, the expected **incidence** count is Hρ, regardless of dependence within the list. Uniformly translating a consecutive odd list gives exactly these marginals. Independent random traces would instead give pair-occupancy probability 1−(1−ρ)^H; that is not an exact formula for consecutive traces. If p itself is heuristically sampled among primes in reduced classes modulo ℓ, the side-number event has local probability 1/(ℓ−1), not 1/ℓ. Combined with a uniform trace it contributes φ(t)/(ℓ(ℓ−1)); this averaged heuristic is not a fixed-p existence theorem.

**CERTIFIED / incidences, not just occupied levels.** Across the Mordell scan there are 9234 eligible (t,ℓ) pairs at 7116 levels. The 32 fixed odd traces yield 24529 incidences, versus exact uniform-marginal expectation 25237.705. Eight seeded random translations of the same trace list, independently at each pair, give

    25181, 25094, 25161, 25270, 25293, 25143, 25157, 25136.

The baseline gives 6620 incidences versus expectation 6734.600. The near-square subset gives 155 versus 161.161. These expected values are conditioned on the actual target factorizations, not estimates of how often the factorizations supply target primes.

**EVIDENCE / interpretation.** Fixed small traces show a 2.8% deficit relative to the Mordell conditional expectation, not a positive coupling. The translated controls are diagnostic; they are not new globally integral traces common to all pairs. No asymptotic or p-uniform probability conclusion follows.

**CERTIFIED / complete finite range at the requested primes.** These are global failures or successes of the displayed restricted detector, since all 4|t≤p+2 are exhausted:

| p | (★) hit levels | prime-hit levels | odd-P≤63 hit levels |
|---:|---:|---:|---:|
| 193 | 2 | 1 | 1 |
| 409 | 0 | 0 | 0 |
| 577 | 0 | 0 | 0 |
| 2521 | 1 | 0 | 0 |
| 3361 | 1 | 0 | 0 |
| 5569 | 0 | 0 | 0 |
| 9601 | 0 | 0 | 0 |
| 66529 | 4 | 0 | 0 |

**CERTIFIED / complete prime-support census below 10⁶.** A further reverse sieve exhausts **all** levels, not only t≤256: enumerate every prime ℓ≤(4·999999+1)/3 with ℓ≡3 (4), every 4|t dividing ℓ+1, and the progression p≡−t⁻¹ (mod ℓ), p≡1 (4). The bound (2) proves completeness. Among all 39175 primes p≡1 (4) below 10⁶ there are 274348 target pairs and **94 primes with empty support**; 58 of these are Mordell-hard. In the ranges [5,10⁴), [10⁴,10⁵), [10⁵,10⁶), the failure counts are respectively **11/609, 24/4174, 59/34392**. The largest is 997201; the first is 73. All 94 zeros are independently checked through prime factors h of p+u: proper factors require u≤(p+2)/7, while h=p+u is tested via u|p+1. Thus these are global failures of (PI) with arbitrary trace, not a short-list artifact.

**EVIDENCE / caution on PI∞.** Failures continue throughout the tested range. The shrinking failure proportion does not establish finiteness of failures; the increasing absolute counts provide no affirmative evidence for eventual universal success. Prime-only thinning is a real additional lower-tail problem. A theorem or larger-range model for this restricted support is needed before treating PI∞ as a plausible ES strategy.

**CERTIFIED / explicit composite losses.** At 2521 the sole unordered (★) factor pair is t=44, (87,1275); at 3361 it is t=20, (99,679). At 66529 the four are

    t=8:   (39,13647),     t=36:  (323,7415),
    t=116: (1623,4755),    t=512: (2559,13311).

All endpoints are composite. At 193 the prime certificate is t=8, ℓ=103, P=9, Q=−28, yielding (u,B,C)=(13,2,2) and denominators 52,772,5018. Consequently **no choice of P whatsoever**, canonical, huge or selected by factoring a Lucas term, can make the original (PI) work at 2521 or 66529. This is a restriction of this line, not a failure of ES or of all PM-II certificates.

**PROVED / T1.** At n=m² and ℓ|tn+1, ℓ∤m and (n/ℓ)=+1. The inert condition is impossible, even though split primitive divisors can exist. The mechanism vanishes at precisely this step, not through nonexistence of all Lucas factors.

**CERTIFIED / controls.** For every odd m from 3 through 31, all 4|t≤m²+2 have zero inert factors and zero (★) certificates. For numerator 8 the analogue is t=8C, N=tn+1, with the same factorization and positivity bound t≤n+2. All these levels at n=131 and 241 have zero target divisors, despite respectively 15 and 31 inert-prime-factor incidences. For 131≡3 (4), (P²−131)/4 is not integral for odd P: the finite-field Cayley dictionary remains valid, or use integral roots P±√131 with discriminant 4·131. Thus the control does **not** silently apply a nonintegral Lucas pair. The obstruction is target class/order, not lack of inert factors. The checked conditions are sufficient subfamilies for 8/n; the full nonrepresentability of 8/131 and 8/241 is the prior result cited in FRONTIER, not inferred from these subfamily counts.

### 3.5 What the literature actually supplies

**PROVED (literature, precisely attributed).** Bilu–Hanrot–Voutier, *Existence of primitive divisors of Lucas and Lehmer numbers*, J. reine angew. Math. 539 (2001), 75–122, Theorem 1.4: every Lucas/Lehmer term of index t>30 has a primitive prime divisor. The retained primary download `bhv.txt` is an access-block page, not evidence of reading the paper. The statement is verified through Stewart's introduction and P. Voutier, *n-defective Lehmer pairs for small n: Corrections and Clarifications*, arXiv:2411.07909v2, introduction; Voutier's Theorem 1 repairs small Lehmer classifications, not the t>30 bound. The exact excerpts are in `data/z45_recent_pointwise_tools/`.

**PROVED (literature statement).** C. L. Stewart, *On divisors of Lucas and Lehmer numbers*, arXiv:1008.1274v1, Theorem 1, gives

    P⁺(Φ_t(α,β)) > t exp(log t/(104 log log t))

for t>C, with C effectively dependent on ω(αβ) and the discriminant of Q(α/β). Its introduction explains the combination of archimedean size with upper bounds on prime valuations. This is a lower bound for a greatest prime factor of the cyclotomic value, not a lower bound for its prescribed gcd with tp+1; uniformity in the changing field cannot be assumed.

**PROVED (verified secondary attribution).** Stewart §1 records Schinzel's eventual primitive-divisor theorem for Lehmer numbers (1962), and its uniform predecessor to BHV (1974). The latter reference is A. Schinzel, *Primitive divisors of the expression Aⁿ−Bⁿ in algebraic number fields*, J. reine angew. Math. 268/269 (1974), 27–33. We use no unverified effective threshold or general assertion about all polynomial values.

**Assessment.** None of these statements bounds the inert primitive part **inside** gcd(U_t,tp+1). Even an arbitrarily large primitive part can be entirely coprime to tp+1, and a largest factor can lie outside the certificate bound (2). Schinzel-style primitive divisors of power/polynomial expressions still concern the values of the chosen expression. Making that expression identical with the side number brings back Theorem 4; making it share an unspecified factor is the intersection problem itself. These observations reject the stated transfers, not all possible refinements of logarithmic-form, primitive-part, or polynomial-value methods.

## 4. Every FRONTIER §4 screen

**Assessment.** PASS means the issue is respected, not that an ES existence mechanism is supplied.

| # | status | reason |
|---:|---|---|
| 1 odd squares | PASS | Inertness is impossible at m²; essential use of the quadratic character. |
| 2 numerator 8 | FAIL as forcing | The dictionary also works at 8C; the controls have no targets. No 4-specific existence input. |
| 3 numerator-uniform laws | FAIL as forcing | No distinguishing transport/counting law is supplied; a threshold-free uniform conjecture is false. |
| 4 tied modulus | FAIL | The missing step is a prime in gcd(U_t,tp+1) with inert exact rank t. |
| 5 fixed p | PASS for theorems | CRT trace averages keep p fixed; the p-averaged local heuristic is explicitly not a proof. |
| 6 scale | PASS as safeguard | No power-size count of distinct ES solutions: trace multiplicity merely repeats the same certificates. |
| 7 one-sided | PASS | PI∞ asks nonemptiness, not a false two-sided asymptotic for R. |
| 8 B1 | FAIL for fixed menus; open for growing t | Theorem 3 makes finite (t,P) menus explicit congruences; identity coupling is ruled out at t>4. |
| 9 class not parity | PASS after intersection | Inert exact order t really gives the entire class −1; neither condition alone does. |
| 10 privacy | PASS | Theorem 2 actually proves distinct target pairs have distinct primes; no cross-shift collision. |
| 11 signed reflection | N.A. | Formula (1) produces positive certificates directly. |
| 12 relaxation transport | FAIL for bare BHV | Its primitive primes are not forced into tp+1 or the bound (2). Actual PI hits need no transport. |
| 13 BM shortcut | PASS | Neither local solubility nor the BM sign is asserted sufficient. |
| 14 hard primes | FAIL for universal detector | Complete failures at 409,577,2521,3361,5569,9601,66529; require a threshold or more slices. |
| 15 Mordell / near squares | FAIL as uniform forcing | The full Mordell scan shows losses, not a surviving deterministic mechanism. |
| 16 thin-family transfer | PASS as safeguard | Identities are scoped precisely; no transfer from special polynomial families is claimed. |
| 17 large-factor class | FAIL at existence step | Exact order would control it, but no theorem forces a prescribed large factor to have that order. |

## 5. New-theory sketch and solved toys

**Assessment / proposed framework: target-conditioned torsion occupancy.** Rather than count all primitive divisors, retain three objects separately:

    E_p(T): the prescribed prime-certificate support;
    A_(t,ℓ)⊂F_ℓ: the φ(t) good trace residues;
    I_p(T,H)=Σ_(t,ℓ)∈E_p(T) #{odd P≤H: p∤P, P mod ℓ∈A_(t,ℓ)}.

The new input would have to address **support nonemptiness**, or support nonemptiness jointly with short-trace occupancy. Theorem 2 solves full-residue occupancy exactly once support is present; it does not solve support. Theorem 3 expresses the same incidence from the other direction, through prime factors of F_t(P). This separation prevents the common mistake of treating a positive trace average conditional on support as a proof that support exists.

**CONJECTURE / first genuinely useful theorem needed.** Prove PI∞, or a weaker family-union version over all three Type-II rows of §2.1 with explicitly handled exceptions, by an arithmetic estimate that is not conditioned on E_p(T)≠∅. A quantitative short-trace version could lower-bound I_p(p+2,(log p)^A) by a positive constant for every sufficiently large prime. Its exact remaining implication is still an eventual single-prime divisor-class theorem; no standard conjecture or pointwise tool cited here is known to imply it.

**CERTIFIED toy 1 (joint independence, including admissibility).** At p=5, the target pairs (4,3),(4,7) have trace probabilities 2/3 and 2/7. Among the 84 odd residues P mod 210 avoiding multiples of 5, the counts with 0,1,2 hits are respectively **20,48,16**. Hence union density is 16/21=1−(1−2/3)(1−2/7), and simultaneous density 4/21. This tests the stronger CRT theorem rather than merely repeating the old one-prime trace count.

**CERTIFIED toy 2 (short consecutive lists are not independent).** At (p,t,ℓ)=(193,8,103), the good trace residues are {9,10,93,94}. Translate the 32 odd traces 1,3,…,63 through all 103 offsets. The counts of offsets with 0,1,2 hits are **20,38,45**; the exact mean is 128/103 and union probability 83/103. The independent-draw prediction is only 1−(99/103)^32≈0.718. Thus even the trace-selection toy needs dependence control for occupancy, although the incidence expectation is exact. Neither toy addresses whether a target pair exists.

## 6. Verdict and next steps

**Assessment: PARTIAL, promise 1/5.** The strongest unconditional result is the combination of Theorems 1–3: the original primitive-intersection family is exactly prime-divisor (★), its full trace ensemble has an explicit CRT product law, and its fixed-trace intersections are exactly an explicit specialized-cyclotomic prime menu. Theorem 4 closes rational exact-index identity coupling at every 4|t>4. These are precise restrictions and useful bookkeeping, not progress toward an ES lower-tail estimate.

**Assessment / concrete next steps.** First, before investing in any new BHV transfer, demand a lower bound for the inert rank-t part of gcd(U_t,tp+1), or an explicit coupling not covered by Theorem 4. Second, if continuing computations, extend the separate **prime-divisor (★)** census beyond 10⁶ and model its 94 failures before conjecturing eventual success; retain composite-only certificates, since a full-(★) census is insufficient evidence for PI∞. Third, any proposed CF/unit rule should first beat the conditioned φ(t)/ℓ baseline and the parity exclusion (10), rather than merely find many ordinary ES certificates. Extending to the three Type-II rows is legitimate only with the exact side integers and ranks in §2.1; it cannot be silently identified with the original (PI).

**Reproducibility.** Own files only: this document; `scripts/z46_primitive_intersection_scan.py`; `scripts/z46_primitive_intersection_algebra.py`; `data/z46_primitive_intersection/{summary.json,rows.jsonl.gz,baseline.json,algebra.json,full_support.json}`. Run the scan before the algebra script, which independently checks its selected full-range results. Existing z45 scripts already cover the basic Cayley/rank census; the added checks concern elimination, joint occupancy, units, and the extended full-range failures.
