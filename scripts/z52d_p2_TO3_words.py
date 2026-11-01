"""Pass-2 TO3: word-census checks (Z0753-Z0776, Z0755-Z0771, Z0780, Z0766, Z0770, Z0755 squares).
Regenerate the census first:  gcc -O2 -o /tmp/z52/words scripts/z52b_fingerprint_words.c && /tmp/z52/words 3000000 > /tmp/z52/words3e6.txt
Columns: n W I3 R Uv ESC T1 T2.  Usage: uv run --with numpy python scripts/z52d_p2_TO3_words.py [/tmp/z52/words3e6.txt]"""
import sys
import numpy as np
fn = sys.argv[1] if len(sys.argv) > 1 else '/tmp/z52/words3e6.txt'
W = np.loadtxt(fn, dtype=np.int64)
n = W[:, 0]; Wd = W[:, 1]; I3 = W[:, 2]; R = W[:, 3]; Uv = W[:, 4]; ESC = W[:, 5]
isq = lambda x: np.floor(np.sqrt(x)) ** 2 == x
I3z = n[I3 == 0]
print('I3 zeros', len(I3z), 'max', int(I3z.max()), '| odd >50:', [int(x) for x in I3z if x % 2 and x > 50])
print('I3 zero squares', [int(x) for x in I3z if isq(x)])
print('I3 zero primes', [int(x) for x in n[(I3 == 0)] if x > 1 and all(x % d for d in range(2, int(x ** .5) + 1))])
print('ESC zeros non-square', [int(x) for x in n[(ESC == 0) & ~isq(n)]])
print('R zeros 2^k-1', {k: int(R[2 ** k - 2]) for k in range(2, 22)})
print('I3=1 beyond 1000', [int(x) for x in n[(I3 == 1) & (n > 1000)]])
print('Uv zeros odd nonsq 1 mod 4 (U-failure proxy)', [int(x) for x in n[(Uv == 0) & (n % 4 == 1) & ~isq(n)]])
print('at 1560^2,35^2,105: I3,R,Uv,ESC =', [(int(k), int(I3[k - 1]), int(R[k - 1]), int(Uv[k - 1]), int(ESC[k - 1])) for k in (2433600, 1225, 105)])
for r in range(8):
    m = (n % 8 == r) & (n % 2 == 1) & ~isq(n)
    if m.sum(): print('odd non-square n = %d mod 8: R=0 frac %.5f, Uv=0 frac %.5f' % (r, (R[m] == 0).mean(), (Uv[m] == 0).mean()))
print('R=0 incl. odd squares, n = 1 mod 8:', float((R[(n % 8 == 1)] == 0).mean()))
sq = np.arange(1, 1733) ** 2; ratio = I3[sq - 1]
for d in (4, 12, 60):
    sel = np.arange(1, 1733) % d == 0
    print('m divisible by %d: mean I3(m^2)=%.2f, zeros %d of %d' % (d, ratio[sel].mean(), (ratio[sel] == 0).sum(), sel.sum()))
