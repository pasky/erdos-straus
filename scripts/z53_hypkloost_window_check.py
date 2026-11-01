"""Numerical check of the frequency-window identity (Theorem B (a)) and of the zero-mean fact (Theorem B (b)).

Identity (W): for g with g^ supported in [-H, H],
   sum_h g^(h) S_{-h}(n) = sum_pi sum_l g(l/q_pi) 1[q_pi | n + l + s_pi],
with S_h(n) = sum_pi e(h (n+s_pi)/q_pi).  We take the Fejer pair
   g(t) = (H+1) (sin(pi (H+1) t) / (pi (H+1) t))^2,   g^(xi) = max(0, 1 - |xi|/(H+1)),
truncate the l-sum at |l| <= Lmax (tail of g is <= 1/(pi^2 (H+1) t^2)), and compare.
Also checks: E_n S_h(n) = #{pi : q_pi | h} (n uniform mod L) for 0 < h < q_min, i.e. = 0, by exact averaging over n mod lcm.
Usage: uv run --with mpmath python scripts/z53_hypkloost_window_check.py
"""
import math, cmath, itertools, random
from math import gcd

def pairs(U, V):
    return [(u, B) for u in range(U + 1, 2 * U + 1) for B in range(V + 1, 2 * V + 1)]

def S(h, n, P):
    return sum(cmath.exp(2j * math.pi * h * ((n + u + B) / (4 * u * B))) for u, B in P)

def g(t, H):
    if t == 0:
        return H + 1.0
    x = math.pi * (H + 1) * t
    return (H + 1) * (math.sin(x) / x) ** 2

def check_identity(n, U, V, H, Lmax):
    P = pairs(U, V)
    lhs = sum(max(0.0, 1 - abs(h) / (H + 1)) * S(-h, n, P) for h in range(-H, H + 1))
    rhs = 0.0
    tail_bound = 0.0
    for u, B in P:
        q, s = 4 * u * B, u + B
        # l with q | n + l + s, |l| <= Lmax
        l0 = (-(n + s)) % q
        for l in itertools.chain(range(l0, Lmax + 1, q), range(l0 - q, -Lmax - 1, -q)):
            rhs += g(l / q, H)
        # tail: sum over |l| > Lmax in the progression, g(t) <= 1/(pi^2 (H+1) t^2)
        tail_bound += 2 * sum(q * q / (math.pi ** 2 * (H + 1) * (Lmax + k * q) ** 2) for k in range(0, 2000))
    return lhs, rhs, tail_bound

if __name__ == "__main__":
    random.seed(5)
    print("Identity (W): Fejer weights, LHS (frequency side) vs RHS (window side)")
    for (n, U, V, H) in [(10007, 3, 3, 5), (100003, 5, 7, 20), (1000003, 8, 8, 40), (1000033, 8, 8, 200), (4 * 10**6 + 1, 10, 6, 100)]:
        lhs, rhs, tb = check_identity(n, U, V, H, Lmax=20 * 4 * (2 * U) * (2 * V))
        print(f"  n={n} U={U} V={V} H={H}: LHS={lhs.real:.6f}{lhs.imag:+.1e}i  RHS(trunc)={rhs:.6f}  |diff|={abs(lhs.real-rhs):.2e}  tail<= {tb:.2e}")
    print("Zero mean of S_h for 0 < h < q_min (exact average over n mod lcm of all q):")
    U, V = 2, 3
    P = pairs(U, V)
    L = 1
    for u, B in P:
        q = 4 * u * B
        L = L * q // gcd(L, q)
    qmin = min(4 * u * B for u, B in P)
    for h in [1, 2, 5, qmin - 1, qmin, 2 * qmin]:
        # average over n mod L of e(h (n+s)/q) = 1[q | h] * e(h s / q) -> compute exactly via the formula and by brute force on a sample
        exact = sum(cmath.exp(2j * math.pi * h * (u + B) / (4 * u * B)) if h % (4 * u * B) == 0 else 0 for u, B in P)
        brute = sum(S(h, n, P) for n in range(L)) / L
        print(f"  h={h}: E S_h = {brute.real:+.6f}{brute.imag:+.1e}i ; formula sum_[q|h] e(hs/q) = {exact.real:+.6f}  (q_min={qmin}, L={L})")
