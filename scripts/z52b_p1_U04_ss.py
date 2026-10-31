"""Z1385 detail: fraction of primes-level witness sets S=divisor residues mod m with S*S == S, and mean |SS|/|S|."""
import json, sys
sys.argv = ['x']
src = open('scripts/z52b_p1_U04_witness.py').read().split("ps = [p for p")[0]
ns = {}
exec(src.replace("PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000", "PMAX=20000").replace("CMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 30", "CMAX=30").replace("import sys, json",""), ns)
factor, dp_residues, primes_upto = ns['factor'], ns['dp_residues'], ns['primes_upto']
ps = [p for p in primes_upto(20000) if p % 4 == 1 and p > 5]
eq = 0; ratio = []; n = 0
for p in ps[:400]:
    for C in range(1, 31):
        m = 4 * C
        S = set(dp_residues(factor(m * p + 1), m))
        SS = {a * b % m for a in S for b in S}
        n += 1; eq += (SS == S); ratio.append(len(SS) / len(S))
res = dict(n=n, frac_SS_equals_S=round(eq / n, 4), mean_SS_over_S=round(sum(ratio) / len(ratio), 4))
print(json.dumps(res)); json.dump(res, open('data/z52b/pass1/U04/Z1385_SS.json', 'w'))
