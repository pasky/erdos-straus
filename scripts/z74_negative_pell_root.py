"""Independent symbolic and finite-chart checks, not a proof of the PID construction."""
from itertools import product
from math import gcd
from sympy import I, cancel, discriminant, expand, symbols


def symbolic():
    u, v, a, b, t, x = symbols('u v a b t x')
    C, D, Y = u*u-v*v, 2*u*v, u*u+v*v
    P, X, L = a*a+b*b, C*a-D*b, D*a+C*b
    assert expand((a+I*b)*(u+I*v)**2-X-I*L) == 0
    assert expand(P*Y**2-X**2-L**2) == 0
    assert expand(discriminant(L,u) - (4*P*v*v)) == 0
    chart = {a: (C*x+D)/Y**2, b: (C-D*x)/Y**2}
    for f in (L-1, X-x, P*Y**2-1-x*x):
        assert cancel(f.subs(chart)) == 0
    for j in [I, -I]:
        fibre = {a: j/t**2, b: 1/t**2, u: t-j*v}
        for f in (P, L-1, X-j, b*(u+j*v)**2-1):
            assert cancel(f.subs(fibre, simultaneous=True)) == 0


def residue_points(q):
    squares = {n*n%q for n in range(1,q)}
    all_good, special = set(), 0
    # Direct enumeration: no chart restriction on the original row.
    for u,v,a,b in product(range(q), repeat=4):
        C, D, Y = u*u-v*v, 2*u*v, (u*u+v*v)%q
        if (D*a+C*b)%q != 1:
            continue
        X, P = (C*a-D*b)%q, (a*a+b*b)%q
        assert (X*X+1-P*Y*Y)%q == 0
        if P == 0:
            special += 1
            assert b and X*b%q == a
        if Y and P in squares:
            all_good.add((u,v,X,a,b))
    chart = set()
    for u,v,X in product(range(q), repeat=3):
        Y, C, D = (u*u+v*v)%q, u*u-v*v, 2*u*v
        if not Y or (1+X*X)%q not in squares:
            continue
        h = pow(Y, -2, q)
        chart.add((u,v,X,(C*X+D)*h%q,(C-D*X)*h%q))
    assert chart == all_good
    split = q-1 in squares
    pairs = (q-1)**2 if split else q*q-1
    assert len(chart) == pairs*((q-1-2*int(split))//2)
    assert special == 2*int(split)*q*(q-1)
    return len(chart)


def centers(n):
    units = [s for s in range(n) if gcd(n,s)==1]
    norms = {(u*u+v*v)%n for u,v in product(range(n),repeat=2)}
    # X=0: check the signed inverse-root recipe on *every* unit-square class.
    for s in units:
        y = pow(s,-1,n)
        assert y in norms or -y%n in norms


if __name__ == '__main__':
    symbolic()
    for q in (3,5,7,11,13,17,19):
        print(f'q={q}: {residue_points(q)} marked chart points')
    for n in (256,81,125,49):
        centers(n)
    print('Gaussian signs, rank-one fibres, Pell identity, inverse charts and local centers pass.')
