"""R214 from-scratch checks of G1, G2 (y1_gamma8_trace), R1 (y1_reciprocal_parity) and the K1 collision count
(y1_heegner_level_t). Not reusing y1_* scripts."""
import sys, math
from sympy import jacobi_symbol, primerange, divisors

def M(t,u,v):
    S=lambda x: ((x,-1),(1,0))
    def mul(P,Q): return tuple(tuple(sum(P[i][k]*Q[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return mul(mul(S(v),S(t)),S(u))

# G1: chi = f(M mod 8); also mod 4 and mod 16
B=int(sys.argv[1]) if len(sys.argv)>1 else 48
for mod in (4,8,16):
    tab={}; clash=0
    for t in range(1,B):
        for u in range(1,B):
            for v in range(1,B):
                n=t*u*v-u-v
                if n<1 or n%2==0: continue
                A=t*u-1
                chi=jacobi_symbol(-A % n, n) if n>1 else 1
                m=M(t,u,v); assert m==((n,-(t*v-1)),(t*u-1,-t)), (t,u,v,m)
                key=tuple(x%mod for r in m for x in r)
                if key in tab and tab[key]!=chi: clash+=1
                tab.setdefault(key,chi)
    print(f"G1 mod {mod}: keys={len(tab)} clashes={clash} (letters < {B})")

# G2 example
for w in [(1,3,3),(3,3,1)]:
    t,u,v=w; n=t*u*v-u-v; print("G2", w, "n=",n, "chi=", jacobi_symbol(-(t*u-1)%n,n), "trace", M(*w)[0][0]+M(*w)[1][1])

# K1 collisions: least t with a divisor A | tp+1, (-A/p) = -1, for p = 1 (24) < X
X=int(sys.argv[2]) if len(sys.argv)>2 else 200000
mx=0; cnt=0; arg=None
for p in primerange(25,X):
    if p%24!=1: continue
    cnt+=1
    for t in range(1,100):
        if any(jacobi_symbol((-A)%p,p)==-1 for A in divisors(t*p+1)):
            if t>mx: mx,arg=t,p
            break
    else: print("no t<100 at",p)
print(f"K1 collisions: {cnt} primes p=1(24) < {X}, max least t = {mx} (at p={arg})")
