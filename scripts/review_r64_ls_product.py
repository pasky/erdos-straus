"""R64 from-scratch checks for §13.
(1) Lemma 'atoms': {-u v^{-1} mod M : uvw=A_M} == {-4D mod M : D | A_M^2} for M<=T, M=3 mod 4.
(2) Squares of units mod 840 are exactly Mordell's six classes.
(3) Thm 13.1 system E_T: every prime T<p<=X avoiding E_T has W(p)>T (direct W) and is hard;
    and every prime with W(p)>T that is a square mod 840 avoids E_T.
(4) Prop 13.2(a): the product set S (1 mod 8; QR mod odd l<=y; complement of B_l for y<l<=T)
    avoids every atom (M,D), M<=T, checked component-wise; report log(1/delta(S)) vs pi(y)log2.
"""
from math import gcd, log, isqrt
from sympy import divisors, primerange, isprime, factorint

T = 1500
def classes_uvw(M):
    A = (M + 1) // 4; out = set()
    for u in divisors(A):
        for v in divisors(A // u):
            out.add((-u * pow(v, -1, M)) % M)
    return out
def classes_D(M):
    A = (M + 1) // 4
    return {(-4 * D) % M for D in divisors(A * A)}
Ms = [M for M in range(3, T + 1, 4)]
R = {}
for M in Ms:
    a, b = classes_uvw(M), classes_D(M)
    assert a == b, M
    R[M] = b
print("(1) atom-class identity ok for all M<=%d" % T)
sq = sorted({(x * x) % 840 for x in range(840) if gcd(x, 840) == 1})
assert sq == sorted([1, 121, 169, 289, 361, 529]), sq
print("(2) unit squares mod 840:", sq)
def W_gt_T(n):
    return all(n % M not in R[M] for M in Ms)
nonsq = {c for c in range(840) if gcd(c, 840) == 1 and c not in sq}
cnt = 0; cntW = 0
for p in primerange(T + 1, 3 * 10**6):
    avoid = (p % 840 not in nonsq) and W_gt_T(p)
    if W_gt_T(p): cntW += 1
    if W_gt_T(p) and p % 840 in sq: assert avoid
    if avoid:
        cnt += 1; assert p % 840 in sq
print(f"(3) primes in (T,3e6] avoiding E_T: {cnt} (all hard, W>T); primes with W>T: {cntW}")
# (4) product set
y = int(T ** 0.55)
B = {}
for M in Ms:
    f = factorint(M); big = [l for l in f if l > y]
    if not big: continue
    assert len(big) == 1 and f[big[0]] == 1
    l = big[0]; B.setdefault(l, set()).update({c % l for c in R[M]})
def in_S_component(l, e, c):  # c mod l^e
    if l == 2: return c % 8 == 1
    if l <= y: return pow(c % l, (l - 1) // 2, l) == 1
    if l <= T: return (c % l) not in B.get(l, set())
    return True
bad = 0
for M in Ms:
    f = factorint(M)
    for c in R[M]:
        if all(in_S_component(l, e, c % l**e) for l, e in f.items()): bad += 1
assert bad == 0
ld = log(4) + sum(log(2) for l in primerange(3, y + 1)) + sum(-log(1 - len(B.get(l, ())) / (l - 1)) for l in primerange(y + 1, T + 1))
print(f"(4) product set avoids all atoms; y={y}, max|B_l|/l = {max(len(B[l])/l for l in B):.3f}, log(1/delta)={ld:.1f}, pi(y)log2={sum(1 for _ in primerange(3,y+1))*log(2):.1f}")
