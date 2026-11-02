# brute-force 2-cycle count N2 (unordered pairs {u,B} in (U,2U], u<B, uB | n+u+B) and N4 (4 | level); cross-check for z54_bilindiv_td.c
import sys, math
def iroot4(n):
    r=int(round(n**0.25))
    while (r+1)**4<=n: r+=1
    while r**4>n: r-=1
    return r
for line in sys.stdin:
    n=int(line); U=iroot4(n); N2=N4=0
    for u in range(U+1,2*U+1):
        for B in range(u+1,2*U+1):
            if (n+u+B)%(u*B)==0:
                N2+=1; k=(n+u+B)//(u*B)
                if k%4==0: N4+=1
    print(n,U,N2,N4)
