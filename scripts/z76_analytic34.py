"""Exact vertex checks for the near-cube estimates in ANALYTIC_34.md."""
from fractions import Fraction as F

half = F(1, 2)
bo = F(13, 84), F(55, 84)
ty = [(F(4742, 38463), F(35731, 51284)), (F(18, 199), F(593, 796)),
      (F(2779, 38033), F(58699, 76066)), (F(715, 10238), F(7955, 10238))]


def B(pair):
    k, l = pair
    return l - half, k + half


def A(pair):
    k, l = pair
    return k/(2+2*k), half + l/(2+2*k)


def theta(pair):
    k, l = pair
    return 2*(1+2*k)/(7+12*k-l)


def direct(pair):
    k, l = pair
    m = 3+2*k-2*l
    return m/(1+3*m-k-l)


def vertices(t):
    return [(t, 1-2*t, t), (t, t, 1-2*t), ((1-t)/2, (1-t)/2, t)]


for pair in [(half, half), B(ty[3])]:
    k, l = pair
    t = theta(pair)
    print('after periodic shift:', pair, 'theta', t, float(t))
    for a, b, g in vertices(t):
        r = b-t
        j = 2*(r+g-t)
        d = j+2*r+1-b-2*g
        f = r+((1+l)*g+k*d)/2
        print(f'  alpha={a} beta={b} gamma={g} shift margin={g-j-2*r} D={d} F={f}')
        assert r >= 0 and j >= 0 and 2*r+g-b >= 0
        assert j+2*r < g and d > 0 and 3*g-1 < l*g
        assert b-2*r <= t and b-g <= t and f <= t

pair = ty[1]
k, l = pair
t = direct(pair)
print('direct off-line pair:', pair, 'theta', t, float(t))
for a, b, g in vertices(t):
    r = b-t
    v = (3+2*k-2*l)*r+k*a+l*g
    assert 2*r < g and 2*g < 1 and 3*r <= t and v <= t
    print(f'  alpha={a} beta={b} gamma={g} term={v}')

# Linear fractional objectives with positive denominator have half-plane
# sublevels. A minimum at a vertex of a convex polygon can thus be checked
# just on its two neighbors (strict inequalities give uniqueness).
assert direct(ty[1]) < min(direct(ty[0]), direct(ty[2]))
assert theta(B(ty[3])) < min(theta(B(ty[2])), theta(B(A(ty[0]))))
print('TY convex hull: adjacent-vertex tests passed')
