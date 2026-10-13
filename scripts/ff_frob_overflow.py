"""FROBENIUS_FIRING (O196) §5: the overflow scale ES_q^{(s,e)} between ES_q (e = 0) and the mute variant (e = oo).
ES_q^{(s,e)}(A,P): A/P = 1/X + 1/Y + 1/z, X, Y monic in F_q[T], z monic rational with denominator s^{2t}, t <= e, NC.
Per-modulus enumeration: f = A m - 1 (m monic), firing set {-A a^2 d s^{2j} : a d | m, j <= v_s(m/(ad)) + e}.
Each hit is turned into an explicit solution (generalised FF_MUTE Prop 2.1: Q = a s^j,
E = (P + A Q^2 d)/f, X = (P+E)/A, Y = P m, z = P X m/(Q^2 d)) and VERIFIED exactly (identity, monic, NC, z-denominator
= s^{2t}, t <= e).  Reports, per irreducible P of degree n, the least overflow e that is achieved with modulus degree <= D.
usage: ff_frob_overflow.py q A s n D emax
"""
import sys
from sympy import Poly, symbols
from fm_poly import Fp, parse, show

Tsym = symbols('T')
q = int(sys.argv[1]); F = Fp(q)
A = parse(sys.argv[2]); s = parse(sys.argv[3]); n = int(sys.argv[4]); D = int(sys.argv[5]); emax = int(sys.argv[6])
k = len(A) - 1


def fac(m):
    if len(m) == 1:
        return []
    P = Poly(list(reversed(m)), Tsym, modulus=q)
    out = []
    for g, e in P.factor_list()[1]:
        c = [int(x) % q for x in g.monic().all_coeffs()]
        out.append((F.trim(list(reversed(c))), e))
    return out


def pw(a, e):
    r = (1,)
    for _ in range(e):
        r = F.mul(r, a)
    return r


def lc_ratio_one(num, den):
    return num[-1] * pow(den[-1], q - 2, q) % q == 1


def verify(P, f, m, a, d, j, e):
    Q2d = F.mul(pw(F.mul(a, pw(s, j)), 2), d)
    N = F.add(P, F.mul(A, Q2d))
    E, r = F.divmod(N, f)
    if r or not E:
        return False
    X, r = F.divmod(F.add(P, E), A)
    if r or not X or X[-1] != 1:
        return False
    Y = F.mul(P, m)
    num = F.mul(F.mul(P, X), m); den = Q2d
    g = F.gcd(num, den)
    num, _ = F.divmod(num, g); den, _ = F.divmod(den, g)
    c = den[-1]; ci = pow(c, q - 2, q)
    num = F.scal(ci, num); den = F.scal(ci, den)
    if num[-1] != 1:
        return False
    t2 = F.val(den, s)
    if den != pw(s, t2) or t2 % 2 or t2 // 2 > e:
        return False
    lhs = F.mul(F.mul(F.mul(A, X), Y), num)
    rhs = F.mul(P, F.add(F.add(F.mul(Y, num), F.mul(X, num)), F.mul(den, F.mul(X, Y))))
    if lhs != rhs:
        return False
    return min(len(X) - 1, len(Y) - 1, len(num) - len(den)) >= n - k


SQ = len(sys.argv) > 7 and sys.argv[7] == 'sq'  # T1 control: P = M^2, M irreducible of degree n/2
Ps = ([F.mul(M, M) for M in F.irreducibles(n // 2) if F.mod(A, M) and F.mod(s, M)] if SQ
      else [P for P in F.irreducibles(n) if F.mod(A, P) and P != s])
best = {P: None for P in Ps}
for dd in range(k, D + 1):
    for m in F.monics(dd - k):
        f = F.sub(F.mul(A, m), (1,))
        sf = not F.mod(f, s)  # s | f: only j = 0
        fs = fac(m)
        # enumerate (a, d) with a d | m
        opts = [((1,), (1,), (1,))]  # (a, d, m/(ad))
        for g, E in fs:
            new = []
            for (a, d, rest) in opts:
                for al in range(E + 1):
                    for de in range(E - al + 1):
                        new.append((F.mul(a, pw(g, al)), F.mul(d, pw(g, de)), F.mul(rest, pw(g, E - al - de))))
            opts = new
        table = {}
        for a, d, rest in opts:
            sig = F.val(rest, s) if len(s) > 1 else 0
            for j in range(0, 1 if sf else sig + emax + 1):
                ov = max(0, j - sig)
                w = F.mod(F.neg(F.mul(A, F.mul(pw(F.mul(a, pw(s, j)), 2), d))), f)
                if w not in table or table[w][0] > ov:
                    table[w] = (ov, a, d, j)
        for P in Ps:
            r = F.mod(P, f)
            if r in table:
                ov, a, d, j = table[r]
                if best[P] is None or ov < best[P]:
                    if verify(P, f, m, a, d, j, ov):
                        best[P] = ov
hist = {}
for P, v in best.items():
    hist[v] = hist.get(v, 0) + 1
unsolved0 = [f"{show(P)}:{v}" for P, v in best.items() if v != 0]
print(f"{'SQUARES ' if SQ else ''}q={q} A={show(A)} s={show(s)} n={n} D={D} emax={emax}: #P={len(Ps)} least-overflow histogram "
      f"{dict(sorted(hist.items(), key=lambda t: (t[0] is None, t[0] or 0)))}  (None = unsolved)")
print("  P with no e=0 (Type II ES_q) hit, as P:least-e:", ' '.join(unsolved0))
