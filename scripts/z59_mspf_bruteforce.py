# brute force: count (u,B,C) with 4uBC-u-B=n, compare to 4kB | n+k+B count
import math
def R_triple(n):
    c=0
    for u in range(1,n+1):
        for B in range(1,n//(2*u)+2):
            t=n+u+B
            if t%(4*u*B)==0: c+=1
    return c
def R_d(n):
    c=0
    for d in range(3,2*n+2,4):
        k=(-n)%d
        if k and ((d+1)//4)%k==0: c+=1
    return c
bad=0
for n in range(1,3000,4):
    a=R_triple(n); b=R_d(n)
    if a!=b: bad+=1; print("MISMATCH",n,a,b)
print("checked, mismatches:",bad)
