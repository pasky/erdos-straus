"""R219: naive brute force (no factoring) over words of X_n with |t|<=T: list least |t| for strictly-signed
and for positive chi=-1 words. chi=(-A/n) via sympy-free Jacobi (Python's own implementation below)."""
import sys
def jac(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def words(n,t):
    M=t*n+1
    # A = t*u-1 divides M; iterate over u with |A|<=|M|
    out=[]
    for A in range(-abs(M),abs(M)+1):
        if A==0 or A==-1 or M%A: continue
        if (A+1)%t: continue
        B=M//A
        if B==-1: continue
        u=(A+1)//t; v=(B+1)//t
        assert t*u*v-u-v==n
        out.append((t,u,v,A,jac(-A,n)))
    return out
n=int(sys.argv[1]); T=int(sys.argv[2])
for s in range(1,T+1):
    for t in (s,-s):
        for w in words(n,t):
            pos = w[0]>0 and w[1]>0 and w[2]>0
            if w[4]==-1: print("chi=-1", "POS" if pos else "SGN", w)
