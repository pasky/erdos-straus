# For zero primes p and C=1..CMAX: factor 4Cp+1; count prime factors q (with mult) that are QNR mod p, i.e. (q/p)=-1.
# Check identity (q/p) = kronecker(-C, q) for q | 4Cp+1.  Compare to random primes = 1 mod 4 (and 1 mod 8).
import sys, random
from sympy import factorint, isprime
from sympy.functions.combinatorial.numbers import jacobi_symbol, legendre_symbol
ZEROS=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
CMAX=int(sys.argv[1]) if len(sys.argv)>1 else 40
def kron(a,q):
    # Kronecker symbol (a/q) for odd prime q
    return jacobi_symbol(a%q,q)
def stats(p,CMAX):
    tot=0; qnr=0; allqr=0
    for C in range(1,CMAX+1):
        N=4*C*p+1
        f=factorint(N)
        nq=0
        for q,e in f.items():
            s=legendre_symbol(p%q,q) if q!=p else 0
            assert s==kron(-C,q),(p,C,q)
            tot+=e
            if s==-1: nq+=e
        qnr+=nq
        if nq==0: allqr+=1
    return tot,qnr,allqr
if __name__=="__main__":
    random.seed(2)
    for p in ZEROS:
        t,q,a=stats(p,CMAX)
        rs=[]
        for _ in range(12):
            x=random.randrange(p//2,2*p)|1
            while not (isprime(x) and x%8==1): x+=2
            rs.append(stats(x,CMAX))
        print(f"p={p}: Omega={t} QNR={q} allQR_C={a}/{CMAX} | random 1mod8: QNR={sorted(r[1] for r in rs)} allQR={sorted(r[2] for r in rs)}")
