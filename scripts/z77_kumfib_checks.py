"""Exact small checks and bounded d-form probes; no giant integers n at locked indices."""
from math import lcm, isqrt, prod


def pell(t, d):
    # x_m + y_m sqrt(2) = (3 + 2 sqrt(2))^m: keep x_m,x_{m+1}
    a, b = 1, 3
    for bit in bin(t)[2:]:
        c = (2*a*b - 3) % d
        if bit == '1': a, b = c, (2*b*b - 1) % d
        else: a, b = (2*a*a - 1) % d, c
    return a % d


def res(family, t, d):
    if family == 'exp': return 752257 * pow(11, 2*t, d) % d
    if family == 'pell': return 4545 * pell(t, d)**2 % d
    g = 2*pow(3, t, d)-3
    return g*(256*g-33) % d


def probe(family, t, K, cap):
    for d in range(K-1, cap+1, K):
        a = -res(family, t, d) % d
        if a and (d+1) % (K*a) == 0: return (d, a)
    return None


def lock(B):
    # An exponent annihilating GL(2,Z/p^e) for every p^e <= B, also units.
    t = 1
    for p in range(2,B+1):
        if any(p%i==0 for i in range(2,isqrt(p)+1)): continue
        h = p; order = (p*p-1)*(p*p-p)
        while h*p<=B: h*=p; order*=p**4
        t = lcm(t, order)
    return t


def exact(n,K):
    # Independent: enumerate smaller a and B by factoring n+a = B*(K*a*h-1)
    for a in range(1, isqrt(n)+2):
        if K*a*a-2*a>n: break
        for b0 in range(1,isqrt(n+a)+1):
            if (n+a)%b0: continue
            for b in (b0,(n+a)//b0):
                if b>=a and ((n+a)//b+1)%(K*a)==0: return True
    return False


def main():
    for n in (1,17**2,4545,752257):
        for K in (4,8): assert not exact(n,K), (n,K)
    print('independent exact no-hit seeds (K=4,8): 1,289,4545,752257')
    for k, c, a,b,d in ((3,22,6,148,3),(4,2,1,5,1),(5,2,3,3,1)):
        n=c**k+1; assert 4*a*b*c*d==a+b+n*c
        print('positive cubic/quartic/quintic control',k,c,n,a,b,d)
    x,y=1,0
    for t in range(65):
        for m in (7,8,23,1080,7357): assert x%m==pell(t,m)
        for fam,n in [('exp',752257*11**(2*t)),('pell',4545*x*x)]:
            for K in (4,8):
                h=probe(fam,t,K,10000)
                if h:
                    d,a=h; assert (n+a)%d==0 and (d+1)%(K*a)==0
                    b=(n+a)//d; assert K*a*b*((d+1)//(K*a))-a-b==n
        x,y=3*x+4*y,2*x+3*y
    print('t=0..64: all probe hits independently substituted using full input and successive Pell multiplication')
    for t in range(1,201):
        g = 2*3**t-3
        n = g*(256*g-33)
        assert 8*g*(32*g)-g-32*g==n and isqrt(n)==16*g-2
        for d in (63,511,1009): assert n%d==res('moving',t,d)
    for H in (7,11,23,47):
        primes = [p for p in range(2,H+1) if all(p%j for j in range(2,isqrt(p)+1))]
        g = 8*prod(primes)-1
        n = g*(256*g-33)
        assert n%840==289 and isqrt(n)==16*g-2
        assert all(n%p==289%p for p in primes)
    print('moving controls: actual imprimitive witnesses t=1..200, primorial congruences H=7,11,23,47')
    for fam in ('exp','pell','moving'):
        for K in (4,8):
            hits=[probe(fam,t,K,10000) for t in range(2,201)]
            print(fam,'ordinary K',K,'decided',sum(h is not None for h in hits),'of',len(hits),'max first d',max(h[0] for h in hits if h))
        for B in (16,64,128,256):
            t=lock(B)
            row = [probe(fam,t,K,150000) for K in (4,8)]
            assert all(h is None or h[0]>B for h in row)
            print(fam,'locked B',B,'t bits',t.bit_length(),'first (d,a) K4,K8 through 150000',row,flush=True)


if __name__=='__main__': main()
