# z57 BFO §4.2 (Assessment): relative Burgess saving f(q,theta,r) = q^{-theta/r+(r+1)/(4r^2)} (log q)^{1/(2r)} with constant c=1.
import math
def f(lq, th, r): return math.exp(lq*(-th/r + (r+1)/(4*r*r)) + math.log(lq)/(2*r))
for th in (1/3, 0.4, 0.5):
    lq = math.log(1e10)
    best = min((f(lq, th, r), r) for r in range(2, 200))
    # smallest q (in decimal digits) with min_r f <= 1/2
    d = 10
    while min(f(d*math.log(10), th, r) for r in range(2, 400)) > 0.5: d += 1
    print(f"theta={th:.3f}: at q=1e10 min_r f = {best[0]:.3f} (r={best[1]}); min_r f <= 1/2 first at q ~ 1e{d}")
