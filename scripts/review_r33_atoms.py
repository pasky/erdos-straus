"""R33 from-scratch checks: Lemma 2.1 (atoms), Lemma 2.2 (class of one),
and the key steps of Lemma 2.3 (g preserved by D -> A^2/D; g | gcd(4sr^2+1, r+k);
inner-sum bound sum_{k} g/k <= (3+log X) tau(4sr^2+1))."""
import math
from sympy import divisors, gcd

def R(M):
    A = (M + 1) // 4
    return {(-4 * D) % M for D in divisors(A * A)}

def mult(M):
    A = (M + 1) // 4
    out = set()
    for u in divisors(A):
        for v in divisors(A // u):
            out.add((-u * pow(v, -1, M)) % M)
    return out

bad = 0
for M in range(3, 3000, 4):
    r = R(M)
    if r != mult(M):
        bad += 1; print("atoms mismatch", M)
    if 1 % M in r:
        bad += 1; print("class of one fails", M)
    A = (M + 1) // 4
    for D in divisors(A * A):
        g = math.gcd(M, 4 * D + 1)
        if math.gcd(M, 4 * (A * A // D) + 1) != g:
            bad += 1; print("g not preserved", M, D)
print("lemma 2.1/2.2/g-symmetry bad:", bad)

# inner sum bound: for s,r, sum over k in [r,X] of g/k with M=4srk-1, D=sr^2
X = 2000
worst = 0
for s in range(1, 40):
    for r in range(1, 40):
        if s * r * r > X:
            continue
        tot = 0.0
        for k in range(r, X // (s * r) + 1):
            M = 4 * s * r * k - 1
            g = math.gcd(M, 4 * s * r * r + 1)
            assert (r + k) % g == 0 and (4 * s * r * r + 1) % g == 0
            tot += g / k
        bound = (3 + math.log(X)) * len(divisors(4 * s * r * r + 1))
        worst = max(worst, tot / bound)
print("max ratio inner-sum / bound:", worst)
