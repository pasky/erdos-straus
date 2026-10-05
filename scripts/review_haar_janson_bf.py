"""R46 from-scratch brute force of POINTWISE_HAAR Lemma 1.1, Lemma 1.3, Thm 1.4.

Exact rational arithmetic on small product spaces with one-hot coordinates.
Events: partial assignments (single values). Adversarial: many overlapping events,
nonuniform marginals.
"""
import itertools, random, sys
from fractions import Fraction as Fr
from math import log

def space(ranges, probs):
    pts = []
    for x in itertools.product(*[range(r) for r in ranges]):
        p = Fr(1)
        for v, a in enumerate(x):
            p *= probs[v][a]
        pts.append((x, p))
    return pts

def occurs(E, x):
    return all(x[v] == a for v, a in E.items())

def P(pts, pred):
    return sum(p for x, p in pts if pred(x))

def conflict(E, F):
    return any(v in F and F[v] != a for v, a in E.items())

def share(E, F):
    return (set(E) & set(F)) and not conflict(E, F)

def rand_instance(rng):
    import os
    if os.environ.get('ADV'):
        nv = rng.randint(3, 4); ranges = [rng.randint(4, 6) for _ in range(nv)]
    else:
        nv = rng.randint(2, 4)
        ranges = [rng.randint(2, 4) for _ in range(nv)]
    probs = []
    for r in ranges:
        w = [rng.randint(1, 6) for _ in range(r)]
        s = sum(w)
        probs.append([Fr(a, s) for a in w])
    ne = rng.randint(2, 7) if not os.environ.get('ADV') else rng.randint(6, 10)
    evs = []
    for _ in range(ne):
        k = rng.randint(1, nv) if not os.environ.get('ADV') else rng.randint(2, nv)
        S = rng.sample(range(nv), k)
        E = {v: rng.randrange(ranges[v]) for v in S}
        if E not in evs:
            evs.append(E)
    return ranges, probs, evs

def check(rng, fails, stats):
    ranges, probs, evs = rand_instance(rng)
    pts = space(ranges, probs)
    pE = [P(pts, lambda x, E=E: occurs(E, x)) for E in evs]
    n = len(evs)
    # Lemma 1.1: A atomic, C family non-conflicting with A
    A = evs[0]
    C = [E for E in evs[1:] if not conflict(A, E)]
    lhs = P(pts, lambda x: occurs(A, x) and not any(occurs(E, x) for E in C))
    rhs = pE[0] * P(pts, lambda x: not any(occurs(E, x) for E in C))
    if lhs > rhs:
        fails.append(("L1.1", evs, lhs, rhs))
    # find x_E = t*P(E) valid
    Gam = [[j for j in range(n) if j != i and conflict(evs[i], evs[j])] for i in range(n)]
    best = None
    for t in [1.01, 1.1, 1.3, 1.6, 2, 2.5, 3, 4, 6, 10]:
        xs = [min(0.999, t * float(pE[i])) for i in range(n)]
        ok = True
        for i in range(n):
            prod = 1.0
            for j in Gam[i]:
                prod *= 1 - xs[j]
            if float(pE[i]) > xs[i] * prod * (1 - 1e-12):
                ok = False; break
        if ok:
            K = max([1.0] + [1 / __import__('math').prod(1 - xs[j] for j in Gam[i]) for i in range(n)])
            if best is None or K < best[0]:
                best = (K, xs)
    if best is None:
        stats['nolll'] += 1
        return
    K, xs = best
    stats['lll'] += 1
    # Lemma 1.3 for every subfamily S and A ranging over events and random atomic A
    As = list(evs)
    for _ in range(3):
        k = rng.randint(1, len(ranges)); Sv = rng.sample(range(len(ranges)), k)
        As.append({v: rng.randrange(ranges[v]) for v in Sv})
    for mask in range(1 << n):
        S = [evs[j] for j in range(n) if mask >> j & 1]
        pav = P(pts, lambda x: not any(occurs(E, x) for E in S))
        if pav == 0:
            stats['zeroav'] += 1
            continue
        for Aa in As:
            pa = P(pts, lambda x: occurs(Aa, x))
            pas = P(pts, lambda x: occurs(Aa, x) and not any(occurs(E, x) for E in S))
            bound = float(pa)
            for j in range(n):
                if mask >> j & 1 and conflict(Aa, evs[j]):
                    bound /= (1 - xs[j])
            if float(pas / pav) > bound * (1 + 1e-12):
                fails.append(("L1.3", evs, Aa, mask, float(pas / pav), bound))
    # Theorem 1.4
    pav = P(pts, lambda x: not any(occurs(E, x) for E in evs))
    mu = float(sum(pE))
    Dl = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            if share(evs[i], evs[j]):
                Dl += float(P(pts, lambda x: occurs(evs[i], x) and occurs(evs[j], x)))
    lhs = -log(float(pav)) if pav > 0 else float('inf')
    r1 = mu - K * Dl
    r2 = min(mu / 2, mu * mu / (4 * K * Dl)) if Dl > 0 else mu / 2
    if lhs < r1 - 1e-12 or lhs < r2 - 1e-12:
        fails.append(("T1.4", evs, lhs, r1, r2, K))
    stats['tightest'] = max(stats.get('tightest', -9), r1 - lhs)

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    rng = random.Random(seed)
    fails, stats = [], {'lll': 0, 'nolll': 0, 'zeroav': 0}
    for _ in range(N):
        check(rng, fails, stats)
    print("stats", stats, "fails", len(fails))
    for f in fails[:5]:
        print(f)
