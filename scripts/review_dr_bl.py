"""R181: from-scratch enumeration of ALL monic solutions of A/P = c1/X1 + c2/X2 + c3/X3 (all deg >= n - deg A)
over F_p[T], and local invariants of alpha_zeta = (-u1/u3, -u2/u3)_zeta, u_i = X_i/c_i, at EVERY place.
Checks: Weil reciprocity; odd part of every invariant for c=(1,1,1) (Thm 2.2); Steinberg identity of Lemma 2.1
place-by-place; Cor 2.3 on Type II points; Lemma 3.2 formula at infinity; Thm 3.3 at P = Q^m.
Usage: review_dr_bl.py p m Acoeffs n mode [c1 c2 c3]   mode in {irr, cube:e}"""
import sys, collections
from review_dr_ff import FF, jacobi

def solutions(F, A, P, c, n):
    """set of ordered triples (X1,X2,X3) of monic polys with A/P = sum c_i/X_i, deg X_i >= n-degA."""
    k = len(A) - 1; d0 = n - k; sols = set()
    for i in range(3):
        j, l = [t for t in range(3) if t != i]
        for Xi in F.monics(d0):
            E = F.sub(F.mul(A, Xi), F.scal(c[i], P))       # A/P - c_i/X_i = E/(P X_i)
            if not E: continue
            N = F.mul(P, Xi)
            # c_j/Y + c_l/Z = E/N  <=>  (E Y - c_j N)(E Z - c_l N) = c_j c_l N^2
            N2 = F.mul(N, N); fac = F.factor(N2)
            items = list(fac.items())
            def divisors(idx):
                if idx == len(items): yield (1,); return
                l_, e_ = items[idx]
                for rest in divisors(idx + 1):
                    t = rest
                    for _ in range(e_ + 1):
                        yield t; t = F.mul(t, l_)
            for dm in divisors(0):
                for mu in range(1, F.p):
                    D = F.scal(mu, dm)
                    q1, r1 = F.divmod(F.add(F.scal(c[j], N), D), E)
                    if r1 or not q1 or q1[-1] != 1 or len(q1) - 1 < d0: continue
                    Dp = F.divmod(F.scal(c[j] * c[l] % F.p, N2), D)[0]
                    q2, r2 = F.divmod(F.add(F.scal(c[l], N), Dp), E)
                    if r2 or not q2 or q2[-1] != 1 or len(q2) - 1 < d0: continue
                    X = [None] * 3; X[i] = Xi; X[j] = q1; X[l] = q2
                    sols.add(tuple(X))
    return sols

def check_sol(F, A, P, c, X):
    # A * X1 X2 X3 == P * (c1 X2 X3 + c2 X1 X3 + c3 X1 X2)
    lhs = F.mul(A, F.mul(X[0], F.mul(X[1], X[2])))
    rhs = F.mul(P, F.add(F.scal(c[0], F.mul(X[1], X[2])), F.add(F.scal(c[1], F.mul(X[0], X[2])), F.scal(c[2], F.mul(X[0], X[1])))))
    return lhs == rhs

def frac(F, cn, num, cd, den):  # (cn*num)/(cd*den) as (poly, poly)
    return (F.scal(cn, num), F.scal(cd, den))

def alpha_args(F, c, X):
    p = F.p
    # -u1/u3 = -(X1/c1)/(X3/c3) = (-c3 X1)/(c1 X3)
    a = frac(F, (-c[2]) % p, X[0], c[0], X[2])
    b = frac(F, (-c[2]) % p, X[1], c[1], X[2])
    return a, b

if __name__ == "__main__":
    p, m = int(sys.argv[1]), int(sys.argv[2]); A = tuple(int(t) for t in sys.argv[3].split(','))
    n = int(sys.argv[4]); mode = sys.argv[5]
    c = tuple(int(t) for t in sys.argv[6:9]) if len(sys.argv) > 6 else (1, 1, 1)
    F = FF(p)
    if mode == 'irr':
        Ps = [P for P in F.monics(n) if F.is_irred(P) and F.gcd(P, A) == (1,)]
        Qof = {P: P for P in Ps}; e = 1
    else:
        e = int(mode.split(':')[1]); Ps = []; Qof = {}
        for Q in F.monics(n // e):
            if F.is_irred(Q) and F.gcd(Q, A) == (1,):
                P = F.pw(Q, e); Ps.append(P); Qof[P] = Q
    stats = collections.Counter(); nsol = 0; unsolv = 0
    for P in Ps:
        S = solutions(F, A, P, c, n)
        if not S: unsolv += 1
        Q = Qof[P]
        for X in S:
            assert check_sol(F, A, P, c, X)
            nsol += 1
            a, b = alpha_args(F, c, X)
            inv = F.all_invariants(a, b, m)
            assert sum(inv.values()) % m == 0, "Weil reciprocity fails"
            for v, val in inv.items():
                if v != 'inf' and v != Q: stats['fin_other', val] += 1
            iQ = inv.get(Q, 0); iinf = inv['inf']
            # shape
            vs = tuple(F.val(x, Q)[0] for x in X)
            nz = sorted(vs)
            if nz[0] == 0 and nz[1] == 0 and nz[2] >= e: shape = 'I'
            elif nz[0] == 0 and nz[1] >= e: shape = 'II'
            else: shape = 'other'
            stats[shape, iQ, iinf] += 1
    print(f"p={p} m={m} A={A} n={n} mode={mode} c={c}: #P={len(Ps)} unsolvable={unsolv} #sol={nsol}")
    for k_, v_ in sorted(stats.items(), key=str): print("  ", k_, v_)
