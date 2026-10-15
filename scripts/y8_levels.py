# usage: y8_levels.py data/y8/y8_sample600.txt 30 100   (sample = 600 random primes p = 1 mod 4 in (2e5,1e6), seed 1)
# fraction of "Legendre-clean" levels: all prime factors l of tp+1 have (l/p)=+1 (=> every level-t word has chi=+1)
import sys, math
from sympy import factorint, legendre_symbol as L
from collections import defaultdict
T=int(sys.argv[2]); Y=int(sys.argv[3]) if len(sys.argv)>3 else 100; g=defaultdict(lambda:[0,0,0.0,0.0])
for line in open(sys.argv[1]):
    p=int(line.split()[0]); B=next(q for q in range(2,p) if L(q,p)==-1)
    for t in range(1,T+1):
        f=factorint(t*p+1); clean=all(L(l%p,p)==1 for l in f)
        k=(p%8,min(B,17)); a=g[k]; a[0]+=1; a[1]+=clean; a[2]+=math.sqrt(math.log(B)/math.log(t*p)); small_ok=all(L(l%p,p)==1 for l in f if l<=Y); k=sum(1 for l in f if l>Y and f[l]%2); s_ev=sum(1 for l in f if l>Y and f[l]%2==0)
        a[3]+= (2.0**(-s_ev-max(k-1,0)) if small_ok else 0.0)  # R-O217 repair: even-exponent rough primes are free coins  # coin model: exact signs for l<=Y, fair coins above Y, with the exact constraint prod_l (l/p)^{e_l} = ((tp+1)/p) = +1
for k in sorted(g): c,cl,pr,fc=g[k]; print(k, c, "clean frac %.3f"%(cl/c), "sqrt(logB/log tp) %.3f"%(pr/c), "coin model (exact <=Y, constrained coins >Y) %.3f"%(fc/c))
