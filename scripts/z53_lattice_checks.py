"""z53 LATTICE: numeric checks for Z53_LATTICE.md.
(1) grid check of R-1 >= (a^2+b^2)/2 (Lemma 2.4); (2) constants c0, D1, n0 of Theorem 2.6;
(3) binomial tail for the Thue-angle count at the 14 (*)-zero primes (Sec. 6)."""
import numpy as np, math
a = np.linspace(-0.999, 0.999, 1999); A, B = np.meshgrid(a, a)
R = (1 + A*B) / ((1 - A**2) * (1 - B**2))
print('Lemma 2.4 grid: min (R-1)-(a^2+b^2)/2 =', ((R - 1) - (A**2 + B**2)/2).min())
c0 = 64 * 3**(4/3); print('c0 =', c0)
lam = lambda s: math.log((1 + s)/(1 - s)); print('lambda(1/2)/(1/2) =', lam(0.5)/0.5, '<= 8/3')
f = lambda D: D**(1/3) - (c0/4) * math.log(9*D)**2
lo, hi = 1e10, 1e18
for _ in range(200):
    mid = math.sqrt(lo*hi)
    if f(mid) > 0: hi = mid
    else: lo = mid
print('case D>n/17: D1 = %.4g, n < 17*D1 = %.4g' % (hi, 17*hi))
for n in [2.5e8, 2.6e8]:
    D = n/17; print('case D<=n/17 at n=%.3g possible?' % n, D + (128/9)*c0*D**(2/3) >= n)
p = math.atan(0.16)/(math.pi/4)
tail = sum(math.comb(14, k) * p**k * (1-p)**(14-k) for k in range(6, 15))
print('P(b/a<0.16)=%.4f, P(>=6 of 14)=%.4f' % (p, tail))
