"""Z1131: cavity / sum-product BP on a small loopy factor graph for 4/p = 1/x+1/y+1/z (G4, NC0).
Exact solution set S = {(x<=y<=z) : 4/p = 1/x+1/y+1/z} enumerated exactly (x in [ceil(p/4), floor(3p/4)],
y in [x, floor(2/(4/p-1/x))], z solved; no box truncation). Variables X,Y,Z over the domain D = values
appearing in S (unordered union). Factor graph (loopy):
  F_exact(X,Y,Z) : 1 iff (X,Y,Z) in S   (sparse 3-ary factor)
  F_xy, F_yz, F_xz : ordering indicators [X<=Y], [Y<=Z], [X<=Z]  (pairwise, create cycles)
Sum-product BP (damped, flooding) vs exact marginals = uniform over S (ordered triples).
Report: max/mean L1 marginal error, iterations, and whether MAP = a solution."""
import sys, math
from fractions import Fraction
import numpy as np


def solutions(p):
    S = []
    for x in range(math.ceil(p / 4), (3 * p) // 4 + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        ymax = math.floor(2 / r)
        for y in range(x, ymax + 1):
            r2 = r - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1:
                S.append((x, y, r2.denominator))
    return S


def bp(p, S, iters=200, damp=0.5):
    D = sorted({v for t in S for v in t})
    idx = {v: i for i, v in enumerate(D)}
    n = len(D)
    T = np.array([[idx[a], idx[b], idx[c]] for a, b, c in S])  # sparse table
    # factor-to-variable messages for F_exact: store as arrays over domain
    # variable-to-factor messages (uniform init)
    mu = {k: np.ones(n) / n for k in "XYZ"}          # var->F_exact
    # var->order-factor messages: pairs (X,Y),(Y,Z),(X,Z); ordering factor matrix L[a,b]=[D[a]<=D[b]]
    Ds = np.array(D)
    L = (Ds[:, None] <= Ds[None, :]).astype(float)
    ord_pairs = [("X", "Y"), ("Y", "Z"), ("X", "Z")]
    nu = {}  # (var, pair) var->ordering factor
    fo = {}  # ordering factor -> var
    for pr in ord_pairs:
        for v in pr:
            nu[(v, pr)] = np.ones(n) / n
            fo[(pr, v)] = np.ones(n) / n
    fe = {k: np.ones(n) / n for k in "XYZ"}           # F_exact -> var
    col = {"X": 0, "Y": 1, "Z": 2}
    for it in range(iters):
        # --- F_exact -> var (sum-product over the sparse table) ---
        new_fe = {}
        for v in "XYZ":
            c = col[v]
            others = [w for w in "XYZ" if w != v]
            prod = np.ones(len(T))
            for w in others:
                prod *= mu[w][T[:, col[w]]]
            m = np.bincount(T[:, c], weights=prod, minlength=n)
            new_fe[v] = m / max(m.sum(), 1e-300)
        # --- ordering factors -> var, var -> ordering factor ---
        new_fo = {}
        for pr in ord_pairs:
            a, b = pr
            # message to a: sum_b L[a,b] nu_b(b)
            new_fo[(pr, a)] = L @ nu[(b, pr)]
            new_fo[(pr, b)] = L.T @ nu[(a, pr)]
            for vv in (a, b):
                new_fo[(pr, vv)] /= max(new_fo[(pr, vv)].sum(), 1e-300)
        # --- var -> factors (product of incoming except target) ---
        new_mu = {}
        # var->F_exact : product of incoming from ordering factors only
        for v in "XYZ":
            inc = np.ones(n)
            for pr in ord_pairs:
                if v in pr:
                    inc *= fo[(pr, v)]
            new_mu[v] = inc / max(inc.sum(), 1e-300)
        new_nu = {}
        for pr in ord_pairs:
            for v in pr:
                inc = fe[v].copy()
                for pr2 in ord_pairs:
                    if v in pr2 and pr2 != pr:
                        inc *= fo[(pr2, v)]
                new_nu[(v, pr)] = inc / max(inc.sum(), 1e-300)
        # damping
        diff = 0.0
        for v in "XYZ":
            nv = damp * mu[v] + (1 - damp) * new_mu[v]
            diff = max(diff, np.abs(nv - mu[v]).sum()); mu[v] = nv
            fe[v] = damp * fe[v] + (1 - damp) * new_fe[v]
        for k in new_fo:
            fo[k] = damp * fo[k] + (1 - damp) * new_fo[k]
        for k in new_nu:
            nu[k] = damp * nu[k] + (1 - damp) * new_nu[k]
        if diff < 1e-10 and it > 5:
            break
    # beliefs
    belief = {}
    for v in "XYZ":
        b = fe[v].copy()
        for pr in ord_pairs:
            if v in pr:
                b *= fo[(pr, v)]
        belief[v] = b / b.sum()
    return D, belief, it + 1


def bp_pairwise(p, S, iters=500, damp=0.5):
    """Loopy BP on the triangle of PAIRWISE projections of S (no 3-ary factor): F_XY, F_YZ, F_XZ."""
    D = sorted({v for t in S for v in t})
    idx = {v: i for i, v in enumerate(D)}
    n = len(D)
    P = {"XY": np.zeros((n, n)), "YZ": np.zeros((n, n)), "XZ": np.zeros((n, n))}
    for t in S:
        a, b, c = (idx[v] for v in t)
        P["XY"][a, b] = 1; P["YZ"][b, c] = 1; P["XZ"][a, c] = 1
    facs = {"XY": ("X", "Y"), "YZ": ("Y", "Z"), "XZ": ("X", "Z")}
    v2f = {(v, f): np.ones(n) / n for f, (a, b) in facs.items() for v in (a, b)}
    f2v = {(v, f): np.ones(n) / n for f, (a, b) in facs.items() for v in (a, b)}
    for it in range(iters):
        new_f2v = {}
        for f, (a, b) in facs.items():
            M = P[f]
            new_f2v[(a, f)] = M @ v2f[(b, f)]
            new_f2v[(b, f)] = M.T @ v2f[(a, f)]
            for k in ((a, f), (b, f)):
                new_f2v[k] = new_f2v[k] / max(new_f2v[k].sum(), 1e-300)
        new_v2f = {}
        for (v, f) in v2f:
            inc = np.ones(n)
            for g in facs:
                if g != f and v in facs[g]:
                    inc = inc * new_f2v[(v, g)]
            new_v2f[(v, f)] = inc / max(inc.sum(), 1e-300)
        diff = 0.0
        for k in v2f:
            nv = damp * v2f[k] + (1 - damp) * new_v2f[k]
            diff = max(diff, np.abs(nv - v2f[k]).sum()); v2f[k] = nv
            f2v[k] = damp * f2v[k] + (1 - damp) * new_f2v[k]
        if diff < 1e-12 and it > 5:
            break
    belief = {}
    for v in "XYZ":
        b = np.ones(n)
        for g in facs:
            if v in facs[g]:
                b = b * f2v[(v, g)]
        belief[v] = b / b.sum()
    return D, belief, it + 1


def exact_marg(D, S):
    idx = {v: i for i, v in enumerate(D)}
    out = {}
    for c, v in enumerate("XYZ"):
        m = np.zeros(len(D))
        for t in S:
            m[idx[t[c]]] += 1
        out[v] = m / m.sum()
    return out


MODE = sys.argv[1] if len(sys.argv) > 1 else "exact3"
PRIMES = [int(a) for a in sys.argv[2:]] or [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
print("mode:", MODE)
print(f"{'p':>4s} {'|S|':>5s} {'|D|':>5s} {'iters':>5s} {'meanL1':>8s} {'maxL1':>8s} {'MAP-ok':>6s}")
for p in PRIMES:
    S = solutions(p)
    D, bel, its = bp(p, S) if MODE == "exact3" else bp_pairwise(p, S)
    ex = exact_marg(D, S)
    errs = [np.abs(bel[v] - ex[v]).sum() for v in "XYZ"]
    # MAP: argmax belief per variable; is the triple (argmax) a solution?
    mx = tuple(D[int(np.argmax(bel[v]))] for v in "XYZ")
    mapok = mx in set(S) or tuple(sorted(mx)) in set(S)
    print(f"{p:4d} {len(S):5d} {len(D):5d} {its:5d} {np.mean(errs):8.4f} {np.max(errs):8.4f} {str(mapok):>6s}")
