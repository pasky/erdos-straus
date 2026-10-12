"""O159 §6: search for genuinely two-variable Type I ET families for n = Q(u,v).

For small polynomial levels c, d in Z[u,v], factor N = n^2 + 4c^2 d over Q (ET (2.9): N = f f',
f = 4acd - n, f' = 4bcd - n) and test every divisor f = kappa*f0 (kappa a rational constant fixed by
requiring 4cd | n + f in Q[u,v]).  For each polynomial solution, verify all ET Type I equations, test
whether the family is genuinely two-variable (not invariant under an infinite-order rational
Q-rotation, i.e. not in Q[n]^6), compute the positivity arc A_F of the top forms, the integrality
modulus K and whether F is integral on any square class mod lcm(8, K, 2|D|) (Theorem 3.2 predicts:
never when A_F is nonempty).

usage: bf_search_typeI.py QNAME CMODE DCOEF   (QNAME in {sum2, u2p2v2, u2puvpv2})
"""
import sys, itertools, math
from fractions import Fraction
import sympy as sp

u, v, kap = sp.symbols('u v kappa')
FORMS = {
    'sum2': (u**2 + v**2, -4, ((sp.Rational(3, 5), -sp.Rational(4, 5)), (sp.Rational(4, 5), sp.Rational(3, 5)))),
    # rotation from (1+2sqrt(-2))/3 acting on u + v sqrt(-2)
    # pipeline test only (one-variable O145 case, v is a dummy): must rediscover k=21, c=1, d=22
    'u2p21': (u**2 + 21, -84, ((1, 0), (0, 1))),
    'u2p2v2': (u**2 + 2*v**2, -8, ((sp.Rational(1, 3), -sp.Rational(4, 3)), (sp.Rational(2, 3), sp.Rational(1, 3)))),
}
qname = sys.argv[1] if len(sys.argv) > 1 else 'sum2'
cmode = sys.argv[2] if len(sys.argv) > 2 else 'lin'
dco = [int(x) for x in (sys.argv[3] if len(sys.argv) > 3 else '-1,0,1').split(',')]
Q, D, ROT = FORMS[qname]
(r11, r12), (r21, r22) = ROT
if qname != 'u2p21':
    assert sp.expand(Q.subs({u: r11*u + r12*v, v: r21*u + r22*v}, simultaneous=True) - Q) == 0

mons1 = [sp.Integer(1), u, v]
mons2 = mons1 + [u*u, u*v, v*v]


def polys(mons, rng):
    for cf in itertools.product(rng, repeat=len(mons)):
        p = sum(c*m for c, m in zip(cf, mons))
        if p != 0:
            yield sp.expand(p)


if cmode == 'const':
    CS = [sp.Integer(k) for k in (1, 2, 3)]
else:
    CS = [sp.Integer(k) for k in (1, 2)] + [p for p in polys(mons1, (-1, 0, 1, 2)) if sp.Poly(p, u, v).total_degree() == 1]
DS = list(polys(mons2, dco))


def divides(g, h):
    q, r = sp.div(sp.Poly(h, u, v, domain='QQ'), sp.Poly(g, u, v, domain='QQ'))
    return (q.as_expr() if r.is_zero else None)


def is_rot_invariant(G):
    return sp.expand(G.subs({u: r11*u + r12*v, v: r21*u + r22*v}, simultaneous=True) - G) == 0


def topform(G):
    P = sp.Poly(G, u, v)
    dg = P.total_degree()
    return sum(c*u**i*v**j for (i, j), c in P.terms() if i + j == dg)


def arc(F):
    tops = [sp.lambdify((u, v), topform(G)) for G in F]
    good = [t for t in range(720) if all(T(math.cos(t*math.pi/360), math.sin(t*math.pi/360)) > 1e-12 for T in tops)]
    return len(good)


def integrality(F):
    den = 1
    for G in F:
        for c in sp.Poly(G, u, v, domain='QQ').coeffs():
            den = math.lcm(den, int(sp.fraction(c)[1]))
    fs = [sp.lambdify((u, v), sp.expand(G*den)) for G in F]
    K = den
    M = math.lcm(8, K, 2*abs(D))
    if M > 1500:  # cost is M^2 Python evaluations; report as unchecked instead of hanging
        return K, M, 'skip', 'skip'
    qf = sp.lambdify((u, v), Q)
    sq = {(s*s) % M for s in range(M) if math.gcd(s, M) == 1}
    integral_cls, square_cls = 0, 0
    for a in range(M):
        for b in range(M):
            if math.gcd(int(qf(a, b)), M) != 1:
                continue
            if all(int(f(a, b)) % den == 0 for f in fs):
                integral_cls += 1
                if int(qf(a, b)) % M in sq:
                    square_cls += 1
    return K, M, integral_cls, square_cls


