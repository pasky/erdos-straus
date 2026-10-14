"""R219: K1/K2 of s4_kudla_green_infinity from scratch. For all words of odd n <= N (signed and positive):
 B_T := quaternion algebra (-B, -t n) attached to T_w = [[B,1],[1,A]] (det tn; T ~ <B, B t n>).
 Check: (1) inv_v B_T = eps_v(Q_w) (isotropy sign of the path form) at v = 2, inf, and every l | n, l | t;
        (2) T_w positive definite <=> w positive (K1);
        (3) at odd squares: Diff := Ram_fin(B_T) ∪ ({inf} if T not pos.def.) has odd size, and Diff = {inf} <=> certificate."""
import sys
sys.path.insert(0,'scripts')
from review_r219_slots import jac, fac, divisors
from review_r219_threebit import hilb2, hilbp, hilbinf, eps
import math
N=int(sys.argv[1]); bad={'1':0,'2':0,'3':0}; cnt=0; sq=0
for n in range(3,N+1,2):
    for t in [x for s in range(1,n+4) for x in (s,-s)]:
        M=t*n+1
        for d in divisors(fac(abs(M))):
            for A in (d,-d):
                if A==-1 or (A+1)%t: continue
                B=M//A
                if B==-1: continue
                u=(A+1)//t; v=(B+1)//t; cnt+=1
                pos=t>0 and u>0 and v>0; diag=(v,v*B,n*B)
                places=[2,'inf']+[l for l in set(fac(n))|set(fac(abs(t))) if l>2]
                for pl in places:
                    h = hilb2(-B,-t*n) if pl==2 else hilbinf(-B,-t*n) if pl=='inf' else hilbp(-B,-t*n,pl)
                    if h!=eps(diag,pl): bad['1']+=1
                pd = B>0 and t*n>0
                if pd!=pos: bad['2']+=1
                r=math.isqrt(n)
                if r*r==n:
                    sq+=1
                    ram=[pl for pl in [2]+[l for l in set(fac(n))|set(fac(abs(t))) if l>2] if (hilb2(-B,-t*n) if pl==2 else hilbp(-B,-t*n,pl))==-1]
                    diff=set(ram)|({'inf'} if not pd else set())
                    cert=any(x%4==0 for x in (A,B,t,u,v))
                    if len(diff)%2==0 or (diff=={'inf'})!=cert: bad['3']+=1
print("words",cnt,"square-n words",sq,"violations",bad)
