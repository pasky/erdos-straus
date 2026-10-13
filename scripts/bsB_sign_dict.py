"""bsB sign dictionaries (O175). Checks:
 (Z) Zolotarev/transpose: for a Type I (a=1) certificate g n + 1 = m m'' (m = fg-1, m'' = cg-1, 4|m),
     the transpose of an m x m'' array is x -> m x mod (gn) and sgn = (m/gn) = (-1)^{C(m,2)C(m'',2)} = +1,
     and its Z/n-component has sign (m/n) = class sign.
 (T) theta multiplier: gamma^{-1} = [[-g, m''],[-m, n]] in Gamma_0(4), multiplier (c/d) = (-m/n) = (m''/n).
usage: python bsB_sign_dict.py NMAX"""
import sys
from sympy import jacobi_symbol as J
def perm_sign(perm):
    n=len(perm); seen=[False]*n; s=1
    for i in range(n):
        if not seen[i]:
            L=0; j=i
            while not seen[j]: seen[j]=True; j=perm[j]; L+=1
            if L%2==0: s=-s
    return s
N=int(sys.argv[1]); cnt=0; bad=0; small=0
for n in range(5,N+1,4):
    for g in range(3,n+3,4):          # t = g = 3 mod 4 (forced)
        T=g*n+1
        for m in range(4,T+1,4):
            if T%m: continue
            mm=T//m
            if (m+1)%g or (mm+1)%g: continue   # m = fg-1, m''=cg-1  (both = -1 mod g)
            cnt+=1
            s_n=J(m%n,n) if n>1 else 1
            if J(mm%n,n)!=s_n or s_n!=-1: bad+=1
            if J((-m)%n,n)!=J(mm%n,n): bad+=1          # theta multiplier (c/d), d=n=1 mod 4
            if m*mm<=400:                                # explicit transpose permutation
                small+=1; M=m*mm-1
                perm=[(x*m)%M for x in range(M)]
                tr=[ (k%mm)*m + k//mm for k in range(M)]
                if perm!=tr or perm_sign(perm)!=J(m%M,M) or perm_sign(perm)!=1: bad+=1
                # Z/n component: multiplication by m on Z/n
                if perm_sign([(x*m)%n for x in range(n)])!=s_n: bad+=1
print(f"certificates={cnt} explicit_perm_checks={small} violations={bad}")
