"""z52d avenue Q10 (Z3144): deterministic Chebyshev test at fixed p over levels C.
D_C = #{u : (4uC-1) | p+u}, E_C = Σ_u 1/φ(4uC-1) (prime density); if all D_C = 0 then Σ(D-E)² = ΣE², so a bound
Σ_C (D_C - E_C)² < Σ_C E_C² would certify (★). Prints the ratio Σ(D-E)²/ΣE² (always 1 at (★) zeros).
Run: timeout 60 python3 scripts/z52d_avenue_Q10_levelmoment.py"""
import numpy as np
PS = [409, 577, 5569, 9601, 100049, 100153, 102001, 200009, 250013]
N = max(PS) + max(PS) // 3 + 10
phi = np.arange(N + 1)
for i in range(2, N + 1):
    if phi[i] == i: phi[i::i] -= phi[i::i] // i
for p in PS:
    D, E = {}, {}
    u = 1
    while 3 * u - 1 <= p:
        C = 1
        while 4 * u * C - 1 <= p + u:
            m = 4 * u * C - 1
            E[C] = E.get(C, 0) + 1 / phi[m]
            if (p + u) % m == 0: D[C] = D.get(C, 0) + 1
            C += 1
        u += 1
    lhs = sum((D.get(C, 0) - e) ** 2 for C, e in E.items()); rhs = sum(e * e for e in E.values())
    print(f'p={p} R={sum(D.values())} M={sum(E.values()):.1f} E_1={E[1]:.2f} #levels with E_C>1: {sum(e > 1 for e in E.values())} '
          f'Σ(D-E)²={lhs:.1f} ΣE²={rhs:.1f} ratio={lhs / rhs:.2f}')
# fraction of primes p ≡ 1 (4) in [50000, 60000] where the Chebyshev inequality holds (ratio < 1)
def ratio(p):
    D, E = {}, {}
    u = 1
    while 3 * u - 1 <= p:
        C = 1
        while 4 * u * C - 1 <= p + u:
            m = 4 * u * C - 1
            E[C] = E.get(C, 0) + 1 / phi[m]
            if (p + u) % m == 0: D[C] = D.get(C, 0) + 1
            C += 1
        u += 1
    return sum((D.get(C, 0) - e) ** 2 for C, e in E.items()) / sum(e * e for e in E.values())
ps = [p for p in range(50001, 60000, 4) if all(p % d for d in range(2, int(p ** .5) + 1))][:150]
rs = [ratio(p) for p in ps]
print(f'{len(ps)} primes ≡ 1 (4) in [5e4, 6e4]: ratio < 1 at {sum(r < 1 for r in rs)}; median ratio {sorted(rs)[len(rs) // 2]:.2f}')
