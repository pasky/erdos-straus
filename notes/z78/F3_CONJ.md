Result: Both x*_1 and x*_2 are uncovered over F₃[T] for A=T²: Conjecture 0.2 holds and there is no finite linear covering of ES₃(T²,·). Label: PROVED (rel. §§1–3, the sign-symmetry lemma of §4, §6, and the cited tuple, parity, minimum-level and Case A reductions)
Scope: All linear families (Case A and Case B) in the model of FUNCTIONFIELD_ES2 §0, for q=3 and A=T². This is not a result for A=T, a decision on polynomial solutions for individual irreducibles, or a statement about integer ES.
Review: cross-model on §§1–5 (Anthropic Claude Opus, `data/z78/xreview/REVIEW_F3_CONJ_OPUS.md`; D1–D9 applied); fresh Opus hostile review of §§6–7 and their dependencies (`data/z78/xreview/REVIEW_F3_CONJ_R2_OPUS.md`, no mathematical defect; repairs applied). Internal cross-lab review, not external peer review.
Triage: HEADLINE
STATUS delta: retain the existing q=3^r, r≥2, A=T result and replace the q=3 open-target text with “F₃[T], A=T²: x*_1,x*_2 ∈ O(3,T²); no finite linear covering (PROVED rel. the tuple and parity reductions; `notes/z78/F3_CONJ.md` §6; cross-review `data/z78/xreview/REVIEW_F3_CONJ_R2_OPUS.md`).” Remove Conjecture 0.2 from the §2 target. Not a result for A=T, individual irreducibles, or integer ES.

## 1. Two-sided reconstruction (PROVED relative to the indicated tuple lemmas)

Use n=s−2 ∈ {2N−3,2N−2}, K=N+1, u=1+cT. Write X for the short side, B for the long side of (w₁,C₁); write m=m', g=g', V=v₁. In orientation A set (X,B,p,q)=(w₁,C₁,1,u); in orientation B set (X,B,p,q)=(C₁,w₁,u,1). The old Liouville exclusion gives exactly these two disjoint possibilities. Put r=deg X, z=deg m, d=z+r, L=n−d=deg B; L>r+1 in these windows. All four of X,B,m,g are monic T-units. The two identities are mXB=T^n+V and X+B=TgV; thus V is monic, a T-unit, of degree L−1−deg g. Covering is precisely

    pX+qB=T^K H,

by the R3 identity (FF_THIRDS_CORNER Lemma 1.1), since K≤s−1. H≠0 by the exact-tuple exclusion, and has degree h=L+deg q−K with leading coefficient lc q. In particular d≤n+deg q−K.

**Short-side bound in B as well as A.** In A, Mg≡−c mod T^N, M=mX: this is not equality (the exceptional M=g=1 is excluded by FUNCTIONFIELD_ES3 Lemma 2.2). In B, uMg≡c mod T^N and equality is impossible by degree. Thus d+deg g≥N in A, ≥N−1 in B. Consequently deg V≤n−1−N in A, ≤n−N in B. By FF_THIRDS_CORNER Corollary 3.2 the polynomials pMX+qV and its counterpart for the other side cannot vanish identically; T^K divides pMX+qV. Since deg(qV)<K, we have d+r+deg p≥K: **d+r≥N in B**, ≥N+1 in A. This is for both y=deg g regimes; for y≥N the existing extra restriction d+deg V≤s−N−3 remains.

**Reconstruction theorem.** Enumerate H at the prescribed degree and leading coefficient, and only the smaller-degree one of X,m. Given X, test divisibility by q and form B=(T^K H−pX)/q; M is then the polynomial quotient of T^n by B since deg V<L. Test X|M. Conversely given m one can reconstruct X uniquely from the top r+1 coefficients (degrees n+deg q down to n+deg q−r) of mX(T^K H−pX)=q(T^n+V), aligning both sides at degree n+deg q. More explicitly, start at degree r and descend to degree 0: the coefficient x_i first enters the linear term at degree z+K+h+i, and its effect there is lc H; in the quadratic term its effect has degree ≤z+deg p+r+i<z+K+h+i. At these degrees the V term is absent since n−r=L+z≥L. This triangular system recovers X. In either route, verify the original identities, all degrees, monicity, units and covering. No random or independence assumption enters. The number of trials up to polynomial factors is 3^(h+min(z,r)). Here h≤N−d, and max(z,r)=d−min(z,r)≥max(d/2,N−d)≥N/3. This route costs 3^(2N/3+o(N)), superseded by 3^(N/3+o(N)) in §3. These are quotient/factor trials, not distinct M's.

