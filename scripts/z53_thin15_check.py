# z53_thin15_check.py — independent exact checker for the certificates of z53_thin15_solve.py.
# Each line "t m d1 d2": n = 15*2^(60t)+1, x = (n+m)/4, N = n*x, k = (d1+d2)/m, y = N*k/d1, z = N*k/d2.
# Checks: m = 3 (mod 4) so x is an integer, d1 | x and d2 | x (so d1, d2 | N), m | d1+d2, and 4xyz = n(xy+yz+zx).
# Prints the covered range and exits nonzero on any failure or any gap in t.
# Usage: z53_thin15_check.py certfile
import sys
from gmpy2 import mpz
ts = []; bad = 0
for line in open(sys.argv[1]):
    w = line.split()
    if not w or w[0].startswith('#'): continue
    t = int(w[0])
    if w[1] == 'NONE': print('NO CERT', t); bad += 1; continue
    m, d1, d2 = int(w[1]), mpz(w[2]), mpz(w[3])
    n = 15 * (mpz(1) << (60 * t)) + 1
    ok = (n + m) % 4 == 0 and m > 0
    x = (n + m) // 4
    ok = ok and x % d1 == 0 and x % d2 == 0 and (d1 + d2) % m == 0
    if ok:
        N = n * x; k = (d1 + d2) // m
        ok = (N * k) % d1 == 0 and (N * k) % d2 == 0
        y = N * k // d1; z = N * k // d2
        ok = ok and x > 0 and y > 0 and z > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)
    if not ok: print('FAIL', t); bad += 1
    ts.append(t)
ts.sort()
gaps = [t for t in range(ts[0], ts[-1] + 1) if t not in set(ts)]
print('checked %d certificates, t = %d..%d (s = 60t up to %d), failures %d, gaps %d' %
      (len(ts), ts[0], ts[-1], 60 * ts[-1], bad, len(gaps)))
sys.exit(1 if bad or gaps else 0)
