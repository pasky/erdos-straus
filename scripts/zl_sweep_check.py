"""zl_sweep_check.py -- O228 validation of zl_sweep.c against the per-n enumerators of R223 (review_se2_identities):
(1) 'all' mode with A = X1, Y = 0: JP(n) = #P-data, JQ(n) = #Q-data for every odd n in [X0, X1);
(2) prime mode with given A, Y: JQ(n) = #{Q-data of n: a < A, a d > Y} for every prime n; JP(n) as in (1)."""
import sys, subprocess, os
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se2_identities import P_data, Q_data
from sympy import isprime
X0, X1, A, Y, exe = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
for mode in ('all', 'prime'):
    a_, y_ = (X1, 0) if mode == 'all' else (A, Y)
    args = [exe, str(X0), str(X1), str(a_), str(y_), '4'] + (['all'] if mode == 'all' else [])
    out = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, ZL_DUMP='1')).stdout
    bad = tot = 0
    for line in out.splitlines():
        if not line.startswith('N '): continue
        _, n, jp, jq = line.split(); n, jp, jq = int(n), int(jp), int(jq)
        if mode == 'prime' and not isprime(n): continue
        p = len(P_data(n)); q = sum(1 for (a, b, c, d, e, f) in Q_data(n) if a < a_ and a * d > y_)
        tot += 1
        if (p, q) != (jp, jq): bad += 1; print('mismatch', mode, n, p, jp, q, jq)
    print(f'{mode}: X0={X0} X1={X1} A={a_} Y={y_}: {tot} n checked, mismatches {bad}')
