"""R127: from-scratch simulation of the Prop 7.2 diagonal construction (one unit class r_m != -1
per modulus m >= 3), J stages; checks every p_j avoids every class with m <= MAX, and reports the
Haar expectation sum_{m<=X} 1/m (not 1/phi(m)) of the system."""
from math import gcd, lcm
from sympy import isprime, totient
J, MAX = 5, 20000
M = [3]
for j in range(1, J + 2):  # M_j: phi(m) > j+1 for all m > M_j (phi(m) >= sqrt(m/2) so scan to 4(j+1)^2+10)
    bad = [m for m in range(3, 8 * (j + 2) ** 2 + 50) if totient(m) <= j + 1]
    M.append(max(max(bad), M[-1] + 1))
r = {}; P = []
def choose(m, avoid):
    for a in range(1, m):
        if gcd(a, m) == 1 and a != m - 1 and all(a != q % m for q in avoid): return a
    raise SystemExit(f"no class for m={m}")
for m in range(3, M[1] + 1): r[m] = choose(m, [])
for j in range(1, J + 1):
    L = lcm(*range(1, M[j] + 1)); p = L - 1
    while not isprime(p): p += L
    P.append(p)
    for m in range(M[j] + 1, M[j + 1] + 1): r[m] = choose(m, P)
for m in range(M[J + 1] + 1, MAX + 1): r[m] = choose(m, P)  # later stages: avoid all p_j
fails = [(p, m) for p in P for m in range(3, MAX + 1) if p % m == r[m]]
print("M_j:", M); print("p_j:", P); print("hits of p_j in the system (m<=%d):" % MAX, fails)
print("sum_{3<=m<=MAX} 1/m =", sum(1 / m for m in range(3, MAX + 1)), " (Haar: P(n = r_m mod m) = 1/m)")
