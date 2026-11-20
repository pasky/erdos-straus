"""Independent re-derivation (Opus review 2) of the exponent bookkeeping of
ANALYTIC_WILD §§7-8.  Everything is recomputed from the raw error terms, not
copied from scripts/z78_analytic_r2.py.

Raw quantities (exponents to base n, block U~n^a, V~n^b, W~n^g, a+b+g=1):
  P=n^r, N=P^2=n^{2r}, H=n^j, L=NW/V, |l|<=L, h<=H,
  Y=n|l|h/W^3, T=WY, Z=Y h^2/W, sigma=hN/W.
Block bound: n^t needs
  detector V/P, zero freq V/N + V/W, diagonal W*sqrt(N/H),
  off-diagonal sqrt(W*N*avg_h E_h).
E_h (second moment, (8)):  1 + sqrt(WN)*sqrt((1+Z)(1+Y/(ZN^2)))
E_h (fourth moment, (9)):  1 + sqrt(W)*Y^{1/4}*((1+Z)(1+Y/(ZN^2)))^{1/4}
side: HN/W<1 strictly, T>1 strictly (g<1/2), quartic T sigma^4 <= 1 (or n^delta),
      L>=1.
"""
from fractions import Fraction as F
import itertools

def exps(a, b, g, r, j, moment):
    """return dict of exponents; Y uses max l and h=H.  For the 1/h term we
    average over h<=H (h^{-1} -> H^{-1} log, h^{-1/2} -> H^{-1/2})."""
    N = 2*r
    Lx = N + g - b
    Y = 1 + Lx + j - 3*g           # max over l,h
    Z = Y + 2*j - g                # at h=H
    T = g + Y
    out = {}
    out['detector'] = b - r
    out['zero'] = max(b - N, b - g)
    out['diag'] = g + (N - j)/2
    # off-diagonal: need (g + N + Eavg)/2 <= t
    if moment == 2:
        # sqrt(WN)*sqrt((1+Z)(1+Y/(Z N^2))) expanded, h-dependence:
        # sqrt(WN): h^0 ; h sqrt(NY): Y~h so h^{3/2}: max at H ;
        # W/(h sqrt N): avg -> /H ; sqrt(WY/N): max at H
        Es = [(g+N)/2, j + N/2 + Y/2, g - j - N/2, (g+Y-N)/2]
    else:
        Es = [g/2 + Y/4, g/4 + Y/2 + j/2, 3*g/4 + Y/4 - j/2 - N/2, (g+Y-N)/2]
    Eavg = max([F(0)] + Es)
    out['offdiag'] = (g + N + Eavg)/2
    out['Eterms'] = Es
    out['side_shift'] = g - j - N        # >0 needed
    out['side_T'] = 1 - 2*g              # >0 needed (min T at l=h=1)
    out['quartic'] = T + 4*(j + N - g)   # <=0 (with n^delta slack)
    out['L'] = Lx                        # >=0
    return out

def check(t, moment, pts):
    worst = {}
    for (a, b, g) in pts:
        r = b - t
        j = 2*(r + g - t)
        e = exps(a, b, g, r, j, moment)
        ok = (e['detector'] <= t and e['zero'] <= t and e['diag'] <= t
              and e['offdiag'] <= t and e['side_shift'] > 0 and e['side_T'] > 0
              and e['quartic'] <= 0 and e['L'] >= 0 and r >= 0 and j >= 0)
        if not ok:
            return False, (a, b, g, e)
        for k in ('offdiag', 'quartic'):
            worst[k] = max(worst.get(k, F(-10)), e[k])
    return True, worst

def triangle_grid(t, M):
    """all rational points of the triangle b>=a>=t, g>=t, a+b+g=1 on a grid"""
    pts = []
    v = [(t, 1-2*t, t), (t, t, 1-2*t), ((1-t)/2, (1-t)/2, t)]
    for i in range(M+1):
        for k in range(M+1-i):
            l = M - i - k
            p = tuple((i*v[0][c] + k*v[1][c] + l*v[2][c])/M for c in range(3))
            pts.append(p)
    return pts

for moment, t in ((2, F(7, 22)), (4, F(20, 63))):
    ok, w = check(t, moment, triangle_grid(t, 30))
    print('moment', moment, 't', t, 'grid(30) over whole triangle ok:', ok, w if ok else '')
    # vertex 1 details
    a, b, g = t, 1-2*t, t
    r = b - t; j = 2*(r+g-t)
    e = exps(a, b, g, r, j, moment)
    print('  vertex1 r', r, 'j', j, 'Eterms', e['Eterms'], 'goal for E', 2*t - g - 2*r,
          'quartic', e['quartic'])
    # slightly below fails?
    tm = t - F(1, 10**4)
    ok2, info = check(tm, moment, triangle_grid(tm, 6))
    print('  t-1e-4 ok?', ok2)

# Optimise freely over (r,j) at vertex 1 (not forced to the note's choice):
def best_t(moment, quartic_hard=True):
    lo, hi = F(1, 4), F(1, 3)
    for _ in range(40):
        t = (lo + hi)/2
        a, b, g = t, 1-2*t, t
        feas = False
        for rr in range(0, 201):
            r = (b - t) + F(rr, 4000)
            for jj in range(0, 201):
                j = F(jj, 1000)
                e = exps(a, b, g, r, j, moment)
                if (e['detector'] <= t and e['zero'] <= t and e['diag'] <= t
                        and e['offdiag'] <= t and e['side_shift'] > 0 and e['side_T'] > 0
                        and (e['quartic'] <= 0 or not quartic_hard) and e['L'] >= 0):
                    feas = True; break
            if feas: break
        if feas: hi = t
        else: lo = t
    return float(hi)

print('free (r,j) grid optimum at vertex1, 2nd moment:', best_t(2), ' 7/22=', 7/22)
print('free (r,j) grid optimum at vertex1, 4th moment:', best_t(4), ' 20/63=', 20/63)
print('4th moment, quartic constraint dropped (only to see which binds):', best_t(4, False))
