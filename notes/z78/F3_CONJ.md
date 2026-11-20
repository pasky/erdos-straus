Result: The whole high-deg g' branch is impossible in either orientation, and in the low branch deg rad(uMV)≥N+1. Label: PROVED (rel. Mason–Stothers and the tuple lemmas in §1)
Scope: Case B families at the two specified points for F₃[T], A=T², minimum level N≥4; no all-level conclusion about sterility, finite covering, or integer ES.
Review: none
Triage: DATA
STATUS delta: none

## 1. Two-sided reconstruction (PROVED relative to the indicated tuple lemmas)

Use n=s−2 ∈ {2N−3,2N−2}, K=N+1, u=1+cT. Write X for the short side, B for the long side of (w₁,C₁); write m=m', g=g', V=v₁. In orientation A set (X,B,p,q)=(w₁,C₁,1,u); in orientation B set (X,B,p,q)=(C₁,w₁,u,1). The old Liouville exclusion gives exactly these two disjoint possibilities. Put r=deg X, z=deg m, d=z+r, L=n−d=deg B; L>r+1 in these windows. All four of X,B,m,g are monic T-units. The two identities are mXB=T^n+V and X+B=TgV; thus V is monic, a T-unit, of degree L−1−deg g. Covering is precisely

    pX+qB=T^K H,

by the R3 identity (FF_THIRDS_CORNER Lemma 1.1), since K≤s−1. H≠0 by the exact-tuple exclusion, and has degree h=L+deg q−K with leading coefficient lc q. In particular d≤n+deg q−K.

**Short-side bound in B as well as A.** In A, Mg≡−c mod T^N, M=mX: this is not equality (the exceptional M=g=1 is excluded by FUNCTIONFIELD_ES3 Lemma 2.2). In B, uMg≡c mod T^N and equality is impossible by degree. Thus d+deg g≥N in A, ≥N−1 in B. Consequently deg V≤n−1−N in A, ≤n−N in B. By FF_THIRDS_CORNER Corollary 3.2 the polynomials pMX+qV and its counterpart for the other side cannot vanish identically; T^K divides pMX+qV. Since deg(qV)<K, we have d+r+deg p≥K: **d+r≥N in B**, ≥N+1 in A. This is for both y=deg g regimes; for y≥N the existing extra restriction d+deg V≤s−N−3 remains.

**Reconstruction theorem.** Enumerate H at the prescribed degree and leading coefficient, and only the smaller-degree one of X,m. Given X, test divisibility by q and form B=(T^K H−pX)/q; M is then the polynomial quotient of T^n by B since deg V<L. Test X|M. Conversely given m one can reconstruct X uniquely from the top r+1 coefficients (degrees n+deg q down to n+deg q−r) of mX(T^K H−pX)=q(T^n+V), aligning both sides at degree n+deg q. More explicitly, start at degree r and descend to degree 0: the coefficient x_i first enters the linear term at degree z+K+h+i, and its effect there is lc H; in the quadratic term its effect has degree ≤z+deg p+r+i<z+K+h+i. At these degrees the V term is absent since n−r=L+z≥L. This triangular system recovers X. In either route, verify the original identities, all degrees, monicity, units and covering. No random or independence assumption enters. The number of trials up to polynomial factors is 3^(h+min(z,r)). Here h≤N−d, and max(z,r)=d−min(z,r)≥max(d/2,N−d)≥N/3. This gives the exponent in §0. These are quotient/factor trials, not distinct M's.

## 2. Moving ABC to the covering congruence (PROVED)

**Theorem.** With K=N+1 and v=deg V, put F=pMX/(qV). Then F′≠0 and K≤deg rad(uMV)≤1+d+v. In particular y=deg g=L−1−v≤n−1−N, strictly below N in either orientation.

*Separable proof.* T^K divides pMX+qV (Lemma 3.1); the denominators are T-units. The sum is nonzero by Corollary 3.2. Divide both summands by their gcd D, retaining divisibility of the sum by T^K. Mason–Stothers bounds the degree of the coprime sum by the sum of the radical degrees of the two summands plus the degree of its radical minus one. The latter radical has degree ≤deg(sum)−K+1. Since rad(pqMXV)=rad(uMV), cancellation proves the claim. This is the Wronskian form of ABC; it uses only a simple zero of u, not a presumed bound on rad(E_M).

*Inseparable proof.* Write n=s−2. Both orientations give V | T^n+MX (because MX+B M=TgMV and MB=T^n+V). Also gcd(MX,V)=1 since MX is supported on M and MB=T^n+V with T∤M. Work over the perfect field F₃. If F′=0, the multiplicity at each prime of F is a multiple of three, so (away from u) V and MX are separately cubes up to units. Let U=T+c be the monic associate of u. Write MX=U^i A³ and V=U^j D³ (monic polynomials), 0≤i,j≤2. By coprimality and ord_U(F)≡0 mod 3 exactly one of i,j is nonzero.

