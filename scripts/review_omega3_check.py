#!/usr/bin/env python3
"""Independent hostile-review checks for POINTWISE_OMEGA3 (Thm 3.2, Lemma 3.1, Lemma 3.3).

Written from scratch (does not import omega3_compose_check.py).  Everything is
evaluated POINTWISE at an outcome x: the cells of B_3 that contain x are exactly
(U, x|_U); their merged coefficient is
    coef(U,x) = kappa(U,x) - 4^{L3+1} * cov(U,x),
    kappa(U,x) = sum_{F subset A_3(x), supp F = U} (-1)^{|F|}           (O2 Lemma 1.3(2))
    cov(U,x)   = #{(P,C): |P|=L3+1, C private cover of P, all of C occur, pi(C)=U}
and the composed minorant is B(x) = sum_U coef(U,x) * gamma_U(x) with gamma = beta
(coef>0) or alpha (coef<0) of the level-2 system conditioned on the cell (U,x|_U).

modes:
  compose  N seed     exhaustive B <= F2*F3 on random/adversarial systems (uniform measure)
  tilt     N seed     exact check of Lemma 3.1 (LLL lower bound, HSS tilt) under (P)
  push     N seed     exact check of Lemma 3.3 (post-conditions, F2F3 <= 1[no original], Markov masses)
"""
import itertools
import math
import random
import sys

# ---------------------------------------------------------------- basics
# event: tuple of (coord, frozenset(values)) sorted by coord


def mk(d):
    return tuple(sorted((l, frozenset(v)) for l, v in d.items()))


def supp(e):
    return frozenset(l for l, _ in e)


def occ(e, x):
    return all(x[l] in v for l, v in e)


def subfamilies(events, maxsupp):
    """all subfamilies F (tuples of indices) with |supp F| <= maxsupp, with their support."""
    out = []
    n = len(events)
    sp = [supp(e) for e in events]

    def rec(i, cur, s):
        out.append((cur, s))
        for j in range(i, n):
            s2 = s | sp[j]
            if len(s2) <= maxsupp:
                rec(j + 1, cur + (j,), s2)
    rec(0, (), frozenset())
    return out


def kappa_by_U(occ_events, L):
    d = {}
    for F, s in subfamilies(occ_events, L):
        d[s] = d.get(s, 0) + (-1) ** len(F)
    return d  # includes U=empty with value 1


def is_private_cover(C, P, sp):
    cover = frozenset().union(*[sp[i] for i in C]) if C else frozenset()
    if not P <= cover:
        return False
    for i in C:
        others = frozenset().union(*[sp[j] for j in C if j != i]) if len(C) > 1 else frozenset()
        if not ((sp[i] & P) - others):
            return False
    return True


def cov_by_U(occ_events, u):
    """G^cov_u(x) split by pi(C)."""
    d = {}
    sp = [supp(e) for e in occ_events]
    n = len(occ_events)
    for k in range(1, u + 1):
        for C in itertools.combinations(range(n), k):
            piC = frozenset().union(*[sp[i] for i in C])
            if len(piC) < u:
                continue
            cnt = sum(1 for P in itertools.combinations(sorted(piC), u)
                      if is_private_cover(C, frozenset(P), sp))
            if cnt:
                d[piC] = d.get(piC, 0) + cnt
    return d


def esym(vals, k):
    e = [1] + [0] * k
    for a in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * a
    return e[k]


def BL(occ_events, L):
    return sum(v for v in kappa_by_U(occ_events, L).values())


def graph_level(occ2, coords, L):
    """(B_L, G_{L+1}=e_{L+1}(a)) of O2 Lemma 1.2 for an occurring level-2 family."""
    a = [sum(1 for e in occ2 if l in supp(e)) for l in coords]
    return BL(occ2, L), esym(a, L + 1)


def conditioned_level2(lev2, U, x):
    """occurring events of the level-2 system conditioned on cell (U, x|U), evaluated at x.
    Returns None if the cell kills F_2 (some level-2 event inside U occurs)."""
    out = []
    for e in lev2:
        s = supp(e)
        inside = s & U
        if inside == s:
            if occ(e, x):
                return None
            continue
        if inside:
            # realised part must match the cell, else the event vanishes on the cell
            if all(x[l] in v for l, v in e if l in U):
                rest = tuple((l, v) for l, v in e if l not in U)  # induced event
                if occ(rest, x):
                    out.append(rest)
            continue
        if occ(e, x):
            out.append(e)
    return out


