"""R48c from-scratch toy check of Lemma 1.1 (beta-weighted LLL) and the I1(b) twist chain.

Exact enumeration on small product spaces. Coordinates: odd primes l, X_l uniform on the units
mod l (a=0 coordinates), plus one fibre coordinate mod 7^2 on the fibre x = r (mod 7)
(a=1, only 7 values).  Events fix single values on their support (1..3 coordinates).
Events are added greedily while (1.1)  w~_l = sum_{E∋l} beta^{s(E)} P(E) <= eta  holds,
so (1.1) is near-tight.  We check, for every system:
  (i)   P(no event) >= exp(-(4/3) sum beta^s P(E))
  (ii)  for every E∋l0 (l0 a unit coordinate): P(E\\l0 | F') <= beta^{s(E)-1} P(E\\l0),
        F' = avoid all events not involving l0
  (iii) |E[F psi]| <= beta^{-1} w~_{l0} E F'  and  E F >= (1-eta) E F'   (psi = Legendre at l0,
        times Legendre at a second unit coordinate)
Usage: python review_o13c_twist.py TRIALS
"""
import sys, math, random
import numpy as np


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def run(trials, beta, seed):
    rng = random.Random(seed)
    eta = 0.75 * math.log(beta)
    worst = {"i": 0.0, "ii": 0.0, "iii": 0.0, "iv": 0.0}
    nev_tot = 0
    for t in range(trials):
        primes = rng.sample([11, 13, 17, 19, 23], 3)
        coords = [("u", p, [x for x in range(1, p)]) for p in primes]
        coords.append(("f", 7, [3 + 7 * k for k in range(7)]))  # fibre x=3 mod 7, values mod 49
        sizes = [len(c[2]) for c in coords]
        nC = len(coords)
        grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
        events = []
        wt = [0.0] * nC
        for _ in range(400):
            k = rng.choice([1, 2, 2, 3, 3])
            supp = rng.sample(range(nC), k)
            pr = 1.0
            for c in supp:
                pr /= sizes[c]
            x = beta ** k * pr
            if all(wt[c] + x <= eta for c in supp):
                events.append({c: rng.randrange(sizes[c]) for c in supp})
                for c in supp:
                    wt[c] += x
        if not events:
            continue
        nev_tot += len(events)
        ind = []
        for e in events:
            m = np.ones(sizes, dtype=bool)
            for c, v in e.items():
                m &= grids[c] == v
            ind.append(m)
        F = np.ones(sizes, dtype=bool)
        for m in ind:
            F &= ~m
        Sres = sum(beta ** len(e) * np.prod([1.0 / sizes[c] for c in e]) for e in events)
        delta = F.mean()
        worst["i"] = max(worst["i"], math.exp(-(4 / 3) * Sres) / delta)
        # twist at l0 = coordinate 0 (a unit coordinate), psi = Legendre(l0) * Legendre(coord 1)
        l0 = 0
        Fp = np.ones(sizes, dtype=bool)
        for e, m in zip(events, ind):
            if l0 not in e:
                Fp &= ~m
        EFp = Fp.mean()
        for e in events:
            if l0 not in e:
                continue
            A = np.ones(sizes, dtype=bool)
            for c, v in e.items():
                if c != l0:
                    A &= grids[c] == v
            PA = A.mean()
            PA_cond = (A & Fp).mean() / EFp
            if len(e) >= 2:  # s(E)=1 gives A = whole space, ratio exactly 1
                worst["ii"] = max(worst["ii"], PA_cond / (beta ** (len(e) - 1) * PA))
        p0 = coords[0][1]
        p1 = coords[1][1]
        L0 = np.array([legendre(x, p0) for x in coords[0][2]])
        L1 = np.array([legendre(x, p1) for x in coords[1][2]])
        psi = L0.reshape([-1] + [1] * (nC - 1)) * L1.reshape([1, -1] + [1] * (nC - 2))
        EFpsi = abs((F * psi).mean())
        wl0 = wt[l0]
        if wl0 > 0:
            worst["iii"] = max(worst["iii"], EFpsi / (wl0 / beta * EFp))
        worst["iv"] = max(worst["iv"], (1 - eta) * EFp / F.mean())
    return worst, nev_tot


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    for beta in [1.05, 1.15, 1.288, math.exp(1 / 3)]:
        w, n = run(trials, beta, seed=int(beta * 1000))
        print(f"beta={beta:.4f} eta={0.75*math.log(beta):.4f} events={n}: "
              f"max (i) exp(-4S/3)/delta={w['i']:.4f}  max (ii, s>=2) cond/bound={w['ii']:.6f}  "
              f"max (iii) |E[F psi]|/(w l0 EF'/beta)={w['iii']:.4f}  max (iv) (1-eta)EF'/EF={w['iv']:.4f}"
              "   [all must be <=1]")


if __name__ == "__main__":
    main()
