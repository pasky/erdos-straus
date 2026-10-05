"""R38b: adversarial hill-climbing for violations of Cor 4.1 / C-1.
usage: review_o10b_hill.py MODE N K OBJ ITERS RESTARTS SEED
 MODE: bu (bool uniform) | bb (bool, per-coordinate bias also climbed) | qa (q-ary, random alph<=4, random measure)
 OBJ : G   -> G_F(2^{1/k})                    (C-1 says <=1)
       T   -> max_t energy(t) 2^{(t+1)/k}      (Cor 4.1 says <=1)
       T2  -> same, restricted to t >= 2k-1   (tests the exponential rate, not the t<k regime)
 Prints the best objective found per restart and overall."""
import sys, numpy as np
from review_o10b_lib import bad_indicator, level_weights

mode, n, k, obj, iters, restarts, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
rng = np.random.default_rng(seed)
lam = 2 ** (1 / k)


def rand_dims():
    if mode == "qa":
        return tuple(int(x) for x in rng.integers(2, 5, size=n))
    return (2,) * n


def rand_probs(dims):
    if mode == "bu":
        return [np.full(q, 1 / q) for q in dims]
    return [rng.dirichlet(np.ones(q) * 0.7) * 0.98 + 0.02 / q for q in dims]


def rand_term(dims):
    w = int(rng.integers(1, k + 1))
    vs = rng.choice(n, size=w, replace=False)
    return {int(v): int(rng.integers(dims[v])) for v in vs}


def score(dims, probs, events):
    if not events:
        return -1.0
    h = bad_indicator(dims, events)
    lw = level_weights(1 - h, probs)
    if obj == "G":
        return float(sum(lw[d] * lam ** d for d in range(n + 1)))
    t0 = 0 if obj == "T" else 2 * k - 1
    best = 0.0
    for t in range(t0, n):
        best = max(best, lw[t + 1:].sum() * 2 ** ((t + 1) / k))
    return float(best)


def mutate(dims, probs, events):
    ev = [dict(e) for e in events]
    pr = [p.copy() for p in probs]
    r = rng.random()
    if r < 0.15 or not ev:
        ev.append(rand_term(dims))
    elif r < 0.25 and len(ev) > 1:
        ev.pop(int(rng.integers(len(ev))))
    elif r < 0.85:
        e = ev[int(rng.integers(len(ev)))]
        s = rng.random()
        if s < 0.35 and len(e) < k:
            free = [v for v in range(n) if v not in e]
            v = int(rng.choice(free)); e[v] = int(rng.integers(dims[v]))
        elif s < 0.55 and len(e) > 1:
            del e[int(rng.choice(list(e)))]
        elif s < 0.8:
            v = int(rng.choice(list(e))); e[v] = int(rng.integers(dims[v]))
        else:
            v = int(rng.choice(list(e))); free = [u for u in range(n) if u not in e]
            if free:
                u = int(rng.choice(free)); c = e.pop(v); e[u] = int(rng.integers(dims[u]))
    elif mode != "bu":
        v = int(rng.integers(n))
        p = pr[v] * np.exp(rng.normal(0, 0.5, size=len(pr[v])))
        pr[v] = p / p.sum()
    else:
        ev.append(rand_term(dims))
    return pr, ev


overall = -1
for rs in range(restarts):
    dims = rand_dims()
    probs = rand_probs(dims)
    events = [rand_term(dims) for _ in range(int(rng.integers(1, 2 * n)))]
    cur = score(dims, probs, events)
    for it in range(iters):
        pr2, ev2 = mutate(dims, probs, events)
        s2 = score(dims, pr2, ev2)
        if s2 >= cur or rng.random() < 0.02:
            probs, events, cur = pr2, ev2, s2
        if cur > overall:
            overall = cur
            best = (dims, [np.round(p, 3).tolist() for p in probs], [dict(sorted(e.items())) for e in events])
    print(f"restart {rs}: final {cur:.6f} overall {overall:.6f}", flush=True)
print(f"MODE={mode} n={n} k={k} OBJ={obj} OVERALL MAX = {overall:.8f}  (max-1 = {overall-1:.3e})")
print("best:", best)
