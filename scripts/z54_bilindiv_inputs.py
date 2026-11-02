# Input lists for Z54_BILINDIV §6 (writes to the directory given as argv[1], default /tmp):
#  p8 (300 consecutive primes > 1e8), p12/p14/p16/p18 (20/10/6/3 primes = 1 mod 24 after 1e12/1e14/1e16/1e18),
#  sq12/ns12 (10 odd squares (m+2i)^2, m = isqrt(1e12)|1, and the near-squares +4), sq16 (3 odd squares near 1e16),
#  test (the 14 FRONTIER §4 item-14 inputs), p10big/p12big (8000/4000 consecutive primes after 1e10/1e12).
import sys, math
from sympy import nextprime
d=sys.argv[1] if len(sys.argv)>1 else '/tmp'
def w(name,L): open(f'{d}/{name}.txt','w').write('\n'.join(map(str,L))+'\n')
def cons(base,cnt):
    p=base; out=[]
    while len(out)<cnt: p=nextprime(p); out.append(p)
    return out
def mod24(base,cnt):
    p=base; out=[]
    while len(out)<cnt:
        p=nextprime(p)
        if p%24==1: out.append(p)
    return out
w('p8',cons(10**8,300)); w('p12',mod24(10**12,20)); w('p14',mod24(10**14,10)); w('p16',mod24(10**16,6)); w('p18',mod24(10**18,3))
m=math.isqrt(10**12)|1; w('sq12',[(m+2*i)**2 for i in range(10)]); w('ns12',[(m+2*i)**2+4 for i in range(10)])
m=math.isqrt(10**16)|1; w('sq16',[(m+2*i)**2 for i in range(3)])
w('test',[409,577,5569,9601,23929,83449,102001,329617,712321,8813281,193,2521,66529,3361])
w('p10big',cons(10**10,8000)); w('p12big',cons(10**12,4000))
