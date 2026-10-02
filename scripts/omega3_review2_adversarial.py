"""Independent adversarial brute force for O2 Lemmas 1.2/10.1/10.2/2.1 and the
O3 use-site claims (conditional LLL tilt, cell-conditioned codegrees/masses).
Written from scratch for reviews/pointwise-omega3-review-2.md.

Model: primes 0..n-1, X_l in {0..m_l-1} with arbitrary probabilities q_l.
A vertex is (l, value); an event is a frozenset of vertices at distinct primes.
Usage: python omega3_review2_adversarial.py SEED TRIALS
Exit code 1 on any violation."""
import itertools as it, math, random, sys
from math import comb, e, exp

TOL = 1e-9
import os
NEG = os.environ.get('NEG') == '1'  # negative control: drop higher-codegree terms
viol = []
stats = {}
def st(key, ratio):
    c, mx = stats.get(key, (0, 0.0))
    stats[key] = (c + 1, max(mx, ratio))

def rand_system(rng, n, mmax, nev, kmax, dense=False):
    if dense and rng.random() < .4:
        # cluster mode: one heavy vertex per prime, events = random subsets
        m = [2] * n
        q = []
        for l in range(n):
            a = rng.uniform(.3, .97); q.append([a, 1 - a])
        evs = set()
        for _ in range(nev):
            sz = rng.randint(1, kmax)
            evs.add(frozenset((l, 0) for l in rng.sample(range(n), min(sz, n))))
        return m, q, sorted(evs, key=lambda E: sorted(E))
    m = [rng.randint(2, mmax) for _ in range(n)]
    q = []
    for l in range(n):
        w = [rng.random() ** (3 if dense else 1) for _ in range(m[l])]
        s = sum(w); q.append([x / s for x in w])
    evs = set()
    for _ in range(nev):
        sz = rng.randint(1, kmax)
        ps = rng.sample(range(n), min(sz, n))
        # bias toward value 0/1 so vertices are shared (hubs)
        evs.add(frozenset((l, rng.choice([0, 0, 1, rng.randrange(m[l])])) for l in ps))
    return m, q, sorted(evs, key=lambda E: sorted(E))

def pv(q, v):
    return q[v[0]][v[1]]

def pev(q, E):
    r = 1.0
    for v in E:
        r *= pv(q, v)
    return r

def outcomes(m, q):
    for x in it.product(*[range(k) for k in m]):
        pr = 1.0
        for l, xl in enumerate(x):
            pr *= q[l][xl]
        yield x, pr

def occurs(E, x):
    return all(x[l] == a for (l, a) in E)

def supp(E):
    return frozenset(l for (l, _) in E)

def priv_count_by_size(C):
    """#P of each size privately covered by family C (list of events)."""
    S = [supp(E) for E in C]
    allp = frozenset().union(*S) if S else frozenset()
    privs = []
    for i, Si in enumerate(S):
        others = frozenset().union(*[S[j] for j in range(len(S)) if j != i]) if len(S) > 1 else frozenset()
        privs.append(Si - others)
    if any(not pr for pr in privs):
        return {}
    allp = sorted(allp); cnt = {}
    for r in range(len(allp) + 1):
        for P in it.combinations(allp, r):
            Ps = set(P)
            if all(Ps & pr for pr in privs):
                cnt[r] = cnt.get(r, 0) + 1
    return cnt

def is_private(C):
    S = [supp(E) for E in C]
    for i, Si in enumerate(S):
        others = set().union(*[S[j] for j in range(len(S)) if j != i]) if len(S) > 1 else set()
        if not (Si - others):
            return False
    return True

def cover_G(A, umax):
    G = [0] * (umax + 1)
    G[0] = 1
    for r in range(1, len(A) + 1):
        for C in it.combinations(A, r):
            for u, c in priv_count_by_size(list(C)).items():
                if 1 <= u <= umax:
                    G[u] += c
    return G

