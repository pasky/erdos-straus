"""R50 from-scratch checks of Cor 1.2/1.3 (DNF Fourier tails) of paper/energy-dnf-note.tex.
Exact rationals for tails; mpmath (60 digits) only for the irrational endpoint 2^{1/k}.

Usage: PYTHONPATH=scripts uv run --with mpmath python scripts/review_r50_dnf.py SEED NRAND
"""
import itertools, random, sys
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 60


def energies_biased(n, ps, g):
    """g: tuple of +-1 values indexed by integer x (bit v of x = 1 means x_v=-1).
    ps[v] = P[x_v=-1] (Fraction).  Returns list W[d] = sum_{|U|=d} ||g^{=U}||^2, and E g."""
    pts = range(2 ** n)
    prob = []
    for x in pts:
        pr = Fr(1)
        for v in range(n):
            pr *= ps[v] if (x >> v) & 1 else 1 - ps[v]
        prob.append(pr)
    W = [Fr(0)] * (n + 1)
    for U in range(2 ** n):
        c = Fr(0)
        for x in pts:
            if prob[x] == 0:
                continue
            t = Fr(1)
            for v in range(n):
                if (U >> v) & 1:
                    xv = -1 if (x >> v) & 1 else 1
                    t *= xv - (1 - 2 * ps[v])        # x_v - E x_v
            c += prob[x] * g[x] * t
        var = Fr(1)
        for v in range(n):
            if (U >> v) & 1:
                var *= 4 * ps[v] * (1 - ps[v])
        if var == 0:
            assert c == 0
            continue
        W[bin(U).count("1")] += c * c / var
    p = sum(prob[x] for x in pts if g[x] == -1)
    return W, p


def min_width(n, g):
    """minimal DNF width of the function 'g == -1' (True = -1)."""
    k = 0
    for x in range(2 ** n):
        if g[x] != -1:
            continue
        best = None
        for r in range(n + 1):
            for S in itertools.combinations(range(n), r):
                mask = sum(1 << v for v in S)
                if all(g[y] == -1 for y in range(2 ** n) if (y & mask) == (x & mask)):
                    best = r; break
            if best is not None:
                break
        k = max(k, best)
    return max(k, 1)


def check(n, ps, g, k, stats):
    W, p = energies_biased(n, ps, g)
    assert sum(W) == 1
    c = 4 * p * (2 - p)
    for t in range(n + 1):
        tail = sum(W[t + 1:])
        # tail <= c 2^{-(t+1)/k}  <=>  tail^k 2^{t+1} <= c^k
        assert tail ** k * 2 ** (t + 1) <= c ** k, (g, t, tail, c, k)
        if c > 0 and tail > 0:
            r = mp.mpf(tail.numerator) / tail.denominator * mp.mpf(2) ** (mp.mpf(t + 1) / k) / (mp.mpf(c.numerator) / c.denominator)
            stats["ratio"] = max(stats["ratio"], r)
    lam = mp.mpf(2) ** (mp.mpf(1) / k)
    Gg = sum(lam ** d * (mp.mpf(W[d].numerator) / W[d].denominator) for d in range(n + 1))
    pf = mp.mpf(p.numerator) / p.denominator
    assert Gg <= 1 + 4 * pf + mp.mpf(10) ** -50, (Gg, p)
    I = sum(d * (mp.mpf(W[d].numerator) / W[d].denominator) for d in range(n + 1))
    assert I <= 4 * k * pf / mp.log(2) + mp.mpf(10) ** -50
    if pf > 0:
        stats["infl"] = max(stats["infl"], I / (k * pf))
        stats["gend"] = max(stats["gend"], (Gg - 1) / pf)


def dnf_eval(n, terms):
    """terms: list of dict v->bit (bit 1 means literal x_v=-1). returns g tuple."""
    g = []
    for x in range(2 ** n):
        sat = any(all(((x >> v) & 1) == b for v, b in T.items()) for T in terms)
        g.append(-1 if sat else 1)
    return tuple(g)


def main():
    seed, nrand = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    # (1) all Boolean functions on 4 bits, uniform measure, minimal width
    n = 4
    stats = {"ratio": mp.mpf(0), "infl": mp.mpf(0), "gend": mp.mpf(0)}
    half = [Fr(1, 2)] * n
    for m in range(2 ** (2 ** n)):
        g = tuple(-1 if (m >> x) & 1 else 1 for x in range(2 ** n))
        check(n, half, g, min_width(n, g), stats)
    print("C1 all 65536 functions on 4 bits, uniform: OK; max tail/(4p(2-p)2^{-(t+1)/k}) =",
          mp.nstr(stats["ratio"], 6), " max I/(kp) =", mp.nstr(stats["infl"], 6),
          "(bound 4/ln2=", mp.nstr(4 / mp.log(2), 6), ") max (G-1)/p =", mp.nstr(stats["gend"], 6))
    # (2) random DNFs with random widths under biased measures (incl. very biased)
    stats = {"ratio": mp.mpf(0), "infl": mp.mpf(0), "gend": mp.mpf(0)}
    for i in range(nrand):
        n = rng.randint(2, 6)
        ps = [rng.choice([Fr(1, 2), Fr(1, 3), Fr(1, 10), Fr(1, 50), Fr(2, 3), Fr(49, 50), Fr(rng.randint(1, 9), 10)]) for _ in range(n)]
        k = rng.randint(1, n)
        terms = []
        for _ in range(rng.randint(1, 8)):
            S = rng.sample(range(n), rng.randint(1, k))
            terms.append({v: (1 if rng.random() < .7 else 0) for v in S})
        g = dnf_eval(n, terms)
        check(n, ps, g, k, stats)
    print("C2 random DNFs (n<=6) under biased product measures: OK on", nrand,
          "; max ratio =", mp.nstr(stats["ratio"], 6), " max I/(kp) =", mp.nstr(stats["infl"], 6))
    # (3) adversarial families
    stats = {"ratio": mp.mpf(0), "infl": mp.mpf(0), "gend": mp.mpf(0)}
    for k in (1, 2, 3):
        for b in range(1, 6 // k + 1):
            n = k * b
            terms = [{v: 1 for v in range(i * k, (i + 1) * k)} for i in range(b)]  # tribes / disjoint ANDs
            for pr in (Fr(1, 2), Fr(1, 5), Fr(1, 20), Fr(1, 100)):
                check(n, [pr] * n, dnf_eval(n, terms), k, stats)
    print("C3 disjoint-AND (tribes / sharpness family) k<=3, n<=6, p in {1/2,1/5,1/20,1/100}: OK; max ratio =",
          mp.nstr(stats["ratio"], 6))
    stats = {"ratio": mp.mpf(0), "infl": mp.mpf(0), "gend": mp.mpf(0)}
    n = 6
    for k in (2, 3, 4):
        # sunflower: all terms share a core of k-1 variables, distinct petals
        core = {v: 1 for v in range(k - 1)}
        terms = [{**core, v: 1} for v in range(k - 1, n)]
        for pr in (Fr(1, 2), Fr(1, 10), Fr(9, 10)):
            check(n, [pr] * n, dnf_eval(n, terms), k, stats)
        # all k-subsets ANDs (threshold function >= k)
        terms = [{v: 1 for v in S} for S in itertools.combinations(range(n), k)]
        for pr in (Fr(1, 2), Fr(1, 10)):
            check(n, [pr] * n, dnf_eval(n, terms), k, stats)
    print("C4 sunflowers / threshold DNFs n=6: OK; max ratio =", mp.nstr(stats["ratio"], 6))


if __name__ == "__main__":
    main()
