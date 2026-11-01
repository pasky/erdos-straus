"""Transcribe Cao–Xu Tables 2.1/3.1/3.2 and independently synthesize exact certificates.
Polynomial range modulo M is an image, NOT universal coverage of a progression.
"""
import json,itertools,math,time
from pathlib import Path
import sympy as s
import numpy as np
out=Path('data/z52b/pass2/ZF0/Z1518'); t=time.time(); x,y,z=s.symbols('x y z',nonnegative=True)
# Wild tuples: xy,x,y,constant. Double-checked against PDF Table 3.1.
wild=[(6,5,5,4),(15,10,7,4),(21,7,10,3),(22,11,7,3),(21,14,17,11),(23,23,19,18),(30,20,13,8),(30,10,29,9),(42,14,13,4),(42,28,5,3),(42,14,19,6),(42,28,41,27),(46,46,7,6),(46,46,15,14),(66,33,19,9),(66,33,41,20),(66,33,43,21),(66,33,65,32),(69,69,10,9),(69,69,11,10),(69,69,34,33),(69,69,56,55),(92,92,74,73),(114,19,113,18),(114,95,37,30),(138,138,17,16),(138,138,43,42),(138,138,67,66),(138,138,89,88),(138,138,91,90),(138,138,109,108),(138,138,113,112),(138,138,137,136)]
tame=['x-y+(4*x+1)*(16*y+3+z*(24*y+5))','(z+1)*(4*x+3)*(24*y+5)-x-y-1','7*x-y+(16*y+8+z*(24*y+13))*(12*x+1)','(z+1)*(12*x+1)*(8*y+7)-x-y-1','(z+1)*(4*x+1)*(24*y+17)-x-y-1','(z+1)*(12*x+5)*(24*y+13)-x-y-1','7*x-y+4+(12*x+7)*(16*y+z*(24*y+1))','(z+1)*(12*x+7)*(8*y+3)-x-y-1','3*x-y+1+(12*x+7)*(16*y+11+z*(24*y+17))','(z+1)*(12*x+11)*(24*y+1)-x-y-1','2*x-y+2*(16*y+7+z*(24*y+11))*(4*x+1)','2*((z+1)*(4*x+3)*(24*y+11)-x-1)-y','2*x-y+2*(16*y+7+z*(24*y+11))*(4*x+3)+1','4*(6*x+1)*(16*y+4+z*(24*y+7))+14*x-y+2','5*y-2*x+2*(8*x+3+z*(12*x+5))*(8*y+3)+1']
polys=[24*x*y+r*(x+y)+(r*r-1)//24 for r in [1,5,7,11,13,17,19,23]]+[a*x*y+b*x+c*y+d for a,b,c,d in wild]+[s.sympify(e,locals={'x':x,'y':y,'z':z}) for e in tame]
records=[]
def integer_valued(poly,vs):
    # Multivariate Newton/binomial coefficients integral iff all values in degree box integral.
    poly=s.Poly(poly,*vs); deg=[poly.degree(v) for v in vs]
    return all(poly.eval(dict(zip(vs,pt))).q==1 for pt in itertools.product(*[range(d+1) for d in deg]))
def nonnegative(poly,vs):return all(c>=0 for c in s.Poly(poly,*vs).coeffs())
def two_term(Q,r,vs):
    const,factors=s.factor_list(Q,*vs); assert const.q==1
    divs=s.divisors(int(const)**2)
    for exps in itertools.product(*[range(2*e+1) for f,e in factors]):
      base=s.prod(f**e for (f,k),e in zip(factors,exps)); other=s.prod(f**(2*k-e) for (f,k),e in zip(factors,exps))
      for c in divs:
        D=c*base; E=(const**2/c)*other
        Y=s.Poly((D+Q)/r,*vs).as_expr(); Z=s.Poly((E+Q)/r,*vs).as_expr()
        if integer_valued(Y,vs) and integer_valued(Z,vs) and nonnegative(Y,vs) and nonnegative(Z,vs):return s.factor(Y),s.factor(Z)
    return None
for i,m in enumerate(polys,1):
    m=s.expand(m); n=24*m+1; vs=(x,y) if i<=41 else (x,y,z)
    rec={'id':i,'table':'2.1' if i<=8 else ('3.1' if i<=41 else '3.2'),'type':'composite' if i<=8 else ('wild' if i<=41 else 'tame'),'m':str(m),'parameters':{'x_min':1 if i==1 else 0,'y_min':1 if i==1 else 0,**({'z_min':0} if i>=42 else {})}}
    if i<=8:
      r=[1,5,7,11,13,17,19,23][i-1]; assert s.expand(n-(24*x+r)*(24*y+r))==0
      rec['certificate']={'factorization':str((24*x+r)*(24*y+r)),'symbolic':True}
    else:
      if i>=42:
        # Type II synthesis from the two linear factors of the z coefficient.
        fac=s.factor_list(s.diff(m,z),x,y)[1]
        if len(fac)==2:
          u,v=[f for f,e in fac]
          aa,bb,cc=s.symbols('aa bb cc'); rem=s.expand(n.subs(z,0)+aa*u+bb*v-cc*u*v)
          # Match the residual bilinear polynomial to a constant multiple of u*v.
          sols=s.solve(s.Poly(rem,x,y).coeffs(),(aa,bb,cc),dict=True)
          for so in sols:
            A=so[aa]*u; B=so[bb]*v; D=s.cancel((n+A+B)/(4*A*B))
            dens=[s.cancel(n*B*D),s.cancel(n*A*D),s.cancel(A*B*D)]
            if all(q.is_polynomial(*vs) and integer_valued(q,vs) and nonnegative(q,vs) and q.subs({x:0,y:0,z:0})>0 for q in dens):
              X,Y,Z=dens;assert s.expand(4*X*Y*Z-n*(X*Y+X*Z+Y*Z))==0
              rec['certificate']={'denominators':[str(s.factor(q)) for q in dens],'symbolic':True,'integrality':'Newton degree-box exact test','positivity':'nonnegative coefficients and positive constant'};break
      # Factor a linear first denominator; wild families select exact k automatically.
      ks=[] if 'certificate' in rec else range(1,40)
      if i<=41:
        a,b,c,d=wild[i-9]; kk=s.Rational(6*b*c,a)-6*d;ks=[kk]
      for k in ks:
        X=s.factor(6*m+k); r=4*k-1
        if r<=0 or not integer_valued(X,vs) or not nonnegative(X,vs):continue
        # Skip irreducible Q: gives only huge constant residue scans, usually no template.
        if len(s.factor_list(X,*vs)[1])<2 and i>=42:continue
        yz=two_term(s.expand(n*X),r,vs)
        if yz:
          Y,Z=yz
          assert s.expand(4*X*Y*Z-n*(X*Y+X*Z+Y*Z))==0
          rec['certificate']={'denominators':[str(X),str(Y),str(Z)],'symbolic':True,'integrality':'Newton degree-box exact test','positivity':'nonnegative coefficients and positive constant'};break
      if 'certificate' not in rec:rec['certificate']={'symbolic':False}
    print(i,rec['certificate']['symbolic'],flush=True);records.append(rec)
    (out/'families.json').write_text(json.dumps(records,indent=2))
# Exact modular polynomial images, memory bounded O(M). For z-affine polynomials,
# each (x,y) gives a coset modulo gcd(z_coefficient,M); no cubic-sized array.
coverage=[]
for M in [840,1680,3360]:
    union=np.zeros(M,dtype=bool); sol=np.zeros(M,dtype=bool); per=[]; yy=np.arange(M,dtype=np.int64)
    for rec,m in zip(records,polys):
      hit=np.zeros(M,dtype=bool)
      if rec['id']<=41:
        fn=s.lambdify((x,y),m,'numpy')
        for xx in range(M):hit[np.asarray(fn(xx,yy)%M,dtype=int)]=True
      else:
        A=s.lambdify((x,y),s.diff(m,z),'numpy');B=s.lambdify((x,y),m.subs(z,0),'numpy')
        for xx in range(M):
          aa=np.broadcast_to(A(xx,yy),(M,)).astype(np.int64);bb=np.broadcast_to(B(xx,yy),(M,)).astype(np.int64);gg=np.gcd(aa,M)
          for g in np.unique(gg):
            for residue in np.unique(bb[gg==g]%g):hit[int(residue)::int(g)]=True
          if hit.all():break
      union|=hit
      if rec['id']>8:sol|=hit
      per.append(int(hit.sum()))
    coverage.append({'modulus_m':M,'modulus_n':24*M,'all_56_image_size':int(union.sum()),'ES48_image_size':int(sol.sum()),'per_family':per,'missing_m':np.flatnonzero(~union).tolist()})
# Genuine eventually covered residue classes: fix other parameters, retain a
# linear parameter with positive slope dividing M. Each marked progression has
# a literal nonnegative-parameter preimage past its intercept.
progressions=[]
for M in [35,70,140,280,840,1680]:
    hits=set(); thresholds=[]
    for rec,m in zip(records,polys):
      if rec['id']<=8 or not rec['certificate']['symbolic']:continue
      settings=({x:a} for a in range(257)) if rec['id']<=41 else ({x:a,z:b} for a in range(33) for b in range(33))
      for setting in settings:
        lin=s.Poly(m.subs(setting),y); slope=int(lin.nth(1)); intercept=int(lin.nth(0))
        if slope>0 and M%slope==0:
          hits.update(range(intercept%slope,M,slope));thresholds.append(intercept)
    progressions.append({'modulus_n':24*M,'n_1mod24_classes':M,'certified_eventual_classes':len(hits),'uncovered_n_residues':[24*j+1 for j in range(M) if j not in hits],'sufficient_m_threshold':max(thresholds,default=None)})
res={'label':'CERTIFIED (computer)','families':len(records),'symbolically_certified':sum(r['certificate']['symbolic'] for r in records),'uncertified':[r['id'] for r in records if not r['certificate']['symbolic']],'coverage':coverage,'genuine_progression_coverage':progressions,'seconds':time.time()-t,'warning':'Modular images are existential necessary compatibility, NOT proof every integer in an image has an integral preimage. Composite families are compositeness certificates, not ES identities.'}
(out/'summary.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
