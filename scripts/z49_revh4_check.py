#!/usr/bin/env python3
"""Independent hostile-review checks for H4_NOT_POLYLOG.md (branch side-agent/z49-h4lower).

Written from scratch (does not import the author's checker).  Sections:
  A  gcd identities of Lemma 3
  B  conditional Haar probability phi(gcd(m,Q))/phi(m) of eq. (2)
  C  safe point n=1 (Lemma 2) and the two omitted edges are non-certifying at p = 1 (mod 24)
  D  growth of the inflated masses (3), (4)
  E  hard-prime controls (H4, A_min)
  F  BRW identity F - B = sum_i A_i (sum_{j<i} A_j (F_<j - u_j))^2
  G  digit-filtration energy inequality (10) with REAL congruence events incl. 2-adic digits
     above a fixed 2^3, absolute digit weights, unconditioned and conditioned on a cylinder.
"""
import math, random, itertools, sys, json
from math import gcd
import numpy as np

out = {}

def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r

# ---------------- A
rng = random.Random(4049)
bad = 0
for _ in range(200000):
    a = rng.randint(1, 10**6); v = rng.randint(a + 1, a + 10**6)
    if gcd(a * v, a + v + 1) != gcd(a * (a + 1), a + v + 1):
        bad += 1
    d = rng.randint(1, 10**5); k = rng.randint(1, 10**5)
    A = d * k - 1
    if A >= 2 and gcd(A, d + 1) != gcd(d + 1, k + 1):
        bad += 1
out['A_gcd_failures'] = bad

# ---------------- B
bad = 0; tested = 0
for _ in range(3000):
    Q = rng.choice([8, 24, 120, 840, 16 * 3, 8 * 9 * 5, 32 * 7])
    m = rng.randint(2, 400)
    b = rng.randint(0, m - 1)
    if gcd(b, m) != 1:
        continue
    if (b - 1) % gcd(m, Q) != 0:
        continue
    N = Q * m // gcd(Q, m)
    units = [n for n in range(N) if gcd(n, N) == 1 and n % Q == 1 % Q]
    hit = sum(1 for n in units if n % m == b)
    tested += 1
    if hit * phi(m) != len(units) * phi(gcd(m, Q)):
        bad += 1
out['B_condprob'] = {'tested': tested, 'failures': bad}

# ---------------- C
H = 300
safe_edge = [(a, v) for v in range(2, H + 1) for a in range(1, v) if gcd(a, v) == 1 and (1 + a + v) % (a * v) == 0]
safe_cov = [(A, d) for A in range(2, H + 1) for d in range(1, A) if (A + 1) % d == 0 and (1 + d) % A == 0]
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0
def cert(t, u, v):
    return any(x % 4 == 0 for x in (t, u, v, t * u - 1, t * v - 1))
