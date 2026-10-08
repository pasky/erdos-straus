"""O92 sanity check of POINTWISE_TYPEI5 Lemma 1.1 (Lehmer minimality), exact integers.
For all P<=Pmax, Q=7*Q1 (Q1<=Qmax), PQ non-square: find the minimal solution of 16PX^2-Qu^2=1 by iterating
the group G (fundamental unit of A^2-16dB^2=1 via continued fractions), generate alpha^n (n odd <= 15),
check u_n = u_1*L_n and that u_n is a 7-power only for n=1.  Usage: typei5_lehmer_check.py Pmax Qmax"""
import sys
from math import isqrt
def fund(D):  # fundamental solution of A^2 - D B^2 = 1
    a0=isqrt(D); m,dd,a=0,1,a0; p0,p1=1,a0; q0,q1=0,1
    while p1*p1-D*q1*q1!=1:
        m=dd*a-m; dd=(D-m*m)//dd; a=(a0+m)//dd; p0,p1=p1,a*p1+p0; q0,q1=q1,a*q1+q0
    return p1,q1
def is7pow(x):
    while x%7==0: x//=7
    return x==1
Pmax,Qmax=int(sys.argv[1]),int(sys.argv[2]); nsol=0; bad=0
for P in range(1,Pmax+1):
  for Q1 in range(1,Qmax+1):
    Q=7*Q1; d=P*Q
    if isqrt(d)**2==d: continue
    A,B=fund(16*d)               # generator nu0 of G = {A+4B sqrt d}
    # alpha^2 = nu0 (m=1) iff nu0 = (16PX^2+Qu^2) + 8Xu sqrt d with 16PX^2-Qu^2=1: A-1 = 2Qu^2
    if (A-1)%(2*Q): continue
    u2=(A-1)//(2*Q); u=isqrt(u2)
    if u*u!=u2 or (A+1)%(32*P): continue
    X=isqrt((A+1)//(32*P))
    if 16*P*X*X-Q*u*u!=1: continue
    nsol+=1
    # generate alpha^n via (4X sqrt P + u sqrt Q) recursion: multiply by alpha^2 = A + 4B sqrt d
    Xn,un=X,u
    for n in range(3,16,2):
        Xn,un=(4*Xn*A+4*un*B*Q)//4, 16*Xn*B*P+un*A
        assert 16*P*Xn*Xn-Q*un*un==1 and un%u==0
        if is7pow(un): bad+=1; print("COUNTEREXAMPLE",P,Q,n,un)
print(f"pairs with odd-u solutions (m=1 case): {nsol}; 7-power u_n with n>=3: {bad}")
