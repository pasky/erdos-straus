"""Opus review (z77): brute large-shift P data (e >= 2^j) vs z77_routes / z77_pfine bucket bounds at small n."""
import sys, inspect; sys.path.insert(0, 'scripts')
import z77_pfine, z77_routes
from math import isqrt
src = inspect.getsource(z77_pfine.refine).replace(
    "    return min((pooled(n,j)", "    return buckets\n    return min((pooled(n,j)")
ns = dict(vars(z77_pfine)); exec(src, ns); fbuckets = ns['refine']

def large_data(N, j):
    # all in-cell P data with a<=b and e >= 2^j: acd <= (N/2^j+1)/2
    T = (N // (1 << j) + 1) // 2; out = 0; boxes = set(); r = None
    for a in range(1, T + 1):
        for c in range(1, T // a + 1):
            for d in range(1, T // (a * c) + 1):
                f = 4 * a * c * d - 1
                if (N * c + a) % f: continue
                b = (N * c + a) // f
                if b < a or (a + b) % c: continue
                e = (a + b) // c
                if 4 * a * b * d != N + e or e < (1 << j): continue
                out += 1
    return out

if __name__ == '__main__':
    r, K, b = map(int, sys.argv[1:4])
    N = r ** K; n = 1 << b; assert n // 2 < N <= n
    rb = z77_routes.routes(n); fb = fbuckets(n)
    for j in range(b // 3 - 3, b // 2 + 1):
        print(j, large_data(N, j), 'routes', rb[j] if j < len(rb) else None, 'fine', fb[j], flush=True)
