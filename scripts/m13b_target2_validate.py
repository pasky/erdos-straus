"""Validate m13b_target2 against the engine: random engine boxes of I2/II1/I4 (h <= X, ratio exponents
<= E), target search at the box centre must report the datum or a datum with a box containing the centre
at a lower-or-equal level with the same family (s = common T-factor is dropped, Lemma in §5).
usage: m13b_target2_validate.py rundir binary X E nsamples"""
import glob, pickle, random, subprocess, sys
from m13b_invert import tpart, boxes_of
run, binary, X, E, ns = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
data = []
for fn in glob.glob(run + '/inv_*.pkl'):
    for (fam, MT, r), P in pickle.load(open(fn, 'rb'))['boxes'].items():
        if fam in ('I2', 'II1', 'I4') and P[2] <= X and MT > 1 and r % 11 and r % 13:
            data.append((fam, MT, r, P))
random.seed(7); sample = random.sample(sorted(set(data)), ns)
bad = 0
for fam, MT, r, P in sample:
    out = subprocess.run([binary, str(r), str(r), str(P[2] + 3), str(E)], capture_output=True, text=True).stdout
    found = False
    for line in out.split('\n'):
        w = line.split()
        if len(w) < 5 or w[1] != fam: continue
        ev = lambda s: eval(s.split('=')[1].replace('^', '**'))
        Q = (ev(w[2]), ev(w[3]), ev(w[4]))
        if Q[2] != P[2]: continue
        if any(MT % M2 == 0 and r % M2 == r2 for M2, r2 in boxes_of(fam, Q)): found = True
    if not found:
        bad += 1; print('NOT FOUND', fam, P, MT, r)
print(f'sampled {len(sample)} of {len(data)}, not found {bad}')
