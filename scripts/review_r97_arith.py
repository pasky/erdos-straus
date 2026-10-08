"""R97 from-scratch arithmetic checks for paper/es-mn-short-note.tex.

(1) Lemma identity: exact rational check of m/n = 1/(suw)+1/(nsvw)+1/(nuvw).
(2) Brute-force m-representability for small n, then:
    (a) every n in a forced class -u v^{-1} (mod k*l) with k*l+1 = m*u*v*w is representable;
    (b) smooth-part closure (Lemma smooth (a)): n exceptional => n' exceptional;
    (c) n = 1 exceptional for m >= 4; m <= 3 never exceptional (small n).
Written independently of the author's scripts.  EVIDENCE only.
"""
from fractions import Fraction
import math, random, sys

random.seed(97)


def divisors_of_square(b):
    # factor b by trial division, return divisors of b^2
    f = {}
    x = b
    p = 2
    while p * p <= x:
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        f[x] = f.get(x, 0) + 1
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(2 * e + 1)]
    return ds


def two_unit(a, b):
    """is a/b (reduced, >0) a sum of two unit fractions?  (a y - b)(a z - b) = b^2."""
    for d in divisors_of_square(b):
        if (d + b) % a == 0 and (b * b // d + b) % a == 0:
            return True
    return False


def representable(m, n):
    r = Fraction(m, n)
    # x <= y <= z: 1/x >= r/3, 1/x < r
    xlo = max(1, math.floor(1 / r) + 1) if r <= 1 else 1
    xhi = math.floor(3 / r)
    for x in range(xlo, xhi + 1):
        rest = r - Fraction(1, x)
        if rest <= 0:
            continue
        if two_unit(rest.numerator, rest.denominator):
            return True
    return False


def check_identity(trials=3000):
    bad = 0
    done = 0
    while done < trials:
        m = random.randint(2, 80)
        k = random.randint(1, 300)
        l = random.randint(1, 3000)
        A = k * l + 1
        if A % m:
            continue
        A //= m
        # random factorization A = u v w
        ds = [d for d in range(1, int(A ** 0.5) + 2) if A % d == 0]
        u = random.choice(ds)
        rest = A // u
        ds2 = [d for d in range(1, rest + 1) if rest % d == 0] if rest < 10 ** 5 else [1]
        v = random.choice(ds2)
        w = rest // v
        assert u * v * w * m == k * l + 1
        inv = pow(v, -1, k * l) if k * l > 1 else 0
        n0 = (-u * inv) % (k * l) if k * l > 1 else 0
        for n in [n0 + k * l * j for j in range(0, 4)]:
            if n < 1:
                continue
            assert (n * v + u) % (k * l) == 0
            s = (n * v + u) // (k * l)
            lhs = Fraction(m, n)
            rhs = Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w)
            if lhs != rhs:
                bad += 1
        done += 1
    return bad


def main():
    print("identity failures:", check_identity())
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    for m in [2, 3]:
        ex = [n for n in range(1, 300) if not representable(m, n)]
        print(f"m={m}: exceptional n<300: {ex}")
    for m in [4, 5, 6, 7, 8, 9, 12, 13]:
        rep = {n: representable(m, n) for n in range(1, NMAX + 1)}
        ex = [n for n in rep if not rep[n]]
        assert not rep[1]
        # (b) smooth closure for several y
        viol = 0
        for y in [2, 3, 5, 7, 11]:
            P = [p for p in range(2, y + 1) if all(p % q for q in range(2, p))]
            for n in ex:
                np_ = n
                for p in P:
                    while np_ % p == 0:
                        np_ //= p
                if rep[np_]:
                    viol += 1
        # (a) forced classes: enumerate k*l+1 = m*u*v*w with k*l <= NMAX, all n<=NMAX in class rep.
        forced_viol = 0
        nclasses = 0
        for kl in range(1, NMAX + 1):
            if (kl + 1) % m:
                continue
            A = (kl + 1) // m
            for u in range(1, A + 1):
                if A % u:
                    continue
                for v in range(1, A // u + 1):
                    if (A // u) % v:
                        continue
                    if math.gcd(v, kl) != 1:
                        continue
                    n0 = (-u * pow(v, -1, kl)) % kl if kl > 1 else 0
                    nclasses += 1
                    for n in range(n0 if n0 > 0 else kl, NMAX + 1, kl):
                        if not rep[n]:
                            forced_viol += 1
        print(f"m={m}: #exc<= {NMAX}: {len(ex)} (first {ex[:12]}), smooth-closure violations {viol}, "
              f"forced classes {nclasses}, forced-class violations {forced_viol}")


if __name__ == "__main__":
    main()
