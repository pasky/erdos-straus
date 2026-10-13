"""gm_orbits.py — solutions of nA^2 + B^2 + D = 2*lam*D*A*B (GROWING_MUTE Prop 1.2) with A, B <= X.

A even, B odd, gcd(A,B)=1, gcd(B,n)=1. For each (A,B), divisors g = 2AB*lam - 1 of N = nA^2+B^2 are found by
scanning min(lam, D) <= sqrt(N/(2AB-1)) (lam*D ~ N/(2AB)). Prints, per n: #solutions, #with B squarefree and B>1,
whether n | lam ever occurs (Prop 1.2(c) says never for n ≡ 1 mod 4), and the (lam, D) pairs with their counts.
Usage: gm_orbits.py X n1 n2 ...
"""
import sys
from math import gcd, isqrt
from collections import Counter
import numpy as np
from sympy import factorint

X = int(sys.argv[1])
for n in map(int, sys.argv[2:]):
    sols = set()
    Bs_all = np.arange(1, X + 1, 2, dtype=np.int64)
    for A in range(2, X + 1, 2):
        Bs = np.array([b for b in Bs_all if gcd(int(b), A) == 1 and gcd(int(b), n) == 1], dtype=np.int64)
        if len(Bs) == 0:
            continue
        N = n * A * A + Bs * Bs
        M = 2 * A * Bs
        T = N // (M - 1)
        dmax = isqrt(int(T.max())) + 1
        for d in range(1, dmax + 1):
            # D = d
            ok = (N % d == 0) & (d <= T)
            if ok.any():
                g = N // d
                ok &= ((g + 1) % M == 0)
                for b in Bs[ok]:
                    gg = (n * A * A + int(b) ** 2) // d
                    sols.add((A, int(b), (gg + 1) // (2 * A * int(b)), d))
            # lam = d
            g = M * d - 1
            ok = (N % g == 0)
            for b in Bs[ok]:
                gg = 2 * A * int(b) * d - 1
                sols.add((A, int(b), d, (n * A * A + int(b) ** 2) // gg))
    for (A, B, lam, D) in sols:
        assert n * A * A + B * B + D == 2 * lam * D * A * B
    sqf = [s for s in sols if s[1] > 1 and all(e == 1 for e in factorint(s[1]).values())]
    es = [s for s in sols if s[1] == 1]
    nl = [s for s in sols if lam % n == 0] if False else [s for s in sols if s[2] % n == 0]
    pairs = Counter((s[2], s[3]) for s in sols)
    print(f"n={n} X={X}: solutions {len(sols)}, ES (B=1) {len(es)}, B>1 squarefree {len(sqf)}, n|lam: {len(nl)}, "
          f"distinct (lam,D) {len(pairs)}")
    print("  most common (lam,D):", pairs.most_common(8))
    print("  smallest B>1 sqfree sols:", sorted(sqf, key=lambda s: (s[1], s[0]))[:5])
