"""Lane 4 finite checks (stdlib only). No asymptotic is inferred from a census."""
from fractions import Fraction as F
from collections import Counter
from math import gcd, isqrt, prod, sqrt, pi


def primes(n):
    tab = bytearray(b'\1') * (n + 1)
    tab[:2] = b'\0\0'
    for q in range(2, isqrt(n) + 1):
        if tab[q]:
            tab[q*q::q] = bytes((n - q*q)//q + 1)
    return (i for i in range(2, n+1) if tab[i])


def chi(a, k):
    r = pow(a, (k-1)//2, k)
    return -1 if r == k-1 else r


def rootup(q):
    scale = 10**12
    return F(1 + isqrt((q*scale**2).__floor__()), scale)


w, v, tau2 = F(31, 100), F(1, 8), F(4999, 10000)
zeta = 1/(2+w*w)
tau = zeta*(1+v*v)
# Inner integral after the two substitutions in z81, with negative correction.
jhi = 4*w**3/3 - 14*w**5/(15*(1+w*w)**2)
low = 4*(v-v**3/6)/(F(22, 7)*rootup(tau))
cost = F(3,4)*(2/tau2)*rootup(2/tau2)*jhi
assert low-cost > F(1, 350) and tau < F(4846, 10000)
print('thin level, zeta, switched level:', tau, zeta, tau2)
print('certified rational lower margin:', low-cost, '>', F(1,350))
print('rounded margin lower:', float(low-cost))

# Unconditional asymmetric (complete, truncated) sieve. Upper/lower square
# roots and the positive atanh series avoid using libm for the sign.
def rootlo(q):
    return rootup(q) - F(1, 10**12)


def ash(s):
    x = rootlo((s-1)/s)
    return sum(x**(2*i+1)/(2*i+1) for i in range(23))


a,b = F(445,1000), F(1,100)
s7 = F(26,10); s3=(F(499,1000)-s7*b)/a
dp = F(499,1000)-2*b/a
wmax = rootup(1/a-2)
# On each subinterval bound s^2 and sqrt(2+s^2) at the right end,
# (1+s^2)^(-2) at the left. Round up contributions before summing.
J2 = F(0)
for i in range(1000):
    left = wmax*i/1000; right = left + wmax/1000
    summand = 2*right**2*rootup(2+right**2)*(1+2/(1+left**2)**2)/3
    J2 += F((summand*10**12).__ceil__(), 10**12)*wmax/1000
Ahi=F(152,100) # gamma<0.58, exp(.58)<1.8, pi>3.14
# one factor A divided out of the margin
margin = (ash(s3)/rootup(s3) - Ahi/rootlo(s3)*(1/rootlo(F(2))-ash(s7)/rootup(s7))
          - Ahi*rootup(a/2)*J2/dp)
assert margin>F(1,250)
print('asymmetric sieve a,b,s3,s7,dp:',a,b,s3,s7,dp)
print('J2 rigorous upper (display rounded):',float(J2),'margin/A certified > 1/250')

for k in [3,7]:
    # Formula from L(1,chi) for odd primitive real characters. Inert product
    # omitted logarithmic tail <= sum_{j>N} 2/(j-1)^2 for these products.
    lk = -pi/k**1.5 * sum(a*chi(a,k) for a in range(1,k))
    N = 1_000_000
    bad = [q for q in primes(N) if chi(q,k)<0]
    ck = sqrt(lk*(1-1/k)*prod(1-1/q**2 for q in bad)/pi)
    ak = 2*ck*prod(1/(1-1/q) for q in [2,3,5,7] if chi(q,k)!=1)*prod(1-1/(q-1)**2 for q in bad if q>7)
    print('k, Euler cutoff, C, A, A/32, A/192 (float):',k,N,ck,ak,ak/32,ak/192)
    # Bound A^2 using fixed-point interval multiplication (no huge rational
    # products), L(1,chi)/pi = -sum a chi(a)/(k sqrt(k)).
    scale = 10**25
    negsum = -sum(a*chi(a,k) for a in range(k))
    finite = 4*F(negsum,k)*F(k-1,k)*prod(F(q,q-1)**2 for q in [2,3,5,7] if chi(q,k)!=1)
    lo = (finite*scale/rootup(F(k))).__floor__(); hi=(finite*scale/rootlo(F(k))).__ceil__()
    for q in bad:
        num, den = q*q-1, q*q
        if q>7:
            z=(q-1)**2; num *= (z-1)**2; den *= z*z
        lo=lo*num//den; hi=-((-hi*num)//den)
    # log-free union bound for the omitted products, since sum_{m>N}
    # [(1/m^2)+2/(m-1)^2] <= 3/(N-1).
    lower=rootlo(F(lo,scale)*(1-F(3,N-1))); upper=rootup(F(hi,scale))
    print('certified interval for A:',lower,upper)
    digits={3:F(22132,10000),7:F(22405,10000)}[k]
    assert digits<lower<upper<digits+F(1,10000)
    for r in [1,121,169,289,361,529]:
        h=k+1; b=(r+k)//h; M=840//h; s=gcd(b,M); Q=M//s
        assert h*b==r+k and h*s*Q==840 and chi(b//s,k)==1 and gcd(b//s,Q)==1
        assert all(chi(q,k)==1 for q in primes(s) if s%q==0)
        assert all(Q%q==0 for q in [2,3,5,7] if chi(q,k)!=1)
        print('fibre k,r,s,Q,b1:',k,r,s,Q,b//s)

# Toy H2 with signed coefficients: compare the actual quotient square with a
# separate enumeration by determinant and measure the false noncoprime edges.
# No Fourier estimates or primality asymptotics are being tested here.
labels = [i*j for i in (11,13) for j in (17,19)]
mn = Counter()
for m in range(360,721):
    for n in range(320,641):
        if gcd(m*n, 2*11*13*17*19)==1:
            mn[m*n] += (-1 if m%4==3 else 1)*(1+n%4)
for k in [3,7]:
    byH=Counter()
    for P,cnt in mn.items():
        for a in labels:
            if (P+k)%a==0:
                byH[(P+k)//a]+=cnt
    direct=sum(x*x for h,x in byH.items() if h%(k+1)==0)
    paired=spurious=disjoint=0
    for a in labels:
        for c in labels:
            for P,cnt in mn.items():
                num=c*P+k*(c-a) # cP-aP'=k(a-c)
                if num%a or (Q:=num//a) not in mn: continue
                if (P+k)%a:
                    assert gcd(a,c)>1
                    spurious+=1; continue
                if ((P+k)//a)%(k+1)==0:
                    paired+=cnt*mn[Q]
                    disjoint+=gcd(a,c)==1
    assert direct==paired and min(paired,spurious,disjoint)>0
    print('toy H2: k, quotient-square=determinant sum, disjoint edges, spurious unrestricted pairs:',k,direct,disjoint,spurious)
