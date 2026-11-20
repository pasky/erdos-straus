Result: At r=17, x=5, P hits require a fourth-root shift bound, and only finitely many levels can hit in each fixed square class of de (P) or d (Q). Label: PROVED (rel. SE §3.1 and the p-adic Subspace Theorem; (2.3) elementary)
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

Indeed M(paS+qH)=(UJ−qv)S+q(qB+J)=USJ+DqB. For vY, use vS=pB+J and U H=pa+qb. For the third, U SH−Y=S(UH−pa)−qH=q(bS−H); bS−H=pBg by Mb=UB+v. With Z=Y/B the companion is **pgJ=B Z−D H**: indeed Y−DH=paS+pH=p(aS+H); gv=a+b and vS=pB+J give gJ=(a+b)S−pBg=aS+H since bS−H=pBg. Similarly the third identity in unscaled form is U SH−Y=uBg. For P, Z=(rSJ+Dq)/M is integral because gcd(B,M)=1, and the numerator is 0 modulo M (multiply by B). Thus the determinant W of the F₃ note ports to Z=(paS+qH)/B>0. For Q one should retain Y, or allow the rational Z=Y/e. Repeating the proof of (6.1) without division gives

    pMY + U q m H² = DuB + UB (m H Y/B −u S) = DuB + U(mHY−uBS).

Proof: pMY=pU S(MH−qB)+DuB; substitute M=m a and paS=Y−qH. In P divide by B: **pMZ + r q m H² = D u + U(m H Z−uS)**. In Q: **pMY + F q m H² = D u e + F(m H Y−ueS)**. In particular reducing the Q equation mod F only recovers pMY≡Due. The clearing factor e cannot be replaced by an r-power. All the identities are equalities over ℤ; none uses abc.

## 2. Two positive P gaps force a fourth-root shift (PROVED)

Here x=5, (p,q)=(1,5) or (5,1), r=17 (also any prime r≥17 distinct from 5; the covering interpretation requires the given nonsquare cell). U=r^L, B=U/r. Set A=ma² and C=6. The bounds below apply for U≥10⁶, amply below the start of the unexplored depth range at 17. We retain deliberately loose constants. The primary inequalities are

    mab≤2N,     H≤2CB/M,     A≥(2/5)U/p,     M≥4Cq,
    e≤2p(2C+|D|)a,       e≤4C² N/A+D².                              (2.1)

Indeed e≤2b and M≥4 give b≤N/(M−2)≤2N/M. With k=1+a/b≤2 we have e=Nk/(Mc−k), and Mc≥(U−|D|)/p by S≥1. Hence qe/U ≤ 2uU/[r(U−|D|−2p)]<3/5. Since J≥1, pA≥(2/5)U and M²=mA≥(8/5)U/p, giving the first line. Next eZ=rHJ−Dpa, Z≥1, so e≤p(2C+|D|)a+(2Cq/M)e. Finally e divides D²+rmH² by reduction of (pa+qb)²=(UH)² modulo e, where b≡−a and mab≡N: multiply by rm and cancel the r-unit. More explicitly mU²H²≡mD²a²≡−ND² mod e since ma²≡−N mod e; cancel N since gcd(e,r)=1. This is M17D Remark 2.4 with our signs. Its positive cofactor gives the last bound.

**Third gap.** The integer I=mHZ−uS is positive by (6.1)'s P port: pMZ+rq mH²>Du for r≥17. Set C₁=p²(2C+|D|), C₂=4q C²/r, C₃=2uC+|D|u. Using eZ≤p(2C+|D|)a+(2Cq/M)e as just proved yields

    1 ≤ I ≤ C₁ A/(Ue) + C₂ U/A + C₃/U.                               (2.2)

Thus either A≤4 C₂ U or e≤2 C₁ A/U. In the former case (2.1) gives e≤2p(2C+|D|)√(C₂ U) since m≥4. In the latter, if e≥2D² then e≤8C² N/A and hence e²≤16 C₁ C² N/U. Otherwise e<32. In particular, uniformly in depth for 17,

    e ≤ 1100 √U  = 1100 (rN)^(1/4).                                   (2.3)

The same constant works for every r≥17 (use p≤5,q≤5,C₂≤720/17). This is an unconditional exclusion of *large* shifts, not of all small shifts. The residual bands (2.1)–(2.2) are stronger than the fourth-root summary. There is no degree rule bounding positive integer Z by a numeral independent of U: eZ≤p(2C+|D|)a+(2Cq/M)e gives an upper bound involving a/e, not an absolute ceiling. Unlike F₃[T], positivity yields a carry I≥1, not a monic top coefficient. In particular, (2.2) permits A on the scale U and e on the scale a. It does not compel the single FF endpoint.

## 3. Q contacts and an unconditional square-class finiteness theorem

