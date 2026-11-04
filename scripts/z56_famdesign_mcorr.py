# EVIDENCE: at the mgen_split primes, compare the exact counts R_F = 2 hits_F (z56scan) with the exact genus parts:
# G-part (F4 = A∩G) vs M_G, corner K vs M_K, all vs M_gen. Prints ratio means and correlations per set.
import sys, statistics as st
scan = {int(l.split()[0]): list(map(int, l.split()[1:])) for l in open(sys.argv[2])}
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])][1:]
COLS = ['all', 'F0', 'F1', 'F2U', 'F2S', 'F3U', 'F3S', 'F4', 'F4L', 'K', 'H3', 'HC']
def corr(x, y):
    mx, my = st.mean(x), st.mean(y); sx = sum((a - mx) ** 2 for a in x) ** .5; sy = sum((b - my) ** 2 for b in y) ** .5
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy) if sx * sy > 0 else float("nan")
for tag in ['test', '1e6', '1e7', '1e8', '1e9']:
    R = [r for r in rows if r[-1] == tag]
    if len(R) < 3: continue
    p = [int(r[0]) for r in R]; v = {k: [float(r[i]) for r in R] for i, k in enumerate(['L2', 'M0', 'M0G', 'Mgen', 'MG', 'MK', 'MGl', 'M0Gl'], 1)}
    RG = [2 * scan[q][COLS.index('F4')] for q in p]; RK = [2 * scan[q][COLS.index('K')] for q in p]; RA = [2 * scan[q][0] for q in p]
    out = [f'{tag:4s} n={len(p):2d}', 'R_G/M_G %.3f' % st.mean([a / b for a, b in zip(RG, v['MG'])]),
           'R_K/M_K %.3f' % st.mean([a / b for a, b in zip(RK, v['MK']) if b > 0]),
           'corr(R_G,M_G) %.2f' % corr(RG, v['MG']), 'corr(R_K,M_K) %.2f' % corr(RK, v['MK']), 'corr(R,Mgen) %.2f' % corr(RA, v['Mgen']),
           'sd(R_G/M_G) %.3f' % st.pstdev([a / b for a, b in zip(RG, v['MG'])])]
    print('  '.join(out))
