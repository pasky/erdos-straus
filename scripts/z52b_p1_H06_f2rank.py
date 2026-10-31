"""Z2406: F2-rank of the squarefree kernels of A = tu-1 over all words w=(t,u,v), tuv-u-v=n, gcd(A,n)=1
(SIGN_IDENTITY convention; chi(w) = (-A/n)). Random-multiplicative model: P(f(A)=f(-1)... all words chi=+1) = 2^-rank
(sign of -1 fixed since n ≡ 1 mod 4). Compare primes with odd squares (where every word has chi=+1, i.e. the event is certain)."""
import sys, math
from sympy import factorint, primerange, jacobi_symbol
def words(n):
    for u in range(1,n+3):
        t=1
        while (t-1)*u<=n+1:
            A=t*u-1
            if A>0 and (n+u)%A==0: yield t,u,(n+u)//A,A
            t+=1
def f2rank(vecs):
    basis={}   # pivot -> int bitmask
    for v in vecs:
        while v:
            h=v.bit_length()-1
            if h in basis: v^=basis[h]
            else: basis[h]=v; break
    return len(basis)
def analyse(n):
    idx={}; vecs=[]; Nm=0; W=0
    for t,u,v,A in words(n):
        if math.gcd(A,n)!=1: continue
        W+=1
        if jacobi_symbol((-A)%n,n)==-1: Nm+=1
        m=0
        for q,e in factorint(A).items():
            if e%2:
                if q not in idx: idx[q]=len(idx)
                m|=1<<idx[q]
        vecs.append(m)
    return W,len(idx),f2rank(vecs),Nm
for n in map(int,sys.argv[1:]):
    W,nprimes,r,Nm=analyse(n)
    print('n=%d words=%d odd-exponent primes=%d F2-rank=%d  model P(fail)=2^-%d  actual N_-=%d'%(n,W,nprimes,r,r,Nm))
