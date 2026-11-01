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
tail = float('nan')  # superseded by the computed count below (review M5)
print('P(b/a<0.16)=%.4f' % p)

# --- review repairs (R1): thresholds for the (V2) covering and (V3) Minkowski forms, K in (0,inf)^3 ---
def root(g, lo=1.0, hi=1e30):
    # largest D with g(D) <= 0, assuming g<0 then >0 (bisection on log scale from a point where g>0)
    for _ in range(400):
        mid = math.sqrt(lo*hi)
        if g(mid) > 0: hi = mid
        else: lo = mid
    return hi
g1 = lambda D: D**(1/3) - (c0/4)*math.log(9*D)**2
print('V1 thick: D1 = %.6g (exact c0/4), n < %.4g' % (root(g1, 1e10), 17*root(g1, 1e10)))
g2 = lambda D: D**(1/3) - c0*((1+math.log(9*D))**2/2 + 9*(1+math.log(9*D)))
D2 = root(g2, 1e10); print('V2 thick (integer-point count): D2 = %.4g, n < %.4g' % (D2, 17*D2))
g3 = lambda D: 8*D**(4/3)/c0 - (10/3)*(18*D+1)
D3 = root(g3, 1.0, 1e20); print('V3 thick (Minkowski box): D3 = %.4g, n < %.4g' % (D3, 17*D3))
# monotonicity check of D^(1/3)/log^2(9D) beyond the root
xs = np.logspace(10, 20, 2000); ys = xs**(1/3)/np.log(9*xs)**2
print('D^(1/3)/log^2(9D) increasing on [1e10,1e20]:', bool(np.all(np.diff(ys) > 0)))

# --- review repair (M5): Thue angle count at the 14 (*)-zero primes computed, not hard-coded ---
zeros = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
def ba(p):
    a = math.isqrt(p)
    while 2*a*a >= p:
        b2 = p - a*a; b = math.isqrt(b2)
        if b*b == b2: return b/a
        a -= 1
    return None
r = [ba(p) for p in zeros]; k = sum(x < 0.16 for x in r)
print('b/a at zeros:', ['%.4f' % x for x in r])
print('count b/a<0.16: %d of 14; P(Bin(14,%.4f) >= %d) = %.4f' % (k, p, k, sum(math.comb(14, j)*p**j*(1-p)**(14-j) for j in range(k, 15))))
