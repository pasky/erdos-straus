"""y5_words_at: list all positive formal words (c,m,s) at N with Jacobi sign (h'/N); counts interior sign -1 words.
usage: y5_words_at.py N"""
from y2_even_edge import jacobi
import sys
N=int(sys.argv[1]); res=[]
for c in range(1,N+2):
    # s*h = N + c, h = c*m - 1
    n=N+c
    for h in range(max(1,c-1), n+1):
        if h*h>n*4 and h>n: break
        if n%h or (h+1)%c: continue
        m=(h+1)//c; s=n//h
        if m<1: continue
        res.append((c,m,s,jacobi(m*s-1,N)))
    if c*c*1>4*N+10: break
neg=[w for w in res if w[3]==-1]; inter=[w for w in neg if min(w[:3])>=2]
print(N,'words',len(res),'neg',len(neg),'interior neg',len(inter),inter[:20])
