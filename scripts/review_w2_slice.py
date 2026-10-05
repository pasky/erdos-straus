#!/usr/bin/env python3
"""R29: direct test of the §6.3 claim "slice-separable fakes cannot work".
Discrete model (own build, float), two windows, theta = 1/2.
Slice-separable conditions on delta = nu - mu:
 (1) for every window-7 config Q and every NONEMPTY window-3 S3 with s3 <= theta:
       sum_P delta(P,Q) emb(S3,P) = 0
 (2) m(Q) = sum_P delta(P,Q) satisfies, for every S7 (incl. empty) with s7 <= theta:
       sum_Q m(Q) emb(S7,Q) = 0
Minimise nu(empty,empty) subject to nu >= 0.  Also reports the one-window
quantity  max total mass of nu' >= 0 with nu'(empty)=0 and nonempty visible
correlations = mu's  (to test the '0.256' step of the author's argument).
Usage: review_w2_slice.py EPS K THETA
"""
import sys, itertools
from math import comb, factorial, log, exp, sqrt
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog

eps, K, th = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
E = [exp(log(eps) * (1 - i / K)) for i in range(K + 1)]
g = [sqrt(E[i] * E[i + 1]) * (1 + 1e-7 * (i + 1)) for i in range(K)]
w = [0.5 * log(E[i + 1] / E[i]) for i in range(K)]
def vecs(cap, strict):
    return [m for m in itertools.product(*[range(int(cap / x) + 1) for x in g])
            if ((sum(a * b for a, b in zip(m, g)) < cap) if strict else (sum(a * b for a, b in zip(m, g)) <= cap))]
W = [m for m in vecs(1, True) if sum(m) % 2 == 0]
def muw(m):
    s = sum(a * b for a, b in zip(m, g)); v = max(1 - s, 1e-3) ** -0.5
    for k in range(K): v *= w[k] ** m[k] / factorial(m[k])
    return v
mu1 = np.array([muw(m) for m in W]); n = len(W)
V = vecs(th, False); Vne = [s for s in V if any(s)]
def emb(s, c):
    r = 1
    for a, b in zip(s, c):
        if a > b: return 0
        r *= comb(b, a)
    return r
E1 = np.array([[emb(s, c) for c in W] for s in V], float)      # rows V
E1ne = np.array([[emb(s, c) for c in W] for s in Vne], float)
z = W.index(tuple([0] * K))
# one-window: max total mass with nu'(empty)=0, nonempty correlations matched
x = linprog(-np.ones(n), A_eq=E1ne, b_eq=E1ne @ mu1, bounds=[(0, 0) if j == z else (0, None) for j in range(n)], method="highs")
print("one-window: max total of nu' (nu'(empty)=0) - total mu =", -x.fun - mu1.sum(), "(tau=1)")
x = linprog(np.ones(n), A_eq=E1ne, b_eq=E1ne @ mu1, bounds=[(0, 0) if j == z else (0, None) for j in range(n)], method="highs")
print("one-window: min total of nu' - total mu =", x.fun - mu1.sum())
# two-window separable LP; variable index (P,Q) -> P*n+Q ; delta = nu - mu
mu = np.outer(mu1, mu1).ravel()
rows = []
I = sp.identity(n, format="csr")
A1 = sp.kron(sp.csr_matrix(E1ne), I)          # (S3,Q) rows: sum_P emb(S3,P) nu(P,Q)
A2 = sp.kron(sp.csr_matrix(np.ones((1, n))), sp.csr_matrix(E1))  # (S7) rows: sum_{P,Q} emb(S7,Q) nu
A = sp.vstack([A1, A2]).tocsr()
b = A @ mu
# scale columns by mu, rows by b
Asc = sp.diags(1 / b) @ A @ sp.diags(mu)
c = np.zeros(n * n); c[z * n + z] = 1
r = linprog(c, A_eq=Asc, b_eq=np.ones(A.shape[0]), bounds=(0, None), method="highs")
print("separable two-window LP: status", r.status, " min nu(empty,empty)/tau =", r.fun)
