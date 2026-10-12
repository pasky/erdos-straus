"""O153 W3 sanity check: odd squares n = m^2 lie in no ET class C_II(a,b,e) = {n = -e mod 4ab}, e | a+b,
nor C_I(a,b,e) = {ne = -1 mod 4ab}, e | a+b (no gcd conventions imposed).
Type II is exhaustive (4ab <= n+e forces e <= (n+4)/3); Type I is checked for e <= EMAX (scope stated).
Usage: PYTHONPATH=scripts uv run python scripts/bs_wild_squares.py MMAX EMAX
"""
import sys
from sympy import divisors


def hit(N, e):
    ds = divisors(N)
    for a in ds:
        M = N // a
        for b in divisors(M):
            if (a + b) % e == 0:
                return (a, b)
    return None


def main():
    MMAX = int(sys.argv[1]); EMAX = int(sys.argv[2])
    bad = []
    for m in range(1, MMAX + 1, 2):
        n = m * m
        for e in range(3, (n + 4) // 3 + 1, 4):
            h = hit((n + e) // 4, e)
            if h:
                bad.append(('II', m, e, h)); break
        for e in range(3, EMAX + 1, 4):
            h = hit((n * e + 1) // 4, e)
            if h:
                bad.append(('I', m, e, h)); break
    print(f"odd m <= {MMAX}: Type II exhaustive, Type I e <= {EMAX}; hits: {bad[:10]} (total {len(bad)})")


if __name__ == "__main__":
    main()
