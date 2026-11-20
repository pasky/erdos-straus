Result: Both orientations admit a complete search using the quotient of the covering congruence and the shorter of two factors, with cost poly(N)·3^(2N/3) per level. Label: PROVED (rel. FF_THIRDS_CORNER Lemma 1.2 and Corollary 3.2)
Scope: Case B families at the two specified points for F₃[T], A=T², minimum level N≥4; no all-level conclusion about sterility, finite covering, or integer ES.
Review: none
Triage: DATA
STATUS delta: none

## 1. Two-sided reconstruction (PROVED relative to the indicated tuple lemmas)

Use n=s−2 ∈ {2N−3,2N−2}, K=N+1, u=1+cT. Write X for the short side, B for the long side of (w₁,C₁); write m=m', g=g', V=v₁. In orientation A set (X,B,p,q)=(w₁,C₁,1,u); in orientation B set (X,B,p,q)=(C₁,w₁,u,1). The old Liouville exclusion gives exactly these two disjoint possibilities. Put r=deg X, z=deg m, d=z+r, L=n−d=deg B; L>r+1 in these windows. All four of X,B,m,g are monic T-units. The two identities are mXB=T^n+V and X+B=TgV; thus V is monic, a T-unit, of degree L−1−deg g. Covering is precisely

    pX+qB=T^K H,

by the R3 identity (FF_THIRDS_CORNER Lemma 1.1), since K≤s−1. H≠0 by the exact-tuple exclusion, and has degree h=L+deg q−K with leading coefficient lc q. In particular d≤n+deg q−K.

**Short-side bound in B as well as A.** In A, Mg≡−c mod T^N, M=mX: this is not equality (the exceptional M=g=1 is excluded by FUNCTIONFIELD_ES3 Lemma 2.2). In B, uMg≡c mod T^N and equality is impossible by degree. Thus d+deg g≥N in A, ≥N−1 in B. Consequently deg V≤n−1−N in A, ≤n−N in B. By FF_THIRDS_CORNER Corollary 3.2 the polynomials pMX+qV and its counterpart for the other side cannot vanish identically; T^K divides pMX+qV. Since deg(qV)<K, we have d+r+deg p≥K: **d+r≥N in B**, ≥N+1 in A. This is for both y=deg g regimes; for y≥N the existing extra restriction d+deg V≤s−N−3 remains.

**Reconstruction theorem.** Enumerate H at the prescribed degree and leading coefficient, and only the smaller-degree one of X,m. Given X, test divisibility by q and form B=(T^K H−pX)/q; M is then the polynomial quotient of T^n by B since deg V<L. Test X|M. Conversely given m one can reconstruct X uniquely from the top r+1 coefficients (degrees n down to n−r) of mX(T^K H−pX)=q(T^n+V), aligning both sides at degree n+deg q. More explicitly, start at degree r and descend to degree 0: the coefficient x_i first enters the linear term at degree z+K+h+i, and its effect there is lc H; in the quadratic term its effect has degree ≤z+deg p+r+i<z+K+h+i. At these degrees the V term is absent since n−r=L+z≥L. This triangular system recovers X. In either route, verify the original identities, all degrees, monicity, units and covering. No random or independence assumption enters. The number of trials up to polynomial factors is 3^(h+min(z,r)). Here h≤N−d, and max(z,r)=d−min(z,r)≥max(d/2,N−d)≥N/3. This gives the exponent in §0. These are quotient/factor trials, not distinct M's.
