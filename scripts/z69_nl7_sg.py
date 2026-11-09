"""NL7 Prop SG: Sophie-Germain identity words on the quartic curve n = t^4 + 1.
n + (4k^4 - 1) = t^4 + 4k^4 = (t^2 + 2kt + 2k^2)(t^2 - 2kt + 2k^2).
(1) verify the explicit identity  n = 16 s^4 + 1, s ≡ 18 (mod 126):
      (x, y, z) = (4(s^2 - 2s + 2), (4(s^2 + 2s + 2) + 1)/63, 63)   is a U7 word (8 | xy).
(2) for k = 1..6 find all residue classes r mod R = lcm(16, L)*k of even t such that EVERY sampled t ≡ r has a U7
    word with letter L = 4k^4 - 1 (empirical classes of bounded-letter identities), and report whether the class is
    an LC class (n a nonzero square mod 3, 5, 7 for suitable t in the class).
"""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import isprime
from math import gcd

print("(1) identity check, s = 18 + 126 j, j = -40..40")
cnt = npr = 0
ex = []
for j in range(-40, 41):
    s = 18 + 126 * j
    n = 16 * s**4 + 1
    x, y, z = 4 * (s * s - 2 * s + 2), (4 * (s * s + 2 * s + 2) + 1) // 63, 63
    assert (4 * (s * s + 2 * s + 2) + 1) % 63 == 0
    assert x > 0 and y > 0 and x * y * z - x - z == n and (x * y) % 8 == 0, s
    cnt += 1
    if isprime(n):
        npr += 1
        if len(ex) < 6: ex.append((s, n, n % 840))
print(f"   {cnt} values verified; {npr} of them prime; examples (s, n, n mod 840): {ex}")
print("   classes of n mod 840 hit when also 5 | s:", sorted({(16 * (18 + 126 * j)**4 + 1) % 840 for j in range(0, 400) if (18 + 126 * j) % 5 == 0}))

print("(2) empirical bounded-letter identity classes on n = t^4 + 1, t even")
def qr_unit(n, ell):
    return n % ell != 0 and pow(n, (ell - 1) // 2, ell) == 1
for k in range(1, 4):
    L = 4 * k**4 - 1
    R = (16 * L // gcd(16, L)) * k
    good = []
    for r in range(0, R, 2):
        ok = True
        for j in range(1, 13):
            t = r + R * j
            if not words_with_letter(t**4 + 1, L):
                ok = False; break
        if ok:
            good.append(r)
    # LC: class r compatible with n a unit square mod 3,5,7 ?  (t mod 3,5,7 is free unless the prime divides R)
    def lc(r):
        for ell in (3, 5, 7):
            cand = [u for u in range(ell) if qr_unit(u**4 + 1, ell)]
            if R % ell == 0:
                if (r % ell) not in cand: return False
        return True
    lcgood = [r for r in good if lc(r)]
    print(f"   k={k} L={L} R={R}: classes of even t with a letter-L U7 word for all 12 samples: {len(good)} of {R//2}; LC-compatible: {len(lcgood)}  e.g. {lcgood[:8]}")
