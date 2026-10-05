"""R57 from-scratch check of POINTWISE_OMEGA15 Lemma 1.1 and the TV bound of Prop 2.5(i).

Toy planted systems, exact rationals.  Small coordinate s uniform on {0..S-1}; big coordinates
X_b uniform on Z/m_b; Omega_b(s) a subset of Z/m_b depending on s.  The planted law nu is built
from the DEFINITION (O14 Lemma 1.1 measure on bits, then X_b drawn uniformly conditioned on its
bit) and E_nu h is computed by summing over all bit patterns y (2^n terms) and over Z/m_b --
no use of the author's closed form.  h = h_s(s) prod_{b in I} h_b(X_b) with |h|<=1, |E h_b|<=1/4.
Checks: (a) nu is a probability law, k-wise marginals = mu, nu(all-zero bits)=0;
(b) E_rho h = 0 if |I|<=k; (c) |E_rho h| <= (4 r*)^{k+1}; (d) |rho| <= P0 2^{k+1} <= e^{-(1-p*)R} 2^{k+1}.
Adversarial h_b: beta_b in {+-1}, gamma_b extreme subject to the mean constraint.
Usage: PYTHONPATH=scripts uv run python scripts/review_o15_lemma11.py [seed] [trials]
"""
import itertools, math, random, sys
from fractions import Fraction as Fr


def esym(vals, a):
    e = [Fr(0)] * (a + 1); e[0] = Fr(1)
    for v in vals:
        for j in range(a, 0, -1):
            e[j] += e[j - 1] * v
    return e[a]


def planted_bits(p, k):
    """dict y(frozenset)->nu(y) for O14 Lemma 1.1 law; also mu."""
    n = len(p)
    r = [x / (1 - x) for x in p]
    P0 = Fr(1)
    for x in p:
        P0 *= 1 - x
    mu = {}
    for m in range(n + 1 if n <= 11 else k + 2):
        for y in itertools.combinations(range(n), m):
            v = P0
            for i in y:
                v *= r[i]
            mu[frozenset(y)] = v
    nu = dict(mu)
    e = esym(r, k + 1)
    for J in itertools.combinations(range(n), k + 1):
        w = Fr(1)
        for i in J:
            w *= r[i]
        if w == 0:
            continue
        w /= e
        for m in range(len(J) + 1):
            for y in itertools.combinations(J, m):
                nu[frozenset(y)] += P0 * w * (-1) ** (m + 1)
    return mu, nu, P0, r


def rand_hb(m, omega, rng, adversarial):
    """values on Z/m with |h|<=1 and |mean|<=1/4."""
    while True:
        if adversarial:
            bval = Fr(rng.choice([-1, 1]))
            no = len(omega); nc = m - no
            target = Fr(rng.choice([-1, 1]), 4)          # mean exactly +-1/4
            g = (target * m - bval * no) / nc
            g = max(Fr(-1), min(Fr(1), g))
            h = [bval if x in omega else g for x in range(m)]
        else:
            h = [Fr(rng.randint(-8, 8), 8) for _ in range(m)]
        if abs(sum(h) / m) <= Fr(1, 4):
            return h


def trial(rng, adversarial):
    n = rng.randint(6, 11) if rng.random() < 0.5 else rng.randint(17, 26)
    S = rng.randint(1, 3)
    ms = [rng.choice([8, 9, 10, 12, 16]) for _ in range(n)]
    omegas = [[set(rng.sample(range(ms[b]), 1 if ms[b] < 16 else rng.randint(1, 2))) for b in range(n)]
              for _ in range(S)]
    # p_b(s) = |Omega|/m <= 1/8
    ps = [[Fr(len(omegas[s][b]), ms[b]) for b in range(n)] for s in range(S)]
    pstar = max(max(row) for row in ps)
    rstar = pstar / (1 - pstar)
    # largest k with (1.0) for all s
    k = -1
    while all(sum(x / (1 - x) for x in ps[s]) >= (k + 2) + (2 * k + 3) * rstar for s in range(S)):
        k += 1
    if k < 0:
        return None
    I = sorted(rng.sample(range(n), rng.randint(1, n)))
    hs = [Fr(rng.choice([-1, 1])) for _ in range(S)]
    hb = {b: rand_hb(ms[b], omegas[0][b], rng, adversarial) for b in I}
    Erho = Fr(0); tvmass = Fr(0); worst_P0 = Fr(0); worstR = None
    for s in range(S):
        mu, nu, P0, r = planted_bits(ps[s], k)
        assert nu[frozenset()] == 0 and min(nu.values()) >= 0
        if n <= 11:
            assert sum(nu.values()) == 1
        for K in (itertools.combinations(range(n), min(k, n)) if n <= 11 else []):   # k-wise marginals
            for z in itertools.product([0, 1], repeat=len(K)):
                a = sum(v for y, v in nu.items() if all((i in y) == bool(zi) for i, zi in zip(K, z)))
                c = sum(v for y, v in mu.items() if all((i in y) == bool(zi) for i, zi in zip(K, z)))
                assert a == c
        cond = {}
        for b in I:
            om = omegas[s][b]; m = ms[b]
            inn = [hb[b][x] for x in om]; out = [hb[b][x] for x in range(m) if x not in om]
            cond[b] = (sum(out) / len(out), sum(inn) / len(inn))   # (gamma, beta)
        for y in nu:
            d = nu[y] - mu[y]
            if d == 0:
                continue
            tvmass += abs(d) / S
            t = d * hs[s]
            for b in I:
                t *= cond[b][1] if b in y else cond[b][0]
            Erho += t / S
        R = sum(r)
        worst_P0 = max(worst_P0, P0)
        bound_tv = math.exp(-(1 - float(pstar)) * float(R)) * 2 ** (k + 1)
        assert float(P0) * 2 ** (k + 1) <= bound_tv * (1 + 1e-12)
    if len(I) <= k:
        assert Erho == 0, (I, k, Erho)
    bound = (4 * rstar) ** (k + 1)
    assert abs(Erho) <= bound, (abs(Erho), bound)
    assert tvmass <= worst_P0 * 2 ** (k + 1)
    return k, len(I), float(abs(Erho) / bound), float(tvmass / (worst_P0 * 2 ** (k + 1)))


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    rng = random.Random(seed)
    done = 0; worst = 0.0; worst_tv = 0.0; zero_cases = 0; ks = {}
    while done < trials:
        res = trial(rng, adversarial=(done % 2 == 1))
        if res is None:
            continue
        k, mI, ratio, tvr = res
        done += 1; ks[k] = ks.get(k, 0) + 1
        zero_cases += mI <= k
        worst = max(worst, ratio); worst_tv = max(worst_tv, tvr)
    print(f"trials={trials} k-distribution={ks} cases |I|<=k (E_rho=0 verified)={zero_cases}")
    print(f"worst |E_rho h|/(4r*)^(k+1) = {worst:.3e}; worst |rho|/(P0 2^(k+1)) = {worst_tv:.3f}")
    print("all assertions passed")


if __name__ == "__main__":
    main()
