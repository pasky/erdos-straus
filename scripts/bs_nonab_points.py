"""O147(c): (1) #U_n(F_l) for 4xyz = n(xy+yz+zx) over F_l (brute, small l); (2) Type I/II counts at cubes m^3."""
import math, sys
def cnt(n,l):
    return sum(1 for x in range(l) for y in range(l) for z in range(l) if (4*x*y*z-n*(x*y+y*z+z*x))%l==0)
print("(1) point counts N(n,l) vs l^2+1:")
for l in [3,5,7,11,13]:
    print(l, [(n,cnt(n,l)) for n in [1,2,5,7,13,l,2*l]], "l^2+1 =",l*l+1)
def types(n):
    t1=t2=0
    for x in range(n//4+1, n+1):
        num,den=4*x-n, n*x            # 1/y+1/z = num/den, y<=z
        if num<=0: continue
        for y in range(max(x, den//num+1), 2*den//num+1):
            zn=num*y-den
            if zn<=0 or (den*y)%zn: continue
            z=den*y//zn
            if z<y: continue
            v=[x,y,z]; dv=[w%n==0 for w in v]; k=sum(dv)
            cop=all(math.gcd(n,w)==1 for w,d in zip(v,dv) if not d)
            if k==1 and cop: t1+=1
            if k==2 and cop: t2+=1
    return t1,t2
print("(2) (m, n, Type I, Type II) counts, x<=y<=z:")
for m in [3,5,7,9,11,13,15]:
    for e in [2,3]:
        n=m**e; print(m,e,n,types(n))
