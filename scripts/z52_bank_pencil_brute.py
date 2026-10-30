"""Independent brute force for S_{n,k}(N): x<=y<=z, n/4 < x <= 3n/4, y in [x, Y(x)], z from the linear equation.
Y(x): from 4/n - 1/x = 1/y + 1/z + k/(nxyz) with z >= y: for k>0, (4x-n)/(nx) > 1/y  => no upper bound from that side;
we use the other side: (4x-n)/(nx) <= 2/y + k/(n x y^2) => y <= (2nx + sqrt(4n^2x^2 + 4k(4x-n)x... )) conservative:
we simply loop y while (4x-n)*y*y <= 2*n*x*y + |k| + n*x  (a safe over-estimate)."""
import sys
def count(n, k):
    c = 0
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        m = 4 * x - n
        if m <= 0: continue
        y = x
        while m * y * y <= 2 * n * x * y + abs(k) + n * x:
            den = m * y - n * x          # z*(m*y - n*x) = n*x*y + k
            num = n * x * y + k
            if den > 0 and num % den == 0:
                z = num // den
                if z >= y:
                    assert 4*x*y*z - n*(x*y+y*z+z*x) == k
                    c += 1
            y += 1
    return c
k = int(sys.argv[1]); lo, hi = int(sys.argv[2]), int(sys.argv[3])
for n in range(lo, hi + 1):
    print(n, count(n, k))
