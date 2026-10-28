import sys; sys.path.insert(0,'scripts')
from z49_i3fable_stats import M0_exact
from sympy import divisors
from math import log
def Ct(n):
    s=0.0
    for u in range(3,(n+3)//8+1):
        N=n+u; lo=3*u-1; hi=N//3
        if lo>hi: break
        s+=sum(1 for d in divisors(N) if lo<=d<=hi)/u
    return s
for n in [100003, 123456, 999983, 1000000, 2433600]:
    c=Ct(n); m=M0_exact(n)
    print(n, "Ctilde=%.2f  M0=%.2f  ratio=%.3f  bound (1/(72 ln2)) log^2 n = %.2f"%(c,m,c/m,log(n)**2/(72*log(2))))
