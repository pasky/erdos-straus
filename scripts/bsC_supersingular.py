"""O176 memo bsC_supersingular_transfer numerics.

For primes 5 <= p <= X:
 (i)  Kaneko ratio of certificates: Type I e = det(2T)/p, Type II det(2T')/(4p)... we report
      min_e(Type I) and min c^2 d (Type II: det(2T') = 16 c^2 d p).
 (ii) curves that can carry a Type I certificate: E must have Z[sqrt(-d)] in End(E); #such E <= R(-4d) :=
      number of all (incl. imprimitive) reduced forms of disc -4d.  B(p) := sum over distinct certificate d of R(-4d),
      compared with #supersingular j ~ p/12.
 (ii') sharper: Lambda_{d,ab} is Eichler of level e, so #E carrying a given Type I certificate <= 2 tau(e);
      C_I(p) := sum over Type I tuples of 2 tau(e).
 (iii) T1 control: no tuples at odd squares.
Run: PYTHONPATH=scripts uv run python scripts/bsC_supersingular.py X
"""
import sys
from math import isqrt
from collections import Counter
from sympy import isprime, divisor_count
from bsC_common import typeI_all, typeII_all

X = int(sys.argv[1]) if len(sys.argv) > 1 else 5000


def nforms(D):  # all reduced forms (a,b,c), b^2-4ac = D < 0, primitive or not
    cnt = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            cnt += 1
        a += 1
    return cnt


I = typeI_all(X)
II = typeII_all(X)
st = Counter()
worst = 0.0
worstC = 0.0
mins = []
for p in range(5, X + 1, 2):
    if not isprime(p):
        continue
    tI, tII = I.get(p, []), II.get(p, [])
    st['primes'] += 1
    st['primes with no Type I'] += (not tI)
    st['primes with no Type II'] += (not tII)
    if tI:
        ds = {t[3] for t in tI}
        B = sum(nforms(-4 * d) for d in ds)
        C = int(sum(2 * int(divisor_count(t[4])) for t in tI))
        st['primes with C_I(p) >= p/12'] += (C >= (p - 1) / 12)
        if p > 1000:
            worstC = max(worstC, C / ((p - 1) / 12))
        worst = max(worst, B / ((p - 1) / 12))
        st['primes with B(p) >= p/12'] += (B >= (p - 1) / 12)
        mins.append((p, min(t[4] for t in tI), min(t[2] ** 2 * t[3] for t in tII) if tII else None))
sq = [m * m for m in range(3, isqrt(X) + 1, 2)]
st['tuples at odd squares'] = sum(len(I.get(s, [])) + len(II.get(s, [])) for s in sq)
print(dict(st))
print('max B(p)/(p/12) =', round(worst, 4), ' max_{p>1000} C_I(p)/(p/12) =', round(worstC, 4))
print('max over p of min Type I e:', max(m[1] for m in mins),
      ' max over p of min Type II c^2 d:', max(m[2] for m in mins if m[2]))
big = sorted(mins, key=lambda m: -m[1])[:5]
print('largest min-e primes (p, min e, min c^2d):', big)
