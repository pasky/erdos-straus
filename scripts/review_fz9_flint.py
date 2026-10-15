"""review_fz9_flint.py (R221, from scratch): exact Case B counts over F_9 for the patterns that the factoring-free
enumerator review_fz9_enum.c skips (cost > cap), using factoring by FLINT (python-flint, fq_default; independent of the
author's own Cantor–Zassenhaus code) and R221's own divisor enumeration.

(B): m'wC = T^s + v, w + C = g'v, T || w, T || C, T ∤ m'g', v != 0, all of m', g', w, C monic; w = T w1, C = T C1,
v = T^2 v1 (FF_STERILE_PUSH Lemma 1.1(iii)), m'w1C1 = T^{s-2} + v1, w1 + C1 = T g' v1.
Identities used (all re-derived in the review, §1):
  E := m'g'w - 1:  E * E' = 1 + T^s m' g'^2,  E * C1 = g' T^{s-1} + w1,  E * v1 = T^{s-2} + m' w1^2.
Factoring routes (each pattern is assigned to exactly ONE group; inside a group every tuple has a unique key + divisor):
  F14 (z, a):  (m', w1)             -> E | T^{s-2} + m'w1^2,  deg E = a+y+z  -> v1, C1
  F11 (z, t):  (m', v1 ≡ -T^{s-2} mod m') -> w1 | (T^{s-2}+v1)/m', deg a-1 -> C1, g'
  F12 (z, y):  (m', g')             -> E | 1 + T^s m'g'^2,    deg a+y+z  -> w = (E+1)/(m'g'), C = (g'T^s + w)/E
  F13 (a, y):  (w1, g')             -> E | g'T^{s-1} + w1,    deg a+y+z  -> m' = (E+1)/(T w1 g'), C1
  F16 (a, t):  (w1, v1 ≡ -T^{s-2} mod w1) -> C1 | (T^{s-2}+v1)/w1, deg b-1 -> m'
Every candidate is checked against (B) itself; the pattern is read off the candidate's own degrees and counted only if
it belongs to the group's pattern set.
usage: uv run --with python-flint python scripts/review_fz9_flint.py s C_OUTPUT_FILE [force=0] [route kind 11|12|13|14|16]
  reads the C output (lines "s a z y t count" / "s a z y t SKIP"), fills the SKIP patterns, prints all patterns of level s.
  force=1: treat ALL patterns of level s as SKIP (validation against the C enumerator)."""
import sys, itertools, time
import flint

F = flint.fq_default_ctx(3, 2)
R = flint.fq_default_poly_ctx(F)
g = F.gen()
EL = [F(a) + F(b) * g for b in range(3) for a in range(3)]           # all 9 elements, EL[0] = 0
assert len({str(x) for x in EL}) == 9 and EL[0] == 0 and EL[1] == 1
ONE, T = R([1]), R([0, 1])
TWO = EL[2]


def monic(d):
    """all monic polys of degree d with nonzero constant term"""
    if d == 0:
        yield R([1]); return
    for c0 in EL[1:]:
        for mid in itertools.product(EL, repeat=d - 1):
            yield R([c0, *mid, 1])


def fixed_lc(d, lc):
    """all polys of degree d with leading coefficient lc (any constant term)"""
    for low in itertools.product(EL, repeat=d):
        yield R([*low, lc])


def deg(p):
    return p.degree()


def divisors_by_degree(fac, degs):
    """monic divisors of a factored polynomial with degree in the set degs (own enumeration)"""
    fs = [(f.monic(), e) for f, e in fac[1]]
    out, mx = [], max(degs) if degs else -1
    rem = [0] * (len(fs) + 1)
    for i in range(len(fs) - 1, -1, -1):
        rem[i] = rem[i + 1] + deg(fs[i][0]) * fs[i][1]
    mn = min(degs) if degs else 0

    def rec(i, cur, cd):
        if i == len(fs):
            if cd in degs: out.append(cur)
            return
        if cd + rem[i] < mn: return
        f, e = fs[i]; df = deg(f); p = cur
        for k in range(e + 1):
            if cd + k * df > mx: break
            rec(i + 1, p, cd + k * df)
            p = p * f
    rec(0, ONE, 0)
    return out


def exact_div(a, b):
    q, r = divmod(a, b)
    return q if r == 0 else None


def checkB(s, m, gp, w1, C1, v1):
    """full (B) check; returns the pattern (a, z, y, t) or None"""
    if m is None or w1 is None or C1 is None or v1 is None or v1 == 0 or w1 == 0 or C1 == 0:
        return None
    w, C, v = T * w1, T * C1, T * T * v1
    if gp is None:
        gp = exact_div(w + C, v)
        if gp is None: return None
    for p in (m, gp, w, C):
        if p == 0 or p.leading_coefficient() != 1: return None
    if m.coeffs()[0] == 0 or gp.coeffs()[0] == 0: return None
    if w.coeffs()[1] == 0 or C.coeffs()[1] == 0: return None            # T || w, T || C (w(0) = C(0) = 0 by construction)
    if m * w * C != T ** s + v or w + C != gp * v: return None
    a, b, z, y, t = deg(w), deg(C), deg(m), deg(gp), deg(v)
    if a > b: return None
    return (a, z, y, t)


