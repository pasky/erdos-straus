"""fms_affine.py A HMAX — check Theorem 2.1 (affine shot classification) of FIXED_MODULUS_SHOTS.md.

For every pair 1 <= alpha, beta <= A (gcd 1) and every h <= HMAX, h = 3 mod 4, gcd(h, 2*alpha*beta) = 1:
  certifies(h)  := exists c, j >= 1 with c*j | (h+1)/4 and h | alpha*c - beta*j
                   (= some prime/odd p with h | alpha p + beta has a cube point with divisor h);
  predicted(h)  := h = -1 mod 4M for some M in Mset(alpha, beta).
Asserts predicted => certifies; records certifies & not predicted (exceptions) and checks they are < 4 mu^5.
"""
import sys
from math import gcd, isqrt


def mset(a, b):
    g = gcd(a, b)
    c0, j0 = b // g, a // g
    out = {c0 * j0}
    if b % (4 * a) == 0:
        D = b // (4 * a)
        out |= {D // c for c in range(1, isqrt(D) + 1) if D % (c * c) == 0}
    if a % (4 * b) == 0:
        E = a // (4 * b)
        out |= {E // j for j in range(1, isqrt(E) + 1) if E % (j * j) == 0}
    return out


def divs(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return small + [n // d for d in reversed(small) if d * d != n]


def main():
    A, HMAX = int(sys.argv[1]), int(sys.argv[2])
    DIV = [None] * (HMAX // 4 + 2)
    nexc = npairs = 0
    worst = 0.0
    for a in range(1, A + 1):
        for b in range(1, A + 1):
            if gcd(a, b) != 1:
                continue
            npairs += 1
            mu = max(a, b)
            Ms = mset(a, b)
            exc = []
            for h in range(3, HMAX + 1, 4):
                if gcd(h, 2 * a * b) != 1:
                    continue
                k = (h + 1) // 4
                if DIV[k] is None:
                    DIV[k] = divs(k)
                cert = False
                for c in DIV[k]:
                    for j in DIV[k // c]:
                        if (a * c - b * j) % h == 0:
                            cert = True
                            break
                    if cert:
                        break
                pred = any((h + 1) % (4 * M) == 0 for M in Ms)
                assert not (pred and not cert), (a, b, h)
                if cert and not pred:
                    exc.append(h)
                    assert h < 4 * mu ** 5, (a, b, h)
            nexc += len(exc)
            if exc:
                worst = max(worst, max(exc) / mu ** 2)
            if a <= 4 and b <= 4:
                print(f"(alpha,beta)=({a},{b}) M-set={sorted(Ms)} exceptions={exc}")
    print(f"pairs {npairs}, total exceptions {nexc}, max exception/mu^2 = {worst:.2f}")


if __name__ == "__main__":
    main()
