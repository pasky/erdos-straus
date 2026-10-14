"""fz_rate.py (O220): continuum steering for max_p min_route phi(p) - 1/2 (units of log q), routes of FF_STERILE_PUSH
Lemma 1.6 (as in fs_rate.py) plus the division routes D1, D1c, D2, D3 of FF_STERILE_SMALL Lemma 1.2.
EVIDENCE/steering only (grid + local refinement). usage: fz_rate.py r[,r..] [G=80] [new=1]"""
import sys, random
from math import log
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import fs_rate as F
NEW = True
def routes(a, z, y, t, lq):
  R = F.routes(a, z, y, t, lq)
  if not NEW: return R
  b = y + t
  if z > t:
    R['D1'] = z + (a + b) * F.H(a / (a + b)) / lq if a + b > 0 else z
    if F.ok(a + b, a, t): R['D1c'] = z
  if a > t and F.ok(z + b, b, t): R['D2'] = a
  if F.ok(z + a, a, t): R['D3'] = b
  if NEW >= 3:   # Lemma 1.4: refined class routes (penalty instead of failure)
    def pen(n, d, rho):
      if n <= 0 or d < rho: return 0.0
      return max(0.0, d * (n - d) / n - rho)
    dE = a + y + z; dEp = b + y + z
    m = lambda u, v: max(u, v)
    R['R2p'] = y + z + pen(1 + 2 * y + z, dE, y + z); R['R3p'] = a + y + pen(1 + y, dE, a + y)
    R['R4p_'] = a + z + pen(1, dE, a + z); R['R3Cp'] = b + y + pen(1 + y, dEp, b + y)
    R['R4Cp'] = b + z + pen(z + 2 * b, dEp, z + b)
    R['R5ap'] = m(a, t) + pen(b + z, b, t); R['R5bp'] = m(b, t) + pen(a + z, a, t)
    R['R6ap'] = t + F.H(a) / lq + pen(b + z, b, t); R['R6bp'] = t + F.H(b) / lq + pen(a + z, a, t)
    R['R10ap'] = m(z, t) + pen(a + b, a, t); R['R10bp'] = t + F.H(z) / lq + pen(a + b, a, t)
  if NEW >= 2:   # Lemma 1.3: v1 in a class mod the fixed factors
    R['R9a3'] = max(z, t) + (a + b) * F.H(a / (a + b)) / lq
    if F.ok(a + b, a, t): R['R10a3'] = max(z, t)
    if F.ok(z + b, b, t): R['R5a3'] = max(a, t)
    if F.ok(z + a, a, t): R['R5b3'] = max(b, t)
    R['X1_3'] = y + max(z, t); R['X2_3'] = y + max(a, t); R['R4p3'] = max(z + a, t)
  return R
def val(p, lq):
  a, z, y = p; t = 1 - a - z - y
  if a <= 1e-9 or z < 0 or z > 1 - 1e-9 or y < 0 or t < 0 or a > y + t + 1e-12: return -9
  return min(routes(a, z, y, t, lq).values())
def opt(lq, G=80, seed=1):
  rnd = random.Random(seed); best = []
  for i in range(G + 1):
    for j in range(G + 1 - i):
      for k in range(G + 1 - i - j):
        p = (i / G, j / G, k / G); v = val(p, lq)
        if v > -9: best.append((v, p))
  best.sort(reverse=True); out = []
  for v, p in best[:12]:   # local refinement (random hill climbing)
    st = 1.0 / G
    for it in range(3000):
      q = tuple(x + rnd.gauss(0, st) for x in p); w = val(q, lq)
      if w > v: v, p = w, q
      if it % 500 == 499: st /= 2
    out.append((v, p))
  out.sort(reverse=True); return out
HSCALE = 1.0   # 0.0 = fixed-q asymptotics: divisor counts are q^{o(n)} (FF_STERILE_SMALL Lemma 4.x), entropy terms vanish
_H = F.H; _Hm = F.Hm
F.H = lambda p: HSCALE * _H(p); F.Hm = lambda *ps: HSCALE * _Hm(*ps)
if __name__ == '__main__':
  if len(sys.argv) > 4: HSCALE = float(sys.argv[4])
  G = int(sys.argv[2]) if len(sys.argv) > 2 else 80
  if len(sys.argv) > 3: NEW = int(sys.argv[3])
  for r in [int(x) for x in sys.argv[1].split(',')]:
    lq = r * log(3); res = opt(lq, G)
    for v, p in res[:3]:
      a, z, y = p; t = 1 - a - z - y; R = routes(a, z, y, t, lq)
      print(r, '%+.4f' % (v - .5), '(a,z,y,t)=', [round(x, 4) for x in (a, z, y, t)],
            ' '.join('%s=%.4f' % kv for kv in sorted(R.items(), key=lambda kv: kv[1])[:6]), flush=True)
