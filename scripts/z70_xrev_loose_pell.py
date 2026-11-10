"""Bounded independent local-null checks, loading only selected lane functions.
Max brute-force modulus is 200; no dense Cartesian-product arrays are allocated.
"""
import ast, gzip, json, math, pathlib, random, sys
import numpy as np
root=pathlib.Path(sys.argv[1]); env={'np':np,'CS':[-3,-2,-1,1,2,3],'SS':[-2,-1,0,1,2]}
for filename,names in [('z70_loose_pell.py',{'targets_T','null_prob'}),('z70_loose_pell_recal2.py',{'v2','null_prob_2adic'})]:
    tree=ast.parse((root/'scripts'/filename).read_text())
    funcs=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in names]
    exec(compile(ast.Module(body=funcs,type_ignores=[]),filename,'exec'),env)
def D(T,U,l):
    return U%l==0 or any((T+c*U+s)%l==0 for c in range(-3,4) for s in range(-2,3))
def brute(p,l):
    v=(l&-l).bit_length()-1;P=1<<(v+1);hits=total=0
    for T in range(l):
        for U in range(l):
            if (T*T-p*U*U+1)%l:continue
            if v and (T%min(4,1<<v) or (T*T-p*U*U+1)%P):continue
            total+=1;hits+=D(T,U,l)
    return hits/total
rng=random.Random(7070123)
ps=[17,41,73,89,97,113,137,193,233,241,257,281,313]
for i in range(160):
    p=rng.choice(ps);l=rng.randrange(5,201)
    expected=brute(p,l);actual=env['null_prob_2adic'](p,l)
    assert abs(actual-expected)<1e-14,(p,l,actual,expected)
print('160 independently enumerated local nulls: agreement (l <= 200).')
for p,l in ((9601,56),(28961,24),(59929,24),(241,22)):
    print('fixture',p,l,'plain',env['null_prob'](p,l),'lifted',brute(p,l),'lane',env['null_prob_2adic'](p,l))
# Check the stated S_v really is the reduction of a higher precision conic.
for p in ps[:6]:
    for v in range(1,7):
        N=1<<v;big=8*N
        roots={}
        for u in range(big):roots.setdefault(p*u*u%big,[]).append(u)
        projected={(t%N,u%N) for t in range(big) for u in roots.get((t*t+1)%big,[])}
        stated={(t,u) for t in range(N) for u in range(N) if t%min(4,N)==0 and (t*t-p*u*u+1)%(2*N)==0}
        assert projected==stated and len(stated)==1<<(v-1),(p,v)
print('36 lifted-set checks, v2=1..6: agreement.')
# Verify stored observed D without relying on the lane's Pell routine.
checked=0
for name in ('Htrain','Htest','CTRL'):
    recs=[json.loads(s) for s in gzip.open(root/f'data/z70/loose/pell_{name}_recal2.jsonl.gz','rt')]
    for rec in sorted(recs,key=lambda r:r['p'])[:10]:
        p=rec['p'];a0=math.isqrt(p);a=a0;mm=0;dd=1
        hm2,hm1,km2,km1=0,1,1,0
        for _ in range(100000):
            h=a*hm1+hm2;k=a*km1+km2
            if h*h-p*k*k==-1:break
            hm2,hm1,km2,km1=hm1,h,km1,k
            mm=dd*a-mm;dd=(p-mm*mm)//dd;a=(a0+mm)//dd
        else:raise RuntimeError('Pell limit')
        for row in rec['rows']:
            assert bool(row['D'])==D(h,k,row['l']);checked+=1
            for l,event,_ in row.get('dec',[]):assert bool(event)==D(h,k,l);checked+=1
print('Stored Pell D events independently checked:',checked,'(30 primes).')
