"""R30b from-scratch interface checks (OMEGA8 minorant -> PO Thm 4.1).

(i)  For random unit-cell combinations B = sum c_i 1[n=b_i (d_i)] with d_i | prod l^{e_l}
     (prime powers included): mu := sum c_i/phi(d_i) = E_Haar[B], and for every real primitive
     psi of conductor f | prod l:  mu_psi := sum_{f|d_i} c_i psi(b_i)/phi(d_i) = E_Haar[B psi]
     (cells with f not dividing d_i contribute 0).  Also M_1(fg) <= M_1(f)M_1(g) prod_{l in I cap J} phi(l^e).
(ii) Lemma 3.2's coefficient formula: the level-<=t Efron-Stein truncation equals
     sum_{|W|<=t} c_W E[phi|X_W], c_W = sum_{i=0}^{t-|W|} (-1)^i binom(N-|W|, i).
(iii) A toy ES-type system on units mod 31,37,41,43 (single-value events, supports <=k=3,
     per-prime mass <= 1/(64k)): BRW minorant B with u_j = level-t truncations of F^(j);
     checks B<=F, E[F-B] vs EF/100, Lemma 3.3 chain |E[F psi]| <= sum p_l0(E) P(E\\l0 & F')
     <= 1.07 w_l0 E F', and the twist |E[B psi]| <= mu/4 for all 15 real primitive psi.
Usage: review_o8b_interface.py seed t nevents
"""
import sys, itertools, math, random
import numpy as np

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def part_i(rng):
    PR = [(3, 2), (5, 1), (7, 1), (11, 1)]  # (l, e): coordinates mod 9, 5, 7, 11
    D = 1
    for l, e in PR: D *= l ** e
    units = [n for n in range(D) if math.gcd(n, D) == 1]
    phiD = len(units)
    worst = 0.0; worst_m1 = -1.0
    for trial in range(200):
        cells = []
        for _ in range(rng.randint(1, 8)):
            sub = [pe for pe in PR if rng.random() < 0.6]
            d = 1
            for l, e in sub: d *= l ** rng.randint(1, e)
            b = rng.choice([x for x in range(d) if math.gcd(x, d) == 1]) if d > 1 else 0
            cells.append((rng.uniform(-3, 3), b, d))
        Bv = {n: sum(c for c, b, d in cells if n % d == b % d) for n in units}
        mu = sum(c / sum(1 for x in range(d) if math.gcd(x, d) == 1) for c, b, d in cells)
        EB = sum(Bv.values()) / phiD
        worst = max(worst, abs(mu - EB))
        for r in range(1, 5):
            for S in itertools.combinations([3, 5, 7, 11], r):
                f = math.prod(S)
                psi = lambda n: math.prod(legendre(n, p) for p in S)
                mupsi = sum(c * psi(b) / sum(1 for x in range(d) if math.gcd(x, d) == 1)
                            for c, b, d in cells if d % f == 0)
                EBpsi = sum(Bv[n] * psi(n) for n in units) / phiD
                worst = max(worst, abs(mupsi - EBpsi))
    # M_1 product bound on single cells
    for trial in range(500):
        def rc():
            sub = [pe for pe in PR if rng.random() < 0.6]
            d = 1
            for l, e in sub: d *= l ** e
            b = rng.choice([x for x in range(d) if math.gcd(x, d) == 1]) if d > 1 else 0
            return b, d, {l for l, e in sub}
        (b1, d1, I), (b2, d2, J) = rc(), rc()
        P = lambda pr: sum(1 for n in units if pr(n)) / phiD
        lhs = P(lambda n: n % d1 == b1 and n % d2 == b2)
        rhs = P(lambda n: n % d1 == b1) * P(lambda n: n % d2 == b2) * math.prod((l - 1) * l ** (e - 1) for l, e in PR if l in I & J)
        worst_m1 = max(worst_m1, lhs - rhs)
    print(f"(i) max |mu-E B|, |mu_psi - E[B psi]| over 200 random combos x 15 psi: {worst:.2e}; "
          f"max [P(C&D) - P(C)P(D)prod phi] over 500 pairs: {worst_m1:.2e} (<=0 expected)")

def cond_mean(arr, keep, N):
    axes = tuple(a for a in range(N) if a not in keep)
    return arr.mean(axis=axes, keepdims=True) if axes else arr

def es_trunc(arr, coords, t):
    """level-<=t Efron-Stein truncation of arr w.r.t. the coordinates `coords` (others pinned/irrelevant)."""
    N = arr.ndim; out = np.zeros_like(arr)
    for r in range(0, t + 1):
        for U in itertools.combinations(coords, r):
            for s in range(len(U) + 1):
                for W in itertools.combinations(U, s):
                    out = out + (-1) ** (len(U) - s) * cond_mean(arr, set(W) | (set(range(N)) - set(coords)), N)
    return out

