#!/usr/bin/env python3
"""Enumerate all length-3 words (t,u,v) of n = tuv-u-v <= N, n = 1 mod 4, and test the
local (2-adic) rule for the Jacobi symbol (A/n), A = tu-1.

Predicted rule (n = 1 mod 4):
  GOOD (A/n) = -1  iff
    t = 0 (4)                                  -> always
    t = 2 (4)                                  -> u or v in {0,3} mod 4
    t = 1 (4)                                  -> u or v = 0 mod 4
    t = 3 (4)                                  -> u or v even, or (u,v odd and t*n = 7 mod 8)
"""
import sys
from math import gcd, isqrt

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0

def predicted(t, u, v, n):
    tm, um, vm = t % 4, u % 4, v % 4
    if tm == 0:
        return -1
    if tm == 2:
        return -1 if (um in (0, 3) or vm in (0, 3)) else 1
    if tm == 1:
        return -1 if (um == 0 or vm == 0) else 1
    # tm == 3
    if u % 2 == 0 or v % 2 == 0:
        return -1
    return -1 if (t * n) % 8 == 7 else 1

def words(N):
    """yield (n, t, u, v) with n <= N, n = 1 mod 4, t,u,v >= 2."""
    for t in range(2, N // 4 + 2):
        for u in range(2, N + 1):
            # n = v(tu-1) - u <= N  -> v <= (N+u)/(tu-1)
            A = t * u - 1
            if 2 * A - u > N:
                break
            vmax = (N + u) // A
            for v in range(2, vmax + 1):
                n = v * A - u
                if n % 4 == 1:
                    yield n, t, u, v

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    bad = 0
    cnt = 0
    sq_good = 0
    for n, t, u, v in words(N):
        A = t * u - 1
        assert gcd(A, n) == 1
        j = jacobi(A, n)
        cnt += 1
        if j != predicted(t, u, v, n):
            bad += 1
            if bad < 10:
                print("MISMATCH", n, t, u, v, A, j, predicted(t, u, v, n))
        if isqrt(n) ** 2 == n and j == -1:
            sq_good += 1
    print(f"N={N} words={cnt} mismatches={bad} square_words_with_-1={sq_good}")

if __name__ == "__main__":
    main()
