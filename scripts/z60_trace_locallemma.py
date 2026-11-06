# Local lemma for the elliptic term (Theorem 2 via Cohen-Stromberg Thm 12.4.11 at level M=Q^2, summed over chi mod Q):
#   W(t) := sum_{f} h_w((t^2-4N)/f^2) * psi(M)/psi(M/M_f) * #{x mod M : x^2 - t x + N = 0 mod M*M_f, x = -1 mod Q}
# Claim: W(t) = psi(M) * H((4N-t^2)/Q^2) if t = -2 - Q*n (mod Q^2) [i.e. t=Qw-2, w=-n mod Q], else 0.  (N = Qn+1)
import sys
from fractions import Fraction
from math import gcd, isqrt
import cypari2
pari=cypari2.Pari()
def psi(m):
    r=Fraction(m); q=m; d=2
    while d*d<=q:
        if q%d==0:
            r*=Fraction(d+1,d)
            while q%d==0: q//=d
        d+=1
    if q>1: r*=Fraction(q+1,q)
    return r
def hw(D):  # D negative discriminant
    h=int(pari.qfbclassno(D)); w=6 if D==-3 else (4 if D==-4 else 2)
    return Fraction(h*2,w)
def H(D): return Fraction(str(pari.qfbhclassno(D)))
bad=0; cnt=0
for Q in [4,8,12,16,20]:
    M=Q*Q; pM=psi(M)
    for n in range(1, int(sys.argv[1])+1):
        N=Q*n+1
        L=isqrt(4*N-1)
        for t in range(-L, L+1):
            D=t*t-4*N
            W=Fraction(0)
            f=1
            while f*f<=-D:
                if D%(f*f)==0 and (D//(f*f))%4 in (0,1):
                    Mf=gcd(M,f); mod=M*Mf
                    c=sum(1 for x in range(-1, M, Q) if x>=0 and (x*x-t*x+N)%mod==0) if True else 0
                    # x runs over residues mod M with x = -1 mod Q: x = Q-1, 2Q-1, ...
                    c=sum(1 for x in range(Q-1, M, Q) if (x*x-t*x+N)%mod==0)
                    if c: W+=hw(D//(f*f))*pM/psi(M//Mf)*c
                f+=1
            good = ((t+2+Q*n) % M == 0)
            exp = pM*H((4*N-t*t)//M) if good else 0
            cnt+=1
            if W!=exp:
                bad+=1
                if bad<5: print("MISMATCH",Q,n,t,W,exp)
print("cases",cnt,"mismatches",bad)
sys.exit(1 if bad else 0)
