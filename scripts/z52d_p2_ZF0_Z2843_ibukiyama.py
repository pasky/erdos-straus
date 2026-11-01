"""Exact Lambda_(d,m) embeddings into explicitly checked Ibukiyama O(q,r).
Source: Ibukiyama 1982 pp181-184, especially Lemma1.4's displayed basis.
Memory bounded: norm shells enumerated one at a time; no Cartesian arrays.
"""
import math,json,time
from collections import defaultdict
from sympy import Matrix,Rational,primerange
from bsC_common import typeI_all
from z52d_p2_ZF0_Z2806_words import chi,save

def product(x,y,p,q):
 a,b,c,d=x;e,f,g,h=y
 return Matrix([a*e-p*b*f-q*c*g-p*q*d*h,a*f+b*e+q*(c*h-d*g),a*g+c*e+p*(d*f-b*h),a*h+d*e+b*g-c*f])

def basis_check(p,q,r):
 B=Matrix([[1,Rational(1,2),0,0],[0,0,Rational(1,2),0],[0,Rational(1,2),0,Rational(r,q)],[0,0,Rational(1,2),Rational(1,q)]])
 inv=B.inv();G=Matrix(4,4,lambda i,j:2*product(B[:,i],B[:,j],p,q)[0])
 assert G.det()==-p*p
 for i in range(4):
  for j in range(4):assert all(x.q==1 for x in inv*product(B[:,i],B[:,j],p,q))
 return B

def shell(n,p,q,r):
 # scaled pure coordinates (C,B,K)/(2q) in basis alpha,beta,alpha*beta.
 out=[];cmax=math.isqrt(4*n//p)
 for c in range(-cmax,cmax+1):
  rem0=4*q*n-p*q*c*c
  if rem0<0:continue
  kmax=math.isqrt(rem0//p)
  lo=-kmax+((-kmax-q*c)%2)
  for K in range(lo,kmax+1,2):
   rem=rem0-p*K*K;B=math.isqrt(rem)
   if B*B!=rem:continue
   d=(K-q*c)//2
   for BB in ((B,-B) if B else (0,)):
    if (BB-2*r*d)%(2*q)==0:out.append((q*c,BB,K))
 return out

def pair(us,vs,p,q):
 for u in us:
  for v in vs:
   if p*u[0]*v[0]+q*u[1]*v[1]+p*q*u[2]*v[2]==-2*q*q:return u,v
 return None

def coords(x,q,r):
 C,B,K=x;c=C//q;d=(K-C)//2;h=(B-2*r*d)//(2*q)
 assert C==q*c and K==q*c+2*d and B==2*q*h+2*r*d
 return (-h,2*h,c,d)

start=time.monotonic();tuples=typeI_all(199);rows=[];prime_rows=[];orders=tests=hits=0;maxshell=0
for p in primerange(3,200):
 certs=tuples[p];targets=defaultdict(list)
 for a,b,c,d,e in certs:targets[(d,a*b,e)].append((a,b,c))
 qs=[q for q in primerange(3,1000) if q%8==3 and q!=p and chi(-q,p)==-1]
 covered=set();min_e={};qrows=[]
 for q in qs:
  r=next(x for x in range(q) if (x*x+p)%q==0)
  Bmat=basis_check(p,q,r);orders+=1;ucache={};qhit=0;emin=None
  for d,m,e in targets:
   tests+=1
   if d not in ucache:ucache[d]=shell(d,p,q,r)
   if not ucache[d]:continue
   vs=shell(m,p,q,r);maxshell=max(maxshell,len(vs));pv=pair(ucache[d],vs,p,q)
   if pv is None:continue
   hits+=1;qhit+=1;covered.add((d,m,e));emin=e if emin is None else min(emin,e)
   u,v=pv;uc,vc=coords(u,q,r),coords(v,q,r)
   ux=Bmat*Matrix(uc);vx=Bmat*Matrix(vc)
   assert product(ux,ux,p,q)==Matrix([-d,0,0,0])
   assert product(vx,vx,p,q)==Matrix([-m,0,0,0])
   assert product(ux,vx,p,q)+product(vx,ux,p,q)==Matrix([1,0,0,0])
   # Verify index e directly in this maximal-order basis.
   J=Bmat.inv()*Matrix.hstack(Matrix([1,0,0,0]),ux,vx,product(ux,vx,p,q))
   assert all(z.q==1 for z in J) and abs(J.det())==e
   rows.append({'p':p,'q':q,'r':r,'d':d,'m':m,'e':e,'certificate_ab_c':targets[(d,m,e)][0],'u_basis':uc,'v_basis':vc})
  qrows.append({'q':q,'embedded_targets':qhit,'least_embedded_e':emin})
 prime_rows.append({'p':p,'certificate_tuples':len(certs),'distinct_orders':len(targets),'covered_orders':len(covered),'least_certificate_e':min(e for d,m,e in targets),'least_covered_e':min((e for d,m,e in covered),default=None),'uncovered_targets':[list(x) for x in sorted(set(targets)-covered)],'q_tests':qrows})
 print(p,len(targets),len(covered),flush=True)
out={'p_range':'3<=p<200','q_bound':1000,'basis':'1,(1+beta)/2,alpha(1+beta)/2,(r+alpha)beta/q; alpha^2=-p,beta^2=-q','tested_maximal_orders':orders,'embedding_tests':tests,'successful_embeddings':hits,'target_orders':sum(r['distinct_orders'] for r in prime_rows),'covered_target_orders':sum(r['covered_orders'] for r in prime_rows),'primes_with_embedding':sum(r['covered_orders']>0 for r in prime_rows),'primes_preserving_min_level':sum(r['least_certificate_e']==r['least_covered_e'] for r in prime_rows),'max_norm_shell_size':maxshell,'elapsed_seconds':time.monotonic()-start,'prime_rows':prime_rows,'witnesses':rows}
save('Z2843',out);print(json.dumps({k:v for k,v in out.items() if k not in ('prime_rows','witnesses')},indent=2))
