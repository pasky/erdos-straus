# z58 TRYF2: check Remark 1.2: for n = 1 (4), #hits with u,B >= 2 equals #{d<n: CF(d/n) canonical = [0;a0,1,a2,1,a4] (a4>=2) or [0;a0,1,a2,2], a2 = 2 mod 4}
from math import gcd
def cf(a,b):
    q=[]
    while b: q.append(a//b); a,b=b,a%b
    return q  # canonical: last term >=2 unless length 1
def R_split(n):
    tot=0; u1=0
    u=1
    while 4*u-1-u<=n:
        C=1
        while True:
            d=4*u*C-1
            if d-u>n: break
            if (n+u)%d==0:
                B=(n+u)//d
                tot+=1
                if u==1 or B==1: u1+=1
            C+=1
        u+=1
    return tot,u1
bad=0
for n in range(5,3000,4):
    tot,u1=R_split(n)
    cnt=0
    for d in range(1,n):
        if gcd(d,n)!=1: continue
        q=cf(d,n)  # q[0]=0
        ok=False
        if len(q)==6 and q[2]==1 and q[4]==1 and q[5]>=2 and q[3]%4==2: ok=True
        if len(q)==5 and q[2]==1 and q[4]==2 and q[3]%4==2: ok=True
        cnt+=ok
    if cnt!=tot-u1: bad+=1; print("MISMATCH",n,tot,u1,cnt)
print("checked n<3000, mismatches:",bad)
