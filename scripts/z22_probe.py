"""probe the hard primes with no cap-0 among their first 10 forced windows: all forced prime windows q <= QM."""
import sys
from sympy import primerange, factorint
from z22_common import best_cap, verify
QM = int(sys.argv[1])
for p in map(int, sys.argv[2:]):
    forced = [q for q in primerange(3, QM) if q % 4 == 3 and pow(p, (q - 1) // 2, q) == q - 1]
    res = []
    for i, q in enumerate(forced):
        c = best_cap(p, q, 3, fK=factorint((p + q) // 4))
        res.append((q, None if c is None else c[0]))
        if c is not None and c[0] == 0:
            verify(p, q, c[1], 0); break
    m0 = next(m for m in range(3, 10 ** 6, 4) if (c := best_cap(p, m, 0)) is not None)
    print(p, 'forced windows tried', len(res), 'first cap-0 forced window', res[-1] if res[-1][1] == 0 else None,
          'caps', [r[1] for r in res[:12]], 'least cap-0 window (any m)', m0)
