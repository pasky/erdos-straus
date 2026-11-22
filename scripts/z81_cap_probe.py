"""Exact finite local checks for the inverse-carrier and fixed-root packets. No imports beyond stdlib."""
from fractions import Fraction
from math import gcd, lcm, isqrt, prod
from pathlib import Path
from collections import Counter


def factors(n):
    f = {}; j = 2
    while j*j <= n:
        while n % j == 0:
            f[j] = f.get(j,0)+1; n //= j
        j = 3 if j == 2 else j+2
    if n>1: f[n]=1
    return f


def divisors(f):
    a = [1]
    for q,c in f.items(): a = [d*q**j for d in a for j in range(c+1)]
    return sorted(a)


def prime(n): return n>=2 and all(n%j for j in range(2,isqrt(n)+1))


def packet(n,m,d,r):
    k=(n+m)//4
    assert 4*k==n+m and (k+d)%m==0 and gcd(n,m)==1
    a=(k+d)//m; y=n*a; z=Fraction(n*k*a,d)
    assert z>0 and Fraction(1,k)+Fraction(1,y)+1/z==Fraction(4,n)
    assert z.denominator==r*r and gcd(2*n,r)==1
    return k,y,z


def fixed_root(n):
    # d = 9 K^2. Return actual m, not a boolean norm proxy.
    if n%12 != 1: return None
    for m in divisors(factors(9*n+4)):
        if m%12!=11: continue
        k=(m+n)//4
        x,y,z=packet(n,m,9*k*k,3); assert y%3==0
        return m
    return None


def integral_fixed_x(p,m,k):
    # Full hyperbola, including delta_p = +/-1, not just Type II.
    f=factors(p*k)
    return next((d for d in divisors({q:2*b for q,b in f.items()}) if (d+p*k)%m==0),None)


def find_block():
    found=[]
    for p in range(841,2000000,840):
        if not prime(p): continue
        for m in divisors(factors(9*p+4)):
            if m%12!=11 or m>=2*p: continue
            k=(p+m)//4
            if integral_fixed_x(p,m,k) is None:
                packet(p,m,9*k*k,3)
                found.append((p,m,k,factors(k)))
                if len(found)==5: return found
    return found


def inv_examples():
    cnt=Counter(); worked=None
    pool=[t for t in range(7,200,4) if prime(t)]
    for s in range(17,110,4):
        if not prime(s): continue
        lam=s*s-s+1
        ts=[t for t in pool if pow(s%t,(t-1)//2,t)==t-1 and lam%t!=0 and t!=s]
        # one representative per residue; real proof uses Fourier inversion
        # on all subsets, not the greedy order or these tiny prime lists.
        dp={1:()}
        for t in ts:
            for a,ls in list(dp.items()): dp.setdefault((a*t)%s,ls+(t,))
        for p in range(17,4200,8):
            if not prime(p) or pow(p%s,(s-1)//2,s)!=s-1 or (-p)%s not in dp: continue
            ls=dp[(-p)%s]; m0=prod(ls); assert len(ls)%2 and m0%4==3
            lift=(p+m0)%(s*s)==0; m=m0*lam if lift else m0
            h=lcm(3,*[(t-1)//2 for t in ls]); k=(p+m)//4
            assert k%s==0 and k%(s*s)!=0 and pow(s,h,m)==m-1
            # Reconstruct even enormous-h packets via modular identities;
            # also reconstruct the reduced Fraction at small h.
            cnt['modular']+=1; cnt['lift_used']+=lift
            if h<=200:
                _,y,_=packet(p,m,k*s**h,s**((h-1)//2)); assert y%s==0
                cnt['fraction']+=1
            if lift and (worked is None or h<worked[-1]): worked=(p,s,ls,m0,lam,h)
    return sorted(cnt.items()),worked


def main():
    print('fixed-x obstruction on 1 mod 840 (p,m,K,factors):',find_block())
    print('inverse packets:',inv_examples())
    zeros=[int(t) for t in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if t and not t.startswith('#')]
    screens={'odd square':[9,25,49,121,169,361,841,1681], 'F2':[11,17,131,241,1590284203561,6955940568721],
             'F3':[105,1465,3865,4545,10305,12145,39361,67425], 'F4':zeros+[17401609]}
    for name,ns in screens.items(): print(name,[(n,fixed_root(n) if n%12==1 else 'out') for n in ns])

if __name__=='__main__': main()
