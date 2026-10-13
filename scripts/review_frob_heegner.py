"""R196 from-scratch checks of FROBENIUS_FIRING §3 F1/F2 and Prop 1.2(a).
(F1) For primes 5 <= p < PMAX: the set of prime Type II moduli from a brute-force Type II enumeration
     (4/p = 1/x + 1/y + 1/z, p nmid x, p | y, p | z; modulus 4y' - 1 and 4z' - 1, y = p y', z = p z')
     equals {f prime : exists c, d >= 1, f | 1 + 4c^2 d p, f = -1 mod 4cd}; and for every such (f, c, d) there is
     t with t^2 = -dp mod f and 1 + 2ct = 0 mod f (degree-1 prime of Q(sqrt(-dp)) dividing 1 + 2c sqrt(-dp)),
     exactly one of the two roots t working.
(F2) (-d/f) = -1 at every certificate (c, d, f); for d in {1,2,3,7,11} the CM curves have #E(F_f) = f + 1.
(1.2a) max Type II modulus <= (p+1)(p+5)/4 (Type I bound not re-checked numerically).
usage: review_frob_heegner.py PMAX
"""
import sys
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return ds


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def typeII_moduli(p):
    """brute force: x with p/4 < x <= p/2 (p nmid x), e = 4x - p, e/x = 1/y' + 1/z'."""
    mods = set()
    for x in range(p // 4 + 1, p // 2 + 1):
        e = 4 * x - p
        # 1/y' + 1/z' = e/x  <=>  (e y' - x)(e z' - x) = x^2
        for D in divisors(x * x):
            if (x + D) % e == 0 and (x + x * x // D) % e == 0:
                y1 = (x + D) // e; z1 = (x + x * x // D) // e
                mods.add(4 * y1 - 1); mods.add(4 * z1 - 1)
    return mods


def F1_set(p, bound):
    out = {}
    c = 1
    while 4 * c * c * p + 1 <= 10 ** 12 and 4 * c - 1 <= bound:
        d = 1
        while 4 * c * d - 1 <= bound:
            N = 1 + 4 * c * c * d * p
            for f in divisors(N):
                if f > 2 and (f + 1) % (4 * c * d) == 0 and is_prime(f):
                    out.setdefault(f, []).append((c, d))
            d += 1
        c += 1
    return out


def count_points(coeffs, f):
    a1, a2, a3, a4, a6 = coeffs
    cnt = 1
    for x in range(f):
        for y in range(f):
            if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % f == 0:
                cnt += 1
    return cnt


CM = {1: (0, 0, 0, -1, 0), 3: (0, 0, 0, 0, 1), 2: (0, 4, 0, 2, 0), 7: (1, -1, 0, -2, -1), 11: (0, -1, 1, -7, 10)}
BAD = {1: {2}, 3: {2, 3}, 2: {2}, 7: {7}, 11: {11}}


def main(PMAX):
    ps = [p for p in range(5, PMAX) if is_prime(p)]
    mism = 0; nonunique = 0; legbad = 0; cm_checked = 0; cm_bad = 0; bound_bad = 0
    for p in ps:
        tm = {h for h in typeII_moduli(p) if is_prime(h)}
        allm = typeII_moduli(p)
        if max(allm, default=0) > (p + 1) * (p + 5) // 4:
            bound_bad += 1
        F1 = F1_set(p, (p + 1) * (p + 5) // 4)
        if set(F1) != tm:
            mism += 1; print("F1 mismatch", p, sorted(set(F1) ^ tm)[:10])
        for f, cds in F1.items():
            for (c, d) in cds:
                roots = [t for t in range(f) if (t * t + d * p) % f == 0]
                good = [t for t in roots if (1 + 2 * c * t) % f == 0]
                if len(roots) != 2 or len(good) != 1:
                    nonunique += 1
                if legendre(-d, f) != -1:
                    legbad += 1
                if d in CM and f >= 5 and f not in BAD[d] and f < 400:
                    cm_checked += 1
                    if count_points(CM[d], f) != f + 1:
                        cm_bad += 1
    print(f"primes 5<=p<{PMAX}: {len(ps)}; F1 set mismatches vs brute-force prime Type II moduli: {mism}; "
          f"root non-uniqueness: {nonunique}; (-d/f) != -1: {legbad}; CM point counts checked {cm_checked}, "
          f"#E != f+1: {cm_bad}; Type II modulus > (p+1)(p+5)/4: {bound_bad}")


if __name__ == '__main__':
    main(int(sys.argv[1]))
