"""U02 batch, items Z0259, Z0868, Z0872, Z0277 (cheap structural checks). Uses z52b_p1_U02_lib.esols."""
import sys, json
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
from sympy import primerange, isprime
res = {}
# Z0259: repeated denominators for p = 1 mod 4 (p < 3000)
P1 = [p for p in primerange(5, 3000) if p % 4 == 1]
rep = []
for p in P1:
    S = esols(p)
    r = [s for s in S if s[0] == s[1] or s[1] == s[2]]
    if r: rep.append((p, len(r), r[:2]))
res['Z0259'] = {'primes_1mod4_tested': len(P1), 'primes_with_repeated_denominator': rep[:20], 'n_such_primes': len(rep)}
# Z0868: odd n, count solutions with < 2 even denominators
Odd = [n for n in range(3, 1200, 2)]
bad = []
tot = 0
for n in Odd:
    for s in esols(n):
        tot += 1
        if sum(1 for v in s if v % 2 == 0) < 2:
            bad.append((n, s)); break
res['Z0868'] = {'odd_n_tested': len(Odd), 'solutions_total': tot, 'odd_n_with_violating_solution': bad[:10], 'n_violations': len(bad)}
# Z0872: F4 = {n : no solution with 4 not dividing x*y*z}
F4 = []
for n in range(2, 1001):
    S = esols(n)
    if all(any(v % 4 == 0 for v in s) for s in S):
        F4.append(n)
res['Z0872'] = {'n_tested': 999, 'F4_count': len(F4), 'F4_first': F4[:40],
                'F4_not_mult16': [n for n in F4 if n % 16 != 0][:40],
                'mult16_not_in_F4': [n for n in range(16, 1001, 16) if n not in F4][:40]}
# Z0277: 4/n = sum of 3 terms 1/(c s_i^2), c in {1,2,3,5,6}, n <= 600
def sq3(n, c):
    # 4/n = sum_{i=1..3} 1/(c*s_i^2), s_1<=s_2<=s_3; each term >= 4/(3n) => c s^2 <= 3n/4 * ... use bound s^2 <= 3*c*n/4 for max term
    # max term 1/(c s1^2) >= (4/n)/3 => c*s1^2 <= 3n/4 ; but all terms: s_i^2 <= 3*c*n/4 (since 1/(c s^2) <= 4/n)
    B = int((3 * c * n / 4) ** 0.5) + 1
    target = 4 * 1  # compare fractions via integers: 4/n = sum 1/(c s_i^2)
    from fractions import Fraction
    t = Fraction(4, n)
    sq = [s * s for s in range(1, B + 1)]
    for i, a in enumerate(sq):
        ta = t - Fraction(1, c * a)
        if ta <= 0: continue
        for j in range(i, len(sq)):
            b = sq[j]
            tb = ta - Fraction(1, c * b)
            if tb <= 0: continue
            # need 1/(c s3^2) = tb -> c*s3^2 = 1/tb
            if tb.numerator == 1 and (tb.denominator % c == 0):
                s3sq = tb.denominator // c
                if s3sq >= b and int(s3sq ** 0.5) ** 2 == s3sq:
                    return True
    return False
cnt = {}
for c in (1, 2, 3, 5, 6):
    ok = [n for n in range(2, 601) if sq3(n, c)]
    cnt[c] = {'count_yes': len(ok), 'first_yes': ok[:25], 'frac_yes': round(len(ok) / 599, 3)}
res['Z0277'] = cnt
json.dump(res, open('data/z52b/pass1/U02/cheap_a.json', 'w'), indent=1, default=str)
for k, v in res.items():
    print(k, str(v)[:700])
