# z53 HCHYP: lower tail of Z(X) = number of successful lines x in C, x <= X (E and L counted separately),
# from the .hc files of z53_hchyp_lines.c (columns: n HC Z64 Z256 Z1024 Z2048).
import sys, math
def pois_cdf(mu,j): return sum(math.exp(-mu+k*math.log(mu)-math.lgamma(k+1)) for k in range(j+1))
for fn in sys.argv[1:]:
    rows=[list(map(int,l.split())) for l in open(fn)]
    N=len(rows); L=sum(math.log(r[0]) for r in rows)/N
    hc=[(r[1] or 10**9) for r in rows]; mx=max(hc)   # 0 = censored (no success <= Xmax) -> 10**9
    print(f"== {fn}: N={N} mean log n={L:.2f}  max HC={mx} (n={rows[hc.index(mx)][0]})  maxHC/log n={mx/L:.2f}  maxHC/(log n)^1.386={mx/L**1.386:.2f}")
    for j,X in enumerate([64,256,1024,2048]):
        z=[r[2+j] for r in rows]; mu=sum(z)/N; var=sum((a-mu)**2 for a in z)/N
        if mu==0:
            print(f"  X={X:4d}: all Z = 0 (no successful line; e.g. odd squares, T1)"); continue
        zmin=min(z); q001=sorted(z)[int(0.001*N)]
        thr=int(mu/3); emp=sum(a<=thr for a in z)/N; po=pois_cdf(mu,thr)
        print(f"  X={X:4d}: mean Z={mu:6.2f} var/mean={var/mu:5.2f} min Z={zmin:3d} (min/mean={zmin/mu:.2f}) q0.001={q001:3d}"
              f" | P(Z<=mean/3={thr})={emp:.2e} Poisson={po:.2e}  -logP/mean={(-math.log(emp)/mu) if emp>0 else float('inf'):.3f}")
