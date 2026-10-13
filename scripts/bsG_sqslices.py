# For n = m^2 (and control: non-squares), tabulate middle letter t mod 8 over all words xyz-x-z=n (x,z>=2, y=t>=2).
# words with middle t <-> factorisations t n + 1 = X Z, X = Z = -1 (mod t), X,Z >= 2t-1.
import sys
from collections import Counter
from sympy import divisors
def words(n):
    out=[]
    for x in range(2, int((n/2)**0.5)+3):
        N=n+x
        for d in divisors(N):
            if d%x==x-1 and d>=2*x-1:
                z=N//d
                if z>=2: out.append((x,(d+1)//x,z))
    return out
M=int(sys.argv[1])
for label,ns in [("odd squares",[m*m for m in range(5,M,2)]),("even squares",[m*m for m in range(4,M,2)]),("control n=m^2+2 (odd m)",[m*m+2 for m in range(5,M,2)])]:
    c=Counter(); tot=0
    for n in ns:
        for (x,t,z) in words(n): c[t%8]+=1; tot+=1
    print(label, "words:",tot, "t mod 8:",dict(sorted(c.items())))
