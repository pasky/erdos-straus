"""Numerical companion for EXCEPTIONAL_THETA.md Assessment 5.8 (O): deadly values.

Fix a prime l.  For every cofactor q <= X with q*l = 3 (mod 4), M = q*l, A=(M+1)/4,
the forced classes R(M) = {-4D mod M : D | A^2} project to residues b mod l.
Under the CRT measure the "rest" of such a class (n = class mod q) holds with
probability 1/q, so the expected number of conditions through (l, b) with rest set is
    m_b = sum_{q<=X} #{classes of R(ql) congruent to b mod l} / q.
We print, against (log l)^2 and (log X):
   S_all   = sum_b m_b                (uncapped "sum over coordinates" mass, x l)
   S_cap   = sum_b min(1, m_b)        (capped: what enters Assessment 5.8 (O))
   n_dead  = #{b : m_b >= 1}          (deadly values)
   S_sq    = sum_b min(1, m_b)^2      (the off-diagonal quantity of Assessment 5.8 (O))
Run: uv run python scripts/theta_deadly_values.py
"""
import math
from collections import defaultdict

from sympy import factorint


def run(l, X):
    m = defaultdict(float)
    for q in range(1, X + 1):
        M = q * l
        if M % 4 != 3:
            continue
        A = (M + 1) // 4
        f = factorint(A)
        divs = [1]
        for p, e in f.items():
            divs = [d * p ** k for d in divs for k in range(2 * e + 1)]
        res = {(-4 * D) % M for D in divs}
        for r in res:
            m[r % l] += 1.0 / q
    S_all = sum(m.values())
    S_cap = sum(min(1.0, v) for v in m.values())
    n_dead = sum(1 for v in m.values() if v >= 1)
    S_sq = sum(min(1.0, v) ** 2 for v in m.values())
    return S_all, S_cap, n_dead, len(m), S_sq


if __name__ == "__main__":
    print(f"{'l':>8} {'X':>6} {'S_all':>9} {'S_cap':>9} {'n_dead':>7} {'#b used':>8} {'(log l)^2':>9} {'S_cap/(log l)^2':>15} {'S_sq':>8} {'S_sq/(log l)^2':>14}")
    for l in [10007, 100003, 1000003]:
        for X in [1000, 4000]:
            S_all, S_cap, n_dead, nb, S_sq = run(l, X)
            L2 = math.log(l) ** 2
            print(f"{l:>8} {X:>6} {S_all:9.1f} {S_cap:9.1f} {n_dead:7d} {nb:8d} {L2:9.1f} {S_cap / L2:15.3f} {S_sq:8.1f} {S_sq / L2:14.3f}", flush=True)
