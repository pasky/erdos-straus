# y7 (O215): list all solutions of m/n = 1/x+1/y+1/z (x<=y<=z), small n; classify Type (n | which denominators)
import sys
from math import gcd
def sols(m,n):
    out=[]
    for x in range(n//m+1, 3*n//m+1):
        A=m*x-n; B=n*x
        if A<=0: continue
        # A/B = 1/y+1/z, y<=z, y>=x
        for y in range(max(x,B//A+1), 2*B//A+1):
            num=A*y-B
            if num>0 and (B*y)%num==0: out.append((x,y,B*y//num))
    return out
if __name__=="__main__":
    m=int(sys.argv[1])
    for n in map(int,sys.argv[2:]):
        for s in sols(m,n):
            print(m,n,s,"n|",[d%n==0 for d in s])
