"""s9_janson_stats.py (O271): empirical test of a Janson-type inequality P(R = 0) <= exp(-mu + Delta/2) for the (★) count.
Inputs: s9_janson output (p R D) and z38_mbm output (p isprime R M0 MBM MBM8), p == 1 (mod 4).  Bins primes by M_BM8
(O268's mod-8-refined BM main term); in each bin mu = mean R, Delta = mean D (ordered dependent pairs: shared level or shift
integer, mirrors included).  Reports observed zeros vs Poisson e^{-mu}, swap-Poisson e^{-mu/2}, Janson exp(-mu + Delta/2).
usage: python s9_janson_stats.py JAN MBM"""
import sys
import numpy as np
J = np.loadtxt(sys.argv[1], dtype=np.int64)
M = np.loadtxt(sys.argv[2])
mb = {int(r[0]): (int(r[2]), r[4], r[5]) for r in M if int(r[0]) % 4 == 1}
p, R, D, NL = J[:, 0], J[:, 1], J[:, 2], J[:, 3]
assert all(mb[int(x)][0] == int(r) for x, r in zip(p[:50000], R[:50000])), "R mismatch with z38_mbm"
m8 = np.array([mb[int(x)][2] for x in p])
print(f"primes p == 1 (4) <= {p.max()}: {len(p)}; R agrees with z38_mbm on the first 50000")
print(" M_BM8 bin   |  n     zeros | mu=E R   Delta=E D  D/mu | n e^-mu   n e^-mu/2   n exp(-mu+D/2) | mu^2/(2D)  E#levels  mean log p")
edges = [0, 4, 6, 8, 10, 12, 14, 16, 20, 25, 40, 80]
for a, b in zip(edges[:-1], edges[1:]):
    s = (m8 >= a) & (m8 < b)
    n = s.sum()
    if n == 0: continue   # self-review fix: no bin is dropped
    mu, De = R[s].mean(), D[s].mean()
    print(f"[{a:2d},{b:2d})  | {n:6d} {int((R[s]==0).sum()):5d} | {mu:7.2f} {De:9.2f} {De/mu:5.2f} | {n*np.exp(-mu):8.2e} {n*np.exp(-mu/2):9.2e} {n*np.exp(-mu+De/2):10.2e} | {mu*mu/(2*De):8.2f} {NL[s].mean():8.2f} {np.log(p[s]).mean():8.2f}")
