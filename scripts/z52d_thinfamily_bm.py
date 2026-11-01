# z52d_thinfamily_bm.py — calibration for lane THINFAMILY (Z52D_THINFAMILY.md §1):
# (a) Berlekamp–Massey over Q on the ACTUAL proof certificates of 3*2^s+1 (paper Thm 4.1 + Prop 2.1 cubic family) and
#     63*2^s+1 (paper Lemma 4.3 + Table 2), per rule and per valid residue class of the rule's parameter t;
#     the recurrence found is checked against the predicted characteristic polynomial prod_j (X - 2^{omega T j}) and
#     used to predict 10 further terms exactly.
# (b) the same on MINIMAL certificates (least x, then least y) of 3*2^s+1, s <= SMIN, per class s mod 2, 3, 4.
# Usage: PYTHONPATH=scripts uv run --with sympy --with cypari2 python scripts/z52d_thinfamily_bm.py [SMIN]
import sys
from fractions import Fraction as Fr
from math import gcd
sys.argv = [sys.argv[0]] + sys.argv[1:]
SMIN = int(sys.argv[1]) if len(sys.argv) > 1 else 60
import c1_expfam_verify as V
from sympy import Poly, symbols, expand, cancel
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)

def bm(seq):
    """Berlekamp–Massey over Q. Returns connection polynomial C (list, C[0] = 1) and linear complexity L:
    sum_{i=0}^{L} C[i] a[n-i] = 0 for all n >= L."""
    a = [Fr(x) for x in seq]
    C, B = [Fr(1)], [Fr(1)]; L, m, b = 0, 1, Fr(1)
    for n in range(len(a)):
        d = a[n] + sum(C[i] * a[n - i] for i in range(1, L + 1))
        if d == 0:
            m += 1; continue
        T = C[:]; coef = d / b
        C = C + [Fr(0)] * (len(B) + m - len(C))
        for i in range(len(B)): C[i + m] -= coef * B[i]
        if 2 * L <= n:
            L, B, b, m = n + 1 - L, T, d, 1
        else:
            m += 1
    return C[:L + 1] + [Fr(0)] * (L + 1 - len(C[:L + 1])), L

def predict(C, L, a, extra):
    a = [Fr(x) for x in a]
    for _ in range(extra):
        a.append(-sum(C[i] * a[-i] for i in range(1, L + 1)))
    return a

X = symbols('X')
def charpoly_ok(C, L, roots):
    """C(X) = 1 + C1 X + ... ; its reciprocal X^L + C1 X^{L-1} + ... must equal prod (X - r)."""
    P = Poly(sum(C[i] * X ** (L - i) for i in range(L + 1)), X)
    Q = Poly(1, X)
    for r in roots: Q = Q * Poly(X - r, X)
    return P == Q

def calib(fam, K=24, EXTRA=10):
    rows = []
    for rule in fam.rules:
        A = V.analyse(fam, rule)
        om, T = rule['omega'], A['T']
        degs = [Poly(cancel(expand(R)), V.Y).monoms() for R in rule['xyz']]
        for v in A['V']:
            t0 = A['tstar'] + ((v - A['tstar']) % T)
            ts = [t0 + T * k for k in range(K + EXTRA)]
            vals = [V.eval_rule(rule, A, t) for t in ts]
            assert all(s is not None for s in vals)
            res = []
            for ci in range(3):
                seq = [s[ci] for s in vals]
                C, L = bm(seq[:K])
                ok_pred = predict(C, L, seq[:K], EXTRA) == [Fr(z) for z in seq]
                roots = [Fr(2) ** (om * T * e[0]) for e in degs[ci]]     # monomials Y^e of the coordinate
                ok_cp = (L == len(roots)) and charpoly_ok(C, L, roots)
                res.append((L, ok_pred, ok_cp))
            rows.append((rule['label'], rule['s0'], rule['sigma'], om, T, v, res))
            print('%-34s s=%d+%d*t, Y=2^(%d t), t = %d mod %d: (L, predicts, charpoly=prod(X-2^{%dTe})) = %s'
                  % (rule['label'][:34], rule['s0'], rule['sigma'], om, v, T, om, res), flush=True)
    return rows

def cubic3():
    """EXP_OPEN Prop 2.1: s = 0, 12 mod 36, s >= 36, Y = 2^{s/3}: a = 80, c = 1, d = (21Y+64)/320, b = (Y^2-3Y+9)/7."""
    F = V.Fam('3*2^s+1 cubic', 3, 2, 1)
    Y = V.Y; n = 3 * Y ** 3 + 1; a, c = 80, 1; d = (21 * Y + 64) / 320; b = (Y ** 2 - 3 * Y + 9) / 7
    F.add('II-ac (a,c)=(80,1), Y=2^(s/3)', 0, 3, 1, a * b * d, a * c * d * n, b * c * d * n, extra=[b, d])
    return F

def min_cert(n, xmax_extra=20000):
    """least x, then least y, solution of 4/n = 1/x+1/y+1/z (window lemma (a), exhaustive in divisors)."""
    for x in range(n // 4 + 1, n // 4 + 1 + xmax_extra):
        m, N = 4 * x - n, n * x
        g = gcd(m, N); m2, N2 = m // g, N // g
        ds = [int(t) for t in pari.divisors(N2)]
        S = {}
        for d in ds: S.setdefault(d % m2, []).append(d)
        best = None
        for d1 in ds:
            for d2 in S.get((-d1) % m2, []):
                y = N2 * (d1 + d2) // (m2 * d2); z = N2 * (d1 + d2) // (m2 * d1)
                if y >= x and z >= y and (best is None or y < best[1]): best = (x, y, z)
        if best:
            xx, yy, zz = best; assert 4 * xx * yy * zz == n * (xx * yy + yy * zz + zz * xx)
            return best
    return None

if __name__ == '__main__':
    print('=== (a) actual certificates: 3*2^s+1 (Thm 4.1) ===')
    calib(V.fam_proth3())
    print('=== (a) actual certificates: 3*2^s+1 cubic moving-gap family (EXP_OPEN Prop 2.1) ===')
    calib(cubic3())
    print('=== (a) actual certificates: 63*2^s+1 (Thm 4.4) ===')
    calib(V.fam_63())
    print('=== (b) minimal certificates of 3*2^s+1, s = 1..%d ===' % SMIN)
    mc = {}
    for s in range(1, SMIN + 1):
        n = 3 * 2 ** s + 1; mc[s] = min_cert(n)
        print('s=%d n=%d min cert (x, y, z) = %s gap m=%d' % (s, n, mc[s], 4 * mc[s][0] - n), flush=True)
    for (mod, smin) in ((2, 1), (3, 1), (4, 1), (12, 1), (2, 14), (4, 14)):
        for r in range(mod):
            ss = [s for s in range(smin, SMIN + 1) if s % mod == r]
            for name, idx in (('x', 0), ('y', 1), ('gap', None)):
                seq = [(4 * mc[s][0] - (3 * 2 ** s + 1)) if idx is None else mc[s][idx] for s in ss]
                C, L = bm(seq)
                print('min-cert class s=%d mod %d, s>=%d (%d terms) coord %-3s: linear complexity L = %d (a genuine recurrence '
                      'needs L << len/2)' % (r, mod, smin, len(seq), name, L), flush=True)
