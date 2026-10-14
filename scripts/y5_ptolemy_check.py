"""y5_ptolemy_check: transport law = Ptolemy mod 8 (memo y5_transport_is_ptolemy).
For all formal words (c,m,s) (letters >= 1) with odd N = mcs - c - s <= X check:
 (L1) ee' = N+o, 1+o, 1+o, N+o, 1+N*o for the even edge {h',c},{c,m},{m,s},{s,h},{h,h'} (o opposite);
 (C2) (h'/N) = -(-1/N) (2/o) (2/N)^eps   (Jacobi symbols; gcd issues: h' coprime to N always).
usage: y5_ptolemy_check.py X ; exits nonzero on failure."""
import sys
from collections import Counter
from y2_even_edge import jacobi

X = int(sys.argv[1]); bad = 0; T = Counter()
EPS = {0: 1, 1: 0, 2: 0, 3: 1, 4: 1}  # edge (i,i+1): 0={h',c},1={c,m},2={m,s},3={s,h},4={h,h'}
for c in range(1, X + 3):
    for m in range(1, X + 3):
        if c * m - 1 - c > X and c * m > 1: break  # s=1 gives N = cm - c - 1
        s = 1
        while True:
            N = c * m * s - c - s
            if N > X: break
            if N <= 0:
                if c * m - 1 <= 0: break  # c=m=1: N = -1 forever
                s += 1; continue
            if N % 2:
                q = (m * s - 1, c, m, s, c * m - 1)
                ev = [i for i in range(5) if q[i] % 2 == 0]
                i = ev[0] if (ev[1] - ev[0]) % 5 == 1 else ev[1]
                o = q[(i + 3) % 5]; e, e2 = q[i], q[(i + 1) % 5]; eps = EPS[i]
                if e * e2 != {0: N + o, 1: 1 + o, 2: 1 + o, 3: N + o, 4: 1 + N * o}[i]: bad += 1
                lhs = jacobi(q[0], N)
                rhs = -jacobi(-1 % N, N) * jacobi(2, o) * (jacobi(2, N) if eps else 1) if N > 1 else 1
                if N > 1 and lhs != rhs: bad += 1
                T[(N % 8, i)] += 1
            s += 1
print("cells (N mod 8, edge):", dict(sorted(T.items())))
print("words:", sum(T.values()), "failures:", bad)
sys.exit(1 if bad else 0)