## 2. Moving ABC to the covering congruence (PROVED)

**Theorem.** With K=N+1 and v=deg V, put F=pMX/(qV). Then F′≠0 and K≤deg rad(uMV)≤1+d+v. In particular y=deg g=L−1−v≤n−1−N, strictly below N in either orientation.

*Separable proof.* T^K divides pMX+qV (Lemma 3.1); the denominators are T-units. The sum is nonzero by Corollary 3.2. Divide both summands by their gcd D, retaining divisibility of the sum by T^K. Mason–Stothers bounds the degree of the coprime sum by the sum of the radical degrees of the two summands plus the degree of its radical minus one. The latter radical has degree ≤deg(sum)−K+1. Since rad(pqMXV)=rad(uMV), cancellation proves the claim. The only contribution of u in the radical bound is its degree one.

*Inseparable proof.* Both orientations give V | T^n+MX (because MX+B M=TgMV and MB=T^n+V). Also gcd(MX,V)=1 since MX is supported on M and MB=T^n+V with T∤M. Work over the perfect field F₃. If F′=0, the multiplicity at each prime of F is a multiple of three, so (away from u) V and MX are separately cubes up to units. Let U=T+c be the monic associate of u. Write MX=U^i A³ and V=U^j D³ (monic polynomials), 0≤i,j≤2. By coprimality and ord_U(F)≡0 mod 3 exactly one of i,j is nonzero.

If j>0, put f=T^n+V. Then TU f′−jT f=T^n(nU−jT), whose last linear factor is nonzero (U(0)≠0, j≠0 in F₃). As T∤f, deg gcd(f,f′)≤1. But M|f and MX=A³ with X|M mean every prime dividing M occurs at least twice in M. Hence M has degree at most 2: there is at most one repeated prime of f, linear and of multiplicity exactly 2 (multiplicity ≥3 contributes at least 2 to the gcd). If i>0 and 3∤n, then V=D³ and f is squarefree (f′=nT^(n−1)), so MX has multiplicities at most 2 and hence M is supported on U alone with d≤1. Neither d≤2 alternative fits §1 for N≥5 (d+r+deg p≥K, r≤d); at N=4 the inequalities 2d+deg p≥K and d≤n+deg q−K are already incompatible.

Finally if i>0 and 3|n, V=D³ divides T^n+MX, whose derivative iU^(i−1)A³ is prime to V. Thus V=1. The parity law z≡v≡s mod 2 (FF_ODD_ABSENCE Cor. 1.7) forces n even. But U|M|T^n+1 contradicts (−c)^n+1=2. This proves separability without descending to a nonexistent smaller covering tuple. ∎

**Active-prime sharpening (PROVED).** Let R₃(F) be the product of monic primes whose signed multiplicity in F is nonzero mod 3. The nonzero differential coefficient F′/F has only simple finite poles, all on R₃(F), and tends to zero at infinity. Thus the numerator over R₃(F) is nonzero of degree at most deg R₃(F)−1. It is divisible by T^(K−1) because F≡−1 mod T^K. Hence **deg R₃(F)≥K**. In particular neither MX nor V can be a cube: otherwise deg R₃(F)≤1+v or ≤1+d respectively, both <K. This excludes the Frobenius branch of the original ABC equation too, including when 3|n. If 3 divides deg(pMX)−deg(qV), the logarithmic derivative is O(T⁻²) at infinity, raising K to K+1.

## 3. Elimination of the two large powers (PROVED)

Write b=n−K and δ=N−b∈{3,4} (notation for §§3–5; b is not the degree of C in FF_THIRDS_CORNER), P=deg p, Q=deg q, κ=(q−p)/T∈{c,−c}. Define two nonzero polynomials

    T^K J = pMX+qV,                 T^N S = pMg+κ.

The first is integral and nonzero by §1; the second is the original short-side covering congruence, using uMg≡c for B. Nonvanishing of the second was checked in §1. We have j=deg J=d+r+P−K and deg S=b+P−v (by y=L−1−v). Direct substitution and X+B=TgV give

    MH=qT^b+J,                     VS=pT^b+J.

