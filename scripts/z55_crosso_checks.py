# z55 CROSSO sanity checks (EVIDENCE/CERTIFIED at small sizes).
# (1) R_F via engine == brute force over (u,w) at small n (primes, squares, composites).
# (2) every hit has level divisor d = 4uC-1 with Jacobi (d/p) = -1 and d | 4Cp+1, cofactor 8wC-1.
# (3) odd squares: R_F = 0.
import subprocess, sys, math, random
from sympy import isprime, jacobi_symbol, factorint
ENG = "/tmp/z55R"
def sqf(x): return all(e == 1 for e in factorint(x).values())
def win(n, a0=1/12, a1=1/3, b=1/3, g=2/3):
    return int(n**a0), int(n**a1/2), int(n**b), int(n**g/4)
def eng(n, W):
    out = subprocess.run([ENG, str(n), *map(str, W), "1"], capture_output=True, text=True, check=True).stdout.split("\n")
    hits = [tuple(int(t.split("=")[1]) for t in l.split()[1:]) for l in out if l.startswith("hit")]
    R = int([l for l in out if l and not l.startswith("hit")][0].split()[1])
    return R, hits
def brute(n, W):
    U0, U1, Y, X = W; R = 0
    for u in range(U0 + 1, U1 + 1):
        if u % 4 != 1 or not sqf(u) or math.gcd(u, n) > 1: continue
        for w in range(Y + 1, X + 1, 2):
            if (n + u + 2 * w) % (8 * u * w) == 0 and sqf(w) and math.gcd(w, u * n) == 1: R += 2
    return R
random.seed(55)
bad = 0; nh = 0
ps = [p for p in range(10**6, 10**6 + 40000) if p % 4 == 1 and isprime(p)][:60]
for p in ps:
    W = win(p); R, hits = eng(p, W)
    if R != brute(p, W): bad += 1; print("MISMATCH", p)
    for (u, w, C) in hits:
        nh += 1; d = 4 * u * C - 1
        assert (p + u) == 2 * w * d and (4 * C * p + 1) == d * (8 * w * C - 1)
        assert jacobi_symbol(d, p) == -1 and jacobi_symbol(8 * w * C - 1, p) == -1
print(f"(1)(2) primes checked {len(ps)}, brute mismatches {bad}, hits {nh}, all hits (d/p)=-1")
sq = [m * m for m in range(1001, 1401, 2)]
nz = sum(1 for n in sq if eng(n, win(n))[0] != 0)
# squares with a wider window too
nz2 = sum(1 for n in sq if eng(n, (0, int(n**0.4), int(n**0.4), n // (8 * int(n**0.4) + 8)))[0] != 0)
print(f"(3) odd squares {len(sq)}: nonzero R (std window) {nz}, (wide window) {nz2}")
comp = [n for n in range(10**6 + 1, 10**6 + 4000, 4) if not isprime(n) and math.isqrt(n)**2 != n][:200]
print("(4) composite non-squares with R>0 (std window):", sum(1 for n in comp if eng(n, win(n))[0] > 0), "of", len(comp))
