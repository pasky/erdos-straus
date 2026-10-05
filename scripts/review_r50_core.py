"""R50 from-scratch checks of Thm 1.1 / Lemma 3.1 / Lemma 4.1 / Thm 4.3 of
paper/energy-dnf-note.tex.  Exact rationals.  Independent of energy_note_check.py.

Usage: PYTHONPATH=scripts uv run python scripts/review_r50_core.py SEED NCASES
"""
import itertools, random, sys
from fractions import Fraction as Fr


def subsets(s):
    s = list(s)
    for r in range(len(s) + 1):
        for c in itertools.combinations(s, r):
            yield frozenset(c)


def es_energies(qs, pis, f):
    """f: dict point->value on prod range(q).  Returns dict U -> ||f^{=U}||^2.
    Computed via conditional expectations and Mobius inversion, pointwise."""
    n = len(qs)
    pts = list(itertools.product(*[range(q) for q in qs]))
    prob = {x: _prod(pis[v][x[v]] for v in range(n)) for x in pts}
    # conditional expectation E[f | x_W] as function of the point
    cond = {}
    for W in subsets(range(n)):
        num, den = {}, {}
        for x in pts:
            key = tuple(x[v] for v in sorted(W))
            num[key] = num.get(key, 0) + prob[x] * f[x]
            den[key] = den.get(key, 0) + prob[x]
        cond[W] = {x: (num[k] / den[k] if den[k] else Fr(0))
                   for x in pts for k in [tuple(x[v] for v in sorted(W))]}
    out = {}
    for U in subsets(range(n)):
        comp = {x: sum((-1) ** (len(U) - len(W)) * cond[W][x] for W in subsets(U))
                for x in pts}
        out[U] = sum(prob[x] * comp[x] ** 2 for x in pts)
    return out, prob, pts


def _prod(it):
    r = Fr(1)
    for a in it:
        r *= a
    return r


def avoid(events, pts):
    """events: list of dict v->value."""
    return {x: Fr(int(not any(all(x[v] == s for v, s in e.items()) for e in events)))
            for x in pts}


def N(H, V):
    """signed cover count, brute force over subfamilies (H a list of frozensets)."""
    V = frozenset(V)
    tot = 0
    for r in range(len(H) + 1):
        for J in itertools.combinations(H, r):
            cov = frozenset().union(*[j & V for j in J]) if J else frozenset()
            if cov == V:
                tot += (-1) ** r
    return tot


def Q(H, mu, V0):
    return sum(_prod(mu[v] for v in V) * N(H, V) ** 2 for V in subsets(V0))


def Theta(C, lam):
    tot = Fr(0)
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            u = frozenset().union(*J) if J else frozenset()
            tot += (-1) ** r * _prod(lam[v] for v in u)
    return tot


def rand_measure(q, rng, tiny=False):
    w = [rng.randint(1, 6) for _ in range(q)]
    if tiny:
        w[0] = 1; w = [1] + [rng.randint(20, 60) for _ in range(q - 1)]
    s = sum(w)
    return [Fr(a, s) for a in w]


WEIGHTS = [Fr(1), Fr(9, 8), Fr(5, 4), Fr(4, 3), Fr(7, 5), Fr(3, 2), Fr(5, 3), Fr(2)]


def rand_weights(n, events, rng):
    """random rational weights, then lowered until every event weight <= 2;
    try to make some event weight exactly 2."""
    lam = [rng.choice(WEIGHTS) for _ in range(n)]
    while True:
        bad = [e for e in events if _prod(lam[v] for v in e) > 2]
        if not bad:
            return lam
        v = rng.choice(sorted(set().union(*[set(e) for e in bad])))
        i = WEIGHTS.index(lam[v])
        lam[v] = WEIGHTS[max(0, i - 1)]


def check_case(rng, n, qs, nev, tiny):
    pis = [rand_measure(q, rng, tiny) for q in qs]
    events = []
    for _ in range(nev):
        k = rng.randint(1, n)
        S = rng.sample(range(n), k)
        if tiny:  # bias towards the rare value 0 (adversarial)
            events.append({v: (0 if rng.random() < .7 else rng.randrange(qs[v])) for v in S})
        else:
            events.append({v: rng.randrange(qs[v]) for v in S})
    lam = rand_weights(n, events, rng)
    mu = [l - 1 for l in lam]
    pts = list(itertools.product(*[range(q) for q in qs]))
    F = avoid(events, pts)
    en, prob, _ = es_energies(qs, pis, F)
    G = sum(_prod(lam[v] for v in U) * e for U, e in en.items())
    assert G <= 1, (G, events, lam)
    # Lemma 3.1 for every V, and the matching refinement
    for V in subsets(range(n)):
        LV = sum(e for U, e in en.items() if V <= U)
        rhs = Fr(0)
        for x in pts:
            H = sorted({frozenset(e) for e in events if all(x[v] == s for v, s in e.items())}, key=sorted)
            rhs += prob[x] * N(H, V) ** 2
        assert LV <= rhs, (V, LV, rhs)
    # G_F <= E_x min_M prod (w_J - 1)
    ref = Fr(0)
    for x in pts:
        H = sorted({frozenset(e) for e in events if all(x[v] == s for v, s in e.items())}, key=sorted)
        best = Fr(1)
        for r in range(1, len(H) + 1):
            for M in itertools.combinations(H, r):
                if all(not (a & b) for a, b in itertools.combinations(M, 2)):
                    best = min(best, _prod(_prod(lam[v] for v in J) - 1 for J in M))
        ref += prob[x] * best
    assert G <= ref, (G, ref)
    return G


def check_hyper(rng, n):
    V0 = range(n)
    m = rng.randint(0, 6)
    H = []
    for _ in range(m):
        H.append(frozenset(rng.sample(range(n), rng.randint(0, min(3, n)))))
    H = sorted(set(H), key=sorted)
    lam = rand_weights(n, H, rng)
    mu = [l - 1 for l in lam]
    q = Q(H, mu, V0)
    # polarization: exact expectation over P
    ex = Fr(0)
    for P in subsets(V0):
        pr = _prod((mu[v] / lam[v]) if v in P else (1 - mu[v] / lam[v]) for v in V0)
        HP = [J for J in H if not (J & P)]
        ex += pr * Theta(HP, lam) ** 2
    assert q == ex, (q, ex)
    # Theta bound for every matching, and Q bound
    for r in range(len(H) + 1):
        for M in itertools.combinations(H, r):
            if all(not (a & b) for a, b in itertools.combinations(M, 2)):
                b = _prod(_prod(lam[v] for v in J) - 1 for J in M)
                assert abs(Theta(H, lam)) <= b
                assert q <= b
                if len(M) == len(H):
                    assert q == b
    return q


if __name__ == "__main__":
    seed, ncases = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    mx = Fr(0)
    for i in range(ncases):
        n = rng.randint(1, 4)
        qs = [rng.randint(2, 4) for _ in range(n)]
        G = check_case(rng, n, qs, rng.randint(1, 7), tiny=(i % 2 == 1))
        mx = max(mx, G)
    print("A: Thm1.1 + Lemma3.1 + matching refinement OK on", ncases, "systems; max G =", float(mx))
    mq = Fr(0)
    for i in range(ncases):
        mq = max(mq, check_hyper(rng, rng.randint(1, 5)))
    print("B: polarization identity + Theta/Q matching bounds OK on", ncases, "hypergraphs; max Q =", float(mq))
