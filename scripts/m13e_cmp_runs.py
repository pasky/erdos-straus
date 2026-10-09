"""m13e_cmp_runs.py — compare per-level box sets of two run dirs (inv_N.pkl) on their common levels.
usage: m13e_cmp_runs.py dirA dirB"""
import glob, os, pickle, sys
A, B = sys.argv[1:3]
na = {os.path.basename(f) for f in glob.glob(A + '/inv_*.pkl')}
nb = {os.path.basename(f) for f in glob.glob(B + '/inv_*.pkl')}
com = sorted(na & nb, key=lambda s: int(s[4:-4])); bad = 0; tot = 0
for f in com:
    a = set(pickle.load(open(f'{A}/{f}', 'rb'))['boxes']); b = set(pickle.load(open(f'{B}/{f}', 'rb'))['boxes'])
    tot += len(a)
    if a != b:
        bad += 1; print('DIFF', f, len(a), len(b), len(a - b), len(b - a))
print(f'common levels {len(com)}, boxes {tot}, differing levels {bad}')
