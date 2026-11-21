"""Index of the full gcd-ratio group. Produce/replay rows of certified factorizations.
No full discrete logarithms: the expected local defect has length at most one.
Track a minor of index prime to l or of l-valuation one. Deterministic PARI
isprime (not ispseudoprime) in replay. Run with -B; see note for invocation.
"""
from math import gcd, prod
from functools import cache
from pathlib import Path
import sys,json
from cypari2 import Pari
pa=Pari(); pa.allocatemem(48<<20,512<<20,silent=True); root=Path('data/z80/proth/index')
@cache
def hints():
    import re
    txt=Path('data/z80/proth/cunningham-slice.txt').read_text();P={}
    for m in re.finditer(r'^\s*(\d+) +([^\n]+)((?:\n +\.[^\n]+)*)',txt,re.M):
        h=int(m[1]);s=re.sub(r'\([^)]*\)','',m[2]+m[3]);z=2**h-1
        primes={q for d,ps in P.items() if h%d==0 for q,e in ps}
        primes.update(int(a) for a in re.findall(r'(?<![P\d])\b\d+\b',s));F=[]
        for q in sorted(primes):
            if q<2:continue
            e=0
            while z%q==0:z//=q;e+=1
            if e:F.append((q,e))
        if z>1:F.append((z,1))
        assert all(prime(q) for q,e in F),(h,F);P[h]=F
    return P
@cache
def fac(n):return tuple((int(p),int(e)) for p,e in zip(*pa.factor(n)))
@cache
def prime(n):return bool(pa.isprime(n))
def verifyfac(n,F):
    assert prod(q**e for q,e in F)==n and len(set(q for q,e in F))==len(F)
    assert all(e>=1 and prime(q) for q,e in F)
def calculate(h,base=None,unit_only=False):
    H=2**h-1
    if base is None:
        fs=hints()[h]; base=[[q,e,fac((q-1)*q**(e-1))] for q,e in fs]
    verifyfac(H,[(q,e) for q,e,_ in base]); blocks={}
    for q,e,F in base:
        n=q**e; o=(q-1)*q**(e-1);verifyfac(o,F)
        for l,v in F:blocks.setdefault(l,[]).append((n,o,v))
    ab=[(a,gcd(a,h)) for a in range(1,h) if a!=gcd(a,h) and (not unit_only or gcd(a,h)==1)]
    vals=[((1+(1<<a))*pow(1+(1<<b),-1,H))%H for a,b in ab]
    I=1
    for l,bl in blocks.items():
        if len(bl)==1 and any(pow(x,bl[0][1]//l,bl[0][0])!=1 for x in vals):continue
        # Test index at l using only a quotient killed by l^2. Index < l^2 there
        # determines the exact primary index by the structure theorem.
        M=l*l; rows=[];orders=[];gens=[];logs=[]
        for n,o,v in bl:
            m=l**min(v,2);orders.append(m);t=o//m;g=2
            while gcd(g,n)!=1 or pow(g,o//l,n)==1:g+=1
            g=pow(g,t,n);gens.append((g,m,t,n));logs.append({1:0})
        rows=[[orders[i] if i==j else 0 for j in range(len(bl))] for i in range(len(bl))]
        def ix():
            G=pa.matrix(len(bl),len(rows[0]),sum(rows,[]))
            return int(pa.matdet(pa.mathnf(G)))
        for k,x in enumerate(vals,1):
            for i,(g,m,t,n) in enumerate(gens):
                y=pow(x,t,n);D=logs[i]
                if y not in D:
                    z=int(pa.znlog(pa.Mod(y,n),pa.Mod(g,n),m));assert pow(g,z,n)==y;D[y]=z
                rows[i].append(D[y])
            if k in (3,8,16,32) and ix()==1:break
        v=ix();assert v<M,(h,l,v);I*=v
    return {'h':h,'index':I,'factors':base}
if __name__=='__main__':
    if sys.argv[1]=='check':
        rows=json.loads((root.parent/'indices.json').read_text());counts={}
        assert [data['h'] for data in rows]==list(range(3,400,2))
        for data in rows:
            h=data['h'];res=calculate(h,data['factors']);assert res==data
            assert res['index']==(6 if h%9==0 else 2 if h%3==0 else 1)
            counts[res['index']]=counts.get(res['index'],0)+1
        print(len(rows),counts)
    else:
        root.mkdir(exist_ok=True)
        for h in map(int,sys.argv[1:]):
            f=root/f'{h:03}.json'
            if not f.exists():
                res=calculate(h);f.write_text(json.dumps(res,separators=(',',':'))+'\n');print(h,res['index'],flush=True)
