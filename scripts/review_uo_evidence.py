"""R186: from-scratch EVIDENCE for ES^(S), S = {3,5,7,11}.
(1) Hilbert-symbol sanity: product formula on random pairs.
(2) Every prime 13 <= p < P (p not in S): find smallest Q in <S> with n + 4Q^2 having a prime factor r = 3 mod 4,
    build the Prop 2.1 solution independently, verify exactly (equation, positivity, Z[1/S], parity, Type II at p),
    and check Lemma 1.1 (inv_q = 0 for q in S) + global product formula with Hilbert symbols.
(3) Odd non-squares n < N2 coprime to 2S, same.
usage: review_uo_evidence.py P N2
"""
import sys, random
from fractions import Fraction
from sympy import factorint
from review_uo_common import *

S = [3, 5, 7, 11]
P = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
N2 = int(sys.argv[2]) if len(sys.argv) > 2 else 20000

# (1) product formula sanity
random.seed(1)
for _ in range(2000):
    a = Fraction(random.choice([-1, 1]) * random.randint(1, 500), random.randint(1, 50))
    b = Fraction(random.choice([-1, 1]) * random.randint(1, 500), random.randint(1, 50))
    ps = set(factorint(abs(a.numerator) * a.denominator * abs(b.numerator) * b.denominator).keys()) | {2}
    prod = hilbert(a, b, 0)
    for p in ps:
        prod *= hilbert(a, b, p)
    assert prod == 1, (a, b)
print("Hilbert product formula OK on 2000 random pairs")

QS = smonoid(S, 10 ** 7)


def shot(n):
    for Q in QS:
        a = n + 4 * Q * Q
        for r in factorint(a):
            if r % 4 == 3:
                return Q, r
    return None


def build(n, Q, r):
    a = n + 4 * Q * Q
    e = a // r
    x = Fraction(n + e, 4)
    y = Fraction(n * (r + 1), 4)
    z = Fraction(n) * x * (r + 1) / (4 * Q * Q)
    return x, y, z


def full_check(n, Q, r):
    x, y, z = build(n, Q, r)
    check_ESS(n, x, y, z, S)
    for l, k in factorint(n).items():  # Type II at every prime of n
        assert vp(x, l) == 0 and vp(y, l) >= k and vp(z, l) >= k
    a1, a2 = -x / z, -y / z
    for q in S:
        assert inv(a1, a2, q) == 0, ("Lemma 1.1 fails", n, Q, r, q)
    assert inv(a1, a2, 2) == 0 and inv(a1, a2, 0) == 1
    s = sum(inv(a1, a2, l) for l in factorint(n))
    assert s % 2 == 1
    negq = any(vp(z, q) < 0 for q in S)
    return negq


stats = {}
maxQ = 0
nneg = 0
cnt = 0
for p in primes_upto(P):
    if p < 13 or p in S:
        continue
    res = shot(p)
    assert res is not None, p
    Q, r = res
    nneg += full_check(p, Q, r)
    stats[Q] = stats.get(Q, 0) + 1
    maxQ = max(maxQ, Q)
    cnt += 1
print(f"primes 13<=p<{P}: {cnt} solved, max Q = {maxQ}, Q=1 for {stats.get(1,0)}, "
      f"z with negative q-valuation in {nneg}; Q distribution {sorted(stats.items())[:12]}")

cnt = 0
maxQ = 0
for n in range(3, N2, 2):
    if any(n % q == 0 for q in S):
        continue
    m = int(round(n ** 0.5))
    if m * m == n:
        # squares: no Q up to bound may give r = 3 mod 4 (sum of two coprime squares)
        for Q in QS[:40]:
            assert all(r % 4 == 1 for r in factorint(n + 4 * Q * Q))
        continue
    res = shot(n)
    assert res is not None, n
    full_check(n, *res)
    maxQ = max(maxQ, res[0])
    cnt += 1
print(f"odd non-squares n<{N2} coprime to 2S: {cnt} solved, max Q = {maxQ}; squares: no shot (Q among first 40)")
