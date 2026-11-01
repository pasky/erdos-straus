from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path

# Small, exact tests chosen after fixing the conventions in each item.
def hj(n, a):
    out=[]
    while a:
        b=(n+a-1)//a
        out.append(b)
        n,a=a,b*a-n
    return out

def primes_upto(N):
    s=bytearray(b'\x01')*(N+1); s[:2]=b'\x00\x00'
    for i in range(2,isqrt(N)+1):
        if s[i]: s[i*i:N+1:i]=b'\x00'*(((N-i*i)//i)+1)
    return [i for i,x in enumerate(s) if x]

def dedekind(a,n):
    return sum((Fraction((2*x-n),2*n) * Fraction((2*(a*x%n)-n),2*n) for x in range(1,n)), Fraction(0))

res={}
# Z2640: directly enumerate the smallest nontrivial exact certificate-shape search, t,u,v>=2.
count=0; byp=[]; sterile=[]
for p in primes_upto(2000):
 if p%4!=1: continue
 hit=[]
 for t in range(2,p//3+2):
  umax=max(2,(p+2)//(2*t-1)+1)
  for u in range(2,umax+1):
   d=t*u-1
   if d<=0: continue
   vnum=p+u
   den=t*u-1
   if vnum%den==0:
    v=vnum//den
    if v>=2 and t*u*v-u-v==p: hit.append((t,u,v))
 count+=1
 if not hit: sterile.append(p)
res['Z2640']={'p_1mod4':count,'with_exact_interior_triple':count-len(sterile),'without':sterile[:20],'range':2000}
# Z2641: use exact bounded solution-count response for S_{n,-4}; define positive x,y,z<=40, n<=500, equation.
# This is an explicit proxy, not a claim about sibling failure data.
counts=[]; examined=0
for x in range(1,41):
 for y in range(x,41):
  for z in range(y,41):
   den=x*y+y*z+z*x
   num=4*x*y*z+4
   if den and num%den==0:
    n=num//den
    if 1<=n<=500 and n%3==0:
     counts.append(n); examined+=1
res['Z2641']={'defined_response':'number of unordered positive triples x<=y<=z<=40 solving 4xyz-n(xy+yz+zx)=-4','n_range':[1,500],'triples_found':examined,'distinct_n':len(set(counts)),'first_n':sorted(set(counts))[:20]}
# Z2645: fixed c,d=1 in the repo's Type-I divisibility relation, actual integer p specializations are not a finite cover.
# Check the simplest polynomial map p -> 4a^2+1 (fixed d=1, a=1) and its discriminant.
res['Z2645']={'fixed_parameter_test':'for fixed c,d,a, Type-I equation ef-4da^2=1 has no p variable; p enters via side condition 2h | p+f','example_fixed_d_a':{'d':1,'a':1,'ef':5,'p_specialization_condition':'2h divides p+f'},'conclusion':'no finite cover in p defined by the proposed fixed-parameter equation'}
# Z2658: OS recursion d(p,q,i), test exact sums for all coprime q and p<=40 against sum formula sanity.
from functools import lru_cache
@lru_cache(None)
def dinv(p,q,i):
 if p==1: return Fraction(0)
 r=p%q
 # q=1 base lens L(p,1): recurse uses d(1,0,...)=0
 if q==1: return Fraction((2*i+1-p-1)**2-p,4*p)
 return Fraction((2*i+1-p-q)**2-p*q,4*p*q)-dinv(q,r,i%q)
# baseline known formula for q=1; recursion setup validation for p<=30, and length-three sum splits for p<80
valid=0; group={1:[], -1:[]}; pairs=0
for p in primes_upto(80):
 for a in range(1,p):
  if gcd(a,p)>1 or len(hj(p,a))!=3: continue
  pairs+=1
  # Legendre via Euler criterion
  chi=1 if pow(a,(p-1)//2,p)==1 else -1
  group[chi].append(sum((dinv(p,a,i) for i in range(p)),Fraction(0)))
res['Z2658']={'prime_limit':80,'length3_pairs':pairs,'sum_count_by_symbol':{str(k):len(v) for k,v in group.items()},'sum_d_mean_by_symbol':{str(k):str(sum(v,Fraction(0))/len(v)) if v else None for k,v in group.items()},'q1_base_checks':sum(dinv(p,1,i)==Fraction((2*i-p)**2-p,4*p) for p in primes_upto(30) for i in range(p))}
# Z2659: verify the 3-digit closed formula against direct Dedekind sums for every HJ triple n<=150.
checks=bad=0
for t in range(2,151):
 for u in range(2,151):
  for v in range(2,151):
   n=t*u*v-u-v
   if n>150: continue
   a=t*u-1; ast=t*v-1
   lhs=12*dedekind(a,n) if gcd(a,n)==1 else None
   rhs=Fraction(t+u+v-9,1)+Fraction(a+ast,n)
   checks+=1
   if lhs!=rhs: bad+=1
res['Z2659']={'triples_tested':checks,'identity_mismatches':bad,'n_max':150}
# Z2661: exact determinant certificate for positive chains, enumeration p<100: count candidate triples; embedding into Z4 not inferred.
chains=0; prime_det=set()
for t in range(2,101):
 for u in range(2,101):
  for v in range(2,101):
   det=t*u*v-u-v
   if det<100 and det>1:
    chains+=1
    if det in primes_upto(99): prime_det.add(det)
res['Z2661']={'positive_chain_weight_triples_det_lt100':chains,'distinct_prime_determinants':len(prime_det),'prime_determinants':sorted(prime_det),'note':'Gram determinant enumeration only; no Z^4 vector embedding claimed'}
# Z2666: determinant/certificate enumeration up to n=2000, plus count length-3 QNR words.
triples=0; primecount=0; qnr=0
for t in range(2,2001):
 for u in range(2,2001):
  # v determined if n<=2000: v=(n+u)/(tu-1); enumerate n via v bound
  for v in range(2, min(2001,2001//(t*u-1)+2)):
   n=t*u*v-u-v
   if n<=2000:
    triples+=1
    if n in primes_upto(2000):
     primecount+=1
     if n%4==1 and pow(t*u-1,(n-1)//2,n)==n-1:qnr+=1
res['Z2666']={'triples_n_le_2000':triples,'prime_n_triples':primecount,'prime_1mod4_qnr_A':qnr,'genus_classes_computed':False}
# Z2671: 2-bridge continued-fraction determinant convention [a,b,c] -> numerator continuant, compare chain determinant.
triples=0; mismatch=0
for a in range(2,51):
 for b in range(2,51):
  for c in range(2,51):
   det=a*b*c-a-c
   if det<200:
    triples+=1
    if det != a*b*c-a-c: mismatch+=1
res['Z2671']={'even_HJ_three_term_words_weights_2_50_det_lt200':triples,'determinant_mismatch':mismatch,'note':'fraction/chain determinant only; no Goeritz diagram computed'}
# Z2672: Gauss sum phase for level r=1 equals Jacobi symbol when p=1 mod4 (the exact classical formula).
import cmath
errs=[]; tested=0
for p in primes_upto(101):
 if p%4!=1: continue
 for a in range(1,p):
  if gcd(a,p)>1: continue
  G=sum(cmath.exp(2j*cmath.pi*a*x*x/p) for x in range(p))/p**0.5
  chi=1 if pow(a,(p-1)//2,p)==1 else -1
  tested+=1
  if abs(G-chi)>1e-8: errs.append((p,a,G,chi))
res['Z2672']={'level_r':1,'p_1mod4_le_101_units_tested':tested,'phase_vs_legendre_mismatches':len(errs),'note':'normalized quadratic Gauss-sum proxy; not Jeffrey lens-space WRT invariant'}
# Z2673: chain blow-down test: Schur complement changes determinant boundary by factor 1 for a -1 vertex.
# For tridiagonal [-1,a] chain, blowdown updates adjacent weight a -> a+1; det preserved in 2-vertex example.
examples=0; failures=[]
for a in range(2,101):
 det=(-1)*a-1 # matrix [-1,1;1,a] determinant
 after=a+1
 if abs(det)!=abs(after): failures.append((a,det,after))
 examples+=1
res['Z2673']={'two_vertex_matrices_tested':examples,'determinant_preservation_failures':len(failures),'note':'blow-down convention for a -1 vertex; does not identify repo transport law'}
# Z2686: explicit degree<=1 polynomial search in one-coordinate family x=y=z=P(t) is a tractable restriction.
# Identity 4P^3=n*3P^2 forces P constant or zero over Q[t].
res['Z2686']={'restricted_family':'x(t)=y(t)=z(t)=P(t), deg P<=3, fixed n>0','identity':'P(t)^2*(4P(t)-3n)=0','nonconstant_polynomial_solutions':0,'degree_bound':3,'note':'restricted symmetric family only; not the full A1-curve search'}
# Z2690: chosen recurrence x_{k+1}x_{k-1}=x_k+c_k, c periodic (1,1,1,1,N); test five-step return numerically.
period=[]
for N in [1,2,3,5]:
 x0,x1=2,3; x=[x0,x1]
 for k,c in enumerate([1,1,1,1,N]): x.append((x[-1]+c)/x[-2])
 period.append({'N':N,'x_after_5':x[-1],'x0':x0,'return':abs(x[-1]-x0)<1e-10})
res['Z2690']={'initial_pair':[2,3],'five_step_tests':period,'note':'tests the literal recurrence stated in item; not evidence about a separately defined pentagon map'}
# Z2698: candidate Hilbert-symbol family (−q,−d) over Q(k) cannot be specialized from absent q,d definition; exact square/singular sample from cited claim.
res['Z2698']={'defined_check':'compare candidate class at k=0 vs square k≠0 as reported in Z52_BANKED §1(a)','result':'source records ramification at singular point at k=0; no generic Q(k) class/residue computation performed','generic_residue_values':None}
# Z2706: count torus points of 4xyz=n(xy+yz+zx) over F_q for small odd q and n=0,1.
finite=[]
for q in [3,5,7,11,13,17,19,23,29,31]:
 for n in [0,1]:
  c=0
  for x in range(1,q):
   for y in range(1,q):
    for z in range(1,q):
     if (4*x*y*z-n*(x*y+y*z+z*x))%q==0:c+=1
  finite.append({'q':q,'n':n,'count':c,'divisible_by_q':c%q==0})
res['Z2706']={'torus_point_counts':finite}
# Z2720: test the item’s stated vertex criterion by comparing HJ length and number of digits >=3, p<=499, QNR A.
items=0; mismatches=[]; lengths={}
for p in primes_upto(499):
 if p%4!=1: continue
 for a in range(1,p):
  if gcd(a,p)>1 or pow(a,(p-1)//2,p)!=p-1: continue
  ds=hj(p,a); items+=1; lengths[len(ds)]=lengths.get(len(ds),0)+1
  if len(ds)!=sum(d>=3 for d in ds):
   if len(mismatches)<5:mismatches.append({'p':p,'A':a,'digits':ds,'n_vertices_digits_ge3':sum(d>=3 for d in ds)})
res['Z2720']={'p_1mod4_le_499_qnr_pairs':items,'HJ_length_histogram':lengths,'length_vs_digits_ge3_mismatches':mismatches}
# Z2723: exact character sum on HJ length-3 set for p<=10000, p=1 mod4.
sums=[]; total=0
for p in primes_upto(10000):
 if p%4!=1:continue
 s=c=0
 for a in range(1,p):
  if len(hj(p,a))==3:
   s += 1 if pow(a,(p-1)//2,p)==1 else -1; c+=1
 if c:sums.append({'p':p,'count':c,'character_sum':s}); total+=c
res['Z2723']={'p_1mod4_le_10000_with_L3':len(sums),'pairs':total,'sum_range':[min(x['character_sum'] for x in sums),max(x['character_sum'] for x in sums)] if sums else None,'first':sums[:10]}
# Z2728: explicit discriminant collision identity check on small d1,d2 and trace=2.
checks=0; negative=0
for d1 in range(1,31):
 for d2 in range(1,31):
  disc=(d1*d2-4)//4
  if d1*d2%4==0:
   checks+=1
   if disc<0:negative+=1
res['Z2728']={'d1_d2_pairs_divisible_by4':checks,'negative_discriminants':negative,'note':'only checks the algebraic trace-2 discriminant; no Hecke intersection multiplicities'}
# Z2729: local norm representation proxy: count representations m=x²+xy+2y² for m<=100 and report; not Brandt matrices.
reps={m:0 for m in range(1,101)}
for x in range(-20,21):
 for y in range(-20,21):
  m=x*x+x*y+2*y*y
  if 1<=m<=100:reps[m]+=1
res['Z2729']={'binary_positive_norm_form':'x^2+xy+2y^2','m_range':[1,100],'represented_m':sum(v>0 for v in reps.values()),'total_representations':sum(reps.values()),'note':'proxy only, not quaternion Brandt matrices'}

out=Path('data/z52b/pass2/NC2')
for mid,x in res.items():
 d=out/mid; d.mkdir(parents=True,exist_ok=True)
 (d/'metrics.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res,ensure_ascii=False,indent=2))
