"""Z2865: GPPV / CCFGH homological blocks Ẑ_b(q) of Seifert manifolds with 3 singular fibres,
via CCFGH arXiv:1809.10148 eq. (6.2)/(6.4)-(6.5):
  Ẑ_b(q) = q^{-(3L+Σ a_v)/4} · v.p.∮ Π_v dz_v/(2πi z_v) (z_v - 1/z_v)^{2-deg v} Σ_{ℓ∈2MZ^L+b} q^{-(ℓ,M^{-1}ℓ)/4} Π z_v^{ℓ_v}
(v.p. = average of the expansions at z→0 and z→∞).  For a star graph only ℓ supported on the centre (odd) and the
three leg ends (±1) contribute (CCFGH Lemma 1 proof).  We enumerate all such ℓ, group them by their class in
(2Z^L+δ)/2MZ^L, and output every reachable block.  Calibrated on CCFGH (6.12)-(6.13), M(-1;1/2,1/3,1/9), and on
Σ(2,3,5) = M(-2;1/2,2/3,4/5).
ES spaces: for a solution 4/n = 1/x+1/y+1/z take Y = M(-3; (x-1)/x, (y-1)/y, (z-1)/z), e = -4/n (negative definite).
"""
import sys
from fractions import Fraction as Fr
from math import gcd


