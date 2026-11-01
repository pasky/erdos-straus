"""z52d pass2 fix, TO0b Z0086: exact check of a Lemma-3.1 route for D=3 (N(eps)=+1), eps = 2+sqrt3.
eta = eps^5 = 362+209 sqrt3 (eta = -1 mod 11 O_K), kappa = (1+eta)/11 = 33+19 sqrt3, totally positive,
u = kappa/eta, v = kappa, e = 1/u+1/v = 11. For every rational n = 1 mod 4 with x = (n+11)/4:
4/n = 1/x + 1/(u n x) + 1/(v n x) in Q(sqrt3). Exact arithmetic on pairs (a,b) = a + b sqrt3 with Fractions."""
from fractions import Fraction as Fr
class Q3:
    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a+o.a, s.b+o.b)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a-o.a, s.b-o.b)
    def __mul__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a*o.a+3*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__ = __mul__
    def conj(s): return Q3(s.a, -s.b)
    def norm(s): return s.a*s.a-3*s.b*s.b
    def inv(s): c = s.conj(); n = s.norm(); return Q3(c.a/n, c.b/n)
    def __truediv__(s, o): o = o if isinstance(o, Q3) else Q3(o); return s * o.inv()
    def __eq__(s, o): o = o if isinstance(o, Q3) else Q3(o); return s.a == o.a and s.b == o.b
    def __repr__(s): return f'{s.a} + {s.b}*sqrt3'
    def tot_pos(s): return s.a > 0 and (s.a*s.a - 3*s.b*s.b) > 0 and s.a + s.b*0 > 0 and (s.conj().a + 0 > 0 and (s.a - s.b*0) > 0) and (s.a - 0) and True
    def sign_pair(s):
        # total positivity: value and conjugate value both > 0 (floats fine for sign with exact rationals below)
        import math
        v = Fr(s.a) + Fr(s.b) * 0
        r3 = math.sqrt(3)
        return (float(s.a) + float(s.b) * r3, float(s.a) - float(s.b) * r3)
eps = Q3(2, 1); eta = Q3(1)
for _ in range(5): eta = eta * eps
print('eta = eps^5 =', eta)
one = Q3(1)
kappa = (one + eta) / Q3(11)
print('kappa = (1+eta)/11 =', kappa, ' integral coords:', kappa.a.denominator == 1 and kappa.b.denominator == 1)
print('kappa totally positive:', kappa.sign_pair(), ' eta totally positive:', eta.sign_pair())
u = kappa / eta; v = kappa
print('1/u + 1/v == 11 :', (one / u + one / v) == Q3(11))
ok = True
for n in [5, 9, 13, 17, 21, 101, 1001]:
    x = Fr(n + 11, 4)
    X = Q3(x); N = Q3(n)
    lhs = Q3(Fr(4, n))
    rhs = one / X + one / (u * N * X) + one / (v * N * X)
    good = (lhs == rhs)
    ok &= good
    print(f'n={n}: x={x}, identity 4/n = 1/x + 1/(u n x) + 1/(v n x) holds: {good}; u,v totally positive: {u.sign_pair()[0] > 0 and u.sign_pair()[1] > 0} {v.sign_pair()}')
print('ALL OK:', ok)
