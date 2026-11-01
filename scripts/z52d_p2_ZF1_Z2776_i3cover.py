#!/usr/bin/env python3
"""z52d Pass-2 ZF1/S6 item Z2776: I3 on exponential families n_k = c·b^k + d by exponent coverings.

I3(n): n = t·u·v − u − v with t, u, v ≥ 3 (I3_DEEP_FABLE.md §5.5).  Two menus of fixed-parameter words:
  E (endpoints u, v fixed):  uv | n + u + v,           t = (n+u+v)/(uv)
  L (level t and u fixed):   (tu − 1) | n + u,         v = (n+u)/(tu − 1)
For k ≥ K0 (K0 > every exponent of b in the moduli) each condition is periodic in k with period ord_w(b), w = modulus
with the primes of b removed.  We record, for each word with period | L, its set of residues k mod L, and test whether
the union covers ℤ/L (greedy cover printed).  Then: direct verification of the chosen cover for K0 ≤ k ≤ KCHK
(exact division + coordinate ≥ 3), and a brute-force I3 search for the small k < K0 (and any k the cover misses).
Unlike the z49 search, moduli sharing primes with b and with c are handled exactly (no skipping).
Usage: z52d_p2_ZF1_Z2776_i3cover.py c b d [B=3000] [Ls=...] [KCHK=400]
"""
import sys, math, json
from sympy import n_order, factorint

def strip(m, b):
    for q in factorint(b):
        while m % q == 0: m //= q
    return m

def words(B):
    E = [(u, v) for u in range(3, B) for v in range(u, B // u + 1) if u * v <= B]
    Lw = [(t, u) for t in range(3, B) for u in range(3, (B + 1) // t + 1) if t * u - 1 <= B]
    return E, Lw

def i3_brute(n):
    # n = tuv - u - v  <=>  (tu-1)(tv-1) = tn+1 ; search t>=3, u<=v
    t = 3
    while 3 * (t * 3) - 6 <= n:
        N = t * n + 1; a = 3 * t - 1          # a = tu-1, u>=3, a ≡ -1 mod t, a <= sqrt(N)
        while a * a <= N:
            if N % a == 0:
                bb = N // a
                if (bb + 1) % t == 0 and (bb + 1) // t >= 3: return (t, (a + 1) // t, (bb + 1) // t)
            a += t
        t += 1
    return None

PARTIAL = False
def run(c, b, d, B=3000, Ls=(12, 24, 36, 48, 60, 72, 120, 144, 180, 240, 360, 720, 1440, 2160, 2520, 5040), KCHK=400):
    E, Lw = words(B)
    mods = {}
    for (u, v) in E: mods.setdefault(u * v, []).append(('E', u, v))
    for (t, u) in Lw: mods.setdefault(t * u - 1, []).append(('L', t, u))
    K0 = max(1, max(int(math.log(m, 2)) for m in mods) + 1)
    per = {m: n_order(b, strip(m, b)) if strip(m, b) > 1 else 1 for m in mods}
    res = {}
    for L in Ls:
        cls = []
        for m, ws in mods.items():
            if L % per[m]: continue
            pw = pow(b, K0, m); seq = []
            for i in range(L):
                seq.append((c * pw + d) % m); pw = pw * b % m      # n_k mod m for k = K0 + i
            for w in ws:
                sh = (w[1] + w[2]) if w[0] == 'E' else w[2]
                S = frozenset(i for i in range(L) if (seq[i] + sh) % m == 0)
                if S: cls.append((len(S), m, w, S))
        allS = set().union(*[x[3] for x in cls]) if cls else set()
        miss = sorted(set(range(L)) - allS)
        res[L] = miss
        if not miss or (PARTIAL and L == Ls[-1]):
            # greedy cover
            unc = set(range(L)) - set(miss); chosen = []
            while unc:
                best = max(cls, key=lambda x: (len(unc & x[3]), -x[1])); chosen.append(best); unc -= best[3]
            return L, K0, chosen, res
    return None, K0, None, res

def n_of(c, b, d, k): return c * b ** k + d

def verify(c, b, d, L, K0, chosen, KCHK, miss=()):
    bad = []
    for k in range(K0, KCHK + 1):
        if (k - K0) % L in miss: continue
        n = n_of(c, b, d, k); ok = False
        for (_, m, w, S) in chosen:
            if (k - K0) % L not in S: continue
            if w[0] == 'E':
                u, v = w[1], w[2]
                if (n + u + v) % (u * v) == 0 and (n + u + v) // (u * v) >= 3: ok = True; break
            else:
                t, u = w[1], w[2]
                if (n + u) % (t * u - 1) == 0 and (n + u) // (t * u - 1) >= 3: ok = True; break
        if not ok: bad.append(k)
    return bad

if __name__ == '__main__':
    c, b, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    B = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
    KCHK = 400
    Ls = tuple(int(x) for x in sys.argv[5].split(',')) if len(sys.argv) > 5 else (12, 24, 36, 48, 60, 72, 120, 144, 180, 240, 360, 720, 1440, 2160, 2520, 5040)
    PARTIAL = len(sys.argv) > 6 and sys.argv[6] == 'partial'
    L, K0, chosen, res = run(c, b, d, B, Ls)
    out = {'family': f'{c}*{b}^k{d:+d}', 'B': B, 'K0': K0}
    if L is None:
        out['covered'] = False
        out['uncovered_by_L'] = {str(k): (v if len(v) <= 40 else v[:40] + ['...', len(v)]) for k, v in res.items()}
        out['note'] = 'residues are i = k - K0 (mod L)'
        print(json.dumps(out)); sys.exit(0)
    miss = res[L]
    bad = verify(c, b, d, L, K0, chosen, KCHK, set(miss))
    small = {}
    for k in list(range(0, K0)) + bad:
        n = n_of(c, b, d, k)
        if n < 3: continue
        hit = None
        for (_, m, w, S) in chosen:      # try the cover's own words first (they need not be periodic below K0)
            if w[0] == 'E' and (n + w[1] + w[2]) % (w[1] * w[2]) == 0 and (n + w[1] + w[2]) // (w[1] * w[2]) >= 3:
                hit = [(n + w[1] + w[2]) // (w[1] * w[2]), w[1], w[2]]; break
            if w[0] == 'L' and (n + w[2]) % (w[1] * w[2] - 1) == 0 and (n + w[2]) // (w[1] * w[2] - 1) >= 3:
                hit = [w[1], w[2], (n + w[2]) // (w[1] * w[2] - 1)]; break
        small[k] = hit if hit else (i3_brute(n) if n < 10 ** 9 else 'not-checked')
    out.update({'covered': not miss, 'L': L, 'residual_k_mod_L': sorted((i + K0) % L for i in miss), 'words': [[w[0], w[1], w[2], m, sorted(S)[:6] + (['...'] if len(S) > 6 else []), len(S)] for (_, m, w, S) in chosen],
                'verify_K0..KCHK_failures': bad, 'small_k_brute': {str(k): v for k, v in small.items()}})
    print(json.dumps(out))
