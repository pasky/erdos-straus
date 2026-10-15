"""O221 (NEAR_SQUARE §2): brute-force search for Type I / Type II ES polynomial families for n = m^2 + k.

Each of a, c, d is lam * (monic product of linear factors (m - r)), total degree 2 (Type I) or <= 2 (Type II, with e
determined).  The polynomial identities (f | na + c, resp. f | n + 4a^2 d) are checked exactly over Q; survivors are
tested for positivity and integrality at large m, valid classes m mod L are listed, and the witness D (d resp. de)
is reduced mod m^2 + k to decide whether the family 'escapes' (non-zero m-coefficient).
Usage: ns_polyfam.py K R [OUTFILE]  (k = K, roots r in [-R, R] with denominators 1, 2)"""
import sys, itertools
from fractions import Fraction as Fr
from math import lcm

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0: p.pop()
    return tuple(p)
def add(p, q):
    n = max(len(p), len(q)); return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])
def sc(p, s): return trim([s * x for x in p])
def mul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i + j] += x * y
    return trim(r)
def divmod_(p, q):
    p = list(p); q = trim(q); out = [Fr(0)] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and any(p):
        coef = p[-1] / q[-1]; sh = len(p) - len(q); out[sh] = coef
        for i, y in enumerate(q): p[sh + i] -= coef * y
        p.pop()
        p = list(trim(p)) if p else [Fr(0)]
        if len(p) < len(q): break
    return trim(out), trim(p)
def deg(p): return -1 if (len(p) == 1 and p[0] == 0) else len(p) - 1
def ev(p, m): return sum(c * m ** i for i, c in enumerate(p))
def den(p): return lcm(*[x.denominator for x in p])

K = int(sys.argv[1]); R = int(sys.argv[2])
N = (Fr(K), Fr(0), Fr(1))
roots = sorted({Fr(x, q) for q in (1, 2) for x in range(-R * q, R * q + 1)})
lams = sorted({Fr(x, q) for x in (1, 2, 3, 4) for q in (1, 2, 3, 4, 8)})
def lin(r): return (-r, Fr(1))
ONE = (Fr(1),)

def shapes(total):
    # distribute `total` linear factors among (a, c, d)
    for da in range(total + 1):
        for dc in range(total + 1 - da):
            yield da, dc, total - da - dc

def monics(dg):
    if dg == 0: yield ONE, ()
    elif dg == 1:
        for r in roots: yield lin(r), (r,)
    else:
        for r1, r2 in itertools.combinations_with_replacement(roots, 2): yield mul(lin(r1), lin(r2)), (r1, r2)

def classes(polys, extra_ok, mlo=10 ** 4):
    L = lcm(*[den(p) for p in polys]) * 4
    if L > 20000: return L, None
    good = [r for r in range(L) if extra_ok(mlo * L + r)]
    return L, good

found = []
skipped = 0
OUT = open(sys.argv[3], "w") if len(sys.argv) > 3 else None
def report(kind, D, params, L, good):
    if OUT: OUT.write(repr((kind, {k: [str(x) for x in v] for k, v in params.items()}, L, good)) + "\n")
    q, rem = divmod_(D, N)
    esc = deg(rem) == 1
    found.append((kind, esc))
    print(kind, "escape" if esc else "nonesc", "params", params, "L", L, "classes", (good if good is not None and len(good) <= 12 else (len(good) if good is not None else None)))

for typ in (1, 2):
    for total in ((2,) if typ == 1 else (0, 1, 2)):
        for da, dc, dd in shapes(total):
            if typ == 1 and dd == 0: continue          # constant d: never escapes (Cor 1.2)
            for (ma, ra), (mc, rc), (md, rd) in itertools.product(monics(da), monics(dc), monics(dd)):
                for la, lc_, ld in itertools.product(lams, lams, lams):
                    a, c, d = sc(ma, la), sc(mc, lc_), sc(md, ld)
                    acd4 = sc(mul(mul(a, c), d), 4)
                    if typ == 1:
                        f = add(acd4, sc(N, -1))
                        if deg(f) < 0 or f[-1] <= 0: continue
                        num = add(mul(N, a), c)
                        if deg(f) >= 1:
                            b, r0 = divmod_(num, f)
                            if deg(r0) >= 0: continue
                        else:
                            b = sc(num, 1 / f[0])
                        e, r1 = divmod_(add(sc(mul(mul(a, a), d), 4), ONE), f)
                        if deg(r1) >= 0: continue
                        D = d
                    else:
                        f = add(acd4, (Fr(-1),))
                        if deg(f) < 0 or f[-1] <= 0: continue
                        e, r0 = divmod_(add(N, sc(mul(mul(a, a), d), 4)), f)
                        if deg(r0) >= 0: continue
                        if deg(mul(mul(mul(a, c), d), e)) != 2: continue
                        b = add(mul(c, e), sc(a, -1))
                        D = mul(d, e)
                        if deg(D) == 0: continue          # constant witness: congruence family
                    q, rem = divmod_(D, N)
                    if deg(rem) != 1: continue            # only escaping families are of interest here
                    polys = [a, b, c, d, e, f]
                    if any(p[-1] <= 0 for p in polys): continue
                    def ok(m, polys=polys):
                        n = m * m + K
                        return n % 4 == 1 and all(ev(p, m).denominator == 1 and ev(p, m) > 0 for p in polys)
                    L, good = classes(polys, ok)
                    if good == []: continue
                    if good is None: skipped += 1; continue      # period > 20000: classes not computed (R-O221 repair)
                    report("TypeI" if typ == 1 else "TypeII", D, dict(a=a, b=b, c=c, d=d, e=e, f=f), L, good)
print("k =", K, "R =", R, "escaping families with computed non-empty classes:", len(found), "; skipped (period > 20000):", skipped)
