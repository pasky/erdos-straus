# fraction of "Legendre-clean" levels: all prime factors l of tp+1 have (l/p)=+1 (=> every level-t word has chi=+1)
import sys, math
from sympy import factorint, legendre_symbol as L
from collections import defaultdict
T=int(sys.argv[2]); g=defaultdict(lambda:[0,0,0.0])
for line in open(sys.argv[1]):
    p=int(line.split()[0]); B=next(q for q in range(2,p) if L(q,p)==-1)
    for t in range(1,T+1):
        f=factorint(t*p+1); clean=all(L(l%p,p)==1 for l in f)
        k=(p%8,min(B,17)); a=g[k]; a[0]+=1; a[1]+=clean; a[2]+=math.sqrt(math.log(B)/math.log(t*p))
for k in sorted(g): c,cl,pr=g[k]; print(k, c, "clean frac %.3f"%(cl/c), "sqrt(logB/log tp) %.3f"%(pr/c))
