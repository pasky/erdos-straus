"""fz_rankin_check.py (O220): brute-force check of FF_STERILE_SMALL Lemma 4.1 as implemented in fz_sum.c (lRk):
max over monic F of exact degree n, F(0) != 0, of #{monic D | F, deg D = d} vs exp(lRk(n, d)), q prime, small n.
Counts by tallying all products D*D' (deg D = d, deg D' = n - d). usage: fz_rankin_check.py q N  (needs /tmp/rk_exp)"""
import sys, itertools, subprocess
from collections import Counter
q = int(sys.argv[1]); N = int(sys.argv[2])
bd = {}
for line in subprocess.run(['/tmp/rk_exp', str(q), str(N)], capture_output=True, text=True).stdout.split('\n'):
    if line: n, d, v = line.split(); bd[int(n), int(d)] = float(v)
def monic(d):
    for c in itertools.product(range(q), repeat=d): yield tuple(c) + (1,)
def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % q
    return tuple(r)
worst = 0; viol = 0
for n in range(1, N + 1):
    for d in range(0, n // 2 + 1):
        A = [p for p in monic(d) if p[0] != 0]; B = [p for p in monic(n - d) if p[0] != 0]
        cnt = Counter(mul(x, y) for x in A for y in B)
        mx = max(cnt.values()) if d != n - d else max(cnt.values())
        b = bd[n, d]
        if mx > b + 1e-9: viol += 1; print('VIOL', n, d, mx, b)
        worst = max(worst, mx / b)
    print(f'n={n} done, worst ratio so far {worst:.3f}', flush=True)
print(f'q={q} N={N} violations={viol} worst max/bound={worst:.4f}')