Hence modulo M, J≡−qT^b and T^N S≡κ; define W=(T^δ SJ+κq)/M, an integral nonzero T-unit (the numerator has constant κ). Multiplication by V and use of the preceding identities give

    VW=T^δ HJ−κpX,                 pXS=T^(b+1)W−qH.

For the first, subtract the two expressions after multiplying by M and use MH−VS=κT^(b+1), T^K J=pMX+qV. For the second eliminate qVW between q(VW) and (T^K J−pMX)W: (T^K W−qT^δ H)J=pX(MW−κq)=pXT^δ SJ. Cancel T^δ J. Since δ>deg q, the first defining expression for W has degree δ+deg S+j−d, i.e.

    deg W = r−v+2P−1 ≥ 0.

In particular **N−d≤v≤r−1 (A), N−d≤v≤r+1 (B)**. Also deg rad(uMV)≥K, indeed deg R₃(F)≥K (§2). This bound does not use a probabilistic model. The last product gives an alternative exact enumeration: for fixed H,W, each X divides T^(b+1)W−qH, after which §1 recovers everything. In fact MW=T^δ SJ+κq and MH=qT^b+J give T^δ SH−W=pqg after multiplication by M. Eliminating M from the same pair gives the companion product **pgJ=T^b W−κH**.

**Upper search exponent 2/5 (PROVED; superseded below by N/3, not the engine used in the census).** At a fixed degree pattern use the cheapest of four indices: (i) V, factoring T^n+V for M and X; (ii) J, factoring qT^b+J for M and pT^b+J for V, then pMX=T^K J−qV; (iii) H and the shorter of m,X as in §1; (iv) H,W as just proved. Both polynomials in route (ii) are nonzero by the identities MH and VS. Deterministic Berlekamp factorisation over the fixed base field costs poly(N); a degree-O(N) polynomial has 3^o(N) divisors uniformly (split at prime degree (log₃ N)/2: O(√N) low primes with ≤O(N) choices each, and O(N/log N) high prime factors with multiplicity). Each factor list produces only subexponential overhead, including choosing X|M. From h≤N−d, w≤r−v+1 and j≤d+r−N, the four base-3 exponents are at most v, d+r−N, N−r (using z=d−r), N−d+r−v+1. If their minimum is e, adding the second and fourth gives 2e≤2r−v+1; using v≥e and r≤N−e gives 5e≤2N+1. Thus complete search costs 3^(2N/5+o(N)). No decay of the number of hits follows from this running-time bound.

### A second contact of order n forces W to have bounded degree (PROVED)

Write A₀=qB−pX, a T-unit of degree L+Q. Completing the square in characteristic 3 gives

    m A₀² + uV = T^n D,        D=m T^(2K−n) H²−u.

Indeed A₀²=(qB+pX)²−4pqBX, with 4=1 and pq=u. D(0)=−1. Apply the same logarithmic-derivative test, now to G=m A₀²/(uV), which agrees with −1 to order n. If G were a cube, every prime of V outside u(q+p) would occur in V with multiplicity divisible by 3: such a prime misses m and also A₀, since A₀≡−(q+p)X mod V and gcd(X,V)=1. Thus all active primes of the *first* ratio F would lie on u(q+p)M, of degree at most d+2 < K, contradicting §2. Hence G′≠0, and

    n ≤ deg R₃(G) ≤ z+L+Q+1+v = n−r+Q+1+v.

Together with §3 this gives **r−Q−1≤v≤r+2P−1**, i.e. the §0 ranges. Since lc S=lc p and lc J=lc p, W is monic. In A, w=r−v−1∈{0,1}; in B, w=r−v+1∈{0,1,2}. Since W(0)≠0, the search needs just 3 possible polynomials in A or 9 in B, independent of N! Furthermore w≡d+1 mod 2 by the tuple parity law. This sharpens the running-time proof too: the H,W route has exponent h+O(1)≤N−d+O(1), and the J route j≤2d−N. Their minimum is ≤N/3+O(1); hence **3^(N/3+o(N))** complete search with factoring. No claim is made that every W on these lists occurs. Quantitatively, 0≤deg(m A₀ uV)−deg R₃(G)≤1+P−w. Thus repeated factors and common support in this product together cost at most two degrees (including inactive primes); this is an additional restriction, not an assertion of squarefreeness.

## 4. Census and an infinite near-miss family

