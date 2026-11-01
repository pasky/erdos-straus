"""Z2832: Conway topograph rivers of Q_mu(A,B) = n A^2 - 2 mu A B + B^2 (disc 4(mu^2-n)), n = p prime = 1 mod 4 < 500.
Marks V_n points (river faces with value -D, D | mu, A even, gcd(D,n)=1) and ES points (B = 1).
River walk: keep an edge (e_pos, e_neg) with Q(e_pos) > 0 > Q(e_neg); next face e_pos+e_neg replaces the one of equal
sign.  All faces met are the faces adjacent to the river.  Walk both directions from the edge {(0,1),(1,mu)} until the
state (Q(e_pos), Q(e_neg), h) repeats (one full period).
Usage: python z52d_p2_ZF1_Z2832_river.py NMAX out.json
"""
import sys, json, math
from sympy import primerange


def Q(n, mu, v):
    A, B = v
    return n * A * A - 2 * mu * A * B + B * B


def walk(n, mu, direction, maxruns, target=None):
    """Run-compressed river walk. Returns (runs, period_runs, hit) where runs = list of (sign, base, step, K):
    faces base + k*step, k = 1..K, all of sign `sign`; hit = (run_index, k, face_index) of target (up to sign)."""
    ep, en = (0, 1), (1, mu)
    if direction < 0:
        en = (-1, -mu)
    runs = []; seen = {}; faces_before = 0; hit = None
    for r in range(maxruns):
        qp, qn = Q(n, mu, ep), Q(n, mu, en)
        w = (ep[0] + en[0], ep[1] + en[1]); qw = Q(n, mu, w)
        state = (qp, qn, qw)
        if state in seen:
            return runs, r - seen[state], hit, faces_before
        seen[state] = r
        if qw == 0:
            return runs, None, hit, faces_before
        if qw > 0:
            base, step, sgn = ep, en, +1
        else:
            base, step, sgn = en, ep, -1
        a, h, c = Q(n, mu, base), qw - qp - qn, Q(n, mu, step)   # Q(base + k step) = a + k h + k^2 c
        # largest K >= 1 with sgn*Q(base + K step) > 0 (c has the opposite sign of sgn)
        lo, hi = 1, 1
        while sgn * (a + hi * h + hi * hi * c) > 0:
            hi *= 2
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if sgn * (a + mid * h + mid * mid * c) > 0:
                lo = mid
            else:
                hi = mid
        K = lo
        runs.append((sgn, base, step, K))
        if target is not None and hit is None:
            for tv in (target, (-target[0], -target[1])):
                # tv = base + k step ?
                det = step[0] * 0
                for k in ([(tv[0] - base[0]) // step[0]] if step[0] else ([(tv[1] - base[1]) // step[1]] if step[1] else [])):
                    if 1 <= k <= K and (base[0] + k * step[0], base[1] + k * step[1]) == tv:
                        hit = (r, k, faces_before + k)
        faces_before += K
        newf = (base[0] + K * step[0], base[1] + K * step[1])
        if sgn > 0:
            ep = newf
        else:
            en = newf
    return runs, None, hit, faces_before


def norm_vec(v):
    A, B = v
    if A < 0 or (A == 0 and B < 0):
        A, B = -A, -B
    return (A, B)


def main():
    NMAX = int(sys.argv[1])
    out = dict(NMAX=NMAX, small_mu={}, es=[], summary={})
    pos_hist = {}
    for p in primerange(5, NMAX):
        if p % 4 != 1:
            continue
        # (a) the item's range mu <= 3 sqrt p
        sm = dict(definite=0, rivers=0, vn_points=0, es_points=0)
        for mu in range(1, int(3 * math.isqrt(p)) + 2):
            if mu * mu <= p:
                sm['definite'] += 1; continue
            if math.isqrt(mu * mu - p) ** 2 == mu * mu - p:
                continue
            sm['rivers'] += 1
            runs, per, _, _ = walk(p, mu, +1, 10 ** 6)
            fs = [((b[0] + k * st[0], b[1] + k * st[1]), None) for sg, b, st, K in runs for k in range(1, K + 1) if sg < 0]
            for v, q in fs:
                q = Q(p, mu, v)
                A, B = norm_vec(v)
                if q < 0 and mu % (-q) == 0 and A % 2 == 0 and math.gcd(-q, p) == 1 and math.gcd(A, B) == 1:
                    sm['vn_points'] += 1
                    if B == 1:
                        sm['es_points'] += 1
        out['small_mu'][p] = sm
        # (b) all ES points (B = 1): mu = p j + t, D = 4tj - 1 | mu  (COMPOSITION_ES Thm 1.3)
        for j in range(1, p + 2):
            for t in range(1, p + 1):
                D = 4 * t * j - 1
                mu = p * j + t
                if D > mu:
                    break
                if mu % D:
                    continue
                f = mu * mu - p
                fr, fper, fhit, fF = walk(p, mu, +1, 10 ** 6, (2 * j, 1))
                br, bper, bhit, bF = walk(p, mu, -1, 10 ** 6, (2 * j, 1))
                rec = dict(p=p, mu=mu, j=j, t=t, D=D, fwd_hit=fhit, bwd_hit=bhit, period_runs=fper, period_faces=fF,
                           D_lt_sqrt_f=D * D < f, first_runs=[(sg, K) for sg, b, st, K in br[:5]])
                idx = fhit[0] if fhit else None; idxb = bhit[0] if bhit else None
                out['es'].append(rec)
                key = (idx, idxb)
                pos_hist[str(key) + ' j=' + ('1' if j == 1 else '>=2')] = pos_hist.get(str(key) + ' j=' + ('1' if j == 1 else '>=2'), 0) + 1
    out['summary']['es_points'] = len(out['es'])
    out['summary']['position_hist(fwd_index,bwd_index)'] = pos_hist
    out['summary']['es_not_on_river'] = sum(1 for r in out['es'] if r['fwd_hit'] is None and r['bwd_hit'] is None)
    out['summary']['small_mu_totals'] = {k: sum(v[k] for v in out['small_mu'].values()) for k in
                                         ['definite', 'rivers', 'vn_points', 'es_points']}
    print(json.dumps(out['summary'], indent=1))
    ex = [r for r in out['es'] if r['p'] in (13, 17, 29)][:8]
    print(json.dumps(ex)[:3000])
    for r in out['es']:
        pass
    json.dump(out, open(sys.argv[2], 'w'))


if __name__ == '__main__':
    main()
