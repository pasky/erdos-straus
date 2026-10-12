"""O153 W1: how many primes p = 1 (mod 4) have a fundamental unit of polynomial size, eps <= p^C?
Uses the continued fraction of sqrt(p); eps' = x + y sqrt(p) is the fundamental solution of x^2 - p y^2 = -1
(always solvable for prime p = 1 mod 4); eps' = eps_p or eps_p^3. Stops early once x > p^C.
Usage: PYTHONPATH=scripts uv run python scripts/bs_wild_units.py X C
"""
import sys
from math import isqrt, log
from sympy import primerange


def small_unit(p, C):
    """Return log(x + y sqrt p) for the fundamental solution if x <= p^C, else None."""
    a0 = isqrt(p)
    m, d, a = 0, 1, a0
    h_prev, h = 1, a0  # numerators
    k_prev, k = 0, 1   # denominators
    bound = p ** C
    while True:
        if h * h - p * k * k in (1, -1):
            return log(h + k * p ** 0.5)
        m = d * a - m
        d = (p - m * m) // d
        a = (a0 + m) // d
        h_prev, h = h, a * h + h_prev
        k_prev, k = k, a * k + k_prev
        if h > bound:
            return None


def main():
    X = int(sys.argv[1]); C = float(sys.argv[2])
    tot = 0; small = 0; ex = []
    for p in primerange(5, X + 1):
        if p % 4 != 1:
            continue
        tot += 1
        r = small_unit(p, C)
        if r is not None:
            small += 1
            if len(ex) < 12:
                ex.append(p)
    print(f"X={X} C={C}: primes p=1(4): {tot}; with eps' <= p^C: {small} "
          f"(ratio to sqrt(X)*log(X)^2: {small / (X ** 0.5 * log(X) ** 2):.3f}); first: {ex}")


if __name__ == "__main__":
    main()
