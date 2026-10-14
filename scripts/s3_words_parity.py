"""O208 memo s3_words_parity: parity of the number of chi = -1 sigma-orbits of positive words of p.
Words: (t,u,v) >= 1 with t u v - u - v = n; enumerate by u <= v: A = t u - 1 | n + u, A = -1 mod u.
chi(w) = (-A / n) (Jacobi). sigma: u <-> v preserves chi (A A* = t n + 1). Usage: s3_words_parity.py N"""
import sys
from sympy import primerange, jacobi_symbol
from sympy import divisors
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000


def orbits(n):
    """list of (chi, orbit size) over sigma-orbits; words with u <= v"""
    out = []
    for u in range(1, n + 2):
        # A | n + u, A = t u - 1 >= u - 1, v = (n+u)/A >= u  ->  A <= (n+u)/u
        if (u - 1) * u > n + u:
            break
        for A in divisors(n + u):
            if (A + 1) % u or A * u > n + u:
                continue
            t = (A + 1) // u
            v = (n + u) // A
            if t < 1 or v < u:
                continue
            assert t * u * v - u - v == n
            out.append((jacobi_symbol((-A) % n, n), 1 if u == v else 2))
    return out


from collections import Counter
stat = Counter()
for p in primerange(5, N):
    ob = orbits(p)
    neg = sum(1 for c, s in ob if c == -1)
    tot = len(ob)
    stat[(p % 8, neg % 2, tot % 2)] += 1
for k in sorted(stat):
    print('p mod 8 = %d, #chi=-1 orbits parity %d, #orbits parity %d : %d primes' % (k[0], k[1], k[2], stat[k]))
sq = Counter()
for m in range(3, int(N ** 0.5) + 1, 2):
    ob = orbits(m * m)
    sq[(sum(1 for c, s in ob if c == -1), len(ob) % 2)] += 1
print('odd squares: (#chi=-1 orbits, #orbits parity) ->', dict(sq))
