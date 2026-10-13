"""FROBENIUS_FIRING (O196) §4 numerics over Z: one mute place S = {s}.
For every n in the input set, find the least j >= 0 such that n + 4 s^{2j} has a prime factor r = 3 (mod 4)
  [ES^{(s)}]  and the least j such that it has a prime factor r = 3 (mod 4), r = -1 (mod s)  [self-mute ES^{(y)}].
Every solution of UNIT_ORBIT Prop 2.1 is verified exactly (equation, positivity, z-denominator supported on {s},
even exponent, s | y for ES^{(y)}, n coprime to s).
usage: ff_frob_selfmute.py s N [jmax] [squares]
"""
import sys
from fractions import Fraction
from sympy import factorint, primerange

s = int(sys.argv[1]); N = int(sys.argv[2]); jmax = int(sys.argv[3]) if len(sys.argv) > 3 else 60
squares = len(sys.argv) > 4 and sys.argv[4] == 'squares'


def vs(x, q):
    v = 0
    while x % q == 0:
        x //= q; v += 1
    return v


def verify(n, Q, r, selfmute):
    a = n + 4 * Q * Q
    assert a % r == 0
    e = a // r
    assert (n + e) % 4 == 0 and (r + 1) % 4 == 0
    x = (n + e) // 4; y = n * (r + 1) // 4
    z = Fraction(n * x * (r + 1), 4 * Q * Q)
    assert x > 0 and y > 0 and z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    den = z.denominator
    if den > 1:
        assert den == s ** vs(den, s) and vs(den, s) % 2 == 0
        if selfmute:
            assert y % s == 0
    return True


inputs = ([m * m for m in range(3, int(N ** 0.5) + 1, 2) if m % s] if squares
          else [p for p in primerange(5, N) if p % s])
hist1, hist2 = {}, {}
fail1 = fail2 = 0
for n in inputs:
    j1 = j2 = None
    for j in range(jmax + 1):
        Q = s ** j
        fs = factorint(n + 4 * Q * Q)
        r1 = [r for r in fs if r % 4 == 3]
        r2 = [r for r in r1 if r % s == s - 1]
        if j1 is None and r1:
            j1 = j; verify(n, Q, r1[0], False)
        if j2 is None and r2:
            j2 = j; verify(n, Q, r2[0], True)
        if j1 is not None and j2 is not None:
            break
    if j1 is None: fail1 += 1
    else: hist1[j1] = hist1.get(j1, 0) + 1
    if j2 is None: fail2 += 1
    else: hist2[j2] = hist2.get(j2, 0) + 1
print(f"s={s} inputs={'odd squares' if squares else 'primes'} < {N} (coprime to s): count={len(inputs)} jmax={jmax}")
print(f"  ES^(s)  least-j histogram {dict(sorted(hist1.items()))}  unsolved={fail1}")
print(f"  ES^(y)  least-j histogram {dict(sorted(hist2.items()))}  unsolved={fail2}")
