# z53_thin15_check.py — independent exact checker for the certificates of z53_thin15_solve.py.
# Each line "t m d1 d2": n = 15*2^(60t)+1, x = (n+m)/4, N = n*x, k = (d1+d2)/m, y = N*k/d1, z = N*k/d2.
# Structural checks (a complete proof, Z53_THIN15.md §5): m = 3 (mod 4) so 4x = n + m with x an integer; d1 | x and
# d2 | x (so y, z are integers); m | d1 + d2.  Then 1/y + 1/z = (d1+d2)/(N k) = m/N and 1/x + m/(n x) = 4/n.
# In addition, for t <= FULL the product identity 4xyz = n(xy+yz+zx) is checked literally.
# Prints progress; exits nonzero on any failure or any gap in t.   Usage: z53_thin15_check.py certfile [FULL]
import sys
from gmpy2 import mpz
FULL = int(sys.argv[2]) if len(sys.argv) > 2 else 10000
ts = []; bad = 0; nfull = 0
for line in open(sys.argv[1]):
    w = line.split()
    if not w or w[0].startswith('#'): continue
    t = int(w[0])
    if w[1] == 'NONE': print('NO CERT', t); bad += 1; continue
    m, d1, d2 = int(w[1]), mpz(w[2]), mpz(w[3])
    n = 15 * (mpz(1) << (60 * t)) + 1
    ok = m > 0 and m % 4 == 3 and (n + m) % 4 == 0 and d1 > 0 and d2 > 0
    x = (n + m) // 4
    ok = ok and x % d1 == 0 and x % d2 == 0 and (d1 + d2) % m == 0
    if ok and t <= FULL:
        N = n * x; k = (d1 + d2) // m
        y = N * k // d1; z = N * k // d2
        ok = 4 * x * y * z == n * (x * y + y * z + z * x); nfull += 1
    if not ok: print('FAIL', t, flush=True); bad += 1
    ts.append(t)
    if len(ts) % 2000 == 0: print('.. %d checked (last t=%d), failures %d' % (len(ts), t, bad), flush=True)
s = set(ts); gaps = [t for t in range(min(ts), max(ts) + 1) if t not in s]
print('checked %d certificates, t = %d..%d (s = 60t up to %d), product identity literally checked for %d, failures %d, gaps %d'
      % (len(ts), min(ts), max(ts), 60 * max(ts), nfull, bad, len(gaps)))
sys.exit(1 if bad or gaps else 0)
