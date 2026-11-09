# z69 MINE: systematic relation search between U7 witnesses of p and a dictionary of p-intrinsic values.
# Usage: python scripts/z69_mine_scan.py H.wit H.feat.jsonl C.wit C.feat.jsonl [out.txt]
# For each prime p: witnesses (f, r=x, y, z=t) from z69_mine_allwit.c, features from z69_mine_feat.py.
# Dictionary families D_fam(p) (positive integers) and Pell residues; tests per witness:
#   eq   : some v in D equals one of x, y, z, f, f+1                     (v >= 3)
#   divf : f | v                                                          (v != 0)
#   divq : q | v for a prime q | f, q >= 5
#   divl : l | v for a letter l in {x, y, z}, l >= 5
#   vdiv : v | f+1 or v | x or v | y or v | z (v >= 5)
# REAL = dictionary of p vs witnesses of p; SHUF = dictionary of a size-neighbour p' vs witnesses of p
# (two shuffles: next and previous neighbour in the sorted list, averaged). The shuffle keeps the size
# distribution and destroys any p-specific link. Reported per (family, test): total hits, #primes with a hit.
import sys, json, math, collections
import numpy as np
from sympy import factorint

def load_wit(fn):
    wit = {}; cur = None
    for l in open(fn):
        a = l.split()
        if a[0] == 'W': cur = int(a[1]); wit[cur] = []
        else: wit[cur].append(tuple(map(int, a)))
    return wit

def lin(u, v, R=3):
    out = set()
    for al in range(0, R + 1):
        for be in range(-R, R + 1):
            if (al, be) in ((1, 0), (0, 1), (0, 0)): continue
            if al == 0 and be <= 0: continue
            if math.gcd(al, abs(be)) != 1: continue
            out.add(abs(al * u + be * v))
    out.discard(0); return out

