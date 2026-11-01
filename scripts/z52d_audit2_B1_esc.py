# Z0773: ESC(p)/log^2 p vs U(p)/log^2 p, R(p)/log^2 p on dyadic windows of primes p≡1 (4).
# words file from scripts/z52b_fingerprint_words.c 3000000 | awk '{print $1,$6,$4,$5,$2,$3}'  (n ESC R Uv W I3)
import numpy as np, sys, json
from sympy import primerange
W=np.loadtxt(sys.argv[1],dtype=np.int64)
F=np.loadtxt('data/z52b/raw/f4_all_30000.txt',dtype=np.int64); G=np.loadtxt('data/z52b/raw/pr_20001_200000.txt',dtype=np.int64)
U={int(r[0]):int(r[1]) for r in F}; U.update({int(r[0]):int(r[1]) for r in G})
ps=np.array([p for p in primerange(5,3_000_001) if p%4==1])
L2=np.log(ps)**2
cols={'ESC':W[ps-1,1],'R':W[ps-1,2],'Uv':W[ps-1,3],'W':W[ps-1,4]}
uu=np.array([U.get(int(p),-1) for p in ps]); cols['U']=uu
out=[]
X=1000
while X<3_000_000:
    m=(ps>=X)&(ps<2*X)
    row={'X':X,'n':int(m.sum())}
    for k,v in cols.items():
        mm=m&(v>=0) if k=='U' else m
        if k=='U' and (2*X>200000): continue
        r=v[mm]/L2[mm]
        i=np.argmin(r); lv=np.log(np.maximum(v[mm],1))
        row[k]=dict(min=round(float(r.min()),4),argmin=int(ps[mm][i]),mean=round(float(r.mean()),4),minovermean=round(float(r.min()/r.mean()),3),sdlog=round(float(lv.std()),3))
    out.append(row); X*=2
for row in out:
    print(row['X'],row['n'],' | '.join(f"{k}: min {row[k]['min']} @{row[k]['argmin']} mean {row[k]['mean']} min/mean {row[k]['minovermean']} sdlog {row[k]['sdlog']}" for k in ['ESC','U','R','Uv'] if k in row))
# correlation ESC vs U on primes <=2e5
m=(uu>0)
print('spearman-ish corr log ESC vs log U (p<=2e5):',np.corrcoef(np.log(cols['ESC'][m]),np.log(uu[m]))[0,1])
print('ratio ESC/U mean',np.mean(cols['ESC'][m]/uu[m]),'min',np.min(cols['ESC'][m]/uu[m]),'max',np.max(cols['ESC'][m]/uu[m]))
json.dump(out,open('data/z52d/audit2/B1/esc_windows.json','w'),indent=0)
