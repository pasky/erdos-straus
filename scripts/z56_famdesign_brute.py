# brute-force all (★) solutions (o,e,C) of n = 4oeC - o - e for small n; compare total count with z56scan's 'all' column
import sys, subprocess
def brute(n):
    s = 0
    for x in range(1, n + 1):           # x = first coordinate u
        m0 = 4 * x
        # n + x = B(4xC - 1)
        N = n + x
        C = 1
        while 4 * x * C - 1 <= N:
            d = 4 * x * C - 1
            if N % d == 0: s += 1
            C += 1
    return s  # ordered (u,B) count = R(n)
ns = [n for n in range(5, 3001, 2)]
out = subprocess.run(['/tmp/z56scan', '-'], input='\n'.join(map(str, ns)), capture_output=True, text=True).stdout.split('\n')
bad = 0
for line in out:
    if not line.strip(): continue
    f = list(map(int, line.split())); n = f[0]
    r = brute(n)
    if r != 2 * f[1]: bad += 1; print('MISMATCH', n, r, f[1])
print('checked', len(ns), 'mismatches', bad)
