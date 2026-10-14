r"""s4_sail: Lambda_A = {(x,y): x = A y mod p}. Positive vectors (c,s) in Lambda_A with cs | p+c+s are exactly the
length-3 words (c, m, s), m = (p+c+s)/(cs), with A = c/s mod p ((J)39 Lemma 1.1 in lattice form).
Test: does the Gauss(Lagrange)-reduced basis of Lambda_A (Minkowski minima; sign-blind) ever produce the words?
For each prime p = 1 mod 8 <= P: fraction of QNR A whose reduced basis +-b1, +-b2, +-(b1+-b2) contains a positive
word vector; and primes where NO QNR A has one.  usage: s4_sail.py P"""
import sys
from sympy import primerange, legendre_symbol as leg

def gauss(b1, b2):
    n = lambda v: v[0] * v[0] + v[1] * v[1]
    dot = lambda a, b: a[0] * b[0] + a[1] * b[1]
    while True:
        if n(b2) < n(b1): b1, b2 = b2, b1
        mu = round(dot(b1, b2) / n(b1))
        if mu == 0: return b1, b2
        b2 = (b2[0] - mu * b1[0], b2[1] - mu * b1[1])

P = int(sys.argv[1]); hit = tot = 0; bad = []; sign_pos = 0
for p in primerange(9, P):
    if p % 8 != 1: continue
    anyhit = False
    for A in range(2, p):
        if leg(A, p) != -1: continue
        b1, b2 = gauss((p, 0), (A, 1))
        cands = [b1, b2, (b1[0] + b2[0], b1[1] + b2[1]), (b1[0] - b2[0], b1[1] - b2[1])]
        sign_pos += b1[0] * b1[1] > 0
        ok = False
        for x, y in cands:
            if x * y < 0: continue
            c, s = abs(x), abs(y)
            if c and s and (p + c + s) % (c * s) == 0: ok = True
        tot += 1; hit += ok; anyhit |= ok
    if not anyhit: bad.append(p)
print(f"QNR pairs {tot}: reduced-basis word {hit} ({hit/tot:.4f}); shortest vector in positive quadrant {sign_pos/tot:.3f}")
print("primes p=1(8) with no QNR A whose reduced basis is a word:", len(bad), bad[:15])
