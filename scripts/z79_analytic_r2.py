"""Exact polytope replay for two Poisson transforms and pooled product bins."""
from fractions import Fraction as F
from itertools import product


def verify(kappa, lam):
    z=(8-2*lam)/(3+kappa+lam)
    theta=(8-z)/(25-3*z)
    print('pair',kappa,lam,'k exponent/r',z,'theta',theta)
    worst={}
    for mu in (F(0), F(1,3)):
        t=theta+(1-3*theta)*mu
        for a,b,g in dict.fromkeys(((t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t))):
            r=b-t; j=2*(r+g-t); v=z*r; p=2*r
            length=mu+p+g-b
            assert min(length,r,j,v,p-v)>=0 and g>j+p and 1>2*g
            assert b-mu-p<=t and b-mu-g<=t and 0<=g-j
            assert g+p+g-j==2*t
            local={}
            for x,e,i in product((F(0),j), (F(0),length), (F(0),v)):
                y=1+e+x-3*g
                u=p+i  # log of typical product k(Q+k)
                f=y+2*x+u-g  # second B-process phase size
                s=2*(x+p-g)
                assert f+2*s<0 # second-order remainder in the SECOND critical value
                # J=1+B sigma, V=B/Y, population E V. If J>E V use trivial bound.
                terms={'shift diagonal':-v,'B tails':i-v-f/2,
                       'bin diagonal':i-v-(y+e)/2,
                       'bin correction':i-v+(f+s-y-e)/2,
                       'product kernel':i-v+(1+kappa)*f/2-y+(lam-kappa-1)*u/2,
                       'curvature reciprocal':i-v+f/4-y,
                       'curvature residual':i-v+f/2+s/4-y}
                for name,term in terms.items():
                    # First B-process triangle, followed by signed ell pooling in the second square.
                    slack=2*(g-j)-(2*(x-j+e-length)+g+y+term)
                    local[name]=min(slack,local.get(name,slack))
                    worst[name]=min(slack,worst.get(name,slack))
            print('mu',mu,'vertex',a,b,g,'min squared slacks',*local.values())
    for name, slack in worst.items():
        print(name,slack)
    assert min(worst.values())>=0
    print('saving on 13/41',F(13,41)-theta,'gap to 3/10',theta-F(3,10))


if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 60 uv run --offline --no-project python scripts/z79_analytic_r2.py')
    verify(F(1,2),F(1,2))
    verify(F(13,84),F(55,84))
    verify(F(1418,5119),F(2917,5119))
