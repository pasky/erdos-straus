"""O154 driver: build primes of a design (scripts/bs_adv_construct.c), count exact f_II(p)
(scripts/bs_adv_count.c), verify the reported Type II solution with exact fractions, record features.
Usage: PYTHONPATH=scripts uv run python scripts/bs_adv_run.py TAG X M r K seed "S2" "S1" [E]
(X = @file: read the primes from file instead.) Appends JSON lines to logs/bs_adv_TAG.jsonl (small)."""
import sys, subprocess, json, math
from fractions import Fraction
from concurrent.futures import ThreadPoolExecutor
from sympy import factorint, divisor_count

tag, X, M, r, K, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
S2 = sys.argv[7] if len(sys.argv) > 7 else ''
S1 = sys.argv[8] if len(sys.argv) > 8 else ''
Earg = sys.argv[9:10]
ps = (open(X[1:]).read().split() if X.startswith('@') else
      subprocess.run(['/tmp/bs_adv_construct', X, M, r, K, seed, S2, S1], capture_output=True, text=True).stdout.split())


def tau(n):
    return int(divisor_count(n))


def one(p):
    p = int(p)
    out = subprocess.run(['/tmp/bs_adv_count', str(p)] + Earg, capture_output=True, text=True).stdout.split()
    f, A, B = int(out[1]), int(out[2]), int(out[3])
    Xs = [int(x) for x in out[5:13]]
    emin, Wmin = int(out[15]), int(out[17])
    a, b, c, d, e = (int(x) for x in out[19:24])
    ok = f > 0 and Fraction(4, p) == Fraction(1, a*b*d) + Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p)
    fp = factorint(p - 1)
    L = math.log(p)
    rec = dict(tag=tag, p=p, f=f, partA=A, partB=B, Xs=Xs, emin=emin, Wmin=Wmin, verified=ok,
               fL3=f / L**3, tau_pm1=math.prod(v + 1 for v in fp.values()), omega_pm1=len(fp),
               s16=sum(tau((p + e) // 4) for e in range(1, 17) if (p + e) % 4 == 0))
    return rec


with ThreadPoolExecutor(2) as ex:
    recs = list(ex.map(one, ps))
with open(f'logs/bs_adv_{tag}.jsonl', 'a') as fh:
    for rec in recs:
        fh.write(json.dumps(rec) + '\n')
fl = [r['fL3'] for r in recs]
print(tag, len(recs), 'min f', min(r['f'] for r in recs), 'mean f/L3 %.4f min %.4f' % (sum(fl)/len(fl), min(fl)),
      'all verified', all(r['verified'] for r in recs), 'mean tau(p-1) %.1f' % (sum(r['tau_pm1'] for r in recs)/len(recs)))
