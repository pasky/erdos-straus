"""Z2815: braid (mutation) action on weighted semiorthogonal Gram matrices and its invariant, vs S_{n,D}: nA^2+B^2+D = ABC.

Lattice with bilinear form chi, semiorthogonal basis (e1,e2,e3): chi(e_j,e_i) = 0 for j > i, chi(e_i,e_i) = d_i.
Left mutation of the adjacent pair (e_i, e_{i+1}):  (e_i, e_{i+1}) -> (e_{i+1} - (chi(e_i,e_{i+1})/d_i) e_i, e_i)
(Bondal's formula for exceptional objects, d_i = 1; for d_i != 1 it is the rational/lattice version, integral iff
d_i | chi(e_i, e_{i+1})).  Any basis change is a congruence G -> P G P^T, so the pencil polynomial
det(G^T + s G) / det(P)^2 is invariant; we compute it and every mutation explicitly.
"""
import sympy as sp

a, b, c, s = sp.symbols('a b c s')
d1, d2, d3, n, A, B, C, D = sp.symbols('d1 d2 d3 n A B C D')


def gram(d, x, y, z):
    return sp.Matrix([[d[0], x, y], [0, d[1], z], [0, 0, d[2]]])


def mutate(G, i):
    """left mutation at positions (i, i+1); returns new Gram matrix and change-of-basis matrix P (rows = new basis)."""
    m = G.shape[0]
    P = sp.eye(m)
    di = G[i, i]
    coef = G[i, i + 1] / di
    # new basis: f_i = e_{i+1} - coef e_i, f_{i+1} = e_i, others unchanged
    P[i, :] = sp.zeros(1, m); P[i, i + 1] = 1; P[i, i] = -coef
    P[i + 1, :] = sp.zeros(1, m); P[i + 1, i] = 1
    Gn = sp.simplify(P * G * P.T)
    return Gn, P


def main():
    G = gram((d1, d2, d3), a, b, c)
    pencil = sp.factor(sp.expand((G.T + s * G).det()))
    print("det(G^T + s G) =", sp.collect(sp.expand((G.T + s * G).det()), s))
    # coefficient of s (and s^2) carries the quadratic-cubic invariant
    co = sp.Poly(sp.expand((G.T + s * G).det()), s).all_coeffs()
    print("coefficients (s^3..s^0):", [sp.factor(x) for x in co])
    inv = sp.expand(co[1])   # s^2 coefficient
    print("s^2 coefficient:", inv)
    # semiorthogonality and invariance under the two mutations, generic weights
    for i in (0, 1):
        Gn, P = mutate(G, i)
        lower = [sp.simplify(Gn[r, q]) for r in range(3) for q in range(r)]
        print(f"mutation sigma_{i+1}: lower-triangular entries after mutation = {lower}; new diag = {[Gn[k,k] for k in range(3)]}")
        newinv = sp.Poly(sp.expand((Gn.T + s * Gn).det()), s).all_coeffs()
        print("   pencil coefficients unchanged:", [sp.simplify(x - y) for x, y in zip(newinv, co)],
              " new (a,b,c) =", (sp.simplify(Gn[0, 1]), sp.simplify(Gn[0, 2]), sp.simplify(Gn[1, 2])))
    # braid relation sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 on Gram matrices (generic)
    G121 = mutate(mutate(mutate(G, 0)[0], 1)[0], 0)[0]
    G212 = mutate(mutate(mutate(G, 1)[0], 0)[0], 1)[0]
    print("braid relation holds on Gram:", sp.simplify(G121 - G212) == sp.zeros(3, 3))
    # (i) the item's proposal d = (1, n, 1)
    I1 = sp.factor(inv.subs({d1: 1, d2: n, d3: 1}))
    print("\n[item proposal d=(1,n,1)] invariant s^2-coeff:", I1)
    # (ii) which diagonal reproduces n A^2 + B^2 - ABC (no C^2 term)?
    print("general s^2-coefficient: d1 d2 d3 * (3 terms) ->", sp.expand(inv))
    sol = sp.expand(inv.subs({d1: 0, d2: 1, d3: n}))
    print("[d=(0,1,n)] s^2-coeff:", sol, " with (a,b,c)=(C,B?,A?)")
    # dictionary search: map (a,b,c) to signed permutations of (A,B,C) and match -(nA^2+B^2-ABC) up to scalar
    target = n * A ** 2 + B ** 2 - A * B * C
    import itertools
    hits = []
    for dd in itertools.product([0, 1, n], repeat=3):
        e = sp.expand(inv.subs({d1: dd[0], d2: dd[1], d3: dd[2]}))
        for perm in itertools.permutations((A, B, C)):
            for sg in itertools.product((1, -1), repeat=3):
                ee = sp.expand(e.subs({a: sg[0] * perm[0], b: sg[1] * perm[1], c: sg[2] * perm[2]}, simultaneous=True))
                for lam in (1, -1):
                    if sp.expand(ee - lam * target) == 0:
                        hits.append((dd, perm, sg, lam))
    print("diagonals/dictionaries giving exactly +-(nA^2+B^2-ABC):", hits)
    # (iii) on d = (0,1,n) [or the hit], which mutations are defined, and what do they do?
    for dd, perm, sg, lam in hits[:1]:
        Gs = gram(dd, a, b, c)
        print("\nGram", Gs.tolist(), "det =", Gs.det())
        for i in (0, 1):
            if Gs[i, i] == 0:
                print(f" sigma_{i+1}: undefined (divides by chi(e_{i+1},e_{i+1}) = 0)")
                continue
            Gn, P = mutate(Gs, i)
            print(f" sigma_{i+1}: new diag {[Gn[k,k] for k in range(3)]}, new (a,b,c) = {(sp.simplify(Gn[0,1]), sp.simplify(Gn[0,2]), sp.simplify(Gn[1,2]))}")
    # (iv) right/left inverse mutations through e3 (weight n) e.g. sigma_2^{-1}
    print("\nVieta involutions of S_{n,D}: A -> BC/n - A (needs n | BC), B -> AC - B; C fixed (MARKOFF_ES Prop 2.1).")


