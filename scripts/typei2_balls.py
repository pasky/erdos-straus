"""O69 (POINTWISE_TYPEI2.md §2): 7-adic ball picture for r=7.

Fix every component of x* except x_7: x*_q = a_q for q in S' (q != 7), x*_q = W elsewhere, all of them
squares in Z_q^x (so the unforced slices are exactly those with v_7(c) odd, for any non-square x_7).
For an unforced slice (c,k) with v=v_7(ck), a certificate (c,k,F) holds at x* iff
  F | f_{c,k}  (fixed part of N away from 7; 7 never divides N since 7|c)  and  F = -x* mod 4ck/7^v,
  and then additionally x_7 = -F (mod 7^v).
So each certificate forbids one ball of radius 7^-v for x_7.  This script collects the balls of all
certificates with ck <= X and v <= L, and reports the surviving non-square classes of x_7 mod 7^L.

Usage: typei2_balls.py X L W [q:a:E ...]
"""
import sys
from collections import defaultdict
from math import gcd
from sympy import divisors, factorint
from typei2_formal import rep_mod, fixed_part


def main():
    X, L, W = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    x_S = {}
    for t in sys.argv[4:]:
        q, a, E = (int(u) for u in t.split(':'))
        assert q != 7
        x_S[q] = (a % q ** E, E)
    # squares check
    for q, (a, E) in x_S.items():
        assert (a % 8 == 1) if q == 2 else pow(a, (q - 1) // 2, q) == 1, f"component at {q} not a square"
    assert W % 8 == 1 and all(pow(W, (q - 1) // 2, q) == 1 for q in factorint(W) if q > 2 and q not in x_S) or True
    x_S7 = dict(x_S)
    balls = defaultdict(set)   # v -> set of x_7 classes mod 7^v
    wit = {}
    for P in range(7, X + 1, 7):
        for c in divisors(P):
            k = P // c
            a = 0
            cc = c
            while cc % 7 == 0:
                cc //= 7; a += 1
            if a % 2 == 0:
                continue
            v = 0
            pp = P
            while pp % 7 == 0:
                pp //= 7; v += 1
            if v > L:
                continue
            h = 4 * c * k
            h0 = h // 7 ** v
            x_S7[7] = (1, 1)   # dummy unit; 7 never divides N here, so irrelevant for fixed_part
            f = fixed_part(c, k, {q: x_S[q] for q in x_S}, W)
            f.pop(7, None)
            fval = 1
            for q, e in f.items():
                fval *= q ** e
            t0 = (-rep_mod(x_S7, W, h0)) % h0 if h0 > 1 else 0
            for D in divisors(fval):
                if D % h0 == t0 and gcd(D, h) == 1:
                    cls = (-D) % 7 ** v
                    if pow(cls, 3, 7) == 6:   # non-square mod 7
                        if cls not in balls[v]:
                            wit[(v, cls)] = (c, k, D)
                        balls[v].add(cls)
    # surviving classes
    surv = [b for b in range(7) if pow(b, 3, 7) == 6]
    for v in range(1, L + 1):
        if v > 1:
            surv = [s + 7 ** (v - 1) * d for s in surv for d in range(7)]
        surv = [s for s in surv if not any(s % 7 ** u in balls[u] for u in range(1, v + 1))]
        print(f"level {v}: balls {len(balls[v])}, surviving classes {len(surv)} of {3 * 7 ** (v - 1)}"
              f"  (fraction {len(surv) / (3 * 7 ** (v - 1)):.4f})")
        if len(surv) <= 6:
            print("   survivors:", surv)
        if not surv:
            break
    for v in range(1, min(L, 2) + 1):
        print(f"  level-{v} witnesses:", sorted((cls, wit[(v, cls)]) for cls in balls[v])[:12])


if __name__ == '__main__':
    main()
