"""Small independent checks for DISPROOF_DEEP. No zero by truncated search."""
from math import isqrt
from collections import Counter


def direct(n,c):
    # abd <= n/2; fix a,d and solve for b. Exhaustive with a<=b.
    hits=set()
    for a in range(1,isqrt(n//2)+1):
        for d in range(1,n//(2*a*a)+1):
            b,r=divmod(a+n*c,4*a*c*d-1)
            if r==0 and a<=b:
                hits.add((a,b,d))
    return hits


def by_e(n,c):
    # Independently: ce=a+b and n+e=4abd. Sort a<=b. Since
    # ce<=2b, acde<=2abd<=n, so e<=n/c and ad<=n/(ce).
    hits=set()
    for e in range((-n-1)%4+1,n//c+1,4):
        for a in range(1,min(c*e//2,n//(c*e))+1):
            b=c*e-a
            d,r=divmod(n+e,4*a*b)
            if r==0:
                hits.add((a,b,d))
    return hits


def reduced(c,a,d,e,r):
    while True:
        assert c*c+4*d*a*a+e+r==4*a*d*e*c
        cp=4*a*d*e-c; ap=c*e-a
        assert cp>0 and ap>0 and cp%2==c%2
        if cp<c: c=cp
        elif ap<a: a=ap
        else: return c,a


def main():
    for r in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,63,65]:
        seeds=Counter(); ns=0
        for c in range(2,202,2):
            n=c*c+r
            hits=by_e(n,c)
            assert direct(n,c)==hits
            ns+=bool(hits)
            for a,b,d in hits:
                e=(a+b)//c; z,w=reduced(c,a,d,e,r)
                seeds[z,w,d,e]+=1
            if r==1: assert not hits
        print('shift',r,'even heights with points to 200',ns,'seeds (c,a,d,e)',sorted(seeds))
    for c in range(2,202,2):
        n=c*c-1; assert (c//2,c//2,1) in by_e(n,c)
    for n,k,q,L in [(4545,4,11,13),(131,8,7,5),(241,8,7,5)]:
        assert pow(-n,(q-1)//2,q)==1 and q%k==k-1 and (n+1)%q
        assert L%4==1 and pow(q,(L-1)//2,L)==L-1
        print('square patch n k q L',n,k,q,L)

if __name__=='__main__': main()
