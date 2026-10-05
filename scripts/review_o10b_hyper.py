"""R38b: from-scratch checks of Lemma 3.2 (Q = E_P Theta^2), Lemma 3.3 (|Theta|<=prod_M (w-1)),
Thm 3.4 (Q <= prod_M (w-1)), and Lemma 3.1 (G_F <= E_x Q(H(x))) incl. BIASED q-ary measures.
usage: review_o10b_hyper.py TRIALS SEED"""
import itertools, sys, numpy as np
from review_o10b_lib import bad_indicator, G_weighted

trials, seed = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(seed)


def subsets(n):
    return [frozenset(c) for r in range(n + 1) for c in itertools.combinations(range(n), r)]


def N_cover(H, V):  # signed count of subfamilies covering V (brute force)
    s = 0
    for r in range(len(H) + 1):
        for J in itertools.combinations(H, r):
            U = frozenset().union(*J) if J else frozenset()
            if V <= U:
                s += (-1) ** r
    return s


def tau_hat(H, V):  # Mobius transform of transversal indicator, computed independently
    s = 0
    for r in range(len(V) + 1):
        for R in itertools.combinations(sorted(V), r):
            R = set(R)
            s += (-1) ** (len(V) - r) * all(R & E for E in H)
    return s


def Q(H, mu, n):
    return sum(np.prod([mu[v] for v in V]) * tau_hat(H, V) ** 2 for V in subsets(n))


def Theta(C, lam):
    s = 0.0
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            U = frozenset().union(*J) if J else frozenset()
            s += (-1) ** r * np.prod([lam[v] for v in U])
    return s


def matchings(H):
    out = [[]]
    for r in range(1, len(H) + 1):
        for M in itertools.combinations(H, r):
            if all(not (a & b) for a, b in itertools.combinations(M, 2)):
                out.append(list(M))
    return out


worst = {"L32": 0, "L33": -9, "T34": -9, "L31": -9, "N=tauhat": 0}
for tr in range(trials):
    n = int(rng.integers(2, 7))
    m = int(rng.integers(1, 6))
    H = list({frozenset(int(v) for v in rng.choice(n, size=int(rng.integers(1, n + 1)), replace=False)) for _ in range(m)})
    # weights with all w_E <= 2: random positive, then scale logs
    a = rng.exponential(1, size=n) * (rng.random(n) < 0.8)
    mx = max(sum(a[v] for v in E) for E in H)
    a = a * (np.log(2) / mx if mx > 0 else 1) * (1 if rng.random() < 0.6 else rng.random())
    lam = np.exp(a); mu = lam - 1
    for V in subsets(n)[: 12]:
        worst["N=tauhat"] = max(worst["N=tauhat"], abs(abs(N_cover(H, V)) - abs(tau_hat(H, V))))
    q = Q(H, mu, n)
    # Lemma 3.2: exact expectation over P
    EP = 0.0
    for P in subsets(n):
        pr = np.prod([mu[v] / lam[v] if v in P else 1 / lam[v] for v in range(n)])
        EP += pr * Theta([E for E in H if not (E & P)], lam) ** 2
    worst["L32"] = max(worst["L32"], abs(EP - q))
    for M in matchings(H):
        b = np.prod([np.prod([lam[v] for v in E]) - 1 for E in M]) if M else 1.0
        worst["T34"] = max(worst["T34"], q - b)
        # Lemma 3.3 for random subfamily containing M (with possible empty edge)
        C = M + [E for E in H if E not in M and rng.random() < 0.7]
        worst["L33"] = max(worst["L33"], abs(Theta(C, lam)) - b)
# Lemma 3.1 on random biased q-ary single-value systems
for tr in range(trials // 4):
    n = int(rng.integers(2, 6))
    dims = tuple(int(x) for x in rng.integers(2, 4, size=n))
    probs = [rng.dirichlet(np.ones(q)) for q in dims]
    k = int(rng.integers(1, n + 1))
    evs = []
    for _ in range(int(rng.integers(1, 7))):
        vs = rng.choice(n, size=int(rng.integers(1, k + 1)), replace=False)
        evs.append({int(v): int(rng.integers(dims[v])) for v in vs})
    a = rng.exponential(1, size=n)
    mx = max(sum(a[v] for v in e) for e in evs)
    lam = np.exp(a * np.log(2) / mx); mu = lam - 1
    G = G_weighted(1 - bad_indicator(dims, evs), probs, lam)
    gam = 0.0
    for x in itertools.product(*[range(q) for q in dims]):
        px = np.prod([probs[v][x[v]] for v in range(n)])
        Hx = list({frozenset(e) for e in evs if all(x[v] == c for v, c in e.items())})
        gam += px * Q(Hx, mu, n)
    worst["L31"] = max(worst["L31"], G - gam)
    worst["T34"] = max(worst["T34"], gam - 1)
print({k: float(v) for k, v in worst.items()})
print("expected: L32~0, N=tauhat=0, L33<=0, T34<=0, L31<=0")
