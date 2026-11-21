"""Exact finite word census for the endpoint squareclass restriction in §5."""
import sys
from collections import Counter
from z80_square_span import words,fac,primes_to,jac


def main(B):
    qs=primes_to(B); bins=Counter(); first={}
    for p in qs:
        if p%840!=1: continue
        q=next(l for l in qs if jac(l,p)==-1); sg=q%4
        kernels={}
        for u,t,v in words(p):
            if jac(t*u-1,p)!=-1:continue
            S=frozenset(l for l,e in fac(u*v) if e%2)
            assert S and jac(u*v,p)==-1
            kernels[S]=(u,t,v)
        direct=frozenset([q]) in kernels
        assert not direct or sg==3
        if sg==3 and (p+4)%q==0 and p>10*q:
            assert direct
        P=min(max(S) for S in kernels)
        bins[sg,'all']+=1; bins[sg,'direct']+=direct; bins[sg,'P>q']+=(P>q)
        if P>q and sg not in first:first[sg]=(p,q,P,min((u,t,v) for S,(u,t,v) in kernels.items() if max(S)==P))
    print('bound',B,'bins',sorted(bins.items()),'examples (p,q,P,word)',sorted(first.items()))

if __name__=='__main__':main(int(sys.argv[1]))