seen = set()
nfam = 0
out = []
for c in CS:
    for d in DS:
        N = sp.expand(Q**2 + 4*c**2*d)
        cst, facs = sp.factor_list(N)
        if len(facs) == 1 and facs[0][1] == 1:
            continue  # irreducible: only constant f, which is one-variable (Prop 5.1-type)
        for exps in itertools.product(*[range(m + 1) for _, m in facs]):
            f0 = sp.Integer(1)
            for (g, _), k in zip(facs, exps):
                f0 *= g**k
            f0 = sp.expand(f0)
            # need 4cd | Q + kap*f0 : coefficientwise linear in kap after division attempt
            degA = max(2, sp.Poly(f0, u, v).total_degree()) - sp.Poly(4*c*d, u, v).total_degree()
            if degA < 0:
                continue
            amons = [u**i*v**j for i in range(degA + 1) for j in range(degA + 1 - i)]
            acs = sp.symbols('a0:%d' % len(amons))
            A = sum(x*m for x, m in zip(acs, amons))
            eqs = sp.Poly(sp.expand(Q + kap*f0 - 4*c*d*A), u, v).coeffs()
            sol = sp.solve(eqs, list(acs), dict=True)  # kappa as a free parameter
            if not sol:
                sol = sp.solve(eqs, list(acs) + [kap], dict=True)
            cands = []
            for s in sol:
                if any(x not in s for x in acs):
                    continue
                if kap in s:
                    cands.append(s)
                else:  # kappa free (e.g. 4cd constant): try small rational kappa
                    dv = sp.divisors(int(abs(cst)) * 64)
                    for m in dv:
                        for n_ in dv:
                            for sg in (1, -1):
                                k0 = sp.Rational(sg*m, n_)
                                cands.append({**{x: s[x].subs(kap, k0) for x in acs}, kap: k0})
            for s in cands:
                if s[kap] == 0:
                    continue
                k = s[kap]
                f = sp.expand(k*f0)
                a = sp.expand(A.subs(s))
                if sp.expand(Q + f - 4*c*d*a) != 0:  # sympy may drop kappa-only conditions
                    continue
                fp = divides(f, N)
                if fp is None:
                    continue
                b = divides(4*c*d, sp.expand(Q + fp))
                if b is None:
                    continue
                e = divides(c, sp.expand(a + b))
                if e is None or a == 0 or b == 0 or e == 0:
                    continue
                F = [sp.expand(x) for x in (a, b, c, d, e, f)]
                chk = [4*F[0]*F[1]*F[3] - Q*F[4] - 1, F[2]*F[4] - F[0] - F[1], 4*F[0]*F[2]*F[3] - Q - F[5], F[4]*F[5] - 4*F[0]**2*F[3] - 1]
                assert all(sp.expand(x) == 0 for x in chk), F
                if qname != 'u2p21' and all(is_rot_invariant(G) for G in F):
                    continue  # one-variable (in Q[n])
                for sgn in (1, -1):  # dilation (a,b,c) -> -(a,b,c)
                    G6 = [sp.expand(sgn*F[0]), sp.expand(sgn*F[1]), sp.expand(sgn*F[2]), F[3], F[4], F[5]]
                    key = tuple(str(x) for x in G6)
                    if key in seen:
                        continue
                    seen.add(key)
                    na = arc(G6)
                    K, M, ic, sc = integrality(G6) if na > 0 else (None, None, None, None)
                    nfam += 1
                    line = f"F=(a,b,c,d,e,f)={G6}  arc={na}/720  K={K} M={M} integral_unit_classes={ic} square_classes={sc}"
                    out.append(line)
                    print(line, flush=True)
                    if na > 0 and isinstance(sc, int) and sc > 0:
                        print("!!! COUNTEREXAMPLE TO THEOREM 3.2 ???", flush=True)
print(f"# Q={Q} cmode={cmode} dcoef={dco}: |C|={len(CS)} |D|={len(DS)} genuinely-2var families found: {nfam}")
