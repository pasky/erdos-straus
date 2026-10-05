"""R38: exact (Fraction) check of Lemma 3.1, G_F <= E_x Q_mu(H(x)), and of
C-1 exactly, on small product spaces. From scratch (uses review_o10_q.Q only).
usage: review_o10_cover.py seed ntrials
"""
import sys, itertools, random
from fractions import Fraction as Fr
from review_o10_q import Q, boundary_lam


def G_exact(qs, F, lam):
    n = len(qs)
    pts = list(itertools.product(*[range(q) for q in qs]))
    tot = Fr(0)
    for V in range(1 << n):
        arr = {x: Fr(F[x]) for x in pts}
        coef = Fr(1)
        for v in range(n):
            if V >> v & 1:
                coef *= lam[v] - 1
                if coef == 0:
                    break
                avg = {}
                for x in pts:
                    key = x[:v] + x[v + 1:]
                    avg[key] = avg.get(key, 0) + arr[x]
                arr = {x: arr[x] - avg[x[:v] + x[v + 1:]] / qs[v] for x in pts}
        if coef == 0:
            continue
        tot += coef * sum(a * a for a in arr.values()) / len(pts)
    return tot


def main():
    seed, ntr = map(int, sys.argv[1:3])
    rng = random.Random(seed)
    worst = Fr(0)
    for t in range(ntr):
        n = rng.randint(1, 4)
        qs = [rng.randint(2, 3) for _ in range(n)]
        evs = []
        for _ in range(rng.randint(1, 6)):
            S = rng.sample(range(n), rng.randint(1, n))
            evs.append({v: rng.randrange(qs[v]) for v in S})
        H = list({sum(1 << v for v in e) for e in evs})
        lam = boundary_lam(rng, H, n)
        if lam is None:
            continue
        pts = list(itertools.product(*[range(q) for q in qs]))
        F = {x: 0 if any(all(x[v] == c for v, c in e.items()) for e in evs) else 1 for x in pts}
        g = G_exact(qs, F, lam)
        mu = [l - 1 for l in lam]
        gam = Fr(0)
        for x in pts:
            Hx = list({sum(1 << v for v in e) for e in evs if all(x[v] == c for v, c in e.items())})
            gam += Q(Hx, mu, n)
        gam /= len(pts)
        assert g <= gam <= 1, (qs, evs, lam, g, gam)
        worst = max(worst, g)
    print("exact: G<=Gamma<=1 in all cases; max G", float(worst))


if __name__ == "__main__":
    main()
