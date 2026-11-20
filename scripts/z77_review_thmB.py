"""z77 review of Theorem B transfer, on a SMALLER modulus Q' (fixed-row odd lcm * 255 * 127; s<32 multiples omitted,
so only s>=32 is tested). N = c 2^s + d, c = 2^(2J-1)+127, d = 2^(2J-1)-127, J = 4 + ord_Q'(2)."""
import json, sys
from math import lcm
sys.path.insert(0, 'scripts')
from z77_review_proth_e2e import check, word_triples, root
rows = json.loads((root/'255-5040-0.json').read_text())['rules']
def fac(n):
    f = {}; p = 2
    while p*p <= n:
        while n % p == 0: f[p] = f.get(p, 0)+1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
oddQ = 61500575996988381601913565
print('factor oddQ', fac(oddQ))
Q = lcm(oddQ, 255, 127)
def order(a, m):
    o = 1
    for p, e in fac(m).items():
        o = lcm(o, next(t for t in range(1, p**e) if pow(a, t, p**e) == 1))
    return o
o = order(2, Q); J = 4 + o; c = 2**(2*J-1) + 127; d = 2**(2*J-1) - 127
print('ord', o, 'bits c', c.bit_length(), c % 255, d % Q, c % 128, d % 128)
from collections import Counter
cnt = Counter()
for s in list(range(32, 32+5040, 7)) + [5040*i for i in range(1, 8)]:
    N = c*2**s + d
    R = 'X' if s % 5040 == 0 else check(255, rows, s, N)
    if R == 'X':  # same divisor A as for n = 255 2^s + 1, applied to N + 254 = c(2^s+1)
        from z77_review_proth_e2e import phi
        q = s//315
        while q % 7 == 0: q //= 7
        x = 2**q; M = 8*254; divs = [e for e in range(1, 316) if 315 % e == 0]
        F = {e: phi(2*e, x) for e in divs}
        reach = {cc: (cc, ()) for cc in (1, 3, 5, 15, 17, 51, 85, 255)}
        for e in divs:
            for r0, (cc, T) in list(reach.items()): reach.setdefault(r0*F[e] % M, (cc, T+(e,)))
        cc, T = reach[(7*254-1) % M]; A = cc
        for e in T: A *= F[e]
        assert (N+254) % A == 0 and (A+1) % 254 == 0
        assert word_triples(N, (A+1)//254, 254, (N+254)//A)
    cnt[R] += 1
print('Theorem B transfer (s>=32, Q\')', dict(cnt))
