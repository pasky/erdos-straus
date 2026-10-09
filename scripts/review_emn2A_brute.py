"""R102A from-scratch brute force: is m/p = 1/x + 1/y + 1/z solvable in positive integers?

Independent of PW's Type I/II parametrisation. Order x <= y <= z, so p/m < x <= 3p/m.
For each x, m/p - 1/x = A/B (reduced, A > 0); A/B = 1/y + 1/z  <=>  (Ay - B)(Az - B) = B^2
with Ay - B > 0, i.e. there is a divisor d of B^2 with d = -B (mod A) (then y = (d+B)/A,
z = (B^2/d + B)/A, and the cofactor is automatically = -B mod A since d * d' = B^2 = 0... checked
explicitly below).

Usage:
  review_emn2A_brute.py compare m P1 P2 stride  -> per-prime comparison with the author's C scanner
  review_emn2A_brute.py prop m N stride         -> representable proportion among primes p in (N/2,N], p not | m
"""
import subprocess
import sys
from math import gcd


def factor(n, out):
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def two_unit(A, B, fB):
    """A/B reduced, fB = factorisation of B. Is A/B = 1/y + 1/z, y,z >= 1?"""
    f2 = {p: 2 * e for p, e in fB.items()}
    BB = B * B
    for d in divisors_from(f2):
        if (d + B) % A == 0 and (BB // d + B) % A == 0:
            return True
    return False


def representable(m, p):
    lo = p // m + 1
    hi = (3 * p) // m
    for x in range(lo, hi + 1):
        num = m * x - p
        den = p * x
        if num <= 0:
            continue
        g = gcd(num, den)
        A, B = num // g, den // g
        f = factor(p, {})
        factor(x, f)
        fB = {}
        for q, e in f.items():
            # exponent of q in B = exponent in den minus exponent in g
            gg, eg = g, 0
            while gg % q == 0:
                gg //= q
                eg += 1
            if e - eg > 0:
                fB[q] = e - eg
        if two_unit(A, B, fB):
            return True
    return False


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes_in(P1, P2, m, stride):
    out, idx = [], 0
    for p in range(P1 + 1, P2 + 1):
        if isprime(p) and m % p:
            if idx % stride == 0:
                out.append(p)
            idx += 1
    return out


def main():
    mode = sys.argv[1]
    if mode == "compare":
        m, P1, P2, stride = map(int, sys.argv[2:6])
        ps = primes_in(P1, P2, m, stride)
        res = subprocess.run(["/tmp/r102a_scan", str(m), str(P1), str(P2), "2", str(stride)],
                             capture_output=True, text=True, check=True).stdout.split("\n")
        exc_author = {int(l.split()[1]) for l in res if l.startswith("E ")}
        mism = 0
        nexc = 0
        for p in ps:
            mine = not representable(m, p)
            nexc += mine
            if mine != (p in exc_author):
                mism += 1
                print("MISMATCH", m, p, "brute exc" if mine else "brute rep")
        print(f"m={m} ({P1},{P2}] stride={stride}: primes={len(ps)} exceptional={nexc} mismatches={mism}")
        sys.exit(1 if mism else 0)
    elif mode == "prop":
        m, N, stride = map(int, sys.argv[2:5])
        ps = primes_in(N // 2, N, m, stride)
        rep = sum(representable(m, p) for p in ps)
        print(f"m={m} N={N} primes={len(ps)} rep={rep} prop={rep/len(ps):.3f}")


if __name__ == "__main__":
    main()
