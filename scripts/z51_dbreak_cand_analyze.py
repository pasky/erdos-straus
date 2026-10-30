# Analyse top-band candidates: is X_top a mixed Poisson with intensity c*W(n), W(n) = sum over candidates of 1/log p?
import sys, math
rows=[tuple(map(float,l.split())) for l in open(sys.argv[1])]
n=len(rows)
C=[r[1] for r in rows]; X=[r[2] for r in rows]; W=[r[3] for r in rows]
mX=sum(X)/n; mW=sum(W)/n; c=mX/mW
P0=sum(1 for x in X if x==0)/n
varX=sum((x-mX)**2 for x in X)/n
pred_mixed=sum(math.exp(-c*w) for w in W)/n
pred_binom=None
print(f"samples {n}  E C_top {sum(C)/n:.2f}  E X_top {mX:.4f}  var/mean {varX/mX:.3f}  c=EX/EW {c:.3f}")
print(f"P(X_top=0) {P0:.5f} (+-{math.sqrt(P0*(1-P0)/n):.5f})  Poisson e^-EX {math.exp(-mX):.5f}  mixed-Poisson E e^(-cW) {pred_mixed:.5f}")
print(f"ratio actual/Poisson {P0/math.exp(-mX):.3f}  actual/mixed {P0/pred_mixed:.3f}")
# conditional on candidate-intensity deciles
srt=sorted(range(n),key=lambda i:W[i])
for d in range(10):
    idx=srt[d*n//10:(d+1)*n//10]
    p0=sum(1 for i in idx if X[i]==0)/len(idx); mx=sum(X[i] for i in idx)/len(idx); pm=sum(math.exp(-c*W[i]) for i in idx)/len(idx)
    print(f" W-decile {d}: W in [{W[idx[0]]:.2f},{W[idx[-1]]:.2f}]  E C {sum(C[i] for i in idx)/len(idx):.1f}  E X {mx:.3f}  P0 {p0:.5f}  mixed {pm:.5f}  ratio {p0/pm if pm>0 else float('nan'):.3f}")
print("lower tail of C_top: fraction with C_top <= k:", {k: sum(1 for x in C if x<=k)/n for k in (0,1,2,5,10,20,40)})