**PROVED (direct substitution).** The repeated B-oriented near-miss at c=1, N=0 mod 3 is not random. For every odd k≥5 set n=3k, N=(3k+3)/2, m=T+1, X=(T^k+1)/(T+1), B=T^(2k)−T^k−1, V=T^k−1. Here M=T^k+1, MB=T^n+V and (1+T)X+B=T^(2k), divisible by T^K. But B+1=T^k V, so (X+B) mod TV equals X−1, of degree k−1. Moreover (T+1)(X−1)≡1−T mod V and gcd(T+1,V)=1; thus gcd(TV,X+B)=T(T−1) up to a unit, even if 3|k. In particular these candidates pass the low and high coefficient tests and fail exactly the condition defining g. This is not a family covering x*_1.

**Sign symmetry (PROVED rel. the parity law; Opus D6).** On monics put σf=(−1)^(deg f)f(−T), a multiplicative involution. Since z≡v≡n (mod 2), r≡L (mod 2); since y+1+v=L, substitution T↦−T with these signs preserves mXB=T^n+V and X+B=TgV. Moreover y+z+deg w₁≡L−1+deg w₁≡1 mod 2, so the new E is E(−T). Thus σ bijects covering tuples at c with those at −c, preserving level and orientation. The c=2 run is a consistency check, not independent evidence.

**EVIDENCE (a second near-miss pattern, Opus).** In A at N=24 and 33 (n=9k, k=5,7), the witnesses have m=1+T and X=T^(4k)+T^(3k)−T^(2k)−T^k−1 at c=1. This observation is finite; no claim about larger k is needed.

**Census protocol (CERTIFIED relative to the degree filters).** Data under `data/z78/` and sources `scripts/z78_f3{,_hybrid}.c`. Build with gcc -O3. Two disjoint bit planes represent ±1 coefficients. `f3_1.txt`, `f3_2.txt` run levels 4..28; `f3_high_{1,2}.txt` continue 29..31. Both n, c and orientations are separate rows. `Mpool` counts *distinct* monic T-units in the allowed d range prior to imposing z parity. `trials` counts the actual H/short-factor trials, then `unitX`, `intB`, `split`, `monicV` count successive tests. `case1/2[vbound]` applies the older upper bound on v from §1 and parity v≡z≡n (FF_ODD_ABSENCE Corollary 1.7); `integralG` is the survivor count after TV | X+B. Extremal gcd and remainder degrees refer to the last divisibility; a witness is m/X/B in ascending ternary coefficients, sentinels −1/99 mean no trial reached this stage. On paths that reach it, no nonintegral g has been rounded to a polynomial.

**Hybrid lift (PROVED, algorithm).** For fixed H with degree h and fixed j, all possible J are exactly J=−(qT^b mod H)+HD with deg J=j and lc J=lc p. Enumerate the affine class (one trial at most if j<h); then M=(qT^b+J)/H. For z>0, §3 gives deg(qV)≤r+P<d+P so X is the quotient of T^K J by pM. For z=0 simply X=M. Test every reconstructed tuple directly. The hybrid uses this lift or the first algorithm depending on which has fewer indexing digits. It records the stronger §3 window on v: the near-miss counts in the two programs therefore need not agree. `case2` is identically empty in the hybrid by §2. `split` here counts monic integral sides before checking whether MB−T^n has the required degree. No factorisation library or probabilistic subroutine is used. The census checks necessary conditions for exact points, not a sampling of residue classes.

**Finite result (CERTIFIED relative to the PROVED degree windows §§1–3).** `hybrid_{1,2}.txt`: through N=38, zero hits, both orientations and both c; N≤3 is inherited from FF_THIRDS_CORNER §2. For each c, over all 140 rows N=4..38, 207,527,711 short-factor trials plus 515,538,632 lift trials gave only 20 candidates reaching the `near` stage; all fail TV | X+B. Largest gcd degree 2, least remainder degree 4 (per c, in this filtered census, not a global assertion about unfiltered candidates). Earlier exhaustive code covers N≤20; the original bit-plane engine here confirms through N=31 with shared low-level arithmetic but different filtering. Beyond 31 there is only one implementation here. The independent Opus brute force reproduced intermediate counts in all 96 rows N=4..15 (including 8 near-stage survivors), checked all patterns through N=10 and replayed the full c=1 hybrid log byte-for-byte in about eight minutes. For replay: `ulimit -v 6000000; gcc -O3 -std=gnu11 scripts/z78_f3_hybrid.c -o data/z78/hyb; timeout 1800 data/z78/hyb 4 38 1` (repeat for c=2). The repeated absence of hits is not an all-level proof.

