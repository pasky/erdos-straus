"""Check Lemma 2.1: p prime = 1 mod 4, k with (k/p) = -1  =>  p+4k has an odd number (with multiplicity) of prime
factors l with (l/p) = -1, and (l/p) = (-k/l) (Kronecker/Jacobi) for every odd prime l | p+4k, l != p.
(At odd squares n = m^2 the hypothesis (k/n) = -1 never holds for gcd(k, m) = 1; nothing to test there.)"""
from sympy import primerange, factorint, jacobi_symbol, legendre_symbol
viol = 0; tests = 0
for p in primerange(5, 200000):
    if p % 4 != 1: continue
    for k in range(1, 60):
        if k % p == 0: continue
        N = p + 4 * k; f = factorint(N)
        cnt = sum(e for l, e in f.items() if l != p and legendre_symbol(l % p, p) == -1)
        for l in f:
            if l != p and legendre_symbol(l % p, p) != jacobi_symbol(-k % l, l): viol += 1
        if legendre_symbol(k % p, p) == -1:
            tests += 1
            if cnt % 2 != 1: viol += 1
print(f"prime tests {tests}, violations {viol}")
