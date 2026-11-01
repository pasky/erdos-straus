from fractions import Fraction as F
from sympy import factorint,legendre_symbol,primerange
import json
n=3861;Delta=n**3+16
fac={int(p):int(e) for p,e in factorint(Delta).items()}
def val(x,p):
 x=F(x);a,b=x.numerator,x.denominator;v=0
 while a%p==0:a//=p;v+=1
 while b%p==0:b//=p;v-=1
 return v,F(a,b)
def hilbert(a,b,p):
 va,u=val(a,p);vb,v=val(b,p)
 def residue(x,m):return x.numerator*pow(x.denominator,-1,m)%m
 if p==2:
  u,v=residue(u,8),residue(v,8)
  return (-1)**(((u-1)*(v-1)//4+va*(v*v-1)//8+vb*(u*u-1)//8)%2)
 u,v=residue(u,p),residue(v,p)
 return int((-1)**((va*vb*(p-1)//2)%2)*int(legendre_symbol(u,p))**(vb%2)*int(legendre_symbol(v,p))**(va%2))
ell=next(p for p,e in fac.items() if e%2)
t=next(a for a in range(2,ell) if legendre_symbol(a,ell)==-1)
ps=sorted({2,3,11,13,*fac,*primerange(3,100)})
rows=[]
for p in ps:
 if p==2:x,y,z=F(2),F(4),F(2*(2*n+1),16-3*n)
 elif p==ell:x,y,z=F(4,t),F(0),F(-t,n)
 elif n%p==0:y=F(1);z=F(n+1,4-n);x=4+n*z
 else:x,y,z=F(4),F(0),F(-1,n)
 assert 4*x*y*z-n*(x*y+y*z+z*x)==4
 assert all(a.denominator%p for a in (x,y,z))
 q=4*y-n;d=q*z-n*y
 rows.append(dict(p=p,point=list(map(str,(x,y,z))),A=hilbert(-q,-d,p),B=hilbert(Delta,d,p)))
assert [r['p'] for r in rows if r['A']==-1]==[2]
assert [r['p'] for r in rows if r['B']==-1]==sorted([2,ell])
out=dict(n=n,k=4,Delta=Delta,factorization=fac,chosen_ramified_prime=ell,nonsquare=t,finite_points=rows,real_invariants=dict(A='1/2',B='0'),positive_real_point=[str(n),str(F(4+n**3,2*n*n)),str(n)])
json.dump(out,open('data/z52b/pass2/ZF0/Z2834/local.json','w'),indent=1)
print(Delta,fac,'chosen',ell,t,'all local tests passed')
