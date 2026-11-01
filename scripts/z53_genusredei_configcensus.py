# Configuration census for JRT (Z53_GENUSREDEI §6.2): line N = 4Cp + 1 (level 12, C = 3), primes p ≡ 1 (4),
# N = l1*l2 with l1 < l2 primes > B (B = 61) and s = 1. Decorations: a1 = l1 mod 12 (a2 = a1^{-1} forced by (L1)),
# q_i = [l_i is a 4th power mod p], eps = (l1/l2). Laws predict: (L3) (l/p) = (-3/l) (QR iff l ≡ 1 mod 3);
# (L2) zeta1*zeta2 = 1, so q1 = q2; quartic symbol of a non-QR is never 1. Law-compatible configurations: 12.
import sys
from sympy import factorint, primerange, legendre_symbol as leg
P = int(sys.argv[1]); C = 3; t = 4 * C; B = 61
cnt = {}; viol = 0; tot = 0
for p in primerange(5, P):
    if p % 4 != 1: continue
    N = 4 * C * p + 1; f = factorint(N)
    if len(f) != 2 or any(e > 1 for e in f.values()) or min(f) <= B: continue
    l1, l2 = sorted(f); tot += 1
    q1 = pow(l1, (p - 1) // 4, p) == 1; q2 = pow(l2, (p - 1) // 4, p) == 1
    r1 = leg(l1 % p, p); r2 = leg(l2 % p, p)
    if r1 != leg(-3 % l1, l1) or r2 != leg(-3 % l2, l2) or q1 != q2 or (l1 * l2) % t != 1: viol += 1
    key = (l1 % t, l2 % t, q1, q2, leg(l1, l2)); cnt[key] = cnt.get(key, 0) + 1
print("# p <", P, "line 12p+1, two large factors, s=1: instances", tot, "law violations", viol)
print("# a1 a2 q1 q2 eps count")
for k in sorted(cnt): print(*[int(x) if isinstance(x, bool) else x for x in k], cnt[k])
print("# distinct configurations:", len(cnt), "(law-compatible: 12)")
