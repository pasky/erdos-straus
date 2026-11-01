"""Small modular-curve special 0-cycles in characteristics 3,7.
Exact maximal orders O=Z[(−1+i)/2,j], i²=−p,j²=−1,ij=−ji.
GK/Kitaoka local factor is read from Kudla Bourbaki (5.3)–(5.5).
"""
import math,json
from fractions import Fraction
X=1000
rows=[];totals=[]
for p in (3,7):
    units=sum(a*a-a*b+(p+1)//4*b*b+c*c-c*d+(p+1)//4*d*d==1
              for a in range(-3,4) for b in range(-3,4) for c in range(-3,4) for d in range(-3,4))
    vectors=[[] for _ in range(X+1)]
    R=math.isqrt(4*X//p)+1
    for x in range(-R,R+1,2) if R%2==0 else range(-R+1,R+1,2):
        for z in range(-R,R+1):
            rem=4*X-p*x*x-p*z*z
            if rem<0:continue
            Y=math.isqrt(rem)
            for y in range(-Y,Y+1):
                if (y-z)%2:continue
                norm=(p*x*x+y*y+p*z*z)//4
                if norm: vectors[norm].append((x,y,z))
    U=vectors[1]
    support=missing=certindices=0;sumdeg=Fraction(0);sumcert=0
    for m in range(1,X+1):
        discr=4*m-1
        if discr%p:continue
        e=discr//p
        reps=sum(p*u[0]*v[0]+u[1]*v[1]+p*u[2]*v[2]==-2 for u in U for v in vectors[m])
        vp=0;tmp=discr
        while tmp%p==0:vp+=1;tmp//=p
        unord=ordered=0;factors=[]
        for a in range(1,math.isqrt(m)+1):
            if m%a==0:
                b=m//a
                if (a+b)%e==0:
                    unord+=1;ordered+=1 if a==b else 2;factors.append([a,b,(a+b)//e,1])
        if reps:assert vp%2==1
        delta=Fraction(vp+1,2) if reps else None
        degree=Fraction(reps,units)*delta if reps else Fraction(0)
        support+=reps>0;missing+=bool(reps and not unord);certindices+=unord>0
        sumdeg+=degree;sumcert+=unord
        if (p,m) in [(3,1),(3,4),(3,7),(3,10),(3,19),(7,2),(7,9),(7,16)]:
            rows.append(dict(p=p,m=m,T=[[1,'-1/2'],['-1/2',m]],e=e,aut_E=units,norm1_vectors=len(U),ordered_endomorphism_pairs=reps,stack_mass=str(Fraction(reps,units)),vp_det=vp,GK_length=str(delta),normalized_Kitaoka_derivative=str(delta),degree_div_logp=str(degree),certificate_unordered=unord,certificate_ordered=ordered,tuples=factors))
    totals.append(dict(p=p,mmax=X,indices_with_p_div_det=sum((4*m-1)%p==0 for m in range(1,X+1)),cycle_support=support,positive_cycle_no_certificate=missing,certificate_indices=certindices,sum_degree_div_logp=str(sumdeg),sum_unordered_certificates=sumcert))
print(json.dumps(dict(examples=rows,totals=totals),indent=2))
