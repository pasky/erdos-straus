from cf_lib import *
from itertools import product
# epsilon_2 of path form of (t,u,v); chi relation; rotation & scaling
def eps2(w):
    return -1 if ternary_aniso(word_diag(w),2) else 1
def K(t,u,v): return t*u*v-u-v
bad=0; cnt=0; rotbad=0; rotcnt=0; cellbad=0
cell={}
for t,u,v in product(range(1,41),repeat=3):
    n=K(t,u,v)
    if n<1 or n%2==0: continue
    e=eps2((t,u,v)); c=chi((t,u,v),n); cnt+=1
    if c!=-e: bad+=1
    key=(t%8,u%8,v%8)
    if cell.setdefault(key,e)!=e: cellbad+=1
    # rotation (v,t,u)->(t,u,v): new middle u, outer t,v ; as (t',u',v')=(u, v, t)? word [[v,t,u]] -> [[t,u,v]]: middle u, left t, right v
    w2=(u,v,t)  # (t,u,v) format: middle=u, 'u'-slot=v, 'v'-slot=t
    n2=K(*w2)
    if n2>=1 and n2%2==1:
        rotcnt+=1
        if chi(w2,n2)!=c: rotbad+=1
print("words",cnt,"chi!=-eps2",bad,"cell(mod8) inconsistencies",cellbad,"cells",len(cell))
print("rotations",rotcnt,"chi changed",rotbad)
# scaling: (v',a t,u') word of m -> (a v', t, a u') of a m
sb=0;sc=0
for a in range(2,12):
  for t,u,v in product(range(1,25),repeat=3):
    m=K(a*t,u,v)
    if m<1 or (a*m)%2==0: continue
    w1=(a*t,u,v); w2=(t,a*u,a*v)
    assert K(*w2)==a*m
    sc+=1
    if chi(w1,m)!=chi(w2,a*m): sb+=1
print("scalings",sc,"chi changed",sb)
