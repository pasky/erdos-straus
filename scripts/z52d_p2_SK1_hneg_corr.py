# z52d pass2 SK1 (Z0815): does h(-4p) (imag. quadratic proxy; NOT h(Q(sqrt p))) predict hardness at primes p<=1e5?
# hardness: U(p) (count of unordered solutions, count.c m=4) and Cmin(p) ((star) least C), both residualised on log p.
import math, sys
import numpy as np
D='data/z52b/pass2/SK1/'
U={}
for l in open(D+'Z0707_count4_primes1e5.txt'):
    r=l.split(); U[int(r[0])]=int(r[1])
H={}
for l in open(D+'Z0815_hneg4p_1e5.txt'):
    p,h=map(int,l.split()); H[p]=h
CM={}; R={}
for l in open(D+'Z0815_star_1e5.txt'):
    pass
# Cmin from star output (only R0/BONLY lines are listed); recompute Cmin via words file is absent -> use BONLY/R0 status only
Rzero=set(int(l.split()[1]) for l in open(D+'Z0815_star_1e5.txt') if l.startswith('R0'))
Bonly=set(int(l.split()[1]) for l in open(D+'Z0815_star_1e5.txt') if l.startswith('BONLY'))
ps=sorted(set(U)&set(H))
def run(cls,label):
    xs=[];ys=[];zs=[]
    for p in ps:
        if p%4!=cls or p<=7: continue
        xs.append(math.log(p)); ys.append(math.log(U[p])); zs.append(math.log(H[p]))
    x=np.array(xs); y=np.array(ys); z=np.array(zs)
    A=np.vstack([np.ones_like(x),x]).T
    by=np.linalg.lstsq(A,y,rcond=None)[0]; ry=y-A@by
    bz=np.linalg.lstsq(A,z,rcond=None)[0]; rz=z-A@bz
    c=np.corrcoef(rz,ry)[0,1]
    print(f"{label}: n={len(x)} slope logU~logp={by[1]:.3f}  corr(resid logU, resid log h(-4p)) = {c:+.3f}")
    # quartile means of residual logU by h quartile
    q=np.quantile(rz,[0.25,0.5,0.75]); bins=np.digitize(rz,q)
    print("   mean resid logU by h-quartile:", [round(float(ry[bins==k].mean()),3) for k in range(4)])
run(1,"p=1 mod 4")
run(3,"p=3 mod 4")
rz=[p for p in ps if p%4==1 and p>7]
hz=[H[p] for p in Rzero if p in H]; print("R-zeros <=1e5 (p=1 mod 4):",sorted(Rzero)[:10],"h(-4p) at them:",[H[p] for p in sorted(Rzero) if p in H][:10])
print("mean h(-4p) at R-zeros:", round(float(np.mean([H[p] for p in Rzero if p in H])),2), " mean over p=1 mod4:", round(float(np.mean([H[p] for p in rz])),2))
