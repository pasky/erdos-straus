# z52d pass2 TO1 (Z0269): per-family failure counts for the standard Type I / Type II divisor families (FRONTIER.md 'Parametrisations';
# CONDITIONAL_ES.md s1): Type I(c,d): f | p^2+4c^2 d with f = -p (mod 4cd);  Type II(c,d): f f' = 1+4c^2 d p with f = f' = -1 (mod 4cd).
# Primes p = 1 mod 4, p < N; parameters 1<=c,d<=R. usage: uv run --with sympy python scripts/z52d_p2_TO1_families.py N R
import sys, json
from sympy import primerange, divisors
N=int(sys.argv[1]); R=int(sys.argv[2])
P=[p for p in primerange(5,N) if p%4==1]
fam1={}; fam2={}
covI=dict(); covII=dict()
anyI={p:False for p in P}; anyII={p:False for p in P}
for c in range(1,R+1):
    for d in range(1,R+1):
        m=4*c*d
        f1=[]; f2=[]
        for p in P:
            M=p*p+4*c*c*d
            ok1=any(((f+p)%m==0) for f in divisors(M))
            if ok1: anyI[p]=True
            f1.append(ok1)
            M2=1+4*c*c*d*p
            ok2=False
            for f in divisors(M2):
                if (f+1)%m==0 and ((M2//f)+1)%m==0: ok2=True; break
            if ok2: anyII[p]=True
            f2.append(ok2)
        fam1[(c,d)]=sum(1 for v in f1 if not v); fam2[(c,d)]=sum(1 for v in f2 if not v)
print(f"primes p=1 mod 4 < {N}: {len(P)}; families c,d<={R}")
best1=sorted(fam1.items(), key=lambda t:t[1])[:6]; best2=sorted(fam2.items(), key=lambda t:t[1])[:6]
print("Type I: fewest failing primes:", best1, " median failures over families:", sorted(fam1.values())[len(fam1)//2])
print("Type II: fewest failing primes:", best2, " median failures over families:", sorted(fam2.values())[len(fam2)//2])
print("union over all Type I families:", sum(1 for p in P if not anyI[p]), "primes uncovered;  union over all Type II families:", sum(1 for p in P if not anyII[p]), "uncovered;  I or II:", sum(1 for p in P if not (anyI[p] or anyII[p])))
json.dump({'typeI_fail':{f"{k[0]},{k[1]}":v for k,v in fam1.items()}, 'typeII_fail':{f"{k[0]},{k[1]}":v for k,v in fam2.items()}}, open(f'data/z52b/pass2/TO1/families_{N}_{R}.json','w'))
