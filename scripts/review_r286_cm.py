"""R286 check of LOWER_TAIL_FABLE §2 / §3.3 claim: 'every integer built as a primitive norm from Z[i] (including
#E(F_p) for CM by Z[i] and its twists, and (a+b)^2 = p + 2ab) has no prime factor = 3 (mod 4), hence carries no
certificate'.
#E(F_p) for E_D: y^2 = x^3 - D x is counted directly (Legendre-symbol sum) for every D mod p (all quartic twists),
and we test whether #E or (a+b)^2 has a prime factor = 3 (mod 4).
"""
from collections import Counter
from review_r286_canon import isprime, factor


def count_points(p, D):
    sq = [0] * p
    for y in range(p):
        sq[y * y % p] += 1
    return 1 + sum(sq[(x * x * x - D * x) % p] for x in range(p))


if __name__ == "__main__":
    st = Counter(); ex = []
    for p in range(5, 1200, 4):
        if not isprime(p):
            continue
        a = next(a for a in range(1, p) if int((p - a * a) ** 0.5) ** 2 == p - a * a)
        b = int((p - a * a) ** 0.5)
        orders = {count_points(p, D) for D in range(1, p)}
        st["primes"] += 1
        bad = [N for N in orders if any(q % 4 == 3 for q in factor(N))]
        st["primes with a Z[i]-CM order having a prime factor 3 mod 4"] += bool(bad)
        s = (a + b) ** 2
        st["primes where (a+b)^2 has a prime factor 3 mod 4"] += any(q % 4 == 3 for q in factor(s))
        if bad and len(ex) < 4:
            ex.append((p, (a, b), sorted(orders), bad, s, factor(s)))
    print(dict(st))
    for e in ex:
        print(e)
