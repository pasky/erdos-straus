"""z77 review: independently re-check every positive row of u7-panel.txt and u7-follow.txt (trial-division primality)."""
from math import isqrt
def isprime(q):
    if q<2 or q%2==0:return q==2
    for i in range(3,isqrt(q)+1,2):
        if q%i==0:return False
    return True
def chk(p,f,c=None):
    r=-p%f; assert f%8==7 and r and (f+1)%r==0
    x,y,z=r,(f+1)//r,(p+r)//f; assert x*y*z-x-z==p and (x*y)%8==0 and min(x,y,z)>=1
    cs=[c] if c else [1,3,5]; assert any(f%c==0 and isprime(f//c) for c in cs),(p,f)
    assert p%8==1 and isprime(p) if p<10**10 else p%8==1
rows=[tuple(map(int,l.split())) for l in open('data/z77/proth/u7-panel.txt')]
pos=[(p,f) for p,f in rows if f];[chk(p,f) for p,f in pos]
print('panel rows',len(rows),'positive verified',len(pos),'zeros',[p for p,f in rows if not f])
for l in open('data/z77/proth/u7-follow.txt'):
    p,x,f,c=map(int,l.split());chk(p,f,c);print('follow ok',p,f,c,f//c)
