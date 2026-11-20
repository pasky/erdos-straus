Result: The integer P determinant and the denominator-cleared Q determinant satisfy exact third-elimination identities, but Q has a moving denominator and a positive endpoint gives no monic degree gap. Label: PROVED (rel. SE §3.1; elementary identities below)
Scope: Positive rational endpoints on the single-r generic line, chiefly x=5 at r=17, in nonsquare cells. No all-depth sterility result or conclusion on integer ES.
Review: none
Triage: BARRIER-SCOPED
STATUS delta: none

## 1. The exact identity, in both boxes (PROVED)

Use `notes/z77/R17_F3.md` §2 / `STERILE_EXPLICIT.md` §3.1 for the reduction of the seven ET families to P and Q. Take a≤b, m=4d, M=ma, r∤abcde. For x=s/t>0 in lowest terms with r∤st use (p,q)=(t,s) or (s,t) so that the oriented hit is exactly U | pa+qb. Put D=q−p, u=pq, C=p+q. The first congruence uses −a/b; the swapped coefficients account for −b/a. Do not identify the two orientations unless justified.

**Unified calculation.** Write Mb=UB+v, a+b=gv; for P use U=r^L, N=r^(2L−1)=U²/r, B=U/r, v=e, g=c. For Q use U=F=r^k, B=e, v=1, g=ce. In particular the Q replacement for N is eF, *not F itself*. Define

    H=(pa+qb)/U,     J=(pMa+qv)/U,     S=(pMg+D)/U.

For a hit, all three are positive integers: MH=qB+J, and v(pMg+D)=pM(a+b)+Dv=U(J+pB), with v a unit at r. The numerator of S is positive since M≥4, g≥1. The FF correction κ becomes D, not D/r: the integer sum is gv, not r times a unit times v. Set Y=(U SJ+DqB)/M. Then Y is integral since J≡−qB and US≡D mod M. The following are exact:

    Y=paS+qH,       vY=UHJ−DpBa,       U SH−Y=uBg,
    p g J=Y−D H.

Indeed M(paS+qH)=(UJ−qv)S+q(qB+J)=USJ+DqB. For vY, use vS=pB+J and U H=pa+qb. For the third, U SH−Y=S(UH−pa)−qH=q(bS−H); bS−H=pBg by Mb=UB+v. With Z=Y/B the companion is **pgJ=B Z−D H**: indeed Y−DH=paS+pH=p(aS+H); gv=a+b and vS=pB+J give gJ=(a+b)S−pBg=aS+H since bS−H=pBg. Similarly the third identity in unscaled form is U SH−Y=uBg. For P, Z=(rSJ+Dq)/M is integral because gcd(B,M)=1, and the numerator is 0 modulo M (multiply by B). Thus the determinant W of the F₃ note ports to Z. For Q one should retain Y, or allow the rational Z=Y/e. Repeating the proof of (6.1) without division gives

    pMY + U q m H² = DuB + UB (m H Y/B −u S) = DuB + U(mHY−uBS).

Proof: pMY=pU S(MH−qB)+DuB; substitute M=m a and paS=Y−qH. In P divide by B: **pMZ + r q m H² = D u + U(m H Z−uS)**. In Q: **pMY + F q m H² = D u e + F(m H Y−ueS)**. In particular reducing the Q equation mod F only recovers pMY≡Due. The clearing factor e cannot be replaced by an r-power. All the identities are equalities over ℤ; none uses abc.
