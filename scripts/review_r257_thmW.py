# review_r257_thmW.py — R257 FROM-SCRATCH finite check for EXP_OPEN Theorem W (no z19_ imports).
# Enumerates a SUPERSET of limit relations allowed by Lemmas 1.1-1.5:
#   w odd, m = 4 c0 w^4 - k > 0  (Lemma 1.4; m = 3 mod 8 NOT imposed unless --strict),
#   M = 4^J + m, a1, a2 odd, a1 a2 | M; delta_i in {0,1/2,1}, delta1+delta2 <= 1; n placed in d1, d2 or d3,
#   e_i = -2 delta_i + nu_i (nu_i = 2J if n in d_i else 0);  m | 2^e1 a1 + 2^e2 a2 in Z[1/2].
#   (e1-e2 odd NOT imposed unless --strict.)  Bound: m <= B(m) with E = 2J+2 (Lemma 1.5), r = M/m exact.
# Also an UNBOUNDED sanity mode (--wmax W): ignore B and scan all odd w <= W, to check the bound is not cutting real hits.
import sys
from fractions import Fraction as F

def divisors(N):
    ds, p, f = [1], 2, {}
    x = N
    while p * p <= x:
        while x % p == 0: f[p] = f.get(p, 0) + 1; x //= p
        p += 1
    if x > 1: f[x] = f.get(x, 0) + 1
    for q, e in f.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return sorted(ds)

def B(m, J):
    E = 2 * J + 2; M = 4 ** J + m; r = F(M, m)
    return max(2 ** E * 4 ** J + 2 ** (2 * E + 2) * r * r, 2 ** E * 4 * r * r + 4 ** J)

def hits_for_m(m, J, strict):
    M = 4 ** J + m; out = []
    if strict and m % 8 != 3: return out
    D = [d for d in divisors(M)]        # M odd => all divisors odd
    for a1 in D:
        for a2 in D:
            if M % (a1 * a2): continue
            for d1 in (0, 1, 2):          # 2*delta
                for d2 in (0, 1, 2):
                    if d1 + d2 > 2: continue
                    for npos in (1, 2, 3):
                        e1 = -d1 + (2 * J if npos == 1 else 0)
                        e2 = -d2 + (2 * J if npos == 2 else 0)
                        if strict and (e1 - e2) % 2 == 0: continue
                        lo = min(e1, e2)
                        if (2 ** (e1 - lo) * a1 + 2 ** (e2 - lo) * a2) % m == 0:
                            out.append((a1, a2, F(d1, 2), F(d2, 2), npos, e1, e2))
    return out

def run(c0, k, strict, wmax=None):
    J = next(j for j in range(1, 40) if 4 ** j == c0 + k)
    assert c0 % 2 == 1 and k % 8 == 1
    res, w, lastw = {}, 1, None
    while True:
        m = 4 * c0 * w ** 4 - k
        if wmax is None:
            if m > 0 and m > B(m, J): break
        elif w > wmax: break
        if m > 0:
            h = hits_for_m(m, J, strict)
            if h: res[m] = h
            lastw = w
        w += 2
    return J, lastw, res

if __name__ == '__main__':
    strict = '--strict' in sys.argv
    wmax = None
    if '--wmax' in sys.argv: wmax = int(sys.argv[sys.argv.index('--wmax') + 1])
    pairs = [(15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9), (3, 1), (7, 9), (23, 41), (39, 25)]
    for c0, k in pairs:
        J, lw, res = run(c0, k, strict, wmax)
        print((c0, k), 'J=%d last w=%s' % (J, lw), 'hits m:', {m: len(v) for m, v in res.items()},
              ('example ' + str(next(iter(res.values()))[0])) if res else '')
