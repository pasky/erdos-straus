"""Pass-2 SK2 Z1992/Z1993: exact checks of the Frobenius / denumerant reading of (star) and of the Popoviciu
closed form for the denumerant N(n;u,B) = #{(a,b) in Z>=0^2 : a u + b B = n}, gcd(u,B)=1.
Checks:
 (1) Popoviciu: N(n) = n/(uB) - {u' n / B} - {B' n / u} + 1 for n >= 0, with u'u = 1 mod B, B'B = 1 mod u
     (fractional parts of residues; a 'two-wave' Sylvester decomposition evaluated at n).  Tested on all coprime
     u,B <= 40 and n <= 2000 (exact, no floats: integer arithmetic).
 (2) Frobenius/denumerant identity: F = uB - u - B, N(F + j uB) = j for j >= 0 (exact);  so the (star) triple
     (u,B,C): p = (4C-1)uB + F(u,B)  <=>  N(p;u,B) = 4C-1 and p = F mod uB.
 (3) R(p) = sum over coprime (u,B) of [p = F mod uB and N(p;u,B) = 3 mod 4] (+ non-coprime pairs, checked separately)
     vs the exact divisor count R(p) for primes p = 1 mod 4 <= 600.
Run: python3 scripts/z52d_p2_SK2_frobenius.py  (pure python, < 10 s)
"""
import math, json
def denum(n, u, B):
    if n < 0: return 0
    return sum(1 for b in range(n // B + 1) if (n - b * B) % u == 0)
def popov(n, u, B):
    # exact: n/(uB) - {u'n/B} - {B'n/u} + 1 with integer arithmetic (multiply by uB)
    up = pow(u, -1, B) if B > 1 else 0
    Bp = pow(B, -1, u) if u > 1 else 0
    a = (up * n) % B if B > 1 else 0
    b = (Bp * n) % u if u > 1 else 0
    # value*(uB) = n - a*u - b*B + uB
    num = n - a * u - b * B + u * B
    assert num % (u * B) == 0
    return num // (u * B)
bad1 = 0; tot1 = 0
for u in range(1, 41):
    for B in range(1, 41):
        if math.gcd(u, B) != 1 or u == 1 or B == 1: continue
        for n in range(0, 2001):
            tot1 += 1
            if popov(n, u, B) != denum(n, u, B): bad1 += 1
bad2 = 0; tot2 = 0
for u in range(2, 30):
    for B in range(2, 30):
        if math.gcd(u, B) != 1: continue
        F = u * B - u - B
        for j in range(0, 12):
            tot2 += 1
            if denum(F + j * u * B, u, B) != j: bad2 += 1
# (3) R(p) via denumerant vs exact divisor count
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def Rdiv(p):
    tot = 0
    for C in range(1, (p + 2) // 4 + 2):
        N = 4 * C * p + 1
        d = [x for x in range(1, int(N ** .5) + 1) if N % x == 0]
        ds = set(d) | set(N // x for x in d)
        tot += sum(1 for x in ds if x % (4 * C) == 4 * C - 1)
    return tot
def Rdenum(p):
    # all (u,B) with uB | p+u+B and (p+u+B)/(uB) = 0 mod 4: coprime pairs via denumerant, others by direct check
    tot = 0
    for u in range(1, p + 2):
        for B in range(1, p + 2):
            if u * B > p + u + B: break
            if (p + u + B) % (u * B) != 0: continue
            q = (p + u + B) // (u * B)
            if q % 4 != 0: continue
            if math.gcd(u, B) == 1:
                # (star) with 4C = q; denumerant reading: N(p;u,B) = q-1 = 4C-1 = 3 mod 4
                assert denum(p, u, B) == q - 1
            tot += 1
    return tot
bad3 = 0; n3 = 0
for p in primes_upto(600):
    if p % 4 != 1: continue
    n3 += 1
    if Rdiv(p) != Rdenum(p): bad3 += 1
res = {"Z1993_popoviciu_pairs_checked": tot1, "Z1993_popoviciu_mismatches": bad1,
       "Z1992_frobenius_checks": tot2, "Z1992_frobenius_mismatches": bad2,
       "Z1992_R_divisor_vs_denumerant_primes": n3, "Z1992_R_mismatches": bad3}
json.dump(res, open("data/z52b/pass2/SK2/frobenius_checks.json", "w"), indent=1)
print(res)
