"""z56 PRIMET1 S3 (Z56_PRIMET1.md §3.5): the 14 (★)-zeros vs matched controls.
For each zero p0: 50 controls in P24 with R > 0, same p mod 35 and p mod 16, nearest in |log p - log p0| (from the sieve file).
Per family a pre-registered scalar; per-zero mid-rank percentile; two-sided Fisher combination; permutation null (each
replicate replaces every zero by a random member of its own matched set); Holm over the 16 families.
Usage: uv run --with cypari2 --with numpy --with scipy python z56_primet1_s3.py SIEVE_1e8.bin OUTPREFIX
"""
import sys, math, subprocess
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_feat import DT, init, one
import z56_primet1_feat as zf
from z56_primet1_tests import families, holm, FAMS, v_adic

ZEROS = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]

def scalars(feat, cf):
    F = families(feat, cf)
    h4 = feat['h4'].astype(np.int64); p = feat['p'].astype(np.float64); L = np.log(p)
    s = {'G1': F['G1'][0][:, 0], 'G2': v_adic(h4, 2).astype(float), 'G3': (h4 % 3 == 0).astype(float),
         'G4': (feat['hR'] > 1).astype(float), 'G5': F['G5'][0][:, 0], 'G6': F['G6'][0][:, 0], 'G7': F['G7'][0][:, 0],
         'G8': v_adic(feat['i2'].astype(np.int64), 2).astype(float), 'G9': v_adic(feat['i3'].astype(np.int64), 2).astype(float),
         'G10': feat['r3'].astype(float), 'G11': feat['r4'].astype(float), 'G12': F['G12'][0][:, 0], 'G13': F['G13'][0][:, 0],
         'G14': v_adic((feat['p'] - np.uint64(1)).astype(np.int64), 2).astype(float), 'G15': F['G15'][0].sum(1),
         'G16': F['G16'][0][:, 0]}
    return s

def midp(x0, xc):
    n = len(xc); less = np.sum(xc < x0); eq = np.sum(xc == x0)
    u = (less + 0.5 * eq + 0.5) / (n + 1)
    return min(1.0, 2 * min(u, 1 - u))

if __name__ == '__main__':
    d = np.fromfile(sys.argv[1], dtype=np.dtype([('p', '<u8'), ('r', '<u2')]))
    P = d['p'].astype(np.int64); Rr = d['r']; lp = np.log(P.astype(float))
    sets = []
    for z in ZEROS:
        m = (P % 35 == z % 35) & (P % 16 == z % 16) & (Rr > 0)
        idx = np.nonzero(m)[0]; o = idx[np.argsort(np.abs(lp[idx] - math.log(z)))[:50]]
        sets.append([z] + P[o].tolist())
    allp = sorted(set(x for s in sets for x in s))
    init()
    feats = np.array([one(p) for p in allp], dtype=DT)
    cfo = subprocess.run([sys.argv[3] if len(sys.argv) > 3 else './cfper'], input='\n'.join(map(str, allp)) + '\n',
                         capture_output=True, text=True).stdout.split('\n')
    cf = {int(l.split()[0]): float(l.split()[1]) for l in cfo if l.strip()}
    S = scalars(feats, np.array([cf[int(p)] for p in feats['p']]))
    pos = {int(p): i for i, p in enumerate(feats['p'])}
    rng = np.random.default_rng(56)
    rows = []; per = []
    for g in FAMS:
        x = S[g]
        def fisher(choice):
            st = 0.0
            for k, s in enumerate(sets):
                vals = np.array([x[pos[q]] for q in s]); j = choice[k]
                st += -2 * math.log(midp(vals[j], np.delete(vals, j)))
            return st
        obs = fisher([0] * len(sets))
        null = np.array([fisher(rng.integers(0, 51, len(sets))) for _ in range(4000)])
        pv = (1 + np.sum(null >= obs)) / (1 + len(null))
        rows.append((g, obs, pv))
        for k, s in enumerate(sets):
            vals = np.array([x[pos[q]] for q in s]); per.append((g, s[0], vals[0], np.median(vals[1:]), midp(vals[0], vals[1:])))
    adj = holm([r[2] for r in rows])
    with open(sys.argv[2] + '_s3.tsv', 'w') as f:
        f.write('family\tfisher_stat\tp_perm\tp_holm\n')
        for r, a in zip(rows, adj): f.write('%s\t%.3f\t%.4f\t%.4f\n' % (r + (a,)))
    with open(sys.argv[2] + '_s3_perzero.tsv', 'w') as f:
        f.write('family\tzero\tvalue\tcontrol_median\ttwo_sided_midp\n')
        for r in per: f.write('%s\t%d\t%.4g\t%.4g\t%.3f\n' % r)
    with open(sys.argv[2] + '_s3_zerofeat.tsv', 'w') as f:
        f.write('\t'.join(DT.names) + '\tcflen\n')
        for z in ZEROS + [193, 2521, 66529, 3361, 5101441]:
            if z not in pos:
                row = one(z); cfz = subprocess.run([sys.argv[3] if len(sys.argv) > 3 else './cfper'], input=f'{z}\n', capture_output=True, text=True).stdout.split()[1]
            else:
                row = tuple(feats[pos[z]]); cfz = cf[z]
            f.write('\t'.join(str(v) for v in row) + f'\t{cfz}\n')
    print(open(sys.argv[2] + '_s3.tsv').read())
