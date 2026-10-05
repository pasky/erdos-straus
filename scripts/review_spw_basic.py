"""R40 from-scratch checks: (a) Lemma 1.3(i) identity, reflection identity;
(b) Fourier pinning criterion 'pinned <=> gcd(k,e) >= e/D' (via rank of profile
constraints vs DFT); (c) Fejer kernel identities/bounds; (d) A*(N)."""
from fractions import Fraction as Fr
from math import gcd, sin, pi
import numpy as np

def frac(x):  # fractional part of a Fraction
    return x - (x.numerator // x.denominator)

def c(b, d, N):
    return sum(1 for n in range(1, N + 1) if (n - b) % d == 0)

# (a)
for N in range(1, 40):
    for d in range(1, 45):
        for b in range(-50, 50):
            assert c(b, d, N) == Fr(N, d) + frac(Fr(-b, d)) - frac(Fr(N - b, d))
for d in range(1, 30):
    for y in range(-60, 60):
        assert frac(Fr(-y - 1, d)) == 1 - Fr(1, d) - frac(Fr(y, d))
print("(a) Lemma 1.3(i) and reflection identity OK")

# (b) pinned frequencies: span of class indicators mod d|e, d<=D, in C^e;
# frequency k is pinned iff DFT vector chi_k lies in that span.
def pinned_set(e, D):
    rows = []
    for d in range(1, D + 1):
        if e % d == 0:
            for b in range(d):
                rows.append([1.0 if x % d == b else 0.0 for x in range(e)])
    A = np.array(rows)
    # orthonormal basis of row space
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    B = Vt[S > 1e-9]
    out = set()
    for k in range(e):
        chi = np.exp(2j * pi * k * np.arange(e) / e)
        res = chi - B.T @ (B @ chi)
        if np.linalg.norm(res) < 1e-7:
            out.add(k)
    return out

for e, D in [(60, 10), (60, 14), (84, 20), (90, 21), (120, 25), (126, 30), (72, 17)]:
    P = pinned_set(e, D)
    Q = {k for k in range(e) if gcd(k, e) * D >= e}  # gcd(0,e)=e
    assert P == Q, (e, D, sorted(P ^ Q))
print("(b) pinning criterion gcd(k,e) >= e/D confirmed on small cases")

# (c) Fejer kernel on Z/e
for e, M in [(630, 5), (2310, 6), (997, 12), (100, 3)]:
    x = np.arange(e)
    K = np.zeros(e)
    for k in range(-M, M + 1):
        K += (1 - abs(k) / (M + 1)) * np.cos(2 * pi * k * x / e)
    K /= e
    assert K.min() > -1e-12 and abs(K.sum() - 1) < 1e-9
    for xx in range(1, e // 2 + 1):
        assert K[xx] <= e / (4 * (M + 1) * xx * xx) + 1e-12
    for a in range(2, e // 2):
        tail = K[a:e - a + 1].sum()  # |t| >= a
        assert tail <= e / (2 * (M + 1) * (a - 1)) + 1e-12
print("(c) Fejer kernel: K>=0, sum 1, pointwise and tail bounds OK")

# (d) A*(N)
for N in range(12, 61, 2):
    D = N // 2
    best = max(Fr(c(b, d, N) * d, N) for d in range(1, D + 1) for b in range(d))
    assert best == Fr(3, 2) - Fr(3, N), (N, best)
print("(d) A*(N) = 3/2 - 3/N for even N in [12,60]")
