"""z52b Pass-1 U03 (Z0940 follow-up): mark all values <= X of the OEIS bilinear families A213340 (5+8t+12k+16kt)
and A213686 (13+20t+24k+32kt), t,k>=0, then density of primes p=1 mod 4 NOT in the union, for X = 10^4..10^7.
Usage: uv run --with numpy python scripts/z52b_p1_U03_bilinear_sieve.py XMAX"""
import sys, numpy as np
X = int(sys.argv[1])
cov = np.zeros(X + 1, bool)
for a, b, c, d in [(5, 8, 12, 16), (13, 20, 24, 32)]:
    for t in range(0, (X - a) // b + 1):
        base = a + b * t; step = c + d * t
        cov[base::step] = True
s = np.ones(X + 1, bool); s[:2] = False
for i in range(2, int(X ** 0.5) + 1):
    if s[i]: s[i*i::i] = False
pr = np.nonzero(s)[0]; pr = pr[pr % 4 == 1]
for Y in [10**4, 10**5, 10**6, 10**7]:
    if Y > X: break
    m = pr <= Y; unc = int((~cov[pr[m]]).sum())
    print(f"Y={Y}: primes 1 mod 4 = {int(m.sum())}, uncovered = {unc}, density {unc/int(m.sum()):.5f}")
