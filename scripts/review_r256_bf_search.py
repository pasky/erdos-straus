"""R256 from-scratch brute-force search for polynomial Type I / Type II ET families over a binary quadratic form Q.

Type II:  4ABCD = A + B + C*Q      (x, y, z) = (ABD, ACDn, BCDn)
Type I :  4ABCD = Q*(A + B) + C    (x, y, z) = (ABDn, ACD, BCD)

Solve the identity for one coordinate (exact polynomial division over QQ via python-flint) and
classify each polynomial family found: (i) all four in QQ[Q]?  (ii) valid at an integer point
(Type II) / positive on an open arc of directions (Type I)?  Irreducible Q should give only QQ[Q]
families among the valid ones (Thm 1.1/1.2 of SYNTHESIS_SPARKS7); reducible Q is a positive control.

usage: review_r256_bf_search.py QNAME MODE
"""
import itertools, math, sys
import flint

R = flint.fmpq_mpoly_ctx.get(('u', 'v'))
u, v = R.gens()
one = R.from_dict({(0, 0): 1})
QS = {
    'sum2': u*u + v*v, 'eis': u*u + u*v + v*v, 'pell2': u*u - 2*v*v, 'u2p5v2': u*u + 5*v*v,
    'uv': u*v, 'diffsq': u*u - v*v, 'usq': u*u, 'uupv': u*u + u*v,
}
MON1 = [one, u, v]
MON2 = [one, u, v, u*u, u*v, v*v]


def polys(mons, coeffs):
    out = []
    for cs in itertools.product(coeffs, repeat=len(mons)):
        if any(cs):
            out.append(sum((c*m for c, m in zip(cs, mons)), R.from_dict({})))
    return out


S1 = polys(MON1, [-1, 0, 1, 2])
S2 = polys(MON2, [-1, 0, 1])


def todict(p):
    return {tuple(int(t) for t in e): c for e, c in zip(p.monoms(), p.coeffs())}


def tdeg(p):
    return max((sum(e) for e in p.monoms()), default=-1)


def in_QQ_of(g, Q):
    g = R.from_dict(todict(g))
    for _ in range(10):
        d = tdeg(g)
        if d <= 0:
            return True
        if d % 2:
            return False
        Qk = Q**(d//2)
        gd, qd = todict(g), todict(Qk)
        top = [m for m in gd if sum(m) == d]
        m = top[0]
        if qd.get(m, 0) == 0:
            return False
        g2 = g - (gd[m]/qd[m]) * Qk
        if tdeg(g2) >= d:
            return False
        g = g2
    return False


def ev(p, a, b):
    return sum((c * a**e[0] * b**e[1] for e, c in todict(p).items()), flint.fmpq(0))


def top_ev(p, x, y):
    d = tdeg(p)
    return sum(float(c) * x**e[0] * y**e[1] for e, c in todict(p).items() if sum(e) == d)


def integral_valid_point(fam, Q, box=12):
    for a in range(-box, box+1):
        for b in range(-box, box+1):
            n = ev(Q, a, b)
            if n <= 0:
                continue
            vals = [ev(p, a, b) for p in fam]
            if any(x.q != 1 for x in vals):
                continue
            A, B, C, D = [int(x.p) for x in vals]
            if D > 0 and ((A > 0 and B > 0 and C > 0) or (A < 0 and B < 0 and C < 0)):
                return (a, b, n, A, B, C, D)
    return None


def positive_arc(fam, Q, N=720):
    for k in range(N):
        t = 2*math.pi*(k+0.5)/N
        x, y = math.cos(t), math.sin(t)
        if top_ev(Q, x, y) <= 1e-9:
            continue
        T = [top_ev(p, x, y) for p in fam]
        if T[3] > 1e-9 and (all(z > 1e-9 for z in T[:3]) or all(z < -1e-9 for z in T[:3])):
            return round(t, 3)
    return None


def check(typ, fam, Q):
    A, B, C, D = fam
    lhs = 4*A*B*C*D
    rhs = (A + B + C*Q) if typ == 'II' else (Q*(A + B) + C)
    assert lhs == rhs


def run(qname, mode):
    Q = QS[qname]
    found = {}
    def record(typ, fam):
        if any(tdeg(p) < 0 for p in fam):
            return
        check(typ, fam, Q)
        key = (typ,) + tuple(str(p) for p in fam)
        if key in found:
            return
        inq = all(in_QQ_of(p, Q) for p in fam)
        found[key] = (inq, fam)
    if mode == 'IIA':   # A = (B + CQ)/(4BCD - 1), B,C in S1, D in S2
        for B in S1:
            for C in S1:
                num = B + C*Q
                for D in S2:
                    den = 4*B*C*D - 1
                    q, r = divmod(num, den)
                    if r == 0:
                        record('II', (q, B, C, D))
    elif mode == 'IID':  # D = (A + B + CQ)/(4ABC), A in S2, B, C in S1
        for B in S1:
            for C in S1:
                for A in S2:
                    q, r = divmod(A + B + C*Q, 4*A*B*C)
                    if r == 0:
                        record('II', (A, B, C, q))
    elif mode == 'IA':   # A = (QB + C)/(4BCD - Q)
        for B in S1:
            for D in S1:
                for C in S2:
                    den = 4*B*C*D - Q
                    if den == 0:
                        continue
                    q, r = divmod(Q*B + C, den)
                    if r == 0:
                        record('I', (q, B, C, D))
        for C in S1:
            for D in S1:
                for B in S2:
                    den = 4*B*C*D - Q
                    if den == 0:
                        continue
                    q, r = divmod(Q*B + C, den)
                    if r == 0:
                        record('I', (q, B, C, D))
    elif mode == 'ID':   # D = (Q(A+B) + C)/(4ABC), A,B in S1, C in S2
        for i, A in enumerate(S1):
            for B in S1[i:]:
                for C in S2:
                    q, r = divmod(Q*(A + B) + C, 4*A*B*C)
                    if r == 0:
                        record('I', (A, B, C, q))
    nq = [k for k, (inq, _) in found.items() if not inq]
    print(f'Q={qname} mode={mode}: families={len(found)}  in QQ[Q]={len(found)-len(nq)}  outside={len(nq)}')
    nvalid_out = 0
    for k in nq:
        fam = found[k][1]
        ip = integral_valid_point(fam, Q)
        arc = positive_arc(fam, Q) if k[0] == 'I' else None
        rpos = None
        if k[0] == 'II':
            # any real/rational point with valid sign pattern
            for a in range(-12, 13):
                for b in range(-12, 13):
                    vals = [ev(p, a, b) for p in fam]
                    if ev(Q, a, b) > 0 and vals[3] > 0 and (all(x > 0 for x in vals[:3]) or all(x < 0 for x in vals[:3])):
                        rpos = (a, b)
                        break
                if rpos:
                    break
        valid = (ip is not None or rpos is not None) if k[0] == 'II' else (arc is not None)
        nvalid_out += valid
        if valid or len(nq) <= 6:
            print('  OUTSIDE', k, 'int-valid-pt', ip, 'pos-pt', rpos, 'pos-arc', arc)
    print(f'  outside & valid-in-theorem-sense: {nvalid_out}')


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
