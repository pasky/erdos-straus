# Test whether the "profinite point" x in Z^ with x_q = r (q-adic unit, here just r mod q^a matters)
# and x_l = 1 for all l != q lies in the open set U (union of good classes).
# Fixed-d class: d = 3 (4), k | (d+1)/4, class -k mod d.  Fixed-(u,k) class: -u-k mod 4uk.
# x lies in class (a mod m) iff a = 1 mod (m/q^v) and a = r mod q^v (v = v_q(m)), r taken as integer rep.
import sys
from sympy import divisors
q=int(sys.argv[1]); r=int(sys.argv[2]); D=int(sys.argv[3]); UK=int(sys.argv[4])
def vq(m):
    v=0
    while m%q==0: m//=q; v+=1
    return v
def contains(a,m):
    v=vq(m); Q=q**v; mm=m//Q
    return (a-1)%mm==0 and (a-r)%Q==0
hits=[]
for d in range(3,D,4):
    if d%q: continue
    for k in divisors((d+1)//4):
        if contains(-k,d): hits.append(('d',d,k))
for u in range(1,UK):
    for k in range(1,UK):
        if (u*k)%q==0 and contains(-u-k,4*u*k): hits.append(('uk',u,k,4*u*k))
print(len(hits)); print(sorted(hits,key=lambda h:h[-1] if h[0]=='uk' else h[1])[:20])
