"""review_fsp_measure.py (R179): covered slice measure from the reviewer's own solution list
(data/review_fsp_enum*.txt, produced by review_fsp_enum.py). Cylinder of a level-K solution: v ≡ -H L' (mod T^N0),
N0 = max(2, ceil(K/2) + 1), v = (u - 1)/T; measure = normalised Haar on v with v(0) != 0. Exact rationals.
usage: PYTHONPATH=scripts uv run python scripts/review_fsp_measure.py data/review_fsp_enum12.txt"""
import sys
from fractions import Fraction
from review_fsp_poly import F

R = F(3)

def parse(sx):
    return R.norm([int(ch) for ch in sx]) if sx != '0' else ()

def main():
    rows = [l.split() for l in open(sys.argv[1])]
    KMAX = max(int(r[0]) for r in rows)
    cyl = set()
    for K in range(2, KMAX + 1):
        for r in rows:
            if int(r[0]) != K:
                continue
            H, gp, Lpp = parse(r[3]), parse(r[5]), parse(r[6])
            N0 = max(2, -(-K // 2) + 1)
            v = R.neg(R.mul(H, R.mul(gp, Lpp)))
            digits = tuple((list(v) + [0] * N0)[:N0])
            assert digits[0] != 0
            cyl.add(digits)
        # union measure: drop cylinders contained in a shorter one
        mins = [c for c in cyl if not any(len(d) < len(c) and c[:len(d)] == d for d in cyl)]
        mins = set(mins)
        meas = sum(Fraction(1, 3 ** len(c)) for c in mins) / Fraction(2, 3)
        print("K <= %2d: covered slice measure %s = %.4f  (%d maximal cylinders)" % (K, meas, float(meas), len(mins)))

if __name__ == '__main__':
    main()