## 5. Exact residual test and scope (Round 1; made moot by §6)

**PROVED (rel. §§1–3).** At any N≥4 it suffices to take n=2N−3 or 2N−2, choose either orientation, degrees d,r satisfying 0≤r≤d≤n+Q−K, d+r+P≥K, d−r≡n mod 2 and v≡n mod 2 in [max(N−d,r−Q−1),r+2P−1]. Take monic T-unit W of degree r−v+2P−1, H with lc q and degree n−d+Q−K. List the monic T-unit divisors X of T^(b+1)W−qH of degree r. This is a nonzero polynomial: on an actual tuple it equals pXS≠0; discard an identically zero index. Calculate B=(T^K H−pX)/q, requiring an integral monic T-unit of degree n−d. Divide T^n by B to obtain quotient M and V=−remainder. Require m=M/X integral monic, V monic of degree v and g=(X+B)/(TV) a monic T-unit; test MB=T^n+V and E=Tgm w₁−1≡−u mod T^K with all T-unit conditions. Exactly the surviving tuples cover, by FUNCTIONFIELD_ES3 Lemmas 1.1 and 2.1 (minimum level K−1); exact tuples and same-side families are excluded by the earlier notes. The W enumeration may generate false indices until these last tests. In particular the two orientations have not been identified by a symmetry (swapping inverts the target unit, which is not again 1+c′T); the two c, by contrast, are equivalent by §4.

**Assessment at the Round 1 checkpoint (superseded by §6).** Fix the few W and use the sharp *second* logarithmic derivative. If A=rad-active denominator R₃(G), then A·G′/G=T^(n−1) times a polynomial of degree ≤1+P−w≤2. Classify this small numerator together with MW=T^δ SJ+κq, rather than assuming that a single congruence at the prime u vanishes. No proof of empty residual tests at all N, no decision on nonemptiness of O(3,T²), and no implication for integer ES.

## 6. A third elimination closes both orientations (PROVED relative to the reductions in §0)

Assume a covering tuple with N≥4. By the proved sign symmetry (§4) it suffices to take c=1, so **all** of p,q,u,m,H,W are monic with u=1+T. Retain the notation of §3: b=n−K, δ=N−b∈{3,4}, P=deg p, Q=deg q, κ=(q−p)/T, j=deg J, w=deg W. We use the four exact identities

    MW=T^δ SJ+κq,      MH=qT^b+J,       pXS=T^(b+1)W−qH,       T^δ SH−W=ug.

**Key identity (pure algebra).** Use pq=u, M=mX and δ+b=N:

    pMW = T^δ pS(MH−qT^b)+κu
        = T^δ mH(pXS)−T^N uS+κu
        = T^δ mH(T^(b+1)W−qH)−T^N uS+κu.

Thus

    pMW + T^δ q m H² = κu + T^N (T m H W − uS).                    (6.1)

**Degree test.** The second term on the left has degree δ+Q+z+2h=N+b+3Q−d−r ≤ N−δ+3Q+P−1 < N, using d+r+P≥K, Q=1−P and δ≥3. Its degree is at least δ≥3. Also d≤b+Q and w≤1+P by §3, so deg(pMW)=P+d+w≤b+2+P. If this too is <N, the left side must equal κu: by monicity there is no cancellation of leading terms (1+1=2≠0), and degree ≥δ contradicts deg(κu)=1. Thus equality is required in b+2+P≤N: P=1, δ=3, d=b=N−3, w=2. This kills all of A, both orientations when δ=4, and all but the extreme degree pattern of B when δ=3. Since Q=0 and d=b, H=1. The left side of (6.1) now has degree exactly N and is monic; hence

    T mW−uS=1.                                                       (6.2)

**Endpoint.** Here p=u, q=1, κ=−1, b=d, M=T^d+J. By pXS=T^(d+1)W−1 and (6.2) we have X(TmW−1)=T^(d+1)W−1, so X=TWJ+1 and r=3+j. Substituting this and uS=TmW−1 into MW=T³SJ−1 gives

    mW [ T (T³−uW) J − u ] = T³ J + u.                              (6.3)

Let Δ=T³−uW. It is nonzero since W(0)≠0. If deg Δ≥1, as J≠0 the bracket has degree 1+deg Δ+j>1. The degree of the left side is then z+2+1+deg Δ+j>3+j, the right degree. If Δ is constant, T=−1 gives Δ=−1, whence uW=T³+1=u³ and W=u². But the companion product pgJ=T^bW−κH now gives ugJ=T^dW+1, impossible modulo u when u|W. This also follows from MW=T³SJ−1 and ug=T³S−W. No endpoint survives. ∎

