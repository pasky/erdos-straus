"""R162 from-scratch check of INVOLUTION_ES2 Prop 7.1: the Brun–Titchmarsh mass
mu = sum_{a odd >= 3} phi(gcd(24,a^2-1))/phi(a^2-1) over a compatible with p = 1 (24), p = -a (a^2-1),
with an independent certified tail. Also: (i) which a are compatible (recomputed by CRT, not assumed),
(ii) the inequality phi(n) >= c n^0.9 used by the author, (iii) the empirical covered fraction.
Usage: uv run --with sympy python scripts/review_inv2_mass.py AMAX PMAX
"""
import sys
from math import gcd
from fractions import Fraction
from sympy import totient, primerange, factorint

def compatible(a):
    m = a * a - 1
    g = gcd(24, m)
    return (-a - 1) % g == 0  # p = 1 mod 24 and p = -a mod m solvable

def phi_from_sieve(N):
    phi = list(range(N + 1))
    for i in range(2, N + 1):
        if phi[i] == i:
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
    return phi

def main(AMAX, PMAX):
    # (i) compatible residues mod 24 (and check that the class only depends on a mod 24)
    cls = sorted({a % 24 for a in range(3, 2000, 2) if compatible(a)})
    print("compatible a mod 24:", cls)
    assert all(compatible(a) == (a % 24 in cls) for a in range(3, 20000, 2))
    # (ii) min of phi(n)/n^0.9
    phis = phi_from_sieve(10**6)
    worst = min(range(1, 10**6), key=lambda n: phis[n] / n**0.9)
    print(f"min phi(n)/n^0.9 for n<1e6: n={worst}, value={phis[worst]/worst**0.9:.6f}")
    viol = [n for n in range(1, 10**6) if phis[n] < 0.375 * n**0.9]
    print("n < 1e6 violating phi(n) >= 0.375 n^0.9:", viol[:10])
    # exact partial sum with rational arithmetic -> rounded up at the end; phi(a^2-1)=phi(a-1)phi(a+1)/phi(gcd)... use factorint
    S = 0
    fl = 0.0
    for a in range(3, AMAX + 1, 2):
        if a % 24 not in cls:
            continue
        m = a * a - 1
        num, den = int(totient(gcd(24, m))), int(totient(m))
        fl += num / den
        S += -((-num * 10**30) // den)  # rounded up at 1e-30
    # tail: a > AMAX in 2 classes mod 24: phi(gcd)<=8, phi(m) >= c0 m^0.9 with c0 = 0.3746 (true min, below)
    c0 = 0.3746
    # sum_{a>AMAX, two classes mod 24} 8/(c0 (a^2-1)^0.9) <= (2/24)*... bound by integral with one extra term
    # each class: sum_{k>=0} f(a0+24k) <= f(a0) + (1/24) int_{a0}^inf f, with f decreasing, f(a)=8/(c0 (a^2-1)^0.9)
    tail = 0.0
    for r in cls:
        a0 = AMAX + ((r - AMAX) % 24) or AMAX + 24
        if a0 <= AMAX:
            a0 += 24
        f = lambda a: 8 / (c0 * (a * a - 1) ** 0.9)
        # int_{a0}^inf 8/(c0 (a^2-1)^0.9) da <= int 8/(c0 (a^2/1.0001)^0.9) = 8*1.0001^0.9/(c0*0.8) a0^-0.8
        tail += f(a0) + (1 / 24) * 8 * 1.0001**0.9 / (c0 * 0.8) * a0 ** (-0.8)
    print(f"partial sum a<={AMAX}: {S/1e30:.10f} (float acc {fl:.10f}); tail bound {tail:.3e}; mu <= {S/1e30+tail:.7f}; 1-2mu >= {1-2*(S/1e30+tail):.5f}")
    # (iii) empirical: primes p=1 (24), p<PMAX, with some odd a, a^2-1 | p+a
    tot = cov = 0
    for p in primerange(2, PMAX):
        if p % 24 != 1:
            continue
        tot += 1
        a = 3
        while a * a - 1 <= p + a:
            if (p + a) % (a * a - 1) == 0:
                cov += 1; break
            a += 2
    print(f"empirical: {cov}/{tot} primes p=1 (24) < {PMAX} covered by {{t=u}} ({cov/tot:.4f})")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
