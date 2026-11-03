from sympy import isprime, divisors
def fires(p,x):
    for N in (p+x, x*p+1):
        for d in divisors(N):
            if d % x == x-1: return True
    return False
cnt=0; bad=0
for m in range(4,40001,4):
    p=5*m*m+1
    if not isprime(p): continue
    cnt+=1
    if fires(p,4): bad+=1; print("counterexample",p)
print(cnt,"primes checked, x=4 fires at",bad)
# control: all primes p = 1 mod 8 in [1e9, 1e9+2e5) (deterministic, not random): how often line x=4 fails
c=0;f=0
for p in range(10**9+1,10**9+200000,8):
    if isprime(p):
        c+=1; f+= (not fires(p,4))
print("control:",f,"/",c,"fail x=4")
