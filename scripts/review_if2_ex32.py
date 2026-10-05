"""R25 from-scratch check of IF2 Example 3.2, rigidity, Lemma 3.1 and Prop 2.1.

1. Brute-force the identity 1[0 mod 21] = 1[0 mod 7] - 1[1 mod 3] - 1[2 mod 3] + sum_{12 classes}
   and its hybrid charge at N = 20 (beta* charge computed from definitions).
2. LP over M(Q') (Q' = 2520) : min and max of mu(0 mod 21) and of mu(x) for every x mod 21.
3. Generalisation: for N with N+1 = d1*d2, gcd = 1, d1,d2 <= N/2, verify by LP on Z/(N+1)
   (all divisors of N+1 as moduli) that every mu in M vanishes on 0 mod N+1.
"""
import sys
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def c(b, d, N):
    return sum(1 for n in range(1, N + 1) if (n - b) % d == 0)

def beta_star(a, d, N):
    return a * (-(-N // d)) if a > 0 else a * (N // d)

def check_identity():
    N = 20
    terms = [(1, 0, 7), (-1, 1, 3), (-1, 2, 3)]
    terms += [(1, b, 21) for b in range(21) if b % 3 and b not in (7, 14)]
    assert len(terms) == 15
    for n in range(-2000, 2000):
        v = sum(a for a, b, d in terms if (n - b) % d == 0)
        assert v == (1 if n % 21 == 0 else 0), n
    small = sum(a * c(b, d, N) for a, b, d in terms if d <= N / 2)
    large = sum(beta_star(a, d, N) for a, b, d in terms if d > N / 2)
    full = all(c(b, d, N) == -(-N // d) for a, b, d in terms if d > N / 2)
    print(f"identity OK on [-2000,2000); small exact={small}, large beta*={large}, total={small+large}, all large full={full}")
    print(f"charge of 1[0 mod 21] written as itself: {beta_star(1,21,N)}")

def divisors(Q):
    return [d for d in range(1, Q + 1) if Q % d == 0]

def build(N, Q):
    lam = np.zeros(Q)
    for m in range(1, N + 1):
        lam[m % Q] += 1
    Aeq, beq, Aub, bub = [], [], [], []
    for d in divisors(Q):
        for b in range(d):
            row = np.zeros(Q); row[b::d] = 1
            if d <= N / 2:
                Aeq.append(row); beq.append(lam[b::d].sum())
            else:
                Aub.append(row); bub.append(-(-N // d))
                Aub.append(-row); bub.append(-(N // d))
    return lam, np.array(Aeq), np.array(beq), np.array(Aub), np.array(bub)

def extremes(N, Q, target_rows):
    lam, Aeq, beq, Aub, bub = build(N, Q)
    out = []
    for name, row in target_rows:
        r = []
        for sgn in (1, -1):
            res = linprog(sgn * row, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
            assert res.status == 0, res.message
            r.append(sgn * res.fun)
        out.append((name, r[0], r[1]))
    return out

if __name__ == "__main__":
    check_identity()
    N, Q = 20, 2520
    rows = []
    for x in range(21):
        row = np.zeros(Q); row[x::21] = 1; rows.append((f"mu({x} mod 21)", row))
    for name, lo, hi in extremes(N, Q, rows):
        print(f"N=20 Q'=2520 {name}: min={lo:.6f} max={hi:.6f}")
    # generalisation N+1 = d1 d2
    for N in range(6, 120):
        M = N + 1
        ok = [(d1, M // d1) for d1 in range(2, M) if M % d1 == 0 and gcd(d1, M // d1) == 1
              and d1 <= N / 2 and M // d1 <= N / 2 and d1 < M // d1]
        if not ok:
            continue
        row = np.zeros(M); row[0] = 1
        (_, lo, hi), = extremes(N, M, [("mu(0)", row)])
        print(f"N={N} N+1={M}={ok[0][0]}*{ok[0][1]}: mu(0 mod N+1) in [{lo:.3g},{hi:.3g}]")
