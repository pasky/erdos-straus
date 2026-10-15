"""review_r241_brute.py (R241) — naive brute force for k = 1 Case B tuples, to validate review_r241_enum.py.
Enumerates ALL monic T-free (m', w, C) with deg m' + deg w + deg C = d for d in [0, s + EXTRA], sets v = m'wC - T^s and
keeps the tuple iff v != 0, T does not divide v, and w + C = g' v with g' monic (T-free). Prints the same 'P' histogram
lines as review_r241_enum.py, and reports any tuple with d != s (FF_STERILE_SMALL Lemma 7.1(i) says none exist).
usage: review_r241_brute.py p r smin smax [EXTRA=2]"""
import sys, itertools
import flint

p, r, smin, smax = map(int, sys.argv[1:5])
EXTRA = int(sys.argv[5]) if len(sys.argv) > 5 else 2
q = p ** r
F = flint.fq_default_ctx(p, r, 'g'); R = flint.fq_default_poly_ctx(F)
g0 = F.gen()
ELS = []
for cs in itertools.product(range(p), repeat=r):
    e = F(0)
    for i, c in enumerate(cs):
        e += F(c) * g0 ** i
    ELS.append(e)
NZ = [e for e in ELS if e != 0]
def order(e):
    k, x = 1, e
    while x != 1:
        x *= e; k += 1
    return k
PRIM = next(e for e in NZ if order(e) == q - 1)
LOG = {}; x = F(1)
for k in range(q - 1):
    LOG[str(x)] = k; x *= PRIM
T = R([0, 1])
def monics(d):
    if d == 0:
        yield R([1]); return
    for cs in itertools.product(NZ, *([ELS] * (d - 1))):
        yield R(list(cs) + [F(1)])
MON = {}
for s in range(smin, smax + 1):
    hist = {}; bad = 0; n = 0
    Ts = T ** s
    for d in range(0, s + EXTRA + 1):
        for z in range(d + 1):
            for a in range(d - z + 1):
                b = d - z - a
                for d_ in (z, a, b):
                    if d_ not in MON:
                        MON[d_] = list(monics(d_))
                for m in MON[z]:
                    for w in MON[a]:
                        mw = m * w
                        for C in MON[b]:
                            v = mw * C - Ts
                            if v == 0 or v(F(0)) == 0:
                                continue
                            gg, rr = divmod(w + C, v)
                            if rr != 0 or gg == 0 or gg.leading_coefficient() != 1 or gg(F(0)) == 0:
                                continue
                            n += 1
                            if d != s:
                                bad += 1; print('DEG_NE_S', s, m, w, C)
                            t = v.degree(); y = gg.degree()
                            E0 = w(F(0)) / C(F(0))
                            pat = (a, b, z, y, t)
                            hist.setdefault(pat, {}).setdefault(LOG[str(E0)], 0)
                            hist[pat][LOG[str(E0)]] += 1
    for pp in sorted(hist):
        h = hist[pp]
        print('P', s, *pp, ' '.join(f'{k}:{h[k]}' for k in sorted(h)), flush=True)
    print(f'# brute s={s} tuples={n} deg_ne_s={bad}', flush=True)
