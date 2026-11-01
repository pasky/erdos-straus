"""Maximal-order, totally positive search; coefficient height of ALL denominators <=H."""
import json,sys,time,math
import numpy as np
from sympy import primerange, mobius
H=int(sys.argv[1]) if len(sys.argv)>1 else 32
out=[]; start=time.time()
for D in range(2,101):
 if not mobius(D): continue
 # omega^2 = s*omega+t
 s,t=(1,(D-1)//4) if D%4==1 else (0,D)
 els=[(a,b) for a in range(-H,H+1) for b in range(-H,H+1) if 2*a+s*b>0 and a*a+s*a*b-t*b*b>0]
 rows=[]
 for p in primerange(2,1001):
  # x > p/4 in BOTH embeddings, checked without floating point
  es=[(a,b) for a,b in els if 8*a+4*s*b-2*p>0 and (4*a-p)**2+s*(4*a-p)*4*b-t*16*b*b>0]
  if not es: continue
  A,B=np.array(es,dtype=np.int64).T; ii,jj=np.triu_indices(len(es))
  a,b,c,d=A[ii],B[ii],A[jj],B[jj]
  u,v=a*c+t*b*d,a*d+b*c+s*b*d
  e,f=4*u-p*(a+c),4*v-p*(b+d)
  norm=e*e+s*e*f-t*f*f; den=np.where(norm!=0,norm,1)
  za,zb=p*(u*(e+s*f)-t*v*f),p*(v*e-u*f)
  mask=(norm!=0)&(za%den==0)&(zb%den==0)
  aa,bb=za//den,zb//den
  mask &= (abs(aa)<=H)&(abs(bb)<=H)&(2*aa+s*bb>0)&(aa*aa+s*aa*bb-t*bb*bb>0)&((b!=0)|(d!=0)|(bb!=0))
  # canonical triple ordering (x<=y from triu; y<=z lexicographic)
  mask &= (c<aa)|((c==aa)&(d<=bb))
  ix=np.flatnonzero(mask)
  if len(ix):
   unit=(a*a+s*a*b-t*b*b==1)|(c*c+s*c*d-t*d*d==1)|(aa*aa+s*aa*bb-t*bb*bb==1)
   k=int(ix[0]); rows.append(dict(p=int(p),count=len(ix),without_unit=int((mask&~unit).sum()),example=[[int(a[k]),int(b[k])],[int(c[k]),int(d[k])],[int(aa[k]),int(bb[k])]]))
 out.append(dict(D=D,basis_s=s,basis_t=t,elements=len(els),primes_with_solution=len(rows),solutions=sum(x['count'] for x in rows),unit_only_primes=[x['p'] for x in rows if x['without_unit']==0],rows=rows))
 print(D,len(rows),sum(x['count'] for x in rows),flush=True)
json.dump(dict(H=H,pmax=1000,seconds=time.time()-start,fields=out),open(f'data/z52b/pass2/ZF0/Z0272/result_H{H}.json','w'),indent=1)
