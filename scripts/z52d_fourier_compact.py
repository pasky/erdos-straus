"""Compact a scan file for storage: keep only 'top' entries of conductor ≤ 200 (the ones the cross-window test uses)."""
import sys, json, gzip
from fractions import Fraction
def cond(pid):
    f = 1
    for l, fr in pid:
        d = Fraction(fr).denominator; c = 1
        while d % l == 0: d //= l; c += 1
        f *= l ** c
    return f
with gzip.open(sys.argv[2], 'wt') as out:
    for l in open(sys.argv[1]):
        r = json.loads(l)
        if 'top' in r:
            r['top'] = [t for t in r['top'] if cond(t[0]) <= 200]
        out.write(json.dumps(r, separators=(',', ':')) + '\n')
