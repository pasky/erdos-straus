"""R24 from-scratch recomputation of EXCEPTIONAL_TUPLES2 §5(a).

Z11_j = CRT mass of j-tuples (one class per distinct prime l = 3 mod 4, l <= y)
whose class -1 part G has q_G = prod G > N+1.  Computed EXACTLY (up to float
rounding) as  e_j - sum_{G: q_G <= N+1} (1/q_G) * e_{j-|G|}(p' on primes not in G),
p'_l = p_l - 1/l, by DFS over G (no log binning).
Also K = first even >= e^2 mu_y, eta_K = e^{-K/e^2}/K, u0, e_{u0}(q) (Thm 2.1).
usage: review_t2_forced.py N y [J]
"""
import sys
from math import log, exp, ceil, e as E
from sympy import primerange, divisors

N = int(float(sys.argv[1])); y = int(float(sys.argv[2])); J = int(sys.argv[3]) if len(sys.argv) > 3 else 12
P = [l for l in primerange(3, y + 1) if l % 4 == 3]
F = {l: len({(-4 * D) % l for D in divisors(((l + 1) // 4) ** 2)}) for l in P}
p = {l: F[l] / l for l in P}
mu = sum(p.values())

def esym(ws, J):
    c = [1.0] + [0.0] * J
    for w in ws:
        for k in range(J, 0, -1):
            c[k] += w * c[k - 1]
    return c

e = esym(p.values(), J)
pp = esym([p[l] - 1 / l for l in P], J)   # generating poly of non-(-1) hits
K = ceil(E * E * mu); K += K % 2
etaK = exp(-K / E ** 2) / K
Q = [l for l in P if l > y / 2]
u0 = ceil(log(N + 2) / log(y / 2))
eq = esym([1 / l for l in Q], u0)[u0]
print(f"N={N:.0e} y={y} #P={len(P)} mu={mu:.4f} K={K} eta_K={etaK:.3e} u0={u0} sigma={sum(1/l for l in Q):.4f} e_u0(q)={eq:.3e}")

# admissible-mass of (-1)-part: A_j = sum_{G: q_G<=N+1} (1/q_G) e_{j-|G|}(p' off G)
A = [0.0] * (J + 1)
count = 0
def dfs(start, q, G):
    global count
    count += 1
    # series of prod_{l not in G}(1 + p'_l x) = pp / prod_{l in G}(1 + p'_l x)
    c = pp[:]
    for l in G:
        a = p[l] - 1 / l
        for k in range(1, J + 1):
            c[k] -= a * c[k - 1]
    g = len(G)
    for j in range(g, J + 1):
        A[j] += c[j - g] / q
    for i in range(start, len(P)):
        l = P[i]
        if q * l > N + 1 or g + 1 > J:
            break
        dfs(i + 1, q * l, G + [l])
dfs(0, 1, [])
print(f"# admissible (-1)-sets enumerated: {count}")
print("# j  e_j  Z11_j  Z11_j/eta_K")
best = (0, 0)
for j in range(1, J + 1):
    Z = e[j] - A[j]
    print(f"{j:3d} {e[j]:.4e} {Z:.4e} {Z/etaK:.3e}")
    if Z / etaK > best[0]:
        best = (Z / etaK, j)
print(f"max_j Z11_j/eta_K = {best[0]:.3e} at j={best[1]}")
