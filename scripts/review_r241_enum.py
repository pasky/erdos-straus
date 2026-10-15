"""review_r241_enum.py (R241, hostile review #2 of FF_ODD_ABSENCE / O226) — FROM SCRATCH, no author code reused.

Exhaustive enumeration of k = 1 Case B tuples (FF_STERILE_SMALL (B^{k=1})) over F_q, q = p^r:
    m' w C = T^s + v,   w + C = g' v,   m', g', w, C monic,   T does not divide m' g' w C v.
Pattern (s; a, b, z, y, t) = degrees of (w, C, m', g', v); z + a + b = s, y + t = max(a, b) (FF_STERILE_SMALL Lemma 7.1(i)).
Each pattern is enumerated by the cheapest of five complete routes (python-flint factorisation over F_q):
  V[t]    : v (deg t, lc in {1, 2}), ordered monic factorisations T^s + v = m' w C.
  MW[z,a] : (m', w); v = lam * D, D monic | T^s + m' w^2 (since v | T^s + m'w^2), C = (T^s + v)/(m'w).
  MC[z,b] : symmetric with C.
  WG[a,y] : (w, g'); C monic | g' T^s + w (E C = g'T^s + w), v = (w + C)/g', m' = (T^s + v)/(w C).
  CG[b,y] : symmetric.
Every candidate is re-verified against the defining conditions; tuples are deduplicated (all ORDERED tuples, both
orientations w <-> C counted separately). Output: per pattern, histogram of E(0) = w(0)/C(0) (as exponent of a fixed
primitive element, or 'z' never), plus checks of the law E(0)^s = eps(s; z, t) = (-1)^{t + tz + z(1+s) + ts} and of the
unsimplified Lemma 1.1 form.
usage: review_r241_enum.py p r smin smax [maxcost]   -> prints lines 'P s a b z y t k0:count k1:count ...' and 'LAWFAIL'.
"""
import sys, itertools, time, os
import flint

p, r, smin, smax = map(int, sys.argv[1:5])
MAXCOST = float(sys.argv[5]) if len(sys.argv) > 5 else 1e30
q = p ** r
F = flint.fq_default_ctx(p, r, 'g')
R = flint.fq_default_poly_ctx(F)
# primitive element by search (do not trust the generator)
nz = []
def all_elems():
    # enumerate all field elements as polynomials in gen of degree < r
    g = F.gen()
    out = []
    for cs in itertools.product(range(p), repeat=r):
        e = F(0)
        for i, c in enumerate(cs):
            e += F(c) * g ** i
        out.append(e)
    return out
ELS = all_elems()
assert len(set(str(e) for e in ELS)) == q
NZ = [e for e in ELS if e != 0]
def order(e):
    k, x = 1, e
    while x != 1:
        x *= e; k += 1
    return k
PRIM = next(e for e in NZ if order(e) == q - 1)
LOG = {}
x = F(1)
for k in range(q - 1):
    LOG[str(x)] = k; x *= PRIM
assert len(LOG) == q - 1
ONE, TWO = F(1), F(2)
T = R([0, 1])

def monics(d, need_t_free=True):
    """all monic polynomials of degree d with nonzero constant term (if d >= 1)."""
    if d == 0:
        yield R([1]); return
    for cs in itertools.product(NZ if need_t_free else ELS, *([ELS] * (d - 1))):
        yield R(list(cs) + [ONE])

def polys_lc(d, lc):
    if d == 0:
        yield R([lc]); return
    for cs in itertools.product(NZ, *([ELS] * (d - 1))):
        yield R(list(cs) + [lc])

def monic_divisors(Fp):
    """all monic divisors of Fp (nonzero)."""
    _, facs = Fp.factor()
    facs = [(f.monic(), e) for f, e in facs]
    out = [R([1])]
    for f, e in facs:
        new = []
        for d in out:
            pw = R([1])
            for k in range(e + 1):
                new.append(d * pw); pw *= f
        out = new
    return out

def deg(P):
    return P.degree()

def exact_div(A, B):
    qq, rr = divmod(A, B)
    return qq if rr == 0 else None

FOUND = {}   # key (s, m, g, w, C) strings -> pattern, E0log
def check_add(s, m, g, w, C):
    """verify tuple fully; add if valid."""
    for P in (m, g, w, C):
        if P == 0 or P.leading_coefficient() != 1 or P(F(0)) == 0:
            return
    v = m * w * C - T ** s
    if v == 0 or v(F(0)) == 0:
        return
    if w + C != g * v:
        return
    key = (s, str(m), str(g), str(w), str(C))
    if key in FOUND:
        return
    z, a, b, y, t = deg(m), deg(w), deg(C), deg(g), deg(v)
    E0 = w(F(0)) / C(F(0))
    lam = v.leading_coefficient()
    # law checks
    eps = -1 if (t + t * z + z * (1 + s) + t * s) % 2 else 1
    ok_simpl = (E0 ** s == F(eps))
    # unsimplified Lemma 1.1 with mu_M = mu_W = 1: (W0/C0)^s = eps * lam^{z + 2a - s}
    ex = z + 2 * a - s
    lamp = lam ** ex if ex >= 0 else (1 / lam) ** (-ex)
    ok_full = (E0 ** s == F(eps) * lamp)
    FOUND[key] = ((s, a, b, z, y, t), LOG[str(E0)], ok_simpl, ok_full)

