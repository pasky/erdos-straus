# z51 dbreak: cross-check of scripts/z51_dbreak_candidates.c (X_top via the m-view) against a brute-force e-view
# (factor n + 4e for e <= (n+3)/8, count prime factors l > sqrt(2N) with 4e | l+1), on random n in [N/2, N].
# Usage: uv run --with numpy python scripts/z51_dbreak_xcheck_top.py [path-to-compiled-candidates] [N] [count]
import sys, math, random, subprocess
import numpy as np
exe = sys.argv[1] if len(sys.argv) > 1 else "./candidates"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
cnt = int(sys.argv[3]) if len(sys.argv) > 3 else 150
top2 = 2 * N
M = 2 * N + 10
spf = np.arange(M + 1)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == i:
        s = spf[i * i::i]; msk = s == np.arange(i * i, M + 1, i); s[msk] = i; spf[i * i::i] = s
def pf(x):
    fs = set()
    while x > 1:
        p = int(spf[x]); fs.add(p)
        while x % p == 0: x //= p
    return fs
random.seed(5)
ns = []
while len(ns) < cnt:
    n = random.randrange(N // 2, N); n -= (n - 1) % 8
    if math.isqrt(n) ** 2 != n: ns.append(n)
res = subprocess.run([exe, str(N), "0", "1"] + [str(n) for n in ns], capture_output=True, text=True, check=True)
out = [l for l in res.stdout.split("\n") if l.strip()]
assert len(out) == len(ns), (len(out), len(ns))
bad = 0
for n, line in zip(ns, out):
    fields = line.split()
    assert int(fields[0]) == n
    X = sum(1 for e in range(1, (n + 3) // 8 + 1) for l in pf(n + 4 * e) if l * l > top2 and (l + 1) % (4 * e) == 0)
    if X != int(fields[2]): bad += 1; print("MISMATCH", n, X, fields[2])
print("checked", len(ns), "mismatches", bad)
