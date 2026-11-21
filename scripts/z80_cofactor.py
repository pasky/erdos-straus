"""Exact rooted recursion on nonresidue prime factors, and S-star tests."""
from z80_square_span import fac, divs, jac, primes_to
from collections import Counter
import sys


def good(p,x):
    for A in divs(p+x):
        if (A+1)%x==0 and A+1>=2*x and 2*A<=p+x and jac(A,p)==-1:
            return (x,(A+1)//x,(p+x)//A)
    return None


def basin(p,q,signed):
    Q=[q]; seen={q}
    for x in Q:
        for N in ((p+x,p-x) if signed else (p+x,)):
            for y,e in fac(N):
                if y not in seen and jac(y,p)==-1:
                    assert 1<y<p
                    seen.add(y); Q.append(y)
    return Q


def main(b):
    ps=primes_to(b); cnt=Counter(); first={}; largest={}; shapes={}
    for p in ps:
        if p%840!=1:continue
        cnt['all']+=1
        q=next(l for l in ps if jac(l,p)==-1)
        for signed in (False,True):
            Q=basin(p,q,signed); ok=any(good(p,x) for x in Q); k='pm' if signed else 'plus'
            cnt[k+'_miss']+=not ok
            if not ok:
                if k not in first:first[k]=(p,q,Q[:50],len(Q))
                if len(Q)<=4 and (k,len(Q)) not in shapes:shapes[k,len(Q)]=(p,q,Q)
                largest[k]=p
    print('bounds',b,cnt); print('first',first); print('last',largest); print('small failures',shapes)

if __name__=='__main__': main(int(sys.argv[1]))
