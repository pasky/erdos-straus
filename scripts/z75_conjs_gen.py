"""Replay: uv run --offline --no-project --with cypari2 python scripts/z75_conjs_gen.py W1 W2 F1 F2 F3 F4"""
import itertools, json, math, sys
from fractions import Fraction
from pathlib import Path
from collections import Counter, defaultdict
import z70_gen_core as C
P = C.pari
DS = (1,2,3,5,7)

def numbers(f):
    return [int(s.split()[0]) for s in Path('data/z58/screens/'+f+'.txt').read_text().splitlines() if s and s[0]!='#']

def count_forms(N):
    # |b| <= a <= c, with b >= 0 on boundaries; b=2r.
    h=0
    for r in range(math.isqrt(N//3)+1):
        m=N+r*r
        for a in C.divisors(m):
            if a*a>m: break
            if 2*r<=a and math.gcd(a,2*r,m//a)==1:
                h+=1+(r!=0 and 2*r<a and a*a<m)
    return h

def run(n,d):
    G={C.good_class(n,d,s) for s in C.solutions(n,d)}
    if math.isqrt(n)**2==n:
        assert not G
        return dict(n=n,d=d,G=0,T=0,out=[[],[],[]])
    cg=C.ClassGroup(n,d,1000000)
    assert cg.h==count_forms(n*d)
    # Invariant factors have the stated orders (in addition to distinctness and full h).
    one=(1,0,n*d)
    for g,o in zip(cg.gens,cg.cyc): assert tuple(map(int,P.qfbpow(g,o)))==one
    zero=(0,)*len(cg.cyc); pg=cg.sqclass(zero); ng=2**len(pg)
    buckets=defaultdict(list); target={}; anchor=None; qs=[]
    needanchor=any(o & (o-1) for o in cg.cyc)
    q=3
    while len(qs)<3*ng or (needanchor and anchor is None):
        if C.kron(-n*d,q)==1:
            k=int(P.Mod(-n*d,q).sqrt().lift()); r=min(k,q-k)
            v=cg.vec(C.ideal_form(n,d,q,r)); g=cg.sqclass(v)
            # Assigned characters of d and 2 fixed at -1, and Jacobi(q/n)=-1.
            tg=C.kron(q,n)==-1 and all(C.chval(ch,q)==C.chval(ch,8*d*n-1) for ch in C.char_list(n,d) if ch[0]!='q' or d%ch[1]==0)
            assert target.setdefault(g,tg)==tg
            if len(buckets[g])<3:
                qs.append(q); buckets[g].append(v)
            if anchor is None and g==pg and not cg.is2power(v): anchor=(q,v)
        q=int(P.nextprime(q+1))
    T={v for v in cg.byvec if target[cg.sqclass(v)]}
    assert G.issubset({cg.byvec[v] for v in T})
    order=lambda v:(-Fraction(abs(cg.byvec[v][1]),cg.byvec[v][0]),cg.byvec[v])
    # Dynamic programming for exponent words, using each prime at most once.
    R=[{zero},set(),set(),set()]
    for base in itertools.chain.from_iterable(buckets.values()):
        shift={cg.mul(k,base) for k in (-2,-1,1,2)}
        for i in (3,2,1): R[i].update(cg.add(x,y) for x in R[i-1] for y in shift)
    mixed=sorted(T & set.union(*R),key=order)[:4]
    halves=sorted((v for v in T if anchor and any(cg.mul(k,v)==anchor[1] for k in (2,4))),key=order)[:4]
    rep=set(); ac=None; nbr=[]
    if n%8==1:
        for a in range(1,math.isqrt(n//(4*d))+1):
            m=n-4*d*a*a
            if m==math.isqrt(m)**2:
                ac=a; break
        if ac:
            for a in (ac-1,ac+1):
                if a<1: continue
                for l in P.factor(n+4*d*a*a)[0]:
                    l=int(l)
                    if math.gcd(l,2*d*n)==1 and C.kron(l,n)==-1:
                        rep.add(cg.vec(C.ideal_form(n,d,l,(2*d*a)%l))); nbr.append([a,l]); break
    total=Counter(cg.byvec[v][0] for v in T); good=Counter(f[0] for f in G)
    def report(S):
        return [[f,int(f in G),good[f[0]] if v in T else 0,total[f[0]] if v in T else 1] for v in S for f in [cg.byvec[v]]]
    return dict(n=n,d=d,h=cg.h,T=len(T),G=len(G),qs=qs,anchor=anchor and anchor[0],ac=ac,nbr=nbr,out=list(map(report,(mixed,halves,sorted(rep,key=order)))))

def jobs(tag):
    if tag in ('W1','W2'):
        lo=210000 if tag=='W1' else 2100000
        ns=[int(q) for q in P.primes([lo,lo+20000]) if q%24==1][:40]; assert len(ns)==40
    elif tag=='F1': ns=[m*m for m in range(3,302,2)]
    elif tag=='F2': ns=numbers('r8_zeros_1e10')
    elif tag=='F3': ns=numbers('composite_zeros_le8e6'); assert 4545 in ns
    else:
        assert tag=='F4'; ns=sorted(set(numbers('star_prime_zeros')+numbers('gstar_zeros')+[3361,2094481,85664329]))
    ds={'F2':[1,2],'F3':[1]}.get(tag,DS)
    return ((n,d) for n in ns for d in ds if math.gcd(n,d)==1)

if __name__=='__main__':
    for tag in sys.argv[1:]:
        with open('data/z75/conjs/'+tag+'.jsonl','w') as f:
            for n,d in jobs(tag): print(json.dumps(run(n,d),separators=(',',':')),file=f,flush=True)
