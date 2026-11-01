# Z0212: 2-adic shapes of ES solutions at primes p ≡ 1 (4).
# Lemma (2-adic): with a_i = v2(x_i) sorted a1>=a2>=a3, every solution has a1 = a2 > a3.
# 'all even' (8/p)  ⟺ a3 >= 1 ;  'some den ≡ 0 (4)' ⟺ a1 >= 2.  all-even ⇒ some ≡ 0 (4).
# Test the converse existence-wise and count shapes.
import sys
from math import gcd
from sympy import divisors, primerange
def v2(n):
    c=0
    while n%2==0: n//=2;c+=1
    return c
def sols(p):
    for x in range((p+3)//4, 3*p//4+1):
        A=4*x-p; B=p*x; g=gcd(A,B); A//=g; B//=g
        for d in divisors(B*B):
            if d>B: break
            if (B+d)%A==0 and (B+B*B//d)%A==0:
                y=(B+d)//A; z=(B+B*B//d)//A
                if y>=x: yield (x,y,z)
N=int(sys.argv[1])
bad_shape=0; only4=[]; fail_both=[]
for p in primerange(5,N):
    if p%4!=1: continue
    has_even=has4=False
    for s in sols(p):
        a=sorted((v2(t) for t in s),reverse=True)
        if not (a[0]==a[1]>a[2]): bad_shape+=1
        if a[2]>=1: has_even=True
        if a[0]>=2: has4=True
    if has4 and not has_even: only4.append(p)
    if not has4: fail_both.append(p)
print("N",N,"shape violations",bad_shape)
print("primes with a 4|den solution but no all-even solution:",only4)
print("primes with no 4|den solution:",fail_both)
