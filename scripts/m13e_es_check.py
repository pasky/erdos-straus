"""m13e_es_check.py — independent check of m13e_es at large N: for x in given ranges, all y with
1/y + 1/z = 4/N - 1/x, x <= y <= z, by plain Python (sympy factorint; divisors D of s^2 with D <= s).
usage: m13e_es_check.py esbinary N xlo:len [xlo:len ...]    compares with the binary's output on each range."""
import subprocess, sys
from math import gcd
from sympy import factorint

def sols(N, x):
    num, den = 4 * x - N, N * x
    g = gcd(num, den); r, s = num // g, den // g
    f = factorint(s)
    divs = [1]
    for p, e in f.items():
        divs = [d * p ** k for d in divs for k in range(2 * e + 1)]
    out = []
    for D in divs:
        if D <= s and (D + s) % r == 0 and (s * s // D + s) % r == 0:
            y = (D + s) // r
            if y >= x:
                out.append((x, y))
    return out

b, N = sys.argv[1], int(sys.argv[2]); tot = 0
for rg in sys.argv[3:]:
    lo, ln = map(int, rg.split(':')); lo = max(lo, N // 4 + 1); hi = min(lo + ln - 1, 3 * N // 4)
    mine = sorted(t for x in range(lo, hi + 1) for t in sols(N, x))
    out = subprocess.run([b, str(N), str(lo), str(hi)], capture_output=True, text=True).stdout.split('\n')
    eng = sorted(tuple(map(int, l.split())) for l in out if l and not l.startswith('#'))
    tot += len(mine)
    print(f'N={N} x in [{lo},{hi}]: python {len(mine)}, engine {len(eng)}, {"SAME" if mine == eng else "DIFFERENT"}', flush=True)
print('total solutions compared', tot)