def composed_B(lev2, lev3, coords, x, L2, L3, merged=True, neg_control=False):
    o3 = [e for e in lev3 if occ(e, x)]
    kap = kappa_by_U(o3, L3)
    cov = cov_by_U(o3, L3 + 1)
    w = 4 ** (L3 + 1)
    terms = []  # (coef, U)
    if merged:
        allU = set(kap) | set(cov)
        for U in allU:
            c = kap.get(U, 0) - w * cov.get(U, 0)
            if c:
                terms.append((c, U))
    else:
        terms = [(c, U) for U, c in kap.items() if c] + [(-w * c, U) for U, c in cov.items() if c]
    B = 0
    B3 = 0
    for c, U in terms:
        B3 += c
        o2 = conditioned_level2(lev2, U, x)
        if o2 is None:
            continue
        rest = [l for l in coords if l not in U]
        b, g = graph_level(o2, rest, L2)
        beta, alpha = b - 4 ** (L2 + 1) * g, b + 4 ** (L2 + 1) * g
        F2i = 0 if o2 else 1
        assert beta <= F2i <= alpha
        if c > 0 or neg_control:
            B += c * beta
        else:
            B += c * alpha
    return B, B3


# ---------------------------------------------------------------- generators
def rand_vertex(rng, m, single=True):
    if single or rng.random() < 0.6:
        return frozenset([rng.randrange(m)])
    k = rng.randint(1, max(1, m - 1))
    return frozenset(rng.sample(range(m), k))


def gen_system(rng, kind):
    n = rng.randint(3, 5)
    alph = [rng.randint(2, 4) if n <= 4 else rng.randint(2, 3) for _ in range(n)]
    coords = list(range(n))
    lev2, lev3 = [], []
    singlev = kind != 'hyper_only' and rng.random() < 0.5

    def ev(cs, hubval=None):
        d = {}
        for l in cs:
            if hubval is not None and l == cs[0]:
                d[l] = frozenset([hubval % alph[l]])
            else:
                d[l] = rand_vertex(rng, alph[l], single=not singlev)
        return mk(d)
    n2 = rng.randint(0, 4)
    n3 = rng.randint(1, 6)
    for _ in range(n2):
        if rng.random() < 0.35:
            l = rng.randrange(n)
            lev2.append(mk({l: rand_vertex(rng, alph[l], single=False)}))
        else:
            lev2.append(ev(rng.sample(coords, 2)))
    for _ in range(n3):
        sz = 3 if rng.random() < 0.8 else 2
        lev3.append(ev(rng.sample(coords, min(sz, n))))
    if kind == 'hub':  # one vertex shared by many events of both levels
        h = rng.randrange(n)
        for _ in range(4):
            cs = [h] + rng.sample([l for l in coords if l != h], 2)
            lev3.append(ev(cs, hubval=0))
        for _ in range(2):
            cs = [h] + rng.sample([l for l in coords if l != h], 1)
            lev2.append(ev(cs, hubval=0))
    elif kind == 'nested':  # level-2 edges that are sub-pairs of level-3 events (push-down shape)
        for e in list(lev3)[:3]:
            items = list(e)
            if len(items) >= 2:
                lev2.append(tuple(sorted(rng.sample(items, 2))))
    elif kind == 'dense':
        for cs in itertools.combinations(coords, 3):
            lev3.append(mk({l: frozenset([0]) for l in cs}))
    elif kind == 'dup':
        lev3 += lev3[:2]
        lev2 += lev2[:1]
    return coords, alph, lev2, lev3


def run_compose(N, seed):
    rng = random.Random(seed)
    kinds = ['plain', 'hub', 'nested', 'dense', 'dup', 'hyper_only']
    viol = {'B<=F2F3': 0, 'B3<=F3': 0, 'unmerged B<=F2F3': 0}
    negviol = 0
    pts = 0
    stats = []
    for t in range(N):
        kind = kinds[t % len(kinds)]
        coords, alph, lev2, lev3 = gen_system(rng, kind)
        L2 = rng.randint(0, 3)
        L3 = rng.randint(0, 3)
        sumdef = 0.0
        sumF = 0
        for x in itertools.product(*[range(a) for a in alph]):
            pts += 1
            F2 = 0 if any(occ(e, x) for e in lev2) else 1
            F3 = 0 if any(occ(e, x) for e in lev3) else 1
            B, B3 = composed_B(lev2, lev3, coords, x, L2, L3, merged=True)
            if B > F2 * F3:
                viol['B<=F2F3'] += 1
            if B3 > F3:
                viol['B3<=F3'] += 1
            Bu, _ = composed_B(lev2, lev3, coords, x, L2, L3, merged=False)
            if Bu > F2 * F3:
                viol['unmerged B<=F2F3'] += 1
            Bn, _ = composed_B(lev2, lev3, coords, x, L2, L3, merged=True, neg_control=True)
            if Bn > F2 * F3:
                negviol += 1
            sumdef += F2 * F3 - B
            sumF += F2 * F3
        stats.append((kind, sumdef, sumF))
    print(f"compose N={N} seed={seed}: points={pts} violations={viol} neg-control violations={negviol}")
    return sum(viol.values())


