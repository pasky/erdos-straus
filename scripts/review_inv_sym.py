"""R158 from-scratch checks for INVOLUTION_ES §4 (Prop 4.2, Lemma 4.3, Remark 4.5).

(1) Prop 4.2(a),(b),(c): after the unique-factorisation step (top-degree part forces monomial linear part),
    solve F∘g = mu*F over all coordinate permutations with unknown scalars lam_i, translations beta_i,
    n symbolic (a,b: coefficients may depend on n), resp. n-independent (c: require identity for two n values).
(2) Prop 4.2(d) for X: FULL affine g in (A,B,t) (12 unknowns), n-independent, with (A'B'-1)*t == (AB-1)*t'.
(3) Lemma 4.3(i) brute force: pairs x, (alpha A, B/alpha, t) in the integral set => t | r - s.
(4) Remark 4.5 brute force: u_k(A,B,t) = (A, B+kn, t+kA), x and u_k(x) both in the integral set => t=1 or u=1.
"""
import itertools
import sympy as sp
from sympy import divisors

n = sp.symbols('n')  # (nonzero=True makes sympy.solve miss solutions)


def classify(vars_, F, nindep=False):
    d = len(vars_)
    lam = sp.symbols('l0:%d' % d); bet = sp.symbols('b0:%d' % d); mu = sp.symbols('mu')
    sols_all = []
    for perm in itertools.permutations(range(d)):
        sub = {vars_[i]: lam[i] * vars_[perm[i]] + bet[i] for i in range(d)}
        G = sp.expand(F.xreplace(sub) - mu * F)
        if nindep:
            eqs = []
            for nv in (5, 13):
                eqs += sp.Poly(G.subs(n, nv), *vars_).coeffs()
        else:
            eqs = sp.Poly(G, *vars_).coeffs()
        sols = sp.solve(eqs, list(lam) + list(bet) + [mu], dict=True)
        for s in sols:
            if all(s.get(l, l) != 0 for l in lam):
                sols_all.append((perm, s))
    return sols_all


def part1():
    x, y, z = sp.symbols('x y z')
    Fa = sp.Rational(4) / n * x * y * z - (x * y + y * z + z * x)
    print("(a) ES coords:")
    for perm, s in classify([x, y, z], Fa):
        print("  ", perm, s)
    t, u, v = sp.symbols('t u v')
    Fb = t * u * v - u - v - n
    print("(b) O152 (t,u,v) [Groebner; sympy.solve misses the solutions here]:")
    lam = sp.symbols('l0:3'); bet = sp.symbols('b0:3'); mu, w = sp.symbols('mu w'); V = [t, u, v]
    for perm in itertools.permutations(range(3)):
        sub = {V[i]: lam[i] * V[perm[i]] + bet[i] for i in range(3)}
        eqs = sp.Poly(sp.expand(Fb.xreplace(sub) - mu * Fb), *V).coeffs() + [w * lam[0] * lam[1] * lam[2] * n - 1]
        print("  ", perm, list(sp.groebner(eqs, *lam, *bet, mu, w, n, order='lex')))
    a, b, c, k = sp.symbols('a b c k')
    Fc = 4 * a * b * c * k - a - b - n * k
    print("(c) Type II (a,b,c,k), n-independent:")
    for perm, s in classify([a, b, c, k], Fc, nindep=True):
        print("  ", perm, s)


def part2():
    A, B, t = sp.symbols('A B t')
    co = sp.symbols('c0:12')
    Ap = co[0] * A + co[1] * B + co[2] * t + co[3]
    Bp = co[4] * A + co[5] * B + co[6] * t + co[7]
    tp = co[8] * A + co[9] * B + co[10] * t + co[11]
    G = sp.expand((Ap * Bp - 1) * t - (A * B - 1) * tp)
    sols = sp.solve(sp.Poly(G, A, B, t).coeffs(), co, dict=True)
    print("(d) full affine maps preserving (AB-1)/t (n-independent):")
    for s in sols:
        g = [sp.simplify(e.xreplace(s)) for e in (Ap, Bp, tp)]
        print("  ", g)


def integral_X(n_, maxt=None):
    pts = []
    for t_ in range(1, n_ + 3):
        N = t_ * n_ + 1
        for A_ in divisors(N):
            B_ = N // A_
            if (A_ + 1) % t_ == 0 and (B_ + 1) % t_ == 0:
                pts.append((A_, B_, t_))
    return pts


def in_X(A_, B_, t_):
    return t_ >= 1 and A_ >= 1 and B_ >= 1 and (A_ + 1) % t_ == 0 and (B_ + 1) % t_ == 0


def part34(NMAX=400):
    from fractions import Fraction
    bad3 = bad4 = used4 = 0
    alphas = [Fraction(r, s) for r in range(1, 8) for s in range(1, 8) if sp.gcd(r, s) == 1 and r != s]
    for n_ in range(1, NMAX + 1):
        pts = integral_X(n_)
        for (A_, B_, t_) in pts:
            for al in alphas:
                A2 = al * A_; B2 = Fraction(B_) / al
                if A2.denominator == 1 and B2.denominator == 1 and in_X(int(A2), int(B2), t_):
                    if (al.numerator - al.denominator) % t_:
                        bad3 += 1
            for k in list(range(-6, 0)) + list(range(1, 7)):
                y = (A_, B_ + k * n_, t_ + k * A_)
                if in_X(*y):
                    used4 += 1
                    u_ = (A_ + 1) // t_
                    if not (t_ == 1 or u_ == 1):
                        bad4 += 1
    print("Lemma 4.3(i) violations up to n=%d:" % NMAX, bad3)
    print("Remark 4.5: unipotent moves found", used4, "; violations (t!=1 and u!=1):", bad4)


if __name__ == "__main__":
    part1(); part2(); part34()
