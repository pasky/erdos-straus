# z69 TWIST I9, matched design (added after internal review): for each hard prime p (six Mordell classes),
# controls = the NC nearest primes below and the NC nearest above p in the SAME residue class mod 840
# (p + 840k, k = -1,-2,... / +1,+2,...).  Q(p) = [exists prime q | X with (840/q) = -1], p = X^2 + 840 Y^2.
# Stratified statistic: z = sum_i (Q(h_i) - cbar_i) / sqrt(sum_i cbar_i (1-cbar_i) (1 + 1/m_i)).
import sys, math
sys.path.insert(0,'scripts')
from sympy import isprime
from z69_twist_i9 import feat, load, MOR, sets
def run(NC):
    for name,fn in sets.items():
        H=[p for p in load(fn) if p%840 in MOR and isprime(p)]
        num=0.0; var=0.0; hq=0; ctot=0; cq=0; span=[]
        for p in H:
            ctl=[]
            for sgn in (-1,1):
                k=1; got=0
                while got<NC:
                    c=p+sgn*840*k; k+=1
                    if c<5: break
                    if isprime(c): ctl.append(c); got+=1
            q=[bool(feat(c)[2]) for c in ctl]; m=len(q); cb=sum(q)/m
            h=bool(feat(p)[2]); hq+=h; num+=h-cb; var+=cb*(1-cb)*(1+1/m); ctot+=m; cq+=sum(q)
            span.append(max(ctl)/p)
        print(f"{name}: n={len(H)} hard Q={hq/len(H):.3f}; class-matched controls ({ctot}, mean Q={cq/ctot:.3f}); stratified z={num/math.sqrt(var):+.2f}; "
              f"median (largest control)/p = {sorted(span)[len(span)//2]:.2f}")
if __name__=="__main__":
    run(int(sys.argv[1]))
