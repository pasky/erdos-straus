# z60 MS105: brute-force check of Lemma 1 (twisted T1 on uC and BC) and the kernel decomposition (Lemma 2):
# for every n = 1 (4) <= N, every solution (u,B,C) of 4uBC - u - B = n, and every s with n = s*m^2 (s any divisor of n
# with n/s a square): s does not divide u*C and does not divide B*C.  Also checks R(n) = sum_{g | n} Rprim_g(n/g).
import math, sys
from collections import defaultdict
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
sols = defaultdict(list)
for u in range(1, N + 1):
    for B in range(1, (N + u) // (4 * u - 1) + 2):
        base = 4 * u * B
        C = 1
        while base * C - u - B <= N:
            n = base * C - u - B
            if n >= 1: sols[n].append((u, B, C))
            C += 1
bad = 0; checked = 0
for n in range(1, N + 1):
    ss = [s for s in range(1, n + 1) if n % s == 0 and math.isqrt(n // s) ** 2 == n // s]
    for (u, B, C) in sols[n]:
        for s in ss:
            checked += 1
            if (u * C) % s == 0 or (B * C) % s == 0: bad += 1; print('VIOLATION', n, s, u, B, C)
    # kernel decomposition: count primitive solutions of n/g with g | C', summed over g | n
    tot = 0
    for g in range(1, n + 1):
        if n % g: continue
        tot += sum(1 for (u, B, C) in sols[n // g] if math.gcd(u, B) == 1 and C % g == 0)
    if tot != len(sols[n]): bad += 1; print('DECOMP FAIL', n)
print('N', N, 'checked (sol, s) pairs', checked, 'violations', bad)
