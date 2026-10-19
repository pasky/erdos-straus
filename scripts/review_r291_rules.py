"""R291: from-scratch check of Thm 4.1 (3*2^s+1), Lemma 4.3 (63), Lemma 4.8 (105),
Remark 4.2(ii) cubic Type II family, and the small-s / coverage claims around them."""
import sys
from math import lcm
from fractions import Fraction as F
from review_r291_poly import *

SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
OK = True


def report(rule, claimed_mod, claimed_res):
    global OK
    Pi, thr, S = rule.period_set()
    L = lcm(Pi, claimed_mod)
    der = {s for s in range(L) if s % Pi in S}
    cl = {s for s in range(L) if s % claimed_mod in claimed_res}
    sub_ok = cl <= der
    OK &= sub_ok
    print(f'  {rule.name}: period {Pi}, thr {thr}, derived residues mod {Pi}: '
          f'{sorted(S)[:10]}{"..." if len(S) > 10 else ""}; claimed {sorted(claimed_res)} mod {claimed_mod}:'
          f' {"subset OK" if sub_ok else "NOT SUBSET"}{"" if der == cl else " (derived larger)"}')
    return thr


# ---------------- 3*2^s+1 ----------------
print('== Thm 4.1: 3*2^s+1')
n3 = lambda s: 3 * 2 ** s + 1
X = P(0, 1)
nX = P(1, 0, 0, 0, 48)
fp, fm = P(1, 2, 2), P(1, -2, 2)
K = smul(3, mul(fp, fm))
assert add(nX, P(11)) == smul(4, K)
sg_rules = []
claims = {(2, 1): {4, 6}, (0, 2): {2, 3}, (2, 0): {8, 9}, (1, 2): {5, 7}}
for (be, ga), Xres in claims.items():
    d = mul(fp if be == 0 else (fp if be == 1 else mul(fp, fp)), [F(1)]) if be else P(1)
    d = P(1)
    for _ in range(be):
        d = mul(d, fp)
    for _ in range(ga):
        d = mul(d, fm)
    assert divmod_(mul(K, K), d)[1] == []
    Kd = add(K, d)
    y = smul(F(1, 11), mul(nX, Kd))
    z = smul(F(1, 11), mul(nX, exdiv(mul(K, Kd), d)))
    r = Rule(f'SG(beta,gamma)=({be},{ga})', 1, 4, 4, nX, (K, y, z), nfun=n3)
    # X = 2^{(s-4)/4}; X mod 11 in Xres  <=>  (s-4)/4 mod 10 in {k: 2^k mod 11 in Xres}
    ks = {k for k in range(10) if pow(2, k, 11) in Xres}
    sres = {(4 + 4 * k) % 40 for k in ks}
    report(r, 40, sres)
    sg_rules.append((r, 40, sres))
# step 2: classes polynomial in n, Y = 2^s, n = 3Y+1
nY = P(1, 3)
step2 = []
def cls(name, xs, mod, res):
    r = Rule(name, 1, 0, 1, nY, xs, nfun=n3)
    report(r, mod, res)
    step2.append((r, mod, res))
cls('7|n', (smul(F(2, 7), nY), smul(F(15, 7), nY), smul(30, nY)), 3, {1})
cls('n=6(7)', (smul(F(2, 7), add(nY, P(1))), smul(2, nY), smul(F(2, 7), mul(nY, add(nY, P(1))))), 3, {2})
cls('n=7(15)', (smul(F(1, 15), add(smul(4, nY), P(2))), smul(4, nY), smul(F(4, 15), mul(nY, add(smul(2, nY), P(1))))), 4, {1})
cls('n=13(15)', (smul(F(1, 15), add(smul(4, nY), P(8))), smul(4, nY), smul(F(2, 15), mul(nY, add(nY, P(2))))), 4, {2})
cls('5|n', (smul(F(2, 5), nY), smul(F(4, 5), nY), smul(4, nY)), 4, {3})
cls('61|n', (smul(F(16, 61), nY), smul(F(326, 61), nY), smul(2608, nY)), 60, {24})
allr = sg_rules + step2
L = 120
unc = [s for s in range(L) if not any(s % m in res for _, m, res in allr)]
print('  uncovered mod 120:', unc)
OK &= unc == []
for s in range(1, SMAX + 1):
    if not any(s % m in res and r.applies(s) for r, m, res in allr):
        print('  s =', s, 'NOT solved'); OK = False
print('  s=0:', F(1, 2) + F(1, 3) + F(1, 6) == 1)

# ---------------- Remark 4.2(ii) cubic Type II ----------------
print('== Remark 4.2(ii): a=80, c=1, d=(21Y+64)/320, b=(Y^2-3Y+9)/7, Y=2^{s/3}')
nC = P(1, 0, 0, 3)
a, c = F(80), F(1)
d = smul(F(1, 320), P(64, 21))
b = smul(F(1, 7), P(9, -3, 1))
x = smul(a, mul(b, d)); y = smul(a * c, mul(d, nC)); z = smul(c, mul(mul(b, d), nC))
r = Rule('cubicII', 1, 0, 3, nC, (x, y, z), params=(b, d), nfun=n3)
report(r, 36, {0, 12})
print('  s=12 applies?', r.applies(12), '; s=36?', r.applies(36))

# ---------------- Lemma 4.3: 63*2^s+1 ----------------
print('== Lemma 4.3: 63*2^s+1, s = 0 mod 24')
n63 = lambda s: 63 * 2 ** s + 1
nY = P(1, 0, 0, 63)
a, d = F(5), F(17)
b = smul(F(1, 340), P(28, -9, 3, 63)); c = smul(F(1, 340), P(64, 21))
x = smul(a * d, b); y = smul(a * d, mul(c, nY)); z = smul(d, mul(mul(b, c), nY))
assert sub(smul(4 * a * d, b), nY) == smul(3, P(9, -3, 1))
r = Rule('63class', 1, 0, 3, nY, (x, y, z), params=(b, c), nfun=n63)
report(r, 24, {0})
print('  s=0 applies?', r.applies(0), ' s=24?', r.applies(24))
for s in range(24, 2000, 24):
    if not r.applies(s):
        print('  FAIL at', s); OK = False

# ---------------- Lemma 4.8: 4^s+105 ----------------
print('== Lemma 4.8: 4^s+105, s = 34 mod 45, u = 4^{(s-4)/3}')
n105 = lambda s: 4 ** s + 105
nU = P(105, 0, 0, 256)
x = smul(64, P(1, 0, 0, 1))
A_ = smul(F(1, 151), P(66, -2, 2, 64))
y = mul(nU, A_); z = smul(32, mul(mul(nU, P(1, 1)), A_))
r = Rule('105class', 2, 8, 3, nU, (x, y, z), nfun=lambda s: n105(s))
report(r, 45, {34})
for s in range(34, 3000, 45):
    if not r.applies(s):
        print('  FAIL at', s); OK = False
print('ALL OK' if OK else 'PROBLEMS')
