import csv, numpy as np, cypari2
pari=cypari2.Pari(); pari.allocatemem(10**9)
rows=[r for r in csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'),delimiter='\t')]
rows=[r for r in rows if int(r['mod4'])==1 and int(r['p'])>100 and int(r['p'])%8==1 and int(r['U'])>0]
P=np.array([int(r['p']) for r in rows]); U=np.array([float(r['U']) for r in rows]); lp=np.log(P.astype(float))
X=np.column_stack([np.ones(len(P)),lp,np.log(lp)]); y=np.log(U); res=y-X@np.linalg.lstsq(X,y,rcond=None)[0]
h24=np.array([int(pari.qfbclassno(-24*int(p))) for p in P])
l3=np.array([int(pari.kronecker(3,int(p))) for p in P]); l2=np.array([int(pari.kronecker(2,int(p))) for p in P]); l5=np.array([int(pari.kronecker(5,int(p))) for p in P])
for name,mask in [('all',np.ones(len(P),bool)),('(3/p)=+1',l3==1),('(3/p)=-1',l3==-1)]:
    d={int(c):round(float(res[mask&(h24%16==c)].mean()),3) for c in (0,4,8,12)}
    n={int(c):int((mask&(h24%16==c)).sum()) for c in (0,4,8,12)}
    print(name, d, n)
# residual by (2/p),(5/p) combos too
for name,mask in [('(5/p)=+1',l5==1),('(5/p)=-1',l5==-1)]:
    d={int(c):round(float(res[mask&(h24%16==c)].mean()),3) for c in (0,4,8,12)}
    print(name, d)
print('h24 mod 8 vs (3/p)? crosstab', {(int(a),int(b)): int(((h24%8==a)&(l3==b)).sum()) for a in (0,4) for b in (1,-1)})
