"""R205 from-scratch check of LENGTH_THREE §6: pentagons with sides (Q^2,1,1,1,n), lam24 = 4.

Usage: PYTHONPATH=scripts uv run python scripts/review_l3_side.py NMAX QMAX
Enumerates ALL positive integer solutions (c, s, h, h') of the five Ptolemy relations by brute force over c
(no use of the divisor parametrisation), compares with {h | 4n+Q^2, h = 3 mod 4}, checks the Egyptian identity
and ES^(S) membership (Q^2/(cn) in lowest terms has Q^2 | denominator-free part, i.e. gcd(cn, Q) = 1).
Also tests whether the claimed bijection needs Q odd (Q even control).
"""
import sys
from fractions import Fraction as F
from math import gcd


def solutions(n, Q):
    out = []
    Q2 = Q * Q
    c = 1
    while True:
        h = 4 * c - Q2
        if h > 4 * n + Q2:  # h h' = Q^2 + 4n with h' >= 1
            break
        if h >= 1 and (n + c) % h == 0:
            s = (n + c) // h
            hp = 4 * s - 1
            if hp >= 1 and h * hp == Q2 + 4 * n and c * hp == Q2 * s + n:
                out.append((c, s, h, hp))
        c += 1
    return out


def main():
    NMAX = int(sys.argv[1]); QMAX = int(sys.argv[2])
    tot = 0; fails = []; esS_bad = 0; even_mismatch = 0
    for n in range(1, NMAX + 1, 2):
        for Q in range(1, QMAX + 1):
            sols = solutions(n, Q)
            divs = sorted(h for h in range(1, 4 * n + Q * Q + 1) if (4 * n + Q * Q) % h == 0 and h % 4 == 3)
            if Q % 2 == 0:
                if sorted(x[2] for x in sols) != divs:
                    even_mismatch += 1
                continue
            tot += len(sols)
            if sorted(x[2] for x in sols) != divs:
                fails.append(("bij", n, Q))
            for c, s, h, hp in sols:
                if F(4, n) != F(1, s * n) + F(1, s * c) + F(Q * Q, c * n):
                    fails.append(("id", n, Q, c, s))
                if gcd(n, Q) == 1 and gcd(c * n, Q) != 1:
                    esS_bad += 1
    print(f"odd n<={NMAX}, odd Q<={QMAX}: pentagons={tot} fails={len(fails)} {fails[:5]}; "
          f"ES^(S) gcd violations (gcd(n,Q)=1): {esS_bad}; even-Q (n,Q) with bijection mismatch: {even_mismatch}")


if __name__ == "__main__":
    main()
