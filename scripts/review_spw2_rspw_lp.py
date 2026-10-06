"""R53 from-scratch re-solve of the RSPW LP of SPW2 §2 (EVIDENCE table).
R >= 0 on [-L, N+L]; profile mod d <= D equals c(.,d); for every modulus
e > CN: full classes (meeting [1,N]) have mass <= 1-eta, sparse classes <= K
(K = inf: no constraint). Moduli e > span act pointwise. Maximise eta."""
import numpy as np, math, sys
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def solve(N, L, C, K=math.inf):
    D = N//2; xs = np.arange(-L, N+L+1); n = len(xs); span = n
    rows, cols, vals, rhs, kind = [], [], [], [], []
    r = 0
    def add(idx, b, is_full):
        nonlocal r
        rows.extend([r]*len(idx)); cols.extend(idx); vals.extend([1.0]*len(idx))
        if is_full: rows.append(r); cols.append(n); vals.append(1.0)
        rhs.append(b); r += 1
    emin = math.floor(C*N) + 1
    for e in range(emin, span):
        res = np.mod(xs, e)
        for b in range(e):
            idx = np.nonzero(res == b)[0]
            if len(idx) == 0: continue
            full = any(1 <= xs[i] <= N for i in idx)
            if full: add(idx, 1.0, True)
            elif K < math.inf: add(idx, K, False)
    for i in range(n):                       # moduli >= span: single points
        if 1 <= xs[i] <= N: add([i], 1.0, True)
        elif K < math.inf: add([i], K, False)
    Aub = coo_matrix((vals, (rows, cols)), shape=(r, n+1)).tocsr()
    er, ec, ev, eb = [], [], [], []; q = 0
    for d in range(1, D+1):
        res = np.mod(xs, d)
        for b in range(d):
            idx = np.nonzero(res == b)[0]
            er.extend([q]*len(idx)); ec.extend(idx); ev.extend([1.0]*len(idx))
            eb.append(sum(1 for m in range(1, N+1) if m % d == b)); q += 1
    Aeq = coo_matrix((ev, (er, ec)), shape=(q, n+1)).tocsr()
    c = np.zeros(n+1); c[n] = -1
    sol = linprog(c, A_ub=Aub, b_ub=rhs, A_eq=Aeq, b_eq=eb,
                  bounds=[(0, None)]*n + [(None, None)], method="highs")
    assert sol.status == 0, sol.message
    R = sol.x[:n]
    return -sol.fun, R, xs

if __name__ == "__main__":
    args = sys.argv[1:]
    N, L, C = int(args[0]), int(args[1]), float(args[2])
    K = math.inf if len(args) < 4 or args[3] == "inf" else float(args[3])
    eta, R, xs = solve(N, L, C, K)
    W = (xs >= 1) & (xs <= N)
    print(f"N={N} L={L} C={C} K={K}: eta*={eta:.4f}  mass on W={R[W].sum():.3f}  max R on W={R[W].max():.3f}")
