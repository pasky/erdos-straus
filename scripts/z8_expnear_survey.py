# z8_expnear_survey.py — exponential near-squares n_s = c0*4^s + k (m = 2^s, n = c0*m^2 + k).
# For each (c0, k) with n_s odd and n_s = 1 (mod 24) for large s (otherwise Mordell-trivial), search an
# exponent covering by ET + divisor classes (ec_cover.search with base b = 4, additive constant k).
# Usage: PYTHONPATH=scripts uv run python scripts/z8_expnear_survey.py c0 kmax Mmax L1 L2 ...
import sys, functools
import mordell_lib as ML
import ec_cover as EC
ML.residue_table = functools.lru_cache(maxsize=4000)(ML.residue_table)
c0, kmax, Mmax = map(int, sys.argv[1:4])
Ls = [int(x) for x in sys.argv[4:]]
cov, unc, triv = [], [], 0
for k in range(1, kmax + 1, 2):
    # large s: n = k (mod 8); n mod 3 = c0 + k
    if k % 8 != 1 or (c0 + k) % 3 != 1:
        triv += 1
        continue
    f = None
    for L in Ls:
        ch = EC.search(c0, L, Mmax, 4, k, verbose=False)
        if ch:
            f = (L, len(ch)); break
    (cov if f else unc).append((k, f))
    print('c0=%d k=%d: %s' % (c0, k, f), flush=True)
print('c0=%d: trivial %d, covered %d, open %s' % (c0, triv, len(cov), [k for k, _ in unc]))
