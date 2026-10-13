"""O202: genus (local) vs class (global) for x^2 - N z^2 = -D, N = 4(lam^2 D^2 - n), D | lam D.

For each lam <= LAM: loc = primitive local solvability at all p (odd p | N: (-D/p) = 1; p = 2 brute force),
hit = global primitive solution (CF test from mk_fixedD).  Reports #lam, #loc, #hit, and asserts hit => loc.
Usage: mk_genus.py LAM n D [n D ...]
"""
import sys
from sympy import factorint
from mk_fixedD import solve


def loc2(N, D):
    # x odd; -D + N z^2 must be an odd 2-adic square, i.e. = 1 mod 8; N = 4M, so only z mod 2 matters.
    M = N // 4
    return D % 8 == 7 or M % 2 == 1


def local_ok(n, D, lam):
    m = lam * lam * D * D - n
    N = 4 * m
    for p in factorint(m):
        if p == 2:
            continue
        if pow((-D) % p, (p - 1) // 2, p) != 1:
            return False
    return loc2(N, D)


def main():
    LAM = int(sys.argv[1])
    args = list(map(int, sys.argv[2:]))
    for i in range(0, len(args), 2):
        n, D = args[i], args[i + 1]
        tot = loc = hit = 0
        for lam in range(1, LAM + 1):
            r = solve(n, D, lam)
            if r == "skip":
                continue
            tot += 1
            lo = local_ok(n, D, lam)
            h = r is not None
            assert not (h and not lo), (n, D, lam)
            loc += lo
            hit += h
        print(f"n={n:5d} D={D:4d}: lam<={LAM}: tested {tot}, locally ok {loc}, global {hit}, "
              f"P(global|local)={hit / max(loc, 1):.3f}")


if __name__ == "__main__":
    main()
