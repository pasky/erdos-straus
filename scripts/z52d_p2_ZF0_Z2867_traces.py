"""Symbolic HJ/Fricke identities plus a specified non-tautological trace search."""
import math,itertools
from collections import Counter
from sympy import Matrix,symbols,expand,factor,primerange
from z52d_p2_ZF0_Z2806_words import words,save
u,t,v=symbols('u t v');M=lambda k:Matrix([[k,-1],[1,0]])
a,b,c=M(v),M(t),M(u);G=(a*b*c).applyfunc(expand);n=t*u*v-u-v;T=G.trace()
x=(a*b).trace();y=(b*c).trace();z=(a*c).trace()
assert G==Matrix([[n,-(t*v-1)],[t*u-1,-t]])
fricke=x*x+y*y+z*z+x*y*z-(v*t+u*T)*x-(t*u+v*T)*y-(v*u+t*T)*z-4+v*v+t*t+u*u+T*T+v*t*u*T
assert expand(fricke)==0
s,A,As,B,Bs,p=symbols('s A As B Bs p')
GG=Matrix([[p,-As],[A,-t]]);HH=Matrix([[p,-Bs],[B,-s]])
traceprod=expand((GG*HH).trace())
traceinv=expand((GG*Matrix([[-s,Bs],[-B,p]])).trace())
stats=Counter();hits=[];examples=[];perprime=[]
def check(p,values,kind,meta):
 for AA,BB,CC in set(itertools.permutations(values)):
  stats[kind+'_assignments']+=1
  DD=AA*BB*CC-p*AA*AA-BB*BB
  if AA>0 and BB>0 and CC>0 and DD>0:
   stats[kind+'_positive_residual']+=1
   if CC%(2*DD)==0:
    stats[kind+'_level_divisibility']+=1
    if AA%2==0 and BB%2==1 and math.gcd(AA,BB)==math.gcd(BB,p)==1:
     stats[kind+'_shot_family']+=1
     hits.append({'p':p,'kind':kind,'trace_ABC':[AA,BB,CC],'D':DD,'lambda':CC//(2*DD),'source':meta})
for pp in primerange(3,200):
 ww=list(words(pp));stats['words']+=len(ww)
 for tt,uu,vv in ww:check(pp,(vv*tt-2,tt*uu-2,vv*uu-2),'letter_pairs',[tt,uu,vv])
 for w1,w2 in itertools.combinations(ww,2):
  tt,uu,vv=w1;ss,rr,zz=w2
  aa=tt*uu-1;as_=tt*vv-1;bb=ss*rr-1;bs=ss*zz-1
  xx=pp-tt;yy=pp-ss;zz_=pp*pp-as_*bb-aa*bs+tt*ss
  zz_inv=xx*yy-zz_
  # Fricke identity independently with exact integer matrix arithmetic.
  g=Matrix([[pp,-as_],[aa,-tt]]);h=Matrix([[pp,-bs],[bb,-ss]])
  assert (g*h).trace()==zz_ and (g*h.inv()).trace()==zz_inv
  assert (g*h*g.inv()*h.inv()).trace()==xx*xx+yy*yy+zz_*zz_-xx*yy*zz_-2
  stats['word_matrix_pairs']+=1
  check(pp,(xx,yy,zz_),'word_pair_product',[w1,w2])
  check(pp,(xx,yy,zz_inv),'word_pair_inverse',[w1,w2])
out={'word_matrix':str(G),'trace':str(expand(T)),'pair_traces':[str(x),str(y),str(z)],'fricke_cubic_verified':True,'common_p_pair_product_trace':str(traceprod),'common_p_pair_inverse_trace':str(traceinv),'stats':dict(stats),'hits':hits,'scope':'All odd primes p<200, all interior words, all unordered distinct pairs within a prime; all permutations of each specified trace triple; no arbitrary affine reparametrizations.'}
save('Z2867',out);print(out)
