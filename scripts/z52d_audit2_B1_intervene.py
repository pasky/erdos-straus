# Z1232: single-factor interventions on the e-slice event (FRONTIER §1 e-slice form, Type II):
#   ES-slice(p,e) <=> -1 in Q = {a b^-1 mod e : ab | N}, N = (p+e)/4, e ≡ -p (mod 4).
# For prime e ≤ 60 and primes p ≡ 1 (4), replace ONE prime factor l of N (one copy, residue class g mod e) by a
# factor of every other class g' and record how often the slice outcome flips (pivotality / influence).
import random
from sympy import primerange, factorint, isprime
random.seed(1)
def Qset(res_mult,e):       # res_mult: list of (residue, exponent); quotient set of ab|N  = prod g_i^{c_i}, |c_i|<=a_i
    S={1}
    for g,a in res_mult:
        pw=[pow(g,c,e) for c in range(0,a+1)]; inv=[pow(g,-c,e) for c in range(0,a+1)]
        mult=set(pw)|set(inv)
        S={(s*m)%e for s in S for m in mult}
    return S
ps=[p for p in primerange(10**6,2*10**6) if p%4==1]; ps=random.sample(ps,400)
stats={True:[0,0],False:[0,0]}   # outcome -> [flips, trials]
crit_hits=0; hits=0
for p in ps:
    for e in primerange(3,60):
        if (p+e)%4: continue
        N=(p+e)//4; F=factorint(N)
        rm=[(l%e,a) for l,a in F.items() if l%e]   # factors ≡0 mod e can't occur in units; skip them (they are not units)
        if any(l%e==0 for l in F): continue
        base=(e-1) in Qset(rm,e)
        if base: hits+=1
        crit=False
        for i,(g,a) in enumerate(rm):
            for g2 in range(1,e):
                if g2==g: continue
                rm2=rm[:i]+[(g,a-1)]+rm[i+1:]+[(g2,1)]
                o=(e-1) in Qset([(x,y) for x,y in rm2 if y>0],e)
                stats[base][1]+=1
                if o!=base: stats[base][0]+=1; crit=crit or base
        if crit: crit_hits+=1
for b,(f,t) in stats.items(): print(f'base outcome {b}: single-factor class changes flip it in {f}/{t} = {f/t:.3f}')
print(f'hit slices {hits}; hit slices where some single substitution kills the hit: {crit_hits} ({crit_hits/max(hits,1):.2f})')
