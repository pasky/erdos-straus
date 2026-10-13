"""Legendre / SQUFOF midpoint factorisations as ES certificates? (O164 §3)

For N, expand sqrt(N) (principal cycle of disc 4N).  If the period l is even, the midpoint
ambiguous form gives a divisor g = gcd(N, Q_{l/2}) (Legendre's factorisation; trivial g in {1,N}
means negative-Pell-type / 2-power case).  We test whether {g, N/g} is an ES certificate:
  F1 (X-slice, N = t p + 1, t odd): need A in {g, N/g} with A = -1 mod t and 4 | A.
  F2 (Type II e-slice, N = (p+e)/4, e = 3 mod 4): need e | g + N/g  (a = g, b = N/g, ab = N).
Baseline: does ANY divisor pair of N work (same slice)?
Usage: python wr_legendre.py PMAX TMAX
"""
import sys
from math import isqrt, gcd
from sympy import divisors, isprime


def midpoint_divisor(N):
    r = isqrt(N)
    if r * r == N:
        return None
    P, Q, Qprev = 0, 1, N  # standard CF recurrence for sqrt(N)
    a0 = r
    Ps, Qs = [], []
    P, Q = 0, 1
    while True:
        a = (a0 + P) // Q
        P = a * Q - P
        Q = (N - P * P) // Q
        Ps.append(P)
        Qs.append(Q)
        if Q == 1:
            break
    l = len(Qs)
    if l % 2:
        return ("odd", None)
    # symmetric point: P_{l/2} = P_{l/2+1}; Q_{l/2 - 1} divides 2N
    Qm = Qs[l // 2 - 1]
    g = gcd(N, Qm)
    return ("even", g)


def main(pmax, tmax):
    ps = [p for p in range(25, pmax + 1, 24) if isprime(p)]
    stats = {"F1_mid": 0, "F1_any": 0, "F1_trials": 0, "F2_mid": 0, "F2_any": 0, "F2_trials": 0}
    first = {"F1_mid": [], "F1_any": [], "F2_mid": [], "F2_any": []}
    for p in ps:
        f1m = f1a = f2m = f2a = None
        for t in range(3, tmax + 1, 2):
            N = t * p + 1
            stats["F1_trials"] += 1
            mid = midpoint_divisor(N)
            ok_m = False
            if mid and mid[1]:
                g = mid[1]
                ok_m = any(A % 4 == 0 and (A + 1) % t == 0 for A in (g, N // g))
            ok_a = any(A % 4 == 0 and (A + 1) % t == 0 and (N // A + 1) % t == 0 for A in divisors(N))
            stats["F1_mid"] += ok_m
            stats["F1_any"] += ok_a
            if ok_m and f1m is None:
                f1m = t
            if ok_a and f1a is None:
                f1a = t
        for e in range(3, 4 * tmax, 4):
            N = (p + e) // 4
            stats["F2_trials"] += 1
            mid = midpoint_divisor(N)
            ok_m = bool(mid and mid[1] and (mid[1] + N // mid[1]) % e == 0)
            ok_a = any((d + N // d) % e == 0 for d in divisors(N))
            stats["F2_mid"] += ok_m
            stats["F2_any"] += ok_a
            if ok_m and f2m is None:
                f2m = e
            if ok_a and f2a is None:
                f2a = e
        first["F1_mid"].append(f1m)
        first["F1_any"].append(f1a)
        first["F2_mid"].append(f2m)
        first["F2_any"].append(f2a)
    print("primes", len(ps), stats)
    for k, v in first.items():
        print(k, "no success:", sum(x is None for x in v), "max first:", max((x for x in v if x), default=None))


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
