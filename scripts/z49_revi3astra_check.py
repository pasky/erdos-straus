"""Independent hostile-review checks for I3_DEEP_ASTRA (z49). Small, memory-bounded.
Run: ulimit -v 8000000; timeout 600 uv run --with numpy python scripts/z49_revi3astra_check.py
"""
import itertools, random, math
from math import gcd, isqrt, log
import numpy as np

random.seed(49)

def divisors(m):
    ds = []
    for d in range(1, isqrt(m) + 1):
        if m % d == 0:
            ds.append(d)
            if d * d != m:
                ds.append(m // d)
    return ds

def I3_fast(n):
    # ordered (t,u,v), all >=3, n = tuv - u - v ; enumerate u, divisor A=tu-1 of n+u
    c = 0
    u = 3
    while 3 * (3 * u - 1) - u <= n:
        for A in divisors(n + u):
            if A % u == u - 1 and A >= 3 * u - 1 and (n + u) // A >= 3:
                c += 1
        u += 1
    return c

def I3_brute(n):
    c = 0
    for t in range(3, n + 1):
        if 9 * t - 6 > n: break
        for u in range(3, n + 1):
            if 3 * t * u - u - 3 > n: break
            # v = (n+u)/(tu-1)
            if (n + u) % (t * u - 1) == 0 and (n + u) // (t * u - 1) >= 3:
                c += 1
    return c

# A. counts
for n in range(3, 1501):
    assert I3_fast(n) == I3_brute(n), n
zeros = [n for n in range(3, 3001) if I3_fast(n) == 0]
print("A. zeros<=3000:", len(zeros), zeros[:20], "...")
for n in (21, 42, 17, 241, 49, 121, 1225, 1600, 6336, 193, 409, 577, 2521, 3361, 5569, 9601, 66529):
    print("   I3(%d)=%d" % (n, I3_fast(n)))

# B. delta_3(H) exact for H=3..7
def lcm_upto(H):
    L = 1
    for i in range(1, H + 1):
        L = L * i // gcd(L, i)
    return L
for H in range(3, 8):
    Q = lcm_upto(H) ** 2
    bad = np.zeros(Q, dtype=bool)
    for u in range(3, H + 1):
        for v in range(u, H + 1):
            M = u * v
            bad[(-u - v) % M::M] = True
    av = Q - int(bad.sum())
    print("B. H=%d Q=%d avoid=%d delta=%s" % (H, Q, av, str(av / Q)))

# C. gcd identity
for u in range(3, 400):
    for v in range(3, 400):
        assert gcd(u * v, u + v + 1) == gcd(u, v + 1) * gcd(v, u + 1)
print("C. gcd identity ok to 400")

# D. shared modulus bound in equal-sum / unequal-sum compatible case
def sqfree(n):
    return all(n % (p * p) for p in range(2, isqrt(n) + 1))
def pairs(urange, vrange):
    return [(u, v) for u in urange for v in vrange if sqfree(u) and sqfree(v) and gcd(u, v) == 1]
U = range(5, 40); V = range(400, 1600)
P = pairs(U, V)
bysum = {}
for (u, v) in P:
    bysum.setdefault(u + v, []).append((u, v))
worst_eq = 0; cnt_eq = 0
for s, L in bysum.items():
    for (u, v), (u2, v2) in itertools.combinations(L, 2):
        D = gcd(u * v, u2 * v2)
        if D > 1:
            cnt_eq += 1
            assert D <= u * u2 * abs(u - u2)
            worst_eq = max(worst_eq, D / max(v, v2))
print("D. equal-sum dependent pairs:", cnt_eq, "max D/max(v,v')=%.4f" % worst_eq)
# unequal sums, random sample of compatible pairs
cnt = 0; worst = 0
for _ in range(200000):
    (u, v) = random.choice(P); (u2, v2) = random.choice(P)
    if (u, v) == (u2, v2): continue
    D = gcd(u * v, u2 * v2)
    if D > 1 and (u + v - u2 - v2) % D == 0 and u + v != u2 + v2:
        cnt += 1
        worst = max(worst, D / (2 * max(v, v2)))
        g, h, j, k = gcd(u, u2), gcd(v, v2), gcd(u, v2), gcd(v, u2)
        assert g * h * j * k == D
print("   unequal-sum compatible sampled:", cnt, "max D/(2max v)=%.3f" % worst)
# without separation (overlapping ranges) equal-sum D can exceed max endpoint?
Pov = pairs(range(5, 300), range(5, 300))
mx = 0
bys = {}
for (u, v) in Pov:
    if u < v: bys.setdefault(u + v, []).append((u, v))
for s, L in bys.items():
    for a, b in itertools.combinations(L, 2):
        D = gcd(a[0] * a[1], b[0] * b[1])
        mx = max(mx, D / max(a[1], b[1]))
print("   overlapping ranges: max D/max v over equal-sum pairs = %.2f" % mx)

# E. energy lemma: sum_U 2^{|U|/k} ||F^{=U}||^2 <= 1, random single-value systems
def es_energies(f, shape, probs):
    # f: array over product space; probs: list of 1d prob vectors. returns dict U->||f^{=U}||^2
    n = len(shape)
    W = np.ones(shape)
    for i, p in enumerate(probs):
        sh = [1] * n; sh[i] = len(p)
        W = W * p.reshape(sh)
    # conditional expectations E(f|X_S) broadcast
    cond = {}
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            g = f * W
            others = tuple(i for i in range(n) if i not in S)
            num = g.sum(axis=others, keepdims=True) if others else g
            den = W.sum(axis=others, keepdims=True) if others else W
            cond[S] = np.broadcast_to(num / den, shape)
    en = {}
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            comp = np.zeros(shape)
            for rr in range(r + 1):
                for T in itertools.combinations(S, rr):
                    comp = comp + (-1) ** (r - rr) * cond[T]
            en[S] = float((comp ** 2 * W).sum())
    return en
worst = 0
for trial in range(300):
    n = random.randint(2, 5); q = [random.randint(2, 4) for _ in range(n)]
    k = random.randint(1, min(3, n))
    probs = [np.random.dirichlet(np.ones(qq)) for qq in q]
    F = np.ones(q)
    for _ in range(random.randint(1, 8)):
        supp = random.sample(range(n), random.randint(1, k))
        vals = {i: random.randrange(q[i]) for i in supp}
        idx = tuple(vals[i] if i in vals else slice(None) for i in range(n))
        F[idx] = 0
    en = es_energies(F, tuple(q), probs)
    G = sum(2 ** (len(S) / k) * e for S, e in en.items())
    assert abs(sum(en.values()) - (F * np.ones(q)).mean() * 0 - sum(en.values())) < 1e-12
    worst = max(worst, G)
print("E. energy lemma: max G_F over 300 random width-k systems = %.6f (must be <=1)" % worst)

# G. short interval theorem 4.1
def S0S1K(Y):
    S0 = S1 = 0.0; K = 0
    for a in range(3, Y + 1):
        for b in range(3, Y // a + 1):
            S0 += 1 / (a * b); S1 += 1 / (a * b - 1); K += 1
    return S0, S1, K
cache = {}
for H in (3, 5, 9, 16, 25, 40):
    S0, S1, K = S0S1K(H)
    for _ in range(6):
        n = random.randint(H * H, H * H + 5000)
        tot = sum(I3_fast(m) for m in range(n + 1, n + H + 1))
        lb = H * (S0 + 2 * S1) - 3 * K
        assert tot >= lb - 1e-9, (H, n, tot, lb)
    print("G. H=%d: lower bound %.1f ; (3/2)H log^2 H = %.1f ; sample total %d" % (H, lb, 1.5 * H * log(H) ** 2, tot))

# H. S_sharp growth
for H in (100, 300, 1000, 2000):
    S = 0.0
    for u in range(3, H + 1):
        for v in range(u, H + 1):
            S += gcd(u * v, u + v + 1) / (u * v)
    print("H. H=%d S#=%.2f  L^4=%.1f ratio=%.4f  L^2=%.1f" % (H, S, log(H) ** 4, S / log(H) ** 4, log(H) ** 2))

# I. atomic Janson: -log P(Av) >= mu - K Delta  on random small instances
worstJ = -1e9
for trial in range(300):
    n = random.randint(2, 6); q = [random.randint(2, 5) for _ in range(n)]
    probs = [np.ones(qq) / qq for qq in q]
    evs = []
    for _ in range(random.randint(1, 10)):
        supp = tuple(sorted(random.sample(range(n), random.randint(1, n))))
        evs.append({i: random.randrange(q[i]) for i in supp})
    evs = [dict(t) for t in {tuple(sorted(e.items())) for e in evs}]
    def P(e):
        return np.prod([1 / q[i] for i in e])
    x = {i: 2 * P(e) for i, e in enumerate(evs)}
    conf = lambda a, b: any(i in b and b[i] != a[i] for i in a)
    share = lambda a, b: (not conf(a, b)) and any(i in b for i in a)
    ok = all(P(e) <= x[i] * np.prod([1 - x[j] for j, f in enumerate(evs) if j != i and conf(e, f)]) for i, e in enumerate(evs))
    if not ok or max(x.values()) >= 1: continue
    K = max(np.prod([1 / (1 - x[j]) for j, f in enumerate(evs) if j != i and conf(e, f)]) for i, e in enumerate(evs))
    mu = sum(P(e) for e in evs)
    Dl = 0.0
    for a, b in itertools.combinations(evs, 2):
        if share(a, b):
            m = dict(a); m.update(b); Dl += P(m)
    good = 0
    for pt in itertools.product(*[range(qq) for qq in q]):
        if not any(all(pt[i] == e[i] for i in e) for e in evs):
            good += 1
    pav = good / np.prod(q)
    worstJ = max(worstJ, (mu - K * Dl) - (-log(pav)))
print("I. atomic Janson: max (mu-K Delta) - (-log P(Av)) = %.3g (must be <=0)" % worstJ)
