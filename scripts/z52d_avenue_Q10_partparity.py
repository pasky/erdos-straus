"""z52d avenue Q10 (Z0915): null test — partition parity p(n) mod 2 at primes vs the (★) count R(p).
p(n) mod 2 from 1/∏(1-q^k) = 1/Σ(-1)^k q^{k(3k-1)/2}, inverted mod 2 by Newton iteration with exact FFT products.
Run: timeout 60 python3 scripts/z52d_avenue_Q10_partparity.py"""
import numpy as np
from numpy.fft import rfft, irfft
N = 300000
R = np.zeros(N + 1)
u = 1
while 3 * u - 1 <= N:
    B = 1
    while 4 * u * B - u - B <= N:
        R[4 * u * B - u - B::4 * u * B] += 1; B += 1
    u += 1
f = np.zeros(N + 1)
k = 0
while True:
    done = True
    for j in (k, -k):
        e = j * (3 * j - 1) // 2
        if e <= N: f[e] = 1; done = False
    if done and k > 0: break
    k += 1
def mul(a, b, n):
    L = 1 << (2 * n).bit_length()
    return np.rint(irfft(rfft(a[:n], L) * rfft(b[:n], L), L)[:n]) % 2
g = np.array([1.0]); n = 1
while n < N + 1:
    n = min(2 * n, N + 1)
    gg = np.zeros(n); gg[:len(g)] = g
    fg = mul(f, gg, n)            # mod 2: g <- g*(2 - f g) = g*f*g  (since -1 = 1)
    g = mul(gg, fg, n)
g = g.astype(int)
assert list(g[:12]) == [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # p(n) = 1,1,2,3,5,7,11,15,22,30,42,56
s = np.ones(N + 1, bool); s[:2] = 0
for i in range(2, int(N ** .5) + 1):
    if s[i]: s[i * i::i] = 0
ps = np.array([p for p in np.nonzero(s)[0] if p % 4 == 1 and p > 1000])
y = R[ps] / np.log(ps) ** 2
par = g[ps]
print('primes', len(ps), 'frac p(p) odd %.3f' % par.mean())
print('mean R/log²p | p(p) even %.4f, odd %.4f' % (y[par == 0].mean(), y[par == 1].mean()))
print('corr(p(p) mod 2, R/log²p) = %.4f ; agreement with R/2 mod 2: %.3f' % (np.corrcoef(par, y)[0, 1], (par == (R[ps] // 2) % 2).mean()))
