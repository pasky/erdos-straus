#!/usr/bin/env python3
"""z59 WALDS: search y^2 = x^3 + a x + b, |a| <= 60, |b| <= 200, conductor <= 20000 supported on {2,3,5,7}, root number +1,
for numerical analytic rank >= 2 (pari ellanalyticrank; EVIDENCE, not certified). Output: data/z59/walds/rank2_search.txt"""
import cypari2
pari=cypari2.Pari(); pari.allocatemem(800_000_000)
seen={}
def rad_ok(N):
    n=int(N)
    for p in (2,3,5,7):
        while n%p==0: n//=p
    return n==1
for a in range(-60,61):
    for b in range(-200,201):
        if 4*a**3+27*b**2==0: continue
        E=pari.ellinit([0,0,0,a,b])
        N=pari.ellglobalred(E)[0]
        if not rad_ok(N) or int(N)>20000: continue
        if pari.ellrootno(E)!=1: continue
        key=(int(N),str(pari.ellan(E,30)))
        if key in seen: continue
        r=pari.ellanalyticrank(E)[0]
        seen[key]=r
        if r>=2: print("RANK", r, "N=",N, "a,b=",a,b, flush=True)
print("searched; distinct isogeny-ish classes", len(seen))
