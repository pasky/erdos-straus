"""z52d pass2 fix, TO0b.
Z0091: Gaussian cone solutions of 4/p = 1/a+1/b+1/c (a,b,c in Z[i], each with Re,Im both >=0 or both <=0 -- Bradford-Ionascu
Conj 1.1 cone, read as a per-element condition), searched with |Re|,|Im| <= R for p = 5, 13, 17, 29, 37, 41.
Pair completion: given a,b, c = p a b / (4ab - p(a+b)) (exact Gaussian division). Test: do the real parts (or norms) give an
integer ES solution, i.e. 4/p = sum of 1/Re(.) or of 1/N(.) over the three entries (all nonzero)?
Z0178: Ford/Farey pure form: for p prime, b in [1,p), N = b^{-1} mod p in (0,p), e = (Nb-1)/p, criterion: 4 | N and e | aN+1 for some
a | N/4.  Verifies the claim that the pure Ford-circle-of-denominator-p form misses exactly 5, 17, 41, 241 (p <= 3000)."""
import math
from fractions import Fraction as Fr
def gmul(x, y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def gconj(x): return (x[0], -x[1])
def gnorm(x): return x[0]*x[0]+x[1]*x[1]
def gdiv_int(num, den):
    """num/den in Z[i] if exact, else None"""
    n = gnorm(den)
    if n == 0: return None
    c = gmul(num, gconj(den))
    if c[0] % n or c[1] % n: return None
    return (c[0] // n, c[1] // n)
def cone_ok(x):
    return (x[0] >= 0 and x[1] >= 0) or (x[0] <= 0 and x[1] <= 0)
def cone_triple_ok(A, B, C):
    """collective reading: all six parts >=0, or all six <=0 (per-element reading admits integer solutions with mixed signs)"""
    v = [A[0], A[1], B[0], B[1], C[0], C[1]]
    return all(x >= 0 for x in v) or all(x <= 0 for x in v)
out = []
R = 14
box = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1) if (a, b) != (0, 0)]
for p in (5, 13, 17, 29, 37, 41):
    sols = []
    for A in box:
        pass
        for B in box:
            if B < A: continue
            # D = 4AB - p(A+B); c = pAB / D
            AB = gmul(A, B)
            D = (4*AB[0] - p*(A[0]+B[0]), 4*AB[1] - p*(A[1]+B[1]))
            if D == (0, 0): continue
            C = gdiv_int((p*AB[0], p*AB[1]), D)
            if C is None or C == (0, 0) or not cone_triple_ok(A, B, C): continue
            if max(abs(C[0]), abs(C[1])) > 4*R*p: continue
            sols.append((A, B, C))
    # real-part and norm tests
    re_hits = 0; norm_hits = 0; ex = None
    for (A, B, C) in sols:
        parts = [x[0] for x in (A, B, C)]
        norms = [gnorm(x) for x in (A, B, C)]
        if all(v != 0 for v in parts) and Fr(1, parts[0]) + Fr(1, parts[1]) + Fr(1, parts[2]) == Fr(4, p):
            re_hits += 1; ex = ex or (A, B, C)
        if all(v != 0 for v in norms) and Fr(1, norms[0]) + Fr(1, norms[1]) + Fr(1, norms[2]) == Fr(4, p):
            norm_hits += 1
    out.append(f'Z0091 p={p}: cone solutions (collective cone) (entries |Re|,|Im|<={R}, unordered pairs A<=B) = {len(sols)}; real-part ES hits = {re_hits}; norm ES hits = {norm_hits}; example real-part hit {ex}')
# Z0178
def isprime(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
bad = []; hits_pure = []
for p in [q for q in range(5, 3001) if isprime(q)]:
    ok = False; wit = None
    for b in range(1, p):
        N = pow(b, -1, p)     # N in (0,p), N b = 1 mod p
        e = (N * b - 1) // p
        if N % 4: continue
        if e == 0: continue
        for a in range(1, N // 4 + 1):
            if (N // 4) % a == 0 and (a * N + 1) % e == 0:
                ok = True; wit = (b, N, e, a); break
        if ok: break
    if ok: hits_pure.append((p, wit))
missing = [p for p in [q for q in range(5, 3001) if isprime(q)] if p not in [h[0] for h in hits_pure]]
w = {h[0]: h[1] for h in hits_pure}
out.append(f'Z0178: pure Ford-form (N<p, b<p) holds for all primes 5..3000 except {missing} (repo claim: 5,17,41,241 up to 8000); witnesses (b,N,e,a): p=41 {w.get(41)}, p=241 {w.get(241)}')
print('\n'.join(out))
open('data/z52b/pass2/TO0b/fix_Z0091_Z0178.txt', 'w').write('\n'.join(out) + '\n')
