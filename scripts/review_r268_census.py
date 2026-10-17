"""R268 from-scratch census of the b = 1 and c = 1 lines of Type II at primes p = 1 (mod 4).

Independent of scripts/s8_lines.c.  Algorithm: a residue-class SIEVE over all p at once, then a
complete per-p decision for the (few) primes the sieve leaves uncovered.

b = 1 line  (c p + a + 1 = 4acd, a, c, d >= 1).  Reviewer's re-derivation ("t-form"):
    exists t >= 1 and g | t + 1 with 4t | p + g      (c = (t+1)/g, d = (p+g)/(4t)).
  For p = 4i + 1 this needs g = 3 (mod 4) and i = -(g+1)/4 (mod t); d >= 1 is automatic.
  Completeness: g <= t + 1 and 4t <= p + g give t <= (p + 1)/3; and for t >= 1 the least residue
  g = (-p mod 4t) is the only candidate (g < 4t), so per p the decision is O(p) trivial ops.
c = 1 line  (p + a + b = 4abd).  For p = 4i + 1: a + b = 3 (mod 4), i = -(a+b+1)/4 (mod ab).
  Per-p completeness: WLOG a <= b; then 4ab <= p + a + b <= p + 2b gives a(4a - 2) <= p; for each such a,
  b runs over divisors of p + a (b | p + a since 4abd = p + a + b), checked exactly.
usage: python review_r268_census.py N T0
"""
import sys, time
import numpy as np
from sympy import divisors


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for q in range(2, int(n ** 0.5) + 1):
        if s[q]:
            s[q * q::q] = False
    return s


def b1_full(p):
    """complete decision of the b=1 line at p via t-form; returns least t or 0"""
    T = (p + 1) // 3
    step = 5_000_000
    for lo in range(1, T + 1, step):
        t = np.arange(lo, min(T, lo + step - 1) + 1, dtype=np.int64)
        g = (-p) % (4 * t)
        ok = (g > 0) & ((t + 1) % np.maximum(g, 1) == 0)
        if ok.any():
            return int(t[np.argmax(ok)])
    return 0


def c1_full(p):
    a = 1
    while a * (4 * a - 2) <= p:
        for b in divisors(p + a):
            if b >= a and (p + a + b) % (4 * a * b) == 0:
                return (a, b)
        a += 1
    return None


def main():
    N = int(sys.argv[1]); T0 = int(sys.argv[2])
    t0 = time.time()
    isp = primes_upto(N)
    I = N // 4 + 1
    idx = np.arange(I, dtype=np.int64)
    P = 4 * idx + 1
    pm = np.zeros(I, dtype=bool); pm[P <= N] = isp[P[P <= N]]
    pm[0] = False
    nprim = int(pm.sum())
    print(f"N={N}: primes p=1(4) <= N: {nprim}", flush=True)
    cb = np.zeros(I, dtype=bool)
    for t in range(1, T0 + 1):
        for g in divisors(t + 1):
            if g % 4 == 3:
                cb[(-(g + 1) // 4) % t::t] = True
    cc = np.zeros(I, dtype=bool)
    for a in range(1, int(T0 ** 0.5) + 1):
        for b in range(a, T0 // a + 1):
            if (a + b) % 4 == 3:
                m = a * b
                cc[(-(a + b + 1) // 4) % m::m] = True
    print(f"sieve done {time.time()-t0:.0f}s", flush=True)
    resb = P[pm & ~cb]; resc = P[pm & ~cc]
    print(f"b1 residual after sieve: {len(resb)}; c1 residual: {len(resc)}", flush=True)
    failb = [int(p) for p in resb if b1_full(int(p)) == 0]
    print("b1 FAILURES:", failb, flush=True)
    failc = [int(p) for p in resc if c1_full(int(p)) is None]
    print("c1 FAILURES:", failc, flush=True)
    print("intersection:", sorted(set(failb) & set(failc)))
    print(f"total {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
