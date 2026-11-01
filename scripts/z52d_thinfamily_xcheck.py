# z52d_thinfamily_xcheck.py — cross-check of the exact k-loop of z52d_thinfamily_menuA.py (Thm 5; testA with
# force_k=True) against direct divisor enumeration of N, for c0 in {3, 15, 63, 255}, odd u < 400, p in {3, 5, 7},
# N <= 10^30.  Usage: ulimit -v 8000000; uv run --with cypari2 --with gmpy2 python scripts/z52d_thinfamily_xcheck.py
import sys, runpy
sys.argv = ['x', '15', '1']
g = runpy.run_path('scripts/z52d_thinfamily_menuA.py')
pari = g['pari']; testA = g['testA']
bad = tot = 0
for c0 in (3, 15, 63, 255):
    F = c0 + 1; testA.__globals__['F'] = F
    for u in range(1, 400, 2):
        for p in (3, 5, 7):
            c = c0 * u ** p - 1; E = (c & -c).bit_length() - 1; co = c >> E; N = F + c
            if N > 10 ** 30: continue
            direct = sorted((X, N // X) for X in (int(t) for t in pari.divisors(N)) if ((F + X) * (1 + N // X)) % co == 0)
            kl = sorted(set(testA(u, p, E, co, N, force_k=True)))
            tot += 1
            if kl != direct: bad += 1; print('MISMATCH', c0, u, p, direct, kl)
print('k-loop (testA, force_k) vs direct divisor enumeration: checked', tot, 'mismatches', bad)