def negcf(p, q):
    """-p/q = a1 - 1/(a2 - 1/(...)), a_i <= -2  (p/q > 1)."""
    out = []
    P, Q = p, q  # value p/q
    while Q:
        a = -((P + Q - 1) // Q)  # -ceil(P/Q)
        out.append(a)
        # p/q = -a - 1/(r)  => r = 1/(-a - p/q) = Q/(-a*Q - P)
        P, Q = Q, -a * Q - P
    return out


def build(b, fibres):
    """vertices: 0 = centre; legs from fibres [(q,p)] with q/p in (0,1).  returns weights, adjacency, ends, legs"""
    w = [b]
    adj = {0: []}
    ends = []
    legs = []
    for (q, p) in fibres:
        cf = negcf(p, q)
        prev = 0
        leg = []
        for a in cf:
            v = len(w)
            w.append(a)
            adj[v] = [prev]
            adj[prev].append(v)
            leg.append(v)
            prev = v
        ends.append(prev)
        legs.append(leg)
    return w, adj, ends, legs


def tree_solve(w, legs, rhs):
    """solve M x = rhs exactly, M = diag(w) + adjacency (star graph with chain legs)."""
    rhs = [Fr(r) for r in rhs]
    dc, rc = Fr(w[0]), rhs[0]
    elim = []
    for leg in legs:
        # eliminate from tip (last) towards centre
        d = [Fr(w[v]) for v in leg]
        r = [rhs[v] for v in leg]
        for k in range(len(leg) - 1, 0, -1):
            d[k - 1] -= 1 / d[k]
            r[k - 1] -= r[k] / d[k]
        dc -= 1 / d[0]
        rc -= r[0] / d[0]
        elim.append((leg, d, r))
    x = {0: rc / dc}
    for leg, d, r in elim:
        prev = x[0]
        for k in range(len(leg)):
            xv = (r[k] - prev) / d[k]
            x[leg[k]] = xv
            prev = xv
    return [x[i] for i in range(len(w))]


def det_star(w, legs):
    dc = Fr(w[0])
    det = Fr(1)
    for leg in legs:
        d = [Fr(w[v]) for v in leg]
        for k in range(len(leg) - 1, 0, -1):
            det *= d[k]
            d[k - 1] -= 1 / d[k]
        det *= d[0]
        dc -= 1 / d[0]
    return det * dc


def zhat(b, fibres, lmax=60, qmax=None):
    w, adj, ends, legs = build(b, fibres)
    L = len(w)
    D = abs(det_star(w, legs))
    assert D.denominator == 1
    D = int(D)
    special = [0] + ends
    cols = {}
    for v in special:
        e = [0] * L
        e[v] = 1
        cols[v] = tree_solve(w, legs, e)
    # quadratic form block and integer class vectors
    B = {(u, v): cols[v][u] for u in special for v in special}
    Icol = {v: [int(D * c) for c in cols[v]] for v in special}
    for v in special:
        assert all((D * c).denominator == 1 for c in cols[v])
    mod = 2 * D
    pref = Fr(-(3 * L + sum(w)), 4)
    terms = {}
    for lc in range(-lmax, lmax + 1, 2):
        if lc % 2 == 0:
            continue
        for s in range(8):
            eps = [1 if (s >> i) & 1 else -1 for i in range(3)]
            ell = {0: lc}
            for i, e_ in enumerate(ends):
                ell[e_] = ell.get(e_, 0) + eps[i]
            quad = sum(ell[u] * ell[v] * B[(u, v)] for u in ell for v in ell)
            expo = pref - quad / 4
            coef = Fr(1 if lc > 0 else -1, 2)
            for i in range(3):
                coef *= -eps[i]
            key = tuple(sum(ell[v] * Icol[v][k] for v in ell) % mod for k in range(L))
            terms.setdefault(key, {})
            terms[key][expo] = terms[key].get(expo, 0) + coef
    # completeness bound: smallest exponent reachable with |lc| = lmax+2
    bound = None
    for lc in (lmax + 2, -(lmax + 2)):
        for s in range(8):
            eps = [1 if (s >> i) & 1 else -1 for i in range(3)]
            ell = {0: lc}
            for i, e_ in enumerate(ends):
                ell[e_] = ell.get(e_, 0) + eps[i]
            quad = sum(ell[u] * ell[v] * B[(u, v)] for u in ell for v in ell)
            ex = pref - quad / 4
            bound = ex if bound is None or ex < bound else bound
    # delta class key
    delta = [len(adj[v]) - 2 for v in range(L)]
    xd = tree_solve(w, legs, delta)
    dkey = tuple(int(D * c) % mod for c in xd)
    out = {}
    for key, ser in terms.items():
        ser = {e: c for e, c in ser.items() if c != 0 and e < bound}
        out[key] = dict(sorted(ser.items()))
    return out, dkey, D, bound, L, B[(0, 0)]


def fmt(ser, nterms=12):
    if not ser:
        return "0"
    e0 = min(ser)
    s = []
    for e, c in list(ser.items())[:nterms]:
        s.append(f"{'+' if c > 0 else '-'}{abs(c) if abs(c) != 1 else ''}q^{e - e0}")
    return f"q^({e0})·(" + " ".join(s) + " …)"


if __name__ == "__main__":
    # calibration
    for name, b, fib in [("M(-1;1/2,1/3,1/9) [CCFGH 6.12-13]", -1, [(1, 2), (1, 3), (1, 9)]),
                         ("Sigma(2,3,5)=M(-2;1/2,2/3,4/5)", -2, [(1, 2), (2, 3), (4, 5)])]:
        out, dkey, D, bound, L, Bcc = zhat(b, fib, lmax=41)
        print(name, "|H1|=", D, "L=", L, "complete below q^", bound)
        for k, ser in out.items():
            if ser:
                print("   ", "b=δ" if k == dkey else "   ", fmt(ser))


def es_solutions(n):
    sols = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r = Fr(4, n) - Fr(1, x)
        if r <= 0:
            continue
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fr(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                sols.append((x, y, s.denominator))
    return sols


def es_run(nmax=21, lmax=13, zmax=600):
    """For each n<=nmax and solution with z<=zmax: Ẑ_δ, number of reachable classes, check quadratic-form structure."""
    import json
    res = {}
    for n in range(5, nmax + 1):
        for (x, y, z) in es_solutions(n):
            if z > zmax or x < 2:
                continue
            out, dkey, D, bound, L, Bcc = zhat(-3, [(x - 1, x), (y - 1, y), (z - 1, z)], lmax=lmax)
            s2 = x * y + y * z + z * x
            assert D == s2 and Bcc == Fr(-n, 4), (n, x, y, z, D, Bcc)
            zd = out.get(dkey, {})
            nz = sum(1 for k, s in out.items() if s)
            # Weyl-symmetrised delta block (delta = -delta?)
            res[f"{n}:{x},{y},{z}"] = {"H1": D, "L": L, "reach_classes": nz,
                                      "Zdelta": [[str(e), str(c)] for e, c in list(zd.items())[:20]],
                                      "complete_below": str(bound)}
            print(n, (x, y, z), "|H1|=", D, "L=", L, "#reachable classes", nz, " Ẑ_δ =", fmt(zd, 10), flush=True)
    return res


if __name__ == "__main__" and len(sys.argv) > 1:
    import json
    r = es_run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    json.dump(r, open(sys.argv[4], "w"), indent=0)


def es_delta_block(n, x, y, z, nterms=8):
    """Fast exact δ-block for the ES Seifert space via the verified closed form of M^{-1} on {c, ends}:
    B_cc = 1/e, B_ci = 1/(e a_i), B_ij = 1/(e a_i a_j) - δ_ij (a_i-1)/a_i, e = -4/n.  Class test via integer M^{-1}
    columns (numpy).  Returns ord(e_c), list of (ε, residue r mod 2ord) in class δ, and the Weyl-symmetrised block
    (Ẑ_δ + Ẑ_{-δ} if δ ≠ -δ, else Ẑ_δ) as exponent->coefficient (first nterms terms)."""
    import numpy as np
    from math import lcm
    w, adj, ends, legs = build(-3, [(x - 1, x), (y - 1, y), (z - 1, z)])
    L = len(w)
    D = x * y + y * z + z * x
    cols = {}
    for v in [0] + ends:
        e = [0] * L
        e[v] = 1
        cols[v] = tree_solve(w, legs, e)
    ordc = lcm(*[c.denominator for c in cols[0]])
    W = {v: np.array([int(D * c) for c in cols[v]], dtype=np.int64) for v in cols}
    mod = 2 * D
    delta = [len(adj[v]) - 2 for v in range(L)]
    xd = tree_solve(w, legs, delta)
    dk = np.array([int(D * c) % mod for c in xd], dtype=np.int64)
    ndk = (-dk) % mod
    selfconj = bool((dk == ndk).all())
    a = [x, y, z]
    e_ = Fr(-4, n)
    pref = Fr(-(3 * L + sum(w)), 4)
    per = 2 * ordc
    S = []
    for s in range(8):
        eps = [1 if (s >> i) & 1 else -1 for i in range(3)]
        E = sum(eps[i] * W[ends[i]] for i in range(3))
        for lc in range(1 - per, per, 2):
            k = (lc * W[0] + E) % mod
            for tag, tgt in (("+", dk), ("-", ndk)):
                if tag == "-" and selfconj:
                    continue
                if (k == tgt).all():
                    S.append((tuple(eps), lc, tag))
    # build series: terms lc ≡ r (mod per), |lc| up to some range
    def expo(lc, eps):
        u = lc + sum(Fr(eps[i], a[i]) for i in range(3))
        return pref - u * u / (4 * e_) + sum(Fr(a[i] - 1, 4 * a[i]) for i in range(3))
    ser = {}
    for (eps, r, tag) in S:
        if r < 0:
            continue  # handle r and the negative residues via full range below
    for (eps, r, tag) in S:
        for kk in range(-6, 7):
            lc = r + kk * per
            ex = expo(lc, eps)
            c = Fr(1 if lc > 0 else -1, 2)
            for i in range(3):
                c *= -eps[i]
            ser[ex] = ser.get(ex, 0) + c
    # dedupe: residues found in (-per, per) represent each class twice (r and r-per); halve consistently
    ser = {e: c / 2 for e, c in ser.items()}
    ser = {e: c for e, c in sorted(ser.items()) if c != 0}
    return ordc, selfconj, S, dict(list(ser.items())[:nterms])
