"""R60 from-scratch brute force of CEILINGS_UNIFIED Thm 4.1 on small heterogeneous
bit systems (n bits, P(b_i=1)=p_i<=1/4, F = 1[all bits 0]).
LP over multilinear polynomials of degree <= k on {0,1}^n (= V_k after
averaging each big coordinate given its bit).
  minorant:  max E B  s.t. B <= F pointwise
  majorant:  min E G  s.t. G >= F pointwise
Checks:
 (L-) P >= (5/3)(k+1)  =>  max E B <= 0 (and planting condition (1.1) => <= 0)
 (U-) log(1/min E G) <= k log(C0(P+4k)/k) + 4k/3 + 0.5 log(22k+22) + 3
 (U+) even k >= e^2 P : E Q_k(H) <= 2 e^{-P};   (L+) odd k >= e^2 P : E Q_k(H) >= e^{-4P/3}-e^{-(k+1)} > 0
 plus (U+)/(L+) sandwich Q_k(h) pointwise vs F.
"""
import itertools, math, random
import numpy as np
from scipy.optimize import linprog

C0 = 4 * math.exp(4.31)


def lp(p, k, sense):
    n = len(p)
    monos = [S for j in range(k + 1) for S in itertools.combinations(range(n), j)]
    pts = list(itertools.product((0, 1), repeat=n))
    A = np.array([[1.0 if all(x[i] for i in S) else 0.0 for S in monos] for x in pts])
    F = np.array([1.0 if sum(x) == 0 else 0.0 for x in pts])
    # E[prod_{i in S} b_i] = prod p_i
    mean = np.array([math.prod(p[i] for i in S) for S in monos])
    if sense == "min":  # minorant: maximise mean, A c <= F
        r = linprog(-mean, A_ub=A, b_ub=F, bounds=[(None, None)] * len(monos), method="highs")
        return -r.fun if r.status == 0 else (math.inf if r.status == 3 else None)
    else:  # majorant: minimise mean, A c >= F
        r = linprog(mean, A_ub=-A, b_ub=-F, bounds=[(None, None)] * len(monos), method="highs")
        return r.fun


def Qk(h, k):
    return sum((-1) ** j * math.comb(h, j) for j in range(k + 1))


def ek(p, m):
    e = [1.0] + [0.0] * m
    for x in p:
        for j in range(m, 0, -1):
            e[j] += e[j - 1] * x
    return e[m]


def main(trials=120, seed=1):
    rng = random.Random(seed)
    worst = {"L-": -1e9, "U-slack": 1e9}
    nL = nU = 0
    for _ in range(trials):
        n = rng.randint(4, 13)
        p = [rng.uniform(0.12, 0.25) for _ in range(n)]
        P = sum(p); r = [x / (1 - x) for x in p]; R = sum(r); rs = max(r)
        EF = math.prod(1 - x for x in p)
        for k in range(0, min(3, n) + 1):
            # (L-) and planting
            vmax = lp(p, k, "min")
            if P >= 5 / 3 * (k + 1) or R >= (k + 1) + (2 * k + 1) * rs:
                nL += 1
                worst["L-"] = max(worst["L-"], vmax)
                assert vmax <= 1e-9, (p, k, vmax)
            if k >= 1:
                vmin = lp(p, k, "maj")
                assert vmin >= EF - 1e-9
                bound = k * math.log(C0 * (P + 4 * k) / k) + 4 * k / 3 + 0.5 * math.log(22 * k + 22) + 3
                sav = math.log(1 / vmin)
                worst["U-slack"] = min(worst["U-slack"], bound - sav)
                assert sav <= bound + 1e-9
                nU += 1
    # pointwise Bonferroni sandwich
    for k in range(0, 12):
        for h in range(0, 30):
            q = Qk(h, k)
            F = 1 if h == 0 else 0
            assert q == (1 if h == 0 else (-1) ** k * math.comb(h - 1, k))
            assert F <= q <= F + math.comb(h, k + 1) if k % 2 == 0 else F - math.comb(h, k + 1) <= q <= F
    # (U+), (L+) exact means for independent bits: E Q_k(H) via distribution of H
    for _ in range(200):
        n = rng.randint(1, 40)
        p = [rng.uniform(0, 0.25) for _ in range(n)]
        P = sum(p)
        dist = [1.0]
        for x in p:
            nd = [0.0] * (len(dist) + 1)
            for h, w in enumerate(dist):
                nd[h] += w * (1 - x); nd[h + 1] += w * x
            dist = nd
        k = math.ceil(math.e ** 2 * P)
        for kk in (k, k + 1):
            EQ = sum(w * Qk(h, kk) for h, w in enumerate(dist))
            if kk % 2 == 0:
                assert EQ <= 2 * math.exp(-P) + 1e-12, (P, kk, EQ)
            else:
                assert EQ >= math.exp(-4 * P / 3) - math.exp(-(kk + 1)) - 1e-12 and EQ > 0
    print(f"(L-) cases={nL}, max LP minorant mean = {worst['L-']:.3e} (<=0 required)")
    print(f"(U-) cases={nU}, min slack (bound - saving) = {worst['U-slack']:.3f}")
    print("(U+),(L+) and Bonferroni sandwich: OK")


if __name__ == "__main__":
    main()
