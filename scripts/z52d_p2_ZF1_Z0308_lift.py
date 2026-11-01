# Z0308: lift the F_2[T] covering identities for A = T^2 (FUNCTIONFIELD_ES Thm 6.1 / data/review_ffl/cover_q2_A100.txt)
# to Z by T -> 2 with all sign choices of the F_2 coefficients, and classify the resulting 4/n identities.
# Leaf family (E; a=(t0,1); b=(t1,1)): X = (P+E)/A, a = 1, b = P, kappa = (a+b)/E, Y = kappa P X / a, Z = kappa P X / b.
# Signed Z-lift: e = signed lift of E at T=2, a = +-1, b = +-n; identity 4/n = 1/X + 1/Y + 1/Z holds whenever
# X = (n+e)/4, kappa = (a+b)/e are integers (universal algebra: 4/n - 1/X = e/(nX) = (a+b)/(kappa n X)).
import itertools, json, math
from fractions import Fraction as F
leaves = [l.split() for l in open('data/review_ffl/cover_q2_A100.txt') if l.startswith('leaf')]
def lifts(polystr):  # coefficient strings high->low over F2; signed lifts at T=2
    co = [int(ch) for ch in polystr]
    vals = set()
    for signs in itertools.product([1, -1], repeat=sum(co)):
        it = iter(signs); v = 0
        for c in co: v = 2 * v + (next(it) if c else 0)
        vals.add(v)
    return sorted(vals)
rows = []
for L in leaves:
    E = L[3].split('=')[1]
    for e in lifts(E):
        for sa, sb in itertools.product([1, -1], repeat=2):
            # find residue classes n mod 4|e|*3 (n odd prime-like, n coprime to 6e) where X, kappa integral
            mod = 4 * abs(e) * 3
            cls_pos, cls_sgn = [], []
            for r in range(1, mod, 2):
                if math.gcd(r, mod) != 1: continue
                n = r + 1000 * mod  # representative
                if (n + e) % 4 or (sa + sb * n) % e: continue
                X = (n + e) // 4; k = (sa + sb * n) // e
                Y = F(k * n * X, sa); Z = F(k * n * X, sb * n)
                assert F(4, n) == F(1, X) + 1 / Y + 1 / Z
                terms = [X, Y, Z]
                (cls_pos if all(t > 0 for t in terms) else cls_sgn).append(r)
            if cls_pos or cls_sgn:
                rows.append(dict(leaf_E=E, e=e, a=sa, b=('+n' if sb > 0 else '-n'), mod=mod,
                                 positive_classes=cls_pos, signed_classes=cls_sgn))
for r in rows: print(r)
# The hard case: n == 1 (mod 12) (all Mordell-hard classes mod 840 are == 1 mod 12).  Lift e=3, a=-1, b=+n:
# 4/n = 1/X + 1/(kX) - 1/(k n X), X = (n+3)/4, k = (n-1)/3; negative term / (4/n) = 3/(4kX) ~ 9/n^2... measured below.
# Positivity repair: 1/(kX) - 1/(knX) = 3/(nX); 3/(nX) = 1/y + 1/z (y,z>0) iff nX has a divisor pair a+b == 0 (mod 3), i.e.
# (n == 1 mod 3) iff X = (n+3)/4 has a prime factor == 2 (mod 3)  -> exactly the Elsholtz-Tao Type II e-slice e = 3.
import numpy as np
N = 10**7
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
# smallest-prime-factor table up to N/4+1 to test "has a prime factor == 2 mod 3"
M = N // 4 + 2
spf = np.zeros(M + 1, np.int64)
for i in range(2, M + 1):
    if spf[i] == 0:
        spf[i::i][spf[i::i] == 0] = i
def has2mod3(x):
    while x > 1:
        p = spf[x]
        if p % 3 == 2: return True
        while x % p == 0: x //= p
    return False
hard = {1, 121, 169, 289, 361, 529}
stat = dict(n1mod12=0, repaired=0, hard=0, hard_repaired=0, max_neg_ratio=0.0)
fails = []
for p in primes:
    p = int(p)
    if p % 12 != 1: continue
    X = (p + 3) // 4; k = (p - 1) // 3
    stat['n1mod12'] += 1
    ok = has2mod3(X)
    stat['repaired'] += ok
    neg = F(1, k * p * X) / F(4, p)
    stat['max_neg_ratio'] = max(stat['max_neg_ratio'], float(neg) * p * p)
    if p % 840 in hard:
        stat['hard'] += 1; stat['hard_repaired'] += ok
    if not ok and len(fails) < 30: fails.append(p)
stat['first_unrepaired'] = fails
print(stat)
json.dump(dict(lifts=rows, n1mod12_e3_repair=stat, N=N), open('data/z52b/pass2/ZF1/Z0308/lifts.json', 'w'), indent=1)
