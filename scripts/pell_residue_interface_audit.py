"""Finite checks of localized slopes, all residue digits, and division-free decoding."""
from math import gcd


def power_pair(x, w2, s, mod):
    # Coefficients of (x+w)^s with w²=w2=x²+1. Works at negative s.
    a, b = 1, 0
    c, d = (x if s >= 0 else -x) % mod, 1
    s = abs(s)
    while s:
        if s & 1:
            a, b = (a*c+w2*b*d) % mod, (a*d+b*c) % mod
        c, d = (c*c+w2*d*d) % mod, 2*c*d % mod
        s >>= 1
    return a, b


def exact(n, x, y, s):
    a,b = 1,0
    for _ in range(abs(s)):
        xx = x if s >= 0 else -x
        a,b = a*xx+n*b*y, a*y+b*xx
    return a,b


def lift(n, x, k, D):
    a, m = 0, 1
    for _ in range(k):
        f = power_pair(x, x*x+1, 1+4*a, m*n)[1]
        digit, r = divmod(D-f,m)
        assert not r
        a += m*(digit*pow(4,-1,n)%n)
        m *= n
    return a


def verify(n,x,y,k):
    assert x*x+1 == n*y*y
    N = n**k
    seen = bytearray(N)
    for a in range(N):
        D = power_pair(x, x*x+1, 1+4*a,N)[1]
        assert not seen[D]
        seen[D] = 1
    assert all(seen)
    for D in (0,1,2,n-1, N//2,N-1):
        a = lift(n,x,k,D)
        # Compute raw Y_s modulo yN in the original quadratic ring; don't divide by y.
        s=1+4*a; mod=y*N
        A,B=1,0; c,d=x,y
        while s:
            if s&1:
                A,B=(A*c+n*B*d)%mod,(A*d+B*c)%mod
            c,d=(c*c+n*d*d)%mod,2*c*d%mod
            s >>= 1
        assert (-N*B)%(mod+1) == D
    for a in (-3,0,4):
        for gap in (-n,-5,-1,1,5,n):
            j=1+4*a; m=j+4*gap
            Xh,_=exact(n,x,y,(m+j)//2); _,Yd=exact(n,x,y,(m-j)//2)
            raw=exact(n,x,y,m)[1]-exact(n,x,y,j)[1]
            assert raw == 2*Xh*Yd
            num = raw//y-(m-j); den=abs(m-j)
            assert num%(n*gcd(den,n**den.bit_length()))==0
    print(f'n={n}, gcd(n,y)={gcd(n,y)}, all {N} residues, slopes and lifting verified')


if __name__=='__main__':
    for args in [(5,682,305,5),(65,8,1,2),(125,682,61,2),(185,68,5,2),(325,18,1,2)]:
        verify(*args)
