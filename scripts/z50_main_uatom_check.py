from fractions import Fraction as F
import random
random.seed(1)
cnt=0
for _ in range(20000):
    k=random.choice([1,5,9,13,17,21]); l=random.choice([3,7,11,19,23,31,43,47,59,67,71,79,83,103,107])
    M=k*l
    divs=[w for w in range(1,M+2) if (M+1)%(4*w)==0]
    if not divs: continue
    w=random.choice(divs)
    # n ≡ -4w mod M, n ≡ 1 mod 4
    for n in range(M-4*w+M, M-4*w+M+40*M, M):
        if n%4!=1 or n<=0: continue
        t=(M+1)//(4*w); u=(n+4*w)//M; v=4*w
        assert t*u*v-u-v==n
        assert F(4,n)==F(1,w*(t*u-1))+F(1,n*t*w)+F(1,n*t*w*(t*u-1)), (n,k,l,w)
        cnt+=1
print("ok: (atom, n) pairs checked =",cnt)
