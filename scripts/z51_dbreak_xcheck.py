# z51 dbreak: independent brute-force cross-check of sieve4.c at N = 20000 (A_N membership via the e-view).
import sys, math
sys.path.insert(0, "scripts")
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
M = 2 * N + 10
spf = np.arange(M + 1)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == i:
        s = spf[i * i::i]; m = s == np.arange(i * i, M + 1, i); s[m] = i; spf[i * i::i] = s
def primes_of(x):
    fs = []
    while x > 1:
        p = int(spf[x]); fs.append(p)
        while x % p == 0: x //= p
    return fs
alive = []
for n in range(9, N + 1, 8):
    hit = False
    for e in range(1, (n + 3) // 8 + 1):
        for l in primes_of(n + 4 * e):
            if l <= N and (l + 1) % (4 * e) == 0:
                hit = True; break
        if hit: break
    if not hit: alive.append(n)
print(len(alive), sum(1 for n in alive if math.isqrt(n) ** 2 == n))
open("data/z51_dbreak/xcheck_alive_N%d.txt" % N, "w").write("\n".join(map(str, alive)) + "\n")
