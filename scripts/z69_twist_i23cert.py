# z69 TWIST I23: rigorous truncation certificate for "p has no twisted lift".
# A lift of n is w = g/h (lowest terms, h >= 1) with m = p h^2 - g^2 != 0, m | n (w = 0 iff p | n).  Call it LARGE if h > H.
# For a large lift, with sigma = sign(w):  | w - sigma*sqrt(p) | = |m| / (h^2 (|w| + sqrt p)) < n / (H^2 sqrt p).
# Twist equation: sum_i w_i/n_i = 0.
#  (a) three large lifts  =>  | sum sigma_i/n_i | < 3/(H^2 p).            Excluded if mu1 := min_signs |sum sigma_i/n_i| >= 3/(H^2 p).
#  (b) exactly one small lift w_i (finite list)  =>  | w_i/n_i + sqrt(p)(sigma_j/n_j + sigma_k/n_k) | < 2/(H^2 sqrt p).
#      Excluded if mu2 := min over the finite list and signs of that quantity is >= 2/(H^2 sqrt p)
#      (tested EXACTLY in rational arithmetic; the printed margins use 60-digit decimals and are informational).
#  (c) at least two small lifts: finite search (two small lifts enumerated, the third w forced and tested exactly).
# If (a),(b) are excluded and (c) finds nothing for every ES triple of p, then p has NO twisted lift (PROVED for that p).
import sys, math
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
sys.path.insert(0,'scripts')
from z69_twist_i23 import es_triples, lifts, valid
getcontext().prec=60
def cert(p,H):
    sp=Decimal(p).sqrt(); T=es_triples(p); ok=True; nhits=0; worst1=None; worst2=None
    for ns in T:
        # (a)
        mu1=min(abs(Fr(s1,ns[0])+Fr(s2,ns[1])+Fr(s3,ns[2])) for s1 in (1,-1) for s2 in (1,-1) for s3 in (1,-1))
        if not mu1>=Fr(3,H*H*p): ok=False
        r1=mu1/Fr(3,H*H*p); worst1=r1 if worst1 is None else min(worst1,r1)
        # (b)
        L=[lifts(n,p,H) for n in ns]
        thr=Decimal(2)/(Decimal(H*H)*sp)
        for i in range(3):
            j,k=[t for t in range(3) if t!=i]
            for w in L[i]:
                for sj in (1,-1):
                    for sk in (1,-1):
                        q=Fr(sj,ns[j])+Fr(sk,ns[k])
                        # exact test of |A + B sqrt p| >= 2/(H^2 sqrt p)  <=>  R + S sqrt p >= 0,
                        # R = A^2 + p B^2 - 4/(H^4 p), S = 2AB (rational); decided by sign-aware squaring.
                        A=w/ns[i]; R=A*A+p*q*q-Fr(4,H**4*p); S=2*A*q
                        if S>=0: good = (R>=0) or (S*S*p>=R*R)
                        else:    good = (R>=0) and (R*R>=S*S*p)
                        if not good: ok=False
                        val=abs(Decimal(w.numerator)/Decimal(w.denominator*ns[i]) + sp*Decimal(q.numerator)/Decimal(q.denominator))
                        r2=val/thr; worst2=r2 if worst2 is None else min(worst2,r2)   # margin: informational only
        # (c)
        for (i,j,k) in ((0,1,2),(0,2,1),(1,2,0)):
            for wi in L[i]:
                for wj in L[j]:
                    wk=-ns[k]*(wi/ns[i]+wj/ns[j])
                    if valid(wk,ns[k],p): nhits+=1
    return ok,nhits,len(T),worst1,worst2
if __name__=="__main__":
    H=int(sys.argv[1]); out=[]
    for p in [int(a) for a in sys.argv[2:]]:
        ok,nh,nt,w1,w2=cert(p,H)
        print(f"p={p} H={H}: ES triples {nt}; truncation certificate (a),(b) holds: {ok} (margins a: {float(w1):.2f}x, b: {float(w2):.2f}x); lifts found in (c): {nh}; "
              f"{'NO TWISTED LIFT (certified)' if ok and nh==0 else ('LIFT EXISTS' if nh else 'inconclusive at this H')}",flush=True)
