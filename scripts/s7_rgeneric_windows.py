"""s7_rgeneric_windows: cap-0 windows on the r-generic line (p ≡ 1 at every prime l ≠ r, p ≡ c (mod r), c a non-residue).
There K_m = (p+m)/4 ≡ (1+m)/4 (mod l^k) for l ≠ r, so the known part of K_m is (1+m)/4 (exact exponents, r removed)
times r^b with b >= 1 iff c ≡ -m (mod r); the rest is an unknown r-free cofactor (not used). A window m ≡ 3 (4),
gcd(m, r) = 1, certifies the cell c at level 1 iff -1 ∈ {ratios of divisors of the known part} mod m
(offsets [-v, v] for l | (1+m)/4, [-1, 1] for r). Compare STERILE_LOWER Comp 4.1 (level-1 survivors r = 17: {5, 7}).
Usage: python s7_rgeneric_windows.py r MMAX
"""
import sys, math

def fac(n):
    f = {}; l = 2
    while l * l <= n:
        while n % l == 0:
            f[l] = f.get(l, 0) + 1; n //= l
        l += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

r, MMAX = int(sys.argv[1]), int(sys.argv[2])
nonres = [c for c in range(1, r) if pow(c, (r - 1) // 2, r) == r - 1]
covered = {}
for m in range(3, MMAX + 1, 4):
    if math.gcd(m, r) != 1:
        continue
    known = fac((1 + m) // 4); known.pop(r, None)
    for c in nonres:
        if c in covered or (c + m) % r:
            continue
        S = {1 % m}
        items = list(known.items()) + [(r, 1)]
        for l, v in items:
            g = l % m
            if math.gcd(g, m) != 1:
                continue
            gi = pow(g, -1, m)
            pw = {1}
            for j in range(1, v + 1):
                pw.add(pow(g, j, m)); pw.add(pow(gi, j, m))
            S = {x * y % m for x in S for y in pw}
        if (m - 1) in S:
            covered[c] = m
print("r", r, "windows m <=", MMAX, "covered cells:", covered, "survivors:", [c for c in nonres if c not in covered])
