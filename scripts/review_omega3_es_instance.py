#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA3: a small END-TO-END instance of the construction.

T small, y with y^4 > T (so rough parts have <=3 prime factors), Pi_0 = {l <= y},
iterated quarantine (O2 Lemma 11.2) at a toy threshold c0, the distinct surviving
events (singles / edges / 3-hyperedges), push-down (Lemma 3.3 (a),(b),(c)) at toy
thresholds chosen so that every step fires, and the two-level composed minorant B
(Thm 3.2) at small truncations L3, L2, evaluated POINTWISE at integers n = 1 mod Q.

Checks, against an independent brute-force W(n) (min M<=T, M=3 mod 4, with
n mod M in R(M)={-4D mod M : D | A_M^2}):
  * (I):   no original event at n  =>  W(n) > T
  * minorant:  B(n) <= 1[W(n) > T]   for random n and for constructed survivors
  * certificate: some n with B(n) > 0 (hence W(n) > T, confirmed by brute force).
Deviation from the text: vertices are classes mod l^a (not lifted to l^{e_l}); this
changes no pointwise statement.

usage: review_omega3_es_instance.py T y c0 L3 L2 nrand nsurv seed [quantile]
  quantile (default 0.97): toy push-down thresholds = this quantile of deg3 / pair codegree / deg2