def dictionary(F):
    p = F['p']; a, b, c, d, e, g = F['a'], F['b'], F['c'], F['d'], F['e'], F['g']
    D = {}
    D['G1'] = {a, b}
    D['G2'] = lin(a, b)
    D['G3'] = {a * b, abs(a * a - b * b), abs(a * a - 2 * b * b), abs(2 * a * a - b * b), a * a + 2 * b * b,
               2 * a * a + b * b, 2 * a * b, (a * a + 3 * b * b), (3 * a * a + b * b)} - {0}
    D['C1'] = {c, d}; D['C2'] = lin(c, d)
    D['E1'] = {e, g}; D['E2'] = lin(e, g)
    X = set()
    if F['u3']: X |= set(F['u3']) | lin(*F['u3'], R=2)
    if F['s7']: X |= set(F['s7']) | lin(*F['s7'], R=2)
    D['N37'] = X - {0}
    D['CL'] = {F['hm4'], F['hm8'], F['hp'], F['hm4'] // 4, F['hm8'] // 4, F['np'], F['nq7']} - {0}
    D['CFq'] = set(F['quots']) | {F['a0'] + k for k in range(-3, 4)} | {F['L']}
    D['QS'] = set(F['Qset'])
    return D

_cf = {}
def cf_seq(p):
    if p not in _cf:
        a0 = math.isqrt(p); P, Q, a = 0, 1, a0
        seq = [a0]
        while True:
            P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q
            seq.append(a)
            if Q == 1: break
        _cf[p] = np.array(seq, dtype=np.int64)
    return _cf[p]

def pell_mod(p, mods):
    """fundamental solution (T, U) of T^2 - p U^2 = -1 (p prime = 1 mod 4: CF period L odd), reduced mod each m;
    T/U = h_{L-1}/k_{L-1}. Vectorised over the moduli (all < 2^40, quotients < 2^20: no int64 overflow)."""
    seq = cf_seq(p); L = len(seq) - 1
    m = np.array(mods, dtype=np.int64)
    h0 = np.ones_like(m) % m; h1 = seq[0] % m; k0 = np.zeros_like(m); k1 = np.ones_like(m) % m
    for i in range(1, L):
        h0, h1 = h1, (seq[i] * h1 + h0) % m
        k0, k1 = k1, (seq[i] * k1 + k0) % m
    return {int(mm): (int(a), int(b)) for mm, a, b in zip(m, h1, k1)}, L

def pell_vals(T, U, m):
    return {'T': T, 'U': U, 'T+1': (T + 1) % m, 'T-1': (T - 1) % m, 'U+1': (U + 1) % m, 'U-1': (U - 1) % m,
            'T+U': (T + U) % m, 'T-U': (T - U) % m, 'T+2U': (T + 2 * U) % m, 'T-2U': (T - 2 * U) % m}

def main():
    Hw, Hf, Cw, Cf = sys.argv[1:5]
    wit = load_wit(Hw); wit.update(load_wit(Cw))
    feat = {}
    tag = {}
    for fn, t in ((Hf, 'H'), (Cf, 'C')):
        for l in open(fn):
            F = json.loads(l); feat[F['p']] = F; tag[F['p']] = t
    ps = sorted(feat)
    nb = {}
    for i, p in enumerate(ps):
        nb[p] = (ps[(i + 1) % len(ps)], ps[i - 1])
    tests = ['eq', 'divf', 'divq', 'divl', 'vdiv']
    # counters[(group, mode, fam, test)] = [total hits, primes with hit]
    cnt = collections.defaultdict(lambda: [0, 0])
    npr = collections.Counter()
    fq = {}
    pell_cache = {}
    need = collections.defaultdict(set)
    for p in ps:
        for q in (p,) + nb[p]:
            need[q] |= {f for f, r, y, t in wit[p]}
    PMall = {}
    for q in ps:
        PMall[q], _ = pell_mod(q, sorted(need[q]))
    print('pell done', file=sys.stderr, flush=True)
    for p in ps:
        W = wit[p]
        if not W: continue
        grp = tag[p]; npr[grp] += 1
        for f, r, y, t in W:
            if f not in fq: fq[f] = [q for q in factorint(f) if q >= 5]
        mods = sorted({f for f, r, y, t in W})
        dicts = {'real': [dictionary(feat[p])], 'shuf': [dictionary(feat[q]) for q in nb[p]]}
        pmods = {'real': [PMall[p]], 'shuf': [PMall[q] for q in nb[p]]}
        for mode in ('real', 'shuf'):
            w = 1.0 / len(dicts[mode])
            for D, PM in zip(dicts[mode], pmods[mode]):
                hitany = collections.Counter()
                for fam, vals in D.items():
                    for f, r, y, t in W:
                        letters = [v for v in (r, y, t) if v >= 5]
                        for v in vals:
                            h = {}
                            h['eq'] = v >= 3 and v in (r, y, t, f, f + 1)
                            h['divf'] = v % f == 0
                            h['divq'] = any(v % q == 0 for q in fq[f])
                            h['divl'] = any(v % l == 0 for l in letters)
                            h['vdiv'] = v >= 5 and ((f + 1) % v == 0 or r % v == 0 or y % v == 0 or t % v == 0)
                            for te in tests:
                                if h[te]:
                                    cnt[(grp, mode, fam, te)][0] += w; hitany[(fam, te)] = 1
                # Pell: relations m | expr(T,U) for m = f (divf) and q | f (divq)
                for f, r, y, t in W:
                    T, U = PM[f]
                    for nm, val in pell_vals(T, U, f).items():
                        if val == 0:
                            cnt[(grp, mode, 'PELL', 'divf')][0] += w; hitany[('PELL', 'divf')] = 1
                        if any(val % q == 0 for q in fq[f]):
                            cnt[(grp, mode, 'PELL', 'divq')][0] += w; hitany[('PELL', 'divq')] = 1
                for te in tests:
                    if any(k[1] == te for k in hitany):
                        hitany[('ANY', te)] = 1
                for k in hitany:
                    cnt[(grp, mode) + k][1] += w
    out = open(sys.argv[5], 'w') if len(sys.argv) > 5 else sys.stdout
    fams = sorted({k[2] for k in cnt})
    print('primes:', dict(npr), file=out)
    print('%-5s %-5s | %-28s | %-28s' % ('fam', 'test', 'H real/shuf (hits; primes)', 'C real/shuf (hits; primes)'), file=out)
    for fam in fams:
        for te in tests:
            row = []
            for grp in ('H', 'C'):
                R = cnt[(grp, 'real', fam, te)]; S = cnt[(grp, 'shuf', fam, te)]
                if R == [0, 0] and S == [0, 0]: row.append('-'); continue
                z = (R[0] - S[0]) / math.sqrt(S[0] + 1)
                row.append('%7.1f/%7.1f z=%+5.1f; %4.0f/%6.1f' % (R[0], S[0], z, R[1], S[1]))
            if row == ['-', '-']: continue
            print('%-5s %-5s | %s | %s' % (fam, te, row[0], row[1]), file=out)

if __name__ == '__main__':
    main()
