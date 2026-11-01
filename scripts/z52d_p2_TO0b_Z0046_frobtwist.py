"""z52d pass2 TO0b Z0046: char-3 Frobenius-twist denominators. A = T over F_3, monic (H={1}) lemma-free existence test
(exists_general) for P = Q^3 + c (c in F_3) with Q monic of degree m in {1,2} (so deg P = 3m) and for the linear
families P = Q^3 with Q irreducible deg m. Compares failure counts with all irreducible P of the same degree."""
import sys
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_ff import exists_general, monic_irreducibles, str2poly, s2str, F
p = 3; A = str2poly('10'); f = F(p)
def cube(Q):
    return f.mul(Q, f.mul(Q, Q))
for m in (1, 2):
    tot = 0; fails_cube = 0; fails_cube_c = {0: 0, 1: 0, 2: 0}; tot_c = {0: 0, 1: 0, 2: 0}
    for Q in f.monics(m):
        P0 = cube(Q)
        if not exists_general(p, A, P0, H={1}):
            fails_cube += 1
        tot += 1
        for c in range(3):
            P = list(P0) + [0] * (max(0, 1 - len(P0)))
            P[0] = (P[0] + c) % p
            from z52d_p2_TO0b_ff import trim
            P = trim(P)
            if len(P) - 1 != 3 * m or P == A: continue
            tot_c[c] += 1
            if not exists_general(p, A, P, H={1}):
                fails_cube_c[c] += 1
    print(f'deg Q={m} (deg P={3*m}): Q^3 fails {fails_cube}/{tot}; Q^3+c fails by c={fails_cube_c} of {tot_c}', flush=True)
for n in (3, 6):
    Ps = monic_irreducibles(p, n)
    print(f'all irreducible P deg {n}: fails {sum(1 for P in Ps if not exists_general(p, A, P, H={1}))}/{len(Ps)}', flush=True)