# ---------------------------------------------------------------- tilt (Lemma 3.1)
def run_tilt(N, seed):
    """weighted product measure on {0..3}^n, value 0 = 'nothing'; (P) enforced by scaling."""
    rng = random.Random(seed)
    worst_ratio = 0.0
    worst_ratio_hss = 0.0
    worst_lll = 0.0
    bad = 0
    for _ in range(N):
        n = rng.randint(4, 6)
        coords = list(range(n))
        lev2, lev3 = [], []
        for _ in range(rng.randint(1, 6)):
            if rng.random() < 0.3:
                l = rng.randrange(n)
                lev2.append(mk({l: {rng.randint(1, 3)}}))
            else:
                a, b = rng.sample(coords, 2)
                lev2.append(mk({a: {rng.randint(1, 3)}, b: {rng.randint(1, 3)}}))
        for _ in range(rng.randint(1, 7)):
            cs = rng.sample(coords, 3)
            lev3.append(mk({l: {rng.randint(1, 3)} for l in cs}))
        # probabilities: q_l(v) for v=1..3, then scale until per-prime total mass <= 1/32 (tight)
        q = [[0.0] + [rng.random() for _ in range(3)] for _ in coords]

        def P(e):
            return math.prod(q[l][next(iter(v))] for l, v in e)
        for _ in range(60):
            tot = [sum(P(e) for e in lev2 + lev3 if l in supp(e)) for l in coords]
            mx = max(tot)
            if mx <= 1 / 32:
                break
            s = (1 / 32 / mx) ** 0.5
            q = [[0.0] + [v * s for v in row[1:]] for row in q]
        if max(sum(P(e) for e in lev2 + lev3 if l in supp(e)) for l in coords) > 1 / 32 + 1e-15:
            continue
        for l in coords:
            q[l][0] = 1 - sum(q[l][1:])
        pts = list(itertools.product(range(4), repeat=n))
        wts = [math.prod(q[l][x[l]] for l in coords) for x in pts]
        A2 = [0 if any(occ(e, x) for e in lev2) else 1 for x in pts]
        A3 = [0 if any(occ(e, x) for e in lev3) else 1 for x in pts]
        PA2 = sum(w for w, a in zip(wts, A2) if a)
        PA23 = sum(w for w, a, b in zip(wts, A2, A3) if a and b)
        lb = PA2 * math.prod(1 - 2 * P(e) for e in lev3)
        worst_lll = max(worst_lll, lb / PA23)
        if PA23 < lb * (1 - 1e-12):
            bad += 1
        # all private families C of level-3 events
        sp = [supp(e) for e in lev3]
        for k in range(1, len(lev3) + 1):
            for C in itertools.combinations(range(len(lev3)), k):
                if not all(sp[i] - frozenset().union(*[sp[j] for j in C if j != i]) for i in C):
                    continue
                piC = frozenset().union(*[sp[i] for i in C])
                PC = sum(w for w, x in zip(wts, pts) if all(occ(lev3[i], x) for i in C))
                if PC == 0:
                    continue
                lhs = sum(w for w, x, a in zip(wts, pts, A2) if a and all(occ(lev3[i], x) for i in C))
                rhs = PA2 * PC * math.exp(len(piC) / 2)
                gam = [e for e in lev2 if supp(e) & piC]
                rhs_hss = PA2 * PC * math.prod(1 / (1 - 2 * P(e)) for e in gam)
                worst_ratio = max(worst_ratio, lhs / rhs)
                worst_ratio_hss = max(worst_ratio_hss, lhs / rhs_hss)
                if lhs > rhs_hss * (1 + 1e-12) or lhs > rhs * (1 + 1e-12):
                    bad += 1
    print(f"tilt N={N} seed={seed}: failures={bad}  max LHS/RHS(e^(|U|/2))={worst_ratio:.4f}"
          f"  max LHS/RHS(HSS prod)={worst_ratio_hss:.4f}  max LLL-lb/P(A2&A3)={worst_lll:.4f}")
    return bad


