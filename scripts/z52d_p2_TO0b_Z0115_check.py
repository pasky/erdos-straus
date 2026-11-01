"""z52d pass2 TO0b Z0115: premise check 'denominators = 1 mod 3 is impossible when 3 does not divide n'.
Search 4/n = sum of 4 unit fractions (x<=y<=z<=w) all = 1 mod 3, for n = 1 mod 3 and n = 2 mod 3, 3 not| n, n <= 200.
Bounded DFS: first denominator x <= 4n (x ≡ 1 mod 3), then 3-term completion with the same congruence (brute over y).
Also the mod-3 bookkeeping: sum of k terms ≡ k (mod 3) at 3-adic level, so k ≡ n (mod 3) is necessary (4/n ≡ 1/n ≡ n mod 3)."""
from fractions import Fraction as Fr
def three_terms_1mod3(r, lo):
    """find y,z (>=lo, both ≡1 mod 3, y<=z) with r = 1/y+1/z (r>0 Fraction)"""
    if r <= 0: return None
    for y in range(max(lo, int(1 / r) + 1), int(2 / r) + 2):
        if y % 3 != 1: continue
        r2 = r - Fr(1, y)
        if r2 > 0 and r2.numerator == 1 and r2.denominator % 3 == 1 and r2.denominator >= y:
            return (y, r2.denominator)
    return None
def four_terms(n):
    r = Fr(4, n)
    for x in range(max(1, int(1 / r) + 1), 4 * n + 1):
        if x % 3 != 1: continue
        r1 = r - Fr(1, x)
        if r1 <= 0: continue
        # need 3 more terms, all ≡1 mod 3: reuse 3-term search with lower bound x
        for y in range(max(x, int(2 / r1) // 1 if False else x), int(3 / r1) + 2):
            if y % 3 != 1: continue
            r2 = r1 - Fr(1, y)
            if r2 <= 0: continue
            t = three_terms_1mod3(r2, y)
            if t: return (x, y, t[0], t[1])
    return None
hits = []; misses = []
for n in range(2, 201):
    if n % 3 == 0: continue
    if n % 3 == 1 or n % 3 == 2:
        pass
    sol = four_terms(n) if n % 3 == 1 else None
    if n % 3 == 1:
        (hits if sol else misses).append((n, sol))
print('n = 1 mod 3, 3 not| n, n<=200: 4-term all-1-mod-3 solution found for', len(hits), 'of', len(hits) + len(misses))
print('examples:', hits[:6])
print('no solution found (within bounded search) for:', [n for n, s in misses][:20])
print('n = 7 check: 4/7 = 1/4 + 1/7 + 1/7 + 1/28 :', Fr(4, 7) == Fr(1, 4) + Fr(1, 7) + Fr(1, 7) + Fr(1, 28))
