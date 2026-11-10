# z69 MINE round 2, Part A (pre-registered in data/z69/mine/round2_prereg.md): Q-set / CFpA letters vs within-prime
# chi-matched decoys, FULL CF period of sqrt p.
# Usage: python z69_mine_qs2.py <wit file> <prime list file (first column)> <cap witnesses per prime, 0 = all> <seed> <out.jsonl>
import sys, json, math, random
import numpy as np
from sympy import factorint, isprime, prevprime, nextprime
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit
from z69_mine_feat import rep
from z69_mine_phantom import cf_conv_den

def cf_Q(p):
    a0 = math.isqrt(p); P, Q, a = 0, 1, a0; Qs = []
    while True:
        P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; Qs.append(Q)
        if Q == 1: break
    return np.array(Qs, dtype=np.int64)

def chi(p, q):
    return 0 if p % q == 0 else (1 if pow(p % q, (q - 1) // 2, q) == 1 else -1)

def decoy(p, l, rng):
    k = (l & -l).bit_length() - 1
    out = 1 << k
    for q, e in factorint(l >> k).items():
        c = chi(p, q); lo = max(3, int(q / 1.5)); hi = int(1.5 * q) + 1
        cands = None
        for _ in range(200):
            if hi - lo < 50:
                if cands is None:
                    cands = [t for t in range(lo | 1, hi + 1, 2) if isprime(t) and chi(p, t) == c]
                t = rng.choice(cands) if cands else q
                break
            t = nextprime(rng.randint(lo, hi))
            if t <= hi and chi(p, t) == c: break
        else:
            t = q
        out *= t ** e
    return out

def signature(p, m):
    return tuple(sorted((chi(p, q), e) for q, e in factorint(m).items()))

def decoy_exact(p, l, rng, tries=600):
    """size-matched decoy: same 2-adic part, odd part m' within +-5 % of m with the same chi_p-signature
    (multiset of (chi_p(q), exponent)); None if no match found (the letter is then dropped together with its decoys)"""
    k = (l & -l).bit_length() - 1; m = l >> k
    sig = signature(p, m)
    lo, hi = -(-m * 95 // 100), m * 105 // 100          # exact integer window ceil(0.95 m) .. floor(1.05 m)
    lo += (lo % 2 == 0); hi -= (hi % 2 == 0)            # odd endpoints
    if hi < lo: return None
    nodd = (hi - lo) // 2 + 1
    for _ in range(tries):
        t = lo + 2 * rng.randrange(nodd)                # uniform over the admissible odd integers
        assert lo <= t <= hi and t % 2 == 1 and abs(t - m) * 100 <= 5 * m
        if signature(p, t) == sig: return t << k
    return None      # rejection budget exhausted (the letter itself always matches; it is NOT used as fallback)

def stats(Q, L, Aden, l):
    m = (Q % l == 0)
    D = bool(m.any())
    i0 = int(np.argmax(m)) + 1 if D else 0
    return {'D': D, 'R': float(m.sum()) / L, 'E': bool((Q == l).any()), 'A': any(v % l == 0 for v in Aden),
            'pos': i0 / L if D else None, 'par': (i0 % 2) if D else None}

EXACT = False

def main():
    global EXACT
    wf, lf, cap, seed, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    EXACT = len(sys.argv) > 6 and sys.argv[6] == 'exact'
    rng = random.Random(seed)
    W = load_wit(wf)
    ps = [int(l.split()[0]) for l in open(lf) if l.strip()]
    fo = open(out, 'w')
    for p in ps:
        if p not in W or not W[p]: continue
        Q = cf_Q(p); L = len(Q)
        ab = rep('1,0,1', p); a, b = (ab if ab[0] % 2 else ab[::-1]); c, d = rep('1,0,2', p)
        g = 1
        while True:
            e2 = p + 2 * g * g; e = math.isqrt(e2)
            if e * e == e2: break
            g += 1
        Aden = set()
        for A in (a, b, c, d, e, g): Aden |= set(cf_conv_den(p, A))
        Aden -= {0, 1}
        wl = list(W[p]); rng.shuffle(wl)
        if cap: wl = wl[:cap]
        rec = {'p': p, 'L': L, 'sq': math.isqrt(p), 'real': [], 'dec': []}
        for f, r, y, z in wl:
            for l in (r, y):
                if l < 5: continue
                if EXACT:
                    ds = [decoy_exact(p, l, rng) for _ in range(2)]
                    if None in ds: rec['drop'] = rec.get('drop', 0) + 1; continue
                else:
                    ds = [decoy(p, l, rng) for _ in range(2)]
                rec['real'].append([l] + list(stats(Q, L, Aden, l).values()))
                for l2 in ds:
                    rec['dec'].append([l2] + list(stats(Q, L, Aden, l2).values()))
        fo.write(json.dumps(rec) + '\n'); fo.flush()

if __name__ == '__main__':
    main()
