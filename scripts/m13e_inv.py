"""m13e_inv.py — invert the ES solutions of 4/N (output of m13e_es, "x y" lines) to T-generic ET data and
test points (POINTWISE_MORDELL13E §1).  z = 1/(4/N - 1/x - 1/y) is recomputed exactly (must be a positive
integer >= y; any failure aborts).  Inversion = m13b_invert.cands/boxes_of (13B Lemmas 2.1-2.4, validated).
usage: m13e_inv.py N es_files out.pkl [points]   (es_files: comma-separated chunk outputs)   points = "u11,u13;u11,u13" (rationals allowed), default
"2,15;2,2".  Every chunk must end with the "# N=.. xlo=.. xhi=.." completion line of m13e_es, and the chunks must
tile (N/4, 3N/4] exactly (else abort).
Writes {'N','nsol','boxes','hits'} where hits[pt] = list of (fam, P, MT, r)."""
import itertools
import pickle
import sys
from fractions import Fraction

from m13b_invert import cands, boxes_of
from m13e_boxtest import inbox


def main():
    N = int(sys.argv[1])
    pts = sys.argv[4] if len(sys.argv) > 4 else '2,15;2,2'
    pts = [tuple(Fraction(t) for t in p.split(',')) for p in pts.split(';')]
    sols, ranges = [], []
    for fn in sys.argv[2].split(','):
        done = None
        with open(fn) as fh:
            for line in fh:
                if line.startswith('#'):
                    f = dict(t.split('=') for t in line[1:].split())
                    assert int(f['N']) == N and done is None
                    done = (int(f['xlo']), int(f['xhi']))
                    continue
                assert done is None, 'data after completion line'
                x, y = map(int, line.split())
                rest = Fraction(4, N) - Fraction(1, x) - Fraction(1, y)
                assert rest > 0 and rest.numerator == 1, (x, y)
                z = rest.denominator
                assert x <= y <= z
                sols.append((x, y, z))
        assert done, f'{fn} incomplete (no completion line)'
        ranges.append(done)
    ranges.sort()
    assert ranges[0][0] == N // 4 + 1 and ranges[-1][1] == 3 * N // 4, ranges
    assert all(ranges[i][1] + 1 == ranges[i + 1][0] for i in range(len(ranges) - 1)), ranges
    assert len(set(sols)) == len(sols)
    boxes = {}
    hits = {p: [] for p in pts}
    for s in sols:
        for X, Y, Z in set(itertools.permutations(s)):
            for fam, P in cands(N, X, Y, Z):
                for MT, r in boxes_of(fam, P):
                    boxes.setdefault((fam, MT, r), P)
                    for p in pts:
                        if MT == 1 or inbox(MT, r, *p):
                            hits[p].append((fam, P, MT, r))
    print(f"N={N} ES={len(sols)} boxes={len(boxes)} " +
          ' '.join(f'hits{p[0]},{p[1]}={len(h)}' for p, h in hits.items()), flush=True)
    for p, h in hits.items():
        for t in h[:5]:
            print('  HIT', p, t)
    with open(sys.argv[3], 'wb') as fh:
        pickle.dump({'N': N, 'nsol': len(sols), 'boxes': boxes, 'hits': hits}, fh)


if __name__ == '__main__':
    main()
