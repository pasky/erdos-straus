# z53 GENUSX: u-side character-order ladder over exact divisors, reusing Mhat from earlier TSVs.
# For each row (tag, n, Mhat, window) of the given TSVs, rerun the engine (mode E) and record
#   R, G (=K=2), G4, G6, G12, G120 (projection of the exact class onto characters chi mod 8u with chi^K = 1), Mhat.
# Usage: uv run --with numpy python scripts/z53_genusx_ladder.py OUT.tsv IN1.tsv IN2.tsv ...   (env ENG = engine binary)
import sys, os, subprocess
import numpy as np
ENG = os.environ.get('ENG', '/tmp/z53gx2')
out = open(sys.argv[1], 'w')
out.write('tag\tn\tR\tG\tG4\tG6\tG12\tG120\tMhat\n')
rows = []
for fn in sys.argv[2:]:
    for line in open(fn):
        if line.startswith('tag'): continue
        t = line.rstrip('\n').split('\t')
        rows.append((t[0], int(t[1]), t[10], t[-4:]))
for tag, n, M, (U0, U1, Y, X) in rows:
    r = subprocess.run([ENG, 'E', str(n), U0, U1, Y, X], capture_output=True, text=True, timeout=600)
    kv = dict(x.split('=') for x in r.stdout.split())
    out.write('\t'.join([tag, str(n), kv['R'], kv['G'], kv['G4'], kv['G6'], kv['G12'], kv['G120'], M]) + '\n')
out.close()
# summary: share of var(R - M) explained by var(G_K - M), and var(R - G_K)/(2 mean G_K)
d = {}
for line in open(sys.argv[1]):
    if line.startswith('tag'): continue
    t = line.split('\t'); d.setdefault(t[0], []).append([float(x) for x in t[2:9]])
print('tag N | var(GK-M)/var(R-M) for K=2,4,6,12,120 | var(R-GK)/var(R-M) for K=2,4,6,12,120 | mean GK/M')
for tag, A in d.items():
    A = np.array(A); A = A[(A[:, 6] > 0) & ~np.isnan(A[:, 6])]
    if len(A) < 5: continue
    R, M = A[:, 0], A[:, 6]; vRM = (R - M).var()
    a = [((A[:, k] - M).var() / vRM) for k in range(1, 6)]
    b = [((R - A[:, k]).var() / vRM) for k in range(1, 6)]
    c = [(A[:, k] / M).mean() for k in range(1, 6)]
    print(tag, len(A), '|', ' '.join('%.3f' % x for x in a), '|', ' '.join('%.3f' % x for x in b), '|', ' '.join('%.3f' % x for x in c))
