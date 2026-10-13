"""bsA_fareydist: Farey-graph distance d(inf, p/A) (BFS on the ladder of Stern-Brocot ancestors, which contains all
geodesics) vs HJ length; signed least non-residue lam_F(p) = min_{QNR A} d(inf, p/A).
Usage: PYTHONPATH=scripts uv run python scripts/bsA_fareydist.py PMAX"""
import sys
from collections import deque
from sympy import primerange, jacobi_symbol
from bsA_hjlen import hj_len

def ladder(p, q):
    # all intermediate fractions (Stern-Brocot path) from 1/0, 0/1 to p/q, plus integers near
    V = {(1, 0), (0, 1)}
    a, b, c, d = 0, 1, 1, 0  # left a/b, right c/d
    # start from -infinity side: use mediant walk for p/q>0
    while True:
        m = (a + c, b + d); V.add(m)
        if m == (p, q): break
        if m[0] * q < p * m[1]: a, b = m
        else: c, d = m
    return V

def fdist(p, q):
    V = ladder(p, q); V |= {(k, 1) for k in range(0, p // q + 3)}
    adj = {x: [] for x in V}
    L = list(V)
    for i in range(len(L)):
        for j in range(i):
            (x1, y1), (x2, y2) = L[i], L[j]
            if abs(x1 * y2 - x2 * y1) == 1:
                adj[L[i]].append(L[j]); adj[L[j]].append(L[i])
    dist = {(1, 0): 0}; Q = deque([(1, 0)])
    while Q:
        x = Q.popleft()
        for y in adj[x]:
            if y not in dist: dist[y] = dist[x] + 1; Q.append(y)
    return dist[(p, q)]

if __name__ == "__main__":
    P = int(sys.argv[1]); from collections import Counter
    c = Counter(); worse = 0
    for p in primerange(17, P):
        if p % 8 != 1: continue
        lamF = min(fdist(p, A) for A in range(1, p) if jacobi_symbol(A, p) == -1)
        lam = min(hj_len(p, A) for A in range(1, p) if jacobi_symbol(A, p) == -1)
        c[(lam, lamF)] += 1
    print("(lambda_HJ, lambda_Farey) counts, p=1(8) <", P, dict(c))
