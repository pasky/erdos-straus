"""Exact finite replay of the mixed-composite-input and mixed-carrier valuation checks."""
from fractions import Fraction as F
from math import gcd, isqrt
from itertools import permutations
from collections import Counter


def squarefree(s):
    return all(s % (p*p) for p in range(2,isqrt(s)+1))


def run():
    cases = Counter()
    examples = {}
    for u,v,w in permutations([1,3,5,7,11,15,21],3):
        if max(gcd(u,v),gcd(u,w),gcd(v,w))!=1:
            continue
        D=u*v*v*w**4
        for j in (1,3,9,11):
            A=j*u*v*w
            f=4*A-1
            for s in range(4*D//f+1,4*D//f+181):
                n=f*s-4*D
                if n<=1:
                    continue
                x=(n+s)//4
                y=n*A
                z=F(n*x*A,D)
                assert 4*x==n+s and F(1,x)+F(1,y)+1/z==F(4,n)
                root=isqrt(z.denominator)
                assert root*root==z.denominator and squarefree(root) and root%2==1
                assert gcd(n,root)==1 and y%root==0 and w%root==0
                cases['triples']+=1
                if root==w and w in (15,21):
                    cases['two_carriers']+=1
                    examples.setdefault('two_carriers',(n,f,u,v,w,root))
                if gcd(n,D)>1:
                    cases['nonunit_at_D']+=1
                    if root>1:
                        cases['mixed_nonunit_and_overflow']+=1
                        examples.setdefault('mixed_nonunit_and_overflow',(n,f,u,v,w,root))
    assert cases['two_carriers'] and cases['mixed_nonunit_and_overflow']
    print('exact integer inputs from congruence and coprimality check:',dict(sorted(cases.items())))
    print('examples (n,f,u,v,w,root):',dict(sorted(examples.items())))


if __name__=='__main__':
    run()
