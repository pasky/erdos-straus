"""Small exact checks for O157 probabilistic/geometric memo triage; stdlib only."""
from fractions import Fraction as F
from itertools import product
from math import gcd

# Product randomness over deterministic solver coordinates is perfectly possible.
omega = list(product((0, 1), repeat=6))
avoiders = [x for x in omega if all(x[2*i] != x[2*i+1] for i in range(3))]
assert len(avoiders) == 8
print('Independent nonmonotone pair-equality bad events: avoidance probability', F(len(avoiders), len(omega)))

# Re-derive the e-slice and distinguish raw factorizations from primitive counts.
def slice_points(p, e):
    assert (p+e) % 4 == 0
    n = (p+e)//4
    return [(a, b, (a+b)//e, n//(a*b))
            for a in range(1, n+1) for b in range(1, n//a+1)
            if n % (a*b) == 0 and (a+b) % e == 0]

raw = slice_points(29, 3)
primitive = [v for v in raw if gcd(v[0], v[2]) == 1]
assert len(raw) == 6 and len(primitive) == 4
for a, b, c, d in raw:
    assert 4*a*b*c*d == a+b+29*c
    assert F(4,29) == F(1,a*b*d)+F(1,a*c*d*29)+F(1,b*c*d*29)
print('p=29, e=3: raw / primitive counts', len(raw), len(primitive))
assert not slice_points(73, 3)  # (73+3)/4 = 19 = 1 mod 3.
print('p=73, e=3 prime-shift obstruction verified')

# High variance/mean and perfect positive correlation do not preclude a hard floor.
x = [1, 11]
mean = sum(map(F, x))/len(x)
variance = sum((F(t)-mean)**2 for t in x)/len(x)
assert variance/mean > 1 and min(x) > 0
print('Positive-floor distribution {1,11}: variance/mean', variance/mean)

# The stated DC Euclidean inequality holds for the isotropic form q(x,y)=xy.
maximum = F(0)
for d in range(1, 16):
    for a in range(-2*d, 2*d+1):
        for b in range(-2*d, 2*d+1):
            u, v = F(a,d), F(b,d)
            error = abs((u-round(u))*(v-round(v)))
            assert error <= F(1,4)
            maximum = max(maximum, error)
print('Isotropic xy nearest-integer rounding: max sampled |q(error)|', maximum)
assert F(4,9) == F(1,3)+F(1,12)+F(1,36)
assert all(t % 3 == 0 for t in (3,12,36))
print('Square n=9 solution (3,12,36) reduces to the vertex mod 3')
