"""Finite algebra checks for WILD_ES; not an asymptotic test."""
from math import gcd, isqrt
from pathlib import Path


def prime(x):
    return x > 1 and all(x % i for i in range(2, isqrt(x) + 1))


def atom(n, u, v, f):
    if (n*v + u) % f:
        return False
    w, s = (f+1)//(4*u*v), (n*v+u)//f
    x, y, z = s*u*w, n*s*v*w, n*u*v*w
    assert x > 0 and 4*x*y*z == n*(x*y+x*z+y*z)
    return True


def tests():
    # Every residue, not just one successful parameter in a cell.
    for A, B, C in [(1,0,-3),(1,0,24),(3,2,-5),(1,0,0)]:
        ct = [0, 0, 0]
        for l in filter(prime, range(11,300)):
            for k in [1,3,5,7]:
                f = k*l
                for u in range(2,24):
                    for v in range(1,9):
                        if gcd(u,v)>1 or (f+1)%(4*u*v):
                            continue
                        D = v*((B*B-4*A*C)*v-4*A*u)
                        roots = [m for m in range(l) if ((A*m*m+B*m+C)*v+u)%l==0]
                        assert len(roots) == (1 if D%l==0 else 2 if pow(D%l,(l-1)//2,l)==1 else 0)
                        ct[len(roots)] += 1
                        for r in roots:
                            for i in range(k):
                                m = r + (i+k)*l
                                n = A*m*m+B*m+C
                                assert atom(n,u,v,f) == ((n*v+u)%k==0)
                                if B==C==0:
                                    assert (n*v+u)%k != 0
        print('F', (A,B,C), '0/1/2-roots', *ct)


def three(M,n):
    # Exact ordered x<=y<=z, small n only.
    for x in range(n//M+1,3*n//M+1):
        a,b = M*x-n,n*x
        for y in range(max(x,b//a+1),2*b//a+1):
            if (b*y)%(a*y-b)==0:
                return True
    return False


def panel():
    assert not any(three(8,n) for n in [131,241]); print('8/131,8/241: no triple')
    F4=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if not s.startswith('#')]+[17401609]
    F3=[105,1465,3865,4545,10305,12145,39361,67425]
    for n in [81,121,131,241,1590284203561]+F3+F4:
        hits=[]
        for u in range(1,41):
            for v in range(1,17):
                if gcd(u,v)>1: continue
                for f in range(4*u*v-1,12000,4*u*v):
                    if atom(n,u,v,f): hits.append((f,u,v))
        star=[h for h in hits if h[2]==1]
        ce=[h for h in star if (h[0]+1)%(8*h[1])==0]
        if n in F4: assert not star
        if n in (81,121,4545): assert not hits
        if n==1590284203561: assert not ce
        print(n, 'bounded counts ratio/star/C-even',len(hits),len(star),len(ce),'first',min(hits,default=None))


if __name__=='__main__':
    tests(); panel()