If j>0, put f=T^n+V. Then TU f′−jT f=T^n(nU−jT), whose last linear factor is nonzero (U(0)≠0, j≠0 in F₃). As T∤f, deg gcd(f,f′)≤1. But M|f and MX=A³ with X|M mean every prime dividing M occurs at least twice in M. Hence M has degree at most 2: there is at most one repeated prime of f, linear and of multiplicity exactly 2 (multiplicity ≥3 contributes at least 2 to the gcd). If i>0 and 3∤n, then V=D³ and f is squarefree (f′=nT^(n−1)), so MX has multiplicities at most 2 and hence M is supported on U alone with d≤1. Neither d≤2 alternative fits §1 for N≥5 (d+r+deg p≥K, r≤d); at N=4 the only marginal alternative would be B with d=2, excluded by d≤n−K≤1. In A even d=2 is too small at N=4.

Finally if i>0 and 3|n, V=D³ divides T^n+MX, whose derivative iU^(i−1)A³ is prime to V. Thus V=1. The parity law z≡v≡s mod 2 (FF_ODD_ABSENCE Cor. 1.7) forces n even. But U|M|T^n+1 contradicts (−c)^n+1=2. This proves separability without descending to a nonexistent smaller covering tuple. ∎

**Active-prime sharpening (PROVED).** Let R₃(F) be the product of monic primes whose signed multiplicity in F is nonzero mod 3. The nonzero differential coefficient F′/F has only simple finite poles, all on R₃(F), and tends to zero at infinity. Thus the numerator over R₃(F) is nonzero of degree at most deg R₃(F)−1. It is divisible by T^(K−1) because F≡−1 mod T^K. Hence **deg R₃(F)≥K**. In particular neither MX nor V can be a cube: otherwise deg R₃(F)≤1+v or ≤1+d respectively, both <K. This excludes the Frobenius branch of the original ABC equation too, including when 3|n. If 3 divides deg(pMX)−deg(qV), the logarithmic derivative is O(T⁻²) at infinity, raising K to K+1.

## 3. Elimination of the two large powers (PROVED)

Write b=n−K and δ=N−b∈{3,4} (these symbols are local to this section), P=deg p, Q=deg q, κ=(q−p)/T∈{c,−c}. Define two nonzero polynomials

    T^K J = pMX+qV,                 T^N S = pMg+κ.

The first is integral and nonzero by §1; the second is the original short-side covering congruence, using uMg≡c for B. Nonvanishing of the second was checked in §1. We have j=deg J=d+r+P−K and deg S=b+P−v (by y=L−1−v). Direct substitution and X+B=TgV give

    MH=qT^b+J,                     VS=pT^b+J.

Hence modulo M, J≡−qT^b and T^N S≡κ; define W=(T^δ SJ+κq)/M, an integral nonzero T-unit (the numerator has constant κ). Multiplication by V and use of the preceding identities give

    VW=T^δ HJ−κpX,                 pXS=T^(b+1)W−qH.

For the first, subtract the two expressions after multiplying by M and use MH−VS=κT^(b+1), T^K J=pMX+qV. For the second eliminate qVW between q(VW) and (T^K J−pMX)W: (T^K W−qT^δ H)J=pX(MW−κq)=pXT^δ SJ. Cancel T^δ J. Since δ>deg q, the first defining expression for W has degree δ+deg S+j−d, i.e.

    deg W = r−v+2P−1 ≥ 0.

In particular **N−d≤v≤r−1 (A), N−d≤v≤r+1 (B)**. Also rad(uMV)≥K as above, not merely a bound on its total degree. This bound does not use a probabilistic model. The last product gives an alternative exact enumeration: for fixed H,W, each X divides T^(b+1)W−qH, after which §1 recovers everything. This is not the old forced-E_M lottery: the small degree of W is a consequence of two independent congruences modulo M. In fact MW=T^δ SJ+κq and MH=qT^b+J give T^δ SH−W=pqg after multiplication by M. Eliminating M from the same pair gives the companion product **pgJ=T^b W−κH**.

**Upper search exponent 2/5 (PROVED; algorithmic, not the engine used in the census).** At a fixed degree pattern use the cheapest of four indices: (i) V, factoring T^n+V for M and X; (ii) J, factoring qT^b+J for M and pT^b+J for V, then pMX=T^K J−qV; (iii) H and the shorter of m,X as in §1; (iv) H,W as just proved. Both polynomials in route (ii) are nonzero by the identities MH and VS. Deterministic Berlekamp factorisation over the fixed base field costs poly(N); a degree-O(N) polynomial has 3^o(N) divisors uniformly (split at prime degree (log₃ N)/2: O(√N) low primes with ≤O(N) choices each, and O(N/log N) high prime factors with multiplicity). Each factor list produces only subexponential overhead, including choosing X|M. From h≤N−d, w≤r−v+1 and j≤d+r−N, the four base-3 exponents are at most v, d+r−N, N−r (using z=d−r), N−d+r−v+1. If their minimum is e, adding the second and fourth gives 2e≤2r−v+1; using v≥e and r≤N−e gives 5e≤2N+1. Thus complete search costs 3^(2N/5+o(N)). No decay of the number of hits follows from this running-time bound.
