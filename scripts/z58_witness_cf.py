"""z58 WITNESS §4: do (★) solutions sit on continued-fraction data of √p, or on two-square data p = a² + b²?
For each prime (z58_witness_sols output) compute
  * the convergents h_k/q_k of √p with q_k <= p (and h_k <= 2p),
  * the representation p = a² + b² (a odd, b even),
and count solutions (P, Q, C) for which some coordinate or modulus X ∈ {P, Q, C, 4PC−1, 4QC−1, 4PQ} equals a convergent
numerator/denominator, or divides one of a, b, a ± b (X > 1).  Compare hard (R <= 4) vs control rates per solution.
Usage: python3 z58_witness_cf.py hard_sols ctrl_sols PMIN"""
import sys, math
from math import isqrt

def conv_sqrt(p):
    a0 = isqrt(p); m, d, a = 0, 1, a0; h1, h0, k1, k0 = 1, a0, 0, 1
    S = {a0, 1}
    for _ in range(400):
        m = d * a - m; d = (p - m * m) // d; a = (a0 + m) // d
        h1, h0 = h0, a * h0 + h1; k1, k0 = k0, a * k0 + k1
        if k0 > p: break
        S.add(h0); S.add(k0)
    return S

def twosq(p):
    # Cornacchia via sqrt(-1) mod p
    for c in range(2, 200):
        if pow(c, (p - 1) // 2, p) == p - 1:
            x = pow(c, (p - 1) // 4, p); break
    a, b = p, x
    while b * b > p: a, b = b, a % b
    c = isqrt(p - b * b)
    return (b, c) if b % 2 else (c, b)

def load(fn, pmin):
    for line in open(fn):
        a, b = line.split(':'); p, k = map(int, a.split())
        if p >= pmin: yield p, [tuple(map(int, t.split(','))) for t in b.split()]

def rates(fn, pmin, shift=0):
    n = cf = ts = 0; prim = 0
    L = list(load(fn, pmin)); ps = [p for p, _ in L]
    for i, (p, sols) in enumerate(L):
        pp = ps[(i + shift) % len(ps)]   # shift > 0: null model, data of a different prime of similar size
        prim += 1; S = conv_sqrt(pp); a, b = twosq(pp); assert a * a + b * b == pp
        T = [a, b, a + b, abs(a - b)]
        for P, Q, C in sols:
            X = [P, Q, C, 4 * P * C - 1, 4 * Q * C - 1, 4 * P * Q]
            n += 1; cf += any(x in S for x in X if x > 1)
            ts += any(t % x == 0 for x in X if x > 2 for t in T)
    return prim, n, cf / n, ts / n

pm = int(sys.argv[3])
for nm, fn in (('hard', sys.argv[1]), ('ctrl', sys.argv[2])):
    for sh in (0, 1, 2):
        prim, n, r1, r2 = rates(fn, pm, sh)
        print(f"{nm} (shift {sh}{' = null: data of another prime' if sh else ''}): primes {prim}, solutions {n}; "
              f"frac with a coordinate/modulus = CF(√p) convergent term {r1:.4f}; "
              f"frac with a coordinate/modulus (>2) dividing a, b, a+b or |a-b| {r2:.4f}")
