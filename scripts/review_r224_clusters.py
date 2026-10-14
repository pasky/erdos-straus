# R224: clean-level clusters (Summary item 3): # clean levels t <= 10 for the worst primes vs. populations.
import statistics as st
from sympy import factorint
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
rows = [tuple(map(int, l.split())) for l in open('/tmp/r224_census.txt')][1:]
def ncl(p): return sum(all(leg(r, p) == 1 for r in factorint(t * p + 1)) for t in range(1, 11))
worst = sorted(rows, key=lambda r: r[2] / r[1])[:13]
print("13 worst:", [(p, round(Nm / N, 3), q) for p, N, Nm, q in worst])
print("mean clean levels t<=10, 13 worst: %.2f" % st.mean(ncl(p) for p, *_ in worst))
for name, f in [("all p=1(8), lnr>=11", lambda p, q: p % 8 == 1 and q >= 11), ("all p=1(8)", lambda p, q: p % 8 == 1), ("all p=1(8), lnr>=11, p<1e5", lambda p, q: p % 8 == 1 and q >= 11 and p < 10 ** 5)]:
    s = [p for p, N, Nm, q in rows if f(p, q)][::max(1, len([1 for p, N, Nm, q in rows if f(p, q)]) // 1500)]
    print(name, len(s), "mean clean levels t<=10: %.2f" % st.mean(ncl(p) for p in s))
# D5 mechanism among the worst primes: p = m^2 + k, levels with t k + 1 = c^2 are odd-clean
from math import isqrt
for p, N, Nm, q in worst:
    m = isqrt(p); k = p - m * m
    lv = [t for t in range(1, 11) if isqrt(t * k + 1) ** 2 == t * k + 1]
    print(p, "= %d^2 + %d" % (m, k), "T1-type levels t<=10:", lv, "clean:", [all(leg(r, p) == 1 for r in factorint(t * p + 1)) for t in lv], "all clean levels t<=10:", [t for t in range(1, 11) if all(leg(r, p) == 1 for r in factorint(t * p + 1))])
