"""R72 from-scratch exact measure of the union of killed balls in the sign fibre Phi = 9+16Z_2 (Haar, normalised).
Input: lines "B f tmin" (f = 7 mod 16).  Each f kills w in -f + 2^tmin Z_2 (role F) and -f^{-1} + 2^tmin Z_2 (role e).
2-adic balls are nested or disjoint, so the union measure is the sum over maximal balls of 2^(4-t).
Usage: review_typei3_union.py files...   prints uncovered measure, and per-dyadic-bin cumulative values."""
import sys
from fractions import Fraction


def main(files):
    balls = []
    maxf = 0
    for fn in files:
        for line in open(fn):
            if not line.startswith('B '):
                continue
            _, f, t = line.split()
            f, t = int(f), int(t)
            assert f % 16 == 7 and t >= 4
            maxf = max(maxf, f)
            M = 1 << t
            balls.append((t, (-f) % M, f))
            balls.append((t, (-pow(f, -1, M)) % M, f))
    # process in order of f, report cumulative uncovered measure at dyadic boundaries
    balls.sort(key=lambda b: b[2])
    kept = {}  # t -> set of centers
    covered = Fraction(0)
    out = []
    nextb = 1 << 10
    for t, cen, f in balls:
        while f >= nextb:
            out.append((nextb, 1 - covered)); nextb <<= 1
        assert cen % 16 == 9
        contained = any((cen % (1 << tt)) in s for tt, s in kept.items() if tt <= t)
        if contained:
            continue
        # remove kept balls strictly inside the new one
        for tt in list(kept):
            if tt > t:
                inner = {c for c in kept[tt] if c % (1 << t) == cen}
                for c in inner:
                    covered -= Fraction(1, 1 << (tt - 4))
                kept[tt] -= inner
        kept.setdefault(t, set()).add(cen)
        covered += Fraction(1, 1 << (t - 4))
    out.append((maxf + 1, 1 - covered))
    for b, u in out:
        print(f'f < {b}: uncovered {float(u):.6f}')
    print(f'balls {len(balls)}, max f {maxf}, final uncovered {float(1 - covered):.6f}')


if __name__ == '__main__':
    main(sys.argv[1:])