noncert = all(not cert((p + 3) // 2, 1, 2) and not cert((p + 5) // 6, 2, 3) for p in range(1, 24 * 10000, 24))
out['C_safe'] = {'edges_at_1': safe_edge, 'cover_at_1': safe_cov, 'omitted_noncert_p1mod24': noncert,
                 'G2_empty': True, 'jacobi(-2,3)': jacobi(-2, 3)}

# ---------------- D
def masses(H):
    e = 0.0
    for v in range(2, H + 1):
        for a in range(1, v):
            e += gcd(a * v, a + v + 1) / (a * v)
    c = 0.0
    for A in range(2, H + 1):
        for d in range(1, A):
            if (A + 1) % d == 0:
                c += gcd(A, d + 1) / A
    L = math.log(3 * H)
    return {'H': H, 'edge': e, 'edge/L^4': e / L**4, 'edge/L^2': e / L**2, 'cov': c, 'cov/L^3': c / L**3, 'cov/L^2': c / L**2}
out['D_mass'] = [masses(H) for H in (64, 256, 1024, 2048)]

# ---------------- E
def H4_Amin(p):
    best = None
    edges = []
    # enumerate edges u<v with uv | p+u+v ; v | p+u => u = (-p mod v) or u = v-? ; brute by v up to bound
    # edge u<v: v | p+u means u ≡ -p (mod v), u in [1,v-1] unique
    for v in range(2, 2000):
        u = (-p) % v
        if u == 0 or u >= v:
            continue
        if (p + u + v) % (u * v) == 0:
            t = (p + u + v) // (u * v)
            if cert(t, u, v):
                best = v
                break
    amin = None
    for A in range(2, 5000):
        r = p % A
        d = (-r) % A  # p ≡ -d (mod A)
        if 1 <= d < A and (A + 1) % d == 0:
            Aodd = A
            while Aodd % 2 == 0:
                Aodd //= 2
            if Aodd > 1 and jacobi(-d, Aodd) == -1:
                amin = A
                break
    return best, amin
hard = [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281]
out['E_hard'] = {p: H4_Amin(p) for p in hard}

# ---------------- F + G : digit model
def build(primes_spec):
    """primes_spec: list of (l, i0, f). Returns axes list [(l,i)], ranges, per-prime residue arrays on grid."""
    axes = []; sizes = []
    for (l, i0, f) in primes_spec:
        for i in range(i0, f):
            axes.append((l, i))
            sizes.append(l - 1 if i == 0 else l)
    grids = np.indices(sizes)
    res = {}
    k = 0
    for (l, i0, f) in primes_spec:
        base = 1 % (l ** i0) if i0 > 0 else 0
        r = np.full(sizes, base, dtype=np.int64)
        for i in range(i0, f):
            dig = grids[k] + (1 if i == 0 else 0)
            r = r + dig * l ** i
            k += 1
        res[l] = r
    return axes, sizes, res

def es_energy(Fa, axes, sizes, weightfun):
    """Exact Efron-Stein over digit axes; returns sum_U w(U) ||F^{=U}||^2 and total."""
    nd = len(axes)
    cond = {}
    for mask in range(1 << nd):
        drop = tuple(ax for ax in range(nd) if not (mask >> ax) & 1)
        cond[mask] = Fa.mean(axis=drop, keepdims=True) if drop else Fa
    G = 0.0; tot = 0.0
    for U in range(1 << nd):
        comp = np.zeros(sizes)
        sub = U
        while True:
            sgn = -1 if bin(U ^ sub).count('1') % 2 else 1
            comp = comp + sgn * np.broadcast_to(cond[sub], sizes)
            if sub == 0:
                break
            sub = (sub - 1) & U
        e = float((comp ** 2).mean())
        tot += e
        G += weightfun([axes[a] for a in range(nd) if (U >> a) & 1]) * e
    return G, tot

def mU(dset):
    mx = {}
    for (l, i) in dset:
        mx[l] = max(mx.get(l, -1), i)
    return math.prod(l ** (i + 1) for l, i in mx.items())

def rand_event(spec, T, rng):
    for _ in range(1000):
        ev = {}
        m = 1
        for (l, i0, f) in spec:
            v = rng.randint(0, f)
            if m * l ** v > T:
                v = 0
            if v > i0:
                # residue mod l^v, unit, ≡1 mod l^i0
                while True:
                    r = rng.randrange(l ** v)
                    if r % l != 0 and (i0 == 0 or r % l ** i0 == 1 % l ** i0):
                        break
                ev[l] = (v, r)
                m *= l ** v
        if ev:
            return ev, m
    return None, None

def ev_ind(ev, res):
    ind = None
    for l, (v, r) in ev.items():
        x = (res[l] % l ** v) == r
        ind = x if ind is None else (ind & x)
    return ind.astype(float)

spec = [(2, 3, 6), (3, 0, 2), (5, 0, 2), (7, 0, 1)]
axes, sizes, res = build(spec)
grng = random.Random(77)
maxG = 0.0; maxGc = 0.0; maxGrel = 0.0; ntr = 0; brw_err = 0.0
for trial in range(120):
    T = grng.choice([64, 128, 200, 400, 576, 1600])
    Lc = math.log(T)
    nev = grng.randint(2, 6)
    evs = []
    for _ in range(nev):
        ev, m = rand_event(spec, T, grng)
        if ev:
            evs.append(ev)
    if len(evs) < 2:
        continue
    inds = [ev_ind(e, res) for e in evs]
    F = np.ones(sizes)
    for I in inds:
        F = F * (1 - I)
    wabs = lambda d: 2 ** (math.log(mU(d)) / (2 * Lc)) if d else 1.0
    G, tot = es_energy(F, axes, sizes, wabs)
    maxG = max(maxG, G)
    # conditioned on cylinder of event 0: restrict grid
    e0 = evs[0]
    spec_c = []
    for (l, i0, f) in spec:
        if l in e0:
            spec_c.append((l, max(i0, e0[l][0]), f))
        else:
            spec_c.append((l, i0, f))
    # build conditioned grid with fixed lower digits equal to e0's residue
    axes_c = []; sizes_c = []
    for (l, i0, f) in spec_c:
        for i in range(i0, f):
            axes_c.append((l, i)); sizes_c.append(l - 1 if i == 0 else l)
    grids = np.indices(sizes_c) if sizes_c else None
    res_c = {}; k = 0
    for (l, i0, f), (l2, i00, _) in zip(spec_c, spec):
        if l in e0:
            base = e0[l][1]
        else:
            base = 1 % l ** i00 if i00 > 0 else 0
        r = np.full(sizes_c, base, dtype=np.int64)
        for i in range(i0, f):
            r = r + (grids[k] + (1 if i == 0 else 0)) * l ** i
            k += 1
        res_c[l] = r
    Fc = np.ones(sizes_c)
    for e in evs[1:]:
        Fc = Fc * (1 - ev_ind(e, res_c))
    Gc, _ = es_energy(Fc, axes_c, sizes_c, wabs)
    maxGc = max(maxGc, Gc)
    # BRW identity with random u_j
    Fl = [np.ones(sizes)]
    for I in inds:
        Fl.append(Fl[-1] * (1 - I))
    us = [np.random.default_rng(trial + j).normal(size=sizes) for j in range(len(inds))]
    B = np.ones(sizes)
    for i, Ai in enumerate(inds):
        Y = 1 - sum((inds[j] * us[j] for j in range(i)), np.zeros(sizes))
        B = B - Ai * Y ** 2
    rhs = sum((inds[i] * sum((inds[j] * (Fl[j] - us[j]) for j in range(i)), np.zeros(sizes)) ** 2 for i in range(len(inds))), np.zeros(sizes))
    brw_err = max(brw_err, float(np.abs((F - B) - rhs).max()))
    ntr += 1
out['F_brw_max_discrepancy'] = brw_err
out['G_energy'] = {'trials': ntr, 'max_weighted_energy_uncond': maxG, 'max_weighted_energy_cond': maxGc}

# Stress test: single 2-adic cylinder at the tight modulus, weight should be exactly 1-P^2 style <= 1
T = 64; Lc = math.log(T)
ev = {2: (6, 1 + 8 * 5)}  # n ≡ 41 mod 64 on fibre n≡1 mod 8
F = 1 - ev_ind(ev, res)
G, _ = es_energy(F, axes, sizes, lambda d: 2 ** (math.log(mU(d)) / (2 * Lc)) if d else 1.0)
out['G_single_2adic_cylinder_m=T=64'] = G
print(json.dumps(out, indent=1, default=str))
