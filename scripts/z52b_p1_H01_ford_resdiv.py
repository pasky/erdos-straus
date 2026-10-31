"""z52b pass1 H01 (Z0231): Ford-type count of integers with a divisor in a residue class.
For m = 4C and n <= x, n = 1 (mod m) (the shape of N = 4Cp + 1), let F_m(x) = fraction of such n with NO divisor
d = -1 (mod m), d <= sqrt(n). Prints F_m at x = 1e5..1e8 and the local slope of log F vs log log x.
Usage: z52b_p1_H01_ford_resdiv.py XMAX"""
import sys, math
import numpy as np
XMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
xs = [10**k for k in range(4, 20) if 10**k <= XMAX]
print('m   ' + '  '.join('F(1e%d)' % round(math.log10(x)) for x in xs) + '   slopes dlogF/dloglogx')
for C in (1, 2, 3, 4, 5, 6, 8, 10, 15, 25):
    m = 4 * C
    K = XMAX // m + 1                       # n = m*k + 1, k = 0..K-1
    has = np.zeros(K, dtype=bool)
    d = m - 1
    while d * d <= XMAX:
        # n = 0 (mod d), n = 1 (mod m), n >= d^2 ; gcd(d, m) = 1
        k0 = (-pow(m, -1, d)) % d           # m*k + 1 = 0 (mod d)
        kmin = (d * d - 1 + m - 1) // m
        if k0 < kmin:
            k0 += ((kmin - k0 + d - 1) // d) * d
        has[k0::d] = True
        d += m
    Fs = []
    for x in xs:
        kx = (x - 1) // m                   # k = 1..kx  <=>  1 < n <= x
        Fs.append(1 - has[1:kx + 1].mean())
    sl = [(math.log(Fs[i + 1]) - math.log(Fs[i])) / (math.log(math.log(xs[i + 1])) - math.log(math.log(xs[i])))
          for i in range(len(xs) - 1)]
    print('%3d ' % m + '  '.join('%.4f' % f for f in Fs) + '   ' + ' '.join('%.2f' % s for s in sl))
