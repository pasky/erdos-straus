# Z1709: does every coset (a0,b0) mod M with a0^2+b0^2 ≡ (unit square) mod M contain a point (a,b)
# with a^2+b^2 = m^2 an odd square, gcd(m,M)=1?  (Hilbert 90: N(alpha)=s^2 <=> alpha = s*delta^2/N(delta).)
# If yes, any 2-variable identity in (a,b) with p=a^2+b^2 valid on such a coset meets T1 at m^2.
import math, sys
M=int(sys.argv[1]); B=int(sys.argv[2])
sq={(x*x)%M for x in range(M) if math.gcd(x,M)==1}
need=set()
for a0 in range(M):
    for b0 in range(M):
        if (a0*a0+b0*b0)%M in sq: need.add((a0,b0))
hit=set()
# enumerate Pythagorean-type points: alpha = s*delta^2/N(delta), with integral results; simpler: all (a,b) with a^2+b^2=m^2 via m up to B
for m in range(1,B,2):
    if math.gcd(m,M)!=1: continue
    for a in range(-m,m+1):
        b2=m*m-a*a; b=math.isqrt(b2)
        if b*b==b2:
            for bb in (b,-b): hit.add((a%M,bb%M))
print("M",M,"cosets with unit-square norm:",len(need),"hit by odd-square-norm points (m<%d):"%B,len(need&hit), "missing:",len(need-hit))
