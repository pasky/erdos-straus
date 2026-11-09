"""NL7 Prop SG, part 2: which residue classes of t carry a *bounded-letter identity* with letter L = 4k^4 - 1
on n = t^4 + 1 (t even) that is NOT explained by a small Mordell-type congruence?
For each class r mod R (R = lcm(16, L) * k) we sample t ≡ r (mod R) with t ≡ 0 modulo every prime ell <= 13 not
dividing R (so n ≡ 1 mod those ell) and require n to be a nonzero square modulo the primes dividing R ("LC class");
Only "H-shaped" samples are used: both algebraic factors F1, F2 of n + L = (t^2+2kt+2k^2)(t^2-2kt+2k^2) are
(13-smooth) x (prime), so that every divisor of n + L is algebraic and a word with x = L or z = L exists iff a
polynomial identity does.  A class is reported if EVERY one of NS such samples has a U7 word with x = L or z = L.
"""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import factorint, primerange, isprime
from sympy.ntheory.modular import crt
from itertools import product

def divisors_from(facs):
    ds = [1]
    for p, e in facs.items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds

def smooth_cofactor(F):
    for ell in (2, 3, 5, 7, 11, 13):
        while F % ell == 0:
            F //= ell
    return F

def hshaped(t, k):
    F1, F2 = t*t + 2*k*t + 2*k*k, t*t - 2*k*t + 2*k*k
    return isprime(smooth_cofactor(F1)) and isprime(smooth_cofactor(F2))

def letter_words_xz(t, k):
    L = 4 * k**4 - 1
    n = t**4 + 1
    F1, F2 = t*t + 2*k*t + 2*k*k, t*t - 2*k*t + 2*k*k
    assert F1 * F2 == n + L
    fac = dict(factorint(F1))
    for p, e in factorint(F2).items():
        fac[p] = fac.get(p, 0) + e
    ds = divisors_from(fac)
    return words_with_x(n, L, ds) + words_with_z(n, L, ds)

def qr_unit(n, ell):
    if ell == 2:
        return n % 8 == 1
    return n % ell != 0 and pow(n, (ell - 1) // 2, ell) == 1

NS = 4
for k in (1, 2, 3, 4):
    L = 4 * k**4 - 1
    R = (16 * L // gcd(16, L)) * k
    Rprimes = [ell for ell in primerange(2, 100000) if R % ell == 0]
    Q = 1
    for ell in primerange(3, 14):
        if R % ell != 0:
            Q *= ell
    good = []
    nlc = 0
    for r in range(0, R, 2):
        n0 = r**4 + 1
        if not all(qr_unit(n0 % (8 if ell == 2 else ell), ell) for ell in Rprimes):
            continue
        nlc += 1
        t1 = int(crt([R, Q], [r, 0])[0])
        ok = True
        got = 0
        j = 0
        w = None
        while got < NS and j < 200000:
            j += 1
            t = t1 + R * Q * j
            if not hshaped(t, k):
                continue
            got += 1
            ww = letter_words_xz(t, k)
            if not ww:
                ok = False; break
            w = ww[0]
        if ok and got == NS:
            good.append((r, w))
    print(f"k={k} L={L} R={R}: LC classes of even t: {nlc}; classes where all {NS} H-shaped strong-LC samples have a letter-L U7 word (x or z): {len(good)}")
    for r, w in good[:12]:
        pos = 'x' if w[0] == L else 'z'
        print(f"    t ≡ {r} (mod {R})   [t mod L = {r % L}]  sample word position {pos}, y = {w[1]}")
