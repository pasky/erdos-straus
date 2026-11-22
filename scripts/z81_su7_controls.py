"""Literal control words and positivity tests: no certificate inferred from absence up to a cutoff."""
from math import isqrt
from pathlib import Path
from z80_square_span import jac,words,fac

def prime(n):return n>1 and all(n%j for j in range(2,isqrt(n)+1))

def u7(p,limit):
    for f in range(7,limit+1,8):
        r=(-p)%f
        if not r or (f+1)%r:continue
        yield f,r,(f+1)//r,(p+r)//f

def main():
    z=[105,1465,3865,4545,10305,12145,39361,67425]
    zstar=[int(x) for x in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if x and x[0].isdigit()]
    for p in [2521,3361,21841,76441,113035442521,1590284203561,3153419441929,6955940568721]+zstar:
        assert prime(p)
        for f,r,t,v in u7(p,min(2*p+1,1000000)):
            c=next((c for c in [1,3,5,7,9,25] if f%c==0 and prime(f//c)),None)
            if c is None:continue
            print('C6',p,f,c,f//c,r,t,v);break
        else:raise ValueError(p)
    for p in [9,25,49,81,121]+z+[17401609]:
        w=next(u7(p,2*p+1),None);W=words(p);g=next(((a,t,b) for a,t,b in sorted(W) if jac(a*t-1,p)==-1),None)
        print('control',p,'U7',w,'S',g)
    print('2521 complete interior',sorted(words(2521)))
    for n in [11,17,131,241]:
        # Complete sorted 8/n solutions via the smallest-variable bound and 2-term bounds.
        sol=[]
        for x in range(n//8+1,3*n//8+1):
            A,B=8*x-n,n*x
            for y in range(max(x,B//A+1),2*B//A+1):
                if B*y%(A*y-B)==0:sol.append((x,y,B*y//(A*y-B)))
        print('numerator_8',n,sol)
    for p,l,d,s1,s2,qs in [(26881,17,1,124593,1,[83,2447]),(341041,5,11,58330,13106,[151,239])]:
        for q in qs:
            assert prime(q) and all((4*C*p+1)%q==0 for C in (l,d*s1*s1,d*l*s2*s2));assert s1%l==0
            print('marked',p,q,q%(4*l),pow(q,(l-1)//4,l))
if __name__=='__main__':main()
