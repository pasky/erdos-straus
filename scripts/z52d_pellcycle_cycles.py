r"""z52d PELLCYCLE: how much of the small-vertex range the principal cycle covers (Prop 2.4).
For prime p ≡ 1 (mod 8): enumerate ALL reduced quadratic irrationals x = (P + sqrt p)/Q with Q | p - P^2, Q > 0
(reduced: x > 1, -1 < x' < 0  <=>  0 < P < sqrt p, sqrt p - P < Q < sqrt p + P), partition them into CF cycles, and report
  c(p)   = number of cycles,
  |S(p)| = #{1 <= a < sqrt p : x^2 ≡ p (mod a) solvable},
  cov Q(S) = fraction of S(p) among the Q-values of the sqrt(p) cycle, cov Q(S∪W) = among the Q-values of the sqrt(p)
  and omega cycles (Q-values only: R0 and R2 also contain P-values and partial quotients),
  covall = fraction among all cycles (must be 1 by Prop 2.4(b)).
Usage: uv run --with sympy python scripts/z52d_pellcycle_cycles.py p1 p2 ...
"""
import math
import sys

from z52d_pellcycle_lib import cycle_data


def reduced_all(p):
    s = math.isqrt(p)
    out = []
    for P in range(1, s + 1):
        N = p - P * P
        # divisors Q of N in (s - P, s + P]  (sqrt p irrational: sqrt p - P < Q  <=>  Q >= s - P + 1)
        for Q in range(max(1, s - P + 1), s + P + 1):
            if N % Q == 0:
                out.append((P, Q))
    return out


def step(p, P, Q):
    s = math.isqrt(p)
    a = (P + s) // Q
    P2 = a * Q - P
    return P2, (p - P2 * P2) // Q


def main():
    print("| p | c(p) cycles | sizes of the sqrt(p) / omega cycles | |S(p)| | cov Q(S) | cov Q(S∪W) | cov Q(all cycles) |")
    print("|---:|---:|---|---:|---:|---:|---:|")
    for p in map(int, sys.argv[1:]):
        red = reduced_all(p)
        rs = set(red)
        seen = set()
        cycles = []
        for x in red:
            if x in seen:
                continue
            cyc = []
            y = x
            while y not in seen:
                seen.add(y)
                cyc.append(y)
                y = step(p, *y)
                assert y in rs
            cycles.append(cyc)
        s = math.isqrt(p)
        S = {a for a in range(1, s + 1) if any((x * x - p) % a == 0 for x in range(a))} if s < 4000 else None
        if S is None:  # faster: a with p square mod a, via sqrt mod prime powers is overkill; brute force with set of squares
            S = set()
            for a in range(1, s + 1):
                r = p % a
                if r in {x * x % a for x in range(a // 2 + 1)}:
                    S.add(a)
        cd = cycle_data(p)
        Q0 = {q for _, q, _ in cd["S"]["cyc"]}
        Q2 = Q0 | {q for _, q, _ in cd["W"]["cyc"]}
        Qall = {q for c in cycles for _, q in c}
        f = lambda T: len(S & T) / len(S)
        print(f"| {p} | {len(cycles)} | {cd['S']['period']} / {cd['W']['period']} | {len(S)} | {f(Q0):.3f} | {f(Q2):.3f} | {f(Qall):.3f} |")


if __name__ == "__main__":
    main()