**Small levels (algebraic check; no census needed).** For s≤3 there is no tuple by FUNCTIONFIELD_ES3 L2.1. For s=4,5,6 the Liouville alternative of FF_THIRDS_CORNER L1.2 still applies (K≤s−1): A has L≥N, B has L≥N+1. Work at c=1 by §4 and FF_ODD_ABSENCE Cor. 1.7. For s=4 this leaves only A with n=2, d=0; then m=X=1 and v≤1, v even by parity, so the monic V=1 gives B=T²+1, contradicting T | X+B. For s=5 it leaves only A with n=3, d=0, contrary to z≡n mod 2. For s=6, n=K=4 and N=3. In A, d≤1, z even, so m=1. Mg≡−1 mod T³ cannot be equality since Mg is monic; d+y≥3, hence v=n−1−d−y≤0 and V=1. Then T⁴ divides X²+u by L3.1, impossible by degree and leading coefficient. In B we have d=0, m=X=1, ug≡1 mod T³, whence y≥2 and v≤1. Now T⁴ | u+V, impossible by monicity. These are all parameters for the low minimum levels.

**Scope of conclusion.** By FUNCTIONFIELD_ES3 Lemma 3.1 all families of a given tuple have cylinders contained in its minimum-level cylinder. Same-side families cannot cover either x*_c by FUNCTIONFIELD_ES2 §0.2. Thus the two points are in O(3,T²); by FUNCTIONFIELD_ES2 §0.1 a finite linear cover is impossible. §§4–5 are historical finite certificates and reconstruction tests; the all-level conclusion uses neither the large search nor its extrapolation. No claim here concerns all numerators over F₃ or integer ES.

## 7. Other Round 2 tests and limits

**Small differential numerator (PROVED coefficient constraints, not used by §6).** For c=1 one may avoid factoring the active radical. Put C=mA₀uV, G=mA₀²/(uV) as in §3, and let L₀=T^(1−n) C·G′/G. It is a nonzero polynomial: C clears the simple finite poles, and the order-n contact gives the requisite zero. The requested numerator with the active denominator is L₀/(C/R₃(G)), a polynomial. Write ℓ=1+P−w∈{0,1,2}. Then deg L₀≤ℓ. Its constant coefficient is nκ/W(0); its coefficient of T^ℓ is z+2(L+Q)−1−v (as an element of F₃), by the logarithmic derivative at infinity and lc C=1. For ℓ=0 these must coincide and be nonzero. For ℓ=1 this determines both coefficients. Only B with W=1 has ℓ=2; there is one middle coefficient, forced by the formula

    L₀ ≡ (κu²/W) [ n−T(p′/p−W′/W+X′/X) ]    mod T^(ℓ+1).

Indeed differentiating G+1=T^n D/(uV) gives L₀=(uV/A₀)[nD+TD′−TD(uV)′/(uV)]. Here D≡−u mod T^(2K−n), 2K−n≥4, uV/A₀≡−pM mod T^K, V≡−pMX/q mod T^K and M≡κq/W mod T^δ. Differentiating a congruence and then multiplying by T loses no precision. For example, in the sole quadratic case κ=−1, p=u, W=1, the linear coefficient is 1+X′(0)/X(0)−2n. The high-coefficient and low-coefficient rules are simultaneous, not a claim that every formal candidate occurs. By §6 none is realised by a covering tuple. The all-level proof need not classify the individual prime factors in C/R₃(G).

**Frobenius (PROVED, including the near-miss successor).** Cubing mXB=T^n+V preserves it with exponent 3n. Cubing the sum gives X³+B³=T³g³V³, which no longer has simple T-valuation: with the cubed T-units one would need g_new=T²g³. Likewise u³−u=c(T³−T) has valuation 1; replacing cubed u by u in the cubed covering congruence changes a unit-side term already mod T². In the determinant equation W³ is not among bounded-degree W unless W=1 (or one only asks for a higher degree outside the list). Hence direct Frobenius or adjustment by powers of T preserving the T-units is not a descent. The *near-miss* of §4 at k has a successor at 3k, N′=3N−3: M,B,V cube but m stays 1+T and X_new=u²X³. Both fail TV|X+B. EVIDENCE: N=9 and N′=24 occur in the B log. No uniform fixed finite set of primes supporting the unknowns has been established, so a theorem for a fixed S-unit group does not by itself turn these varying instances into Frobenius orbits.

