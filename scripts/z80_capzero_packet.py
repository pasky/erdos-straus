"""Whole inert coset, no factorization of the opaque input. Tiny M=1 packets."""
from z80_square_span import primes_to,jac,fac
from math import prod

def packet(q,M=1):
    Q=(q-1)//2;h=next(pow(x,2,q) for x in range(2,q) if all(pow(x,2*(Q//l),q)!=1 for l,e in fac(Q)))
    power=1;w=[]
    while power<Q:
        r=pow(h,power,q);w.append(1+M*((r-1)*pow(M,-1,q)%q));power*=3
    return h,w

def main():
    tested=0
    for q in primes_to(1000):
        if q%4!=3 or q<7:continue
        h,w=packet(q);G=prod(w);rep={1:(1,1)}
        for z in w:
            old=dict(rep)
            for r,(a,b) in old.items():rep[r*z%q]=z*a,b;rep[r*pow(z,-1,q)%q]=a,z*b
        for ell in range(1,q):
            if jac(ell,q)!=-1:continue
            a,b=rep[-ell%q];b*=ell;n=4*G*ell-q
            if n<=1:continue
            d=G*ell//(a*b);c=(a+b)//q
            assert a+b==q*c and 4*a*b*d==n+q and d>=1
            x,y,z=a*b*d,n*a*c*d,n*b*c*d
            assert 4*x*y*z==n*(x*y+x*z+y*z)
            tested+=1
    print('positive test reconstructions',tested)
    for n in [9,25,49,81,131,241,4545,17401609,1590284203561]:
        hits=[]
        for q in primes_to(200):
            if q%4!=3 or q<7 or n%4!=1 or jac(n,q)!=-1:continue
            h,w=packet(q);G=prod(w)
            if (n+q)%(4*G)==0:hits.append(q)
        print(n,'eligible q<=200',hits)
if __name__=='__main__':main()
