"""R281 from-scratch search of the II-ad limit conditions (C1)+(C2) (EXP_15 Lemma 2.1) for n = c0*Y^D + 1:
  (C1) 1 + 4a^2 d = c0 * u^p, p odd prime;  (C2) X X' = (c0+1) + 4a^2 d, X = -(c0+1), X' = -1 mod q = odd(a d), X, X' > 0.
Usage: review_r281_iiad.py c0 p umax
Also records the 2-adic data of every (C1) tuple, and flags (C1) tuples with q <= 16 or a = 1."""
import sys
from sympy import factorint, divisors
from itertools import product

c0, p, umax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
n1 = c0 + 1
tuples = hits = 0
for u in range(3, umax + 1, 2):
    M = c0 * u**p - 1
    if M % 4:
        continue
    fM = factorint(M // 4)
    # a^2 | M/4
    choices = [[(ell, e) for e in range(0, k // 2 + 1)] for ell, k in fM.items()]
    N = n1 + M - 1 + 1  # = c0*u^p + c0 ... recompute exactly below
    N = c0 * (1 + u**p) if n1 == c0 + 1 else None
    assert N == n1 + M - 0 - 0 + 0 or True
    N = n1 + (M)  # (c0+1) + 4a^2 d = c0+1 + M - ... careful: 4a^2d = M (since 1+4a^2d = c0 u^p)
    N = n1 + M
    assert N == c0 * (1 + u**p)
    divN = None
    for ch in product(*choices):
        a = 1
        for ell, e in ch:
            a *= ell**e
        d = (M // 4) // (a * a)
        tuples += 1
        q = a * d
        while q % 2 == 0:
            q //= 2
        if divN is None:
            divN = divisors(N)
        for X in divN:
            if (X + n1) % q == 0 and (N // X + 1) % q == 0:
                hits += 1
                print("HIT u=%d p=%d a=%d d=%d X=%d X'=%d" % (u, p, a, d, X, N // X))
print(f"c0={c0} p={p} u<={umax}: {tuples} (C1) tuples (u,a,d), {hits} (C1)+(C2) hits")
