"""z68 PC2: check that every ET Prop 1.9 family class gives a positive-integer solution of 4/n = 1/x+1/y+1/z
for EVERY positive integer n in the class (no size threshold), using ET Section 10's explicit N-points.
Type I core: 4abcd = n(a+b) + c, (x,y,z) = (abdn, acd, bcd); Type II core: 4abcd = a + b + nc, (x,y,z) = (abd, acdn, bcdn).
Random parameters; all n in the class up to NMAX.  Usage: python3 scripts/z68_pc2_validity.py TRIALS NMAX SEED
"""
import random, sys
from fractions import Fraction as Fr
from math import gcd

def chk(n, x, y, z):
    assert x > 0 and y > 0 and z > 0 and x.denominator == y.denominator == z.denominator == 1, (n, x, y, z)
    assert Fr(4, n) == 1 / x + 1 / y + 1 / z

def typeI(n, a, b, c, d):
    a, b, c, d = map(Fr, (a, b, c, d))
    assert 4 * a * b * c * d == n * (a + b) + c
    chk(n, a * b * d * n, a * c * d, b * c * d)

def typeII(n, a, b, c, d):
    a, b, c, d = map(Fr, (a, b, c, d))
    assert 4 * a * b * c * d == a + b + n * c
    chk(n, a * b * d, a * c * d * n, b * c * d * n)

def classes(rng):
    a, c, d, b = (rng.randint(1, 9) for _ in range(4))
    out = []
    # I-1
    N = 4 * a * a * d + 1
    f = rng.choice([q for q in range(1, N + 1) if N % q == 0])
    out.append(("I-1", 4 * a * d, (-f) % (4 * a * d), lambda n, a=a, d=d, f=f: typeI(
        n, a, Fr(n + f, 4 * a * d) * Fr(N, f) - a, Fr(n + f, 4 * a * d), d)))
    # I-2
    f = rng.randint(1, 40)
    if gcd(4 * a * c, f) == 1:
        from sympy.ntheory.modular import crt
        r, m = crt([4 * a * c, f], [(-f) % (4 * a * c), (-c * pow(a, -1, f)) % f if f > 1 else 0])
        out.append(("I-2", int(m), int(r), lambda n, a=a, c=c, f=f: typeI(
            n, a, Fr(n * a + c, f), c, Fr(n + f, 4 * a * c))))
    # I-3 (every root)
    f = rng.randint(1, 40)
    if gcd(4 * c * d, f) == 1:
        from sympy.ntheory.modular import crt
        for x in range(f):
            if (x * x + 4 * c * c * d) % f == 0 and gcd(x, f) == 1:
                r, m = crt([4 * c * d, f], [(-f) % (4 * c * d), x])
                out.append(("I-3", int(m), int(r), lambda n, c=c, d=d, f=f: typeI(
                    n, Fr(n + f, 4 * c * d), Fr(n * n + n * f + 4 * c * c * d, 4 * c * d * f), c, d)))
    # I-4, II-1
    e = rng.choice([q for q in range(1, a + b + 1) if (a + b) % q == 0])
    if gcd(e, 4 * a * b) == 1:
        out.append(("I-4", 4 * a * b, (-pow(e, -1, 4 * a * b)) % (4 * a * b), lambda n, a=a, b=b, e=e: typeI(
            n, a, b, Fr(a + b, e), Fr(n * e + 1, 4 * a * b))))
        out.append(("II-1", 4 * a * b, (-e) % (4 * a * b), lambda n, a=a, b=b, e=e: typeII(
            n, a, b, Fr(a + b, e), Fr(n + e, 4 * a * b))))
    # II-2
    t = rng.randint(1, 6)
    f = 4 * a * d * t - 1
    out.append(("II-2", f, (-4 * a * a * d) % f, lambda n, a=a, d=d, f=f: typeII(
        n, a, Fr(a + n * Fr(f + 1, 4 * a * d), f),
        Fr(f + 1, 4 * a * d), d)))
    # II-3
    e = rng.randint(1, 40)
    if gcd(4 * a * d, e) == 1:
        m = 4 * a * d * e
        out.append(("II-3", m, (-4 * a * a * d - e) % m, lambda n, a=a, d=d, e=e: typeII(
            n, a, Fr(n + e, 4 * a * d), Fr(n + 4 * a * a * d + e, 4 * a * d * e), d)))
    return out

def main():
    T, NMAX, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    cnt = {}
    for _ in range(T):
        for name, m, r, fn in classes(rng):
            if gcd(r, m) != 1:
                continue
            n = r if r > 0 else r + m
            while n <= NMAX:
                fn(n)
                cnt[name] = cnt.get(name, 0) + 1
                n += m
    print("all checks passed (every n >= 1 in the class, n <= %d); counts:" % NMAX, dict(sorted(cnt.items())))

if __name__ == "__main__":
    main()
