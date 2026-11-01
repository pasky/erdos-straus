# z52d pass2 SK1 (Z0833): split U(pq) into inherited (= U(p)+U(q): solutions of 4/(pq) with all denominators divisible by q, or by p)
# and non-inherited. Exact claim: the two inherited families are disjoint (all denominators divisible by pq would force
# 4 = 1/y1+1/y2+1/y3, impossible), so inherited = U(p)+U(q) exactly; non-inherited = U(pq)-U(p)-U(q) >= 0.
import math, statistics, collections
U={}
for l in open('data/z52b/pass2/SK1/Z0833_count4_all_3e4.txt'):
    r=l.split(); U[int(r[0])]=int(r[1])
isp=lambda n: n>1 and all(n%d for d in range(2,int(n**.5)+1))
primes=[p for p in U if p>1 and isp(p)]
P=set(primes)
rows=[]
for n in sorted(U):
    if n%2==0 or n<15: continue
    fac=[d for d in range(3,int(n**.5)+1,2) if n%d==0]
    if not fac: continue
    p=fac[0]; q=n//p
    if p not in P or q not in P: continue
    inh=U[p]+U[q]; new=U[n]-inh
    rows.append((n,p,q,U[n],U[p],U[q],inh,new))
print("odd semiprimes pq<=3e4 (p<q):",len(rows))
print("min non-inherited:",min(r[7] for r in rows)," negative count:",sum(1 for r in rows if r[7]<0))
print("zero non-inherited:",sum(1 for r in rows if r[7]==0),"of",len(rows))
fr=[r[7]/r[3] for r in rows if r[3]>0]
print("median fraction new/U(pq):",round(statistics.median(fr),3)," mean:",round(statistics.mean(fr),3))
# dependence of new count on U(p), U(q): median new by quartile of (U(p)+U(q))
rows.sort(key=lambda r: r[4]+r[5])
k=len(rows)//4
for i in range(4):
    seg=rows[i*k:(i+1)*k if i<3 else len(rows)]
    print(f"quartile {i} (U(p)+U(q) range {seg[0][4]+seg[0][5]}..{seg[-1][4]+seg[-1][5]}): median new={statistics.median([r[7] for r in seg])}, median new/U(pq)={round(statistics.median([r[7]/r[3] for r in seg]),3)}")
# both p and q hard (U small) : e.g. pq with p,q both in U-small primes
ex=[r for r in rows if r[0] in (5*13,3*5,5*17,13*17,5*29,3*7)]
for r in ex[:6]: print("example n=%d p=%d q=%d U(n)=%d U(p)=%d U(q)=%d new=%d"%(r[0],r[1],r[2],r[3],r[4],r[5],r[7]))
# regression of log new on log U(p), log U(q), log n (only new>0)
import numpy as np
S=[r for r in rows if r[7]>0]
X=np.array([[1,math.log(r[4]),math.log(r[5]),math.log(r[0])] for r in S]); y=np.array([math.log(r[7]) for r in S])
b=np.linalg.lstsq(X,y,rcond=None)[0]
print("log(new) ~ %.2f + %.3f log U(p) + %.3f log U(q) + %.3f log n  (n=%d, new>0)"%(b[0],b[1],b[2],b[3],len(S)))