# ---------- T1: Lemma 1.1/1.2/10.1 pointwise + 10.1(2) mass ----------
def T1(rng, tag):
    n = rng.randint(3, 5)
    m, q, evs = rand_system(rng, n, 3, rng.randint(3, 9), 3)
    EG = {}
    for L in range(0, n + 1):
        EGu = [0.0] * (L + 2)
        for x, pr in outcomes(m, q):
            A = [E for E in evs if occurs(E, x)]
            V = set().union(*[supp(E) for E in A]) if A else set()
            N = len(V)
            BL = 0
            for r in range(len(A) + 1):
                for F in it.combinations(A, r):
                    if len(set().union(*[supp(E) for E in F])) <= L:
                        BL += (-1) ** r
            G = cover_G(A, L + 1)
            ind = 1 if not A else 0
            for u in range(L + 2):
                EGu[u] += pr * G[u]
                if comb(N, u) > G[u]:
                    viol.append((tag, 'binom(N,u)>Gcov', x, u))
            st('T1 outcomes', 0)
            if BL - 4 ** (L + 1) * G[L + 1] > ind + TOL or abs(BL - ind) > 4 ** (L + 1) * G[L + 1] + TOL:
                viol.append((tag, 'Lemma1.2/10.1 pointwise', x, L))
        # 10.1(2): M1(B_L) <= sum_{u<=L} 2^u E Gcov_u via cell coefficients
        M1 = 0.0
        for r in range(L + 1):
            for U in it.combinations(range(n), r):
                for c in it.product(*[range(m[l]) for l in U]):
                    cell = dict(zip(U, c))
                    AU = [E for E in evs if supp(E) <= set(U) and all(cell[l] == a for (l, a) in E)]
                    kap = 0
                    for s in range(len(AU) + 1):
                        for F in it.combinations(AU, s):
                            if set().union(*[supp(E) for E in F]) == set(U):
                                kap += (-1) ** s
                    pc = 1.0
                    for l in U:
                        pc *= q[l][cell[l]]
                    M1 += abs(kap) * pc
        rhs = sum(2 ** u * EGu[u] for u in range(L + 1))
        if M1 > 0: st('10.1(2) mass', M1 / rhs)
        if M1 > rhs + TOL:
            viol.append((tag, 'Lemma10.1(2) mass', L, M1, rhs))

# ---------- T2: Lemma 10.2 per-h component bound (hypothesis free) ----------
def codeg(q, H, O):
    O = frozenset(O)
    return sum(pev(q, E - O) for E in H if O < E)

def Delta_max(q, H, i):
    verts = sorted(set().union(*H)) if H else []
    best = 0.0
    for O in it.combinations(verts, i):
        if len({l for (l, _) in O}) < i:
            continue
        best = max(best, codeg(q, H, O))
    return best

def connected(K):
    K = list(K); seen = {0}; stack = [0]
    while stack:
        i = stack.pop()
        for j in range(len(K)):
            if j not in seen and K[i] & K[j]:
                seen.add(j); stack.append(j)
    return len(seen) == len(K)

def T2(rng, tag, w):
    n = rng.randint(4, 7)
    m, q, evs = rand_system(rng, n, 3, rng.randint(6, 18), 3, dense=rng.random() < .5)
    H = [E for E in evs if len(E) >= 2]
    if not H:
        return
    k = max(len(E) for E in H)
    SH = sum(pev(q, E) for E in H)
    Dm = {i: Delta_max(q, H, i) for i in range(1, k)}
    for h in range(1, min(5, len(H)) + 1):
        lhs = 0.0
        for K in it.combinations(H, h):
            if not connected(K) or not is_private(K):
                continue
            V = set().union(*K)
            if len({l for (l, _) in V}) < len(V):
                continue
            lhs += (1 + w) ** len(V) * pev(q, frozenset(V))
        Dh = sum((k * h) ** j * Dm[j + 1] for j in range(0, k - 1))
        rhs = (1 + w) ** (k * h) * e * k * SH * (k * e * Dh) ** (h - 1)
        if lhs > 0 and h >= 2:
            st(('10.2 per-h', h), lhs / rhs)
        if lhs > rhs * (1 + 1e-9) + TOL:
            viol.append((tag, 'Lemma10.2 per-h', h, lhs, rhs))