def es_trunc_cW(arr, coords, t):
    N = arr.ndim; n = len(coords); out = np.zeros_like(arr)
    for s in range(0, t + 1):
        cW = sum((-1) ** i * math.comb(n - s, i) for i in range(t - s + 1))
        for W in itertools.combinations(coords, s):
            out = out + cW * cond_mean(arr, set(W) | (set(range(N)) - set(coords)), N)
    return out

def part_ii_iii(rng, t, nev):
    PRS = [31, 37, 41, 43]; N = 4; k = 3; c0 = 1 / (64 * k)
    shape = tuple(p - 1 for p in PRS)
    grids = np.meshgrid(*[np.arange(1, p) for p in PRS], indexing="ij")
    # random single-value events, supports 2..3, per-prime mass <= c0
    events = []; w = [0.0] * N
    tries = 0
    while len(events) < nev and tries < 100000:
        tries += 1
        s = rng.choice([2, 2, 3])
        supp = sorted(rng.sample(range(N), s))
        # cluster: reuse a few values to create dependence
        vals = {a: rng.choice([1, 2, 3, rng.randrange(1, PRS[a])]) for a in supp}
        P = math.prod(1 / (PRS[a] - 1) for a in supp)
        if any(w[a] + P > c0 for a in supp): continue
        key = tuple((a, vals[a]) for a in supp)
        if key in [e for e, _ in events]: continue
        events.append((key, P))
        for a in supp: w[a] += P
    A = [np.ones(shape, dtype=bool) for _ in events]
    for i, (key, P) in enumerate(events):
        for a, v in key: A[i] &= (grids[a] == v)
    A = [x.astype(float) for x in A]
    m = len(events)
    Fl = [np.ones(shape)]
    for i in range(m): Fl.append(Fl[-1] * (1 - A[i]))
    F = Fl[-1]
    # (ii) coefficient formula on a random function
    phi = rng.random() * np.ones(shape) + np.asarray(np.random.default_rng(1).random(shape))
    d_ii = max(np.abs(es_trunc(phi, list(range(N)), tt) - es_trunc_cW(phi, list(range(N)), tt)).max() for tt in range(0, 4))
    print(f"(ii) ES truncation vs Lemma 3.2 c_W formula, t=0..3: max diff {d_ii:.2e}")
    # u_j: truncation of F^(j) (F_{<j} pinned on supp E_j) over the other coordinates
    u = []
    for j, (key, P) in enumerate(events):
        supp = [a for a, v in key]
        idx = [slice(None)] * N
        for a, v in key: idx[a] = slice(v - 1, v)
        Fj = Fl[j][tuple(idx)]  # pinned
        Fj = np.broadcast_to(Fj, shape).copy()
        u.append(es_trunc(Fj, [a for a in range(N) if a not in supp], t))
    B = np.ones(shape); v = np.zeros(shape)
    for i in range(m):
        B -= A[i] * (1 - v) ** 2
        v = v + A[i] * u[i]
    EF = F.mean(); gap = (F - B).mean(); mu = B.mean()
    print(f"(iii) m={m} events, max w={max(w):.5f} (c0={c0:.5f}), EF={EF:.5f}, max(B-F)={np.max(B-F):.2e}, "
          f"E[F-B]/EF={gap/EF:.2e} (needs <=1e-2 for Lemma 3.3)")
    worst_ratio = 0.0; chain_ok = True
    for r in range(1, N + 1):
        for S in itertools.combinations(range(N), r):
            psi = np.ones(shape)
            for a in S:
                leg = np.array([legendre(x, PRS[a]) for x in range(1, PRS[a])], dtype=float)
                sh = [1] * N; sh[a] = -1
                psi = psi * leg.reshape(sh)
            for l0 in S:
                Fp = np.ones(shape); bound1 = 0.0
                for i, (key, P) in enumerate(events):
                    if l0 not in [a for a, _ in key]: Fp *= (1 - A[i])
                for i, (key, P) in enumerate(events):
                    if l0 in [a for a, _ in key]:
                        rest = np.ones(shape, dtype=bool)
                        for a, vv in key:
                            if a != l0: rest &= (grids[a] == vv)
                        bound1 += (1 / (PRS[l0] - 1)) * (rest * Fp).mean()
                lhs = abs((F * psi).mean())
                chain_ok &= (lhs <= bound1 + 1e-15) and (bound1 <= 1.07 * w[l0] * Fp.mean() + 1e-15)
            worst_ratio = max(worst_ratio, abs((B * psi).mean()) / mu)
    print(f"      Lemma 3.3 chain holds for all (psi, l0): {chain_ok}; max |E[B psi]|/mu = {worst_ratio:.4f} (<=1/4 claimed when E[F-B]<=EF/100)")

if __name__ == "__main__":
    seed, t, nev = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    part_i(rng)
    part_ii_iii(rng, t, nev)
