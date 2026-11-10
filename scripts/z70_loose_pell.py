# z70 LOOSE item 4 (MINE open item): Pell residues modulo candidate LETTERS (Z70_LOOSE.md §1.4, pre-registered).
# For each prime p (<= 2e10) and its U7 witness words (x, y, z) (x = r, y = (f+1)/r, z = (p+r)/f), unique letters
# l in {x, y, z} with 5 <= l <= LMAX; negative Pell T^2 - p U^2 = -1 (T = h_{L-1}, U = k_{L-1} of the CF of sqrt p).
# Event D(l) = [l | v for some v in V], V = {T, U} u {T + cU + s : 1 <= |c| <= 3, |s| <= 2} u {T + s : 1 <= |s| <= 2}.
# Exact local null: (T, U) uniform on the conic T^2 - p U^2 = -1 (mod l) -> P0(l) computed exactly.
# Exact decoys: 2 per letter, z69_mine_qs2.decoy_exact (same 2-adic part, odd part +-5 %, same chi_p signature).
# usage: python z70_loose_pell.py <wit file> <prime list> <cap witnesses per prime (0=all)> <seed> <out.jsonl>
import sys, json, math, random
import numpy as np
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit
from z69_mine_qs2 import decoy_exact
LMAX = 200000; PMAX = 2 * 10**10
CS = [c for c in (-3, -2, -1, 1, 2, 3)]; SS = [-2, -1, 0, 1, 2]

def pell_mod(p, m):
    a0 = math.isqrt(p); P, Q, a = 0, 1, a0
    h0, h1, k0, k1 = 1 % m, a0 % m, 0, 1 % m
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q
        if Q == 1: break
        h0, h1 = h1, (a * h1 + h0) % m
        k0, k1 = k1, (a * k1 + k0) % m
    return h1, k1

def targets_T(U, l):
    """array (len(U), K) of T-values that make some v in V vanish mod l (U-dependent), plus the U-free ones"""
    cols = [(-c * U - s) % l for c in CS for s in SS]
    cols += [np.full_like(U, (-s) % l) for s in (-2, -1, 0, 1, 2)]   # T, T+s (s = 0 is v = T)
    return np.stack(cols, axis=1)

def null_prob(p, l):
    U = np.arange(l, dtype=np.int64)
    sq = np.bincount((U * U) % l, minlength=l)          # number of square roots of each residue
    r = ((p % l) * ((U * U) % l) - 1) % l
    total = int(sq[r].sum())                            # |conic mod l|
    if total == 0: return None
    TT = targets_T(U, l)
    ok = (TT * TT) % l == r[:, None]                    # candidate T lies on the conic over U
    TTs = np.where(ok, TT, -1); TTs.sort(axis=1)
    distinct = (TTs[:, 1:] != TTs[:, :-1]) & (TTs[:, 1:] >= 0)
    hitT = distinct.sum(axis=1) + (TTs[:, 0] >= 0)
    hits = hitT.copy()
    hits[0] = sq[r[0]]                                  # U = 0: v = U vanishes, every conic point over U = 0 is a hit
    return float(hits.sum()) / total

def D_event(T, U, l):
    if U % l == 0 or T % l == 0: return True
    for s in (-2, -1, 1, 2):
        if (T + s) % l == 0: return True
    for c in CS:
        for s in SS:
            if (T + c * U + s) % l == 0: return True
    return False

def main():
    wf, lf, cap, seed, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed)
    W = load_wit(wf)
    ps = [int(l.split()[0]) for l in open(lf) if l.strip() and not l.startswith('#')]
    fo = open(out, 'w')
    for p in ps:
        if p not in W or not W[p] or p > PMAX: continue
        wl = list(W[p]); rng.shuffle(wl)
        if cap: wl = wl[:cap]
        letters = {}
        for f, r, y, z in wl:
            for role, l in (('x', r), ('y', y), ('z', z)):
                if 5 <= l <= LMAX: letters.setdefault(l, set()).add(role)
        recs = []
        for l in sorted(letters):
            ds = [decoy_exact(p, l, rng) for _ in range(2)]
            if None in ds or max(ds) > LMAX: recs.append([l, ''.join(sorted(letters[l])), None]); continue
            recs.append([l, ''.join(sorted(letters[l])), ds])
        mods = {l for l, _, ds in recs} | {d for _, _, ds in recs if ds for d in ds}
        if not mods: continue
        M = 1
        for m in mods: M = M * m // math.gcd(M, m)
        T, U = pell_mod(p, M)
        rows = []
        for l, roles, ds in recs:
            row = {'l': l, 'roles': roles, 'D': D_event(T, U, l), 'P0': null_prob(p, l)}
            if ds:
                row['dec'] = [[d, D_event(T, U, d), null_prob(p, d)] for d in ds]
            rows.append(row)
        fo.write(json.dumps({'p': p, 'rows': rows}) + '\n'); fo.flush()

if __name__ == '__main__':
    main()
