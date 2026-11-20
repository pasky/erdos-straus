## §0

Result: For every prime p the pointwise cap satisfies e*(p) ≤ exp(C√(log p · log log(3p))) with an effective absolute C; for p ≡ 1 (8) there is also the explicit bound 4e*(p)+3 ≤ √(4p/3).  Label: PROVED (rel. Gallagher–Linnik, Minkowski II; explicit bound rel. Gauss reduction/genus theory).
Scope: Capped ES only, not ES, not a subpower bound on the least prime non-residue in a prescribed progression, not an exceptional-set improvement.
Review: internal hostile (§6); cross-review owed before promotion.
Triage: RECORD
STATUS delta: Proposed for §1B after review: at primes, e*(p) ≤ exp(O(√(log p · log log(3p)))) unconditionally and effectively, and 4e*(p)+3 ≤ √(4p/3) at p ≡ 1 (8) (`notes/z75/ANALYTIC_BREAK.md`). Retain the existing results for other n and under GRH.

# A large window with a short exponent vector

All logs natural. The nonclassical case is p ≡ 1 (8); for other odd primes the integral identities in `EXSET_LINNIK_CAPS.md` Lemma 4.3 suffice, and p=2 is immediate. We use no bound on the size of the three denominators. The key is not to require the primes we plant in K to generate *all* squares, nor the least non-residue to be a prime 3 mod 4. A separate sign carrier pays just the **index** of the planted square subgroup, not its order. Large windows are now useful.

## 1. Two elementary sign carriers

Write q ≡ 3 (4) for a prime, K=(p+q)/4, b_v=v_v(K). For d supported on K and d ≡ −K mod q, take x=K, A=(K+d)/q, y=pA, z=pKA/d. Then 4/p=1/x+1/y+1/z. At v|d the reduced denominator exponent is (v_v(d)−2b_v)^+ since v∤pq and v_v(K+d)=b_v whenever v_v(d)>b_v; for other cases it is zero. Each overflowing prime divides A. Thus if there is no overflow at 2 and all overflow exponents are even, this is precisely the required relaxation, with cap half the maximum overflow (`CAP_DOWN.md` Lemma 1.1).

*Free carrier.* If (q/p)=−1 then (K/q)=−1. For q ≡ 3 (8), K is odd; for q ≡ 7 (8), (2/q)=1. Thus some **odd** s|K has odd b_s and (s/q)=−1. Taking d=K s^j with j=ord_q(s)/2, an odd integer, gives cap ≤(q−3)/4. This is `CAP_DOWN.md` Prop. 1.3.

*Planted carrier.* Let s be **any odd prime** with (s/p)=−1. Force q ≡ 3 (4), q ≡ 4s−p (mod s²). This is one reduced class mod 4s². Now b_s=1, and (s/q)=(−1/s)(q/s)=(p/s)=−1. The same d works with no condition on (q/p). Effective Linnik gives q ≤ (4s²)^L for an effective absolute L. Thus a small non-residue s, even 1 mod 4, already gives e*(p) ≪ s^{2L}. Using a large power here will cost nothing at the subpower scale. This uses s in the *first denominator*, not the window modulus.

**Independent explicit bound.** Take a reduced form [a,2b,c] of discriminant −4p in the nonprincipal genus, as in Pollack, *The least prime quadratic nonresidue in a prescribed residue class mod 4*, proof of Thm 1 (archived `sources/pollack_jnt2018_least_nonresidue_mod4.pdf`). Here 1<a≤√(4p/3)<p, ac=b²+p. We have (a/p)=−1 even when a is even: over F_p, aF(X,Y)=(aX+bY)²; choose a represented value coprime to 4p (a if odd, c if a even: in the latter case c is odd by primitivity and c≤(p+1)/2 by reduction). Its symbol is −1 by genus. Since (2/p)=1, some odd prime q|a has (q/p)=−1. Also b²≡−p mod q, q∤p, hence (−p/q)=1 and q≡3 (4) by reciprocity. The free carrier proves the explicit §0 inequality. This specialization avoids switching to the larger c as the source of q. It is not needed for the asymptotic proof except as a convenient effective bound below any absolute threshold.

## 2. Elementary alternative to an ineffective Siegel bound

For p sufficiently large put u=log p, k=⌊√(u/log u)⌋, T=√(u log u), Y=p³, w=Y^{1/k}; thus log w=O(T), k log u=O(T). If any prime s≤w is a non-residue, §1 proves the asserted bound (2 is a residue). Otherwise for χ=χ_{−4}χ_p of conductor m=4p every prime ℓ≤w, ℓ≡1 (4), has χ(ℓ)=1. We claim **L(1,χ) ≥ exp(−O(T)) effectively** in this alternative only.

