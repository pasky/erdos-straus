"""Build and check the isolated all-slot word and its two negative prime successors."""
from math import gcd, isqrt
from z80_square_span import jac,divs
from z80_cofactor import basin

def forms(r):
    assert r%2
    return (r,186*r-17,(11*r-1)//6,(31*r-1)//2,527*r-48)

def prime(n):
    return n>=2 and all(n%a for a in range(2,isqrt(n)+1))


def main():
    M=9*140*17*11*13
    r0=next(r for r in range(1,M,2) if (186*r-18)%(840*11*13)==0 and r%17==5 and r%9==2)
    base=forms(r0); step=tuple(b-a for a,b in zip(base,forms(r0+M)))
    print('r=',r0,'+',M,'j; forms (constant, slope)',list(zip(base,step)))
    for a,b in zip(base,step): assert gcd(a,b)==1
    for l in (2,3,5): assert any(all((a+b*k)%l for a,b in zip(base,step)) for k in range(l))
    assert [v for v in divs(1116) if v%11==10]==[186]
    assert not any(v%17==5 for v in divs(186)) and [v for v in divs(186) if v%17==1]==[1]
    assert not any(v%17==16 for v in divs(6)) and not any(v%11==10 for v in divs(12))
    for j in range(200000):
        r=r0+M*j
        if not all(prime(x) for x in forms(r)):continue
        _,p,s,l,k=forms(r)
        assert 17==next(x for x in range(2,18) if jac(x,p)==-1) and jac(r,p)==-1
        Q=basin(p,17,False)
        assert set(Q)=={17,r}
        print('instance j,r,p,S,L,K:',j,r,p,s,l,k,'prime closure',Q)
        for x in (11,17,r):
            N=p+x; O=[]
            for v in divs(N):
                if (p+x+v)%(x*v)==0 and min(v,(p+x+v)//(x*v))>=2: O.append((v,(p+x+v)//(x*v)))
            if x==r: mid=[(u,v) for u in range(2,187) for v in range(2,187//u+1) if u*x*v-u-v==p]
            else: mid=[((d+1)//x,((x*p+1)//d+1)//x) for d in divs(x*p+1) if d%x==x-1 and d+1>=2*x and (x*p+1)//d+1>=2*x]
            assert set(O)==({(r,11)} if x==17 else {(17,11)} if x==r else set())
            assert set(mid)==({(r,17),(17,r)} if x==11 else set())
            print('at',x, 'outer(v,t)',O,'middle(u,v)',mid)
        return
    raise ValueError('no instance in search')

if __name__=='__main__':main()