**Counting (PROVED relative to §6).** At either designated point the deterministic number of actual covering tuples per level is zero, so the tail count from N=39 is exactly zero. The 20 final-test near-misses per sign are not 20 independent trials: the B family alone contributes at N=9,12,…,36. Calibrating a nonzero probability of a hit on these correlated survivors, or extrapolating the empirical number 20 to a tail expectation, has no justification. No covering search beyond N=38 was run; the emptiness at every level follows algebraically, not by extrapolation.

**General polynomial slice: what transfers (PROVED, conditional identities).** Suppose u(0)=1 and u′(0)≠0 and use (p,q)=(1,u) or (u,1), pq=u. The tuple identities, equivalence of covering with T^K | pX+qB (K≤s−1), and T^K | pMX+qV (K≤n) are unchanged. Lemma 1.2 allows exact pX+qB=0 for other u; indeed for some quadratic u there are such tuples (FF_THIRDS_CORNER Prop. 1.4). On the non-exact branch the quotient reconstruction from §1 is valid under its *degree* hypotheses L>r, L+Q>P+r: X is the high-digit triangular solution and B determines M by long division. Do not impose the special affine-point upper/lower bounds on d,y,v in general. The definitions of H,J,S,W and the identities MH, VS, MW, VW, pXS, pgJ, (6.1) hold whenever K≤n, b=n−K, δ=N−b and the covering congruences hold, using the polynomial κ=(q−p)/T; these algebraic identities do not require a derivative. Nonvanishing, monicity and the degree bound on W do not automatically follow. The first separable logarithmic bound generalises to deg R₃(pMX/(qV))≥K when the derivative is nonzero. The square identity mA₀²+uV=T^nD still holds in characteristic 3; n≤deg R₃(G) again requires G′≠0. The proofs excluding cubes and forcing tiny excess used deg u=1. The L₀ expansion above assumes constant κ: for varying κ, V′/V includes an extra +κ′/κ inside the logarithmic-derivative sum subtracted from n, and the available precision must be checked anew.

**Integer analogy (Assessment).** In integer settings the quotient identities, with their actual divisibilities retained, can be rewritten algebraically; no analogous control of leading coefficients, lack of carries, separability, or ABC follows. Even the square simplification 4=1 is special to characteristic 3.

**Measure (Assessment).** The fixed-height obstruction does not bound the number of tuples covering *some* slice point: u varies with the cylinder; its depth-K truncation may have degree K−1, and the exact alternatives need not be excluded. One cannot insert the affine-point count zero into a union bound over the whole slice, assert positive uncovered measure, or invoke Baire to exclude a cover by clopens. No such estimate is needed for nonemptiness, since §6 gives two explicit points.

**Priority check (Assessment; bounded, not a priority claim).** The repo's `Z58_LIT.md` §Q1 and `LITERATURE_2026_UPDATE.md` found no matching function-field ES paper. A fresh Crossref bibliographic query “Erdős Straus conjecture finite fields unit fractions polynomial rings linear covering” (15 returns, `data/z78/f3_priority_crossref.json`) gave no match to this pointwise statement. The related paper *On covering systems of polynomial rings over finite fields*, DOI 10.1090/proc/16864, concerns covering systems, not the specified ES-family validity conditions. This check does not exclude differently indexed prior work. Orchestrator export: update live open-target quotes (STATUS §2; FRONTIER passages at lines 1261,1336,2429 of the pre-wave version); preserve historical WAVES entries.

## Sources

- `FUNCTIONFIELD_ES2.md` §0: compactness, same-side exclusion, Conjecture 0.2.
- `FUNCTIONFIELD_ES3.md` L1.1, L2.1, L2.2, L3.1: validity, tuple normal form, nonzero CRT errors and minimum-level cylinders.
- `FF_THIRDS_CORNER.md` L1.1–1.2, P2.1, L3.1, C3.2: covering congruences, exact-case exclusions and earlier exhaustive search.
- `FF_ODD_ABSENCE.md` C1.7: pattern parity; `notes/z77/F3_TARGET.md`: previous A-side window.
- Mason–Stothers polynomial ABC in the separable case; §2 also gives the elementary logarithmic-derivative form used at both contacts.
