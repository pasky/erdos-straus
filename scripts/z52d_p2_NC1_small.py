# z52d pass2 NC1 small checks: Z1259 mutation test of an exact certificate checker; Z1358 Rademacher-type Dedekind identity vacuity;
# Z1322 LP relaxation feasibility (p=409, integer candidates in [p/4,3p/4], w in [0,1]).
import random, math, json
from fractions import Fraction as F
from fractions import Fraction
from sympy import primerange, divisors
from collections import Counter
from scipy.optimize import linprog
import numpy as np
random.seed(0)
def sols(n):
    out = set()
    for x in range((n+3)//4, (3*n)//4+1):
        a = 4*x-n
        if a <= 0: continue
        b = n*x
        g = math.gcd(a, b); a2, b2 = a//g, b//g
        for d in divisors(b*b):
            if (d+b) % a == 0 or True:
                pass
        # exact: solve (a y - b)(a z - b) = b^2 via divisors of b^2
        for d in divisors(b*b):
            if (d+b) % a: continue
            dp = b*b//d
            if (dp+b) % a: continue
            y = (d+b)//a; z = (dp+b)//a
            if y >= 1 and z >= 1: out.add(tuple(sorted((x, y, z))))
    return sorted(out)
def check(n, xs):
    if any(x <= 0 for x in xs): return False
    return sum(F(1, x) for x in xs) == F(4, n)
# Z1259 mutations
base = []
for n in [p for p in primerange(5, 400) if p % 24 == 1][:25]:
    for s in sols(n)[:6]:
        base.append((n, s))
muts = Counter(); survived = Counter()
kinds = {
 'sign_flip_x': lambda n,s: (n, (-s[0],)+s[1:]),
 'x_plus_1': lambda n,s: (n, (s[0]+1,)+s[1:]),
 'y_times_2': lambda n,s: (n, (s[0], 2*s[1], s[2])),
 'n_plus_4': lambda n,s: (n+4, s),
 'drop_term': lambda n,s: (n, s[:2]),
 'residue_shift_4C': lambda n,s: (n, (s[0], s[1], s[2]+4)),
 'swap_then_mutate': lambda n,s: (n, (s[1], s[0]+1, s[2])),
}
for name, fn in kinds.items():
    for n, s in base:
        n2, s2 = fn(n, s)
        muts[name] += 1
        if check(n2, list(s2)): survived[name] += 1
# sanity: unmutated base solutions must all pass
base_ok = sum(check(n, list(s)) for n, s in base)
# Z1358: Dedekind sums and Rademacher three-term identity s(bc,a)+s(ca,b)+s(ab,c) = -1/4 + (a^2+b^2+c^2)/(12abc)
def ded(h, k):
    # Dedekind sum s(h,k), k>0
    from fractions import Fraction
    if k == 1: return Fraction(0)
    s = Fraction(0)
    for i in range(1, k):
        t = Fraction(i, k) - Fraction(1, 2)
        u = (h*i) % k
        if u == 0: continue
        s += t*(Fraction(u, k) - Fraction(1, 2))
    return s
ded_tests = 0; ded_ok = 0
for _ in range(300):
    a, b, c = random.randint(2, 40), random.randint(2, 40), random.randint(2, 40)
    if math.gcd(a, b) != 1 or math.gcd(b, c) != 1 or math.gcd(a, c) != 1: continue
    lhs = ded(b*c, a) + ded(c*a, b) + ded(a*b, c)
    rhs = Fraction(-1, 4) + Fraction(a*a+b*b+c*c, 12*a*b*c)
    ded_tests += 1; ded_ok += int(lhs == rhs)
# Z1322 LP: 4/p = sum w_x / x, sum w_x = 3, 0<=w_x<=1 over integer candidates x in [ceil(p/4), 2p]
p = 409
xs = list(range(math.ceil(p/4), 2*p+1))  # candidate denominators (all three terms may be large; x<=3p/4 is only the smallest-term bound)
A_eq = np.array([[1.0/x for x in xs], [1.0 for x in xs]]); b_eq = np.array([4.0/p, 3.0])
res = linprog(c=np.zeros(len(xs)), A_eq=A_eq, b_eq=b_eq, bounds=[(0, 1)]*len(xs), method='highs')
out = {'Z1259_mutations': {k: {'tested': muts[k], 'accepted_as_valid': survived[k]} for k in kinds},
       'Z1259_unmutated_base_pass': f'{base_ok}/{len(base)}',
       'Z1358_pairwise_coprime_triples_tested': ded_tests, 'Z1358_identity_holds': ded_ok,
       'Z1322_LP_p409': {'status': int(res.status), 'message': res.message, 'n_candidates': len(xs), 'candidate_range': 'ceil(p/4)..2p'}}
print(json.dumps(out, indent=1))
