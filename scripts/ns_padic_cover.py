"""O221 (NEAR_SQUARE §3): level-L coverage of m-classes for n = m^2 + k by
 (i) ET Prop 1.9 congruence classes of n with modulus dividing L (all seven families, enumerated exhaustively), and
 (ii) escaping polynomial families (file from ns_polyfam.py) with modulus dividing L.
Prints the uncovered m-classes mod L with n odd, n = 1 (mod 4).  Usage: ns_padic_cover.py K L FAMFILE"""
import sys, ast
from math import gcd
K, L = int(sys.argv[1]), int(sys.argv[2])
fams = [ast.literal_eval(l) for l in open(sys.argv[3])] if len(sys.argv) > 3 else []
divL = [x for x in range(1, L + 1) if L % x == 0]
cert = bytearray(L)          # certified n-classes mod L
def mark(mod, res):          # n = res (mod mod), mod | L
    res %= mod
    for x in range(res, L, mod): cert[x] = 1
def divisors(x): return [y for y in range(1, x + 1) if x % y == 0]
for M in divL:
    if M % 4: continue
    Q = M // 4
    for a in divisors(Q):
        for b in divisors(Q // a):
            if Q % (a * b): continue
            if 4 * a * b != M: continue
            for e in divisors(a + b):
                if gcd(e, 4 * a * b) == 1:
                    mark(M, -e)                                   # TII-1
                    mark(M, -pow(e, -1, M))                       # TI-4
        for d in divisors(Q // a):
            if 4 * a * d != M: continue
            for f in divisors(4 * a * a * d + 1): mark(M, -f)     # TI-1
            # TII-3: n = -4a^2 d - e mod 4ade, (4ad, e) = 1 with 4ade | L
            for e in divL:
                if gcd(4 * a * d, e) == 1 and L % (M * e) == 0: mark(M * e, -4 * a * a * d - e)
for f in divL:                                                    # TII-2: n = -4a^2 d (mod f), 4ad | f + 1
    for a in divisors(f + 1):
        for d in divisors((f + 1) // a):
            if (f + 1) % (4 * a * d) == 0: mark(f, -4 * a * a * d)
for M in divL:                                                    # TI-2 / TI-3 with f | L, gcd(M, f) = 1
    if M % 4: continue
    Q = M // 4
    for f in divL:
        if gcd(M, f) != 1 or L % (M * f): continue
        for a in divisors(Q):
            c = Q // a
            # TI-2: n = -f (mod 4ac), n = -c/a (mod f)
            if gcd(a, f) == 1:
                r = (-c * pow(a, -1, f)) % f if f > 1 else 0
                for x in range(-f % M, M * f, M):
                    if x % f == r: mark(M * f, x); break
            # TI-3 with (c, d) = (a, c): n = -f (mod 4cd), n^2 = -4c^2 d (mod f)
            cc, dd = a, c
            for x in range(-f % M, M * f, M):
                if (x * x + 4 * cc * cc * dd) % f == 0: mark(M * f, x)
cls = [(Lf, set(g)) for _, _, Lf, g in fams if g and L % Lf == 0]
unc = [m for m in range(L) if (m * m + K) % 4 == 1 and not cert[(m * m + K) % L] and not any(m % Lf in g for Lf, g in cls)]
tot = sum(1 for m in range(L) if (m * m + K) % 4 == 1)
print(f"k={K} L={L}: certified n-classes {sum(cert)}/{L}; families used {len(cls)}; uncovered m-classes {len(unc)}/{tot}")
print("uncovered:", unc[:40])
