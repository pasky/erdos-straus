# Z2744: Rademacher Phi on the word matrices.  gamma_w = [[p,-A*],[A,-t]] (det 1; from HJ product of [[v,-1],[1,0]]...).
# We use gamma = [[t,-A*],[A,-p]] (= -gamma_w^{-1}, c = A > 0, d = -p), with Rademacher's Phi(gamma) = (a+d)/c - 12 s(d,c).
# Question: does Phi (mod 2, mod 24/...) determine the ES sign (A/p)?  Tested exhaustively for words of primes p = 1 mod 8, p <= P.
import sys
from fractions import Fraction
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def ded(h, k):
    # Dedekind sum s(h,k), k>0, gcd(h,k)=1
    def saw(x):  # ((x)) sawtooth
        if x.denominator == 1: return Fraction(0)
        return x - (x.numerator // x.denominator) - Fraction(1, 2)
    return sum(saw(Fraction(i, k)) * saw(Fraction(h*i % k, k)) for i in range(1, k))
P = int(sys.argv[1]) if len(sys.argv) > 1 else 300
rows = []
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u - 1; As = t*v - 1
        if A < 2: continue
        Phi = Fraction(t - p, A) - 12*ded(-p % A, A)
        sign = L.legendre(A, p)
        rows.append((p, (t, u, v), A, Phi, sign))
# Phi mod 2 (as rational mod 2)
def modp(x, m): return x - m*(x//m)
from collections import Counter
c = Counter()
for (p, w, A, Phi, s) in rows:
    c[(s, modp(Phi, 2))] += 1
print("words:", len(rows))
print("counts (sign, Phi mod 2):", sorted(c.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))))
c24 = Counter((s, modp(12*Phi, 24)) for (p, w, A, Phi, s) in rows)
print("distinct (sign, 12Phi mod 24) classes:", len(c24), sorted(c24.items(), key=lambda kv: (kv[0][0], str(kv[0][1])))[:12])
# Jacobi-symbol test: (d/c) = (-p / A) (Jacobi), for odd A; compare with Phi mod 2 and with the Legendre sign
from sympy import jacobi_symbol
def jac(a, n):
    return jacobi_symbol(a % n, n) if n > 1 else 1
cj = Counter()
for (p, w, A, Phi, s) in rows:
    if A % 2 == 1:
        cj[(jac(-p, A), modp(Phi, 2), s)] += 1
print("odd A: counts (Jacobi (-p/A), Phi mod 2, Legendre (A/p)):", sorted(cj.items(), key=lambda kv: str(kv[0])))
ce = Counter()
for (p, w, A, Phi, s) in rows:
    if A % 2 == 0: ce[(modp(Phi, 2), s)] += 1
print("even A: counts (Phi mod 2, sign):", sorted(ce.items(), key=lambda kv: str(kv[0])))
cp = Counter()
for (p, w, A, Phi, s) in rows:
    if A % 2 == 1: cp[(jac(p, A) == s, modp(Phi, 2) == 0)] += 1
print("reciprocity check (Jacobi (p/A) == Legendre (A/p)) x (Phi even):", sorted(cp.items(), key=lambda kv: str(kv[0])))
# Does Phi mod 2 together with the Jacobi symbol (-p/A) determine the sign? (independence check)
