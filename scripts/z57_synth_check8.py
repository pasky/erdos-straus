# z57 SYNTH: independent check (sympy factorisation, divisor enumeration) of R(p) and R8(p) = #{(★) solutions with C even}
# at given primes.  Every solution (u, B, C) of 4uBC - u - B = p has min(u, B, C) <= M := floor((p/3)^{1/3}) + 2 (if u, B >= 2
# then u + B <= uB <= uBC, so 4uBC = p + u + B <= p + uBC, uBC <= p/3; if u = 1 or B = 1 the minimum is 1).  Enumerate: for C <= M all d | 4Cp+1 with
# d = -1 (mod 4C) (giving u = (d+1)/(4C), B = (4Cp+1)/d ... as (4uC-1)(4BC-1) = 4Cp+1); for u <= M all d | p+u with
# d = -1 (mod 4u) (C = (d+1)/(4u), B = (p+u)/d); B <= M symmetric.  Collect the set of ordered triples.
# usage: uv run --with sympy python scripts/z57_synth_check8.py p1 p2 ...
import sys
from sympy import divisors
def sols(p):
    M = int((p / 3) ** (1 / 3)) + 2; S = set()
    for C in range(1, M + 1):
        N = 4 * C * p + 1
        for d in divisors(N):
            if d % (4 * C) == 4 * C - 1:
                e = N // d
                if e % (4 * C) == 4 * C - 1: S.add(((d + 1) // (4 * C), (e + 1) // (4 * C), C))
    for u in range(1, M + 1):
        for d in divisors(p + u):
            if d % (4 * u) == 4 * u - 1:
                C = (d + 1) // (4 * u); B = (p + u) // d
                S.add((u, B, C)); S.add((B, u, C))
    for t in S: assert 4 * t[0] * t[1] * t[2] - t[0] - t[1] == p
    return S
for a in sys.argv[1:]:
    p = int(a); S = sols(p)
    print(p, 'R =', len(S), 'R8 =', sum(1 for t in S if t[2] % 2 == 0), 'min C =', min(t[2] for t in S) if S else None)
