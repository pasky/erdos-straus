"""R167 from-scratch test of Thm 9.1 / Cor 9.3 (STRONG_APPROX_ES §9).
Characters mod L = 35 = 5*7 built from primitive roots (2 mod 5, 3 mod 7); also imprimitive/trivial ones.
E(n) = sum_i c_i sigma_{k_i}(n; chi_i, psi_i), sigma_k(n;chi,psi) = sum_{d|n} chi(d) psi(n/d) d^k.
Checks: (1) E(l^2) = P(l) := sum_k C_k (1 + l^k + l^{2k}) and E(p) = sum_k C_k(1+p^k) for primes l,p = 1 (L);
(2) a combination with all C_k = 0 vanishes at every p = 1 (L) yet is nonzero at other primes (scope);
(3) random real combinations: sign of E at prime squares l^2 = 1 (L) for large l predicts sign of E(p);
(4) counting version: with theta, B, the top-monomial argument (coefficients recovered by exact fit).
"""
import cmath, random
from sympy import primerange, divisors
L = 35
def char_table():
    # discrete logs mod 5 (gen 2) and mod 7 (gen 3)
    lg5 = {pow(2, i, 5): i for i in range(4)}
    lg7 = {pow(3, i, 7): i for i in range(6)}
    chars = []
    for a in range(4):
        for b in range(6):
            def chi(n, a=a, b=b):
                if n % 5 == 0 or n % 7 == 0:
                    return 0
                return cmath.exp(2j * cmath.pi * (a * lg5[n % 5] / 4 + b * lg7[n % 7] / 6))
            chars.append(((a, b), chi))
    return chars
CH = char_table()
def sig(n, k, chi, psi):
    return sum(chi(d) * psi(n // d) * d**k for d in divisors(n))
def E(n, combo):
    return sum(c * sig(n, k, CH[i][1], CH[j][1]) for (c, k, i, j) in combo)
def Ck(combo):
    C = {}
    for (c, k, i, j) in combo:
        C[k] = C.get(k, 0) + c
    return C
primes1 = [p for p in primerange(3, 20000) if p % L == 1]
others = [p for p in primerange(3, 3000) if p % L != 1 and p % 5 and p % 7]
random.seed(167)
# (1)
worst = 0
for trial in range(20):
    combo = [(complex(random.gauss(0, 1), random.gauss(0, 1)), random.randint(0, 3),
              random.randrange(24), random.randrange(24)) for _ in range(6)]
    C = Ck(combo)
    for l in primes1[:6]:
        P = sum(c * (1 + l**k + l**(2 * k)) for k, c in C.items())
        worst = max(worst, abs(E(l * l, combo) - P) / max(1, abs(P)))
        Ep = sum(c * (1 + l**k) for k, c in C.items())
        worst = max(worst, abs(E(l, combo) - Ep) / max(1, abs(Ep)))
print(f"(1) max relative deviation from P(l), sum C_k(1+p^k): {worst:.2e}")
# (2) C_k = 0 but nontrivial combination
combo = [(1, 1, 5, 0), (-1, 1, 0, 0), (2, 0, 3, 7), (-2, 0, 0, 0)]
assert all(abs(c) < 1e-12 for c in Ck(combo).values())
z1 = max(abs(E(p, combo)) for p in primes1[:10]); zs = max(abs(E(l * l, combo)) for l in primes1[:10])
nz = sum(abs(E(p, combo)) > 1e-6 for p in others[:50])
print(f"(2) all C_k=0: max|E(p)| p=1(L): {z1:.1e}, max|E(l^2)|: {zs:.1e}; nonzero at {nz}/50 other primes")
# (3) real combinations (chi, psi real-valued pairs: use conjugate-symmetrised combos)
agree = tot = 0
for trial in range(200):
    combo = []
    for _ in range(5):
        c = random.gauss(0, 1); k = random.randint(0, 2); i = random.randrange(24); j = random.randrange(24)
        ic = [t for t, ((a, b), _) in enumerate(CH) if (a, b) == ((-CH[i][0][0]) % 4, (-CH[i][0][1]) % 6)][0]
        jc = [t for t, ((a, b), _) in enumerate(CH) if (a, b) == ((-CH[j][0][0]) % 4, (-CH[j][0][1]) % 6)][0]
        combo += [(c / 2, k, i, j), (c / 2, k, ic, jc)]       # real-valued E
    l = primes1[-1]; p = primes1[-2]
    s_sq = E(l * l, combo).real; s_p = E(p, combo).real
    if abs(s_sq) > 1e-6 and abs(s_p) > 1e-6:
        tot += 1; agree += (s_sq > 0) == (s_p > 0)
print(f"(3) sign(E(l^2)) == sign(E(p)) for large l,p = 1 (L): {agree}/{tot}")
# (4) counting version, theta = 1 (rank-4 shape: main term k=1, error n^{1/2+eps} absorbed): if E(l^2) <= B l^{2 theta}
# along l = 1 (L), then E(p) < 2 B p^theta for large p. Test on combos with C_1 in [0, B]:
B = 1.0; viol = 0
for trial in range(200):
    C1 = random.uniform(-2, 2); C0 = random.gauss(0, 5)
    combo = [(C1, 1, 0, 0), (C0, 0, 0, 0), (random.gauss(0, 1), 1, 5, 5), (-0.0, 1, 0, 0)]
    combo[3] = (-combo[2][0], 1, 0, 0)             # keep C_1 = C1
    hyp = all(E(l * l, combo).real <= B * l**2 * 1.001 + 50 for l in primes1[-5:])
    concl = all(E(p, combo).real < 2 * B * p for p in primes1[-5:])
    viol += hyp and not concl
print(f"(4) counting-version violations: {viol}/200")
