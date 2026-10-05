"""R49 from-scratch check of POINTWISE_OMEGA14 Lemma 1.1 (planting).
Full enumeration of {0,1}^n in exact rationals (n<=10), random + edge instances.
Checks: nu>=0, nu(0)=0, total mass 1, all <=k marginals equal mu's.
Also probes: how often nu fails positivity when (1.1) is violated (sanity that the
check can fail)."""
import itertools, random, sys
from fractions import Fraction as Fr


def esym(vals, a):
    e = [Fr(0)] * (a + 1)
    e[0] = Fr(1)
    for v in vals:
        for t in range(a, 0, -1):
            e[t] += e[t - 1] * v
    return e[a]


def build(p, k):
    n = len(p)
    r = [pi / (1 - pi) for pi in p]
    P0 = Fr(1)
    for pi in p:
        P0 *= 1 - pi
    mu = {}
    for x in itertools.product((0, 1), repeat=n):
        w = Fr(1)
        for xi, pi in zip(x, p):
            w *= pi if xi else 1 - pi
        mu[x] = w
    ek1 = esym(r, k + 1)
    assert ek1 > 0
    nu = dict(mu)
    for J in itertools.combinations(range(n), k + 1):
        wJ = Fr(1)
        for i in J:
            wJ *= r[i]
        wJ /= ek1
        if wJ == 0:
            continue
        for s in range(k + 2):
            for y in itertools.combinations(J, s):
                x = tuple(1 if i in y else 0 for i in range(n))
                nu[x] += P0 * wJ * (-1) ** (s + 1)
    return mu, nu, r


def check(p, k):
    n = len(p)
    mu, nu, r = build(p, k)
    ok_pos = all(v >= 0 for v in nu.values())
    ok_zero = nu[tuple([0] * n)] == 0
    ok_tot = sum(nu.values()) == 1
    ok_marg = True
    for s in range(1, k + 1):
        for K in itertools.combinations(range(n), s):
            for z in itertools.product((0, 1), repeat=s):
                a = sum(v for x, v in mu.items() if all(x[K[t]] == z[t] for t in range(s)))
                b = sum(v for x, v in nu.items() if all(x[K[t]] == z[t] for t in range(s)))
                if a != b:
                    ok_marg = False
    return ok_pos, ok_zero, ok_tot, ok_marg, r


def cond(r, k):
    return sum(r) >= (k + 1) + (2 * k + 1) * max(r)


def rand_p(n, rng, lo, hi):
    return [Fr(rng.randint(int(lo * 1000), int(hi * 1000)), 1000) for _ in range(n)]


def main():
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 49)
    tested = fails = 0
    viol_tested = viol_neg = 0
    for trial in range(400):
        k = rng.randint(0, 3)
        n = rng.randint(k + 1, 10)
        mode = rng.random()
        if mode < 0.3:
            p = rand_p(n, rng, 0.0, 0.7)
        elif mode < 0.5:
            p = rand_p(n, rng, 0.3, 0.6)
        elif mode < 0.7:  # some exact zeros
            p = rand_p(n, rng, 0.2, 0.6)
            for i in rng.sample(range(n), rng.randint(0, n // 2)):
                p[i] = Fr(0)
        else:  # one large coordinate
            p = rand_p(n, rng, 0.2, 0.5)
            p[0] = Fr(rng.randint(600, 900), 1000)
        r = [pi / (1 - pi) for pi in p]
        if sum(1 for x in r if x > 0) < k + 1:
            continue
        c = cond(r, k)
        pos, zero, tot, marg, _ = check(p, k)
        if c:
            tested += 1
            if not (pos and zero and tot and marg):
                fails += 1
                print("FAIL", k, p, pos, zero, tot, marg)
        else:
            viol_tested += 1
            assert zero and tot and marg  # these hold unconditionally
            if not pos:
                viol_neg += 1
    # equality edge cases: R exactly (k+1)+(2k+1)r*, all r equal: n r = (k+1)+(2k+1) r
    eq = 0
    for k in range(0, 4):
        for n in range(3 * k + 2, 11):
            # r = (k+1)/(n-2k-1)  -> p = r/(1+r)
            r0 = Fr(k + 1, n - 2 * k - 1)
            p = [r0 / (1 + r0)] * n
            assert sum([r0] * n) == (k + 1) + (2 * k + 1) * r0
            pos, zero, tot, marg, _ = check(p, k)
            eq += 1
            if not (pos and zero and tot and marg):
                fails += 1
                print("EQ-FAIL", k, n, pos, zero, tot, marg)
    print(f"cond-satisfied instances: {tested}, equality instances: {eq}, failures: {fails}")
    print(f"cond-violated instances: {viol_tested}, of which nu has a negative atom: {viol_neg}")


if __name__ == "__main__":
    main()
