"""R48a: from-scratch check of O13 Lemma 3.1 (event classes are non-residues).

Part 1 (exhaustive, no symbols used): for every M<=N1, M=3 mod 4, and every D | A^2
(A=(M+1)/4), check that -4D is NOT a square modulo M (direct enumeration of x^2 mod M).
This is exactly the 'consequence': r a unit square mod every prime of M (odd M =>
square mod M) is never = -4D mod M.  Also checks (a): for each prime l|M,
(-4D | l) == (-d | l), computed by Euler's criterion.
Part 2: own Jacobi symbol, (-4D | M) == -1 for all atoms with M<=N2.
Part 3: simulate square-class quarantine states: random Q = prod l^{a_l} (a_l up to 4,
small primes incl. 3), random r a square mod each l^{a_l}; every atom with M | Q/8 must
have r != -4D mod M.
"""
import sys, random
import numpy as np


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


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def sqfree_part(D):
    s = 1
    for p, e in factor(D).items():
        if e % 2:
            s *= p
    return s


def jacobi(a, n):
    assert n > 0 and n % 2
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


def atoms(N):
    for M in range(3, N + 1, 4):
        A = (M + 1) // 4
        fA = factor(A)
        f2 = {p: 2 * e for p, e in fA.items()}
        for D in divisors_from(f2):
            yield M, D


def main():
    N1 = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    N2 = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
    # Part 1
    n1 = bad1 = bada = 0
    for M in range(3, N1 + 1, 4):
        sq = np.zeros(M, dtype=bool)
        x = np.arange(M, dtype=np.int64)
        sq[(x * x) % M] = True
        A = (M + 1) // 4
        fM = factor(M)
        f2 = {p: 2 * e for p, e in factor(A).items()}
        for D in divisors_from(f2):
            n1 += 1
            if sq[(-4 * D) % M]:
                bad1 += 1
                print("PART1 FAIL", M, D)
            d = sqfree_part(D)
            for l in fM:
                e1 = pow((-4 * D) % l, (l - 1) // 2, l)
                e2 = pow((-d) % l, (l - 1) // 2, l)
                if e1 != e2 or e1 == 0:
                    bada += 1
    print(f"Part1: {n1} atoms M<={N1}; -4D square mod M: {bad1}; (a) failures: {bada}")
    # Part 2
    n2 = bad2 = 0
    for M, D in atoms(N2):
        n2 += 1
        if jacobi(-4 * D, M) != -1:
            bad2 += 1
    print(f"Part2: {n2} atoms M<={N2}; Jacobi != -1: {bad2}")
    # Part 3
    random.seed(7)
    primes = [3, 5, 7, 11, 13, 17, 19, 23]
    bad3 = checked = 0
    for trial in range(3000):
        a = {l: random.choice([0, 0, 1, 1, 2, 3, 4]) for l in primes}
        Qodd = 1
        for l, e in a.items():
            Qodd *= l**e
        if Qodd == 1 or Qodd > 10**9:
            continue
        # r: CRT of random unit squares mod l^{a_l}
        r, mod = 0, 1
        for l, e in a.items():
            if e == 0:
                continue
            m = l**e
            while True:
                y = random.randrange(1, m)
                if y % l:
                    break
            s = y * y % m
            # CRT combine
            t = ((s - r) * pow(mod, -1, m)) % m
            r, mod = r + mod * t, mod * m
        # atoms with M | Qodd, M = 3 mod 4, M <= 10^6
        for M in divisors_from({l: e for l, e in a.items() if e}):
            if M % 4 != 3 or M > 10**6:
                continue
            A = (M + 1) // 4
            for D in divisors_from({p: 2 * e for p, e in factor(A).items()}):
                checked += 1
                if (r + 4 * D) % M == 0:
                    bad3 += 1
                    print("PART3 FAIL", M, D, r)
    print(f"Part3: {checked} (atom, random square-class Q) pairs with M|Q; fired: {bad3}")


if __name__ == "__main__":
    main()
