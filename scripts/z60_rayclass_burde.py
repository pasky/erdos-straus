"""z60 RAYCLASS §4: do class data of TWO imaginary quadratic orders jointly see a non-quadratic (quartic) residue character?
Test: K1 = Q(sqrt-17) (Cl = Z/4, H1 = Hilbert class field, Gal(H1/Q) = D4, genus field Q(i, sqrt17));
      O2 = Z[17i] in K2 = Q(i) (Cl(-1156) = Z/8); L2' = D4-subfield (classes mod the order-2 subgroup).
q splits completely in H1      <=> q = x^2 + 17 y^2           (principal form of disc -68)
q splits completely in L2'     <=> q rep. by [1,0,289] or [2,2,145] (the subgroup of order 2 of Cl(-1156))
Prediction from the fibre-product lemma (§4): the compositum contains a cyclic quartic field; then the q splitting
completely in both have a constant quartic character. Print the distribution of q mod 17 (and mod 68) for such q,
versus q splitting completely in H1 only."""
import math
from collections import Counter
N = 2_000_000
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
def rep(q, a, b, c):
    # does a x^2 + b x y + c y^2 represent q (positive definite)?  brute force over y
    D = b * b - 4 * a * c
    ymax = int(math.isqrt(4 * a * q // (-D))) + 1
    for y in range(-ymax, ymax + 1):
        # a x^2 + b y x + (c y^2 - q) = 0
        disc = (b * y) ** 2 - 4 * a * (c * y * y - q)
        if disc < 0: continue
        s = math.isqrt(disc)
        if s * s != disc: continue
        for sg in (s, -s):
            num = -b * y + sg
            if num % (2 * a) == 0: return True
    return False
QR4 = {pow(x, 4, 17) for x in range(1, 17)}
both, h1only = Counter(), Counter()
for q in range(3, N + 1):
    if not sieve[q] or q in (2, 17): continue
    if not rep(q, 1, 0, 17): continue
    if rep(q, 1, 0, 289) or rep(q, 2, 2, 145): both[q % 17] += 1
    else: h1only[q % 17] += 1
print("quartic residues mod 17:", sorted(QR4))
print("q split completely in H1 and L2' : q mod 17 ->", dict(sorted(both.items())))
print("q split completely in H1, not L2': q mod 17 ->", dict(sorted(h1only.items())))
