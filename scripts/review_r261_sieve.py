"""R261: (1) q3(p) <= (p+1)/2 for p = 1 (4) <= PMAX (Pollack's proof bound); (2) sanity of Thm 3.2's display
#(P(y) cap [1,Q]) <= (N+Q^2)/|A(N,y)| on small parameters (exact counts)."""
import sys
from sympy import primerange, jacobi_symbol
PMAX = int(sys.argv[1])
q3s = [q for q in primerange(3, 10**5) if q % 4 == 3]
worst = 0
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    q = next(q for q in q3s if jacobi_symbol(q, p) == -1)
    assert 2 * q <= p + 1, (p, q)
    worst = max(worst, q / p)
print('q3(p) <= (p+1)/2 for all p = 1 (4) <', PMAX, '; max q3/p =', worst)
for y, N, Q in [(20, 10**6, 10**5), (40, 10**7, 10**6), (60, 10**7, 3 * 10**6)]:
    S = [q for q in q3s if q <= y]
    A = {1}; frontier = [1]
    while frontier:
        nf = []
        for a in frontier:
            for q in S:
                b = a * q
                if b <= N and b not in A:
                    A.add(b); nf.append(b)
        frontier = nf
    P = [p for p in primerange(3, Q + 1) if p % 8 == 1 and all(jacobi_symbol(q, p) == 1 for q in S)]
    print('y', y, 'N', N, 'Q', Q, '#P(y)∩[1,Q] =', len(P), 'min', P[:1], ' bound (N+Q^2)/|A| =', (N + Q * Q) / len(A), '|A| =', len(A))