def run_V(s, t, lams):
    for lam in lams:
        for v in polys_lc(t, lam):
            Fp = T ** s + v
            if Fp.leading_coefficient() != 1:
                continue
            for m in monic_divisors(Fp):
                rest = Fp // m
                for w in monic_divisors(rest):
                    C = rest // w
                    if C.leading_coefficient() != 1:
                        continue
                    g = exact_div(w + C, v)
                    if g is not None:
                        check_add(s, m, g, w, C)

def run_MW(s, z, a, sym):
    for m in monics(z):
        for w in monics(a):
            Fp = T ** s + m * w * w
            for D in monic_divisors(Fp):
                for lam in (ONE, TWO):
                    v = lam * D
                    C = exact_div(T ** s + v, m * w)
                    if C is None:
                        continue
                    g = exact_div(w + C, v)
                    if g is None:
                        continue
                    if sym:
                        check_add(s, m, g, C, w)
                    else:
                        check_add(s, m, g, w, C)

def run_WG(s, a, y, sym):
    for w in monics(a):
        for g in monics(y):
            Fp = g * T ** s + w
            for C in monic_divisors(Fp):
                v = exact_div(w + C, g)
                if v is None or v == 0:
                    continue
                m = exact_div(T ** s + v, w * C)
                if m is None:
                    continue
                if sym:
                    check_add(s, m, g, C, w)
                else:
                    check_add(s, m, g, w, C)

def nmon(d):
    return 1 if d == 0 else (q - 1) * q ** (d - 1)

for s in range(smin, smax + 1):
    t0 = time.time()
    pats = []
    for z in range(s + 1):
        for a in range(s - z + 1):
            b = s - z - a
            for y in range(max(a, b) + 1):
                pats.append((a, b, z, y, max(a, b) - y))
    keys = {}
    skipped = []
    if os.environ.get('R241_P8COMPAT'):   # q = 9 certificate mode: only patterns that can carry P8 tuples (4 | s, eps = (-1)^{s/4})
        pats = [pp for pp in pats if s % 4 == 0 and
                (-1 if (pp[4] + pp[4] * pp[2] + pp[2] * (1 + s) + pp[4] * s) % 2 else 1) == (-1) ** (s // 4)]
    for (a, b, z, y, t) in pats:
        lam_needed = 'two' if a == b else 'one'
        cands = [(2 * nmon(t) if t else 2, ('V', t)),
                 (nmon(z) * nmon(a), ('MW', z, a)), (nmon(z) * nmon(b), ('MC', z, b)),
                 (nmon(a) * nmon(y), ('WG', a, y)), (nmon(b) * nmon(y), ('CG', b, y))]
        c, k = min(cands)
        if c > MAXCOST:
            skipped.append((a, b, z, y, t)); continue
        keys.setdefault(k, []).append((a, b, z, y, t))
    allpats = set(pats)
    ch = os.environ.get('R241_CHUNK')   # 'i/n': run only keys with index % n == i (separate processes: python-flint leaks)
    ci, cn = (map(int, ch.split('/')) if ch else (0, 1))
    hist = {}; nfail = 0; ntup = 0; covered = set()
    for idx, k in enumerate(sorted(keys, key=str)):
        if idx % cn != ci:
            continue
        FOUND.clear()   # per-key: each pattern is counted ONLY from the run of its assigned (complete) route
        if k[0] == 'V':
            run_V(s, k[1], (ONE, TWO))
        elif k[0] == 'MW':
            run_MW(s, k[1], k[2], False)
        elif k[0] == 'MC':
            run_MW(s, k[1], k[2], True)
        elif k[0] == 'WG':
            run_WG(s, k[1], k[2], False)
        else:
            run_WG(s, k[1], k[2], True)
        mine = set(keys[k]); covered |= mine
        for key, (pat, e0, o1, o2) in FOUND.items():
            if not (o1 and o2):
                nfail += 1
                print('LAWFAIL', key, pat, e0, o1, o2)
            if pat[1:] not in allpats and not os.environ.get('R241_P8COMPAT'):
                print('OUTSIDE_PATTERN_SPACE', key, pat)
            if pat[1:] in mine:
                ntup += 1
                hist.setdefault(pat[1:], {}).setdefault(e0, 0)
                hist[pat[1:]][e0] += 1
    for pp in sorted(covered):
        h = hist.get(pp, {})
        print('P', s, *pp, ' '.join(f'{k}:{h[k]}' for k in sorted(h)), flush=True)
    if not ch or ci == 0:
        for pp in skipped:
            print('SKIP', s, *pp)
    print(f'# s={s} chunk={ci}/{cn} tuples={ntup} lawfail={nfail} keys={len(keys)} skipped={len(skipped)} time={time.time()-t0:.1f}s', flush=True)
