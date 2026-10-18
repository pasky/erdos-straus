"""R280: from-scratch reproduction of O269 §6 / z39_quartic_slices item 2.
Primes p = 1 (8) < P; slice k | t of ES words (t,u,v), A = tu-1, A* = tv-1; quartic symbol x^{(p-1)/4} mod p with
i := a * b^{-1} mod p, p = a^2 + b^2, a odd, a, b > 0.  Bit = chi4(min(A, A*)).  Also checks chi4(A*) = chi4(A)^{-1}."""
import sys
from sympy import isprime
P = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
W = {}
for t in range(2, P):
    if 4 * t - 4 > P: break
    for u in range(2, P):
        if 2 * t * u - u - 2 > P: break
        for v in range(u, P):
            n = t * u * v - u - v
            if n > P: break
            W.setdefault(n, []).append((t, u, v))
for k in (4, 8, 16):
    const_i = const = mixed = empty = inv_bad = 0
    for p in range(17, P, 8):
        if not isprime(p): continue
        a = next(x for x in range(1, int(p ** .5) + 1, 2) if int((p - x * x) ** .5) ** 2 == p - x * x)
        b = int((p - a * a) ** .5)
        I = a * pow(b, -1, p) % p
        assert I * I % p == p - 1
        lab = {1: 1, I: 'i', p - 1: -1, p - I: '-i'}
        vals = set()
        for (t, u, v) in W.get(p, []):
            if t % k: continue
            A, As = t * u - 1, t * v - 1
            cA, cAs = pow(A, (p - 1) // 4, p), pow(As, (p - 1) // 4, p)
            if cA * cAs % p != 1: inv_bad += 1
            vals.add(lab[pow(min(A, As), (p - 1) // 4, p)])
        if not vals: empty += 1
        elif len(vals) == 1:
            const += 1; const_i += vals == {'i'}
        else: mixed += 1
    print(f"k={k}: constant {const} (value i in {const_i}), mixed {mixed}, empty {empty}; chi4(A*)!=chi4(A)^-1: {inv_bad}")
