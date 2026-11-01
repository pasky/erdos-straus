# Z1854: one-parameter form R(p)=#{m≡3(4): r=(-p mod m)≠0, r | (m+1)/4}. Check: on the arc (p/q, p/(q-1)] r = qm-p,
# and every win on arc q has B = q (u = r, C = (m+1)/(4u)), i.e. the arcs are exactly the B-lines of the pair form.
from collections import Counter
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
bad=0; tot=0
for p in [q for q in range(5,3000) if q%4==1 and isprime(q)]:
    for m in range(3,p+2,4):
        r=(-p)%m
        if r and ((m+1)//4)%r==0:
            q=(p+r)//m; assert (p+r)%m==0
            u=r; C=(m+1)//(4*u); B=q
            tot+=1
            if 4*u*B*C-u-B!=p: bad+=1
print("wins",tot,"mismatches",bad)
# hard p: wins per arc for 409 and neighbours
for p in [389,401,409,421,433]:
    arcs=Counter()
    for m in range(3,p+2,4):
        r=(-p)%m
        if r and ((m+1)//4)%r==0: arcs[(p+r)//m]+=1
    print(p, "R=",sum(arcs.values()), "wins by arc B:",dict(sorted(arcs.items())))
