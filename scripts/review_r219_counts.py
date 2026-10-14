"""R219: average number of chi=-1 words at primes <= N: strictly signed vs positive vs all (s4_three_bits_meta P3(c));
and (R_2) at t=-1 for all odd n in [5,N] (signed word with certificate)."""
import sys
sys.path.insert(0,'scripts')
from review_r219_slots import jac, fac, divisors
N=int(sys.argv[1]); P=0; S=Pp=0; r2fail=[]
for n in range(5,N+1,2):
    isp = fac(n)=={n:1}
    if isp:
        P+=1
        for t in [x for s in range(1,n+4) for x in (s,-s)]:
            M=t*n+1
            for d in divisors(fac(abs(M))):
                for A in (d,-d):
                    if A==-1 or (A+1)%t: continue
                    B=M//A
                    if B==-1: continue
                    u=(A+1)//t; v=(B+1)//t
                    if jac(-A,n)==-1:
                        if t>0 and u>0 and v>0: Pp+=1
                        else: S+=1
    ok=False
    for A in divisors(fac(n-1)):
        for a in (A,-A):
            B=(1-n)//a
            if a==-1 or B==-1: continue
            u=-(a+1); v=-(B+1)
            if u and v and not (u>0 and v>0) and any(x%4==0 for x in (a,B,u,v)): ok=True
    if not ok: r2fail.append(n)
print("primes",P,"avg strictly-signed chi=-1",S/P,"avg positive chi=-1",Pp/P,"avg all",(S+Pp)/P)
print("(R_2) at t=-1 failures in [5,N]:",r2fail[:10],len(r2fail))
