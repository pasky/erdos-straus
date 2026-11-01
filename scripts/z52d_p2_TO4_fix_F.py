# z52d pass2 TO4 lint-fix F: Z1025 with target-matched baseline: for each (C1<C2≤20) with target C=C1*C2 (≤400, ∉{C1,C2}),
# compare P(win(C) | win(C1)&win(C2)) with P(win(C)) (the unconditional rate of the SAME target C, over the same primes).
import math, statistics
from collections import defaultdict
rows={}
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); rows[t[0]]=set(t[2:2+t[1]])
P=[p for p in sorted(rows) if p%24==1 and 10**4<=p<=10**6]
rate={C: sum(1 for p in P if C in rows[p])/len(P) for C in range(1,401)}
for name,op in [("product",lambda a,b:a*b),("lcm",lambda a,b:a*b//math.gcd(a,b))]:
    n=0; hit=0; base=[]
    for p in P:
        W=rows[p]
        for C1 in range(1,21):
            if C1 not in W: continue
            for C2 in range(C1+1,21):
                if C2 not in W: continue
                C=op(C1,C2)
                if C>400 or C in (C1,C2): continue
                n+=1; hit+= (C in W)
    # target-matched baseline: average unconditional rate over the same multiset of targets
    tg=[]
    for C1 in range(1,21):
        for C2 in range(C1+1,21):
            C=op(C1,C2)
            if C<=400 and C not in (C1,C2): tg.append(C)
    bl=statistics.mean(rate[C] for C in tg)
    print("Z1025 %s: P(win(C)|win(C1)&win(C2))=%.4f over %d (p,C1,C2) triples; target-matched unconditional rate=%.4f; ratio %.2f"%(name,hit/n,n,bl,(hit/n)/bl))