"""
import math
import random
import sys
from collections import defaultdict

from review_omega3_check import composed_B, occ, supp


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_of_square(A):
    ds = [1]
    for p, e in factor(A).items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


class Cls:
    """the class res mod m, as a 'value set' for coordinate values x_l = n mod l^{e_l}."""
    __slots__ = ('m', 'r')

    def __init__(self, m, r):
        self.m, self.r = m, r % m

    def __contains__(self, v):
        return v % self.m == self.r

    def __eq__(self, o):
        return (self.m, self.r) == (o.m, o.r)

    def __lt__(self, o):
        return (self.m, self.r) < (o.m, o.r)

    def __hash__(self):
        return hash((self.m, self.r))

    def __repr__(self):
        return f"{self.r}%{self.m}"


def phi_pp(l, a):
    return l ** (a - 1) * (l - 1)


def main():
    T, y, c0, L3, L2, nrand, nsurv, seed = (int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]),
                                            int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]),
                                            int(sys.argv[7]), int(sys.argv[8]))
    qu = float(sys.argv[9]) if len(sys.argv) > 9 else 0.97
    qc = float(sys.argv[10]) if len(sys.argv) > 10 else qu
    assert y ** 4 > T
    rng = random.Random(seed)
    P = primes_upto(T)
    Rset = {}
    atoms = []  # (M, cls mod M)
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        cl = {(-4 * D) % M for D in divisors_of_square(A)}
        Rset[M] = cl
        atoms += [(M, c) for c in cl]
    fac = {M: factor(M) for M in Rset}

    def events_for(Pi):
        ev = {}
        for M, c in atoms:
            f = fac[M]
            m = math.prod(l ** a for l, a in f.items() if l in Pi)
            r = M // m
            if r == 1:
                continue
            if (c - 1) % m != 0:  # survives iff m | 4D+1 iff  c = -4D = 1 mod m
                continue
            key = tuple(sorted((l, a, c % l ** a) for l, a in f.items() if l not in Pi))
            ev[key] = 1.0 / math.prod(phi_pp(l, a) for l, a, _ in key)
        return ev
    Pi = {l for l in P if l <= y}
    while True:
        ev = events_for(Pi)
        w = defaultdict(float)
        for key, pr in ev.items():
            for l, _, _ in key:
                w[l] += pr
        add = {l for l, v in w.items() if v > c0}
        if not add:
            break
        Pi |= add
    bad = sorted(l for l in Pi if l > y)
    e_l = {l: int(math.floor(math.log(T) / math.log(l) + 1e-12)) for l in P}
    while any(l ** (e_l[l] + 1) <= T for l in P):
        for l in P:
            while l ** (e_l[l] + 1) <= T:
                e_l[l] += 1
    for l in P:
        while l ** e_l[l] > T:
            e_l[l] -= 1
    Q = 24
    for l in Pi:
        Q = Q * l ** e_l[l] // math.gcd(Q, l ** e_l[l])

    def mkev(key):
        return tuple(sorted((l, Cls(l ** a, r)) for l, a, r in key))
    singles = [k for k in ev if len(k) == 1]
    edges = [k for k in ev if len(k) == 2]
    hyp = [k for k in ev if len(k) == 3]
    assert all(len(k) <= 3 for k in ev)
    S1, S2, SH = (sum(ev[k] for k in singles), sum(ev[k] for k in edges), sum(ev[k] for k in hyp))
    print(f"T={T} y={y} c0={c0}: |Pi|={len(Pi)} bad={bad[:12]}{'...' if len(bad) > 12 else ''} "
          f"log Q={math.log(Q):.1f}  #single/edge/hyp={len(singles)}/{len(edges)}/{len(hyp)}  "
          f"S1,S2,SH={S1:.3f},{S2:.4f},{SH:.5f}  max w_l={max(w.values()) if w else 0:.4f}")

    # ---- push-down (Lemma 3.3) at toy thresholds; vertices = (l, a, r)
    def pv(v):
        return 1.0 / phi_pp(v[0], v[1])
    H = {frozenset(k) for k in hyp}
    deg3 = defaultdict(float)
    for e in H:
        for v in e:
            deg3[v] += math.prod(pv(u) for u in e if u != v)
    d3 = sorted(deg3.values())[int(qu * len(deg3))] if deg3 else 1
    hubs = {v for v, d in deg3.items() if d > d3}
    H = {e for e in H if not (e & hubs)}
    nH_a = len(H)
    cod = defaultdict(float)
    for e in H:
        for v in e:
            for u in e:
                if u < v:
                    cod[frozenset((u, v))] += pv([z for z in e if z not in (u, v)][0])
    t = sorted(cod.values())[int(qu * len(cod))] if cod else 1
    heavy = {O for O, c in cod.items() if c > t}
    H = {e for e in H if not any(O <= e for O in heavy)}
    nH_b = len(H)
    E = {frozenset(k) for k in edges} | heavy
    deg2 = defaultdict(float)
    for e in E:
        for v in e:
            deg2[v] += pv([u for u in e if u != v][0])
    dl = sorted(deg2.values())[min(len(deg2) - 1, int(qc * len(deg2)))] if deg2 else 1
    hv = {v for v, d in deg2.items() if d > dl}
    E = {e for e in E if not (e & hv)}
    H = {e for e in H if not (e & hv)}
    S = {frozenset(k) for k in singles} | {frozenset([v]) for v in hubs | hv}
    print(f"push-down: (a) {len(hubs)} hub vertices (deg3>{d3:.2e}), (b) {len(heavy)} heavy pairs "
          f"(cod>{t:.2e}), (c) {len(hv)} level-2 hubs (deg2>{dl:.2e});  final #single/edge/hyp="
          f"{len(S)}/{len(E)}/{len(H)}  (#hyp after a,b: {nH_a},{nH_b})")
    lev2 = [mkev(sorted(s)) for s in S] + [mkev(sorted(e)) for e in E]
    lev3 = [mkev(sorted(e)) for e in H]
    orig = [mkev(k) for k in ev]
    # index by prime for fast occurrence tests
    free = sorted({l for k in ev for l, _, _ in k})
    mods = {l: l ** e_l[l] for l in free}

    def xof(n):
        return {l: n % mods[l] for l in free}

    idx = {}

    def occurring(fam, x):
        key = id(fam)
        if key not in idx:
            d = defaultdict(list)
            for e in fam:
                l0, c0_ = e[0]
                d[(l0, c0_.r % l0)].append(e)
            idx[key] = d
        d = idx[key]
        return [e for l in free for e in d.get((l, x[l] % l), ()) if occ(e, x)]

    def W_gt_T(n):
        return all(n % M not in cl for M, cl in Rset.items())

    def evalB(n):
        x = xof(n)
        o2, o3 = occurring(lev2, x), occurring(lev3, x)
        F2, F3 = (0 if o2 else 1), (0 if o3 else 1)
        coords = sorted({l for e in o2 + o3 for l in supp(e)})
        # composed_B only needs the occurring events; non-occurring ones contribute nothing
        B, B3 = composed_B(o2_full(x), o3, coords, x, L2, L3)
        return B, F2 * F3

    def o2_full(x):
        # conditioned_level2 needs level-2 events that are partially realised on a cell; it is
        # enough to pass those with at least one realised vertex at x (others vanish or don't occur)
        return [e for e in lev2 if any(x[l] in v for l, v in e)]

    by_prime = defaultdict(list)
    for e in orig + lev2 + lev3:
        for l in supp(e):
            by_prime[l].append(e)
    stats = dict(rand=0, rand_W=0, viol=0, I_viol=0, surv=0, surv_pos=0, surv_fail=0, planted=0, planted_B3cells=0, maxB=0.0, minB=0.0)
    musum = 0.0
    for i in range(nrand + nsurv):
        if i < nrand:
            n = 1 + Q * rng.randrange(10 ** 40)
        else:
            # constructed survivor: CRT residues chosen prime by prime avoiding every event
            # (original and final levels); every other one is PLANTED: a random level-3 event
            # is forced first, so that the level-3 cells of B_3 are exercised.
            planted = (i - nrand) % 2 == 1 and lev3
            okk = False
            for _ in range(200):
                res = {}
                if planted:
                    e3 = rng.choice(lev3)
                    for l, c in e3:
                        res[l] = (c.r + c.m * rng.randrange(mods[l] // c.m)) % mods[l]
                okk = True
                for l in free:
                    if l in res:
                        continue
                    choices = (r for r in (rng.randrange(mods[l]) for _ in range(400)) if r % l)
                    for r in choices:
                        res[l] = r
                        if not any(all(l2 in res for l2, _ in e) and occ(e, res) for e in by_prime[l]):
                            break
                    else:
                        okk = False
                        break
                if okk:
                    break
            if not okk:
                stats['surv_fail'] += 1
                continue
            stats['planted'] += bool(planted)
            # assemble n = 1 mod Q, = res[l] mod l^{e_l}
            n, mod = 1, Q
            for l in free:
                m = mods[l]
                k = ((res[l] - n) * pow(mod, -1, m)) % m
                n, mod = n + mod * k, mod * m
            n += mod * rng.randrange(10 ** 6)
        x = xof(n)
        noev = not occurring(orig, x)
        Wgt = W_gt_T(n)
        if noev and not Wgt:
            stats['I_viol'] += 1
        B, F = evalB(n)
        if B > (1 if Wgt else 0):
            stats['viol'] += 1
        if i < nrand:
            stats['rand'] += 1
            stats['rand_W'] += Wgt
            musum += B
        else:
            stats['surv'] += 1
            if B > 0:
                stats['surv_pos'] += 1
                assert Wgt
                if stats['surv_pos'] == 1:
                    print(f"  certificate: n (≡1 mod Q, {n.bit_length()} bits, n mod 10^12={n % 10**12}) B(n)={B}  W(n)>T by brute force: {Wgt}")
        stats['maxB'] = max(stats['maxB'], B)
        stats['minB'] = min(stats['minB'], B)
        if i % 10 == 0:
            print('   progress', i, stats, flush=True)
    print(f"L3={L3} L2={L2}: {stats}  MC mean of B over random n: {musum / max(1, nrand):.4g}")
    sys.exit(1 if stats['viol'] or stats['I_viol'] else 0)


if __name__ == '__main__':
    main()
