"""Generate the z53 FORESTCLASS test lists: hard primes (repo lists) and random samples p ≡ 1 (24).
Usage: uv run --with sympy python scripts/z53_forestclass_lists.py OUTDIR"""
import sys, random
from sympy import isprime
out = sys.argv[1]
Z14 = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
N = [193, 2521, 3361, 66529, 5101441]
HC = [21841, 92401, 691681, 83816041, 147223441]
R0 = [19441, 63361, 93601, 429529, 539401, 696361, 928561, 1202041, 1299601, 1847401, 3819481, 11516521, 13503121,
      17358961, 26120161, 28237801, 28845721, 32676361, 33177601, 36647041, 76737601, 84272401]
HINST = [695556000001, 14682537968401, 19611435110401, 85472983425601, 93900751257601, 101786710323601]
NS = [1299601, 33177601, 476985601, 973440001, 2134440001, 2813241601, 4292870401, 11833088401]
THM1 = [20304874801, 20473689601, 50016279601, 58084462801, 87004184401]
ROOT1 = [409, 1201, 5569, 8521, 8641, 9649, 12289, 12721, 12841, 15241, 16921, 19441, 23761, 23929, 24481, 27241]
D = []
a = 1
while len(D) < 59:
    p = 2521 + 9240 * a
    if isprime(p) and isprime((p + 11) // 12):
        D.append(p)
    a += 1
hard = {}
for name, L in [("Z14", Z14), ("N", N), ("HC", HC), ("R0fail", R0), ("Hinst", HINST), ("nearsq", NS), ("thm1", THM1),
                ("root1", ROOT1), ("D", D)]:
    for p in L:
        assert isprime(p), p
        hard.setdefault(p, []).append(name)
with open(f"{out}/hard_primes.txt", "w") as f:
    for p in sorted(hard):
        f.write(f"{p} {','.join(hard[p])}\n")
random.seed(53)
for e, cnt in [(9, 3000), (10, 1000), (11, 500), (12, 300), (13, 100)]:
    X = 10 ** e
    S = set()
    while len(S) < cnt:
        k = random.randrange(X // 24, (11 * X // 10) // 24)
        p = 24 * k + 1
        if isprime(p):
            S.add(p)
    with open(f"{out}/sample_1e{e}.txt", "w") as f:
        f.write("\n".join(map(str, sorted(S))) + "\n")
print(len(hard), "hard primes")
