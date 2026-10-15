"""O237 (CAP_DOWN Thm 1.2): even windows.

For odd non-square n = 1 (mod 4) with all prime factors = 1 (mod 4) (the only case where e*(n) > 0 is possible):
  q*_old(n): least prime q = 4 - n (mod 8), (q/n) = -1          (CAP_POINTWISE Thm 1.1)
  q*_new(n): least prime q = 3 (mod 4), (q/n) = -1, with (E): q = 7 (mod 8) or v2((n+q)/4) even  (Thm 1.2)
  q*_14(n):  least prime q = 3 (mod 4), (q/n) = -1   (the Pollack-1/4 object; = q*_new when n = 1 mod 8)
At q*_new: build the forced witness of the proof (h = (-K')^((o+1)/2), d = 2^t * prod s^{2 a_s}) and verify exactly
(Fraction) that it is an ES^{(y,e)}(n) solution with e <= q - 3 (Lemma 1.1); also compute the least cap at that window
over the full Lemma 1.1 exponent sets.  Odd squares: count windows (must be 0).
usage: z13_even_windows.py N [mode: primes|all]
"""
import sys
from fractions import Fraction
from math import isqrt
from sympy import jacobi_symbol, isprime, factorint, n_order

N = int(sys.argv[1]); MODE = sys.argv[2] if len(sys.argv) > 2 else 'primes'
QP = [q for q in range(3, 5000) if isprime(q) and q % 4 == 3]


def v2(k):
    t = 0
    while k % 2 == 0:
        k //= 2; t += 1
    return t


def check(n, x, y, z, e):
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z and x > 0 and y > 0 and z > 0
    D = z.denominator
    r = isqrt(D); assert r * r == D and r % 2 == 1
    for l, v in factorint(r).items():
        assert n % l and y % l == 0 and v <= e


def witness(n, q):
    K = (n + q) // 4; t = v2(K); Kp = K >> t
    fs = factorint(Kp)
    h = pow((-Kp) % q, (n_order((-Kp) % q, q) + 1) // 2, q)
    # represent h in <odd primes of K'> by BFS over exponent vectors (q small)
    S = sorted(fs); seen = {1 % q: (0,) * len(S)}; frontier = [1 % q]
    while h not in seen:
        nf = []
        for g in frontier:
            for i, s in enumerate(S):
                gg = g * s % q
                if gg not in seen:
                    vec = list(seen[g]); vec[i] += 1; seen[gg] = tuple(vec); nf.append(gg)
        assert nf, 'h not in H: theorem violated'
        frontier = nf
    a = seen[h]
    d = 2 ** t
    for s, ai in zip(S, a):
        d *= s ** (2 * ai)
    assert (K + d) % q == 0
    A = (K + d) // q
    e = max([0] + [ai - fs[s] for s, ai in zip(S, a)])
    check(n, K, n * A, Fraction(n * K * A, d), e)
    assert e <= q - 3
    return e


def witness2(n, q):
    """Prop 1.3: d = K * s^(o/2) for a non-residue prime s | K' with odd v_s(K); cap = max(0, (o/2 - b)/2)."""
    K = (n + q) // 4; fs = factorint(K); best = None
    for s, b in fs.items():
        if s == 2 or b % 2 == 0 or jacobi_symbol(s, q) != -1:
            continue
        o = n_order(s, q); assert o % 2 == 0 and (o // 2) % 2 == 1 and pow(s, o // 2, q) == q - 1
        e = max(0, (o // 2 - b) // 2)
        if best is None or e < best[0]:
            best = (e, s, o)
    assert best is not None, 'no odd-exponent non-residue prime: Prop 1.3 violated'
    e, s, o = best
    d = K * s ** (o // 2); A = (K + d) // q; assert (K + d) % q == 0
    check(n, K, n * A, Fraction(n * K * A, d), e)
    assert 4 * e <= q - 3
    return e


def best_cap(n, q, emax):
    K = (n + q) // 4; fs = factorint(K); target = (-K) % q
    for e in range(emax + 1):
        R = {1}
        for s, b in fs.items():
            C = set(range(0, 2 * b + 1))
            if s != 2:
                C |= set(range(0, 2 * b + 2 * e + 1, 2))
            P = [pow(s, c, q) for c in C]
            R = {r * p % q for r in R for p in P}
        if target in R:
            return e
    return None


stats = {}
mx = {}
sq_windows = 0
for n in range(5, N + 1, 4):
    if MODE == 'primes' and not isprime(n):
        continue
    r = isqrt(n)
    if r * r == n:
        sq_windows += sum(1 for q in QP[:40] if n % q and jacobi_symbol(q, n) == -1)
        continue
    if any(l % 4 == 3 for l in factorint(n)):
        continue
    qo = qn = q14 = None
    for q in QP:
        if n % q == 0 or jacobi_symbol(q, n) != -1:
            continue
        if q14 is None:
            q14 = q
        t = v2((n + q) // 4)
        if qn is None and (q % 8 == 7 or t % 2 == 0):
            qn = q
        if qo is None and (q + n) % 8 == 4:
            qo = q
        if qo and qn:
            break
    e = witness(n, qn)
    e2 = witness2(n, qn)
    bc = best_cap(n, qn, qn)
    cls = n % 8
    st = stats.setdefault(cls, {'cnt': 0, 'new<old': 0, 'q14bad': 0, 'sum_old': 0, 'sum_new': 0})
    st['cnt'] += 1; st['new<old'] += qn < qo; st['q14bad'] += q14 != qn
    st['sum_old'] += qo; st['sum_new'] += qn
    for key, val in (('qold', qo), ('qnew', qn), ('wit_cap', e), ('prop14_cap', e2), ('best_cap_at_qnew', bc)):
        if val > mx.get((cls, key), (0, 0))[0]:
            mx[(cls, key)] = (val, n)
print('N', N, 'mode', MODE)
for cls, st in sorted(stats.items()):
    print('n mod 8 =', cls, st, 'mean qold %.2f qnew %.2f' % (st['sum_old'] / st['cnt'], st['sum_new'] / st['cnt']))
for k, v in sorted(mx.items()):
    print('max', k, '=', v[0], 'at n =', v[1])
print('odd-square windows (must be 0):', sq_windows)
