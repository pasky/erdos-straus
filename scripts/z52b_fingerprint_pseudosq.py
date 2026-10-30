"""Least primes p≡1 (mod 4) with prescribed least quadratic non-residue q (all primes < q are QR mod p)."""
from sympy import primerange, legendre_symbol, isprime, nextprime
qs=list(primerange(2,48)); best={}
p=5
while len(best)<len(qs) and p<3*10**9:
    if p%4==1:
        for q in qs:
            if legendre_symbol(q,p)==-1:
                if q not in best: best[q]=p; print(q,p,flush=True)
                break
    p=nextprime(p)