# ---------------------------------------------------------------- push-down (Lemma 3.3)
def run_push(N, seed):
    rng = random.Random(seed)
    bad = 0
    pushes = [0, 0, 0]
    for _ in range(N):
        n = rng.randint(4, 6)
        m = rng.randint(2, 4)  # alphabet; uniform measure p(v)=1/m
        coords = list(range(n))
        p = 1.0 / m
        V = lambda l, a: (l, a)
        singles = set()
        edges = set()
        hyp = set()
        for _ in range(rng.randint(0, 3)):
            singles.add(V(rng.randrange(n), rng.randrange(m)))
        for _ in range(rng.randint(0, 5)):
            a, b = rng.sample(coords, 2)
            edges.add(frozenset([V(a, rng.randrange(m)), V(b, rng.randrange(m))]))
        hub = (rng.randrange(n), 0)
        for _ in range(rng.randint(2, 14)):
            cs = rng.sample(coords, 3)
            e = frozenset(V(l, rng.randrange(m)) for l in cs)
            if rng.random() < 0.4 and hub[0] in cs:
                e = frozenset([hub] + [v for v in e if v[0] != hub[0]])
            hyp.add(e)
        orig = ([frozenset([s]) for s in singles], list(edges), list(hyp))
        S1 = len(singles) * p
        S2 = len(edges) * p * p
        SH = len(hyp) * p ** 3
        # toy thresholds (scale-free check of the algebra): degrees are multiples of p^2
        d3 = rng.choice([p * p, 2 * p * p, 3 * p * p])
        t = rng.choice([p, 2 * p])
        dl = rng.choice([p, 2 * p, 3 * p])

        def deg3(v, H):
            return sum(p * p for e in H if v in e)

        def cod(O, H):
            return sum(p for e in H if O <= e)
        H = set(hyp)
        S = set(singles)
        E = set(edges)
        # (a)
        hubs = {v for e in H for v in e if deg3(v, H) > d3 + 1e-12}
        pushes[0] += len(hubs)
        S |= hubs
        H = {e for e in H if not (e & hubs)}
        # (b)
        pairs = {frozenset(O) for e in H for O in itertools.combinations(e, 2)}
        heavy = {O for O in pairs if cod(O, H) > t + 1e-12}
        pushes[1] += len(heavy)
        E |= heavy
        H = {e for e in H if not any(O <= e for O in heavy)}
        # (c)
        def deg2(v):
            return sum(p for e in E if v in e)
        hv = {v for e in E for v in e if deg2(v) > dl + 1e-12}
        pushes[2] += len(hv)
        S |= hv
        E = {e for e in E if not (e & hv)}
        H = {e for e in H if not (e & hv)}
        # post-conditions
        why = []
        if not all(deg3(v, H) <= d3 + 1e-12 for e in H for v in e): why.append('deg3')
        if not all(cod(frozenset(O), H) <= t + 1e-12 for e in H for O in itertools.combinations(e, 2)): why.append('cod')
        if not all(deg2(v) <= dl + 1e-12 for e in E for v in e): why.append('deg2')
        S1n, S2n, SHn = len(S) * p, len(E) * p * p, len(H) * p ** 3
        S2pushed = len(edges | heavy) * p * p  # S_2^{new} after (b), before (c) deletions
        if not SHn <= SH + 1e-12: why.append('SH')
        if not len(edges | heavy) * p * p <= S2 + 3 * SH / t + 1e-12: why.append('S2')
        if not S1n <= S1 + 3 * SH / d3 + 2 * S2pushed / dl + 1e-12: why.append('S1')
        ok = not why
        # pointwise F2F3 <= 1[no original event]
        for x in itertools.product(range(m), repeat=n):
            real = {(l, x[l]) for l in coords}
            newocc = any(s in real for s in S) or any(e <= real for e in E) or any(e <= real for e in H)
            oldocc = any(s in real for s in singles) or any(e <= real for e in edges) or any(e <= real for e in hyp)
            if oldocc and not newocc:
                ok = False
                why.append('pointwise')
                break
        if not ok:
            bad += 1
            if bad <= 3:
                print('  FAIL', why, 'n,m=', n, m, 'S1,S2,SH=', S1, S2, SH, 'new', S1n, S2n, SHn, 'thr', d3, t, dl, 'hubs', len(hubs), 'heavy', len(heavy), 'hv', len(hv))
    print(f"push N={N} seed={seed}: failures={bad}  pushes (a,b,c)={pushes}")
    return bad


if __name__ == '__main__':
    mode, N, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    f = {'compose': run_compose, 'tilt': run_tilt, 'push': run_push}[mode](N, seed)
    sys.exit(1 if f else 0)
