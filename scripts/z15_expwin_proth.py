# O240: exponential window rules for n_s = c*2^s + 1 (c odd).  Window m = c*2^j*w - 1 (j >= 2), K = c*2^(j-2)*(2^(s-j) + w).
# Shapes: SG (Sophie Germain): w = t^4, s-j == 2 (mod 4), 2^(s-j) + t^4 = 4X^4 + t^4 = (2X^2+2Xt+t^2)(2X^2-2Xt+t^2),
#         X = 2^((s-j-2)/4);  CY_e (e odd >= 3): w = t^e, e | s-j, U = 2^((s-j)/e), U^e + t^e = prod_{f|e} Psi_f(U,t).
# Atoms: 2 (mult j-2), primes of c (mult), the algebraic factors (mult 1).  Cap 0: exps <= 2*mult, d == -K (mod m),
# gcd(K, m) = 1.  A rule (shape, j, t, e, exps) is valid on {s : congruence on s mod period, residue condition mod m}:
# the residues of all atoms mod m are periodic in s with period P = (4 or e)*ord_m(2).
# rule_valid(s, rule) is evaluated mod m only (cheap).  exact_check verifies the ES solution for given s.
import sys, math, itertools
from fractions import Fraction as F
from sympy import factorint, n_order, cyclotomic_poly, symbols, Poly
Usym=symbols('U')
def psi(f,U,t,mod):   # homogenised Phi_{2f}(U,t) for odd f, mod `mod`
    co=Poly(cyclotomic_poly(2*f,Usym),Usym).all_coeffs()[::-1]; dgr=len(co)-1
    return sum(int(a)*pow(U,i,mod)*pow(t,dgr-i,mod) for i,a in enumerate(co))%mod
def atoms_mod(c,s,shape,j,t,e,m):
    r=s-j
    if shape=='SG':
        if r%4!=2: return None
        X=pow(2,(r-2)//4,m); fac=[(2*X*X+2*X*t+t*t)%m,(2*X*X-2*X*t+t*t)%m]
    else:
        if r%e: return None
        U=pow(2,r//e,m); fac=[psi(f,U,t,m) for f in range(1,e+1,2) if e%f==0]
    at=[]
    if j>2: at.append((2,j-2))
    for p,v in factorint(c).items(): at.append((p%m,v))
    for x in fac: at.append((x,1))
    return at
def find_rules(c,s,JMAX,TMAX,EMAX,want_all=False):
    n=c*2**s+1; out=[]
    shapes=[('SG',4)]+[('CY',e) for e in range(3,EMAX+1,2)]
    for shape,e in shapes:
        for j in range(2,JMAX+1):
            if j>=s-2: break
            for t in range(1,TMAX+1,2):
                w=t**4 if shape=='SG' else t**e
                m=c*2**j*w-1
                at=atoms_mod(c,s,shape,j,t,e,m)
                if at is None: continue
                K=(c*pow(2,s,m)+1+m)*pow(4,-1,m)%m
                if math.gcd(K,m)!=1 or any(math.gcd(a,m)!=1 for a,_ in at): continue
                tgt=(-K)%m
                for ex in itertools.product(*[range(2*v+1) for _,v in at]):
                    d=1
                    for (a,_),x in zip(at,ex): d=d*pow(a,x,m)%m
                    if d==tgt:
                        out.append((shape,j,t,e,ex,m))
                        if not want_all: return out
                        break
    return out
def exact_check(c,s,rule):
    shape,j,t,e,ex,m=rule; n=c*2**s+1; r=s-j
    if shape=='SG':
        X=2**((r-2)//4); fac=[2*X*X+2*X*t+t*t,2*X*X-2*X*t+t*t]
    else:
        U=2**(r//e); fac=[]
        for f in range(1,e+1,2):
            if e%f==0:
                co=Poly(cyclotomic_poly(2*f,Usym),Usym).all_coeffs()[::-1]; dgr=len(co)-1
                fac.append(sum(int(a)*U**i*t**(dgr-i) for i,a in enumerate(co)))
    at=([2] if j>2 else [])+list(factorint(c).keys())+fac
    d=1
    for a,x in zip(at,ex): d*=a**x
    K=(n+m)//4; assert 4*K==n+m and K%d==0 or (K*K)%d==0
    A=F(K+d,m); z=F(n*K*A,d)
    return A.denominator==1 and z.denominator==1 and F(4,n)==F(1,K)+F(1,n*A)+1/z
if __name__=="__main__":
    c=int(sys.argv[1]); s0=int(sys.argv[2]); step=int(sys.argv[3]); cnt=int(sys.argv[4])
    for i in range(cnt):
        s=s0+step*i
        rs=find_rules(c,s,24,15,9,want_all=True)
        good=[r for r in rs if exact_check(c,s,r)]
        print(s,len(good),[(r[0],r[1],r[2],r[3],r[5],r[4]) for r in good[:4]],flush=True)
