"""R47 from-scratch brute force of §6 (C-1) of es-subexp-note v3.

Random small product probability spaces, random families of cylinder events,
random weights lambda_v>=1 with prod_{supp E} lambda <= 2.  Exact Efron-Stein.
Checks:
 (1) G_F(lambda) = sum_U lambda^U ||F^{=U}||^2 <= 1                (Thm 6.5b)
 (2) ||L_V F||^2 <= E_x N_{H(x)}(V)^2  for every V                 (Lemma 6.2)
 (3) Q_mu(H) == E_P Theta(H_P)^2                                    (Lemma 6.3)
 (4) |Theta(C)| <= prod_{matching}(w_J-1), Q_mu(H) <= 1             (Lemma 6.4, 6.5a)
 (5) energy tail above level t <= 2^{-(t+1)/k}, for F and 1-F       (Cor 6.6)
 (6) sanity: with lambda^{supp} slightly > 2 for a single small event, G>1 can happen.
"""
import itertools, random, math
import numpy as np

def es_components(phi, sizes, probs):
    """phi: ndarray over prod sizes. Return dict U(frozenset)->component array."""
    n = len(sizes)
    # conditional expectations E[phi | X_W]
    cond = {}
    for r in range(n + 1):
        for W in itertools.combinations(range(n), r):
            a = phi
            for v in range(n):
                if v not in W:
                    sh = [1] * n; sh[v] = sizes[v]
                    a = (a * probs[v].reshape(sh)).sum(axis=v, keepdims=True)
            cond[frozenset(W)] = np.broadcast_to(a, phi.shape)
    comps = {}
    for U in cond:
        c = np.zeros(phi.shape)
        for r in range(len(U) + 1):
            for W in itertools.combinations(sorted(U), r):
                c = c + (-1) ** (len(U) - r) * cond[frozenset(W)]
        comps[U] = c
    return comps

def norm2(a, probs):
    w = probs[0]
    for p in probs[1:]:
        w = np.multiply.outer(w, p)
    return float((a * a * w).sum()), w

def N_H(H, V):
    H = list(H); s = 0
    for r in range(len(H) + 1):
        for J in itertools.combinations(H, r):
            cov = set()
            for e in J: cov |= (e & V)
            if cov == V: s += (-1) ** r
    return s

def Theta(C, lam):
    s = 0.0
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            U = set()
            for e in J: U |= e
            s += (-1) ** r * math.prod(lam[v] for v in U)
    return s

def rand_instance(rng, n, maxk):
    sizes = [rng.randint(2, 3) for _ in range(n)]
    probs = []
    for s in sizes:
        p = np.array([rng.random() + 0.05 for _ in range(s)]); probs.append(p / p.sum())
    m = rng.randint(1, 5)
    events = []
    for _ in range(m):
        k = rng.randint(1, maxk)
        S = sorted(rng.sample(range(n), k))
        events.append((tuple(S), tuple(rng.randrange(sizes[v]) for v in S)))
    return sizes, probs, events

def run(trials=300, seed=1):
    rng = random.Random(seed)
    worst = {"G": 0, "cover": -1e9, "polar": 0, "theta": -1e9, "tail": 0}
    for t in range(trials):
        n = rng.randint(2, 4)
        sizes, probs, events = rand_instance(rng, n, min(n, 3))
        # weights: random, then scale so that max over events of lambda^supp <= 2
        lam = [1 + rng.random() * rng.choice([0.1, 1, 3]) for _ in range(n)]
        for _ in range(50):
            mx = max(math.prod(lam[v] for v in S) for S, _ in events)
            if mx <= 2 + 1e-12: break
            lam = [l ** (math.log(2) / math.log(mx)) for l in lam]
        mu = [l - 1 for l in lam]
        F = np.ones(sizes)
        for S, sig in events:
            ind = np.zeros(sizes); idx = [slice(None)] * n
            for v, s in zip(S, sig): idx[v] = s
            ind[tuple(idx)] = 1; F = F * (1 - ind)
        comps = es_components(F, sizes, probs)
        _, wts = norm2(F, probs)
        assert abs(sum(comps.values()) - F).max() < 1e-9
        G = sum(math.prod(lam[v] for v in U) * norm2(c, probs)[0] for U, c in comps.items())
        worst["G"] = max(worst["G"], G)
        assert G <= 1 + 1e-9, (G, events, lam)
        # cover bound per V
        for r in range(n + 1):
            for V in itertools.combinations(range(n), r):
                V = frozenset(V)
                LV = sum(norm2(c, probs)[0] for U, c in comps.items() if V <= U)
                rhs = 0.0
                for x in itertools.product(*[range(s) for s in sizes]):
                    Hx = {frozenset(S) for S, sig in events if all(x[v] == s for v, s in zip(S, sig))}
                    rhs += wts[x] * N_H(Hx, set(V)) ** 2
                worst["cover"] = max(worst["cover"], LV - rhs)
                assert LV <= rhs + 1e-9
        # polarization and matching on the hypergraph of all supports
        H = list({frozenset(S) for S, _ in events})
        Qmu = sum(math.prod(mu[v] for v in V) * N_H(H, set(V)) ** 2
                  for r in range(n + 1) for V in itertools.combinations(range(n), r))
        EP = 0.0
        for P in itertools.product([0, 1], repeat=n):
            pr = math.prod((mu[v] / lam[v]) if P[v] else (1 / lam[v]) for v in range(n))
            HP = [J for J in H if not any(P[v] for v in J)]
            EP += pr * Theta(HP, lam) ** 2
        worst["polar"] = max(worst["polar"], abs(Qmu - EP))
        assert abs(Qmu - EP) < 1e-9
        for r in range(len(H) + 1):
            for M in itertools.combinations(H, r):
                if all(not (a & b) for a, b in itertools.combinations(M, 2)):
                    bd = math.prod(math.prod(lam[v] for v in J) - 1 for J in M)
                    worst["theta"] = max(worst["theta"], abs(Theta(H, lam)) - bd)
                    assert abs(Theta(H, lam)) <= bd + 1e-9
        # tail (Cor 6.6) for F and 1-F
        k = max(len(S) for S, _ in events)
        for tt in range(n + 1):
            en = sum(norm2(c, probs)[0] for U, c in comps.items() if len(U) > tt)
            en1 = sum(norm2(c, probs)[0] for U, c in comps.items() if len(U) > tt and U)
            b = 2 ** (-(tt + 1) / k)
            worst["tail"] = max(worst["tail"], max(en, en1) / b)
            assert en <= b + 1e-9 and en1 <= b + 1e-9
    print("worst:", worst)

def sanity():
    # single event on 1 coordinate, prob p small; lambda = 2.2 > 2 should give G>1
    p = 0.01
    F_E = 1 - 2 * p + p * (2.2 - 1.2 * p)
    print("single-event G with lambda=2.2:", F_E, "(>1 expected)")

if __name__ == "__main__":
    sanity()
    run()
