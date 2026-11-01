# Z1409: QUBO for the (★) Type II line at fixed level C (FRONTIER §2.1: 4uBC - u - B = p, R(p) >= 1 => ES(p)),
# u, B in {0..2^b-1} (b bits each; u = 0 or B = 0 never solves since p > 0), quadratised with the standard Rosenberg
# multiplication gadget w_ij = u_i B_j (b^2 ancillas): n = 2b + b^2 qubits (b = 3: 15 qubits).
#   L = 4C * sum_ij 2^{i+j} w_ij - sum 2^i u_i - sum 2^j B_j - p   (linear in the qubits)  ->  H_P = L^2 + M * sum_ij ros(u_i,B_j,w_ij),
#   ros(x,y,w) = xy - 2xw - 2yw + 3w  (= 0 iff w = xy, >= 1 otherwise).
# M = smallest power of 2 with no ancilla-inconsistent state below the first excited consistent level (enumeration).
# Classical spectrum: E0, gap, ground degeneracy g.  Quantum annealing: H(s) = -(1-s) sum X_q + s * H_P / max|QUBO coeff|;
# Lanczos (scipy eigsh) for the lowest g+1 levels on an s-grid + refinement; Delta_min = min_s (E_g - E_0)  (degeneracy-aware)
# and min_s (E_1 - E_0).
import numpy as np, sys, json, time
from scipy.sparse.linalg import eigsh, LinearOperator
def build(b, C, p):
    nq = 2 * b + b * b; idx = np.arange(1 << nq, dtype=np.int64); bit = lambda q: (idx >> q) & 1
    u = [bit(i) for i in range(b)]; B = [bit(b + j) for j in range(b)]
    wq = lambda i, j: 2 * b + b * i + j
    w = {(i, j): bit(wq(i, j)) for i in range(b) for j in range(b)}
    a = np.zeros(nq)
    for i in range(b):
        a[i] = -2**i; a[b + i] = -2**i
        for j in range(b): a[wq(i, j)] = 4 * C * 2**(i + j)
    X = np.stack([bit(q) for q in range(nq)], axis=1).astype(np.float64)
    L = X @ a - p
    PEN = sum(u[i] * B[j] - 2 * u[i] * w[i, j] - 2 * B[j] * w[i, j] + 3 * w[i, j] for i in range(b) for j in range(b))
    cons = PEN == 0
    L2 = L * L
    lv = np.unique(L2[cons]); E1c = lv[1]
    M = 1
    while (L2 + M * PEN)[~cons].min() < E1c: M *= 2
    H = L2 + M * PEN
    # QUBO coefficients (upper-triangular): L^2 = sum_q (a_q^2 - 2p a_q) x_q + sum_{q<r} 2 a_q a_r x_q x_r + p^2
    Q = np.triu(2 * np.outer(a, a), 1); Q[np.diag_indices(nq)] = a * a - 2 * p * a
    for i in range(b):
        for j in range(b):
            x, y, ww = i, b + j, wq(i, j)
            Q[x, y] += M; Q[x, ww] += -2 * M; Q[y, ww] += -2 * M; Q[ww, ww] += 3 * M
    uval = sum(2**i * u[i] for i in range(b)); Bval = sum(2**j * B[j] for j in range(b))
    return nq, idx, H, float(np.abs(Q).max()), M, uval, Bval
def analyse(p, b, C, s_grid):
    nq, idx, H, scale, M, uval, Bval = build(b, C, p)
    E0 = H.min(); g = int((H == E0).sum()); lv = np.unique(H); E1 = lv[1]
    sols = sorted(set(zip(uval[H == E0].tolist(), Bval[H == E0].tolist()))) if E0 == 0 else []
    Hn = H / scale
    from scipy.sparse import csr_matrix, diags
    rows = np.concatenate([idx] * nq); cols = np.concatenate([idx ^ (1 << q) for q in range(nq)])
    Xsum = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(1 << nq, 1 << nq))
    KMAX = 4   # degeneracy-aware gap only resolved when g + 1 <= KMAX (else reported as E_{KMAX-1} - E_0 lower bound proxy)
    def gap_at(sv):
        op = (-(1 - sv)) * Xsum + diags(sv * Hn)
        k = min(g + 1, KMAX)
        ev = np.sort(eigsh(op, k=k, which='SA', tol=1e-7, return_eigenvectors=False, ncv=max(2 * k + 12, 24), maxiter=100000))
        return float(ev[min(g, k - 1)] - ev[0]), float(ev[1] - ev[0])
    gaps = [(float(sv),) + gap_at(sv) for sv in s_grid]
    j = int(np.argmin([x[1] for x in gaps])); lo = s_grid[max(j - 1, 0)]; hi = s_grid[min(j + 1, len(s_grid) - 1)]
    gaps += [(float(sv),) + gap_at(sv) for sv in np.linspace(lo, hi, 6)[1:-1]]
    gaps.sort(); dmin = min(x[1] for x in gaps); smin = [x[0] for x in gaps if x[1] == dmin][0]
    return dict(p=p, b=b, C=C, nq=nq, M=M, scale=scale, E0=float(E0), classical_gap=float(E1 - E0), ground_deg=g,
                solutions_uB=sols, min_gap=dmin, s_at_min=smin, min_gap_E1E0=min(x[2] for x in gaps),
                gap_at_s1_normalised=float((lv[min(1, len(lv)-1)] - E0) / scale) if g == 1 else None, gaps=gaps)
if __name__ == '__main__':
    ps = [int(x) for x in sys.argv[1].split(',')]; b = int(sys.argv[2]); C = int(sys.argv[3])
    s_grid = np.linspace(0.05, 0.99, int(sys.argv[4]) if len(sys.argv) > 4 else 12)
    for p in ps:
        t0 = time.time(); r = analyse(p, b, C, s_grid); r['secs'] = round(time.time() - t0, 1)
        print(json.dumps(r), flush=True)
