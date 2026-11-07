# Verify the master identities for prime p (and check they cover ALL solutions with p | exactly two / exactly one denominator).
# Case (ii)  [p | exactly two denominators]: if 4YZ | p+s and s | Y+Z, g'=(p+s)/(4YZ), m=(Y+Z)/s then
#      4/p = 1/(g'YZ) + 1/(p m g' Y) + 1/(p m g' Z).   R(p) is the sub-family s = Y+Z (m=1).
#   Class form: p = -4g'Y^2 (mod 4g'Ym-1).
# Case (i)   [p | exactly one denominator]: t=3(4), w=(pt+1)/4, a|w, b|w, t|a+b:
#      4/p = 1/((w/a)(a+b)/t) + 1/((w/b)(a+b)/t) + 1/(p w).
from fractions import Fraction as F
from sympy import primerange, divisors
def case2(p,Y,Z,s):
    if (p+s)%(4*Y*Z) or (Y+Z)%s: return None
    g=(p+s)//(4*Y*Z); m=(Y+Z)//s
    x,y,z=g*Y*Z,p*m*g*Y,p*m*g*Z
    assert F(1,x)+F(1,y)+F(1,z)==F(4,p),(p,Y,Z,s)
    return (x,y,z)
def case1(p,t,a,b):
    if t%4!=3: return None
    w=(p*t+1)//4
    if (p*t+1)%4 or w%a or w%b or (a+b)%t: return None
    x=(w//a)*(a+b)//t; y=(w//b)*(a+b)//t
    assert (w//a)*(a+b)%t==0 and (w//b)*(a+b)%t==0
    assert F(1,x)+F(1,y)+F(1,p*w)==F(4,p),(p,t,a,b)
    return (x,y,p*w)
def all_solutions(p):
    # all (x<=y<=z) with 4/p = 1/x+1/y+1/z
    sols=set()
    x=p//4+1
    while F(3,x)>=F(4,p):
        r=F(4,p)-F(1,x)
        y=x
        while y<= int(2/r)+1 and F(1,y)+F(1,y)>=r:
            r2=r-F(1,y)
            if r2>0 and r2.numerator==1: sols.add((x,y,r2.denominator))
            y+=1
        x+=1
    return sols
if __name__=="__main__":
    for p in primerange(5,80):
        if p%4!=1: continue
        sols=all_solutions(p)
        found=set()
        for Y in range(1,p):
            for Z in range(1,p):
                if 4*Y*Z>p+Y+Z: break
                for s in divisors(Y+Z):
                    r=case2(p,Y,Z,s)
                    if r: found.add(tuple(sorted(r)))
        for t in range(3,2*p*p,4):
            w=(p*t+1)//4
            dv=divisors(w)
            for a in dv:
                for b in dv:
                    r=case1(p,t,a,b)
                    if r: found.add(tuple(sorted(r)))
        assert found<=sols,(p,found-sols)
        miss=sols-found
        print(p,len(sols),len(found),"missed:",miss)
        assert not miss
    print("identities verified and exhaustive for primes p=1(4) < 80")
