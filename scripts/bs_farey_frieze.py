"""O144 (c'): "Farey-chain" (frieze) ES solutions.

For a path r0 < r1 < r2 < r3 of Farey neighbours with denominators q0..q3, r_{i+1} - r_i = 1/(q_i q_{i+1}),
and q_{i-1} + q_{i+1} = k_i q_i (Hirzebruch-Jung recurrence).  Algebraic identity:
   1/(q0 q1) + 1/(q1 q2) + 1/(q2 q3) = (k1 k2 - 1)/(q0 q3)   whenever q1 | q0+q2, q2 | q1+q3.
Question: which ES solutions 4/p = 1/x+1/y+1/z admit an ordering and a factorisation
x = q0 q1, y = q1 q2, z = q2 q3 with q1 | q0 + q2 and q2 | q1 + q3 ("chain solutions")?
Usage: uv run python scripts/bs_farey_frieze.py PMAX
"""
import sys, math
from itertools import permutations
from sympy import primerange, divisors

def solutions(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        A, B = 4 * x - n, n * x  # 1/y + 1/z = A/B
        if A <= 0:
            continue
        g = math.gcd(A, B); A //= g; B //= g
        # (Ay - B)(Az - B) = B^2, y <= z, y >= x
        for u in divisors(B * B):
            if u * u > B * B:
                break
            if (u + B) % A:
                continue
            y = (u + B) // A; v = B * B // u
            if (v + B) % A:
                continue
            z = (v + B) // A
            if y >= x:
                out.append((x, y, z))
    return out

def is_chain(x, y, z):
    for q1 in divisors(math.gcd(x, y)):
        q0, q2 = x // q1, y // q1
        if z % q2 or (q0 + q2) % q1:
            continue
        q3 = z // q2
        if (q1 + q3) % q2 == 0:
            return (q0, q1, q2, q3)
    return None

PMAX = int(sys.argv[1])
tot_s = tot_c = 0; no_chain = []
for p in primerange(5, PMAX + 1):
    S = solutions(p); ch = 0
    for (x, y, z) in S:
        if any(is_chain(*o) for o in set(permutations((x, y, z)))):
            ch += 1
    tot_s += len(S); tot_c += ch
    if ch == 0:
        no_chain.append(p)
print(f"primes 5..{PMAX}: solutions (x<=y<=z) {tot_s}, chain-realisable {tot_c} ({tot_c/tot_s:.3f})")
print("primes with no chain solution:", no_chain[:30], "count", len(no_chain))
