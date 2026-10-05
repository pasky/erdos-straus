"""R48a: from-scratch brute-force check of O13 Lemma 1.1 (beta-weighted LLL).

Product space of k coordinates with small (possibly non-uniform) finite marginals.
Events: random supports, random sets of accepted value-tuples on the support.
x_E = beta^{|supp E|} P(E); hypothesis: sum_{E ni l} x_E <= eta = (3/4) log beta, all l.
Claims checked exactly:
  (i)  P(cap not-E) >= exp(-(4/3) sum x_E)
  (ii) P(E | cap_{F in S} not-F) <= x_E for E not in S.
Random systems + adversarial hill-climbing (maximise violation ratio).
"""
import itertools, math, sys
import numpy as np

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)


def make_space(k, sizes):
    marg = []
    for s in sizes:
        w = rng.random(s) + (0.2 if rng.random() < 0.5 else 5.0)
        marg.append(w / w.sum())
    grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
    pts = np.stack([g.ravel() for g in grids], axis=1)
    prob = np.ones(len(pts))
    for i in range(k):
        prob *= marg[i][pts[:, i]]
    return pts, prob


def rand_event(k, sizes, maxsupp):
    s = rng.integers(1, maxsupp + 1)
    supp = tuple(sorted(rng.choice(k, size=s, replace=False)))
    # accepted tuples: a single tuple (like ES events) or a small random set
    tuples = set()
    ntup = 1 if rng.random() < 0.6 else rng.integers(1, 4)
    for _ in range(ntup):
        tuples.add(tuple(int(rng.integers(sizes[i])) for i in supp))
    return supp, frozenset(tuples)


def indicator(pts, ev):
    supp, tuples = ev
    sub = pts[:, list(supp)]
    ind = np.zeros(len(pts), dtype=bool)
    for t in tuples:
        ind |= np.all(sub == np.array(t), axis=1)
    return ind


def evaluate(pts, prob, events, k, beta, n_cond=20):
    eta = 0.75 * math.log(beta)
    inds = [indicator(pts, e) for e in events]
    P = [prob[i].sum() for i in inds]
    x = [beta ** len(e[0]) * p for e, p in zip(events, P)]
    w = np.zeros(k)
    for e, xe in zip(events, x):
        for l in e[0]:
            w[l] += xe
    slack = eta - w.max()
    bad = np.zeros(len(pts), dtype=bool)
    for i in inds:
        bad |= i
    avoid = prob[~bad].sum()
    lower = math.exp(-(4 / 3) * sum(x))
    r1 = lower / avoid if avoid > 0 else float("inf")
    r2 = 0.0
    m = len(events)
    for _ in range(n_cond):
        E = int(rng.integers(m))
        S = [j for j in range(m) if j != E and rng.random() < 0.6]
        cond = np.ones(len(pts), dtype=bool)
        for j in S:
            cond &= ~inds[j]
        pc = prob[cond].sum()
        if pc <= 0:
            r2 = float("inf")
            continue
        pe = prob[cond & inds[E]].sum() / pc
        r2 = max(r2, pe / x[E] if x[E] > 0 else 0)
    return slack, r1, r2


def main():
    worst1 = worst2 = 0.0
    nvalid = 0
    for trial in range(400):
        k = int(rng.integers(3, 7))
        sizes = [int(rng.integers(3, 9)) for _ in range(k)]
        if np.prod(sizes) > 60000:
            continue
        pts, prob = make_space(k, sizes)
        beta = math.exp(rng.uniform(0.02, 1 / 3))
        m = int(rng.integers(2, 12))
        events = [rand_event(k, sizes, min(3, k)) for _ in range(m)]
        slack, r1, r2 = evaluate(pts, prob, events, k, beta)
        # adversarial hill-climb: add/replace events while (1.1) holds, maximise r1
        best = (r1 if slack >= 0 else -1, events)
        for it in range(60):
            ev2 = list(best[1])
            if rng.random() < 0.5 or len(ev2) < 2:
                ev2.append(rand_event(k, sizes, min(3, k)))
            else:
                ev2[int(rng.integers(len(ev2)))] = rand_event(k, sizes, min(3, k))
            s2, a2, b2 = evaluate(pts, prob, ev2, k, beta, n_cond=5)
            if s2 >= 0:
                nvalid += 1
                worst1 = max(worst1, a2)
                worst2 = max(worst2, b2)
                if a2 > best[0]:
                    best = (a2, ev2)
        if slack >= 0:
            nvalid += 1
            worst1 = max(worst1, r1)
            worst2 = max(worst2, r2)
    print(f"valid systems checked: {nvalid}")
    print(f"max lower/actual (claim <=1): {worst1:.6f}")
    print(f"max P(E|cond)/x_E (claim <=1): {worst2:.6f}")


if __name__ == "__main__":
    main()
