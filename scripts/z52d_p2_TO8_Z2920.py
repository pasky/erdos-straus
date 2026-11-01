# z52d P2 TO8 Z2920: pigeonhole over complementary divisor sets for e-slices (FRONTIER §1 e-slice form).
# For prime p≡1(4), slice e≡-p (mod 4), e odd: N1=(p+e)/4 (Type II), N2=(pe+1)/4 (Type I).
# Div(N) = {d mod e : d | N, gcd(d,e)=1}. Pigeonhole fires if |Div(N1)|+|Div(N2)| > phi(e) (then Div(N1) ∩ -Div(N2) ≠ ∅).
# Certificate for slice e: -1 ∈ {a b^{-1} mod e : ab | N} with N=N1 (type II) or N2 (type I); checked exactly.
import sys, math
from math import gcd
def divisors(N):
    ds = [1]; x = N; q = 2
    while q * q <= x:
        if x % q == 0:
            e = 0
            while x % q == 0: x //= q; e += 1
            ds = [d * q ** k for d in ds for k in range(e + 1)]
        q += 1
    if x > 1: ds = [d * k for d in ds for k in (1, x)]
    return ds
def phi(n):
    r, x, q = n, n, 2
    while q * q <= x:
        if x % q == 0:
            while x % q == 0: x //= q
            r -= r // q
        q += 1
    if x > 1: r -= r // x
    return r
def Div(N, e):
    return {d % e for d in divisors(N) if gcd(d, e) == 1}
def cert(N, e):
    # exists a, b | N (ordered, gcd(ab,e)=1) with a b^{-1} ≡ -1 mod e  <=> a ≡ -b mod e, a,b | N
    D = {d % e for d in divisors(N) if gcd(d, e) == 1}
    return any(((-x) % e) in D for x in D)
def run(p, emax):
    fires = []; certs = []; best = (0, None)
    for e in range(3, emax + 1, 4):   # e ≡ 3 (mod 4) since p ≡ 1 (mod 4), e ≡ -p ≡ 3
        if gcd(e, p) != 1: continue
        if (p + e) % 4 or (p * e + 1) % 4: continue
        N1 = (p + e) // 4; N2 = (p * e + 1) // 4
        d1 = Div(N1, e); d2 = Div(N2, e); ph = phi(e)
        ratio = (len(d1) + len(d2)) / ph
        if ratio > best[0]: best = (ratio, e)
        if len(d1) + len(d2) > ph: fires.append(e)
        if cert(N1, e) or cert(N2, e): certs.append(e)
    return best, fires, certs
hard = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]
ctrl = [1009, 10009, 100049, 999029]
for p in hard + ctrl:
    best, fires, certs = run(p, int(sys.argv[1]) if len(sys.argv) > 1 else 10000)
    print(f"p={p}: max ratio {best[0]:.3f} at e={best[1]}; pigeonhole fires for {len(fires)} e (min {fires[:3]}); exact cert slices (any e<=cap): {len(certs)} e.g. {certs[:5]}")
