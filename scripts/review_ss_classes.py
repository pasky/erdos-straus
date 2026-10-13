"""R188: checks of STERILE_STEER Prop 3.1 (class => N-point at every n >= 1; N-point => I1/II2 class) and of
the 13-line remark in Sec. 3, using the from-scratch tables of review_ss_lib.

usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_ss_classes.py [X=600] [NMAX=2000]
"""
import sys
from collections import defaultdict
import review_ss_lib as L

X = int(sys.argv[1]) if len(sys.argv) > 1 else 600
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2000

cls = list(L.classes_upto(X))
R = defaultdict(set)
for fam, P, M, rho in cls:
    R[M].add(rho)
print('classes', len(cls), 'moduli', len(R))

# 1. cross-check with mordell_lib (a posteriori only)
import mordell_lib as ml
bad = [M for M in range(1, X + 1) if R.get(M, set()) != set(ml.residue_set(M))]
print('residue sets differing from mordell_lib for M <=', X, ':', bad[:10], len(bad))

# 2. every n >= 1 in every class gets an N-point (V_I/V_II) and an ES solution
tot = fail = 0
for fam, P, M, rho in cls:
    n = rho if rho > 0 else M
    while n <= NMAX:
        tot += 1
        if L.es_solution(fam, P, n) is None:
            fail += 1
            if fail < 5:
                print('FAIL', fam, P, M, rho, n)
        n += M
print(f'class->N-point: {tot} (class,n) pairs with 1<=n<={NMAX}, failures {fail}')

# 3. N-point => class (I1 / II2), brute force over small V-points of all n <= 300
def vpoints(n, B=60):
    for a in range(1, B):
        for b in range(1, B):
            for d in range(1, B):
                m = 4 * a * b * d
                for T, e in (('I', (m - 1) // n if (m - 1) % n == 0 else 0), ('II', m - n)):
                    if e > 0 and (a + b) % e == 0:
                        yield T, a, b, (a + b) // e, d, e
nv = nbad = 0
for n in range(1, 301):
    for T, a, b, c, d, e in vpoints(n):
        nv += 1
        if T == 'I':
            f = 4 * a * c * d - n; M = 4 * a * d
            ok = f >= 1 and (4 * a * a * d + 1) % f == 0 and (n + f) % M == 0 and (-f) % M in R.get(M, ()) if M <= X else \
                f >= 1 and (4 * a * a * d + 1) % f == 0 and (n + f) % M == 0
        else:
            f = 4 * a * c * d - 1
            ok = (f + 1) % (4 * a * d) == 0 and (n + 4 * a * a * d) % f == 0
        nbad += not ok
print(f'N-point->class: {nv} V-points (a,b,d<60, n<=300), not in the I1/II2 class: {nbad}')

# 4. squares in classes?
sq = [m * m for m in range(1, 101) if any((m * m) % M in rs for M, rs in R.items())]
print('integer squares <= 10^4 lying in a class of modulus <=', X, ':', sq)

# 5. 13-line, level 1: boxes from classes with v_13(M) = 1, rho = 1 mod M'
NR13 = sorted({u for u in range(1, 13)} - {u * u % 13 for u in range(1, 13)})
cov = defaultdict(set)
for fam, P, M, rho in cls:
    if M % 13 == 0 and M % 169 != 0 and rho % (M // 13) == 1 % (M // 13):
        cov[rho % 13].add(M)
print('13-line level-1 boxes, non-residue u -> moduli:', {u: sorted(cov[u])[:6] for u in NR13})
print('non-residues mod 13 not covered at level 1 (M <=', X, '):', [u for u in NR13 if not cov[u]])
