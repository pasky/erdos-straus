# For prime q: which residues r (x_q = r exactly, x_l = 1 for l != q, l incl. 2) lie in U?
import sys
from sympy import divisors, legendre_symbol, primerange
D=int(sys.argv[1]); UK=int(sys.argv[2])
for q in primerange(3,int(sys.argv[3])):
    def vq(m):
        v=0
        while m%q==0: m//=q; v+=1
        return v
    cov={}
    def test(a,m,tag):
        v=vq(m); Q=q**v; mm=m//Q
        if (a-1)%mm: return
        for r in range(1,q):
            if r not in cov and (a-r)%Q==0: cov[r]=tag
    for d in range(3*q,D,4*q):   # d = 3 mod 4, q | d
        pass
    for d in range(3,D,4):
        if d%q==0:
            for k in divisors((d+1)//4): test(-k,d,('d',d,k))
    for u in range(1,UK):
        for k in range(1,UK):
            if (u*k)%q==0: test(-u-k,4*u*k,('uk',u,k))
    nr=[r for r in range(1,q) if legendre_symbol(r,q)==-1]
    print(q, 'NR:',nr, 'covered:',sorted(cov), {r:cov[r] for r in sorted(cov)})
