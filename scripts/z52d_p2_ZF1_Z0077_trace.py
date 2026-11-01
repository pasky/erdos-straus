# Z0077: Tr_{K/Q}(1/x) = 4/p with x totally positive in O_K, K cyclic cubic of small conductor.
# Tr(1/x) = s2(x)/N(x), so the condition is p*s2(x) = 4*N(x).
# (1) totally positive units u with 4 | Tr(1/u): then x = p*(Tr(1/u)/4)*u solves it for EVERY p (and every n).
# (2) box search over x = a + b*th + c*th^2, |a|,|b|,|c| <= B: all solutions with 4N/s2 = p prime <= 10^4.
import numpy as np, sys, json, itertools
from sympy import isprime, Matrix, discriminant, symbols, Poly
X = symbols('X')
FIELDS = {7: [1, 1, -2, -1], 9: [1, 0, -3, 1], 13: [1, 1, -4, 1], 19: [1, 1, -6, -7]}
B = int(sys.argv[1]) if len(sys.argv) > 1 else 40
out = {}
for f, co in FIELDS.items():
    disc = discriminant(Poly(co, X)); 
    # companion matrix of theta (monic): mult-by-theta in basis 1, th, th^2
    c2, c1, c0 = co[1], co[2], co[3]
    M = np.array([[0, 0, -c0], [1, 0, -c1], [0, 1, -c2]], dtype=object)
    I = np.eye(3, dtype=object).astype(object)
    M2 = M.dot(M)
    roots = np.roots(co).real
    def charpoly(a, b, c):
        A = a * I + b * M + c * M2
        tr = A.trace(); tr2 = A.dot(A).trace(); s2 = (tr * tr - tr2) // 2
        det = Matrix(A.tolist()).det()
        return tr, s2, det
    # (1) units: generated (with -1) by two fundamental units; take th and th+1 type candidates: search small elements of norm +-1
    units = []
    rng = range(-4, 5)
    for a, b, c in itertools.product(rng, rng, rng):
        if (a, b, c) == (0, 0, 0): continue
        tr, s2, det = charpoly(a, b, c)
        if abs(det) == 1: units.append((a, b, c))
    # totally positive units among products u = e1^i e2^j (squares are totally positive); test Tr(u^-1) mod 4 directly on
    # all totally positive units found in a larger box
    tp_units = []
    rng = range(-12, 13)
    hits = []
    for a, b, c in itertools.product(rng, rng, rng):
        conj = a + b * roots + c * roots**2
        if not (conj > 0).all(): continue
        tr, s2, det = charpoly(a, b, c)
        if det == 1:
            # Tr(u^-1) = s2(u)/N(u) = s2
            tp_units.append(((a, b, c), int(s2)))
            if s2 % 4 == 0: hits.append(((a, b, c), int(s2)))
    # (2) box search, vectorised numerically then exact check
    rngB = np.arange(-B, B + 1)
    A_, B_, C_ = np.meshgrid(rngB, rngB, rngB, indexing='ij')
    A_, B_, C_ = A_.ravel(), B_.ravel(), C_.ravel()
    conj = A_[:, None] + B_[:, None] * roots[None, :] + C_[:, None] * roots[None, :]**2
    pos = (conj > 1e-9).all(axis=1)
    sols = []
    for a, b, c in zip(A_[pos], B_[pos], C_[pos]):
        tr, s2, N = charpoly(int(a), int(b), int(c))
        if s2 > 0 and (4 * N) % s2 == 0:
            p = (4 * N) // s2
            if p <= 10**4 and isprime(p):
                g = np.gcd.reduce([int(a), int(b), int(c)])
                tr1, s21, N1 = charpoly(int(a) // g, int(b) // g, int(c) // g)
                sols.append(dict(x=[int(a), int(b), int(c)], p=int(p), N=int(N), content=int(g), unit_times_int=bool(abs(N1) == 1)))
    ps = sorted(set(s['p'] for s in sols))
    nonunit = sorted(set(s['p'] for s in sols if not s['unit_times_int']))
    out[f] = dict(poly=co, disc=int(disc), n_tp_units_in_box=len(tp_units), tp_units_with_4_div_Tr_inv=hits[:10],
                  n_tp_units_4div=len(hits), box=B, n_pos=int(pos.sum()), n_solutions=len(sols), primes_hit=ps,
                  primes_hit_by_non_unit_multiple=nonunit, sample=[s for s in sols if not s['unit_times_int']][:10])
    print(f"conductor {f}: disc {disc}; tot.pos. units in box {len(tp_units)}, with 4|Tr(1/u): {len(hits)} e.g. {hits[:3]}; "
          f"box B={B}: {int(pos.sum())} tot.pos. x, {len(sols)} solutions, primes hit {len(ps)}: {ps[:30]}; "
          f"primes hit by x not (integer)*(unit): {nonunit[:30]}")
json.dump(out, open('data/z52b/pass2/ZF1/Z0077/trace_results.json', 'w'), indent=1)
