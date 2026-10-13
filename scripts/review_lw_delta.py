"""R180: delta_x = 1 - 1/r, r = least 2^j such that -1 is not a 2^j-th power in (Z/x)^* (= least order of an odd character mod x).
Checks the §5 claim 'sum_{x<=X} delta_x = (1+o(1))X'."""
from math import gcd
def delta(x):
    if x <= 2: return 1.0
    G = [a for a in range(1, x) if gcd(a, x) == 1]
    S = set(G); r = 1
    while True:
        r *= 2
        S = {a * a % x for a in S}
        if (x - 1) not in S: return 1 - 1 / r
for X in (12, 100, 1000, 3000):
    ds = [delta(x) for x in range(2, X + 1)]
    print(X, "sum/X = %.3f" % (sum(ds) / X), " frac(delta=1/2) = %.3f" % (sum(1 for d in ds if d == 0.5) / len(ds)))
print({x: delta(x) for x in range(2, 21)})
