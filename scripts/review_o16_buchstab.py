"""R61 from-scratch check of OMEGA16 N1: ratio #{z<p<=x: p+h z-rough (odd primes 3..z) for all h in H}
/ (delta * (pi(x)-pi(z))), delta = prod_{3<=l<=z} (1 - nu_l/(l-1)), nu_l = #distinct classes -h mod l.
usage: review_o16_buchstab.py x u h1 [h2 ...]"""
import sys
import numpy as np


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


x, u = int(float(sys.argv[1])), float(sys.argv[2])
H = [int(a) for a in sys.argv[3:]]
z = int(round(x ** (1 / u)))
isp = sieve(x + max(H))
P = np.nonzero(isp)[0]
small = P[(P >= 3) & (P <= z)]
cand = P[(P > z) & (P <= x)]
ok = np.ones(len(cand), dtype=bool)
logdel = 0.0
for l in small.tolist():
    cls = {(-h) % l for h in H} - {0}  # only unit classes matter for primes p>z
    nu = len(cls)
    logdel += np.log1p(-nu / (l - 1))
    r = cand % l
    for c in cls:
        ok &= r != c
cnt = int(ok.sum())
print(f"x={x:.0e} u={u} z={z} H={H} count={cnt} ratio={cnt/(np.exp(logdel)*len(cand)):.4f}")
