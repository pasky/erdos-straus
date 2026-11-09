# z69 MINE: "phantom prime" test — does p-intrinsic data know anything about a witness f beyond p mod f?
# For a witness f of p (word (r, y, z)), a phantom is a prime p' = p + k f (8 | k, p' prime) — then f is also a
# witness of p' with word (r, y, z' = (p'+r)/f): the local event "p mod f in T_f" is identical. Under the null
# (p's global data — Gaussian / norm-form representations, CF of sqrt p, Pell unit, class number — is independent
# of the witness given p mod f), relation hits between the dictionary and the witness have the same rate for p
# and p'. Excess for the real p = p-intrinsic information about the witness (the brief's target).
# Usage: python z69_mine_phantom.py <wit file> <max witnesses per prime> <phantoms per witness> <seed> <out>
import sys, json, math, random, collections
import numpy as np, cypari2
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit, lin, pell_vals
from z69_mine_feat import rep, cf_sqrt
from sympy import factorint, isprime
pari = cypari2.Pari(); pari.allocatemem(1 << 30)

def lite_feats(p, cf=True):
    F = {'p': p}
    ab = rep('1,0,1', p); a, b = (ab if ab[0] % 2 else ab[::-1]); F['a'], F['b'] = a, b
    F['c'], F['d'] = rep('1,0,2', p)
    g = 1
    while True:
        e2 = p + 2 * g * g; e = math.isqrt(e2)
        if e * e == e2: break
        g += 1
    F['e'], F['g'] = e, g
    F['u3'] = rep('1,0,3', p) if p % 3 == 1 else None
    F['s7'] = rep('1,0,7', p) if pow(p, 3, 7) == 1 else None
    F['hm4'] = int(pari('qfbclassno(%d)' % (-4 * p)))
    q = 2
    while pow(q, (p - 1) // 2, p) == 1: q = int(pari('nextprime(%d)' % (q + 1)))
    F['np'] = q
    q = 7
    while not (q % 8 == 7 and pow(p % q, (q - 1) // 2, q) == q - 1): q = int(pari('nextprime(%d)' % (q + 1)))
    F['nq7'] = q
    if cf and p < BIG:
        a0, L, quots, Qs = cf_sqrt(p)
        F['a0'] = a0; F['L'] = L; F['quots'] = quots[:12] + quots[L // 2 - 1:L // 2 + 2]; F['Qset'] = sorted(set(Qs))
    else:
        F['a0'] = None
    return F

def dictionary(F):
    a, b, c, d, e, g = F['a'], F['b'], F['c'], F['d'], F['e'], F['g']
    D = {}
    D['G1'] = {a, b}; D['G2'] = lin(a, b)
    D['G3'] = {a * b, abs(a * a - b * b), abs(a * a - 2 * b * b), abs(2 * a * a - b * b), a * a + 2 * b * b,
               2 * a * a + b * b, 2 * a * b, a * a + 3 * b * b, 3 * a * a + b * b} - {0}
    D['C1'] = {c, d}; D['C2'] = lin(c, d); D['E1'] = {e, g}; D['E2'] = lin(e, g)
    X = set()
    if F['u3']: X |= set(F['u3']) | lin(*F['u3'], R=2)
    if F['s7']: X |= set(F['s7']) | lin(*F['s7'], R=2)
    D['N37'] = X - {0}
    D['CL'] = {F['hm4'], F['hm4'] // 4, F['np'], F['nq7']} - {0}
    D['G4'] = {abs(a ** 3 - 3 * a * b * b), abs(3 * a * a * b - b ** 3), a ** 3 + b ** 3, abs(a ** 3 - b ** 3),
               abs(a ** 4 - 6 * a * a * b * b + b ** 4), abs(4 * a ** 3 * b - 4 * a * b ** 3)} - {0}
    D['CFpA'] = set()
    for A in (a, b, c, d, e, g):
        D['CFpA'] |= set(cf_conv_den(F['p'], A))
    D['CFpA'] -= {0, 1}
    if F['a0'] is not None:
        D['CFq'] = set(F['quots']) | {F['a0'] + k for k in range(-3, 4)} | {F['L']}
        D['QS'] = set(F['Qset'])
    return D

def pell_one(p, m):
    a0 = math.isqrt(p); P, Q, a = 0, 1, a0
    h0, h1, k0, k1 = 1 % m, a0 % m, 0, 1 % m
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q
        if Q == 1: break      # h1/k1 is now the convergent h_{L-1}/k_{L-1}
        h0, h1 = h1, (a * h1 + h0) % m
        k0, k1 = k1, (a * k1 + k0) % m
    return h1, k1

MATCH = False
XZ = False
BIG = 10 ** 12
TESTS = ['eqxyf', 'eqz', 'divf', 'divq', 'divxy', 'divz', 'vdivxy', 'vdivz']

def cf_conv_den(num, den, cap=200):
    """denominators of the convergents of num/den (regular CF)"""
    out = []; k0, k1 = 1, 0
    while den and len(out) < cap:
        q, rem = divmod(num, den)
        k0, k1 = k1, q * k1 + k0
        out.append(k1); num, den = den, rem
    return out

def hits(D, PT, f, r, y, z, fq, F=None):
    """relation hits between dictionary D (and Pell / convergent data PT) and the witness word (r, y, z) of f.
    eqxyf: v in {x, y, f, f+1};  eqz: v = z;  divf: f | v;  divq: q | v (prime q | f, q >= 5);
    divxy: x or y (>= 5) divides v;  divz: z (>= 5) divides v;  vdivxy: v (>= 5) divides f+1 = xy;  vdivz: v | z."""
    out = collections.Counter()
    xy = [v for v in (r, y) if v >= 5]
    for fam, vals in D.items():
        for v in vals:
            if v >= 3 and v in (r, y, f, f + 1): out[(fam, 'eqxyf')] += 1
            if v >= 3 and v == z: out[(fam, 'eqz')] += 1
            if v % f == 0: out[(fam, 'divf')] += 1
            if any(v % q == 0 for q in fq): out[(fam, 'divq')] += 1
            if any(v % l == 0 for l in xy): out[(fam, 'divxy')] += 1
            if z >= 5 and v % z == 0: out[(fam, 'divz')] += 1
            if v >= 5 and (f + 1) % v == 0: out[(fam, 'vdivxy')] += 1
            if v >= 5 and z % v == 0: out[(fam, 'vdivz')] += 1
    if PT is None: return out
    T, U, nzk, nzh, nzkq, nzhq = PT
    for nm, val in pell_vals(T, U, f).items():
        if val == 0: out[('PELL', 'divf')] += 1
        if any(val % q == 0 for q in fq): out[('PELL', 'divq')] += 1
    # all convergents h_i/k_i of sqrt p over one period: f | k_i, f | h_i ; q | k_i, q | h_i
    if nzk: out[('CFk', 'divf')] += nzk
    if nzh: out[('CFh', 'divf')] += nzh
    if nzkq: out[('CFk', 'divq')] += nzkq
    if nzhq: out[('CFh', 'divq')] += nzhq
    return out

def pell_full(p, f, fq):
    """Pell residues mod f plus counts of convergents (h_i, k_i), 0 <= i < L, with f | k_i, f | h_i, q | k_i, q | h_i"""
    a0 = math.isqrt(p); P, Q, a = 0, 1, a0
    mods = [f] + fq
    h0 = [1 % m for m in mods]; h1 = [a0 % m for m in mods]; k0 = [0] * len(mods); k1 = [1 % m for m in mods]
    nzk = nzh = nzkq = nzhq = 0
    def tally():
        nonlocal nzk, nzh, nzkq, nzhq
        nzk += k1[0] == 0; nzh += h1[0] == 0
        nzkq += any(k == 0 for k in k1[1:]); nzhq += any(h == 0 for h in h1[1:])
    tally()
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q
        if Q == 1: break
        for i, m in enumerate(mods):
            h0[i], h1[i] = h1[i], (a * h1[i] + h0[i]) % m
            k0[i], k1[i] = k1[i], (a * k1[i] + k0[i]) % m
        tally()
    return h1[0], k1[0], nzk, nzh, nzkq, nzhq

SIZE_SENSITIVE = ('CFq', 'QS', 'CFpA', 'CFk', 'CFh')

def main():
    import argparse
    global MATCH, XZ, BIG
    ap = argparse.ArgumentParser(description='phantom-prime relation test (see header)')
    ap.add_argument('wit'); ap.add_argument('cap', type=int); ap.add_argument('K', type=int)
    ap.add_argument('seed', type=int); ap.add_argument('out')
    ap.add_argument('mode', nargs='?', default='same', choices=['same', 'match', 'xz', 'xzm'])
    ap.add_argument('--big', type=int, default=10 ** 12, help='no CF/Pell data for primes >= big')
    ap.add_argument('--maxp', type=int, default=2 * 10 ** 10)
    a = ap.parse_args()
    MATCH, XZ, BIG = a.mode == 'match', a.mode in ('xz', 'xzm'), a.big
    XZM = a.mode == 'xzm'
    cap, K = a.cap, a.K
    rng = random.Random(a.seed)
    wit = load_wit(a.wit)
    fo = open(a.out, 'w')
    order = sorted(wit); rng.shuffle(order)          # random order: a time-limited run is a random subsample
    for p in order:
        if p > a.maxp or not wit[p]: continue
        W = list(wit[p]); rng.shuffle(W); W = W[:cap]
        Fp = lite_feats(p); Dp = dictionary(Fp)
        if MATCH:   # profile-matched phantoms are ~1e3 x larger: drop the size-sensitive families altogether
            for fam in SIZE_SENSITIVE: Dp.pop(fam, None)
        for f, r, y, z in W:
            fq = [q for q in factorint(f) if q >= 5]
            fqs = set(factorint(f))
            real = hits(Dp, (pell_full(p, f, fq) if not MATCH else pell_one(p, f) + (0, 0, 0, 0)), f, r, y, z, fq)
            phs = []
            tries = 0
            if MATCH:
                step = 840 * f
                while len(phs) < K and tries < 20000:
                    tries += 1
                    j = rng.randint(-max(1, p // step), 400)
                    if j == 0: continue
                    q = p + j * step
                    if q < max(17, (f - 1) // 2) or q in phs: continue
                    if any(l not in fqs and pow(q % l, (l - 1) // 2, l) != pow(p % l, (l - 1) // 2, l) for l in (11, 13, 17, 19, 23)):
                        continue
                    if isprime(q): phs.append(q)
            if XZ:
                # (x,z)-phantom: p' = p + 8j x z, |p' - p| <= p/2, word (x, y + 8j, z), f' = x(y + 8j) - 1;
                # require the phantom word to be canonical: x < f'  <=>  x (y' - 1) > 1
                J = p // (16 * r * z)
                xzp = set(factorint(r * z))
                while J >= 1 and len(phs) < K and tries < (8000 if XZM else 2000):
                    tries += 1
                    j = rng.randint(-J, J)
                    yq = y + 8 * j
                    if j == 0 or yq < 2 or r * (yq - 1) <= 1: continue
                    q = p + 8 * j * r * z
                    if XZM and any(l not in xzp and pow(q % l, (l - 1) // 2, l) != pow(p % l, (l - 1) // 2, l) for l in (3, 5, 7, 11, 13)):
                        continue
                    if q in phs or not isprime(q): continue
                    phs.append(q)
            if not MATCH and not XZ:
                # same-size f-phantom: p' = p + 8 j f with 1 <= |j| <= p/(16 f)  (so |p' - p| <= p/2);
                # impossible when f > p/16 -- such witnesses get no phantom and are reported as not covered
                J = p // (16 * f)
                while J >= 1 and len(phs) < K and tries < 2000:
                    tries += 1
                    j = rng.randint(-J, J)
                    if j == 0: continue
                    q = p + 8 * j * f
                    if q in phs or not isprime(q): continue
                    phs.append(q)
            rec = {'p': p, 'f': f, 'r': r, 'y': y, 'z': z, 'real': {'%s:%s' % k: v for k, v in real.items()}, 'ph': []}
            for q in phs:
                Fq = lite_feats(q, cf=not MATCH and q < BIG)
                Dq = dictionary(Fq)
                if MATCH:
                    for fam in SIZE_SENSITIVE: Dq.pop(fam, None)
                if XZ:
                    yq = y + (q - p) // (r * z); fqq = r * yq - 1
                    assert r * yq * z - r - z == q and (r * yq) % 8 == 0
                    assert (q + r) % fqq == 0 and (q + r) // fqq == z and fqq - q % fqq == r and (fqq + 1) % r == 0
                    fqs_ = [t for t in factorint(fqq) if t >= 5]
                    h = hits(Dq, pell_full(q, fqq, fqs_) if q < BIG else None, fqq, r, yq, z, fqs_)
                else:
                    zq = (q + r) // f
                    assert (q + r) % f == 0 and f - q % f == r
                    if MATCH:
                        h = hits(Dq, pell_one(q, f) + (0, 0, 0, 0) if q < BIG else None, f, r, y, zq, fq)
                    else:
                        h = hits(Dq, pell_full(q, f, fq) if q < BIG else None, f, r, y, zq, fq)
                rec['ph'].append({'q': q, 'h': {'%s:%s' % k: v for k, v in h.items()}})
            fo.write(json.dumps(rec) + '\n')
        fo.flush()

if __name__ == '__main__':
    main()
