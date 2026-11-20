"""Independent re-derivation (Opus review) of the ANALYTIC_WILD §§8,11,12,13 exponent systems.

Everything is computed from the primitive quantities (log_n exponents), not copied from
scripts/z78_analytic_r3.py.  Evaluate h at its max H (averages of h^a, a>-1, are ~H^a),
ell at its max L n^delta (all terms increase in Y).
Modes:
  'r2'    : §8  D0=(1+Z)(1+Delta), bounded quartic residual REQUIRED (K<=0)
  'r3a'   : §11 inverse-phase D1 on full band, Abel penalty (1+T sigma^4) on everything
  'r3b'   : §12 frozen quartic, D1 used in each of J bands  (sum D_I <= J D1)
  'r3c'   : §12 localized spacing (11)
kder = order of the derivative test used in the inverse-phase step (note uses 4).
"""
from fractions import Fraction as F
import itertools

def pos(x): return x if x > 0 else 0*x

def system(t, a, b, g, mode, kder=4, mu=0):
    r = b - t                     # P = n^r  (detector V/P = n^t)
    j = 2*(r + g - t)             # H = n^j  (diagonal W^2 N / H = n^{2t})
    N = 2*r
    Lx = mu + N + g - b           # L = M N W / V
    A = 1 + Lx + j                # A = X ell h  (base X)
    Y = A - 3*g
    T = g + Y
    sig = j + N - g               # sigma = hN/W
    Z = Y + 2*j - g
    Dl = Y - Z - 2*N              # Delta = Y/(Z N^2)
    K = pos(T + 4*sig)            # quartic residual size  = log J
    goal = g - j
    base = g/2 + Y/4              # W^{1/2} Y^{1/4}
    # --- spacing bound D (log), per band of length Z/J in v (J=1 if not local)
    Kk = 2**(kder-1); e1 = F(1, 2*Kk-2); e2 = 1 - F(2, Kk)
    def Dcount(Zlen, Jexp):
        # returns list of log-terms of sum over J bands of occupancy, v-length Zlen per band
        terms = [Jexp]  # the +1 per band
        if Z <= 0:
            return [0*t, Dl]
        if Dl >= 0:
            return [Jexp, Jexp + Zlen, Jexp + Dl, Jexp + Zlen + Dl]
        lam = Y - kder*Z          # (f)^{(k)} ~ Y/Z^k
        if lam >= 0:              # derivative test useless; trivial count
            return [Jexp, Jexp + Zlen]
        # ET with B: Zlen*Dl + Zlen/B + Zlen (B lam)^{e1} + Zlen^{e2} lam^{-e1}
        # optimise B: Zlen - Bx = Zlen + e1(Bx + lam) -> Bx = -e1*lam/(1+e1)
        Bx = -e1*lam/(1+e1)
        terms = [Jexp, Jexp+Zlen+Dl, Jexp+Zlen-Bx, Jexp+Zlen+e1*(Bx+lam), Jexp+e2*Zlen-e1*lam]
        terms = [min(x, Jexp+Zlen) if i else x for i, x in enumerate(terms)]  # never worse than trivial
        return terms, Bx
    cons = {}
    if mode == 'r2':
        D = [0*t, Z, Dl, Z + Dl]
        pen = 0
        cons['quartic K<=0'] = -(T + 4*sig)          # >=0 required
    elif mode == 'r3a':
        out = Dcount(Z, 0*t); D = out[0] if isinstance(out, tuple) else out
        pen = K
    elif mode == 'r3b':
        out = Dcount(Z, 0*t); D = out[0] if isinstance(out, tuple) else out
        D = [x + K for x in D]; pen = 0
    elif mode == 'r3c':
        # no separate localisation hypothesis: the +J per-band cost is kept inside D
        out = Dcount(Z - K, K) if Z - K >= 0 else [K, K + Dl]
        D = out[0] if isinstance(out, tuple) else out
        pen = 0
        Bx = out[1] if isinstance(out, tuple) else None
        # the note's own (stronger) localisation hypothesis, reported separately
        cons['note localisation (strict)'] = -(2*j + 8*r - 2*g + max(0*t, 4*(Y + 2*j - g)/15))
    Eterms = [0*t] + [base + x/4 + pen for x in D]
    cons['E_h <= goal'] = goal - max(Eterms)
    cons['HN<<W'] = g - j - N
    cons['T>=n^c'] = 1 - 2*g
    cons['L>>1'] = Lx
    cons['zero freq'] = min(t - (b - N), t - (b - g))
    cons['O(1) term'] = 2*t - g - N
    cons['j>=0,r>=0'] = min(j, r)
    if mode in ('r3b', 'r3c'):
        cons['sextic'] = -(T + 6*sig)
    return cons

STRICT = {'HN<<W', 'T>=n^c', 'sextic', 'note localisation (strict)'}

def ok(t, mode, kder=4, grid=24, mu=0, verbose=False):
    # triangle beta>=alpha>=t, gamma>=t (base X); sample vertices + grid (not only vertices)
    tt = t
    pts = []
    for i in range(grid+1):
        for k in range(grid+1-i):
            # barycentric on vertices
            V1 = (tt, 1-2*tt, tt); V2 = (tt, tt, 1-2*tt); V3 = ((1-tt)/2, (1-tt)/2, tt)
            l1 = F(i, grid); l2 = F(k, grid); l3 = 1 - l1 - l2
            pts.append(tuple(l1*V1[s] + l2*V2[s] + l3*V3[s] for s in range(3)))
    worst = None
    for p in pts:
        c = system(tt, *p, mode=mode, kder=kder, mu=mu)
        for name, v in c.items():
            bad = (v <= 0) if name in STRICT else (v < 0)
            if bad:
                if verbose: print('  fail', name, p, v)
                return False
    return True

def threshold(mode, kder=4, lo=F(3, 10), hi=F(1, 3), it=60):
    for _ in range(it):
        mid = (lo + hi)/2
        if ok(mid, mode, kder, grid=12): hi = mid
        else: lo = mid
    return float(lo), float(hi)

if __name__ == '__main__':
    claims = {'r2': F(20, 63), 'r3a': F(1472, 4637), 'r3b': F(286, 901), 'r3c': F(272, 857)}
    for mode, t0 in claims.items():
        eps = F(1, 10**7)
        a_ok = ok(t0 + eps, mode, grid=30)
        b_ok = ok(t0 - eps, mode, grid=30)
        print(mode, 'claimed', t0, float(t0), 'holds at t0+1e-7:', a_ok, ' holds at t0-1e-7:', b_ok)
        if not b_ok: ok(t0 - eps, mode, grid=30, verbose=True)
        # binding constraints at vertex 1 at t0
        c = system(t0, t0, 1-2*t0, t0, mode)
        print('   vertex-1 margins at t0:', {k: str(v) for k, v in c.items()})
    print('bisection thresholds (float):')
    for mode in claims:
        print('  ', mode, threshold(mode))
    for kd in (2, 3, 5, 6):
        print('  r3c with derivative test k =', kd, threshold('r3c', kder=kd))
    # R_M: base X, mu in [0,1/3], t = th + (1-3th) mu
    th = F(272, 857)
    for mu in [F(0), F(1, 12), F(1, 6), F(1, 4), F(3, 10), F(33, 100)]:
        t = th + (1 - 3*th)*mu
        print('R_M mu', mu, 'holds at t+1e-7:', ok(t + F(1, 10**7), 'r3c', mu=mu, grid=20),
              ' at t-1e-5:', ok(t - F(1, 10**5), 'r3c', mu=mu, grid=20))
