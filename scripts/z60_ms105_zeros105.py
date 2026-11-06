# z60 MS105: list the non-square R-zeros n = 1 (4) <= 1e10 with gcd(n,105)=1 (from z58 LOGIC census), with
# squarefree kernel s and square part m^2.  Output: n s m factorization
import gzip, math, sys
from sympy import factorint
out = []
for line in gzip.open('data/z58/logic/zeros_1e10.txt.gz', 'rt'):
    n = int(line.split()[0])
    if n % 4 != 1 or math.gcd(n, 105) != 1: continue
    r = math.isqrt(n)
    if r * r == n: continue
    f = factorint(n)
    s = 1; m = 1
    for p, e in f.items():
        s *= p ** (e % 2); m *= p ** (e // 2)
    out.append((n, s, m, f))
for n, s, m, f in out:
    print(n, s, m, '*'.join(f'{p}^{e}' if e > 1 else str(p) for p, e in sorted(f.items())))
print('# count', len(out), file=sys.stderr)
