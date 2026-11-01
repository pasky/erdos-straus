# Z0895: verify isosceles law 4/n = 2/x + 1/z (x,z>0, any order) solvable <=> n has a prime factor != 1 mod 4
# via factorisation (4x-2n)(4z-n) = 2n^2: enumerate divisors A of 2n^2.
from sympy import divisors, factorint
def iso(n):
    N=2*n*n
    for A in divisors(N):
        B=N//A
        if (A+2*n)%4==0 and (B+n)%4==0: return True
    return False
def brute(n):
    # 2/x+1/z=4/n, x>n/2; z=n x/(4x-2n)
    for x in range(n//2+1, 2*n*n):  # x bounded: 4x-2n <= 2n^2
        d=4*x-2*n
        if d>2*n*n: break
        if (n*x)%d==0: return True
    return False
bad=[]
for n in range(2,3001):
    a=iso(n); b=a if n>400 else brute(n)
    pred = not all(q%4==1 for q in factorint(n))
    if a!=pred or a!=b: bad.append(n)
fails=[n for n in range(2,3001) if not iso(n)]
print("mismatches",bad[:10],len(bad)); print("failures",len(fails),fails[:12])
