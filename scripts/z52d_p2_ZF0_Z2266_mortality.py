"""Finite-image mortality/reachability, with the actual ES HJ letters."""
from collections import deque
from sympy import primerange
from z52d_p2_ZF0_Z2806_words import mul,chi,save
rows=[]
for p in primerange(3,32):
 gens=[(2%p,p-1,1,0),(3%p,p-1,1,0)]
 seen={(1,0,0,1)};queue=deque(seen)
 while queue:
  g=queue.popleft()
  for h in gens:
   k=mul(g,h,p)
   if k not in seen: seen.add(k);queue.append(k)
 assert len(seen)==p*(p*p-1)
 assert (0,0,0,0) not in seen
 targets=signsum=0
 for t in range(p):
  for u in range(p):
   for v in range(p):
    g=mul(mul((v,p-1,1,0),(t,p-1,1,0),p),(u,p-1,1,0),p)
    assert (g[0]*g[3]-g[1]*g[2])%p==1
    if g[0]==0: targets+=1;signsum+=chi(g[2],p)
 assert targets==p*p-p+1 and signsum==p*chi(-1,p)
 rows.append({'p':p,'reachable':len(seen),'zero_products':0,'length3_zero_entry_targets':targets,'target_sign_sum':signsum})
save('Z2266',{'source':'https://uniformlyatrandom.wordpress.com/2009/07/09/matrix-mortality/','reduction':'adjoin singular projector E11; E11 G E11 = G11 E11','rows':rows})
print(rows)
