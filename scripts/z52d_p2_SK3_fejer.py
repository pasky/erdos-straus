# z52d pass2 SK3 fix, item Z3060: Fejér-weighted level counts W_X(p) = sum_{C<=X} w_C R_C(p),
# R_C(p) = #{d | 4Cp+1 : d = -1 mod 4C} (FRONTIER 2.1 divisor form), w_C = 1 - C/(X+1) (Fejér-type, nonnegative).
# Test 1: since R_C>=0 and w_C>0, W_X(p)>0 iff some level C<=X has R_C(p)>0. Check this on primes <= 10^5 (X=40).
# Test 2 (signed weights): any functional sum_C w_C R_C(p) vanishes at the 14 census primes (R_C=0 for all C, verified
# up to C=10^6 in the Z2363 sweep), so no identity sum_C w_C R_C(p) >= c>0 for all p can exist with a finite level set.
import math
def primes1mod4(hi):
    s = bytearray([1])*(hi+1); s[0]=s[1]=0
    for i in range(2, int(hi**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [p for p in range(5, hi+1) if s[p] and p % 4 == 1]
def R(C, p):
    m = 4*C; N = m*p+1; cnt = 0; d = m-1
    while d*d <= N:
        if N % d == 0: cnt += 2 if d*d != N else 1   # d and N/d (both are = -1 mod 4C since N = 1 mod 4C)
        d += m
    return cnt
X = 40
w = {C: 1 - C/(X+1) for C in range(1, X+1)}
census = [409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
for q in census:
    assert all(R(C, q) == 0 for C in range(1, 200)), q
print("census primes: R_C(p)=0 for all C<200 (checked):", len(census))
zero = []; mism = 0; tot = 0
for p in primes1mod4(100000):
    Ws = sum(w[C]*R(C, p) for C in range(1, X+1))
    lev = any(R(C, p) > 0 for C in range(1, X+1))
    tot += 1
    if (Ws > 0) != lev: mism += 1
    if Ws == 0: zero.append(p)
print(f"primes = 1 mod 4 <= 1e5: {tot}; W_X>0 vs 'some level<=X': mismatches = {mism}")
print(f"zeros of W_X (no level <= {X}): {len(zero)}; largest few: {zero[-6:]}")
print("min W_X over primes with W>0 (relative to sum of w):", min(sum(w[C]*R(C,p) for C in range(1,X+1)) for p in primes1mod4(100000) if p not in zero))
