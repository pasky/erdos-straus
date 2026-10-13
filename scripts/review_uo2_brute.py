"""R190 reviewer-2 from-scratch check of UNIT_ORBIT_ES Prop 2.1 / Thm 2.4 for S = {3,5,7,11}.

For every odd n < N coprime to S: search Q in <S> (increasing) and a prime r = 3 mod 4 dividing n + 4Q^2,
build (x, y, z) of Prop 2.1, verify exactly: 4/n = 1/x+1/y+1/z, x,y in Z_{>0}, z>0, z in Z[1/S] with even
negative q-valuations, Type II shape at every prime of n. Squares: verify no (Q, r) with Q <= QMAX.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_uo2_brute.py [N] [QMAX]
"""
import sys
from fractions import Fraction
from math import isqrt
from sympy import factorint

S = [3, 5, 7, 11]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10**4


def monoid(qs, bound):
    out = {1}
    for q in qs:
        new = set()
        for v in out:
            w = v
            while w <= bound:
                new.add(w)
                w *= q
        out = new
    return sorted(out)


def val(p, num):
    if num == 0:
        return 10**9
    k = 0
    while num % p == 0:
        num //= p
        k += 1
    return k


def fval(p, f):
    return val(p, f.numerator) - val(p, f.denominator)


QS = monoid(S, QMAX)
fail, maxQ, nonsq, sq_hits, nsq = [], 0, 0, 0, 0
hist = {}
for n in range(3, N, 2):
    if any(n % q == 0 for q in S):
        continue
    is_sq = isqrt(n) ** 2 == n
    fn = factorint(n)
    found = None
    for Q in QS:
        a = n + 4 * Q * Q
        rs = [r for r in factorint(a) if r % 4 == 3]
        if rs:
            found = (Q, rs[0])
            break
        if not is_sq and Q > 2000:
            break
    if is_sq:
        nsq += 1
        if found:
            sq_hits += 1
        continue
    nonsq += 1
    if not found:
        fail.append(n)
        continue
    Q, r = found
    maxQ = max(maxQ, Q)
    hist[Q] = hist.get(Q, 0) + 1
    a = n + 4 * Q * Q
    e = a // r
    assert (n + e) % 4 == 0 and (n * (r + 1)) % 4 == 0
    x = (n + e) // 4
    y = n * (r + 1) // 4
    z = Fraction(n * x * (r + 1), 4 * Q * Q)
    assert x > 0 and y > 0 and z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    # z in Z[1/S], even negative valuations
    den = z.denominator
    for q in S:
        while den % q == 0:
            den //= q
        v = fval(q, z)
        assert v >= 0 or v % 2 == 0, (n, Q, r, q, v)
    assert den == 1
    for l, t in fn.items():  # Type II shape at l
        assert x % l != 0 and val(l, y) >= t and fval(l, z) >= t, (n, l)
print(f"N={N}: non-squares coprime to 2S: {nonsq}, failures: {len(fail)} {fail[:10]}, max Q used: {maxQ}")
print("Q histogram (top):", sorted(hist.items(), key=lambda kv: -kv[1])[:12])
print(f"squares coprime to 2S: {nsq}, squares with a hit for Q <= {QMAX}: {sq_hits}")
