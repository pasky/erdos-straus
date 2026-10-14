"""si_fit: exact-relation test of ES-sign counts on X_n against a dictionary of classical functions.

Targets (from data/si/census_*.txt, produced by si_census): Np, Nm, S = Np - Nm, |X|, interior Np/Nm, t-weighted.
Columns: Hurwitz class numbers H(kn) and Kronecker-Hurwitz-type sums sum_s H(kn - j s^2), twisted divisor sums,
shifted divisor sums, representation numbers of small ternary forms, quasi-polynomials.
Test: for each residue class n mod M (M = 8 or 24), rank of [columns | target] vs rank [columns] modulo a large
prime (exact over F_P; an exact Q-relation forces equal rank), plus float least-squares relative residual.
usage: PYTHONPATH=scripts uv run python scripts/si_fit.py census.txt H12.bin NMAX [M]
"""
import sys
import numpy as np
from sympy import factorint

P = 2**61 - 1


def rank_mod(Mat):
    M = [[int(x) % P for x in row] for row in Mat]
    r = 0
    cols = len(M[0])
    for c in range(cols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], P - 2, P)
        M[r] = [(x * inv) % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % P for a, b in zip(M[i], M[r])]
        r += 1
    return r


def kron(D, d):
    from sympy import jacobi_symbol
    # Kronecker symbol (D/d) for d > 0
    res = 1
    while d % 2 == 0:
        d //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            res = -res
    if d == 1:
        return res
    return res * jacobi_symbol(D % d, d)


def main():
    census, hfile, NMAX = sys.argv[1], sys.argv[2], int(sys.argv[3])
    MOD = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    H = np.fromfile(hfile, dtype=np.int32).astype(np.int64)  # 12 H(D)
    d = np.loadtxt(census, dtype=np.int64)
    d = d[(d[:, 0] >= 3) & (d[:, 0] <= NMAX)]
    def h(D):
        return int(H[D]) if 0 <= D < len(H) else None
    def kh(k, j, n, sgn=False):
        s, tot = 0, 0
        while k * n - j * s * s >= 0:
            D = k * n - j * s * s
            w = 1 if s == 0 else 2
            if sgn and s % 2:
                w = -w
            tot += w * int(H[D])
            s += 1
        return tot
    # small ternary forms: r_Q(n) via counting (precompute by brute force)
    tern = {"111": (1, 1, 1), "112": (1, 1, 2), "122": (1, 2, 2), "113": (1, 1, 3), "123": (1, 2, 3), "135": (1, 3, 5)}
    R = {k: np.zeros(NMAX + 1, dtype=np.int64) for k in tern}
    import math
    for k, (a, b, c) in tern.items():
        X = int(math.isqrt(NMAX // a)) + 1
        for x in range(-X, X + 1):
            ax = a * x * x
            if ax > NMAX:
                continue
            Y = int(math.isqrt((NMAX - ax) // b)) + 1
            for y in range(-Y, Y + 1):
                s2 = ax + b * y * y
                if s2 > NMAX:
                    continue
                Z = int(math.isqrt((NMAX - s2) // c))
                zs = np.arange(-Z, Z + 1)
                vals = s2 + c * zs * zs
                np.add.at(R[k], vals[vals <= NMAX], 1)
    names, cols = [], []
    def add(name, f):
        names.append(name)
        cols.append(f)
    add("1", lambda n, F: 1)
    add("n", lambda n, F: n)
    add("12H(n)", lambda n, F: h(n))
    add("12H(3n)", lambda n, F: h(3 * n))
    add("12H(4n)", lambda n, F: h(4 * n))
    add("12H(8n)", lambda n, F: h(8 * n))
    add("12H(12n)", lambda n, F: h(12 * n))
    add("12H(16n)", lambda n, F: h(16 * n))
    add("12H(24n)", lambda n, F: h(24 * n))
    add("KH(1,1)", lambda n, F: kh(1, 1, n))
    add("KH(4,1)", lambda n, F: kh(4, 1, n))
    add("KH(4,1,sgn)", lambda n, F: kh(4, 1, n, True))
    add("KH(8,1)", lambda n, F: kh(8, 1, n))
    add("KH(8,1,sgn)", lambda n, F: kh(8, 1, n, True))
    add("KH(4,2)", lambda n, F: kh(4, 2, n))
    add("KH(8,2)", lambda n, F: kh(8, 2, n))
    add("KH(4,8)", lambda n, F: kh(4, 8, n))
    add("KH(16,1)", lambda n, F: kh(16, 1, n))
    add("KH(3,1)", lambda n, F: kh(3, 1, n))
    add("KH(12,1)", lambda n, F: kh(12, 1, n))
    for D in (1, -4, 8, -8, -3, 12, 5, -7):
        add(f"sig0({D})", lambda n, F, D=D: sum(kron(D, x) for x in F["divs"]))
        add(f"sig1({D})", lambda n, F, D=D: sum(kron(D, x) * x for x in F["divs"]))
    add("sum min(d,n/d)", lambda n, F: sum(min(x, n // x) for x in F["divs"]))
    for s in (1, 2, 3):
        add(f"tau(n+{s})", lambda n, F, s=s: F["tau"][s])
    add("tau(2n+1)", lambda n, F: F["tau2"])
    for k in tern:
        add(f"r_{k}", lambda n, F, k=k: int(R[k][n]))
    add("issq", lambda n, F: 1 if int(math.isqrt(n)) ** 2 == n else 0)
    from sympy import divisors, divisor_count
    targets = {"Np": [], "Nm": [], "S": [], "X": [], "NpI": [], "NmI": [], "SpT": [], "SmT": []}
    rowsets = {}
    for row in d:
        n = int(row[0])
        F = {"divs": divisors(n), "tau": {s: divisor_count(n + s) for s in (1, 2, 3)}, "tau2": divisor_count(2 * n + 1)}
        vals = [f(n, F) for f in cols]
        if any(v is None for v in vals):
            continue
        tv = {"Np": row[1], "Nm": row[2], "S": row[1] - row[2], "X": row[1] + row[2], "NpI": row[3], "NmI": row[4],
              "SpT": row[5], "SmT": row[6]}
        rowsets.setdefault(n % MOD, []).append((vals, tv))
    print(f"columns ({len(names)}):", ", ".join(names))
    for cls in sorted(rowsets):
        rs = rowsets[cls]
        if len(rs) < 3 * len(names):
            continue
        C = np.array([r[0] for r in rs], dtype=float)
        rC = rank_mod([r[0] for r in rs])
        out = []
        for tname in targets:
            y = np.array([float(r[1][tname]) for r in rs])
            rCy = rank_mod([r[0] + [int(r[1][tname])] for r in rs])
            coef, *_ = np.linalg.lstsq(C, y, rcond=None)
            res = y - C @ coef
            rel = np.sqrt(np.mean(res ** 2)) / max(1e-9, np.sqrt(np.mean((y - y.mean()) ** 2)))
            out.append(f"{tname}: {'IN-SPAN' if rCy == rC else 'no'} rel={rel:.3f}")
        print(f"n≡{cls} (mod {MOD}): rows={len(rs)} rank(cols)={rC} | " + "; ".join(out))


if __name__ == "__main__":
    main()
