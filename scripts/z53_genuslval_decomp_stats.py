"""§4 EVIDENCE: genus-character decomposition (z53_genuslval_decomp.c) at the 14 (star)-zero primes vs matched controls.
For each failure p, up to 60 random primes p' = 1 (mod 8) in [0.9p, 1.1p] (all of them if fewer; seed 53) are decomposed too; reports, per category,
the failure's value / log^2 p and its percentile among the controls.  Output: data/z53/genuslval/decomp_stats.txt (+ raw tsv).
Usage: uv run --with sympy python scripts/z53_genuslval_decomp_stats.py
"""
import random, subprocess, math, os
from sympy import isprime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
EXE = '/tmp/z53dec'
if not os.path.exists(EXE):
    subprocess.check_call(['gcc', '-O2', '-o', EXE, os.path.join(HERE, 'z53_genuslval_decomp.c')])
FAIL = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
random.seed(53)
out = []; raw = []
cats = ['P', 'C4', 'CBM', 'CU0', 'CMIX', 'total']
def run(ps):
    res = subprocess.run([EXE] + [str(x) for x in ps], capture_output=True, text=True, check=True).stdout.strip().split('\n')[1:]
    return {int(l.split()[0]): [float(x) for x in l.split()[1:]] for l in res}
summary = {c: [] for c in cats}; deficit = {c: [] for c in cats}
for p in FAIL:
    lo, hi = int(0.9 * p) + 1, int(1.1 * p)
    allc = [q for q in range(lo - (lo % 8) + 1, hi + 1, 8) if lo <= q <= hi and q != p and q not in FAIL and isprime(q)]
    ctr = set(random.sample(allc, min(60, len(allc))))
    vals = run([p] + sorted(ctr))
    L2 = math.log(p) ** 2
    line = [f"{p:>8} (n_ctl={len(ctr)})"]
    for k, c in enumerate(cats):
        fv = vals[p][k]
        cv = [vals[q][k] for q in ctr]
        pct = 100.0 * sum(1 for x in cv if x < fv) / len(cv)
        mean = sum(cv) / len(cv)
        summary[c].append(pct); deficit[c].append((mean - fv) / L2)
        line.append(f"{c}={fv/L2:+.4f}(ctl {mean/L2:+.4f}, pct {pct:5.1f})")
    out.append("  ".join(line))
    for q, v in vals.items():
        raw.append("\t".join([str(q), str(int(q == p))] + [f"{x:.6f}" for x in v]))
hdr = ("Genus decomposition of the u=1 (4) squarefree slices (one order), values / log^2 p; failure vs up to 60 matched "
       "controls p'=1 (8) in [0.9p,1.1p].\nP = principal genus (eta=1); C4 = chi_{-4} twist; CBM = (./u)chi_{-4} "
       "(eta chi_D = chi_p); CU0 = (./u); CMIX = 1<d<u.\n")
txt = hdr + "\n".join(out) + "\n\nmean percentile of the 14 failures: " + \
      ", ".join(f"{c} {sum(v)/len(v):.1f}" for c, v in summary.items()) + \
      "\nmean (control mean - failure)/log^2 p: " + ", ".join(f"{c} {sum(v)/len(v):+.6f}" for c, v in deficit.items()) + "\n"
open(os.path.join(ROOT, 'data/z53/genuslval/decomp_stats.txt'), 'w').write(txt)
open(os.path.join(ROOT, 'data/z53/genuslval/decomp_raw.tsv'), 'w').write(
    "p\tis_fail\t" + "\t".join(cats) + "\n" + "\n".join(raw) + "\n")
print(txt)
