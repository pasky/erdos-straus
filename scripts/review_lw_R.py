"""R180: R(n) = #ordered (x,y,z), x,y,z>=2, xyz-x-z=n; spot-check §2 values."""
from sympy import divisors
from math import isqrt
def R(n):
    c = 0
    for x in range(2, isqrt(n) + 3):
        for d in divisors(n + x):
            if (d + 1) % x or d < 2 * x - 1: continue
            z = (n + x) // d
            if z < x: continue
            c += 1 if z == x else 2
    return c
for n in [2079, 5580, 9090, 174**2, 186**2, 264**2, 570**2, 924**2, 1386**2, 2310**2, 4020**2, 30030**2]:
    print(n, R(n))
print("Lorenzini family:", [R(2**(2*k+1) - 2) for k in range(1, 9)])
