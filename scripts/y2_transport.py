"""y2_transport: check (h'/N) = -(2/o)*(2/N)^[edge in B,C]... empirically: tabulate (N mod 8, edge type, (h'/N), (2/o))
where o = odd quiddity opposite the even edge. usage: y2_transport.py X"""
import sys
from collections import Counter
from y2_even_edge import jacobi
X = int(sys.argv[1]); T = Counter()
for m in range(1, X + 3):
    for c in range(1, X + 3):
        if m >= 2 and m * c - c - 1 > X: break
        s = 1
        while True:
            N = m * c * s - c - s
            if N > X or (m == 1 and s > X + 3): break
            if N > 0 and N % 2:
                q = (m * s - 1, c, m, s, c * m - 1)
                ev = [i for i in range(5) if q[i] % 2 == 0]
                i = ev[0] if (ev[1] - ev[0]) % 5 == 1 else ev[1]
                o = q[(i + 3) % 5]
                T[(N % 8, i, jacobi(q[0], N), jacobi(2, o))] += 1
            s += 1
        if m == 1 and c > X + 3: break
for k in sorted(T): print(k, T[k])
