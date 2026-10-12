"""R159 independent search for Type I two-variable ET families, sliced by e (not by c,d as O159).
Type I: 4abd = n e + 1, c = (a+b)/e, f = 4acd - n.  For e = kappa*e0 we factor n e + 1 over Q,
distribute the irreducible factors among a, b, d (dilation fixes a's scalar), solve for b's scalar
so that e | a + b, and keep polynomial families; check all ET equations; flag those not in Q[n]^6."""
import sys, itertools
from fractions import Fraction
import sympy as sp
u, v, t = sp.symbols('u v t')
def eqs_ok(a,b,c,d,e,f,n):
    E = [4*a*b*d-(n*e+1), c*e-(a+b), 4*a*c*d-(n+f), e*f-(4*a*a*d+1), b*f-(n*a+c), n**2+4*c*c*d-f*(4*b*c*d-n)]
    return all(sp.expand(x) == 0 for x in E)
def in_Qn(F, n):
    # invariant under the rotation (3/5,-4/5;4/5,3/5) (for u^2+v^2) -- we instead test: each coordinate
    # equals a polynomial in n: substitute generic check via sympy reduce in terms of n (u->sqrt(n-v^2) trick avoided):
    # test invariance under the full orthogonal group of Q by two reflections/rotations
    # independent of O159's rotation test: g in Q[n] iff g(t,0) is even and g == h(n) with h(s) = g(sqrt s, 0)
    if n.free_symbols == {u}: return True  # control: one-variable form, trivially "one-variable"
    out = True
    for g in F:
        g0 = sp.Poly(sp.expand(g.subs(v, 0)), u)
        if any(m[0] % 2 for m in g0.monoms()): return False
        h = sum(cf*t**(m[0]//2) for m, cf in zip(g0.monoms(), g0.coeffs()))
        if sp.expand(h.subs(t, n) - g) != 0: return False
    return out
def search(n, e0s, kappas, tag):
    found = 0; tried = 0; feasible = 0; genuine = 0; printed = 0
    for e0 in e0s:
        for kap in kappas:
            e = kap*e0
            N = sp.expand(n*e + 1)
            cont, facs = sp.factor_list(N, u, v)
            irr = []
            for (g, m) in facs: irr += [g]*m
            if len(irr) < 2 and sp.Poly(irr[0], u, v).total_degree() == sp.Poly(N, u, v).total_degree() and True:
                pass
            tried += 1
            idx = range(len(irr))
            seen = set()
            for assign in itertools.product(range(3), repeat=len(irr)):
                key = tuple(sorted((assign[i], str(irr[i])) for i in idx))
                if key in seen: continue
                seen.add(key)
                A0 = sp.Mul(*[irr[i] for i in idx if assign[i]==0])
                B0 = sp.Mul(*[irr[i] for i in idx if assign[i]==1])
                D0 = sp.Mul(*[irr[i] for i in idx if assign[i]==2])
                beta = sp.Symbol('beta')
                # need e0 | A0 + beta*B0 in Q[u,v]: remainder by Groebner/division w.r.t. e0
                q, r = sp.reduced(sp.expand(A0 + beta*B0), [e0], u, v)
                rp = sp.Poly(r, u, v)
                sols = sp.solve(rp.coeffs(), beta, dict=True) if rp.coeffs() else [{}]
                for s in sols:
                    if beta not in s: continue
                    bt = s[beta]
                    if bt == 0: continue
                    a = A0; b = bt*B0; d = sp.expand(cont*D0/(4*bt)) ; 
                    c = sp.cancel((a+b)/e)
                    if not c.is_polynomial(u, v): continue
                    f = sp.expand(4*a*c*d - n)
                    if not eqs_ok(a,b,c,d,e,f,n): print("EQ FAIL", e, a, b, d); continue
                    F = [sp.expand(x) for x in (a,b,c,d,e,f)]
                    if any(x == 0 for x in F): continue
                    found += 1
                    fa, fb, fc, fd = [sp.lambdify((u, v), x) for x in (a, b, c, d)]
                    feas = any(fa(x,y)*fb(x,y)*fd(x,y) > 0 and fa(x,y)*fc(x,y)*fd(x,y) > 0 and fb(x,y)*fc(x,y)*fd(x,y) > 0
                               for x in range(-25, 26, 3) for y in range(-25, 26, 3))
                    if not feas: continue
                    feasible += 1
                    one = in_Qn(F, n)
                    if not one or tag == 'control':
                        if not one: genuine += 1
                        if printed < 20: printed += 1; print(f"[{tag}] family: e={e} a={a} b={sp.factor(b)} c={c} d={d} f={sp.factor(f)} inQ[n]={one}", flush=True)
    print(f"[{tag}] (e0,kappa) pairs tried {tried}, formal families {found}, sign-feasible {feasible}, sign-feasible and NOT in Q[n]^6: {genuine}", flush=True)
if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'control':
        ROT = [[1,0],[0,-1]]  # v is a dummy; any v-reflection fixes u^2+21
        search(u**2+21, [u**2+22], [sp.Rational(1,22)], 'control')
    else:
        ROT = [[sp.Rational(3,5), sp.Rational(-4,5)], [sp.Rational(4,5), sp.Rational(3,5)]]
        n = u**2 + v**2
        lin = [x for x in (al*u+be*v for al in (-1,0,1) for be in (-1,0,1)) if x != 0]
        quad = [al*u**2+be*u*v+ga*v**2 for al in (-1,0,1) for be in (-1,0,1) for ga in (-1,0,1)]
        e0s = set()
        consts = range(int(sys.argv[2]), int(sys.argv[3]))
        for z in consts:
            for L in lin + [0]:
                for Qd in quad:
                    x = sp.expand(Qd + L + z)
                    if sp.Poly(x, u, v).total_degree() >= 1: e0s.add(x)
        kappas = [sp.Rational(1, k) for k in range(1, 13)] + [sp.Integer(2), sp.Integer(3)]
        search(n, sorted(e0s, key=str), kappas, mode)
