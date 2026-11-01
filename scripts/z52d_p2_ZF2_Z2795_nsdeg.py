"""Z2795: Nullstellensatz degree of the bounded (*)-infeasibility system in the natural integer (Q) encoding.
Variables: k bits each for u, B, C with u = 1 + sum 2^i u_i in [1, 2^k] (same for B, C); n = 3k Boolean variables.
System {P := 4uBC - u - B - p = 0, x_i^2 = x_i}. If P has no zero on the cube, the minimal NS degree over Q equals
deg ML(1/P) + 3 (ML = multilinear interpolant on the cube; lower bound since g must reduce to ML(1/P) and deg(gP) =
deg g + 3; upper bound by reducing g P - 1 in the Boolean ideal). We compute deg ML(1/P) exactly mod two large
primes (coefficient vanishing mod both primes treated as zero) via the Moebius transform on {0,1}^n.
Usage: uv run --with numpy python scripts/z52d_p2_ZF2_Z2795_nsdeg.py k p1 p2 ..."""
import sys, json
import numpy as np
QS = [2147483647, 2147483629]
def modinv_vec(a, q):
    r = np.ones_like(a); b = a.copy(); e = q - 2
    while e:
        if e & 1: r = (r * b) % q
        b = (b * b) % q; e >>= 1
    return r
def ml_degree(k, p):
    n = 3 * k; N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    m = (1 << k) - 1
    u = (idx & m) + 1; B = ((idx >> k) & m) + 1; C = ((idx >> (2 * k)) & m) + 1
    P = 4 * u * B * C - u - B - p
    if (P == 0).any():
        return None, int((P == 0).sum())
    pc = np.array([bin(i).count('1') for i in range(N)], dtype=np.int8) if N <= 1 << 22 else None
    degs = []
    for q in QS:
        a = modinv_vec(P % q, q)
        for i in range(n):
            a = a.reshape(-1, 2, 1 << i)
            a[:, 1, :] = (a[:, 1, :] - a[:, 0, :]) % q
            a = a.reshape(N)
        nz = a != 0
        d = int(pc[nz].max()); top = int((nz & (pc == d)).sum())
        degs.append((d, top, int(nz.sum())))
    return degs, 0
if __name__ == '__main__':
    k = int(sys.argv[1]); out = []
    for p in map(int, sys.argv[2:]):
        degs, nsol = ml_degree(k, p)
        rec = {'k': k, 'n_vars': 3 * k, 'p': p, 'box_solutions': nsol}
        if degs:
            rec.update(ml_degree=degs[0][0], ns_degree=degs[0][0] + 3, top_coeffs=degs[0][1], nonzero_coeffs=degs[0][2],
                       agree_two_primes=degs[0] == degs[1], monomials_total=1 << (3 * k))
        print(json.dumps(rec)); sys.stdout.flush()
