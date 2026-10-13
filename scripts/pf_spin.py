"""O165 Prop 2.1 numerics: proportion of II{a,d} slices (4a^2 d <= p) whose N = p+4a^2 d has a prime
factor l not dividing 2ad with (l/p) = -1  (= passes the chi_{-4d} sign test, Lemma 1.3), split by (d/p).
Control n = m^2: the same test with chi_{-4d}(l) (must be 0 %).  Random sample of slices weighted by the box.
Usage: pf_spin.py n samples seed
"""
import sys, random
from sympy import factorint, jacobi_symbol, isprime


def sample(n, S, seed):
    rnd = random.Random(seed)
    sq = not isprime(n)
    tot = {1: 0, -1: 0}; ok = {1: 0, -1: 0}
    amax = int((n / 4) ** 0.5)
    w = [n // (4 * a * a) for a in range(1, amax + 1)]
    for _ in range(S):
        a = rnd.choices(range(1, amax + 1), weights=w)[0]
        d = rnd.randint(1, n // (4 * a * a))
        N = n + 4 * a * a * d
        s = jacobi_symbol(d % n, n) if not sq else 1
        if s == 0:
            continue
        tot[s] += 1
        for l in factorint(N):
            if (2 * a * d) % l == 0:
                continue
            chi = jacobi_symbol(l % n, n) if not sq else jacobi_symbol((-d) % l, l) if l > 2 else 1
            if chi == -1:
                ok[s] += 1
                break
    return tot, ok


if __name__ == "__main__":
    n, S, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    tot, ok = sample(n, S, seed)
    for s in (1, -1):
        if tot[s]:
            print(f"n={n} (d/n)={s:+d}: slices {tot[s]}, pass chi_-4d test {ok[s]} = {ok[s]/tot[s]:.3f}")
