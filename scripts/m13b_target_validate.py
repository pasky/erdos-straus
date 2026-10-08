"""Validate m13b_target against the complete engine (inv_*.pkl): for random engine boxes of families
II3/I3/I1 with e <= X, run the target search at the box centre (u11 = u13 = r) and require the datum.
usage: m13b_target_validate.py rundir target_binary X E nsamples"""
import glob, pickle, random, subprocess, sys
from m13b_invert import tpart
run, binary, X, E, ns = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
import os; FAMS = tuple(os.environ.get('FAMS', 'II3,I3,I1').split(','))
data = []
for fn in glob.glob(run + '/inv_*.pkl'):
    for (fam, MT, r), P in pickle.load(open(fn, 'rb'))['boxes'].items():
        if fam in FAMS and P[2] <= X and MT > 1 and r % 11 and r % 13:
            data.append((fam, MT, r, P))
random.seed(5); sample = random.sample(sorted(set(data)), ns)
bad = 0
for fam, MT, r, P in sample:
    out = subprocess.run([binary, str(r), str(r), str(P[2] + 3), str(E)], capture_output=True, text=True).stdout
    found = False
    for line in out.split('\n'):
        w = line.split()
        if len(w) < 7 or w[1] != fam: continue
        ev = lambda s: eval(s.split('=')[1].replace('^', '**'))
        a = ev(w[2]) * ev(w[3]); d = ev(w[4]) * ev(w[5]); e = ev(w[6])
        if (a, d, e) == tuple(P): found = True
    if not found:
        bad += 1; print('NOT FOUND', fam, P, MT, r)
print(f'sampled {len(sample)} of {len(data)}, not found {bad}')
