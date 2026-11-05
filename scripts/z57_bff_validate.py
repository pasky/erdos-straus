#!/usr/bin/env python3
"""Validate z57_bff_engine against z56 certified data: F4 (= G*) hit counts."""
import sys, random, gzip
sys.path.insert(0, 'scripts')
from z57_bff_engine import gstar_solutions, hits_by_d, in_gstar

random.seed(57)
bad = 0
# 1) zeros_le1e8: column 9 = F4 hits, for every prime with a zero in some family
rows = []
with open('data/z56/famdesign/zeros_le1e8.txt') as f:
    for line in f:
        if line.startswith('#'):
            continue
        t = line.split()
        rows.append((int(t[0]), int(t[8])))
sample = random.sample(rows, 400) + [r for r in rows if r[1] == 0]
for p, f4 in sample:
    got = len(gstar_solutions(p))
    if got != f4:
        bad += 1
        print('MISMATCH zeros_le1e8', p, f4, got)
print('checked', len(sample), 'rows of zeros_le1e8; bad =', bad)
# 2) decide file (1e7..1e10): column 5 = F4 hits
rows = []
with open('data/z56/famdesign/decide_1e7_1e10.txt') as f:
    for line in f:
        if line.startswith('#') or not line[0].isdigit():
            continue
        t = line.split()
        if len(t) >= 6:
            rows.append((int(t[0]), int(t[4])))
sample = random.sample(rows, 60)
for p, f4 in sample:
    got = len(gstar_solutions(p))
    if got != f4:
        bad += 1
        print('MISMATCH decide', p, f4, got)
print('checked', len(sample), 'rows of decide; bad =', bad)
print('564661441 ->', gstar_solutions(564661441))
