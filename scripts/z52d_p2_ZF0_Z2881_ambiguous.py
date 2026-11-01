"""All primitive reduced positive forms and ambiguous word-factorization genera."""
import math,json
from collections import defaultdict
from sympy import primerange
from z52d_p2_ZF0_Z2806_words import words,chi,save
from z52d_p2_ZF0_Z2825_classes import genus,genus_discs

def reduced(D):
 for a in range(1,math.isqrt((-D)//3)+1):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a):continue
   c=(b*b-D)//(4*a)
   if a>c or ((abs(b)==a or a==c) and b<0):continue
   if math.gcd(math.gcd(a,b),c)==1:yield (a,b,c)

rows=[];imprimitive=[];clashes=[];signclashes=[];primword=0;classcount=ambcount=0;wordgenera=set()
for p in primerange(5,500):
 if p%4!=1:continue
 by_t=defaultdict(list)
 for t,u,v in words(p):
  if t<=12 and u<=v:by_t[t].append((t*u-1,t*v-1,u,v))
 for t in range(2,13):
  N=t*p+1;D=-4*N;forms=list(reduced(D));amb=[Q for Q in forms if Q[1]==0 or abs(Q[1])==Q[0] or Q[0]==Q[2]]
  classcount+=len(forms);ambcount+=len(amb)
  wf={};im=0
  for A,B,u,v in by_t[t]:
   g=math.gcd(A,B)
   if g>1:
    im+=1;imprimitive.append({'p':p,'t':t,'A':A,'Astar':B,'content':g,'primitive_discriminant':D//(g*g)})
   else:wf[(A,0,B)]=chi(A,p);primword+=1
  assert all(Q in amb for Q in wf)
  buckets=defaultdict(list)
  for Q in amb:buckets[genus(Q)].append(Q)
  for g,qs in buckets.items():
   yes=[Q for Q in qs if Q in wf];no=[Q for Q in qs if Q not in wf]
   if yes and no:clashes.append({'p':p,'t':t,'D':D,'genus_discs':genus_discs(D),'genus':g,'word':yes[0],'nonword':no[0]})
   if len({wf[Q] for Q in yes})>1:signclashes.append({'p':p,'t':t,'D':D,'genus':g,'words':[(Q,wf[Q]) for Q in yes]})
  gs=sorted(set(genus(Q) for Q in wf));wordgenera.update((D,g) for g in gs)
  rows.append({'p':p,'t':t,'D':D,'class_number':len(forms),'ambiguous_classes':len(amb),'word_primitive_forms':[{'form':Q,'genus':genus(Q),'sign':s} for Q,s in wf.items()],'genus_discs':genus_discs(D),'word_genus_count':len(gs),'imprimitive_word_factorizations':im})
out={'p_condition':'5<=p<500, p=1 mod4','t_range':[2,12],'level_pairs':len(rows),'total_reduced_classes':classcount,'total_ambiguous_classes':ambcount,'primitive_word_factorizations':primword,'imprimitive_word_factorizations':len(imprimitive),'levels_multiple_word_genera':sum(r['word_genus_count']>1 for r in rows),'mixed_word_nonword_genus_cells':len(clashes),'mixed_sign_genus_cells':len(signclashes),'clashes':clashes,'sign_clashes':signclashes,'imprimitive_examples':imprimitive[:10],'rows':rows}
save('Z2881',out)
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','clashes','sign_clashes')},indent=2));print('clash',clashes[:2]);print('sign',signclashes[:2])
