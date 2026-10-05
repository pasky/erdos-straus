"""R48c from-scratch checks (independent of omega13_jacobi.py).

1. Lemma 3.1(b): for every atom (M,D) (M=3 mod 4, A=(M+1)/4, D | A^2), Jacobi(-4D|M) = -1.
   Lemma 3.1(a): Legendre(-4D|l) = Legendre(-d|l) for l | M, d = squarefree part of D.
2. Consequence: if r is a QR mod every prime of M (and coprime), r != -4D mod M.
3. Mordell-hard classes mod 840 (1,121,169,289,361,529) = squares of units mod 840.
4. Real characters mod Q (Q = 8 * odd squarefree-or-not) are all 1 at r when r = 1 mod 8
   and r is a QR mod every odd prime of Q (I3 Case A).
Usage: python review_o13c_jacobi.py MMAX
"""
import sys, random
from math import gcd


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def sqfree_part(D):
    s = 1
    for p, e in factor(D).items():
        if e % 2:
            s *= p
    return s


def main():
    MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    rng = random.Random(1)
    natoms = bad_b = bad_a = bad_cons = 0
    for M in range(3, MMAX + 1, 4):
        A = (M + 1) // 4
        fa = factor(A)
        fa2 = {p: 2 * e for p, e in fa.items()}
        primesM = list(factor(M))
        for D in divisors(fa2):
            natoms += 1
            if jacobi(-4 * D, M) != -1:
                bad_b += 1
            d = sqfree_part(D)
            for l in primesM:
                if jacobi(-4 * D, l) != jacobi(-d, l):
                    bad_a += 1
            # random r: QR unit mod each prime of M (lifted by CRT to mod M arbitrarily)
            for _ in range(2):
                # build r mod M: choose r = x^2 mod M with gcd(x,M)=1  -> QR mod every prime of M
                x = rng.randrange(1, M)
                while gcd(x, M) != 1:
                    x = rng.randrange(1, M)
                r = x * x % M
                # also non-square-mod-M but QR mod every prime: multiply by 1+M' tweaks not needed;
                if (r - (-4 * D)) % M == 0:
                    bad_cons += 1
    print(f"atoms with M<={MMAX}: {natoms}; Lemma3.1(b) failures {bad_b}; (a) failures {bad_a}; "
          f"consequence failures {bad_cons}")
    sq = sorted({x * x % 840 for x in range(840) if gcd(x, 840) == 1})
    print("unit squares mod 840:", sq, "== Mordell list:", sq == [1, 121, 169, 289, 361, 529])
    # 4: real characters mod Q. Real chars mod Q = products of chars mod 8 (4 of them) and
    # Legendre(.|p) for odd p | Q (the only nontrivial real char of (Z/p^a)^*).
    import itertools
    fails = 0
    for Q in [840, 840 * 11, 8 * 9 * 25 * 7 * 13, 8 * 27 * 5 * 49 * 11 * 17]:
        odd = [p for p in factor(Q) if p > 2]
        rs = [r for r in range(1, Q) if gcd(r, Q) == 1 and r % 8 == 1 and all(jacobi(r, p) == 1 for p in odd)]
        chars8 = [lambda n: 1, lambda n: (-1) ** ((n - 1) // 2 % 2), lambda n: 1 if n % 8 in (1, 7) else -1,
                  lambda n: 1 if n % 8 in (1, 3) else -1]
        # brute-force: enumerate all real characters mod Q as homomorphisms to ±1 = products above;
        # verify count equals 2^(#generators of 2-torsion of dual) = 4 * 2^len(odd)
        for c8 in chars8:
            for sub in itertools.product([0, 1], repeat=len(odd)):
                for r in rs[:200]:
                    v = c8(r)
                    for p, s in zip(odd, sub):
                        if s:
                            v *= jacobi(r, p)
                    if v != 1:
                        fails += 1
        # independent check of completeness: number of x with x^2=1 in (Z/Q)^* equals #real chars
        n2 = sum(1 for x in range(1, Q) if gcd(x, Q) == 1 and x * x % Q == 1)
        print(f"Q={Q}: #r={len(rs)}, #real chars listed={4 * 2 ** len(odd)}, #(2-torsion)={n2}")
    print("real-char(r)!=1 failures:", fails)


if __name__ == "__main__":
    main()
