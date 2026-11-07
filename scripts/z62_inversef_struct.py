# For each zero prime p and r=1..RMAX: factor p+r, flag prime factors q (q coprime to 2r) with kronecker(-r,q) = -1 ("inert")
# Also count, for comparison, random primes = 1 (4) of similar size.
import sys, random
from sympy import factorint, isprime
from sympy.ntheory import jacobi_symbol
def kron(a,q):
    # q odd prime
    return jacobi_symbol(a%q,q)
ZEROS=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
RMAX=int(sys.argv[1]) if len(sys.argv)>1 else 24
def profile(p,RMAX):
    out=[]
    for r in range(1,RMAX+1):
        f=factorint(p+r)
        bad=[q for q in f if q%2==1 and r%q!=0 and kron(-r,q)==-1]
        out.append((r,f,bad))
    return out
def nbad(p,RMAX):
    return sum(1 for r,f,bad in profile(p,RMAX) if bad)
if __name__=="__main__":
    for p in ZEROS:
        pr=profile(p,RMAX)
        print(f"p={p}: r with inert prime factor in p+r:", [(r,bad) for r,f,bad in pr if bad])
    random.seed(1)
    for p in ZEROS:
        # random primes near p, =1 mod 4
        cnt=[]
        for _ in range(20):
            q=random.randrange(p//2,2*p)|1
            while not (isprime(q) and q%4==1): q+=2
            cnt.append(nbad(q,RMAX))
        print(f"near p={p}: zero prime nbad={nbad(p,RMAX)}  random primes nbad={sorted(cnt)}")
