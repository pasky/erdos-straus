"""Finite index census, including CRT couplings; discovery/replay uses PARI."""
from collections import Counter
from math import gcd, prod
from cypari2 import Pari

p = Pari()

def fac(n):
    return {int(q): int(e) for q, e in zip(*p.factor(n))}

def indices(h):
    B = lambda a: 1 + (1 << a)
    # One generating column for each index; fix the gcd representative in each orbit.
    ab = [(a, gcd(a,h)) for a in range(1,h) if a != gcd(a,h)]
    blocks = []
    for q, e in fac((1 << h)-1).items():
        n = q**e
        order = n//q*(q-1)
        F = fac(order)
        z = [B(a)*pow(B(b),-1,n)%n for a,b in ab]
        def ix(S):
            v = order
            for l,t in F.items():
                for _ in range(t):
                    if all(pow(x,v//l,n)==1 for x in S): v//=l
                    else: break
            return order//v
        i = ix(z)
        iu = ix([x for x,(_,b) in zip(z,ab) if b==1])
        blocks.append((q,n,order,F,z,i))
        if i!=1 or iu!=1 or q==73: print(f'  q={q} power={e} local_index={i} unit_only={iu}')
    powers = Counter(l for _,_,_,F,_,_ in blocks for l in F)
    index = 1
    for l, cnt in sorted(powers.items()):
        rows=[]; mods=[]
        for q,n,order,F,z,i in blocks:
            if l not in F: continue
            if cnt==1:
                index *= l**fac(i).get(l,0)
                continue
            m = l**F[l]; t = order//m
            g=p.Mod(pow(int(p.znprimroot(n)),t,n),n)
            rows.append([int(p.znlog(pow(x,t,n),g,m)) for x in z]); mods.append(m)
        if rows:
            G=p.matrix(len(rows),len(ab),sum(rows,[]))
            index *= int(p.matdet(p.mathnf(p.concat(p.matdiagonal(p.Vec(mods)),G))))
    print(f'h={h} blocks={len(blocks)} local_product={prod(b[-1] for b in blocks)} index={index}',flush=True)

if __name__=='__main__':
    for h in (9,27,35,77,105,115,119,127,133,143,165,255): indices(h)