# ---------- T2b: Lemma 10.2 full statement, scaled into its hypothesis ----------
def T2b(rng, tag, w):
    n = rng.randint(4, 6)
    m, q, evs = rand_system(rng, n, 3, rng.randint(5, 12), 3)
    # shrink probabilities: put mass eps on values, rest on a null value
    eps = rng.choice([0.003, 0.01, 0.03])
    q2 = []
    for l in range(n):
        q2.append([x * eps for x in q[l]] + [1 - eps])
    m2 = [k + 1 for k in m]
    H = [E for E in evs if len(E) >= 2]
    S1 = sum(pev(q2, E) for E in evs if len(E) == 1)
    k = max([len(E) for E in evs] + [2])
    for U0 in (1, 2, 3):
        D = sum((k * U0) ** j * Delta_max(q2, H, j + 1) for j in range(0, k - 1)) if H else 0
        if D > 1 / (2 * e * k * (1 + w) ** k):
            continue
        SH = sum(pev(q2, E) for E in H)
        lhs = 0.0
        for x, pr in outcomes(m2, q2):
            A = [E for E in evs if occurs(E, x)]
            G = cover_G(A, U0)
            lhs += pr * sum(w ** u * G[u] for u in range(U0 + 1))
        rhs = exp((1 + w) * S1 + 2 * e * k * (1 + w) ** k * SH)
        st('10.2 full', lhs / rhs)
        if lhs > rhs + TOL:
            viol.append((tag, 'Lemma10.2 full', U0, lhs, rhs))
        T2b.checked += 1
T2b.checked = 0

# ---------- T3: Lemma 2.1 tree / pseudoforest component counts ----------
def T3(rng, tag):
    n = rng.randint(4, 7)
    m, q, evs = rand_system(rng, n, 3, rng.randint(6, 16), 2, dense=rng.random() < .5)
    Ed = [E for E in evs if len(E) == 2]
    if not Ed:
        return
    S2 = sum(pev(q, E) for E in Ed)
    verts = sorted(set().union(*Ed))
    delta = max(codeg(q, Ed, [v]) for v in verts)
    for nv in range(2, min(6, len(verts)) + 1):
        lt = lp = 0.0
        for r in range(nv - 1, nv + 1):
            for K in it.combinations(Ed, r):
                V = set().union(*K)
                if len(V) != nv or not connected(K):
                    continue
                if len({l for (l, _) in V}) < nv:
                    continue
                pk = pev(q, frozenset(V))
                lp += pk
                if r == nv - 1:
                    lt += pk
        if lt > 0: st(('2.1 trees', nv), lt / (2 * S2 * e ** nv * delta ** (nv - 2)))
        if lt > 2 * S2 * e ** nv * delta ** (nv - 2) + TOL:
            viol.append((tag, 'Lemma2.1 trees', nv, lt))
        if lp > (1 + nv * nv / 2) * 2 * S2 * e ** nv * delta ** (nv - 2) + TOL:
            viol.append((tag, 'Lemma2.1 pseudoforests', nv, lp))

