# z52d avenue P00 / Z1624: Type I c=1 (f | p^2+4d, f ≡ -p mod 4d) <=> exists k: pk+1 has a divisor g ≡ -p (mod 4k). Numerical cross-check p<3000.
# Type I c=1 shifted form check: exists d,f: f|p^2+4d, f≡-p mod 4d  <=> exists k: g|pk+1, g≡-p mod 4k, g>0
from sympy import isprime, divisors
def typeI_c1(p,D):
    for d in range(1,D):
        N=p*p+4*d
        for f in divisors(N):
            if (f+p)%(4*d)==0: return True
    return False
def shifted(p,K):
    for k in range(1,K):
        for g in divisors(p*k+1):
            if (g+p)%(4*k)==0: return True
    return False
bad=[]
for p in range(5,3000):
    if isprime(p) and p%4==1:
        a=typeI_c1(p,1500); b=shifted(p,1500)
        if a!=b: bad.append(p)
print("mismatch",bad, "typeI fail list", [p for p in range(5,3000) if isprime(p) and p%4==1 and not shifted(p,1500)])
