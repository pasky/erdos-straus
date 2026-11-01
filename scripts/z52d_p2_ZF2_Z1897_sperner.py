"""Z1897: Sperner labelling of the level x divisor grid.
Row C (1<=C<=K): sorted divisors d of N_C = 4Cp+1 at x = log d / log N_C in [0,1].
Label A: d = 1 (mod 4C);  B: d = -1 (mod 4C) [B = (*) certificate];  O: otherwise.
Consecutive rows are joined by the standard merge triangulation of the strip (sweep by x).
Checks: (i) each row's label word is a palindrome (involution d <-> N/d inverts the class);
(ii) boundary parity of {A,O} edges (left/right columns are all A; bottom/top rows);
(iii) number of fully labelled (A,B,O) triangles vs certificates present.
Usage: uv run --with sympy python ... pmax K"""
import sys, json, math
from sympy import divisors, primerange
def lab(d, q):
    r = d % q
    return 'A' if r == 1 % q else ('B' if r == q - 1 else 'O')
def row(p, C):
    N = 4*C*p + 1; q = 4*C
    ds = divisors(N)
    return [(math.log(d)/math.log(N), lab(d, q)) for d in ds]
def strip_tris(r0, r1):
    i = j = 0; tris = []
    while i < len(r0) - 1 or j < len(r1) - 1:
        if j == len(r1) - 1 or (i < len(r0) - 1 and r0[i+1][0] <= r1[j+1][0]):
            tris.append((r0[i][1], r0[i+1][1], r1[j][1])); i += 1
        else:
            tris.append((r0[i][1], r1[j][1], r1[j+1][1])); j += 1
    return tris
def ao_edges(r):
    return sum(1 for a, b in zip(r, r[1:]) if {a[1], b[1]} == {'A', 'O'})
if __name__ == '__main__':
    pmax, K = int(sys.argv[1]), int(sys.argv[2])
    stats = {'primes': 0, 'rows': 0, 'non_palindrome_rows': 0, 'odd_AO_boundary_parity': 0,
             'grids_with_full_tri': 0, 'grids_with_cert': 0, 'full_tri_without_cert': 0, 'full_tri_total_parity_odd': 0}
    for p in primerange(5, pmax):
        if p % 4 != 1: continue
        stats['primes'] += 1
        rows = [row(p, C) for C in range(1, K + 1)]
        for r in rows:
            stats['rows'] += 1
            w = [l for _, l in r]
            if w != w[::-1]: stats['non_palindrome_rows'] += 1
        par = (ao_edges(rows[0]) + ao_edges(rows[-1])) % 2
        stats['odd_AO_boundary_parity'] += par
        full = sum(1 for a, b in zip(rows, rows[1:]) for t in strip_tris(a, b) if set(t) == {'A', 'B', 'O'})
        cert = any(l == 'B' for r in rows for _, l in r)
        stats['grids_with_full_tri'] += full > 0; stats['grids_with_cert'] += cert
        stats['full_tri_without_cert'] += (full > 0 and not cert); stats['full_tri_total_parity_odd'] += full % 2
    print(json.dumps({'pmax': pmax, 'K': K, **stats}))
