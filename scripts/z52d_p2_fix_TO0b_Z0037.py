"""z52d pass2 fix, TO0b Z0037: Int(Z)-denominators for the hard class n = 4t+1.
Search: 4/(4t+1) = 1/X + 1/Y + 1/Z with X,Y,Z in Q[t], each integer-valued at integers (Int(Z)), and positive for t >= 1.
X ranges over c0 + c1 t + c2 binom(t,2) (small integers).  Residual R = 4/n - 1/X = N/D (reduced).  Then 1/Y+1/Z = N/D
has polynomial solutions Y = (D+d)/N, Z = (D + D^2/d)/N for divisors d of D^2 (times constants) with N | (D+d), N | (D+D^2/d).
Rule: check exactly, integer-valuedness on -3..12, positivity on t = 1..30."""
import itertools
import sympy as sp
from sympy import QQ, Poly
t = sp.symbols('t')
T = lambda e: Poly(e, t, domain=QQ)
def integer_valued(P):
    return all(sp.Rational(P.eval(k)).q == 1 for k in range(-3, 13))
def positive(P):
    return all(P.eval(k) > 0 for k in range(1, 31))
cands = []
for c0, c1, c2 in itertools.product(range(-3, 9), range(-3, 9), range(-2, 5)):
    X = T(c0 + c1 * t + c2 * t * (t - 1) / 2)
    if X.is_zero: continue
    if positive(X) and integer_valued(X):
        cands.append(X)
print('candidate X:', len(cands), flush=True)
import sys
R_ = int(sys.argv[1]) if len(sys.argv) > 1 else 1
n = T(4 * t + R_)
consts = [QQ(1), QQ(-1), QQ(2), QQ(-2), QQ(3), QQ(-3), QQ(1, 2), QQ(-1, 2), QQ(1, 3), QQ(-1, 3), QQ(4), QQ(-4), QQ(1, 4), QQ(-1, 4)]
hits = []; checked = 0
for X in cands:
    num = 4 * X - n          # 4/n - 1/X = num/(n X)
    den = n * X
    g = num.gcd(den)
    N = num.quo(g); D = den.quo(g)
    if N.is_zero: continue
    lcN = N.LC(); N = N * (1 / lcN); D = D * (1 / lcN)   # keep N/D unchanged
    checked += 1
    _, facs = D.factor_list()
    base = [f for f, m in facs]; mult = [m for f, m in facs]
    found = None
    for exps in itertools.product(*[range(0, 2 * m + 1) for m in mult]):
        d = T(1)
        for f, e in zip(base, exps):
            d = d * f ** e
        D2 = D * D
        Dq2, r0 = D2.div(d)
        if not r0.is_zero: continue
        for c in consts:
            dd = d * c
            # Y = (D + dd)/N, Z = (D + D^2/dd)/N
            q1, r1 = (D + dd).div(N)
            Zn = D + Dq2 * (1 / c)
            q2, r2 = Zn.div(N)
            if not (r1.is_zero and r2.is_zero): continue
            Y, Z = q1, q2
            if Y.is_zero or Z.is_zero: continue
            if integer_valued(Y) and integer_valued(Z) and positive(Y) and positive(Z):
                # exact identity check: 1/X + 1/Y + 1/Z = 4/n as rational functions
                lhs = sp.together(1 / sp.sympify(X.as_expr()) + 1 / sp.sympify(Y.as_expr()) + 1 / sp.sympify(Z.as_expr()) - sp.Rational(4) / (4 * t + R_))
                if sp.simplify(lhs) == 0:
                    found = (X.as_expr(), sp.factor(Y.as_expr()), sp.factor(Z.as_expr())); break
        if found: break
    if found:
        hits.append(found)
        if len(hits) >= 6: break
print('residual cases with N != 0 checked:', checked)
print('Int(Z)-valued, positive identities found:', len(hits))
for h in hits: print('  X,Y,Z =', h)
