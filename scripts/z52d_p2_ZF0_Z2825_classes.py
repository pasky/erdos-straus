"""Exact minus-CF narrow cycles, genus characters and maximal-order extension.
No PARI: transformations are integral determinant-one substitutions.
"""
import math,json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from sympy import factorint,kronecker_symbol,Matrix,primerange
from sympy.matrices.normalforms import hermite_normal_form
from z52d_p2_ZF0_Z2806_words import words,chi,save

@lru_cache(None)
def fundamental(D):
 sf=math.prod(int(q) for q,e in factorint(D).items() if e%2)
 D0=sf if sf%4==1 else 4*sf
 f=math.isqrt(D//D0);assert f*f*D0==D
 return D0,f

@lru_cache(None)
def genus_discs(D):
 # All prime-discriminant characters valid for this order discriminant.
 ds=[int(q) if q%4==1 else -int(q) for q in factorint(abs(D)) if q!=2]
 ds += [d for d in (-4,8,-8) if D%d==0 and (D//d)%4 in (0,1)]
 return tuple(d for d in ds if D%d==0 and (D//d)%4 in (0,1))

def genus(Q):
 a,b,c=Q;D=b*b-4*a*c
 for H in range(1,100):
  for x,y in ([(x,y) for x in range(-H,H+1) for y in (-H,H)]+[(x,y) for x in (-H,H) for y in range(-H,H+1)]):
   n=a*x*x+b*x*y+c*y*y
   if n>0 and math.gcd(n,D)==1:
    return tuple(int(kronecker_symbol(d,n)) for d in genus_discs(D))
 raise ValueError(('no represented coprime integer',Q))

def cycle(Q):
 a,b,c=Q;D=b*b-4*a*c;sd=math.isqrt(D)
 assert a>0 and D>0 and sd*sd<D
 seen={};forms=[];digits=[]
 while (a,b,c) not in seen:
  seen[a,b,c]=len(forms);forms.append((a,b,c))
  q=(-b+sd)//(2*a)+1 # exact ceil of irrational root
  digits.append(q)
  a,b,c=a*q*q+b*q+c,-2*a*q-b,a
  assert a>0 and b*b-4*a*c==D
  assert len(forms)<100000
 i=seen[a,b,c];forms=forms[i:];digits=digits[i:]
 j=min(range(len(forms)),key=lambda j:forms[j])
 forms=forms[j:]+forms[:j];digits=digits[j:]+digits[:j]
 assert all(q>=2 for q in digits) and any(q>2 for q in digits)
 return tuple(forms),tuple(digits)

def maxform(Q):
 a,b,c=Q;D=b*b-4*a*c;D0,f=fundamental(D);s=D0%2;k=(-b-f*s)//2;l=(D0-s*s)//4
 H=hermite_normal_form(Matrix([[a,k,0,f*l],[0,f,a,k+f*s]]))
 h11,h12,h22=int(H[0,0]),int(H[0,1]),int(H[1,1])
 assert h11%h22==h12%h22==0
 aa=h11//h22;bb=-(2*(h12//h22)+s);cc=(bb*bb-D0)//(4*aa)
 assert bb*bb-4*aa*cc==D0
 return (aa,bb,cc)

if __name__=='__main__':
 rows=[];groups=defaultdict(list);principal_negative=[];zrows=[]
 for p in primerange(5,300):
  if p%4!=1:continue
  ss=0;zs=Fraction(0);zunique={};n=0
  for t,u,v in words(p):
   A=t*u-1;B=t*v-1;T=A+B;D=T*T-4;Q=(t,B-A,-p)
   assert math.gcd(math.gcd(*Q[:2]),Q[2])==1
   cyc,digits=cycle(Q);g=genus(Q)
   assert genus(cyc[0])==g
   mf=maxform(Q);mc,md=cycle(mf);D0,f=fundamental(D)
   z=Fraction(sum(q-3 for q in md),12)
   sgn=chi(A,p);ss+=sgn;zs+=z;n+=1
   zunique[(D0,mc)]=z
   row={'p':p,'word':[t,u,v],'sign':sgn,'trace':T,'D':D,'form':Q,'cycle':cyc,'digits':digits,'genus_discs':genus_discs(D),'genus':g,'D0':D0,'conductor':f,'maximal_form':mf,'maximal_cycle':mc,'maximal_digits':md,'zeta0':str(z)}
   rows.append(row);groups[(D,g)].append(row)
   if sgn==-1 and all(x==1 for x in g):principal_negative.append(row)
  zrows.append({'p':p,'words':n,'sign_sum':ss,'zeta_sum_multiplicity':str(zs),'zeta_sum_distinct_classes':str(sum(zunique.values(),Fraction(0))),'distinct_classes':len(zunique)})
 clashes=[]
 for (D,g),rs in groups.items():
  if len({r['sign'] for r in rs})>1:
   a=next(r for r in rs if r['sign']==1);b=next(r for r in rs if r['sign']==-1)
   clashes.append({'D':D,'genus':g,'words':[[r['p'],r['word'],r['sign']] for r in (a,b)]})
 # D=12: zeta_plus-zeta_minus=L(0,chi_-4)L(0,chi_-3)=1/6,
 # zeta_plus+zeta_minus=0, hence principal value 1/12.
 # D=5 has a negative-norm unit and its single narrow partial value is zero.
 assert Fraction(sum(q-3 for q in cycle((1,0,-3))[1]),12)==Fraction(1,12)
 assert Fraction(sum(q-3 for q in cycle((1,1,-1))[1]),12)==0
 out={'primes':len(zrows),'words':len(rows),'negative_in_principal_genus':len(principal_negative),'first_principal_genus_negative':principal_negative[:3],'genus_sign_clashes':clashes[:10],'clash_count':len(clashes),'rows':rows}
 save('Z2825',out)
 zout={'formula_source':'https://arxiv.org/html/1111.6717v1#S3.E9','formula':'q=1: x_i=1, -B1(1)^2+b_i B2(1)/2=(b_i-3)/12; primitive cycle in maximal order','rows':zrows,'mismatches_multiplicity':sum(r['words']>0 and Fraction(r['zeta_sum_multiplicity'])!=r['sign_sum'] for r in zrows),'mismatches_distinct':sum(r['words']>0 and Fraction(r['zeta_sum_distinct_classes'])!=r['sign_sum'] for r in zrows)}
 save('Z2845',zout)
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','first_principal_genus_negative','genus_sign_clashes')},indent=2));print(out['first_principal_genus_negative'][:1]);print(out['genus_sign_clashes'][:1]);print(json.dumps(zout,indent=2))