# ---------- T4: conditional LLL tilt (O3 Lemma 3.1(2)) exact ----------
def T4(rng, tag):
    n = rng.randint(3, 5)
    m, q, evs = rand_system(rng, n, 4, rng.randint(3, 10), 2)
    eps = rng.choice([0.1, 0.2, 0.3])
    q = [[x * eps for x in ql] + [1 - eps] for ql in q]
    m = [k + 1 for k in m]
    x_ = {E: 2 * pev(q, E) for E in evs}
    # check asymmetric LLL condition; skip if fails
    for E in evs:
        prod = 1.0
        for F in evs:
            if F != E and supp(F) & supp(E):
                prod *= 1 - x_[F]
        if pev(q, E) > x_[E] * prod:
            return
    PA = PAB = 0.0
    U = rng.sample(range(n), rng.randint(1, n))
    Bset = set(it.product(*[range(m[l]) for l in U]))
    Bset = set(rng.sample(sorted(Bset), max(1, len(Bset) // 3)))
    PB = 0.0
    for x, pr in outcomes(m, q):
        inB = tuple(x[l] for l in U) in Bset
        void = not any(occurs(E, x) for E in evs)
        PA += pr * void; PAB += pr * (void and inB); PB += pr * inB
    g = 1.0
    for F in evs:
        if supp(F) & set(U):
            g /= 1 - x_[F]
    st('condLLL', PAB / (PA * PB * g))
    if PAB > PA * PB * g + TOL:
        viol.append((tag, 'cond LLL', PAB, PA * PB * g))

# ---------- T5: cell conditioning (O3 Thm 5.1 codegree/mass inequalities) ----------
def T5(rng, tag):
    n = rng.randint(5, 7)
    m, q, evs = rand_system(rng, n, 3, rng.randint(6, 16), 4, dense=True)
    H = [E for E in evs if len(E) >= 2]
    if not H:
        return
    r = max(len(E) for E in H)
    Pi = rng.sample(range(n), rng.randint(1, 3))
    xi = {l: rng.randrange(m[l]) for l in Pi}
    fixed = [(l, xi[l]) for l in Pi]
    h = len(fixed)
    cond = []
    killed = False
    for E in H:
        inside = [v for v in E if v[0] in xi]
        if any(xi[l] != a for (l, a) in inside):
            continue
        rest = frozenset(v for v in E if v[0] not in xi)
        if not rest:
            killed = True
            continue
        cond.append((rest, frozenset(inside)))
    if killed:
        return
    Dm = {i: Delta_max(q, H, i) for i in range(1, r)}
    # induced mass
    Sind = sum(pev(q, R) for (R, F) in cond if F)
    bound = sum(comb(h, i) * Dm.get(i, 0) for i in range(1, 2 if NEG else r))
    if Sind > 0: st('S_induced', Sind / bound)
    if Sind > bound + TOL:
        viol.append((tag, 'S_induced', Sind, bound))
    cH = [R for (R, F) in cond if len(R) >= 1]
    verts = sorted(set().union(*cH)) if cH else []
    for s in range(1, r):
        for O in it.combinations(verts, s):
            if len({l for (l, _) in O}) < s:
                continue
            Dp = codeg(q, cH, O)
            b = sum(comb(h, i) * Dm.get(s + i, 0) for i in range(0, 1 if NEG else r - s))
            if Dp > 0: st("Delta'", Dp / b)
            if Dp > b + TOL:
                viol.append((tag, "Delta'_O", O, Dp, b))
    # F = F^(i) on the cell, pointwise
    for x, pr in outcomes(m, q):
        if any(x[l] != xi[l] for l in Pi):
            continue
        F = not any(occurs(E, x) for E in H)
        Fi = not any(occurs(R, x) for (R, _) in cond)
        if F != Fi:
            viol.append((tag, 'F!=F^(i) on cell', x))

def main():
    seed, trials = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    for t in range(trials):
        T1(rng, ('T1', t))
        for w in (0.0, 1.0, 16.0, 17 * e ** .5 - 1):
            T2(rng, ('T2', t, w), w)
        T2b(rng, ('T2b', t, 0.0), 0.0); T2b(rng, ('T2b', t, 1.0), 1.0)
        T3(rng, ('T3', t)); T4(rng, ('T4', t)); T5(rng, ('T5', t))
    print(f'seed={seed} trials={trials} T2b_in_hypothesis={T2b.checked} violations={len(viol)}')
    for kk in sorted(stats, key=str):
        print('  ', kk, 'n=%d max lhs/rhs=%.3g' % stats[kk])
    from collections import Counter
    print('violations by type:', dict(Counter(v[1] for v in viol)))
    for v in viol[:20]:
        print(v)
    sys.exit(1 if viol else 0)

if __name__ == '__main__':
    main()
