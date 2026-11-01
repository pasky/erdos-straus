"""Exact reach of the square-sieve bound on the diagonal U=V (a=b, g=1-2b), and at the balanced block.
For each variant, the block bound exponent is max(terms) with r=r*(b,g) (balancing main and dual term); the sieve beats
the trivial exponent t=min(b,g) iff max(terms) < t and 0<r, 2r<g.  All terms are linear in b on the diagonal, so the
feasible set is an interval; we compute it exactly by scanning the breakpoints.
"""
from fractions import Fraction as F
def terms(b,g,kappa,third):
    if third:
        r=(F(7,6)*b-F(1,6)-g/2)/3
        T=[b-r,2*r+F(1,6)+g/2-b/6,r+b/6+g-F(1,6),3*r,b-g,b-2*r,F(1,6)+g/2-b/6-r,b/6+g-F(1,6)-r]
    else:
        r=((1+kappa)*b-kappa-g/2)/3
        T=[b-r,2*r+kappa+g/2-kappa*b,3*r,b-g,b-2*r,kappa+g/2-kappa*b-r]
    return r,max(T)
def ok(b,kappa,third):
    g=1-2*b; r,m=terms(b,g,kappa,third); return r>0 and 2*r<g and m<min(b,g)
def interval(kappa,third,N=20000):
    pts=[F(i,N) for i in range(1,N//2)]
    good=[b for b in pts if ok(b,kappa,third)]
    return (min(good),max(good)) if good else None
for name,k,third in [("Thm A (third-derivative)",None,True),("Bourgain (13/84,55/84)",F(13,84),False),("conjectural (0,1/2)",F(0),False)]:
    iv=interval(k,third)
    print(f"{name}: diagonal gain for b in [{float(iv[0]):.5f}, {float(iv[1]):.5f}] (grid 1/20000; endpoints are roots of linear eqs)")
    for b in [F(1,4),F(1,3)]:
        g=1-2*b; r,m=terms(b,g,k,third); print(f"    b={b}: r*={r} ({float(r):.4f}), sieve exponent={m} ({float(m):.5f}), trivial={min(b,g)}")