**PROVED, size inequalities.** For a Q hit put f=mac−F and f*=mbc−F. Then ef=ma²+1, bf=Fa+c, ff*=F²+mc². Thus 0<f≤F+2 since a≤b, c≤a+b≤2b; mac=F+f≤2F+2. We have b≥F/C and ma≤C(e+1/F). Hence

    F≤pma²+q,     m(F−q)≤p C²(e+1/F)².                               (3.1)

In particular Q has no small-e hits in the entire range below that last explicit square-root threshold (e.g. e≥√(dF)/10 for x=5, F≥100, weakening (3.1)). Modulo F, p f+q f*≡0. Squaring and subtracting 4u f f* gives the stronger contact modulo F²:

    F | p f²+qmc²,                  F² | (pf−q f*)²+4umc².             (3.2)

For the first congruence multiply p f+q f* by f. Both identities hold even if c is not an r-unit, but in the use below c is an r-unit.

**Lemma (PROVED relative to the p-adic Subspace Theorem of Schlickewei, two variables).** Fix nonzero α algebraic in Q_r but not rational. Suppose U=r^L, integers x,y are nonzero, r∤y, |x|,|y|≤U^B for fixed B, and |x−α y|_r≤U^(−k) with fixed k>0. Then for any η>0 there are no such pairs at sufficiently large L with |xy|≤U^(k−η). No effective L is asserted. Indeed use linear forms X,Y at infinity and X−αY,Y at r. The unnormalised product is ≤U^(−η)≤max(|x|,|y|)^(−η/B). Nonprimitive inputs may be divided by their gcd (an r-unit), which only improves this inequality. The Subspace Theorem puts the resulting primitive vectors, apart from bounded ones, on finitely many rational lines. On any such line x/y is constant rational and |y|_r=1, impossible as L→∞. A congruence x²≡βy² mod U^k for a fixed negative rational β that is an r-unit gives the hypothesis for one of the two fixed roots in Q_r (or no solutions), since r is odd and the roots modulo r are distinct. Finitely many choices of β or root cause no difficulty.

**Theorem (PROVED relative to the lemma).** At x=5, r=17, any infinite sequence of P hits of increasing level has the squarefree kernel of de tending to infinity. For Q hits the squarefree kernel of d alone tends to infinity. Here 'kernel' means the squarefree representative modulo rational squares, *not* rad. The statements also hold for any fixed prime r≥17 with 5 a nonsquare mod r on this line.

*P.* In a bounded kernel subsequence, gcd(d,e)=1 gives d=d₀ h², e=e₀ l² with d₀,e₀ fixed after passing to a further subsequence. Put t=pa−qb. Squaring the cover and using mab=N+e gives m t²+4ue=N(rmH²−4u). Thus (ht)²≡−(u e₀/d₀)l² mod N, with denominator l an r-unit. The case t=0 is impossible since pa+qb≡0 mod r and r∤2pqa. Meanwhile

    |ht|l ≤ C h b l ≤ 2C N √e/(a√m),

since b≤2N/(ma), h≤√m/2, l≤√e. By A≥(2/5)U/p and (2.3), the right side is O(N U^(−1/4))=O_r(N^(7/8)). Apply the lemma with modulus N, k=1. All coordinates have polynomial height. This contradicts bounded kernel along arbitrarily high hits.

*Q.* On a fixed square class write d=d₀ h², put x=2ha, y=2hc. They are r-units; d₀xy=mac≤2F+2. First p d₀x²≡−q mod F by (3.1)'s defining J. With denominator 1 the lemma forces x>F^0.9 eventually, hence y=O(F^0.1). Next (3.2) gives f²≡−(q d₀/p)y² mod F, so f y>F^0.9 eventually, i.e. f≫F^0.8. Since f f*=F²+d₀ y² we obtain f*=O(F^1.2). Finally (pf−qf*)²≡−4u d₀y² mod F². Its numerator is nonzero by reduction mod r (f, f* are r-units and p f+q f*≡0); the product of the absolute numerator with y is O(F^1.3), impossible by the lemma with k=2. All three algebraic targets are fixed nonrational roots. This is a use of three different contacts with *the same fixed square class*, not of a moving-target Roth theorem. ∎

**Local qualification for Q (PROVED).** If the source convention allows r|c, note f≡mac mod F could then fail to be a unit. In fact in a nonsquare cell r∤c: r|c gives a+b≡0, so −a/b≡1. The same applies to P; (3.1)–(3.2) themselves do not need this observation.

## 4. What abc would buy (CONDITIONAL, explicit constants)

Assume ABC(ε,Kε): for each primitive positive triple A₁+B₁=C₁ one has C₁≤Kε rad(A₁B₁C₁)^(1+ε), with specified ε>0 and Kε≥1 independent of the triple. Put λ=ε/(1+ε). This is not the false ε=0 inequality with a universal constant. For the first contact in P set A₁:B₁:C₁=pma²:qe:UJ reduced by G₁=gcd(pma²,qe)≤pq (gcd(ma,e)=1). Taking radicals before cancellation and using rad(J)≤J gives

    U ≤ pq Kε r p q m a e (UJ)^λ.

