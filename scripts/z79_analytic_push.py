"""Exact vertex replay for the two-difference bound; single-input falsifiers."""
from fractions import Fraction as F
from math import isqrt


def lp():
    theta = F(13, 41)
    for mu in (F(0), F(1, 3)):
        t = theta + (1-3*theta)*mu
        for a,b,g in dict.fromkeys(((t,1-2*t,t), (t,t,1-2*t), (1-2*t,t,t))):
            r = b-t
            j = 2*(r+g-t)
            d = 1+mu-b+2*r+j-2*g
            costs = ((g+d+j+r)/3, (4*g+d-2*j-2*r)/6,
                     (g+d)/2-r, (3*g+d-2*j-4*r)/4)
            assert g-j >= max(*costs, 0)
            assert g+2*r+(g-j) == 2*t
            assert min(r,j,mu+2*r+g-b,d)>=0
            assert b-mu-2*r<=t and b-mu-g<=t
            assert g>j+2*r and 1>2*g
            print('mu',mu,'a,b,g',a,b,g,'slacks',*(g-j-x for x in costs))
    print('saving',F(46,145)-theta,'over 3/10 by',theta-F(3,10))


def has_word(n, M):
    # Enumerate a<=b using a^2 M <= n+2a at d>=1.
    for a in range(1,(1+isqrt(1+M*n))//M+1):
        # Partition (Mad-1)b=n+a into d<=b and b<d; loop on the smaller variable.
        s=n+a
        d=1
        while (M*a*d-1)*max(d,a)<=s:
            if M*a*d>1 and s%(M*a*d-1)==0:
                return True
            d+=1
        b=a
        while (M*a*(b+1)-1)*b <= s:  # necessary if d>b
            if s%b==0 and (1+s//b)%(M*a)==0:
                return True
            b+=1
    return False


def has_u7(n):
    for f in range(7,2*n+2,8):
        r=(-n)%f
        if r and (f+1)%r==0:
            return True
    return False


if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 180 uv run --offline --no-project python scripts/z79_analytic_push.py')
    lp()
    zeros=(409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281)
    for group, inputs, m in [('F1',tuple(i*i for i in range(3,80,2)),4),
                             ('F2',(131,241),8), ('F4',zeros+(17401609,),4)]:
        for n in inputs:
            assert not has_word(n,m), (m,n)
        print(group, 'direct word-zero checks',len(inputs))
    assert has_word(19,4) and has_word(14,8) and has_u7(17)
    Z7=(105,1465,3865,4545,10305,12145,39361,67425)
    assert not any(map(has_u7,Z7)) and not has_word(4545,4)
    print('F3 direct U7 misses:',*Z7)
