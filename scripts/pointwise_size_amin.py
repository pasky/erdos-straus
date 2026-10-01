#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 8 -- the window frame.

For a prime p = 1 (mod 4) and q = 3 (mod 4) put x = (p+q)/4 (so q = 4x - p) and
    Rat_q(x) = { u/v mod q : u v | x, gcd(u,v)=1 }            (notes Thm 62.1, Lemma 77.1).
By notes Lemma 77.1, 4/p has a solution with p-free denominator x iff
Rat_q(x) meets {-1, -p}  (-1: Type II, -p: Type I).  Put
    a_min(p) = min{ q = 3 (mod 4) : Rat_q((p+q)/4) meets {-1,-p} }.
ES(p) <=> a_min(p) < infinity  (q ranges up to 3p).

Modes
  census N              all hard primes p = 1 (24), p < N  (SPF sieve)
  sample EXP NS SEED    NS random hard primes in [10^EXP, 2*10^EXP)
  class1 T NS SEED      NS random primes p = 1 (mod lcm(24, 1..T)), p < 10^6 * lcm
  formal K KMAX         'formal-generic' adversary: p = 24 q + 1 with (p+a)/4 = C_a * prime
                        for every window a <= K (a = 3 mod 4); a_min of the found p.
"""
import sys
import json
import random
from math import gcd, log
import numpy as np
from sympy import factorint, isprime, primerange


def rat_hits(fac, q, p, full=False):
    """Does Rat_q(x) (x with factorisation fac, gcd(x,q)=1) contain -1 or -p mod q?
    Returns None, or 'II' if -1 is in Rat_q(x) (a Type II solution exists at this window),
    else 'I' (only -p: Type I only).  With full=False the scan stops as soon as -1 appears;
    the label is intrinsic either way (it is computed on the completed set unless -1 is
    already present)."""
    t1, t2 = q - 1, (-p) % q
    S = np.zeros(q, dtype=bool)
    S[1] = True
    for r, e in fac.items():
        rr = r % q
        ri = pow(rr, -1, q)
        cur = np.flatnonzero(S)
        new = S.copy()
        a, b = cur.copy(), cur.copy()
        for _ in range(e):
            a = (a * rr) % q
            b = (b * ri) % q
            new[a] = True
            new[b] = True
        S = new
        if S[t1] and not full:
            return 'II'
    if S[t1]:
        return 'II'
    if S[t2]:
        return 'I'
    return None


def amin(p, factor, qmax=10 ** 7):
    q = 3
    while q <= qmax:
        x = (p + q) // 4
        if x % p:
            ty = rat_hits(factor(x), q, p)
            if ty:
                return q, ty
        q += 4
    return None, None


def census(N, MORDELL=0):
    X = N // 4 + 10 ** 5
    spf = np.zeros(X + 1, dtype=np.int32)
    for l in primerange(2, int(X ** 0.5) + 1):
        idx = np.arange(l, X + 1, l)
        z = spf[idx] == 0
        spf[idx[z]] = l

    def fac(x):
        f = {}
        while x > 1:
            l = int(spf[x]) or x
            f[l] = f.get(l, 0) + 1
            x //= l
        return f
    # primes p = 1 mod 24 below N
    sieve = np.ones(N, dtype=bool)
    sieve[:2] = False
    for l in primerange(2, int(N ** 0.5) + 1):
        sieve[l * l::l] = False
    ps = np.flatnonzero(sieve[1::24]) * 24 + 1
    ps = ps[sieve[ps]]
    if MORDELL:
        ps = ps[np.isin(ps % 5, [1, 4]) & np.isin(ps % 7, [1, 2, 4])]
    hist, rec, by_type = {}, [], {'I': 0, 'II': 0}
    best = 0
    dy = {}
    for p in ps.tolist():
        if p < 25:
            continue
        q, ty = amin(p, fac)
        hist[q] = hist.get(q, 0) + 1
        by_type[ty] += 1
        if q > best:
            best = q
            rec.append((p, q, ty))
        k = p.bit_length()
        if q > dy.get(k, (0, 0))[1]:
            dy[k] = (p, q)
    out = {'N': N, 'primes': int(len(ps)), 'hist': dict(sorted(hist.items())), 'records': rec,
           'type_of_min': by_type,
           'dyadic_max': {k: (p, q, round(q / log(p), 3), round(q * log(log(p)) / log(p), 3))
                          for k, (p, q) in sorted(dy.items())}}
    print(json.dumps(out))


def windows(N, QMAX, MORDELL=0):
    """Per-window failure statistics for all hard primes p < N, windows q <= QMAX:
    marginals f_q, the joint tail P(a_min > Q), the independence product, and the
    dependence on the least quadratic non-residue n_p."""
    X = N // 4 + QMAX
    spf = np.zeros(X + 1, dtype=np.int32)
    for l in primerange(2, int(X ** 0.5) + 1):
        idx = np.arange(l, X + 1, l)
        z = spf[idx] == 0
        spf[idx[z]] = l

    def fac(x):
        f = {}
        while x > 1:
            l = int(spf[x]) or x
            f[l] = f.get(l, 0) + 1
            x //= l
        return f
    sieve = np.ones(N, dtype=bool)
    sieve[:2] = False
    for l in primerange(2, int(N ** 0.5) + 1):
        sieve[l * l::l] = False
    ps = np.flatnonzero(sieve[1::24]) * 24 + 1
    ps = ps[sieve[ps]]
    ps = ps[ps > 4 * QMAX]
    if MORDELL:
        ps = ps[np.isin(ps % 5, [1, 4]) & np.isin(ps % 7, [1, 2, 4])]
    qs = list(range(3, QMAX + 1, 4))
    small_primes = list(primerange(3, 400))
    fails = np.zeros((len(ps), len(qs)), dtype=bool)
    nps = np.zeros(len(ps), dtype=np.int64)
    for i, p in enumerate(ps.tolist()):
        for j, q in enumerate(qs):
            fails[i, j] = rat_hits(fac((p + q) // 4), q, p) is None
        for l in small_primes:
            if pow(p % l, (l - 1) // 2, l) == l - 1:
                nps[i] = l
                break
    marg = fails.mean(axis=0)
    joint, indep = {}, {}
    cum = np.ones(len(ps), dtype=bool)
    prod = 1.0
    for j, q in enumerate(qs):
        cum &= fails[:, j]
        prod *= marg[j]
        joint[q] = float(cum.mean())
        indep[q] = prod
    bynp = {}
    for lo, hi in ((5, 13), (13, 20), (20, 30), (30, 400)):
        sel = (nps >= lo) & (nps < hi)
        if sel.sum() == 0:
            continue
        c = np.ones(int(sel.sum()), dtype=bool)
        row = {}
        for j, q in enumerate(qs):
            c &= fails[sel, j]
            if q in (3, 7, 11, 15, 23, 31, 47, 63):
                row[q] = float(c.mean())
        bynp[f'{lo}<=n_p<{hi}'] = {'count': int(sel.sum()), 'marg_q3_7_11': [float(fails[sel, j].mean()) for j in range(3)],
                                   'joint': row}
    out = {'N': N, 'primes': int(len(ps)), 'marginal_fail': dict(zip(qs, marg.round(5).tolist())),
           'joint_P_amin_gt_Q': joint, 'independence_product': indep, 'by_least_nonresidue': bynp}
    print(json.dumps(out))


def seeded(N, JMAX, MORDELL=1):
    """E2 seeding (section 9): windows q = -p (mod 4 n_p), n_p the least QNR mod p.
    Lemma 9.1: n_p | x and (n_p/q) = -1 (Jacobi), so these windows are never F1.
    Records the first successful seeded index j_min (tail), the per-index success rate on a
    1-in-20 subsample, the size of the first successful seeded q relative to a_min(p),
    and the distribution of n_p."""
    X = N // 4 + 4 * 400 * JMAX
    spf = np.zeros(X + 1, dtype=np.int32)
    for l in primerange(2, int(X ** 0.5) + 1):
        idx = np.arange(l, X + 1, l)
        z = spf[idx] == 0
        spf[idx[z]] = l

    def fac(x):
        f = {}
        while x > 1:
            l = int(spf[x]) or x
            f[l] = f.get(l, 0) + 1
            x //= l
        return f
    sieve = np.ones(N, dtype=bool)
    sieve[:2] = False
    for l in primerange(2, int(N ** 0.5) + 1):
        sieve[l * l::l] = False
    ps = np.flatnonzero(sieve[1::24]) * 24 + 1
    ps = ps[sieve[ps]]
    ps = ps[ps > 10 ** 5]
    if MORDELL:   # Mordell's six classes mod 840: p a QR mod 5 and 7, i.e. n_p >= 11
        ps = ps[np.isin(ps % 5, [1, 4]) & np.isin(ps % 7, [1, 2, 4])]
    succ_j = np.zeros(JMAX)
    tried_j = np.zeros(JMAX)
    jmin_hist = {}
    ratio, f1viol, npdist, worst = [], 0, {}, []
    for k, p in enumerate(ps.tolist()):
        n = next(l for l in primerange(3, 400) if pow(p % l, (l - 1) // 2, l) == l - 1)
        npdist[n] = npdist.get(n, 0) + 1
        q0 = (-p) % (4 * n)
        full = (k % 20 == 0)
        jm = None
        for j in range(JMAX):
            q = q0 + 4 * n * j
            x = (p + q) // 4
            if jacobi(n, q) != -1:
                f1viol += 1
            ok = rat_hits(fac(x), q, p) is not None
            if full:
                tried_j[j] += 1
                succ_j[j] += ok
            if ok and jm is None:
                jm = j
                if not full:
                    break
        jmin_hist[jm if jm is not None else -1] = jmin_hist.get(jm if jm is not None else -1, 0) + 1
        if jm is None or jm >= 5:
            worst.append((p, n, jm))
        if k % 50 == 0 and jm is not None:
            a, _ = amin(p, fac)
            ratio.append((q0 + 4 * n * jm) / a)
    r = np.array(ratio)
    tot = len(ps)
    tail = {}
    c = tot
    for j in range(JMAX):
        c -= jmin_hist.get(j, 0)
        tail[j + 1] = c / tot          # P(no success among the first j+1 seeded windows)
    out = {'N': N, 'JMAX': JMAX, 'primes': tot, 'lemma_9_1_violations': f1viol,
           'P_no_success_first_J': tail, 'jmin_hist': dict(sorted(jmin_hist.items())),
           'seeded_success_rate_by_j(subsample)': (succ_j / np.maximum(tried_j, 1)).round(4).tolist(),
           'median_ratio_first_seeded_q_over_amin(subsample)': float(np.median(r)),
           'n_p_distribution': dict(sorted(npdist.items())), 'worst': worst[:30]}
    print(json.dumps(out))


def sample_seeded(EXP, NS, seed, JMAX=20):
    """Mordell-hard primes near 10^EXP: first successful seeded window index j_min and,
    for comparison, a_min (unseeded)."""
    random.seed(seed)
    lo = 10 ** EXP
    jm, am, nps = [], [], []
    while len(jm) < NS:
        p = lo + random.randrange(lo)
        p -= (p - 1) % 24
        if p < lo or p % 5 in (2, 3) or p % 7 in (3, 5, 6) or not isprime(p):
            continue
        n = next(l for l in primerange(3, 10 ** 4) if pow(p % l, (l - 1) // 2, l) == l - 1)
        q0 = (-p) % (4 * n)
        j0 = JMAX
        for j in range(JMAX):
            q = q0 + 4 * n * j
            if rat_hits(factorint((p + q) // 4), q, p):
                j0 = j
                break
        jm.append(j0)
        am.append(amin(p, factorint)[0])
        nps.append(n)
    jm, am = np.array(jm), np.array(am)
    out = {'EXP': EXP, 'NS': NS, 'P_no_seeded_success_first_J': {J: float((jm >= J).mean()) for J in (1, 2, 3, 5, 10)},
           'P_amin_gt_4J-1': {J: float((am > 4 * J - 1).mean()) for J in (1, 2, 3, 5, 10)},
           'max_jmin': int(jm.max()), 'max_amin': int(am.max()), 'max_n_p': int(max(nps))}
    print(json.dumps(out))


def sample_windows(EXP, NS, seed, QMAX=31):
    """Mordell-hard primes near 10^EXP: per-window failure marginals for q <= QMAX and the
    geometric mean of the marginals (the single-window rate g used in section 8.4)."""
    random.seed(seed)
    lo = 10 ** EXP
    qs = list(range(3, QMAX + 1, 4))
    F = []
    while len(F) < NS:
        p = lo + random.randrange(lo)
        p -= (p - 1) % 24
        if p < lo or p % 5 in (2, 3) or p % 7 in (3, 5, 6) or not isprime(p):
            continue
        F.append([rat_hits(factorint((p + q) // 4), q, p) is None for q in qs])
    F = np.array(F)
    marg = F.mean(axis=0)
    joint = np.cumprod(F, axis=1).mean(axis=0)
    out = {'EXP': EXP, 'NS': NS, 'marginal_fail': dict(zip(qs, marg.round(4).tolist())),
           'geomean_marginal': float(np.exp(np.log(marg).mean())),
           'joint': dict(zip(qs, joint.tolist())), 'indep': dict(zip(qs, np.cumprod(marg).tolist()))}
    print(json.dumps(out))


def jacobi(a, n):
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def sample(EXP, NS, seed):
    random.seed(seed)
    vals = []
    lo = 10 ** EXP
    while len(vals) < NS:
        p = lo + random.randrange(lo)
        p -= (p - 1) % 24
        if p < lo or p % 5 in (2, 3) or p % 7 in (3, 5, 6) or not isprime(p):
            continue
        q, ty = amin(p, factorint)
        vals.append(q)
    v = np.array(vals)
    out = {'EXP': EXP, 'NS': NS, 'seed': seed, 'max': int(v.max()), 'mean': float(v.mean()),
           'tail': {Q: float((v > Q).mean()) for Q in (3, 7, 11, 15, 23, 31, 47, 63, 95, 127)},
           'log p': EXP * log(10)}
    print(json.dumps(out))


def class1(T, NS, seed):
    random.seed(seed)
    L = 24
    for k in range(2, T + 1):
        L = L * k // gcd(L, k)
    vals = []
    while len(vals) < NS:
        p = 1 + L * random.randrange(10 ** 5, 10 ** 6)
        if not isprime(p):
            continue
        q, ty = amin(p, factorint)
        vals.append((q, ty))
    v = np.array([a for a, _ in vals])
    out = {'T': T, 'L': L, 'log10 p ~': round(log(L * 5 * 10 ** 5, 10), 1), 'NS': NS, 'max': int(v.max()),
           'mean': float(v.mean()), 'tail': {Q: float((v > Q).mean()) for Q in (3, 7, 11, 15, 23, 31, 47, 63, 95, 127)},
           'frac_typeI': sum(1 for _, t in vals if t == 'I') / NS}
    print(json.dumps(out))


def formal(K, KMAX):
    """Adversary of Prop. 8.4 (generalised): p = 24q+1 prime, p a nonzero square mod every
    prime l <= K, and for every window a = 3 (mod 4), a <= K, (p+a)/4 = C_a * r_a with r_a
    prime and every prime factor of C_a in Lambda = {primes <= max(K,5)}.  Then every prime
    factor of every window is a QR mod p, so a_min(p) > K (Lemma CT).  Every hypothesis is
    re-checked for each accepted p."""
    windows = list(range(3, K + 1, 4))
    Lam = list(primerange(2, max(K, 5) + 1))
    rng = random.Random(K)
    from sympy.ntheory.modular import crt
    # 2-adic / 3-adic classes: least precision e with every window valuation < e+1 fixed
    # (6q+s = 6r+s mod 2^(e+1) resp. 2*3^(e+1) when q = r mod 2^e resp. 3^e)
    mods, rs = [], []
    for l, start in ((2, 3), (3, 1)):
        for e in range(start, 8):
            cand = [r for r in range(l ** e) if r % l and (l != 3 or (24 * r + 1) % 3)
                    and all(vl(6 * r + (a + 1) // 4, l) <= e for a in windows)]
            if cand:
                mods.append(l ** e)
                rs.append(rng.choice(cand))
                break
    for l in Lam:
        if l in (2, 3):
            continue
        sq = [r for r in range(l) if (24 * r + 1) % l and pow((24 * r + 1) % l, (l - 1) // 2, l) == 1]
        free = [r for r in sq if all((6 * r + (a + 1) // 4) % l for a in windows)]
        if free:            # root-avoiding: windows are l-units, precision l suffices
            mods.append(l)
            rs.append(rng.choice(free))
        else:               # forced: allow v_l = 1, fixed modulo l^2
            cand = [r for r in range(l * l) if r % l in sq
                    and all(vl(6 * r + (a + 1) // 4, l) < 2 for a in windows)]
            mods.append(l * l)
            rs.append(rng.choice(cand))
    qt = int(crt(mods, rs)[0])
    M = 1
    for m in mods:
        M *= m
    forms = [(6, (a + 1) // 4) for a in windows]
    consts = []
    for (al, be) in forms:
        v, C = al * qt + be, 1
        for l in Lam:
            while v % l == 0:
                v //= l
                C *= l
        consts.append(C)
    small = [l for l in primerange(2, 5000) if l not in Lam]
    found, rejected = [], 0
    chunk = 1_000_000
    for k0 in range(0, KMAX, chunk):
        ks = np.arange(k0, min(k0 + chunk, KMAX), dtype=np.int64)
        alive = np.ones(len(ks), dtype=bool)
        for (al, be) in [(24, 1)] + forms:
            for l in small:
                c1, c0 = (al * M) % l, (al * qt + be) % l
                if c1 == 0:
                    continue
                alive &= (ks % l) != ((-c0 * pow(c1, -1, l)) % l)
        for k in ks[alive].tolist():
            q = qt + M * k
            p = 24 * q + 1
            if not isprime(p):
                continue
            if not all((al * q + be) % C == 0 and isprime((al * q + be) // C)
                       for (al, be), C in zip(forms, consts)):
                continue
            # re-check every hypothesis of Prop. 8.4(a) (generalised) independently
            ok = all(pow(p % l, (l - 1) // 2, l) == 1 for l in Lam if l > 2) and p % 8 == 1
            for a in windows:
                for r in factorint((p + a) // 4):
                    if r != 2 and pow(r % p, (p - 1) // 2, p) != 1:
                        ok = False
            if not ok:
                rejected += 1
                continue
            a, ty = amin(p, factorint)
            found.append((p, a, ty))
    out = {'K': K, 'windows': len(windows), 'M': M, 'found': len(found), 'rejected_on_recheck': rejected,
           'p_range': [min(p for p, _, _ in found), max(p for p, _, _ in found)] if found else None,
           'amin': sorted(set(a for _, a, _ in found)),
           'all_exceed_K': all(a > K for _, a, _ in found), 'examples': found[:10]}
    print(json.dumps(out))


def vl(n, l):
    v = 0
    while n and n % l == 0:
        n //= l
        v += 1
    return v


if __name__ == '__main__':
    mode = sys.argv[1]
    a = [int(x) for x in sys.argv[2:]]
    {'census': census, 'windows': windows, 'seeded': seeded, 'sample_seeded': sample_seeded, 'sample_windows': sample_windows, 'sample': sample, 'class1': class1, 'formal': formal}[mode](*a)
