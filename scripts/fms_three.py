"""fms_three.py X — the three modulus-4 shots p+1, p+4, 4p+1 (FIXED_MODULUS_SHOTS Cor 2.3).

For every prime 5 <= p < X and (T1 control) every odd square n = m^2 < X, gcd(m,6)... (all odd m >= 3):
  shot fires iff N has a prime factor r = 3 mod 4 (h = r, cube point from Thm 2.1(a)); the ES solution
  is built from Lemma 1.1 and verified exactly (for primes).  Prints counts of failures of each shot
  and of all three jointly, plus the first few joint failures.
"""
import sys
from fractions import Fraction
import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 0:
            blk = s[i * i::i]
            blk[blk == 0] = i
            s[i * i::i] = blk
    idx = np.nonzero(s == 0)[0]
    s[idx] = idx
    return s


def prime3(N, spf):
    while N > 1:
        q = int(spf[N])
        if q % 4 == 3:
            return q
        while N % q == 0:
            N //= q
    return None


def build(p, shot, h):
    # cube point for divisor h of the shot (Thm 2.1(a))
    k = (h + 1) // 4
    if shot == "p+1":
        c, d, j = 1, k, 1
    elif shot == "p+4":
        c, d, j = 1, 1, k
    else:
        c, d, j = k, 1, 1
    assert (p * j + c) % h == 0
    e = (p + 4 * c * c * d) // h
    x = (p + e) // 4
    return x, p * c * d * j, p * x * j // c


def main():
    X = int(sys.argv[1])
    spf = spf_sieve(4 * X + 2)
    isprime = lambda n: spf[n] == n
    shots = {"p+1": lambda n: n + 1, "p+4": lambda n: n + 4, "4p+1": lambda n: 4 * n + 1}
    for label, pop in (("primes", [p for p in range(5, X) if isprime(p)]),
                       ("odd squares", [m * m for m in range(3, int(X ** 0.5) + 1, 2)])):
        fail = {s: 0 for s in shots}
        joint = []
        for n in pop:
            ok = False
            for s, f in shots.items():
                r = prime3(f(n), spf)
                if r is None:
                    fail[s] += 1
                    continue
                ok = True
                if label == "primes":
                    x, y, z = build(n, s, r)
                    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
            if not ok:
                joint.append(n)
        print(f"{label}: {len(pop)}; fail p+1/p+4/4p+1: {fail['p+1']}/{fail['p+4']}/{fail['4p+1']}; "
              f"all three fail: {len(joint)}; first: {joint[:12]}")


if __name__ == "__main__":
    main()
