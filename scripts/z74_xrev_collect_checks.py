"""z74 Opus cross-review (lane COLLECT): independent finite/algebraic checks.

Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_collect_checks.py

Each check recomputes a finite or symbolic claim of the reviewed notes from scratch (it does not import
or reuse the authors' scripts).  Memory use is tiny (polynomials of degree <= 24, residues mod q <= 199).
"""
from fractions import Fraction as Fr
from itertools import product

import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


# ---------------------------------------------------------------- LOGIC_COLLECTION §3 (conic tower)
w, z, X, Y, T, s, t, u, W, a = sp.symbols('w z X Y T s t u W a')
r2 = sp.sqrt(2)
S_ = (w + 1/w)/2
T_ = (w - 1/w)/(2*r2)
check('conic s^2-2t^2=1', sp.simplify(S_**2 - 2*T_**2 - 1) == 0)
check('s+sqrt2 t = w', sp.simplify(S_ + r2*T_ - w) == 0)
check('s-sqrt2 t = 1/w', sp.simplify(S_ - r2*T_ - 1/w) == 0)
p_z = (3*(z + 1/z)/2 + 1)/4
check('p(z) = (3z^2+2z+3)/(8z)', sp.simplify(p_z - (3*z**2 + 2*z + 3)/(8*z)) == 0)
check('e(p)=p(1)=1', p_z.subs(z, 1) == 1)
m2 = sp.sqrt(-2)
check('(1+sqrt-2)^2 = -1+2sqrt-2', sp.expand((1 + m2)**2) == -1 + 2*m2)
check('N(1+sqrt-2)=3', sp.expand((1 + m2)*(1 - m2)) == 3)
alpha = (-1 + 2*m2)/3
check('alpha root of 3X^2+2X+3', sp.simplify(3*alpha**2 + 2*alpha + 3) == 0)
check('alpha*conj(alpha)=1', sp.simplify(alpha*(-1 - 2*m2)/3) == 1)
check('alpha=(1+sqrt-2)/(1-sqrt-2)', sp.simplify(alpha - (1 + m2)/(1 - m2)) == 0)
for m in range(1, 13):
    f = 3*w**(2*m) + 2*w**m + 3
    fac = sp.factor_list(f, extension=r2)[1]
    check(f'3w^{2*m}+2w^{m}+3 irreducible over Q(sqrt2)', len(fac) == 1 and fac[0][1] == 1)

# ---------------------------------------------------------------- LOGIC_NORM_SPLIT / Z73_NORM_STAGE_CHECK
check('x^2+y^2 irreducible over Q', len(sp.factor_list(X**2 + Y**2)[1]) == 1)
check('x^2+y^2 splits over Q(i)', len(sp.factor_list(X**2 + Y**2, extension=sp.I)[1]) == 2)
for k in range(1, 6):
    f = 1 + T**(2**k)
    check(f'1+T^{2**k} irreducible over Q', len(sp.factor_list(f)[1]) == 1)
    g = sp.factor_list(f, extension=sp.I)[1]
    check(f'1+T^{2**k} = two conjugate factors over Q(i)', len(g) == 2)
    check(f'1+T^{2**k} = (T^{2**(k-1)}+i)(T^{2**(k-1)}-i)',
          sp.expand((T**(2**(k-1)) + sp.I)*(T**(2**(k-1)) - sp.I) - f) == 0)
# Bertrand variant: q-a = 1+2a^(3/4)tau+a^(1/2)tau^2 for Y = sqrt(a)+a^(1/4) tau
L, tau = sp.symbols('L tau', positive=True)
q_minus_a = sp.expand(1 + (L**2 + L*tau)**2 - L**4)
check('q-a = 1+2L^3 tau+L^2 tau^2 (L=a^(1/4))', sp.expand(q_minus_a - (1 + 2*L**3*tau + L**2*tau**2)) == 0)
# for tau<2: q-a < 1+4L^3+4L^2 < 5L^3 once L>5 (an infinite L certainly qualifies)
check('1+4L^3+4L^2 < 5L^3 for L=6', 1 + 4*6**3 + 4*6**2 < 5*6**3)
# square-root-scale obstruction: Y=b+j gives e(1+Y^2)=1+(1+j)^2 >= 2 when e(b)=1
check('e(1+(b+j)^2)=1+(1+j)^2>=2', all(1 + (1 + j)**2 >= 2 for j in range(50)))
# Z73_NORM_STAGE_CHECK singular point of F W - q, q=(s^2+1)^2+t^2+u^2
q = (s**2 + 1)**2 + t**2 + u**2
G = (X**2 + Y**2)*W - q
pt = {s: sp.I, t: 0, u: 0, X: 0, Y: 0, W: 0}
check('(i,0,0,0,0,0) on FW=q', sp.simplify(G.subs(pt)) == 0)
check('all partials of FW-q vanish there',
      all(sp.simplify(sp.diff(G, v).subs(pt)) == 0 for v in (s, t, u, X, Y, W)))
