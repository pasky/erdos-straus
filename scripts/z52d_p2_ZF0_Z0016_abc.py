"""Exact integer checks on c=1 certificates; abc quality is a diagnostic, not abc proof."""
import math,json
from sympy import factorint, symbols, expand, gcd, degree
T=symbols('T'); fn=3*T-1; fx,fy,fz=T,T*fn,fn
assert expand(4*fx*fy*fz-fn*(fx*fy+fx*fz+fy*fz))==0
fA,fB,fD=fn*fx*fy,fn*fx*fz,fy*fz*(4*fx-fn)
fG=gcd(fA,fB)
ff=[expand(v/fG).cancel() for v in (fA,fB,fD)]
assert ff==[T,1,T+1]
ff_example=dict(n=str(fn),denominators=list(map(str,(fx,fy,fz))),primitive=list(map(str,ff)),max_degree=1,radical_degree=2)
rad={k:math.prod(factorint(k)) for k in range(1,401)}
count=0;worst=(0,None);qgt=0;distinct=set();maxn=0;maxz=0
for a in range(1,201):
 for b in range(a,201):
  g=math.gcd(a,b);aa,bb,cc=a//g,b//g,(a+b)//g
  R=rad[aa]*rad[bb]*rad[cc]
  quality=math.log(cc)/math.log(R)
  distinct.add((aa,bb,cc))
  if quality>worst[0]:worst=(quality,[aa,bb,cc,R])
  for C in range(1,13):
   n=4*a*b*C-a-b
   if not 2<=n<=1000000:continue
   x,y,z=a*b*C,a*C*n,b*C*n
   assert 4*x*y*z==n*(x*y+x*z+y*z)
   A,B,D=n*x*y,n*x*z,y*z*(4*x-n)
   G=math.gcd(A,B)
   assert A+B==D and (A//G,B//G,D//G)==(aa,bb,cc)
   count+=1;qgt+=quality>1;maxn=max(n,maxn);maxz=max(x,y,z,maxz)
json.dump(dict(function_field_example=ff_example,solutions=count,distinct_primitive_triples=len(distinct),max_n=maxn,max_denominator=maxz,quality_gt_one=qgt,max_quality=worst,parameters='1<=a<=b<=200;1<=C<=12;2<=n<=10^6'),open('data/z52b/pass2/ZF0/Z0016/abc.json','w'),indent=1)
print(count,len(distinct),maxn,maxz,worst)
