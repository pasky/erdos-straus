# Z1378: does every n have a solution with max(x,y,z) <= n^2?  (★) solutions satisfy max <= n^2/2 (PROVED, see outcome).
# Check the 14 (★)-sterile primes <= 1e10 via general Type II: x=abd, y=nacd, z=nbcd, nc+a+b=4abcd,
# i.e. (4acd-1)(4bcd-1) = 4nc^2 d + 1.  Report the least max-denominator found with c,d <= 60.
from sympy import divisors
from fractions import Fraction as F
ster=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
for n in ster:
    best=None
    for c in range(1,61):
        for d in range(1,61):
            M=4*c*d; N=4*n*c*c*d+1
            for f in divisors(N):
                if f*f>N: break
                if f%M==M-1:
                    g=N//f
                    if g%M!=M-1: continue
                    a=(f+1)//M; b=(g+1)//M
                    x,y,z=a*b*d,n*a*c*d,n*b*c*d
                    if F(1,x)+F(1,y)+F(1,z)!=F(4,n): continue
                    mx=max(x,y,z)
                    if best is None or mx<best[0]: best=(mx,(a,b,c,d))
    print(n, best, 'max/n^2=%.3f'%(best[0]/n/n) if best else 'none')
