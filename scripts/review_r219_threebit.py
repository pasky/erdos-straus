"""R219 from scratch: three-bit law for ALL words (signed and positive) of odd n <= N.
Checks, for every word w=(t,u,v), tuv-u-v=n, t,u,v != 0:
 (a) chi(w) = eps2(w) * eps_inf(w)   [eps_l = +1 iff Q_w isotropic over Q_l; Q_w ~ <v, vB, nB>]
 (b) certificate (4 | A,B,t,u or v)  <=>  eps2(w) = +1
 (c) certificate <=> chi * s_inf = -1  (s_inf = +1 iff w positive)
 (d) eps_inf = -1 <=> positive (L1); (e) eps2 is a function of (t,u,v) mod 8.
Also checks odd-l anisotropy formula eps_l = (-A/l)^{v_l(n)} on all words (CHI_FLIP Thm 1.1 proof without positivity)."""
import sys
sys.path.insert(0,'scripts')
from review_r219_slots import jac, fac, divisors
def v2split(a):
    k=0
    while a%2==0: a//=2; k+=1
    return k,a
def hilb2(a,b):
    al,u=v2split(a); be,w=v2split(b)
    e=lambda x:((x%8)-1)//2 %2
    o=lambda x:(((x%8)**2-1)//8)%2
    return -1 if (e(u)*e(w)+al*o(w)+be*o(u))%2 else 1
def hilbp(a,b,p):
    al=0
    while a%p==0: a//=p; al+=1
    be=0
    while b%p==0: b//=p; be+=1
    s=(-1)**(al*be*((p-1)//2)%2)
    return s*jac(a,p)**be*jac(b,p)**al
def hilbinf(a,b): return -1 if a<0 and b<0 else 1
def eps(diag,place):
    a1,a2,a3=diag; H=(lambda x,y:hilb2(x,y)) if place==2 else (hilbinf if place=='inf' else (lambda x,y:hilbp(x,y,place)))
    c=H(a1,a2)*H(a1,a3)*H(a2,a3); d=a1*a2*a3
    return 1 if c==H(-1,-d) else -1
N=int(sys.argv[1]); cnt=nsg=0; bad={k:0 for k in 'abcdel'}; cell={}
for n in range(3,N+1,2):
    for t in [x for s in range(1,n+4) for x in (s,-s)]:
        M=t*n+1
        for d in divisors(fac(abs(M))):
            for A in (d,-d):
                if A==-1 or (A+1)%t: continue
                B=M//A
                if B==-1: continue
                u=(A+1)//t; v=(B+1)//t
                assert u and v and t*u*v-u-v==n
                cnt+=1; pos=t>0 and u>0 and v>0; nsg+= not pos
                chi=jac(-A,n); diag=(v,v*B,n*B)
                e2=eps(diag,2); ei=eps(diag,'inf')
                cert=any(x%4==0 for x in (A,B,t,u,v)); sinf=1 if pos else -1
                bad['a']+= chi!=e2*ei; bad['b']+= cert!=(e2==1); bad['c']+= cert!=(chi*sinf==-1); bad['d']+=(ei==-1)!=pos
                key=(t%8,u%8,v%8)
                if cell.setdefault(key,e2)!=e2: bad['e']+=1
                for l in fac(n):
                    vl=0; m=n
                    while m%l==0: m//=l; vl+=1
                    if eps(diag,l)!=jac(-A,l)**vl: bad['l']+=1
print("odd n<=",N,"words",cnt,"signed",nsg,"cells",len(cell),"violations",bad)
