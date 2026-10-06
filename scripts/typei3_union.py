"""O72: exact Haar measure (normalised on 9+16Z_2) of the union of 2-adic balls killed by certificates,
from 'B f tmin' lines of `typei3_fsearch r w lo hi mass` (role F: ball -f + 2^t Z_2; role e: -f^{-1} + 2^t Z_2).
Prints the uncovered measure after each dyadic f-bound.  Usage: typei3_union.py ballfile [ballfile...]"""
import sys
P = 40
balls = []
for fn in sys.argv[1:]:
    for line in open(fn):
        if line.startswith('B '):
            _, f, t = line.split(); f = int(f); t = int(t)
            m = 1 << P
            balls.append((f, t, (-f) % m)); balls.append((f, t, (-pow(f, -1, m)) % m))
balls.sort()
# maintain a set of disjoint covered balls (center mod 2^t, t); measure relative to 9+16Z_2
covered = {}  # t -> set of residues mod 2^t

def is_covered(c, t):
    for tt, S in covered.items():
        if tt <= t and (c % (1 << tt)) in S:
            return True
    return False

meas = 0.0; nb = 0; nextb = 1
out = []
for f, t, c in balls:
    while f >= nextb:
        out.append((nextb, 1 - meas)); nextb *= 2
    if c % 16 != 9 or is_covered(c, t):
        continue
    # remove sub-balls contained in the new ball
    for tt in list(covered):
        if tt > t:
            S = covered[tt]
            rm = {x for x in S if x % (1 << t) == c % (1 << t)}
            for x in rm:
                meas -= 2.0 ** (4 - tt)
            S -= rm
    covered.setdefault(t, set()).add(c % (1 << t)); meas += 2.0 ** (4 - t); nb += 1
out.append((nextb, 1 - meas))
for b, u in out:
    if b >= 2 ** 6:
        print(f'f < 2^{b.bit_length()-1}: uncovered measure of 9+16Z_2 = {u:.6f}')
