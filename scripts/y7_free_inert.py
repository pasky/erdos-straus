# y7 (O215): "free" slices of M/p (e in {1,2}: slice condition vacuous) vs the inert classes of Q(sqrt(-M)).
# Type II e-slice needs M | p+e, Type I needs M | pe+1.  e=1: a=b=1,c=2? (a+b=ce: 2=2*1 ok) ; e=2: a=b=1,c=1.
# For odd p: e=2 Type II needs p+2 = M*abd -> fine for any parity of M (N=(p+2)/M); e=2 Type I: 2p+1=M*abd.
# Parity: for M even, p+1, p+2, 2p+1 parity constraints are automatic in the class computation (odd p).
from math import gcd
def kron(a,n):
    # Kronecker symbol (a/n), n>0
    if n==1: return 1
    r=1
    while n%2==0:
        n//=2
        if a%2==0: return 0
        if a%8 in (3,5): r=-r
    a%=n; 
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def classes(M):
    # residue classes of odd primes p mod L=lcm(M,2) coprime to M, as residues mod M (odd p)
    U=[r for r in range(M) if gcd(r,M)==1]
    # need odd p in class: if M even, r must be odd automatically (gcd(r,M)=1)
    free=set()
    for r in U:
        if (r+1)%M==0 or (r+2)%M==0 or (2*r+1)%M==0: free.add(r)
    return U,free
def odd_quadratic_chars(M):
    # exact: odd quadratic characters mod M are Kronecker chi_D with D<0 a fundamental discriminant, |D| | M
    U=[r for r in range(M) if gcd(r,M)==1]
    res=[]
    for D in range(-M,0):
        fund = (D%4==1 and all(D%(q*q) for q in range(2,abs(D)+1))) or \
               (D%4==0 and (D//4)%4 in (2,3) and all((D//4)%(q*q) for q in range(2,abs(D)+1)))
        if not fund or M%abs(D): continue
        vals={r:kron(D,r) for r in U}   # chi_D(r) depends only on r mod |D| for r coprime to D (r>0)
        res.append((D,vals))
    return res
if __name__=="__main__":
    print("M  #units  #free  uncovered(=hard)  exactly kernel of chi_D (odd D, periodic mod M)?")
    for M in range(3,61):
        U,free=classes(M)
        hard=sorted(set(U)-free)
        hits=[D for D,vals in odd_quadratic_chars(M) if set(r for r in U if vals[r]==1)==set(hard)]
        print(M,len(U),len(free),hard if len(hard)<=8 else str(len(hard))+' classes',"chi:",hits[:3])
