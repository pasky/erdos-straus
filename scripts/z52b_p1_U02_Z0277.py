"""Z0277: which n admit 4/n = 1/(c s1^2) + 1/(c s2^2) + 1/(c s3^2) (3 square-type terms), c in {1,2,3,5,6}, n <= N.
Bounds (sorted s1<=s2<=s3, t = 4/n): the largest term >= t/3 so c*s1^2 <= 3n/4 (s1 bounded);
given s1, rem = t - 1/(c s1^2) > 0 and the larger of the last two terms >= rem/2, so s2^2 <= 2/(c*rem) (s2 bounded);
s3 is then forced by the remainder. Exact rational arithmetic throughout."""
import sys, json, math
from fractions import Fraction
sys.path.insert(0, 'scripts')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600

def sq3(n, c):
    t = Fraction(4, n)
    s1max = int(math.isqrt((3 * n) // (4 * c))) + 1
    for s1 in range(1, s1max + 1):
        rem1 = t - Fraction(1, c * s1 * s1)
        if rem1 <= 0: continue
        s2max = int(math.isqrt(int(2 / (c * rem1)) + 1)) + 1
        for s2 in range(s1, s2max + 1):
            rem2 = rem1 - Fraction(1, c * s2 * s2)
            if rem2 <= 0: continue
            if rem2.numerator == 1 and rem2.denominator % c == 0:
                s3sq = rem2.denominator // c
                s3 = math.isqrt(s3sq)
                if s3 * s3 == s3sq and s3 >= s2:
                    return (s1, s2, s3)
    return None

res = {}
for c in (1, 2, 3, 5, 6):
    ok = {n: sq3(n, c) for n in range(2, N + 1)}
    yes = [n for n in ok if ok[n]]
    res[c] = {'count_yes': len(yes), 'frac_yes': round(len(yes) / (N - 1), 4), 'first_yes': [(n, ok[n]) for n in yes[:12]],
              'yes_all_div4': all(n % 4 == 0 for n in yes), 'n_yes_not_div4': [n for n in yes if n % 4][:10]}
json.dump(res, open('data/z52b/pass1/U02/Z0277_sq3.json', 'w'), indent=1, default=str)
for c in res: print(c, res[c]['count_yes'], res[c]['frac_yes'], res[c]['yes_all_div4'], res[c]['n_yes_not_div4'], res[c]['first_yes'][:6])
