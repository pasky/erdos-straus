"""O211 (d): Type I dual Hasse window (O207 spark 1).
Type I certificate: f*g = p^2 + 4c^2 d with f = g = -p (mod 4cd) (the two cofactors are symmetric).
Hasse window for f prime: |1 - p| <= 2 sqrt f  <=>  g <= 4(p^2+4c^2 d)/(p-1)^2, i.e. g is tiny; then 4cd | p + g.
So window certificates = (g odd small, 4cd | p + g, g | p^2 + 4c^2 d, f = (p^2+4c^2d)/g prime).
Reports: #primes with a window certificate; does the trace-(1-p) curve over F_f have CM by Q(sqrt(-d))
(i.e. (1-p)^2 - 4f = -d * square)?  Odd squares n (T1): window-type solutions (should be none).
Usage: PYTHONPATH=scripts uv run python scripts/y3_typeI_hasse.py P"""
import sys, math
from sympy import isprime, primerange, divisors
from sympy.ntheory import factorint

def sqfree_kernel(n):
    s = 1
    for q, e in factorint(abs(n)).items():
        if e % 2: s *= q
    return s

def window(n, prime_f=True):
    out = []
    g = 1
    while True:
        # need g <= 4(n^2+4c^2 d)/(n-1)^2; c^2 d <= ((n+g)/4)^2, crude cap
        if g > 4*(n*n + ((n + g)//4)**2)/(n - 1)**2 + 1: break
        if (n + g) % 4 == 0:
            for m4 in divisors((n + g)//4):
                for c in divisors(m4):
                    d = m4//c; M = n*n + 4*c*c*d
                    if math.gcd(n, c*d*g) != 1: continue  # non-degenerate (automatic for n prime)
                    if M % g: continue
                    f = M//g
                    if (n - 1)**2 > 4*f: continue
                    if prime_f and not isprime(f): continue
                    out.append((c, d, g, f))
        g += 2
    return out

if __name__ == "__main__":
    P = int(sys.argv[1]); np_ = hit = cm = tot = 0; gs = {}
    for p in primerange(5, P):
        np_ += 1; w = window(p)
        if w: hit += 1
        for (c, d, g, f) in w:
            tot += 1; gs[g] = gs.get(g, 0) + 1
            D = (1 - p)**2 - 4*f
            if sqfree_kernel(D) == sqfree_kernel(d) and D < 0: cm += 1
    sq = sum(1 for m in range(3, int(P**.5) + 1, 2) if window(m*m, prime_f=False))
    print(f"P={P} primes={np_} with window Type I cert={hit} ({hit/np_:.3f}); certs={tot}, g-distribution={dict(sorted(gs.items())[:8])}")
    print(f"  certs whose trace-(1-p) curve has CM field Q(sqrt(-d)): {cm}/{tot}; odd squares with window solutions: {sq}")