Indeed f=1*χ is nonnegative on all integers. On products of k distinct such primes it is ≥1. There are ≥c w/log w such primes in (w/2,w] by the effective fixed-modulus PNT mod 4, so their distinct products ≤Y number ≥(c w/(k log w))^k = Y exp(−O(T)); here k log w=3u. On the other hand

    ∑_{n≤Y} f(n) = Y L(1,χ) + O(√(mY)).

To see this, truncate the divisor variable d carrying χ at D=⌊√(mY)⌋. Replacing floors of Y/d for d≤D costs O(D); extending ∑χ(d)/d to infinity costs O(Ym/D) by periodicity; the discarded hyperbola tail is ∑_{a≤Y/D}∑_{D<d≤Y/a}χ(d)=O(mY/D). The error is O(p²), negligible. If χ has a real zero β with 1−β ≤ 1/log(4p), then 1−β ≥ exp(−O(T)): on [β,1], |L′(σ,χ)|≪log²(4p), by summing log n/n^σ up to m and summation by parts beyond m using partial sums O(m). This argument uses neither Siegel nor a lower bound for arbitrary quadratic L-values.

## 3. Many admissible windows at polynomial height (uniform, effective)

Take two disjoint alphabets S₁,S₂, of k odd primes each (the first 2k odd primes in two blocks). Write B_i=4∏_{v∈S_i}v³; log B_i=O(k log k)=O(T). For large p both are prime to p. In each alphabet let a_i mod B_i be 3 mod 4 and 4v²−p mod v³ for each v; it is a unit. At q in this class each planted valuation in K is **exactly two**. Set Q=p max B_i and X=Q^A, with A sufficiently large **absolute effective constant**, log X=O(u). We claim that for at least one i the number of primes q≤X in its class with (q/p)=−1 is ≥ X exp(−O(T)) in the second alternative of §2.

Here are the prime-distribution details. Use Gallagher's log-free PNT in the form of Montgomery–Vaughan, *Multiplicative Number Theory III* draft, Thm 28.19, `sources/omega9/montgomery-mnt3.pdf` pp.229–230 (Gallagher, Invent. Math. 11 (1970), 329–339). For fixed κ≥κ₀, A≥6c, sum over all primitive characters of conductor ≤Q of the absolute errors in their prime-weighted θ(X,ψ). The main terms are X for the trivial character and, if present, −X^β/β for the unique exceptional real character ψ₁ with β>1−1/(κ log Q). In the ordinary case the error sum is ≪ X(e^{−A/κ}+A²/Q); in the exceptional case ≪ (1−β)log X · X(e^{−A}+A/Q). Constants effective for fixed κ. We use the exceptional **factor in the error**, not just a zero-free region. The proof of Thm 28.21 there gives the effective Linnik input in §1.

On units mod pB_i the indicator of the desired classes is 1_{a_i mod B_i}(1−χ_p)/2. Its mean is μ_i=1/(2φ(B_i)); every nonzero character coefficient has absolute value μ_i, its support consists of characters of B_i optionally twisted by χ_p. Each has a distinct primitive inducing character (at this one common modulus). Passing to primitive characters affects θ by at most log(pB_i) per character, total weighted error O(log Q), since the coefficient ℓ¹ norm is 1. Choose alphabet i so any exceptional character whose conductor contains a prime of one alphabet is absent from the chosen support: disjointness ensures this, even if the conductor meets both. The only common possible primitive supports are then 1, χ_{−4}, χ_p, χ_{−4}χ_p (gcd(B₁,B₂)=4). More explicitly, an exceptional conductor not dividing either pB_i contributes nowhere; one dividing just one pB_i is discarded. The trivial character has no exceptional zero, χ_{−4} is harmless (negative on the class), χ_p is negative on the selected classes. Thus only χ_{−4}χ_p has a **positive** exceptional coefficient; §2 treats exactly that case.

For clarity on constants: in the exceptional case put h=(1−β)log X≤A/κ. If the coefficient is absent or negative, the main sum is ≥μ_i X. The error divided by μ_i X is O(h(e^{−A}+A/Q))+O(log Q/(μ_i X)), small by choice of A. If the coefficient is positive, 1−X^{β−1}/β ≥ c min(1,h) for large X (use β=1−h/log X and h≤A/κ). The same error is < half this gain, for large absolute A then sufficiently large p, since h/min(1,h)≤1+A/κ and h≥exp(−O(T)) by §2. Without exception choose A so the ordinary error is <μ_i X/2 after weighting. Dividing the resulting θ lower bound by log X proves the claim, since 1/μ_i and log X are exp(O(T)). The large set counts at **fixed p**; large degree cyclotomic Chebotarev and GRH are not used.

## 4. Short corrections even when the planted subgroup is proper

Fix the chosen alphabet S. For each admissible q let U=(F_q^*)² of odd order (q−1)/2 and H=⟨v²:v∈S⟩⊆U. Let Λ be the kernel lattice in Z^k of the map a↦∏v^{2a_v} to H. For B≥1 the number of q with a nonzero relation of sup norm ≤B is at most

    (2⌊B⌋+1)^k (1+2B log(∏v)/log 2).

