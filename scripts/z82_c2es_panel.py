"""Exact height-limited enumerations; no external packages. Run from repo root."""
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path


def divisors(n):
    small = [d for d in range(1, isqrt(n)+1) if n % d == 0]
    return small + [n//d for d in reversed(small) if d*d != n]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def check(n, M, triple):
    assert min(triple) > 0 and sum(1/Q(x) for x in triple) == Q(M,n)


def inverse(n, M, S):
    # Odd carrier, possibly composite. m coprime to n: genuine primitive window.
    # For fixed s, m odd proper divisor of s+1, so m<s. At most one m in class.
    rows=[]
    for s in range(3,S+1,2):
        m=(-n)%s
        if m%2 != 1 or (s+1)%m or (n+m)%(M*s) or gcd(m,n)>1: continue
        k=(n+m)//M
        y=n*k*((s+1)//m)
        check(n,M,(k,y,y//s))
        rows.append((s,m,prime(s) and s%4==1, k%(s*s)!=0))
    return rows


def half_window(n, M, S=19, H=64):
    # Test signed multipliers u/v with u=a*s^2, v=b, gcd(a*s,b)=1.
    # K multiple of abs multiplier's support base a*b*s, s divides K exactly once.
    for s in range(3,S+1,2):
        if n%s==0 or not prime(s): continue
        for a in range(1,H+1):
            if a%s==0: continue
            for b in range(1,H+1):
                if gcd(a*s,b)>1: continue
                w=M*a*b*s
                for m in divisors(a*s*s+b):
                    if (n+m)%w or gcd(m,n)>1: continue
                    k=(n+m)//M
                    if k%(s*s)==0: continue
                    q=Q(k*(a*s*s+b),m*b)
                    y=n*q; z=y*b/(a*s*s)
                    check(n,M,(k,y,z))
                    assert y.denominator==1 and y.numerator%s==0 and z.denominator==s
                    return s,a,b,m
    return None


def small_es(M,n):
    for x in range(n//M+1,3*n//M+1):
        f=Q(M,n)-1/Q(x)
        j,g=f.numerator,f.denominator
        for d in divisors(g*g):
            if (g+d)%j or (g+g*g//d)%j: continue
            triple=x,(g+d)//j,(g+g*g//d)//j
            check(n,M,triple)
            return triple
    return None


def panel():
    z=[int(t) for t in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if t and not t.startswith('#')]
    groups={'F1':[9,25,49,121,169,289,361,841], 'F2':[11,17,131,241,1590284203561,6955940568721],
            'F3':[105,1465,3865,4545,10305,12145,39361,67425],
            'F4':z+[17401609,2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929,3189177846574333650961]}
    print('group n M s-limit: #h1-odd #h1-prime1mod4 #also-simple-lift ; first(s,m) ; first linked half (s,a,b,m)')
    for group,ns in groups.items():
        for n in ns:
            M=8 if group=='F2' else 4
            S=min(100000,(2*n+1)//(2*M-1))
            rows=inverse(n,M,S)
            half=half_window(n,M)
            if group=='F1': assert not rows and not half
            if group=='F3' and n==4545: assert not rows
            if M==8 and n<=241: assert not small_es(8,n) and not rows
            print(group,n,M,S,len(rows),sum(t[2] for t in rows),sum(t[2] and t[3] for t in rows),rows[0][:2] if rows else '-',half or '-')


if __name__=='__main__': panel()
