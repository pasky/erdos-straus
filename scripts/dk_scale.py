"""O169 §9.2: scaling transfer K(a v', t, a u') = a K(v', a t, u').
(a) brute check of the sign law: for n = a m odd, word (v,t,u)=(a v', t, a u') of n: (A/n) = (-1/a) * (A/m), A = t a u' - 1
    (A is the same number for the m-word (v', a t, u'), u',v' >= 1 allowed).
(b) family F: n = q(qt-2), q = 3 (4): word [[q,t,q]] has (A/n) = -1.
(c) coverage: composite non-square n = 1 (4) <= N with a divisor a = 3 (4): fraction having a -1 word with a | u, a | v.
Usage: uv run python scripts/dk_scale.py N
"""
import sys
from math import isqrt, gcd
def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
N = int(sys.argv[1])
bad = cnt = 0
for a in range(2, 40):
    for t in range(2, 30):
        for u1 in range(1, 25):
            for v1 in range(1, 25):
                m = v1 * a * t * u1 - u1 - v1
                if m < 3 or m % 2 == 0 or a % 2 == 0: continue  # Jacobi needs a, m odd
                n = a * m; A = t * a * u1 - 1
                if gcd(A, n) != 1: continue
                cnt += 1
                if jac(A, n) != (-1) ** ((a - 1) // 2) * jac(A, m): bad += 1
print("(a) sign law checks:", cnt, "failures:", bad)
fb = sum(1 for q in range(3, 200, 4) for t in range(2, 200) if jac(t * q - 1, q * (q * t - 2)) != -1)
print("(b) family [[q,t,q]] failures:", fb)
neg_ua = bytearray(N + 1); anyneg = bytearray(N + 1)
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1; v = 2
        while (n := v * A - u) <= N:
            if n % 4 == 1 and (A % 4 == 0 or (t*v-1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0):
                anyneg[n] = 1
                g = gcd(gcd(u, v), n)
                # some divisor a = 3 mod 4 of g?
                if g > 1:
                    x, ok, q = g, False, 3
                    for d in range(3, g + 1, 4):
                        if g % d == 0: ok = True; break
                    if ok: neg_ua[n] = 1
            v += 1
        u += 1
    t += 1
tot = cov = 0
for n in range(9, N + 1, 4):
    if isqrt(n) ** 2 == n: continue
    if not any(n % d == 0 for d in range(3, isqrt(n) + 1, 2) if d % 4 == 3 or (n // d) % 4 == 3): continue
    tot += 1; cov += neg_ua[n]
print(f"(c) N={N}: composite non-square n=1(4) with a divisor =3(4): {tot}; having a -1 word with a|u,a|v (a=3 mod 4, a|n): {cov}")
