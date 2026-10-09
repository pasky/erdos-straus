"""R111 from-scratch sanity check of Thm 6.2's main term: for fixed d, count
N_d(q) = #{(a,f): A<=a<2A, F<=f<2F, f | 4a^2 d+1, q | 4acd - f}
and compare N_d(q)/N_d(1) with g_{c,d}(q) = prod_{l|q} g(l),
g(l) = (l-1)/(l^2+chi l) (l∤c), (1+chi)/(l+chi) (l|c), chi = (-d/l).
Sharp cut-offs (sanity only).  Divisors of 4a^2d+1 by sympy factorisation.
Usage: review_ttl_perd.py A d [d ...]
"""
import sys, math
from sympy import factorint, legendre_symbol, divisors

def g(l, c, d):
    chi = legendre_symbol((-d) % l, l)
    return (1 + chi)/(l + chi) if c % l == 0 else (l - 1)/(l*l + chi*l)

def run(A, d, cs=(1, 2, 3, 5), qs=(3, 5, 7, 11, 13, 17, 19, 23)):
    F = int(A * math.sqrt(d)) // 2       # f' = f in [F,2F]; needs F >= 8A
    pairs = []
    for a in range(A, 2*A):
        for f in divisors(4*a*a*d + 1):
            if F <= f < 2*F:
                pairs.append((a, f))
    n1 = len(pairs)
    print(f"d={d} A={A} F={F} (F/A={F/A:.1f}) N_d(1)={n1}  (d/A)^1/2={math.sqrt(d/A):.3f}")
    for c in cs:
        row = []
        for q in qs:
            if (2*d) % q == 0: continue
            nq = sum(1 for (a, f) in pairs if (4*a*c*d - f) % q == 0)
            pred = g(q, c, d) * n1
            row.append(f"q={q}:{nq}/{pred:.0f}({(nq-pred)/math.sqrt(pred+1):+.1f}sd)")
        print(f"  c={c}: " + "  ".join(row))

if __name__ == "__main__":
    A = int(sys.argv[1])
    for d in map(int, sys.argv[2:]):
        run(A, d)