Indeed each sign vector of exponents gives a nonzero integer difference of two coprime products (unique factorization); all its prime divisors are counted by its log height. Take B=(X exp(−D T))^{1/(k+1)}, D a sufficiently large effective absolute constant. B→∞; the bound is < half the count in §3: the 3^k and log(∏v) cost exp(O(k+log u)) and the remaining factor is B^{k+1}. Fix a surviving q. Then

* |H|≥(⌊B⌋+1)^k>B^k by injection on [0,⌊B⌋]^k. Thus j=[U:H] ≤ X/B^k; j is odd.
* Every h₀∈H equals ∏v^{2a_v} with **nonnegative** integers a_v≤2⌈kX/B^{k−1}⌉. Indeed the sup-norm successive minima of Λ satisfy λ₁⋯λ_k≤det Λ=|H| by Minkowski II on the sup ball. λ₁>B, hence λ_k≤X/B^{k−1}. Rounding coefficients in a real basis of k independent such vectors (which need not span Λ integrally) gives a coset representative of norm ≤kλ_k. Shift the target first by ∏v^{−2L} with L=⌈kX/B^{k−1}⌉, then add L in all coordinates.

Take the free carrier s of §1, necessarily outside S since all planted valuations are even. Since (−s/q)=1, (−s)^{−j} belongs to H. Represent it by the nonnegative correction just constructed. Then

    d = K · s^j · ∏_{v∈S} v^{2a_v} ≡ −K  (mod q).

At s the resulting exponent b_s+j is even, at v∈S it is 2+2a_v, and all other exponents, including at 2, are unchanged. Thus §1 applies with cap ≤max(j,2L). Finally

    log(X/B^{k−1}) = 2 log X/(k+1) + (k−1)DT/(k+1) = O(T).

This proves the theorem uniformly and effectively, including finitely small p by the explicit bound. The difference from `PHASE_DIAGRAM.md` Thm 5.1 and `CAP_INTERPOLATION.md` Thm 4.2(b) is the quotient correction by the independently available s: no Artin generation of U, no roughness sieve on (q−1)/2, no BV in a modulus containing p. The source of the short vector *avoidance* estimate and Minkowski step itself is `PHASE_DIAGRAM.md`, not new here.

## 5. What the tempting alternatives miss

The composite proposal m=3s, (s/p)=−1, s≡1 (4), (3/p)=1: if every factor of K is 1 mod 3, no supported d gives −K even locally. Making λ(m) small never fixes this. The planted-carrier construction instead puts s in K at a controlled valuation while keeping the window group cyclic. Neither result estimates Pollack's n₃(p) below the Burgess range. For Target 2, `EXSET_BEYOND_CRT.md` §1.1: degree ≍t³ at cost t per atom still needs t⁴≲log N even with better prime-distribution errors. The non-CRT quadratic moment in `EXSET_LINNIK.md` Thm 3.1 requires a character bias; the sign carrier produces a *positive* cap at a non-residue, not an integral solution. The implication needed at cap zero goes in neither proof. No θ improvement claimed. On the GRH side the strongest prior *asymptotic* prime bound we located is already exp(O(√(log₂p log₃p))) under Dedekind GRH (`CAP_INTERPOLATION.md` Thm 4.2(b)); do not report O(log p) under that GRH as new.

## 6. Hostile checks and checkpoint

* F1/T1: at odd squares the planted non-residue does not exist and the free window χ_p(q)=−1 is unavailable (the square character is principal off its conductor). The formal prime p argument cannot be replaced by square inputs.
* F2: q must be 3 mod 4 and K=(p+q)/4 integral; from that congruence one cannot divide p+q by 8 in general. No assertion about integral numerator 8. F3: no unscaled composite-input version asserted. F4: no positive count on (★), at its known zeros or anywhere else. Overflow is allowed; it is measured on the *reduced* rational denominator, not its numerator. B6: the prime average selects q for each fixed p, not good p on average. The changing modulus and the cap cost are explicit.
* Two possible fatal shortcuts avoided: (i) merely knowing an effective lower bound on the **least** prime in a progression cannot justify the deletion in §4 (we need many primes); (ii) a correction by squared primes on top of K at odd planted valuations might produce odd overflow. Prescribing valuations **two** removes that parity bug. One cannot charge index j unless the actual correction target lies in H; the minus sign in (−s)^{−j}, and oddness of j, are essential.
* Next push: save the exp(O(k log k)) cost of planting k primes in one progression, e.g. obtain a short-relation deletion estimate counted inside a varying alphabet selected from the natural factors of K. Current theorem balances log X/k against the alphabet cost, not against a lower bound on e*(p). Even a polylog cap is not cap zero.