def run_group(s, kind, key, pats, counts):
    TS2 = T ** (s - 2)
    ps = set(pats)
    found = []
    if kind == 14:
        z, a = key
        Edegs = {a + y + z for (aa, zz, y, t) in pats}
        for m in monic(z):
            for w1 in monic(a - 1):
                N = TS2 + m * w1 * w1
                for E in divisors_by_degree(N.factor(), Edegs):
                    v1 = exact_div(N, E)
                    C1 = exact_div(TS2 + v1, m * w1) if v1 is not None else None
                    found.append(checkB(s, m, None, w1, C1, v1))
    elif kind == 11:
        z, t = key
        adegs = {a - 1 for (a, zz, y, tt) in pats}
        lcs = {1 if a < s - a - z else 2 for (a, zz, y, tt) in pats}
        for m in monic(z):
            r0 = -(TS2 % m)
            hd = t - 2 - z
            for lc in lcs:
                hs = [R([0])] if hd < 0 else fixed_lc(hd, EL[lc])
                for h in hs:
                    v1 = r0 + m * h
                    if v1 == 0 or deg(v1) != t - 2: continue
                    G = exact_div(TS2 + v1, m)
                    if G is None: raise RuntimeError('class error')
                    for w1 in divisors_by_degree(G.factor(), adegs):
                        found.append(checkB(s, m, None, w1, exact_div(G, w1), v1))
                if hd < 0: break
    elif kind == 12:
        z, y = key
        Edegs = {a + y + z for (a, zz, yy, t) in pats}
        for m in monic(z):
            for gp in monic(y):
                D = ONE + T ** s * m * gp * gp
                for E in divisors_by_degree(D.factor(), Edegs):
                    w = exact_div(E + ONE, m * gp)
                    if w is None or w == 0: continue
                    C = exact_div(gp * T ** s + w, E)
                    if C is None: continue
                    w1, C1 = exact_div(w, T), exact_div(C, T)
                    if w1 is None or C1 is None: continue
                    v1 = exact_div(m * w1 * C1 - TS2, ONE)
                    found.append(checkB(s, m, gp, w1, C1, v1))
    elif kind == 13:
        a, y = key
        Edegs = {a + y + z for (aa, z, yy, t) in pats}
        for w1 in monic(a - 1):
            for gp in monic(y):
                Fp = gp * T ** (s - 1) + w1
                for E in divisors_by_degree(Fp.factor(), Edegs):
                    L = exact_div(E + ONE, T * w1 * gp)
                    if L is None: continue
                    C1 = exact_div(Fp, E)
                    v1 = L * w1 * C1 - TS2
                    found.append(checkB(s, L, gp, w1, C1, v1))
    elif kind == 16:
        a, t = key
        bdegs = {s - a - z - 1 for (aa, z, y, tt) in pats}
        lcs = {1 if a < s - a - z else 2 for (aa, z, y, tt) in pats}
        for w1 in monic(a - 1):
            r0 = -(TS2 % w1)
            hd = t - 2 - (a - 1)
            for lc in lcs:
                hs = [R([0])] if hd < 0 else fixed_lc(hd, EL[lc])
                for h in hs:
                    v1 = r0 + w1 * h
                    if v1 == 0 or deg(v1) != t - 2: continue
                    K = exact_div(TS2 + v1, w1)
                    if K is None: raise RuntimeError('class error')
                    for C1 in divisors_by_degree(K.factor(), bdegs):
                        found.append(checkB(s, exact_div(K, C1), None, w1, C1, v1))
                if hd < 0: break
    for p in found:
        if p is not None and p in ps:
            counts[p] += 1


def main():
    s = int(sys.argv[1]); fn = sys.argv[2]; force = len(sys.argv) > 3 and sys.argv[3] == '1'
    FK = int(sys.argv[4]) if len(sys.argv) > 4 else None
    rows = {}
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split()
        if int(f[0]) != s: continue
        rows[tuple(map(int, f[1:5]))] = None if (force or f[5] == 'SKIP') else int(f[5])
    todo = [p for p, c in rows.items() if c is None]
    groups = {}
    for (a, z, y, t) in todo:
        opts = {(14, (z, a)): z + a - 1, (11, (z, t)): z + max(0, t - 2 - z), (12, (z, y)): z + y,
                (13, (a, y)): a - 1 + y, (16, (a, t)): a - 1 + max(0, t - 1 - a)}
        k = min(opts, key=opts.get) if FK is None else next(o for o in opts if o[0] == FK)
        groups.setdefault(k, []).append((a, z, y, t))
    counts = {p: 0 for p in todo}
    t0 = time.time()
    for (kind, key), pats in sorted(groups.items(), key=lambda kv: kv[0]):
        run_group(s, kind, key, pats, counts)
    print(f'# s={s} flint patterns={len(todo)} groups={len(groups)} time={time.time() - t0:.0f}s', file=sys.stderr)
    for p in sorted(rows):
        c = rows[p] if rows[p] is not None else counts[p]
        print(s, *p, c)


if __name__ == '__main__':
    main()
