"""Numerical check of Theorem C: G = Z/m, k copies of the generator 1 (budget 1), target m/2.
Exact hit count by polynomial convolution; bounded-order |c| vs the bound (ρ_B/3)^k; c(χ_1) vs 1 − 4π²k/(3m²);
image size 2k+1 (k = m/2 − 1 gives every residue except m/2)."""
import numpy as np
for m, k in [(40, 19), (100, 49), (400, 60), (400, 199)]:
    r = np.arange(m); sgn = np.where(r % 2 == 0, 1, -1)
    with np.errstate(over='ignore'):
        c = -sgn * ((1 + 2 * np.cos(2 * np.pi * r / m)) / 3) ** k
    poly = np.array([1], dtype=object)
    for _ in range(k): poly = np.convolve(poly, np.array([1, 1, 1], dtype=object))
    vals = np.arange(-k, k + 1)
    hit = sum(poly[i] for i in range(len(vals)) if vals[i] % m == m // 2)
    image = len({v % m for v in vals})
    order = m // np.gcd(r, m)
    out = [f'm={m} k={k} hits(m/2)={hit} image={image}/{m}']
    for B in (2, 6, 12):
        msk = (order <= B) & (r != 0)
        out.append(f'B={B}: max|c|={np.abs(c[msk]).max():.3g} bound={(max(1, 1 + 2 * np.cos(2 * np.pi / B)) / 3) ** k:.3g}')
    out.append(f'c(chi_1)={c[1]:.4f} ≥ {1 - 4 * np.pi ** 2 * k / (3 * m * m):.4f}; sum_(r≠0) c = {c[1:].sum():.6f}')
    print('; '.join(out))
