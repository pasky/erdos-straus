# y8: number of clean levels t <= 10 at the worst sign-dominance primes vs random p = 1 (8) and lnr >= 11 (input data/y8/y8_sample600.txt; run from repo root)
from sympy import factorint, legendre_symbol as L
def ncl(p,T=10): return sum(all(L(l%p,p)==1 for l in factorint(t*p+1)) for t in range(1,T+1))
worst=[2521,9601,297049,3361,1249,70249,225289,13249,925369,361321,3049,29401,871249]
print("worst:",[(p,ncl(p)) for p in worst])
import statistics
s=[int(l.split()[0]) for l in open('data/y8/y8_sample600.txt')]
s8=[p for p in s if p%8==1]
from sympy import legendre_symbol
big=[p for p in s8 if all(legendre_symbol(q,p)==1 for q in (3,5,7))]
print("random p=1 mod 8 mean clean among t<=10: %.2f (n=%d)"%(statistics.mean(ncl(p) for p in s8),len(s8)))
print("random p=1 mod 840-squares (lnr>=11) mean: %.2f (n=%d)"%(statistics.mean(ncl(p) for p in big),len(big)))
