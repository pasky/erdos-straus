# z70 LOOSE I9, post-hoc size check of the AMENDED (window-free) decoy: two-sided decoys
# (nearest admissible prime below q AND nearest above q); only pairs where both exist; Y(q) vs mean of the two.
import sys, json, math
sys.path.insert(0,'scripts')
from sympy import isprime, legendre_symbol, prevprime, nextprime
from z70_loose_i9 import badq, yword
rows=json.load(open('data/z70/loose/i9_rows.json'))
def side(p,q,X,step):
    c=q
    while True:
        c = prevprime(c) if step<0 else nextprime(c)
        if c<=7: return None
        if c%8==q%8 and X%c and legendre_symbol(p%c,c)==-1: return c
for name in rows:
    for lab,pool in (('hard',rows[name]),('ctl',[c for r in rows[name] for c in r['ctl']])):
        a=[];lr=[]
        for r in pool:
            if not r['Q']: continue
            X,Y,bq=badq(r['p']); q=bq[0]
            lo=side(r['p'],q,X,-1); hi=side(r['p'],q,X,+1)
            if lo is None or hi is None: continue
            a.append((r['Yq'], (yword(r['p'],lo)+yword(r['p'],hi))/2)); lr.append(math.log(lo*hi/q/q)/2)
        if not a: continue
        d=[x-y for x,y in a]; m=sum(d)/len(d); sd=math.sqrt(sum((x-m)**2 for x in d)/max(1,len(d)-1)/len(d)) if len(d)>1 else 0
        print(f"{name} {lab}: pairs={len(a)} Y(q)={sum(x for x,_ in a)/len(a):.3f} Y(two-sided decoy)={sum(y for _,y in a)/len(a):.3f} diff={m:+.4f} z={m/sd if sd else 0:+.2f} mean log(geo-mean decoy/q)={sum(lr)/len(lr):+.3f}")
