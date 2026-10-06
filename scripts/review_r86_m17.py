"""R86 from-scratch spot check of Comp. 6.3 levels 1-2: brute force over ET classes (read off the
7-family definitions) of modulus <= MMAX with 17-adic valuation 1 or 2, collecting the boxes
u mod 17^k (k = v17(modulus)) in the cell C5 = {u = 5 mod 17} on the 17-generic line, and also
checking that no class with 17 not dividing the modulus contains the line (no level-0 box)."""
import sys
from math import gcd
from sympy import divisors
sys.path.insert(0, 'scripts')
from review_r86_families import in_class, admissible
MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000

def v17(m):
    v = 0
    while m % 17 == 0: m //= 17; v += 1
    return v

def modulus(fam, k):
    p, q, r = k
    return {'I1': 4*p*q, 'I2': 4*p*q*r, 'I3': 4*p*q*r, 'I4': 4*p*q, 'II1': 4*p*q, 'II2': r, 'II3': 4*p*q*r}[fam]

def crt(u, K, N):  # n = 1 mod N, n = u mod K
    return (1 + N * ((u - 1) * pow(N, -1, K) % K)) % (K*N) if K > 1 else 1

boxes = {1: set(), 2: set()}; level0 = []
def test(fam, k):
    M = modulus(fam, k); v = v17(M)
    if v > 2: return
    K = 17**v; N = M // K
    if v == 0:
        if in_class(fam, k, 1 + M): level0.append((fam, k))   # n=1+M avoids n=1 edge: same class
        return
    for u in range(5, K, 17):
        if in_class(fam, k, crt(u, K, N) + K*N): boxes[v].add(u)

def triples(bound):  # positive (p,q,r) with p*q*r <= bound
    for p in range(1, bound+1):
        for q in range(1, bound//p + 1):
            for r in range(1, bound//(p*q) + 1):
                yield p, q, r
B = MMAX // 4
for p in range(1, B+1):                      # I1: (a,d,f), f | 4a^2d+1, modulus 4ad
    for q in range(1, B//p + 1):
        if (p*q) % 17: continue
        for f in divisors(4*p*p*q + 1): test('I1', (p, q, f))
for p in range(1, B+1):                      # I4, II1: (a,b,e), e | a+b, modulus 4ab
    for q in range(1, B//p + 1):
        if (p*q) % 17: continue
        for e in divisors(p+q):
            if gcd(e, 4*p*q) == 1: test('I4', (p, q, e)); test('II1', (p, q, e))
for t in triples(B):                         # I2, I3, II3: modulus 4*p*q*r
    if (t[0]*t[1]*t[2]) % 17: continue
    for fam in ('I2', 'I3', 'II3'):
        if admissible(fam, t): test(fam, t)
for p in range(1, MMAX+1):                   # II2: (a,d,f), 4ad | f+1, modulus f
    for q in range(1, (MMAX+1)//(4*p) + 1):
        for f in range(4*p*q - 1, MMAX+1, 4*p*q):
            if f % 17 == 0: test('II2', (p, q, f))
# level-0 sanity on the small range (17 not dividing modulus)
for t in triples(2000):
    for fam in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
        if admissible(fam, t) and v17(modulus(fam, t)) == 0: test(fam, t)
b2 = {u for u in boxes[2] if (u % 17) not in {x for x in boxes[1]}}
print("MMAX", MMAX, "level-1 boxes in C5:", sorted(boxes[1]), "level-2 residues in C5:", sorted(boxes[2]))
cov = len(boxes[1]) / 17 + len([u for u in boxes[2] if u % 289 not in boxes[1]]) / 289
print("covered fraction of C5 after level 2:", 17 * cov, "(paper: 0.235294 = 4/17)", "level0 hits:", level0)
