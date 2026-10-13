"""R195: evaluate the explicit lower bound of FF_MUTE Thm 3.5 from scratch.
d*G(d) >= (delta - L_d) q^d - q^{d/2} [2 delta + 2^omega (D+1) + m_d (h-1)] - delta D,
delta = phi(q-1)/(c_q (q-1) Phi(A)), m_d = floor(d log q / log(2d+1)), L_d = (1 + ln m_d)/(2d), D = k + n + h.
Also checks the 'Lambda_d' claims (|Lambda_d| <= m_d, sum 1/ell <= L_d) exactly by factoring q^d - 1 (sympy)."""
import math
import sys
from fractions import Fraction
import sympy


def phi(n):
    return sympy.totient(n)


def omega(n):
    return len(sympy.factorint(n)) if n > 1 else 0


def bound(q, PhiA, k, h, n, d):
    cq = 2 if q % 2 else 1
    delta = phi(q - 1) / (cq * (q - 1) * PhiA)
    md = math.floor(d * math.log(q) / math.log(2 * d + 1))
    Ld = (1 + math.log(md)) / (2 * d) if md >= 1 else 0.0
    D = k + n + h
    return (delta - Ld) * q ** d - q ** (d / 2) * (2 * delta + 2 ** omega(q - 1) * (D + 1) + md * (h - 1)) - delta * D


def max_n(q, PhiA, k, h, d, nmax=10 ** 8):
    if bound(q, PhiA, k, h, 1, d) <= 0:
        return 0
    lo, hi = 1, nmax
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if bound(q, PhiA, k, h, mid, d) > 0:
            lo = mid
        else:
            hi = mid - 1
    return lo


def lambda_check(q, d):
    fac = sympy.factorint(q ** d - 1)
    Lam = [l for l in fac if (q - 1) % l]
    md = math.floor(d * math.log(q) / math.log(2 * d + 1))
    Ld = (1 + math.log(md)) / (2 * d) if md >= 1 else 0.0
    ok = all(l % (2 * d) == 1 for l in Lam) and len(Lam) <= md and float(sum(Fraction(1, l) for l in Lam)) <= Ld + 1e-15
    return ok, Lam, md, Ld


if __name__ == "__main__":
    primes = [p for p in range(3, 60) if sympy.isprime(p)]
    # (q, Phi(A), k, h, label)
    cases = [(3, 2, 1, 1, "q=3 A=T s=T+1"), (3, 4, 2, 1, "q=3 A=T^2"), (5, 4, 1, 1, "q=5 A=T"),
             (2, 1, 1, 1, "q=2 A=T"), (2, 4, 3, 1, "q=2 A=T^3"), (7, 6, 1, 1, "q=7 A=T"),
             (3, 2, 1, 3, "q=3 A=T s deg 3"), (4, 3, 1, 1, "q=4 A=T"), (9, 8, 1, 1, "q=9 A=T")]
    for (q, PhiA, k, h, lab) in cases:
        row = []
        for d in primes:
            m = max_n(q, PhiA, k, h, d)
            if m:
                row.append(f"d={d}: n<={m}")
            if len(row) >= 4:
                break
        print(lab, "| first primes d with bound>0 for some n:", "; ".join(row))
    bad = 0
    for q in [2, 3, 4, 5, 7, 8, 9, 11]:
        for d in primes:
            if q ** d > 10 ** 40:
                break
            ok, Lam, md, Ld = lambda_check(q, d)
            if not ok:
                bad += 1
                print("Lambda_d claim FAILS", q, d, Lam, md, Ld)
    print("Lambda_d checks (ell = 1 mod 2d, |Lambda_d| <= m_d, sum 1/ell <= L_d): failures", bad)
