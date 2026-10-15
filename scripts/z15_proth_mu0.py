# O240: root-menu (exponential) window classes for n_s = c*2^s + 1 near the unit-square point mu = 0 (s == 0 mod L).
# Window m = c*2^j*w - 1 (j >= 2), K = (n+m)/4 = c*2^(j-2)*(U^e + w), U = 2^((s-j)/e), e | j.
# Near mu = 0 (s == 0 mod e*ord_m(2)): U == 2^(-j/e) mod m and n == c+1 (mod m).
# Atoms: 2 (mult j-2), primes of c (mult v), irreducible factors f_i of U^e + w over Z (mult m_i).
# Cap-0 Lemma 1.1 window: d = prod atom^{c_a}, 0 <= c_a <= 2*mult, d == -K (mod m), gcd(K, m) = 1.
# Usage: z15_proth_mu0.py c EMAX JMAX WMAX
import sys, math, itertools
from fractions import Fraction as F
from sympy import symbols, factor_list, factorint, n_order, Poly
c=int(sys.argv[1]); EMAX=int(sys.argv[2]); JMAX=int(sys.argv[3]); WMAX=int(sys.argv[4])
Uv=symbols('U')
hits=[]
for e in range(2,EMAX+1):
    for w in range(1,WMAX+1,2):
        fl=factor_list(Uv**e+w)[1]
        if len(fl)==1 and fl[0][1]==1: continue          # irreducible: only polynomial-in-n type atoms
        facs=[(Poly(f,Uv).all_coeffs(),mult) for f,mult in fl]
        for j in range(e, JMAX+1, e):
            if j<2: continue
            m=c*2**j*w-1
            o=n_order(2,m)
            U0=pow(pow(2,j//e,m),-1,m)                    # U == 2^(-j/e) mod m
            atoms=[(2,j-2)] if j>2 else []
            for p,v in factorint(c).items(): atoms.append((p,v))
            ok=True
            for co,mult in facs:
                val=0
                for a in co: val=(val*U0+int(a))%m
                if math.gcd(val,m)!=1: ok=False;break
                atoms.append((val,mult))
            if not ok or any(math.gcd(a,m)!=1 for a,_ in atoms): continue
            K=( (c+1)*pow(4,-1,m) )%m                      # K == n/4, n == c+1
            target=(-K)%m
            # meet in the middle over exponent vectors
            ranges=[range(0,2*mult+1) for _,mult in atoms]
            found=None
            for ex in itertools.product(*ranges):
                d=1
                for (a,_),x in zip(atoms,ex): d=d*pow(a,x,m)%m
                if d==target: found=ex;break
            if found: hits.append((e,w,j,m,o,found)); print("HIT e=%d w=%d j=%d m=%d ord=%d exps=%s"%(e,w,j,m,o,found),flush=True)
print("total hits",len(hits))
