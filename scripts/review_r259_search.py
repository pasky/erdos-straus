"""R259 from-scratch brute-force search for polynomial Type I / Type II ET families
over several forms P (written independently of scripts/z20_*).

Type I : 4ABCD = P(A+B) + C   <=>  C(4ABD - 1) = P(A+B)
Type II: 4ABCD = A + B + C P  <=>  C(4ABD - P) = A + B
Enumerate A <= B (index order), D over a candidate set S, solve for C by exact
division, classify: in Q[P] (all four coordinates) or not; for non-collapsing
families look for a valid point (a,b,c same sign, d > 0, n > 0, integers) in a box.

Usage: PYTHONPATH=scripts uv run --with python-flint python scripts/review_r259_search.py <name> [I|II]
"""
import itertools, sys
from fractions import Fraction as Fr
import flint

def ctx(names):
    return flint.fmpq_mpoly_ctx.get(tuple(names), 'deglex')

def top(F):
    d = F.total_degree()
    terms = {m: c for m, c in zip(F.monoms(), F.coeffs()) if sum(m) == d}
    return F.context().from_dict(terms), d

def in_QP(F, P):
    """True iff F in Q[P] (P non-constant). Greedy top-part peeling."""
    k = P.total_degree()
    Ptop, _ = top(P)
    while not F.is_constant():
        Ft, d = top(F)
        if d % k:
            return False
        j = d // k
        PjT = Ptop ** j
        # Ft must be c * PjT
        m0, c0 = PjT.monoms()[0], PjT.coeffs()[0]
        c = Ft.coefficient(Ft.monoms().index(m0)) / c0 if m0 in Ft.monoms() else None
        if c is None or Ft != c * PjT:
            return False
        F = F - c * P ** j
    return True

def candidates(R, P, consts, lincoef, kappas, extra=()):
    g = R.gens()
    S = []
    for c0 in consts:
        for ls in itertools.product(lincoef, repeat=len(g)):
            for ka in kappas:
                f = R.from_dict({}) + c0
                for co, x in zip(ls, g):
                    f = f + co * x
                f = f + ka * P
                if not f.is_zero():
                    S.append(f)
    S.extend(extra)
    # dedupe
    seen, out = set(), []
    for f in S:
        key = str(f)
        if key not in seen:
            seen.add(key); out.append(f)
    return out

def search(R, P, S, typ):
    fams = []
    for i, A in enumerate(S):
        for B in S[i:]:
            if (A + B).is_zero():
                continue
            AB4 = 4 * A * B
            for D in S:
                E = AB4 * D - (1 if typ == 'I' else P)
                if E.is_zero():
                    continue
                num = P * (A + B) if typ == 'I' else A + B
                q, r = divmod(num, E)
                if r.is_zero() and not q.is_zero():
                    fams.append((A, B, q, D))
    return fams

def check_identity(P, A, B, C, D, typ):
    lhs = 4 * A * B * C * D
    rhs = P * (A + B) + C if typ == 'I' else A + B + C * P
    return lhs == rhs

def evalq(F, pt):
    v = F(*[flint.fmpq(x) for x in pt])
    return Fr(int(v.p), int(v.q))

def find_valid2(R, P, fam, box=6):
    nv = len(R.gens())
    for pt in itertools.product(range(-box, box + 1), repeat=nv):
        n = evalq(P, pt)
        if n <= 0:
            continue
        a, b, c, d = (evalq(F, pt) for F in fam)
        if any(x.denominator != 1 for x in (a, b, c, d)):
            continue
        if d > 0 and ((a > 0 and b > 0 and c > 0) or (a < 0 and b < 0 and c < 0)):
            return pt, (n, a, b, c, d)
    return None

def is_degenerate(P, f, typ):
    """The never-valid families named in NORMFORM_CUBIC: Type I (Thm 3.1): A+B = 0, or
    (up to A<->B) B = b const, D = -1/(4b^2), C = -bP.  Type II (Remark in SPARKS7): A+B = 0."""
    A, B, C, D = f
    if (A + B).is_zero():
        return True
    if typ == 'II':
        return False
    for X, Y in ((A, B), (B, A)):
        if Y.is_constant():
            b = Y.leading_coefficient()
            if D == D.context().from_dict({}) - 1 / (4 * b * b) and C == -b * P:
                return True
    return False

def forms():
    out = {}
    R = ctx('uv'); u, v = R.gens()
    out['cubic_u3+2v3'] = (R, u**3 + 2 * v**3)
    out['quad_u2+v2'] = (R, u**2 + v**2)
    out['quad_u2-2v2-1'] = (R, u**2 - 2 * v**2 - 1)   # non-homog, P* irreducible
    out['ctrl_4u2-4v2-1'] = (R, 4 * u**2 - 4 * v**2 - 1)  # P irreducible, P* reducible, units mod P
    out['ctrl_4uv-u-1'] = (R, 4 * u * v - u - 1)         # P irreducible, P* reducible
    out['edge_v+u2'] = (R, v + u**2)                    # P* = u^2 reducible, no units mod P
    out['red_uv'] = (R, u * v)                          # reducible positive control
    R3 = ctx('uvw'); a, b, c = R3.gens()
    out['norm3_cbrt2'] = (R3, a**3 + 2 * b**3 + 4 * c**3 - 6 * a * b * c)
    out['quad3_u2+v2+w2'] = (R3, a**2 + b**2 + c**2)
    return out

if __name__ == '__main__':
    name = sys.argv[1]; typs = sys.argv[2:] or ['I', 'II']
    R, P = forms()[name]
    big = len(R.gens()) == 2
    raw = [1, -1, 2, -2, Fr(1, 2), Fr(1, 4), Fr(-1, 4), 0] if big else [1, -1, 2, Fr(1, 4), 0]
    consts = [flint.fmpq(Fr(x).numerator, Fr(x).denominator) for x in raw]
    S = candidates(R, P, consts, [-1, 0, 1], [0, 1, -1] if big else [0, 1])
    print(name, 'P =', P, '|S| =', len(S), flush=True)
    for typ in typs:
        fams = search(R, P, S, typ)
        assert all(check_identity(P, *f, typ) for f in fams)
        bad = [f for f in fams if not all(in_QP(F, P) for F in f)]
        degen = [f for f in bad if is_degenerate(P, f, typ)]
        nondeg = [f for f in bad if f not in degen]
        print(f' Type {typ}: {len(fams)} families, {len(fams) - len(bad)} in Q[P], {len(degen)} degenerate (never-valid list), {len(nondeg)} other non-Q[P]')
        nvalid = sum(1 for f in nondeg if find_valid2(R, P, f, 4)) if len(R.gens()) == 2 else 'n/a'
        print(f'   non-collapsing families with a valid point in [-4,4]^2: {nvalid}')
        shown = 0
        for f in nondeg:
            val = find_valid2(R, P, f, 4)
            if shown < 4 or val:
                print('   non-collapsing:', [str(x) for x in f], 'valid at', val)
                shown += 1
            if shown >= 6:
                break
