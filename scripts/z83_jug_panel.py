"""Finite certificates for all requested prime controls in the graph domain.
The stabilizer certificate follows z82_wf_hcert.py; exit search is by increasing
negative endpoint, independent of forward BFS. No extrapolation of these rows.
"""
from math import lcm
from pathlib import Path
from z83_jug_dyadic import factors,prime,divisors

def check(p):
    assert p%8==1 and prime(p)
    def neg(x):return pow(x,(p-1)//2,p)==p-1
    def order(x):
        h=p-1
        for l in factors(p-1):
            while h%l==0 and pow(x,h//l,p)==1:h//=l
        return h
    q=next(x for x in range(2,p) if neg(x))
    # z80 A: each integer below q stabilizes C; Fact 2 permits enlargement.
    h=lcm(*(order(y) for y in range(1,q)))
    trace=[('index',(p-1)//h)]
    while h*2<p-1:
        I=(p-1)//h;seen=set()
        for b in range(1,min(p,200000)):
            seen.add(pow(b,h,p))
            if len(seen)==I:break
        assert len(seen)==I
        for y in range(2,min(p,1+(2*p-1)//b,200000)):
            if not neg(y) and pow(y,h,p)!=1:break
        else:raise ValueError('certificate budget exhausted')
        h=lcm(h,order(y));trace.append((b,y,(p-1)//h))
    assert 2*h==p-1
    for x in range(q,p):
        if not neg(x):continue
        for v in sorted(divisors(p+x)):
            if v<2 or v>=p or neg(v):continue
            d=(p+x)//v
            if (d+1)%x or d+1<2*x:continue
            t=(d+1)//x;assert p==t*x*v-x-v
            a,b=t*x-1,t*v-1
            assert a*b==t*p+1 and neg(a+b+2) and neg(a)
            slots=[s for s,i in zip(['t','x','v','a','b'],[t,x,v,a,b]) if i%4==0]
            assert slots
            return q,trace,(x,t,v),','.join(slots)
    raise ValueError('no exit')
def first_anchor(p):
    for k in range(7,2*p+1,8):
        x=(p+k)//4
        f=factors(x)
        for l in list(q for q in f if q!=2) or [1]:
            for j in range(-f[2],f[2]+1):
                for i in range(-f.get(l,0),f.get(l,0)+1):
                    for e in [0,1]:
                        # For e=-1 negate all exponents instead.
                        if pow(p,e,k)*pow(2,j,k)*pow(l,i,k)%k!=k-1:continue
                        u=p**e*2**max(0,j)*l**max(0,i);v=2**max(0,-j)*l**max(0,-i)
                        assert (u+v)%k==0 and p*x%(u*v)==0
                        y=(p*x//u)*((u+v)//k);z=(p*x//v)*((u+v)//k)
                        assert 4*x*y*z==p*(y*z+x*z+x*y)
                        return k,l,i,j,e
    raise ValueError('no one-anchor hit')

if __name__=='__main__':
    hard=[2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929]
    star=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and s[0].isdigit()]
    print('p q index_trace (least_negative_x,t,least_v_at_x) 4-slots (least_even_anchor_k,l,i,j,e)')
    for p in star+hard+[17,241,1590284203561,6955940568721]:print(p,*check(p),first_anchor(p))
