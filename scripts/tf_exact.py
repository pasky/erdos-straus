"""O194 TES_FINITE method A: COMPLETE list of solutions of TES(n): 9/n = w/x + w^2/y + 2/z, x,y,z = 1 mod 2,
using Cor 1.2: some coordinate x_i has N(x_i) <= N(c_i) N(n)/9; then (A x_j - B c_j)(A x_k - B c_k) = B^2 c_j c_k,
A = 9 x_i - c_i n, B = n x_i, enumerated over all divisors (all associates).
usage: tf_exact.py a b [e]        -> solutions of TES((a + b w)^e)
       tf_exact.py census NMAX    -> all 2-primary split primes pi (one per conjugate pair, sign +) with N(pi) <= NMAX
                                     and inert p with p^2 <= NMAX; prints failures and count statistics.
"""
import sys
from sympy import isprime
import tf_core as C

CS = (C.W, C.W2, C.TWO)


def solve(n, normalised=True):
    sols = set()
    Nn = C.norm(n)
    for i in range(3):
        j, k = [m for m in range(3) if m != i]
        for xi in C.disk(C.norm(CS[i]) * Nn / 9):
            if normalised and not C.two_primary(xi):
                continue
            A = C.sub(C.mul(C.NINE, xi), C.mul(CS[i], n))
            B = C.mul(n, xi)
            M = C.mul(C.mul(B, B), C.mul(CS[j], CS[k]))
            fac = C.merge(*[{P: 2 * e for P, e in C.factor(B).items()}, C.factor(CS[j]), C.factor(CS[k])])
            for d in C.divisors(fac):
                xj = C.div(C.add(d, C.mul(B, CS[j])), A)
                if xj is None or xj == (0, 0):
                    continue
                d2 = C.div(M, d)
                xk = C.div(C.add(d2, C.mul(B, CS[k])), A)
                if xk is None or xk == (0, 0):
                    continue
                xs = [None] * 3
                xs[i], xs[j], xs[k] = xi, xj, xk
                if normalised and not all(C.two_primary(x) for x in xs):
                    continue
                assert C.check(n, xs), (n, xs)
                sols.add(tuple(xs))
    return sols


def shape(n_prime, e, xs):
    vals = []
    for x, c in zip(xs, CS):
        v = 0
        q = x
        while True:
            q2 = C.div(q, n_prime)
            if q2 is None:
                break
            q, v = q2, v + 1
        vals.append(v)  # c_i are units at pi (pi does not divide 6)
    z0 = vals.count(0); big = sum(1 for v in vals if v >= e)
    if z0 == 2 and big == 1:
        return 'I'
    if z0 == 1 and big == 2:
        return 'II'
    return 'other'


def two_primary_assoc(P):
    for u in C.UNITS:
        Q = C.mul(u, P)
        if C.two_primary(Q):
            return Q


def census(NMAX):
    fails, counts = [], []
    for p in range(5, NMAX + 1):
        if not isprime(p):
            continue
        if p % 3 == 1:
            pi = two_primary_assoc(C.prime_above(p))
        elif p * p <= NMAX:
            pi = (p, 0)
        else:
            continue
        s = solve(pi)
        sh = [shape(pi, 1, xs) for xs in s]
        counts.append((C.norm(pi), len(s), sh.count('I'), sh.count('II'), sh.count('other')))
        if not s:
            fails.append((p, pi))
    return fails, counts


if __name__ == '__main__':
    if sys.argv[1] == 'census':
        NMAX = int(sys.argv[2])
        fails, counts = census(NMAX)
        print(f"census N(pi) <= {NMAX}: {len(counts)} primes (one per conjugate pair), {len(fails)} with NO solution")
        print("failures (p, pi):", fails)
        print("shapes over all solutions: I", sum(c[2] for c in counts), "II", sum(c[3] for c in counts),
              "other", sum(c[4] for c in counts))
        for lo, hi in [(0, 1000), (1000, 3000), (3000, 10000), (10000, 30000), (30000, 100000), (100000, 10**9)]:
            sub = [c[1] for c in counts if lo < c[0] <= hi]
            if sub:
                print(f"  N in ({lo},{hi}]: {len(sub)} primes, mean #sol {sum(sub)/len(sub):.2f}, min {min(sub)}, "
                      f"#zero {sub.count(0)}")
    else:
        a, b = int(sys.argv[1]), int(sys.argv[2]); e = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        P = (a, b); n = (1, 0)
        for _ in range(e):
            n = C.mul(n, P)
        s = solve(n)
        print(f"TES(({a}+{b}w)^{e}), N(n) = {C.norm(n)}: {len(s)} solutions")
        from collections import Counter
        print(Counter(shape(P, e, xs) for xs in s))
        for xs in sorted(s)[:10]:
            print("  ", xs)
