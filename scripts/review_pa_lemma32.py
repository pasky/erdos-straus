"""R265 from-scratch check of PARITY_AUDIT Lemma 3.2 (squares; free chi-shadow at p=1(8))."""
from sympy import factorint, isprime, jacobi_symbol as J
def kron(D,n):  # Kronecker (D/n) for odd n>0 via Jacobi
    return J(D % n, n) if n>1 else 1
# (1) all squares m^2 (odd and even), u<=60: no divisor f of m^2+u with f=-1 mod 4u
from sympy import divisors
bad=[(m,u) for m in range(1,300) for u in range(1,61) if any(f%(4*u)==4*u-1 for f in divisors(m*m+u))]
print("square hits (m<300,u<=60):",bad[:5],len(bad))
# (2) p=1 mod 8, 1<=u<p QNR (u<=200): exists odd prime l | p+u, l!|u, kron(-4u,l)=-1 and (l/p)=-1
fails=0;tests=0
for p in range(17,40000,8):
    if not isprime(p): continue
    for u in range(1,min(p,200)):
        if J(u,p)!=-1: continue
        tests+=1
        ok=any(l>2 and u%l and kron(-4*u,l)==-1 and J(l,p)==-1 for l in factorint(p+u))
        fails+= not ok
print("chi-shadow tests",tests,"fails",fails)
# (3) p=5 mod 8 counterexamples to the free chi-shadow
ce=[(p,u) for p in range(13,2000,8) if isprime(p) for u in range(1,min(p,50)) if J(u,p)==-1
    and not any(l>2 and u%l and kron(-4*u,l)==-1 for l in factorint(p+u))]
print("p=5(8) counterexamples:",ce[:6],len(ce))
# (4) chi_{-4u}(f) = -1 for every hit f at primes (sanity of the oddness of chi_{-4u})
print(all(kron(-4*u,f)==-1 for u in range(1,40) for f in range(4*u-1,4000,4*u)))
