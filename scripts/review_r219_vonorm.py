"""R219: from-scratch check behind s4_selling_voronoi_wall Lemma S.
(1) identity Q_w = (x1-x2)^2+(x2-x3)^2+(v-1)x1^2+(t-2)x2^2+(u-1)x3^2 (symbolic, via sympy-free polynomial coefficients);
(2) lattice-invariant content: the 7 vonorms (minimal norms in the 7 nonzero cosets of L/2L, brute force over a box,
    no superbase used) equal the norms of the 0/1 superbase sums predicted by the conorms {1,1,0,v-1,t-2,u-1};
    hence the conorm multiset (linear in the vonorm function, up to GL3(F2)) is a lattice invariant.
(3) the obtuse superbase is non-unique when a conorm vanishes: count distinct conorm *labellings* is not checked."""
import random, itertools
random.seed(219)
def Q(w,x):
    t,u,v=w; a,b,c=x; return v*a*a+t*b*b+u*c*c-2*a*b-2*b*c
bad1=bad2=0; R=4
for trial in range(400):
    t=random.randint(2,30); u=random.randint(1,30); v=random.randint(1,30); w=(t,u,v)
    for x in itertools.product(range(-2,3),repeat=3):
        a,b,c=x
        if Q(w,x)!=(a-b)**2+(b-c)**2+(v-1)*a*a+(t-2)*b*b+(u-1)*c*c: bad1+=1
    # superbase e0=-(e1+e2+e3); conorms p01=v-1,p02=t-2,p03=u-1,p12=1,p23=1,p13=0
    p={(0,1):v-1,(0,2):t-2,(0,3):u-1,(1,2):1,(2,3):1,(1,3):0}
    P=lambda i,j:p[(min(i,j),max(i,j))]
    pred={}
    for i in (1,2,3): pred[tuple(1 if k==i else 0 for k in (1,2,3))]=sum(P(i,j) for j in range(4) if j!=i)
    for i,j in ((1,2),(1,3),(2,3)):
        k=[m for m in (1,2,3) if m not in (i,j)][0]
        pred[tuple(1 if m in (i,j) else 0 for m in (1,2,3))]=P(i,0)+P(i,k)+P(j,0)+P(j,k)
    pred[(1,1,1)]=sum(P(i,0) for i in (1,2,3))
    for cls,val in pred.items():
        m=min(Q(w,x) for x in itertools.product(range(-R,R+1),repeat=3) if all((x[k]-cls[k])%2==0 for k in range(3)))
        if m!=val: bad2+=1
print("identity failures",bad1,"; vonorm (coset-minimum) mismatches",bad2,"over 400 random positive words t>=2")
