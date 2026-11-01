"""Exact (rational) verification of the exponent bookkeeping of Theorem A (and variants).
Block exponents: U=n^a <= V=n^b, W=n^g, a+b+g=1. Trivial bound: min(a,g) (a<=b).
Sieve with P=n^r, Q in (P^2,4P^2]:
  third-derivative version (Thm A):   terms  b-r, 2r+1/6+g/2-b/6, r+b/6+g-1/6, 3r, b-g, b-2r, (Sum w)/P terms
  exponent-pair version (kappa, lambda=kappa+1/2): terms b-r, 2r+kappa+g/2-kappa*b, 3r, b-g, b-2r, (Sum w)/P terms
Region where trivial > theta*: a>=theta*, g>=theta*, b=1-a-g>=a. All terms linear in (a,g) once r=r*(b,g) is linear,
so the max over the (closed) triangle is attained at a vertex.  We print all terms at all vertices and assert <= theta*,
plus side conditions 0 < r, 2r < g (Q <= W).
"""
from fractions import Fraction as F
def check(name, theta, kappa, third):
    verts=[]
    # triangle: a=theta,g=theta ; a=theta, g=1-2theta ; g=theta, a=(1-theta)/2
    for a,g in [(theta,theta),(theta,1-2*theta),((1-theta)/2,theta)]:
        b=1-a-g
        if third:
            r=(F(7,6)*b-F(1,6)-g/2)/3
            terms={'main b-r':b-r,'3rd-deriv 2r+1/6+g/2-b/6':2*r+F(1,6)+g/2-b/6,'3rd-deriv(2) r+b/6+g-1/6':r+b/6+g-F(1,6),
                   'Q^{3/2}: 3r':3*r,'V/W: b-g':b-g,'V/Q: b-2r':b-2*r,
                   'Sw/P: 1/6+g/2-b/6-r':F(1,6)+g/2-b/6-r,'Sw/P: b/6+g-1/6-r':b/6+g-F(1,6)-r}
        else:
            r=((1+kappa)*b-kappa-g/2)/3
            terms={'main b-r':b-r,'pair 2r+k+g/2-k b':2*r+kappa+g/2-kappa*b,'Q^{3/2}: 3r':3*r,'V/W: b-g':b-g,'V/Q: b-2r':b-2*r,
                   'Sw/P: k+g/2-k b-r':kappa+g/2-kappa*b-r}
        ok=all(v<=theta for v in terms.values()) and r>0 and 2*r<g
        print(f"[{name}] vertex a={a} b={b} g={g}: r*={r} ({float(r):.5f}); max term={max(terms.values())} ({float(max(terms.values())):.5f}); 0<r, 2r<g: {r>0 and 2*r<g}; OK={ok}")
        for k,v in terms.items(): print(f"      {k:32s} = {v} = {float(v):.5f}")
        assert ok
    print(f"[{name}] PASSED: every block has min(trivial, sieve) <= theta* = {theta} = {float(theta):.6f}\n")
check("Thm A (3rd-derivative test)", F(12,37), None, True)
k=F(13,84); check("Bourgain pair (13/84,55/84) [eps dropped]", 4/(13-4*k), k, False)
k=F(0); check("conjectural pair (0,1/2) [eps dropped]", 4/(13-4*k), k, False)
k=F(1,6); check("pair (1/6,2/3) via exponent-pair form", 4/(13-4*k), k, False)
