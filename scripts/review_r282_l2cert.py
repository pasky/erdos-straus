"""R282 from-scratch: SPARKS9 Lemma 3.1 on random data over G = Z/m and Z/m1 x Z/m2 (characters via FFT).
Certificate value c(g0) = S/|G| - |G|^-1 sqrt(|G|-1) sqrt(sum_{psi != 1}|nhat|^2); check: (i) c(g0) <= n(g0) always;
(ii) c > 0 iff S^2 > (|G|-1) Q iff mbar^2 > (|G|-1) V; (iii) c>0 => min n > 0."""
import numpy as np
rng = np.random.default_rng(282); bad = 0; pos = 0
for trial in range(20000):
    shape = (int(rng.integers(2, 30)),) if trial % 2 else (int(rng.integers(2, 8)), int(rng.integers(2, 8)))
    G = int(np.prod(shape)); lam = rng.choice([0.5, 3, 30, 300])
    n = rng.poisson(lam, size=shape).astype(float)
    if trial % 3 == 0: n = np.full(shape, lam) + rng.normal(0, rng.choice([0.01, 0.1, 1]), size=shape).clip(-lam, None)
    nh = np.fft.fftn(n); S = n.sum(); Q = (n**2).sum()
    E2 = (np.abs(nh)**2).sum() - S**2
    assert abs((np.abs(nh)**2).sum() - G*Q) < 1e-6*max(1, G*Q)
    c = S/G - np.sqrt(G-1)*np.sqrt(max(E2, 0))/G
    mbar = S/G; V = Q/G - mbar**2
    if np.any(c > n + 1e-9): bad += 1; print('lowerbound', shape, c, n.min())
    crit1 = S**2 > (G-1)*Q; crit2 = mbar**2 > (G-1)*V
    if (c > 1e-12) != crit1 or crit1 != crit2: 
        if abs(S**2 - (G-1)*Q) > 1e-6*S**2: bad += 1; print('crit', shape, c, S**2, (G-1)*Q, crit2)
    if c > 1e-9:  # c = 0 up to roundoff is the boundary case S^2 = (|G|-1)Q
        pos += 1
        if n.min() <= 0: bad += 1; print('zero', shape, c, n.min())
print(f"trials=20000, certificate positive in {pos}, violations={bad}")
