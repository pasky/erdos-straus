# Witness morphology: hard set H vs size-matched controls C (per-witness and per-prime statistics).
import sys, collections, math
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit
from sympy import isprime, factorint
H = load_wit('/tmp/z69mine/H.wit'); C = load_wit('/tmp/z69mine/C.wit')
tags = {int(l.split()[0]): l.split()[1] for l in open('data/z69/mine/H.txt')}
def stats(D, sel):
    s = collections.Counter(); n = 0; npr = 0
    for p, Wl in D.items():
        if not sel(p) or not Wl: continue
        npr += 1
        fs = {f for f, r, y, t in Wl}
        for f, r, y, t in Wl:
            n += 1
            m = min(r, y, t)
            s['min<=2'] += m <= 2; s['min<=8'] += m <= 8; s['min>=20'] += m >= 20
            s['x(=r)<=8'] += r <= 8; s['y<=8'] += y <= 8; s['z<=8'] += t <= 8
            s['f prime'] += isprime(f)
            s['f>sqrt(p)'] += f * f > p
            s['reversal also witness'] += (t * y) % 8 == 0 and (t * y - 1) in fs and t * y - 1 != f
            s['8|y'] += y % 8 == 0
            s['r square'] += math.isqrt(r) ** 2 == r
            s['sq|p+r, sq>1 odd'] += any(e >= 2 and q > 2 for q, e in factorint(p + r).items())
    return npr, n, {k: v / n for k, v in s.items()}
for name, D, sel in (('H-low p>=1e4', H, lambda p: 'low' in tags.get(p, '') and p >= 10**4),
                     ('H-np', H, lambda p: 'np' in tags.get(p, '')),
                     ('C p>=1e4', C, lambda p: p >= 10**4)):
    npr, n, st = stats(D, sel)
    print(name, 'primes', npr, 'witnesses', n, 'W/prime %.1f' % (n / npr))
    print('   ' + '  '.join('%s=%.3f' % kv for kv in st.items()))
