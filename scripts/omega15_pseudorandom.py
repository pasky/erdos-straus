"""O57 / POINTWISE_OMEGA15 Lemma 1.1 checks (exact rationals).

(1) Identity check by brute force on tiny product spaces: for the planted law
    nu = mu + P0 * sum_J w_J sigma_J (bits b_i = 1[X_i in Omega_i], coordinates drawn from
    the uniform law conditioned on the bit), E_nu h - E_mu h equals
    -P0 * sum_{J subset I} w_J prod_J (gamma-beta) prod_{I\\J} gamma  for product functions h.
(2) Bound check: on random instances with (1.0) [R >= (k+1)+(2k+1)r*, p* <= 1/8] and random
    reduced products (|h_b| <= 1, |E h_b| <= 1/4), |E_rho h| <= (4 r*)^{k+1}, and E_rho h = 0
    when |I| <= k. Reports the worst observed ratio |E_rho h| / (4 r*)^{k+1}.
Usage: PYTHONPATH=scripts uv run python scripts/omega15_pseudorandom.py [seed]
"""
import itertools
import random
import sys
from fractions import Fraction as Fr


def esym(vals, a):
    e = [Fr(0)] * (a + 1)
    e[0] = Fr(1)
    for v in vals:
        for j in range(a, 0, -1):
            e[j] += e[j - 1] * v
    return e[a]


def planted_rho(p, k):
    """rho = nu - mu on bit configurations, supported on |y| <= k+1 (keys: frozenset y)."""
    n = len(p)
    r = [pi / (1 - pi) for pi in p]
    P0 = Fr(1)
    for pi in p:
        P0 *= 1 - pi
    rho = {}
    ek1 = esym(r, k + 1)
    for J in itertools.combinations(range(n), k + 1):
        w = Fr(1)
        for i in J:
            w *= r[i]
        if w == 0:
            continue
        w /= ek1
        for s_ in range(k + 2):
            for y in itertools.combinations(J, s_):
                key = frozenset(y)
                rho[key] = rho.get(key, Fr(0)) + P0 * w * (-1) ** (s_ + 1)
    return P0, r, rho


def rand_h(rng, m, mean_cap=Fr(1, 4)):
    while True:
        h = [Fr(rng.randint(-8, 8), 8) for _ in range(m)]
        if abs(sum(h) / m) <= mean_cap:
            return h


def beta_gamma(h, Om):
    m = len(h)
    ins = [h[x] for x in range(m) if x in Om]
    out = [h[x] for x in range(m) if x not in Om]
    return sum(ins) / len(ins), sum(out) / len(out)


def E_rho_formula(rho, I, bg):
    tot = Fr(0)
    for y, v in rho.items():
        t = v
        for b in I:
            be, ga = bg[b]
            t *= be if b in y else ga
        tot += t
    return tot


def check_identity(rng, trials=40):
    bad = 0
    for _ in range(trials):
        n = rng.randint(2, 4)
        k = rng.randint(0, n - 1)
        ms = [rng.randint(3, 5) for _ in range(n)]
        Oms = [set(rng.sample(range(m), rng.randint(1, m - 1))) for m in ms]
        p = [Fr(len(O), m) for O, m in zip(Oms, ms)]
        P0, r, rho = planted_rho(p, k)
        I = [b for b in range(n) if rng.random() < 0.7]
        hs = [rand_h(rng, m, Fr(1)) if b in I else [Fr(1)] * m for b, m in enumerate(ms)]
        # brute force E_rho h over the full product space
        brute = Fr(0)
        for y, v in rho.items():
            # conditional law given bits y: uniform on Omega (bit 1) or complement (bit 0)
            t = v
            for b in range(n):
                S = Oms[b] if b in y else set(range(ms[b])) - Oms[b]
                t *= sum(hs[b][x] for x in S) / len(S)
            brute += t
        bg = {b: beta_gamma(hs[b], Oms[b]) for b in I}
        # closed form: -P0 sum_{J subset I} w_J prod_J (gamma-beta) prod_{I\J} gamma
        ek1 = esym(r, k + 1)
        closed = Fr(0)
        for J in itertools.combinations(I, k + 1):
            w = Fr(1)
            for i in J:
                w *= r[i]
            w /= ek1
            t = -P0 * w
            for b in J:
                t *= bg[b][1] - bg[b][0]
            for b in I:
                if b not in J:
                    t *= bg[b][1]
            closed += t
        if brute != closed or brute != E_rho_formula(rho, I, bg):
            bad += 1
    return trials, bad


def check_bound(rng, ks=(0, 1, 2), trials=60):
    worst = Fr(0)
    tot = bad = 0
    for k in ks:
        done = 0
        while done < trials:
            n = rng.randint(14 * (k + 1), 18 * (k + 1))
            ms = [rng.randint(8, 40) for _ in range(n)]
            oms = [max(1, m // 8 - rng.randint(0, 1)) for m in ms]
            p = [Fr(o, m) for o, m in zip(oms, ms)]
            r = [pi / (1 - pi) for pi in p]
            rs = max(r)
            if sum(r) < (k + 1) + (2 * k + 1) * rs:
                continue
            done += 1
            P0, r, rho = planted_rho(p, k)
            for _ in range(5):
                I = [b for b in range(n) if rng.random() < rng.choice([0.2, 0.5, 1.0])]
                bg = {}
                for b in I:
                    Om = set(range(oms[b]))
                    mode = rng.random()
                    if mode < 0.3:  # adversarial: +1 on Omega, balanced elsewhere
                        m = ms[b]
                        h = [Fr(1) if x in Om else Fr(0) for x in range(m)]
                    elif mode < 0.5:  # -1 on Omega, mean-zero-ish elsewhere
                        m = ms[b]
                        h = [Fr(-1) if x in Om else Fr((-1) ** x, 4) for x in range(m)]
                    else:
                        h = rand_h(rng, ms[b])
                    assert abs(sum(h) / len(h)) <= Fr(1, 4)
                    bg[b] = beta_gamma(h, Om)
                val = E_rho_formula(rho, I, bg)
                tot += 1
                bound = (4 * rs) ** (k + 1)
                if len(I) <= k and val != 0:
                    bad += 1
                if abs(val) > bound:
                    bad += 1
                if bound > 0:
                    worst = max(worst, abs(val) / bound)
    return tot, bad, worst


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)
    t, b1 = check_identity(rng)
    print(f"(1) identity (brute force vs closed form): {t} instances, {b1} failures", flush=True)
    assert b1 == 0
    t, b, w = check_bound(rng)
    print(f"(2) bound |E_rho h| <= (4r*)^(k+1): {t} cases, {b} failures, worst ratio {float(w):.3e}")
    assert b == 0
