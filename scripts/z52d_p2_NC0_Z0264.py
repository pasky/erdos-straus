"""Z0264: N[T]-identities 4/P(T) = 1/X1+1/X2+1/X3 with P, X_i in N[T] of degree <= 2 (coeffs <= M).
Evaluation at T=1 gives ES for n=P(1). Search: for each P (deg<=2, nonneg coeffs, P(1)=n) and each X1<=X2,
X3 = P X1 X2 / (4 X1 X2 - P (X1+X2)) must be an exact polynomial with nonneg coefficients.
Usage: python3 z52d_p2_NC0_Z0264.py [M] [nlist]"""
import sys, itertools
from fractions import Fraction as F
M = int(sys.argv[1]) if len(sys.argv) > 1 else 6
NS = [int(a) for a in sys.argv[2].split(',')] if len(sys.argv) > 2 else [5, 13, 17]

def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    return trim(r)
def add(a, b):
    n = max(len(a), len(b)); return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
def sc(c, a): return trim([c*x for x in a])
def sub(a, b): return add(a, sc(-1, b))
def pdiv(a, b):
    """exact division a/b in Q[T]; returns quotient (list of Fractions) or None."""
    a = [F(x) for x in a]; b = [F(x) for x in b]
    if not b: return None
    q = [F(0)] * max(len(a) - len(b) + 1, 0)
    while len(a) >= len(b) and any(a):
        while a and a[-1] == 0: a.pop()
        if len(a) < len(b): break
        c = a[-1] / b[-1]; d = len(a) - len(b); q[d] = c
        for j in range(len(b)): a[d+j] -= c*b[j]
        while a and a[-1] == 0: a.pop()
    if any(a): return None
    return q

def divides_int(b, a):
    """integer pseudo-remainder test: does b divide a in Q[T] (b, a integer lists)?"""
    a = list(a); db = len(b) - 1; lb = b[-1]
    while len(a) - 1 >= db and any(a):
        la = a[-1]; k = len(a) - 1 - db
        a = [x * lb for x in a]
        for j in range(db + 1): a[k + j] -= la * b[j]
        while a and a[-1] == 0: a.pop()
    return not any(a)

polys = [list(c) for c in itertools.product(range(M+1), repeat=3)]
polys = [trim(p) for p in polys if any(p)]
results = {}
for n in NS:
    Ps = [[a, b, c] for a in range(n+1) for b in range(n+1-a) for c in [n-a-b]]
    Ps = [trim(p) for p in Ps]
    found = []
    for P in Ps:
        if len(P) < 3 and False: pass
        for i, X1 in enumerate(polys):
            for X2 in polys[i:]:
                den = sub(sc(4, mul(X1, X2)), mul(P, add(X1, X2)))
                if not den: continue
                num = mul(P, mul(X1, X2))
                if len(num) < len(den) or not divides_int(den, num): continue
                q = pdiv(num, den)
                if q is None: continue
                if any(c < 0 or F(c).denominator != 1 for c in q): continue
                X3 = trim([int(c) for c in q])
                if not X3: continue
                # verify identity
                assert sub(sc(4, mul(X1, mul(X2, X3))), mul(P, add(add(mul(X2, X3), mul(X1, X3)), mul(X1, X2)))) == []
                found.append((P, X1, X2, X3))
    results[n] = found
    distinct_P = sorted({tuple(f[0]) for f in found})
    print(f"n={n}: #P={len(Ps)} #identities(X1<=X2 ordered)={len(found)} P with identity={len(distinct_P)}", flush=True)
    for P in distinct_P[:8]:
        ex = [f for f in found if tuple(f[0]) == P][0]
        print("  P(T) coeffs(low->high)", list(P), "P(2)=", sum(c*2**k for k, c in enumerate(P)),
              " e.g. X1,X2,X3=", ex[1], ex[2], ex[3], flush=True)

# ---- residue analysis: which classes mod 840 are hit by P(t), t in Z (periodic mod 840)
M6 = {1, 121, 169, 289, 361, 529}  # Mordell's uncovered classes mod 840 (for primes/all n)
allP = sorted({tuple(f[0]) for n in NS for f in results[n]})
cov = set()
for P in allP:
    S = {sum(c * t**k for k, c in enumerate(P)) % 840 for t in range(840)}
    hit = S & M6
    cov |= S
    print(f"P={list(P)} residues mod 840 hit={len(S)} hits Mordell-6: {sorted(hit)}")
print("union of residues mod 840 hit by all found P:", len(cov), "; Mordell-6 hit:", sorted(cov & M6))
