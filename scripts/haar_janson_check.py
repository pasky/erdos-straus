"""O46: brute-force sanity check of POINTWISE_HAAR Thm 1.4 on random atomic
event systems (exact enumeration of a small product space).
Checks  -log P(Av) >= mu - K*Delta  whenever the lopsided-LLL hypothesis
with x_E = 2P(E) holds; also reports the tightest ratio seen."""
import itertools, math, random, sys
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
def trial(nv, q, ne, maxw):
    ranges = [q] * nv
    ev = []
    for _ in range(ne):
        w = random.randint(1, min(maxw, nv))
        S = random.sample(range(nv), w)
        ev.append({v: random.randrange(q) for v in S})
    ev = [dict(t) for t in {tuple(sorted(e.items())) for e in ev}]
    P = [q ** (-len(e)) for e in ev]
    conf = lambda a, b: any(v in b and b[v] != a[v] for v in a)
    share = lambda a, b: (not conf(a, b)) and any(v in b for v in a)
    x = [2 * p for p in P]
    for i, e in enumerate(ev):
        prod = 1.0
        for j, f in enumerate(ev):
            if j != i and conf(e, f): prod *= (1 - x[j])
        if not (x[i] < 1 and P[i] <= x[i] * prod): return None
    K = max(1 / math.prod((1 - x[j]) for j, f in enumerate(ev) if j != i and conf(e, f))
            for i, e in enumerate(ev))
    mu = sum(P)
    Delta = sum(q ** (-len(set(ev[i]) | set(ev[j])))
                for i in range(len(ev)) for j in range(i + 1, len(ev)) if share(ev[i], ev[j]))
    cnt = 0
    for pt in itertools.product(*[range(r) for r in ranges]):
        if not any(all(pt[v] == a for v, a in e.items()) for e in ev): cnt += 1
    pav = cnt / q ** nv
    lhs = -math.log(pav)
    return lhs, mu - K * Delta, mu, Delta, K
worst = None; n_ok = 0; n_run = 0
for t in range(3000):
    nv = random.randint(2, 6); q = random.randint(3, 6)
    r = trial(nv, q, random.randint(2, 40), random.randint(1, 3))
    if r is None: continue
    n_run += 1
    lhs, rhs, mu, Delta, K = r
    assert lhs >= rhs - 1e-12, (lhs, rhs, mu, Delta, K)
    if mu > 0:
        gap = (lhs - rhs) / mu
        if worst is None or gap < worst[0]: worst = (gap, lhs, rhs, mu, Delta)
print("systems satisfying the hypothesis:", n_run, " all passed; tightest (lhs-rhs)/mu, lhs, rhs, mu, Delta:", worst)
