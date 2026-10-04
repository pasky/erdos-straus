"""Reviewer check for EXCEPTIONAL_INTERFREQ (Thm 2.2 / Lemma 2.4 / hybrid scope).

Builds Selberg's minorant F of 1_[1/2, N+1/2] with Fourier support [-2/N, 2/N]
(D = N/2) from Beurling's function B, and reports
  * sum_n F(n)  (should be N - D),  min F on [1,N],  max F outside,
  * max over classes b mod d, d > N/2, of G - 1 - N/(2d), where
    G(b,d) = sum_{n = b (d)} (1_[1,N] - F)(n)  (split d in (N/2,N] / d > N).
Run: uv run --with scipy python reviews/exceptional-interfreq-review-check.py 20 50
Memory: arrays of 8000N+1 doubles (N <= 100: < 100 MB).
"""
import sys
import numpy as np
from scipy.special import polygamma


def B(z):
    z = np.asarray(z, float)
    return (np.sin(np.pi * z) / np.pi) ** 2 * (polygamma(1, -z) - polygamma(1, z + 1) + 2 / z)


def minorant(x, a, b, delta):
    return -0.5 * (B(delta * (a - x)) + B(delta * (x - b)))


for N in map(int, sys.argv[1:] or ["20", "50"]):
    assert N % 2 == 0  # keeps delta*(n - 1/2) off the integers
    D = N / 2
    n = np.arange(-4000 * N, 4000 * N + 1)
    F = minorant(n, 0.5, N + 0.5, 1 / D)
    inside = (n >= 1) & (n <= N)
    g = inside.astype(float) - F
    print(f"N={N}: sum F={F.sum():.5f} (N-D={N-D}), min F on [1,N]={F[inside].min():.4f}, "
          f"max F outside={F[~inside].max():.2e}")
    for lo, hi in [(N // 2 + 1, N + 1), (N + 1, 40 * N)]:
        w, arg = -1e9, None
        for d in range(lo, hi):
            G = np.bincount(np.mod(n, d), weights=g, minlength=d)
            ex = G - 1 - N / (2 * d)
            i = int(ex.argmax())
            if ex[i] > w:
                w, arg = ex[i], (d, i, G[i])
        print(f"   d in [{lo},{hi}): max G-1-N/(2d) = {w:.4f} at (d,b,G)={arg}")
