"""R170 from-scratch re-computation of the GROWING_IDENTITIES §4/§5 census of the sign-blind set
D*(n) = {(t, m''): t = 3 (4), t <= n+2, m'' | tn+1, 4 | (tn+1)/m'', m'' = +-1 (t), m'' != 1}.
Also checks: class -1 count = W(n) (direct cubic count) and no non-trivial pair has t > n+2 (sampled)."""
import sys
from math import isqrt
from statistics import mean, pstdev
from sympy import divisors, isprime


def census(n, tcap=None):
    plus = minus = 0
    for t in range(3, (tcap or n + 2) + 1, 4):
        N = t * n + 1
        for mm in divisors(N):
            if mm == 1 or (N // mm) % 4:
                continue
            r = mm % t
            if r == 1:
                plus += 1
            elif r == t - 1:
                minus += 1
    return plus, minus


def W_direct(n):
    w = 0
    for c in range(1, n + 3):
        g = 1
        while c * g - 1 <= n + c:
            e = c * g - 1
            if e > 0 and (n + c) % e == 0 and (((n + c) // e) * g) % 4 == 1:
                w += 1
            g += 1
    return w


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "doc4":
        ps = [p for p in range(10**4, 10600) if p % 24 == 1 and isprime(p)]
        print("primes =1(24) in [1e4,1.06e4]:", [(p, census(p)) for p in ps])
        print("squares:", [(k, census(k * k)) for k in (99, 101, 105, 107)])
        for n in ps[:3] + [99 * 99]:
            pl, mi = census(n)
            print("  W check", n, mi, W_direct(n), "tail t in (n+2, 3n] extra:", census(n, 3 * n + 2) != (pl, mi))
    else:
        P, C, S = [], [], []
        for n in range(4001, 6001):
            if n % 24 != 1:
                continue
            c = census(n)
            r = isqrt(n)
            (S if r * r == n else P if isprime(n) else C).append(c)
        for name, L in (("primes", P), ("composites", C), ("squares", S)):
            print(name, len(L), "means(+1,-1,tot) = %.1f %.1f %.1f sd(tot)=%.1f" % (
                mean(x[0] for x in L), mean(x[1] for x in L), mean(sum(x) for x in L), pstdev([sum(x) for x in L])))
        sq = [(k, census(k * k)) for k in range(63, 79, 2)]
        print("odd squares 63^2..77^2 (not restricted to 1 mod 24):", sq,
              "means %.1f %.1f %.1f sd %.1f" % (mean(x[1][0] for x in sq), mean(x[1][1] for x in sq),
                                                mean(sum(x[1]) for x in sq), pstdev([sum(x[1]) for x in sq])))
