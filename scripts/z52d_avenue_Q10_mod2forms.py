"""z52d avenue Q10 (Z2527): is R(p)/2 mod 2 (primes p ≡ 1 (4), p ≤ 3·10⁵) an F_2-linear combination of
coefficients of level-1 modular forms mod 2? (Nicolas–Serre: these are polynomials in Δ ≡ Σ_{m odd} q^{m²} mod 2;
Δ^k = ∏_{2^i ∥ bits of k} Δ(q^{2^i}) mod 2, and its q^n coefficient vanishes unless n ≡ k (mod 8).)
Run: timeout 60 python3 scripts/z52d_avenue_Q10_mod2forms.py"""
import numpy as np
from numpy.fft import rfft, irfft
N = 300000
R = np.zeros(N + 1, dtype=np.int64)
u = 1
while 3 * u - 1 <= N:
    B = 1
    while 4 * u * B - u - B <= N:
        R[4 * u * B - u - B::4 * u * B] += 1; B += 1
    u += 1
s = np.ones(N + 1, bool); s[:2] = 0
for i in range(2, int(N ** .5) + 1):
    if s[i]: s[i * i::i] = 0
L = 1 << (2 * N + 2).bit_length()
def delta_scaled(e):  # Δ(q^e) mod 2
    a = np.zeros(N + 1); m = 1
    while e * m * m <= N: a[e * m * m] = 1; m += 2
    return a
def mul2(a, b): return np.rint(irfft(rfft(a, L) * rfft(b, L), L)[:N + 1]) % 2
def delta_pow(k):
    out = None; i = 0
    while k:
        if k & 1:
            d = delta_scaled(1 << i); out = d if out is None else mul2(out, d)
        k >>= 1; i += 1
    return out
for r in (1, 5):
    ps = [p for p in np.nonzero(s)[0] if p % 8 == r]
    ks = [k for k in range(1, 64) if k % 8 == r]
    D = [delta_pow(k) for k in ks]
    M = np.array([[int(d[p]) for d in D] for p in ps], dtype=np.uint8)
    y = np.array([(R[p] // 2) % 2 for p in ps], dtype=np.uint8)
    # Gaussian elimination over F_2 on [M | y]
    A = np.concatenate([M, y[:, None]], 1); row = 0
    for c in range(M.shape[1]):
        piv = np.nonzero(A[row:, c])[0]
        if len(piv) == 0: continue
        pr = row + piv[0]; A[[row, pr]] = A[[pr, row]]
        others = np.nonzero(A[:, c])[0]; others = others[others != row]
        A[others] ^= A[row]; row += 1
        if row == A.shape[0]: break
    inconsistent = int(np.any((A[:, :-1].sum(1) == 0) & (A[:, -1] == 1)))
    print(f'p ≡ {r} (8): {len(ps)} primes, Δ^k with k in {ks}: rank {row}, R/2 mod 2 in F_2-span? {not inconsistent}')
