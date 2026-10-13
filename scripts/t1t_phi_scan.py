"""O183: V_phi(p) via the unit Type II mechanism (Prop 1.2) for all primes p < PMAX; odd squares as T1 control.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_phi_scan.py PMAX KMAX SQMAX
"""
import sys
from sympy import primerange
from t1t_phi import solve_unit_typeII, kseq

PMAX, KMAX, SQMAX = map(int, sys.argv[1:4])
hist, fails = {}, []
for p in primerange(3, PMAX):
    if p == 5:
        continue
    for k in kseq(KMAX):
        r = solve_unit_typeII(p, k, trial=10**5)
        if r is not None and r[0] != 'nonintegral':
            hist[abs(k)] = hist.get(abs(k), 0) + 1
            break
    else:
        fails.append(p)
print('primes <', PMAX, 'min|k| hist', sorted(hist.items()), 'unsolved within |k|<=', KMAX, ':', fails)
bad = [m for m in range(3, SQMAX, 2) if m % 5 and any(solve_unit_typeII(m * m, k, trial=10**5) for k in kseq(KMAX))]
print('odd squares m^2, m <', SQMAX, 'with a unit-TypeII solution:', bad)
