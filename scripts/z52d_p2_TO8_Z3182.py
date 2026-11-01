# z52d P2 TO8 Z3182: test candidate switch maps (★)-triple (u,B,C) -> b=1 pair {s,t} (B1 Lemma 1.1: st | p+s+t, 4 | st, s,t>=1)
# and whether the b=1 pair set for p equals the image of (★) triples under a natural map.
from math import gcd
def star(p):
    out=[]; u=1
    while 4*u-1 <= p+u:
        C=1
        while 4*u*C-1 <= p+u:
            if (p+u) % (4*u*C-1)==0:
                B=(p+u)//(4*u*C-1); out.append((u,B,C))
            C+=1
        u+=1
    return out
def b1pairs(p):
    S=set()
    for s in range(1, int((p+1)**0.5)+3):
        for t in range(1, p+s+t if False else 4*p+10):
            if (s*t)%4==0 and (p+s+t) % (s*t)==0 and s<=t: S.add((s,t))
            if t > 4*p: break
        # bounded search: st <= p+s+t  => t <= (p+s)/(s-1) for s>=2
    return S
def b1pairs_fast(p):
    S=set()
    for s in range(1, 2*int((p+1)**0.5)+5):
        if s==1:
            # st | p+1+t: t | p+1+t <=> t | p+1 ; with 4|t
            for t in range(4, p+2, 4):
                if (p+1+t) % t==0: S.add((min(1,t),max(1,t)))
            continue
        # t(s-1) <= p+s  => t <= (p+s)/(s-1)
        tmax=(p+s)//(s-1)+1
        for t in range(1, tmax+1):
            if (s*t)%4==0 and (p+s+t)%(s*t)==0:
                S.add((min(s,t),max(s,t)))
    return S
maps={
 'B,4uC': lambda u,B,C: (B,4*u*C),
 'u,4BC': lambda u,B,C: (u,4*B*C),
 '4uB,C?': lambda u,B,C: (4*u*B, C),
 'u+B,4C': lambda u,B,C: (u+B,4*C),
}
for p in [409, 577, 193, 2521, 1009, 10009, 5569]:
    S=star(p); Y=b1pairs_fast(p)
    line=[f"p={p}: (★)-triples={len(S)}, b=1 pairs={len(Y)}"]
    for name,f in maps.items():
        img=set()
        for tr in S:
            s,t=f(*tr); img.add((min(s,t),max(s,t)))
        line.append(f"{name}: image∩b1={len(img & Y)}/{len(img)}")
    print("; ".join(line))
