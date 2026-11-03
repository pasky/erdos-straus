"""Independent bounded checks for the z54 HCKILL review (not a proof of EH).
Run: ulimit -v 6000000; timeout 120s uv run --with sympy --with cypari2 --with mpmath python scripts/z54_xrev_hckill_check.py
PARI stack: 128 MB; prime sieve: 10 MB; no large Cartesian products.
"""
from fractions import Fraction
from math import gcd, isqrt, log, exp, cosh

import mpmath as mp
import sympy as sp
from cypari2 import Pari


def primes_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p::p] = b"\x00" * ((n-p*p)//p+1)
    return (p for p in range(2, n+1) if sieve[p])


# Factor individual shifts, independently of the branch's progression sieve.
counts = {10**5: 0, 10**6: 0}
for p in primes_to(10**6):
    if p % 8 == 1 and all(q % 4 == 1 for n in (p+4, 4*p+1) for q in sp.factorint(n)):
        for bound in counts:
            counts[bound] += p <= bound
print("independent factored census:", counts)

# F1 converse: the primitive character and its induced character are different at 5.
a, delta, line = 5, 39600, 20
endpoint, level = delta+4*a*line, line*(line*delta+4*a)
assert endpoint == 200**2 and level == 3980**2
# Integrality forces y=10t; odd t gives p=1 mod 8, but p+20 always has a factor 5.
assert all((y*y+delta) % (4*a) != 0 or y % 10 == 0 for y in range(20))
for t in range(1, 200, 2):
    p = 5*t*t+1980
    assert p % 8 == 1 and (p+20) % 5 == 0
    if t % 199:
        assert all(q % 4 == 1 for n in (p+20, 20*p+1) for q in sp.factorint(n))
print("F1 counterexample: x=20, a=5, delta=39600; D_e=D_l=-4; all integral p divisible by 5")
print("sample t=1: p=1985, shifts", sp.factorint(2005), sp.factorint(39701))

# Check the square-class cover and elliptic curve without partial factorization.
U, W = sp.symbols("U W")
aa, dd = (U**2-W**2)/15, (16*W**2-U**2)/15
assert sp.expand(dd+28*aa-(9*U**2-4*W**2)/5) == 0
assert sp.expand(7*(7*dd+4*aa)-7*(36*W**2-U**2)/5) == 0
forms = [9*U**2-4, 36-U**2, 31*U**2-16, 31-U**2]
assert all(sp.gcd(f, sp.diff(f, U)) == 1 for f in forms)
assert all(sp.gcd(forms[i], forms[j]) == 1 for i in range(4) for j in range(i))
print("multiquadratic cover: degree=16, simple branch points=8, genus=", 1+(-32+64)//2)
pari = Pari()
pari.allocatemem(128_000_000)
E = pari.ellinit([0, 532, 0, -1599360, 553190400])
print("E7 rank bounds, conductor, torsion:", pari.ellrank(E), pari.ellglobalred(E)[0], pari.elltors(E))
H = [480, -4320]
print("3H:", pari.ellmul(E, H, 3), "height:", pari.ellheight(E, H))
torsion = [[0], [-1680, 0], [560, 0], [588, 0]]
seen, real, witnesses = set(), 0, []
small_primes = list(primes_to(10**6))
for n in range(-16, 17):
    for T in torsion:
        P = pari.elladd(E, pari.ellmul(E, H, n), T)
        if P == [0] or P[0] == 0:
            continue
        xx = Fraction(int(pari.numerator(P[0])), int(pari.denominator(P[0])))
        m = 1-672/xx
        nn, de = m.numerator, m.denominator
        u, w = abs(4*(5*nn*nn-5*nn*de-de*de)), 5*nn*nn+de*de
        common = gcd(u, w)
        u, w = u//common, w//common
        if (u, w) in seen:
            continue
        seen.add((u, w))
        if not w < u < 4*w:
            continue
        real += 1
        A, B = u*u-w*w, 16*w*w-u*u
        scale = (1 if gcd(A, B) % 3 == 0 else 3)*(1 if gcd(A, B) % 5 == 0 else 5)
        a, delta = scale*scale*A//15, scale*scale*B//15
        assert isqrt(delta+a)**2 == delta+a
        assert isqrt(delta+16*a)**2 == delta+16*a
        # Rational square tests, no factorization of the huge forms.
        for value in (Fraction(9*u*u-4*w*w, 35), Fraction(36*w*w-u*u, 5)):
            assert isqrt(value.numerator)**2 == value.numerator
            assert isqrt(value.denominator)**2 == value.denominator
        bad = next(q for q in small_primes if q > 2 and a % q == 0 and delta % q and pow(-delta, (q-1)//2, q) == q-1)
        witnesses.append((n, bad))
print("E7 distinct ratios:", len(seen), "real:", real, "nonintegrality witnesses:", witnesses)

# Independent Euler products; convergence error O(1/cutoff), not an asymptotic proof.
log_k2, log_singular = -log(8), log(9/8)
for q in primes_to(10**7):
    if q % 4 == 3:
        log_k2 += log(1-1/(q*q))
        if q >= 7:
            log_singular += log(q*q*(q-3)/(q-1)**3)
K, singular = exp(log_k2/2), exp(log_singular)
C = 4*K*K*singular
print("K, singular series, C:", K, singular, C)
mp.mp.dps = 30
for x, count in [(10**5, 295), (10**10, 7962940), (10**11, 65618311)]:
    integrand = lambda u: mp.exp(u)/(u*mp.sqrt(mp.log(mp.exp(u)+4)*mp.log(4*mp.exp(u)+1)))
    prediction = C*mp.quad(integrand, [mp.log(2), mp.log(x)])
    print("observed/predicted (input count):", x, float(count/prediction))
print("vector-sieve threshold:", cosh(0.5)**2)
