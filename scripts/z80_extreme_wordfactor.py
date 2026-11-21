"""Independent exact word counts by factoring either n+u or nt+1. Order
outer letters u<=v, assign the t=u tie to the outer branch only."""
from cypari2 import Pari
import sys
P=Pari();P.default('factor_proven',1);P.allocatemem(128000000,silent=True)
def words(n):
    result=set();x=1
    while x**3-2*x<=n:
        # smallest = u=x <= t and <= v. If tu=1 there is no solution.
        for f in P.divisors(n+x).python():
            if (f+1)%x:continue
            t=(f+1)//x;v=(n+x)//f
            if x<=min(t,v):result.add((x,t,v));result.add((v,t,x))
        # smallest = t=x < u <= v
        for f in P.divisors(x*n+1).python():
            if f*f>x*n+1:break
            if (f+1)%x:continue
            u=(f+1)//x;g=(x*n+1)//f;v,r=divmod(g+1,x)
            if x<u and not r:result.add((u,x,v));result.add((v,x,u))
        x+=1
    assert all(t*u*v-u-v==n for u,t,v in result)
    return [sum(t%4==0 for u,t,v in result),sum(t%8==0 for u,t,v in result),sum(t*u%8==0 for u,t,v in result),sum(min(i%4 for i in (t,u,v,t*u-1,t*v-1))==0 for u,t,v in result),min((t*u-1 for u,t,v in result if min(t,u,v)>=2 and P.kronecker(t*u-1,n)==-1),default=0),len(result)]
if __name__=='__main__':
    print('n,R,R8,U7,ES5,HJmin,words',flush=True)
    for n in map(int,sys.argv[1:]):print(n,*words(n),sep=',',flush=True)
