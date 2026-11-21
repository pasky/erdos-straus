"""Exact LP: R2 with the M-congruence diagonal, and the direct EPC comparison."""
from fractions import Fraction as F
from itertools import product


def strengthened(kappa, lam):
    z=(8-2*lam)/(3+kappa+lam); theta=(8-z)/(25-3*z)
    names=('shift-diagonal','B-tails','bin-diagonal','bin-correction','kernel','reciprocal','residual')
    worst={}
    print('theta',theta,'columns',*names)
    for mu in (F(0),F(1,3)):
        t=theta+(1-3*theta)*mu
        for a,b,g in dict.fromkeys(((t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t))):
            r=b-t; j=2*(r+g-t); v=z*r; p=2*r
            l=p+g-b  # base D=n/M², b=log_D(V/M)
            assert min(l,r,j,v,p-v)>=0 and g>j+p and 1+mu>2*g
            assert b-p<=t and b-g<=t and 0<=g-j and g+p+g-j==2*t
            local={}
            for x,e,i in product((F(0),j),(F(0),l),(F(0),v)):
                y=1+mu+e+x-3*g; u=p+i; f=y+2*x+u-g; s=2*(x+p-g)
                assert f+2*s<0
                costs=[-v,i-v-f/2,i-v-(y+e)/2,i-v+(f+s-y-e)/2,
                       i-v+(1+kappa)*f/2-y+(lam-kappa-1)*u/2,
                       i-v+f/4-y,i-v+f/2+s/4-y]
                for num,cost in enumerate(costs):
                    slack=2*(g-j)-(2*(x-j+e-l)+g+y+cost)
                    worst[num]=min(slack,worst.get(num,slack))
                    local[num]=min(slack,local.get(num,slack))
            print('mu',mu,'vertex',a,b,g,'min squared slacks',*local.values())
    assert min(worst.values())>=0
    print('theta',theta,'M exponent',1-5*theta,'min squared slacks',*worst.values())


def conditional_lp():
    t=F(4,13)
    for a,b,g in ((t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t)):
        r=b-t
        assert 2*r+g/2<=t and g>2*r and 1>2*g
        assert 2*r+g-b>=0 and b-2*r<=t and b-g<=t
        print('EPC vertex',a,b,g,'slack',t-2*r-g/2)


if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 60 uv run --offline --no-project python scripts/z79_analytic_r3.py')
    for k,l in ((F(1,2),F(1,2)),(F(13,84),F(55,84)),(F(1418,5119),F(2917,5119))):
        strengthened(k,l)
    conditional_lp()
