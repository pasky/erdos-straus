"""R280 from-scratch check of O269 Cor K1.
(1) T1 cancellation: for 4 | t, D^-_t(t m^2 + 1) = 0 (no divisor = -1 mod t) -- tested for ALL m (odd and even).
(2) sizes: frakE, frakO, frakB, R, N- at odd squares 317^2..323^2 and the first 12 primes > 1e5, split by t mod 4.
Usage: python review_r280_corK1.py [tmax1=400] [mmax=3000] [nprimes=12]
"""
import sys
from sympy import factorint, isprime, jacobi_symbol

tmax1 = int(sys.argv[1]) if len(sys.argv) > 1 else 400
mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
npr = int(sys.argv[3]) if len(sys.argv) > 3 else 12


def divs(N):
    ds = [1]
    for p, e in factorint(N).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


# (1) direct: smallest divisor search is expensive; use the structural fact via factorisation for t <= 64,
# and a cheap Jacobi-symbol proof check for all t <= tmax1: for d | t m^2 + 1 with d = -1 (t), (-t/d) must be 1.
fails = 0
for t in range(4, 65, 4):
    for m in range(1, 801):
        N = t * m * m + 1
        if any(d % t == t - 1 for d in divs(N)):
            fails += 1
print(f"(1a) 4|t<=64, 1<=m<=800 (odd and even m): tm^2+1 with a divisor = -1 mod t: {fails}")
fails = 0
for t in range(4, tmax1 + 1, 4):
    for d in range(t - 1, 200 * t, t):  # all d = -1 mod t up to 200t
        if jacobi_symbol((-t) % d, d) == 1:
            fails += 1
print(f"(1b) 4|t<={tmax1}: d = -1 mod t (d<200t) with (-t/d)=+1: {fails}  (must be 0 for the proof)")


def split(n):
    tmax = (n + 4) // 4
    E = {r: 0.0 for r in range(4)}; O = {r: 0.0 for r in range(4)}; B = 0; R = 0; Nm = 0
    for t in range(2, tmax + 1):
        N = t * n + 1
        ds = divs(N)
        Dm = sum(1 for d in ds if d % t == (t - 1) % t)
        Dp = sum(1 for d in ds if d % t == 1 % t)
        beta = 2 * ((n + 1) % (t - 1) == 0) - (n == t - 2)
        E[t % 4] += (Dm + Dp - 2) / 2
        O[t % 4] += (Dm - Dp + 2) / 2
        B += beta
        for d in ds:
            if d % t == (t - 1) % t and d >= 2 * t - 1 and N // d >= 2 * t - 1:
                R += 1
                if jacobi_symbol(d % n, n) == -1:
                    Nm += 1
    return E, O, B, R, Nm


def show(tag, n):
    E, O, B, R, Nm = split(n)
    Et, Ot = sum(E.values()), sum(O.values())
    assert abs(Et + Ot - B - R) < 1e-9, (n, Et, Ot, B, R)
    print(f"{tag} n={n}: E={Et:.1f} O={Ot:.1f} B={B} R={R} N-={Nm} | E_(4|t)={E[0]:.1f} O_(4|t)={O[0]:.1f}"
          f" | O by t mod 4: {[round(O[r],1) for r in range(4)]} | t=2 elif-bias tau(2n+1)/2={len(divs(2*n+1))/2}")
    return Et, Ot, B, R


for m in (317, 319, 321, 323):
    show("sq", m * m)
ps, p = [], 100000
while len(ps) < npr:
    p += 1
    if isprime(p):
        ps.append(p)
acc = [0, 0, 0, 0]
for p in ps:
    r = show("pr", p)
    acc = [a + b for a, b in zip(acc, r)]
print("mean over primes: E=%.2f O=%.2f B=%.2f R=%.2f" % tuple(a / len(ps) for a in acc))