if __name__ == '__main__':
    main()


# ---- integral orbit exploration (appended): all integral left/right mutations on integer weighted Gram matrices ----
def int_mutations(state):
    """state = (d1,d2,d3,a,b,c) with G = [[d1,a,b],[0,d2,c],[0,0,d3]]; yields integral mutated states."""
    from fractions import Fraction
    d = list(state[:3]); a_, b_, c_ = state[3:]
    G = [[d[0], a_, b_], [0, d[1], c_], [0, 0, d[2]]]
    out = []
    for i in (0, 1):
        x = G[i][i + 1]
        for kind in ('L', 'R'):
            piv = G[i][i] if kind == 'L' else G[i + 1][i + 1]
            if piv == 0 or x % piv:
                continue
            q = x // piv
            # rows of P: new basis in terms of old
            P = [[1 if r == k else 0 for k in range(3)] for r in range(3)]
            if kind == 'L':   # (e_i, e_{i+1}) -> (e_{i+1} - q e_i, e_i)
                P[i] = [0] * 3; P[i][i + 1] = 1; P[i][i] = -q
                P[i + 1] = [0] * 3; P[i + 1][i] = 1
            else:             # (e_i, e_{i+1}) -> (e_{i+1}, e_i - q e_{i+1})
                P[i] = [0] * 3; P[i][i + 1] = 1
                P[i + 1] = [0] * 3; P[i + 1][i] = 1; P[i + 1][i + 1] = -q
            M = [[sum(P[r][k] * G[k][l] for k in range(3)) for l in range(3)] for r in range(3)]
            Gn = [[sum(M[r][l] * P[t][l] for l in range(3)) for t in range(3)] for r in range(3)]
            assert Gn[1][0] == Gn[2][0] == Gn[2][1] == 0
            out.append((Gn[0][0], Gn[1][1], Gn[2][2], Gn[0][1], Gn[0][2], Gn[1][2]))
    return out


def orbit(start, cap):
    seen = {start}; todo = [start]
    while todo:
        s0 = todo.pop()
        for t in int_mutations(s0):
            if max(abs(x) for x in t[3:]) <= cap and t not in seen:
                seen.add(t); todo.append(t)
    return seen


def vieta_orbit(n_, A_, B_, C_, cap):
    seen = {(A_, B_, C_)}; todo = [(A_, B_, C_)]
    while todo:
        A0, B0, C0 = todo.pop()
        nxt = [(A0, A0 * C0 - B0, C0), (-A0, B0, -C0), (A0, -B0, -C0), (-A0, -B0, C0)]
        if (B0 * C0) % n_ == 0:
            nxt.append((B0 * C0 // n_ - A0, B0, C0))
        for t in nxt:
            if max(map(abs, t)) <= cap and t not in seen:
                seen.add(t); todo.append(t)
    return seen


def orbit_test():
    import json
    res = []
    for (n_, A_, B_, D_) in [(17, 2, 1, 3), (13, 4, 3, 3), (29, 4, 1, 15), (5, 2, 1, 3), (41, 2, 3, 7)]:
        if (n_ * A_ * A_ + B_ * B_ + D_) % (A_ * B_):
            continue
        C_ = (n_ * A_ * A_ + B_ * B_ + D_) // (A_ * B_)
        cap = 10 ** 6
        orb = orbit((0, 1, n_, A_, B_, C_), cap)
        frame = {(s_[3], s_[4], s_[5]) for s_ in orb if s_[:3] == (0, 1, n_)}
        vo = vieta_orbit(n_, A_, B_, C_, cap)
        Cvals = sorted({abs(s_[5]) for s_ in orb if s_[:3] == (0, 1, n_)})
        diag = sorted({s_[:3] for s_ in orb})
        res.append(dict(n=n_, start=(A_, B_, C_, D_), states=len(orb), diagonals=diag, frame_points=len(frame),
                        vieta_points=len(vo), frame_subset_vieta=frame <= vo, vieta_subset_frame=vo <= frame,
                        abs_C_values_in_frame=Cvals[:10]))
    print(json.dumps(res, indent=1))


orbit_test()