check('q irreducible over Q(i)', len(sp.factor_list(q, extension=sp.I)[1]) == 1)
check('q(0)=1', q.subs({s: 0, t: 0, u: 0}) == 1)
# saturation/boundedness example from the audit: X^2/H = 1/(1+tau^2) at X=T, Y=T tau
check('X^2/H at (T,T tau) = 1/(1+tau^2)', sp.simplify((T**2/(T**2 + (T*tau)**2)) - 1/(1 + tau**2)) == 0)
# equal-scale counterexample (Z73_NORM_STAGE_CHECK): hY-kX = hT eps when k=c h, Y/X=c+eps
# repair row FU+XWV=1: at real points F=0 forces X=Y=0 hence XW=0 (no real point over F=0)

# ---------------------------------------------------------------- Z73_ES_ROW_DESCENT §1 failure tests
check('1+1/T+1/(-T)=1', sp.simplify(1 + 1/T + 1/(-T) - 1) == 0)
check('1/(T^2+2)+(T^2+1)/(T^2+2)=1', sp.simplify(1/(T**2 + 2) + (T**2 + 1)/(T**2 + 2) - 1) == 0)
check('1/(1+T)+1/(1+1/T)=1', sp.simplify(1/(1 + T) + 1/(1 + 1/T) - 1) == 0)
d = sp.symbols('d')
check('1/(d+1)+d/(d+1)=1', sp.simplify(1/(d + 1) + d/(d + 1) - 1) == 0)
# ---------------------------------------------------------------- LOGIC_MARKED_SECTIONS failure example
# every integer y has a prime l | y^2+3, so (1,y) lies on W=V(P-1,y^2+3) mod l
check('y^2+3 has a prime factor for |y|<=10^4', all(len(sp.factorint(y*y + 3)) >= 1 for y in range(0, 10001)))
# local conditions: y=0 avoids W mod l for l!=3; y=1 avoids W mod 3
check('y=0: 3 unit mod l!=3', all(3 % l for l in sp.primerange(2, 200) if l != 3))
check('y=1: 4 unit mod 3', 4 % 3 != 0)

# ---------------------------------------------------------------- Z73_ADELIC_ROW_AUDIT stress test (independent)
# P = 1 mod q.  Dirichlet Q=1+Y must be a unit; row1 (P-1)U + Y(Y-1)V = 1 needs integral (U,V);
# row2 (P-1)W' + (V-1)X' = 1 needs integral (W',X').  Brute force over ALL residues of (Y,U,V,W',X')
# modulo q for q <= 13 (P-1 = 0 mod q, so U, W' are free), and the reduced count up to 199.
def feasible_full(q):
    first, second = set(), set()
    for Yv in range(q):
        if (1 + Yv) % q == 0:
            continue
        for V in range(q):
            if (Yv*(Yv - 1)*V - 1) % q == 0:
                first.add(Yv)
                if any(((V - 1)*Xv - 1) % q == 0 for Xv in range(q)):
                    second.add(Yv)
    return first, second


bad1, bad2 = [], []
for qq in sp.primerange(2, 200):
    f1, f2 = feasible_full(qq)
    if not f1:
        bad1.append(qq)
    if not f2:
        bad2.append(qq)
    if qq == 5:
        check('q=5: row1 allows Y in {2,3}, row2 only Y=2', f1 == {2, 3} and f2 == {2})
check('row prefixes infeasible exactly at q in {2,3} (q<200)', bad1 == [2, 3] and bad2 == [2, 3])
# CRT example: 2(8/15)+3(-1/45)=1 corrected by one rational tau to an integral identity
u0, v0 = Fr(8, 15), Fr(-1, 45)
check('2u+3v=1', 2*u0 + 3*v0 == 1)
found = None
for num in range(-2000, 2001):
    tau_ = Fr(num, 45)
    U_, V_ = u0 + 3*tau_, v0 - 2*tau_
    if U_.denominator == 1 and V_.denominator == 1:
        found = (tau_, U_, V_)
        break
check('one rational tau makes (u+3tau, v-2tau) integral', found is not None and 2*found[1] + 3*found[2] == 1)

# ---------------------------------------------------------------- ES bound used for end-extension persistence
# sorted x<=y<=z with 4/n = 1/x+1/y+1/z  =>  x<=3n/4, y<=2nx, z<=nxy  (checked on all solutions, n<=60)
viol = 0
# (y is enumerated far beyond the claimed bound, so the y-bound is tested, not assumed)
for n in range(2, 41):
    for x in range(1, n + 1):
        num = 4*x - n
        if num <= 0:
            continue
        for y in range(x, 4*n*n + 10):
            den = num*y - n*x
            if den <= 0:
                continue
            if (n*x*y) % den == 0:
                zz = n*x*y//den
                if zz >= y:
                    assert Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, zz)
                    if not (4*x <= 3*n and y <= 2*n*x and zz <= n*x*y):
                        viol += 1
check('ES coordinate bounds x<=3n/4, y<=2nx, z<=nxy on all solutions n<=40', viol == 0)

print(f'{len(ok)} checks passed')
for name in ok:
    print('  OK', name)
