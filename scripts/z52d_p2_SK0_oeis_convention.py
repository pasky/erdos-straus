from fractions import Fraction as F
import math
def primes(n):
    s=[1]*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=0
    return [i for i in range(n+1) if s[i]]
def count_unordered(p):
    cnt=0; t=F(4,p)
    x=-(-p//4)
    while True:
        r=t-F(1,x)
        if r<=0 or x>3*p//4+1: break
        if 1/r < 1 and False: pass
        # x <= y <= z with 1/y+1/z = r ; y <= 2/r, y >= max(x, 1/r)
        ylo=max(x, math.floor(1/r)+1); yhi=math.floor(2/r)
        for y in range(ylo, yhi+1):
            r2=r-F(1,y)
            if r2>0 and r2.numerator==1 and r2.denominator>=y: cnt+=1
        x+=1
    return cnt
ps=primes(60)
print([(p,count_unordered(p)) for p in ps[:12]])
