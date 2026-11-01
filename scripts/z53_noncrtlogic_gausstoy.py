#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- end-to-end toy check of Theorem T at the Gaussian trap family P = X^2 + 1.

Program PI_CF (bounded, uses the continued-fraction datum a_0 = floor(sqrt p) of sqrt p):
    q := floor(sqrt(p));  for e in (3, q-1, 2q-1):           # all = 3 mod 4 when 4 | q
        N := (p+e)/4; search coprime a, b with ab | N and e | a+b  (Type II e-slice certificate)
        if found: output the explicit solution 4/p = 1/N + 1/(pN(a+b)/(e a)) + 1/(pN(a+b)/(e b))
    otherwise FAIL.
At p = q^2 + 1 (q = 120 t) the windows factor formally as
    e = 3:     N = (q^2+4)/4 = 4*(q^2/16) + 1 ... formal prime r1 = q^2/4 + 1   (h = X^2 + 4, C = 4)
    e = q-1:   N = q(q+1)/4 = 30 * t * (q+1)                                   (h = X, X+1)
    e = 2q-1:  N = q(q+2)/4 = 60 * t * (q/2+1)                                 (h = X, X+2)
Formal family S = {X^2+1, X, X+1, X+2, X^2+4}; relevant primes for the trap (Lemma T4): 2 (from X+1),
5 (from X+2: 1+2i), 3 (from X^2+4: 1-4 = -3).  Trap point: q = 0 mod 8*3*5 = 120.
ADMISSIBLE t: t prime (t > 5), 120t+1, 60t+1, 3600t^2+1 (= q^2/4+1) and p = q^2+1 all prime.
Theorem T + Theorem M predict PI_CF(p) = FAIL at every admissible t (beyond a small threshold).
Controls: non-admissible t (p prime only) in the same class -- successes expected, and each success must use
a QNR prime (Lemma CT) coming from a composite formal value.

Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_gausstoy.py TMAX NCTRL
"""
import sys
from fractions import Fraction
import gmpy2
from sympy import factorint, primerange, divisors


def certificate(p, e):
    N = (p + e) // 4
    assert 4 * N == p + e
    divs = divisors(N)
    for a in divs:
        if gmpy2.gcd(a, e) != 1:
            continue
        for b in divisors(N // a):
            if gmpy2.gcd(a, b) != 1 or gmpy2.gcd(b, e) != 1:
                continue
            if (a + b) % e == 0:
                y = p * N * (a + b) // (e * a)
                z = p * N * (a + b) // (e * b)
                assert Fraction(4, p) == Fraction(1, N) + Fraction(1, y) + Fraction(1, z)
                return (N, y, z, a, b)
    return None


def run_pi(p):
    q = gmpy2.isqrt(p)
    for e in (3, q - 1, 2 * q - 1):
        e = int(e)
        if e % 4 != (-p) % 4 or e <= 0:
            continue
        c = certificate(p, e)
        if c is not None:
            return e, c
    return None


def has_qnr_factor(n, p):
    return any(gmpy2.jacobi(l, p) == -1 for l in factorint(n))


def main():
    TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000000
    NCTRL = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    adm = []
    ctrl = []
    for t in primerange(7, TMAX):
        q = 120 * t
        p = q * q + 1
        if not gmpy2.is_prime(p):
            continue
        if len(ctrl) < NCTRL:
            ctrl.append(t)
        if gmpy2.is_prime(120 * t + 1) and gmpy2.is_prime(60 * t + 1) and gmpy2.is_prime(3600 * t * t + 1):
            adm.append(t)
    print(f"TMAX={TMAX}: admissible t found: {len(adm)}")
    bad = 0
    for t in adm:
        q = 120 * t
        p = q * q + 1
        r = run_pi(p)
        if r is not None:
            bad += 1
            print("  ADMISSIBLE SUCCESS (contradicts Theorem T):", t, p, r)
    print(f"admissible: FAIL at {len(adm) - bad}/{len(adm)}; first few t = {adm[:10]}")
    succ = 0
    ct_ok = 0
    comp_ok = 0
    for t in ctrl:
        q = 120 * t
        p = q * q + 1
        r = run_pi(p)
        if r is None:
            continue
        succ += 1
        e, (N, y, z, a, b) = r
        if has_qnr_factor(N, p):
            ct_ok += 1
        # which formal values are composite?
        comps = [not gmpy2.is_prime(120 * t + 1), not gmpy2.is_prime(60 * t + 1),
                 not gmpy2.is_prime(3600 * t * t + 1)]
        idx = {3: 2, int(q - 1): 0, int(2 * q - 1): 1}[e]
        if comps[idx]:
            comp_ok += 1
    print(f"controls (p prime, same class, t prime, formal values unconstrained): {len(ctrl)}; successes {succ} "
          f"({succ / max(1, len(ctrl)):.3f}); success with QNR prime in N (Lemma CT, Type II x = N): {ct_ok}/{succ}; "
          f"success window's formal value composite: {comp_ok}/{succ}")


if __name__ == '__main__':
    main()
