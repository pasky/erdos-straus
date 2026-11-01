# z52d pass2 SK1 (Z0859): check x|z <=> y|z over ALL solutions of 4/p (x<=y<=z), p prime <= N, and how often the
# lcm-closed family z = lcm(x,y) (the item's parametrisation) is exhaustive.
# 4/p=1/x+1/y+1/z: z = p*x*y/(a*y - p*x), a = 4x-p, need a*y > p*x and integrality, y in [x, 2px/a].
import sys
from math import gcd
N=int(sys.argv[1])
def isp(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
mism=0; xz=0; xz_lcm=0; sols=0; primes=0; minz_lcm_fail=0; z_div_p=0
for p in range(3,N+1,2):
    if not isp(p): continue
    primes+=1
    for x in range(p//4+1, 3*p//4+1):
        a=4*x-p
        if a<=0: continue
        ymax=(2*p*x)//a
        for y in range(x, ymax+1):
            d=a*y-p*x
            if d<=0: continue
            num=p*x*y
            if num % d: continue
            z=num//d
            if z<y: continue
            sols+=1
            if z%p==0: z_div_p+=1
            a1=(z%x==0); a2=(z%y==0)
            if a1!=a2: mism+=1
            if a1:
                xz+=1
                if x*y//gcd(x,y)==z: xz_lcm+=1
                else: minz_lcm_fail+=1
print(f"primes={primes} solutions={sols} p|z in {z_div_p}  mismatch(x|z vs y|z)={mism}  x|z solutions={xz}; of these z=lcm(x,y): {xz_lcm}, z!=lcm: {minz_lcm_fail}")
