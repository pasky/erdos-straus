"""R285: edge totals quoted in LOWER_TAIL_ASTRA §6 (odd n<=2000; odd squares 9..999^2), by the O(n) residue-parent scan
for n<=2000 and by direct small-u divisor scan for the squares (from scratch)."""
from sympy import divisors
def edges_scan(n):
    E=[]
    for v in range(2,n+3):
        r=(-n)%v
        if r and (n+v+r)%(v*r)==0: E.append((r,v))
    return E
def edges_div(n):
    E=[]; u=1
    while (u-1)*u<=n+1:
        E+=[(u,v) for v in divisors(n+u) if u<v<=n+2 and (n+u+v)%(u*v)==0]; u+=1
    return E
tot=0
for n in range(3,2001,2):
    a=edges_scan(n); b=edges_div(n); assert sorted(a)==sorted(b),n; tot+=len(a)
print("odd n<=2000 edges:",tot)
print("odd squares 9..999^2 edges:",sum(len(edges_div(m*m)) for m in range(3,1000,2)))
