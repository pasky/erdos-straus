# Z0321: local point counts #U_n(Z/m) for 4xyz = n(xy+yz+zx), m = l^k, l != n: check n-flatness (F3 of
# BRAINSTORM/markoff_hasse_failures_vs_es.md) and the p-adic factor at m = p^k.
import itertools
def cnt(n,m):
    c=0
    for x in range(m):
        for y in range(m):
            a=(4*x*y-n*(x+y))%m; b=(n*x*y)%m     # z*(4xy - n(x+y)) = n x y
            c+=sum(1 for z in range(m) if (a*z-b)%m==0)
    return c
for m in (3,9,5,25,7,49,8,16):
    print(m,[ (n,cnt(n,m)/m**2) for n in (1,13,17,29,37,41) if m%n and (m%2 or n%2)])
for p in (5,13):
    print('p-adic',p,[(k,cnt(p,p**k)/p**(2*k)) for k in (1,2)])