Indeed in general for raw total T=U h, primitive gcd G and a radical bound R₀h, ABC yields U≤G Kε^(1−λ) R₀ (T/G)^λ. The second contact is more useful: with t=pa−qb≠0, m t²+4ue=N D₂, D₂=rmH²−4u>0. The gcd G≤4u C², since gcd(m,e)=1 and gcd(t,e)|C from a+b≡0 mod e. Now R₀≤4ur m |t|e, |t|≤Cb, M b≤2N, b≤N/2, e≤N. Hence m t²+4ue≤(C²+4u)N². Applying ABC gives

    a ≤ C₀ e N^(2λ),      C₀=32 u² C³ r Kε (C²+4u)^λ.

Combine with A≥(2/5)U/p: **d e²≥√r N^(1/2−4λ)/(10p C₀²)**. For every θ<1/4 the full abc conjecture therefore rules out P hits with de≤N^θ once U≥10⁶ and N^(1/2−4λ−2θ)>10p C₀²/√r, choosing ε so that the exponent is positive. Together with (3.1) this excludes low de on both sides (use F rather than N for Q). No uniform cutoff for unrestricted de follows, even with those constants. The leftover factor N^(2λ), and the archimedean constants multiplying e, prevent the FF subtraction of exact degrees. This is a restricted conditional result; not a conditional proof of all-depth sterility.

## 5. Reconstruction, controls and scope

**Reconstruction (PROVED).** With H,a given, b=(UH−pa)/q. For P, d obeys N/(4ab)<d≤(N+a+b)/(4ab), interval length ≤1/2. For Q, enumerate positive divisors e of a+b with 4ab | Fe+1 and recover d. Given M alone, c≡−D/(pM) modulo U on P (pM an r-unit); unlike the FF residue polynomial, c is not the unique truncation unless c≤U is separately shown. The exact size is (a+b)/e. In the other direction b gives M=(N+e)/b and M−N/b=e/b≤2/c on P; if c=1,2 this need not be the ordinary quotient of N by b. Symbolic high-digit triangular reconstruction of a polynomial factor is thus not a verbatim integer uniqueness theorem. Lane 2 §6 already gives the successful finite P reconstruction from H a,H d,J.

**Failure at 13 (PROVED, different domain).** The previously refuted point has x₁₁=x₁₃=2, not x₁₁=1: it is not on the single-13 generic line. POINTWISE_MORDELL13B Thm 3.1 gives residue 12650497 at modulus 12670944 (II3). The 11-component 2 is necessary for that witness; one cannot substitute N=13^K in the two-prime problem. Even on the single-13 line every nonsquare cell is covered at level 1 (SIBLING §2.4). For x=2 specifically, Q has (a,b,c,d,e)=(2,9,1,2,11): 4abd=144=13e+1, and 2a+b=13, giving the inverse orientation. This is distinct from the refuted two-prime point. Nothing in (2.3), an eventual upper bound, or in the Subspace Theorem, a finiteness result per square class, would prohibit a finite-level hit.

**Numerical controls (EVIDENCE).** `scripts/z78_endpoint_checks.py`, log `data/z78/r17_endpoint_check.txt`: all identities and pre-rounding inequalities checked with exact integers/Fractions on 100101 P and 2206 Q hit instances (including synthesized positive endpoints on genuine tuples, with repetitions). In 2184 Q controls e∤Y. Input P lists through depth 8 at 17; separate small brute at r=13,17. Lane 2's exact depth-11 data are six *empty hit* summaries (not 130 million stored covering tuples): tested all six logs for the matching endpoint, index and zero count; no x=5 hit exists there on which to validate (2.3) nonvacuously. The first and Z gap antecedents fired on 1699 and 21 synthetic P controls respectively, but the rounded combined small-constant regime did not occur. This is an implementation sanity check, not the proof. For replay: `ulimit -v 6000000; timeout 600 uv run --offline --no-project python -B scripts/z78_endpoint_checks.py --lane ../erdos-straus-claude-agent-worktree-0041` (omit --lane for stand-alone use). The original depth certificates are M17D Comp. 3.4 and `R17_PUSH.md` §6; we did not independently re-enumerate depth 11.

**Assessment (residual).** The free square class is the obstacle to a uniform application of the Subspace Theorem: its linear forms have to be fixed. In P the unclassified hits at depth ≥12 have variable de, e≤1100(rN)^(1/4), the two bands of (2.2), and the shifted divisor condition MH=qB+J, eS=pB+J. In Q the old search excludes k≤15, so only odd k≥17 are open; (3.1)–(3.2) apply. The fixed-class result does not say a fixed class cannot have a first hit past those finite cutoffs. No improvement to the uniform threshold for sterile points is claimed. Next target: uniform control of the simultaneous Q contacts (3.2) with d₀xy≤2F+2.
