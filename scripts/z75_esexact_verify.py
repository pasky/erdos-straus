"""Verify a certificate's denominator triples; 'calibrate EXE' also checks completeness
against an independent denominator-divisor census for small primes. Pure stdlib.
"""
from math import isqrt
from pathlib import Path
from subprocess import run, PIPE, DEVNULL
import sys


def certificate(text):
    head, *rows = text.splitlines()
    p, E, F, n1, n2 = map(int, head.split())
    got = [set(), set(), set()]
    for row in rows:
        i, a, b, c, d = map(int, row.split())
        assert i in (1, 2) and 0 < a <= b and min(c, d) > 0
        x, y, z = a*b*d, a*c*d, b*c*d
        if i == 1:
            x *= p
        else:
            y, z = p*y, p*z
        assert 4*x*y*z == p*(y*z+x*z+x*y)
        assert sum(t % p == 0 for t in (x,y,z)) == i
        triple = tuple(sorted((x,y,z)))
        assert triple not in got[i]
        got[i].add(triple)
    assert list(map(len, got[1:])) == [n1, n2]
    return p, got


def denominators(p):
    # With smallest denominator x and A/B=4/p-1/x, (Ay-B)(Az-B)=B^2.
    # A>0, x<=3p/4; and y<=z implies divisor Ay-B<=B.
    got = [set(), set(), set()]
    for x in range(p//4+1, 3*p//4+1):
        A, B = 4*x-p, p*x
        ds = [1]; n = x; q = 2
        while n > 1:
            if q*q > n: q=n
            if n % q == 0:
                e=0
                while n % q == 0:
                    n//=q; e+=1
                ds += [u*q**k for u in ds for k in range(1, 2*e+1)]
            q+=1
        for d in ds:
            for k in (d,d*p,d*p*p):  # x<p so p not already in ds
                if k>B: break
                if (B+k)%A or (B+B*B//k)%A: continue
                y,z=(B+k)//A,(B+B*B//k)//A
                if y>=x: got[sum(t%p==0 for t in (x,y,z))].add((x,y,z))
    return got


if __name__ == '__main__':
    if sys.argv[1]=='calibrate':
        nums = [p for p in range(5, 901, 4) if all(p%q for q in range(2,isqrt(p)+1))]+[10009, 65537, 1000033]
        for j,p in enumerate(nums):
            E,F = [(1,1),(19,27),(41,65)][j%3] if p<10000 else (1,3)
            output=run([sys.argv[2],str(p),str(E),str(F),'emit'],stdout=PIPE,stderr=DEVNULL,text=True,check=True).stdout
            pp,got=certificate(output)
            assert p==pp and got==denominators(p), ('incomplete',p)
        print(f'independent full triple sets agree: {len(nums)} primes, largest {nums[-1]}')
    else:
        for name in sys.argv[1:]:
            p,got=certificate(Path(name).read_text())
            print(f'{p}: verified {len(got[1])} + {len(got[2])} distinct unordered triples')
