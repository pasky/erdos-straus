"""Exploration only: composite midpoint quadrature; no floating sign is used as proof."""
from math import asinh,sqrt,exp,pi,log
from functools import lru_cache
A=2*sqrt(exp(.5772156649015329)/pi); tau=.49999

def f(s):return 0 if s<1 else A*asinh(sqrt(min(s,3)-1))/sqrt(min(s,3))
# Positive correction beyond s=2, 24-point midpoint quadrature on the smooth substitution.
@lru_cache(maxsize=60000)
def F(s):
    if s<=2:return A/sqrt(s)
    s=min(s,4); top=sqrt(s-2); h=top/24
    return (A+sum((w:=h*(i+.5))*f(1+w*w)/sqrt(2+w*w) for i in range(24))*h)/sqrt(s)
@lru_cache(None)
def J1(a):
    h=sqrt(1-2*a)/128
    return sum(log((1-(h*(i+.5))**2-a)/a)/(1-(h*(i+.5))**2) for i in range(128))*h

def margin(a,b,ret=False):
    lo,s=max(((f((tau-b*v)/a)*F(v) - F((tau-b*v)/a)*(F(v)-f(v)),v) for i in range(21) if (v:=1+i*.1)*b<tau and (tau-b*v)>a), default=(-10,0))
    sw,sp=min((A*sqrt(a)*J1(a)*F(v)/(tau-b*v),v) for v in [1+i*.1 for i in range(31)] if tau-b*v>0)
    return (lo-sw,s,sp) if ret else lo-sw

def U(a,b,D):
    return min(F(v)*F((D-v*b)/a) for v in [1,1.5,2,2.5,3,3.5,4, D/(2*b)] if 0<v*b<D)

def rich(a,b,y):
    step=log(y/b)/48
    return .5*step*sum((1-(t:=b*exp(step*(i+.5)))/y)*U(a,b,tau-t) for i in range(48))

if __name__=='__main__':
    for b in [.01,.015,.02,.025,.03,.035,.04,.05,.1]:
        m,a=max((margin(a,b),a) for i in range(251,470,2) if (a:=i/1000) <tau-b);print('b margin a splits',b,m,a,margin(a,b,True)[1:])
    best=(200,)
    for b in [.002,.004,.006,.008,.01,.012,.014,.016,.018,.02]:
        for i in range(340,470,5):
            a=i/1000;B=margin(a,b)
            if B<=0:continue
            for y in [.25,.3,.35,.4,.45,.48]:best=min(best,(1/y+rich(a,b,y)/B,a,b,y,B,rich(a,b,y)))
    print('Richert count, a,b,y,B,charge',best)
