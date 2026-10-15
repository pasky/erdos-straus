"""R249: from-scratch calibration of SIBLING §2.1/§2.3 under exact uniform placement (hypergeometric):
b_d DISTINCT balls of depth d among M = 3^(d-2) cylinders of a slice; npar = 3^(d-3) parents; A = alive parents (SD §3)."""
from math import comb
b = {3: 1, 4: 2, 5: 4, 6: 12, 7: 13, 8: 28, 9: 26}
A = {2: 1, 3: 2, 4: 6, 5: 16, 6: 44, 7: 130, 8: 380}
def pk(M, bb, k):  # P(a given parent has exactly k ball children), exact
    return comb(3, k) * comb(M - 3, bb - k) / comb(M, bb) if bb >= k else 0.0
T3a = T2a = T3all = T3binom = 0
for d in range(3, 10):
    M, npar = 3 ** (d - 2), 3 ** (d - 3)
    p3, p2 = pk(M, b[d], 3), pk(M, b[d], 2)
    T3a += A[d - 1] * p3; T2a += A[d - 1] * (p2 + p3)
    if d >= 5: T3all += npar * p3
    T3binom += A[d - 1] * (b[d] / M) ** 3
    print(d, "alive: E3 %.4f E>=2 %.3f | all parents: E3 %.4f, E[sibling pairs] exact %.3f (author C(b,2)/npar = %.3f)" % (A[d-1]*p3, A[d-1]*(p2+p3), npar*p3, comb(b[d],2)*2/(M-1), comb(b[d],2)/npar))
print("depths 3-9 alive parents: E[triples] exact %.4f (binomial p^3 model: %.4f), P(none)~%.3f; E[>=2] %.3f" % (T3a, T3binom, 2.718281828 ** -T3a, T2a))
print("all parents, depths 5-9: E[triples] exact %.4f" % T3all)
