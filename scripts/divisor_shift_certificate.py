"""No-sign paired divisor shifts: finite counterexample and a Dickson seed."""
from math import gcd, prod
from signed_two_shifts import factors, prime, divisors_sq, hits


def box(c, n):
    return {t*pow(n,-1,c)%c for t in divisors_sq(factors(n))}


def finite():
    p=214729
    assert prime(p) and p%840==529
    t=(p-1)//4
    ds=sorted(d for d in divisors_sq(factors(t)) if not t%d)
    assert len(ds)==16
    for d in ds:
        c=4*d-1; k=(p+c)//4; n=(p*c+1)//4
        assert hits(p,c)==(False,False)
        print(d,c,factors(k),factors(n))


def seed():
    ds=[d for d in range(1,211) if 210%d==0]
    q=21599; p=840*q+1
    s={r for d in ds for r,_ in factors(4*d-1)}|{r for r in range(2,50) if prime(r)}
    assert gcd(q*p,prod(s))==1
    forms=[(1,0),(840,1)]
    def record(a,b):
        v=a*q+b
        h=prod(r**e for r,e in factors(v) if r in s)
        forms.append((a,b))
        return h,v//h
    for d in ds:
        c=4*d-1; m=210//d
        for a,extra in [(m,p),(m*c,1)]:
            h,y=record(a,1)
            w={v*pow(y,j,c)*pow(extra,k,c)%c for v in box(c,d*h)
               for j in (-1,0,1) for k in (-1,0,1)}
            assert c-1 not in w
        if m>1:
            record(840,1-m)
    assert len(forms)==49
    assert all(a*e!=b*t for i,(a,b) in enumerate(forms) for t,e in forms[:i])
    print('verified all fixed rows, unit seed and 49 pairwise distinct roots')


if __name__=='__main__':
    finite()
    seed()
