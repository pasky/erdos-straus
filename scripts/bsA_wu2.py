"""bsA_wu2: test (A/n) = +1 <=> w.w = n + r - 1 (mod 8) for linear plumbings of length r (HJ words), and the
analogous statement for random positive-definite integral lattices of odd prime determinant (disc-form class)."""
import itertools, random
from sympy import jacobi_symbol, Matrix, isprime
def wu(G):
    r = len(G)
    for eps in itertools.product((0, 1), repeat=r):
        if all(sum(G[j][i]*eps[i] for i in range(r)) % 2 == G[j][j] % 2 for j in range(r)):
            return sum(eps[i]*G[i][j]*eps[j] for i in range(r) for j in range(r))
def K(b):
    a0, a1 = 1, 0
    for x in b: a0, a1 = x*a0 - a1, a0
    return a0
bad = tot = 0
for r in range(1, 6):
    for b in itertools.product(range(2, 10), repeat=r):
        n = K(b)
        if n % 2 == 0: continue
        A = K(b[1:]) if r > 1 else 1
        G = [[b[i] if i == j else (-1 if abs(i-j) == 1 else 0) for j in range(r)] for i in range(r)]
        res = (wu(G) - n - r + 1) % 8
        pred = 1 if res == 0 else (-1 if res == 4 else 0)   # residue must be 0 (sign +1) or 4 (sign -1)
        tot += 1; bad += pred != jacobi_symbol(A, n)
print("linear plumbings r<=5, letters 2..9: tested", tot, "failures", bad)
random.seed(1); bad = tot = 0
while tot < 3000:
    r = 3; B = [[random.randint(-3, 3) for _ in range(r)] for _ in range(r)]
    G = Matrix(B).T * Matrix(B) + Matrix.eye(r) * random.randint(0, 2)
    n = G.det()
    if n < 3 or not isprime(n): continue
    adj = G.adjugate(); k = next(i for i in range(r) if adj[i, i] % n)
    cls = jacobi_symbol(int(adj[k, k]) % n, n)
    res = (wu(G.tolist()) - n - r + 1) % 8
    pred = 1 if res == 0 else (-1 if res == 4 else 0)
    tot += 1; bad += pred != cls
print("random rank-3 lattices, prime det: tested", tot, "failures", bad)
