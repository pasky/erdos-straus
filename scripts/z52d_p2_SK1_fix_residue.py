# z52d pass2 SK1 fix (Z1232 counterfactual by residue; Z1233 active-learning boundary test) on R(p) = #(star) words,
# primes 1 mod 4 <= 3e6 (data from scripts/z52d_p2_SK1_fix_resp.c). Lines "P p R" (R includes all words, R=0 allowed).
from collections import defaultdict
import math
rows=[]
for l in open('data/z52b/pass2/SK1/Z1232_R_primes_3e6.txt'):
    t=l.split()
    if t[0]=='P': rows.append((int(t[1]),int(t[2])))
print("primes 1 mod 4 (<=3e6, incl. p=5):", len(rows), " R=0:", sum(1 for _,R in rows if R==0))
# Z1232: residue-matched comparison: for each class mod 840 compare R>0 rate in the lower and upper half of the range
byc=defaultdict(list)
for p,R in rows: byc[p%840].append((p,R))
mismatch=[]; lo_rate=[]; hi_rate=[]
for c,lst in byc.items():
    if len(lst)<40: continue
    lst.sort(); h=len(lst)//2
    lo=sum(1 for _,R in lst[:h] if R>0)/h; hi=sum(1 for _,R in lst[h:] if R>0)/(len(lst)-h)
    lo_rate.append(lo); hi_rate.append(hi)
print(f"Z1232 residue classes mod 840 with >=40 primes: {len(lo_rate)}; mean R>0 rate lower half {sum(lo_rate)/len(lo_rate):.6f}, upper half {sum(hi_rate)/len(hi_rate):.6f}")
# counterfactual: within the same class, replace p by the next prime in the class (same residue, nearest size) and record R change
ch=[]
for c,lst in byc.items():
    lst.sort()
    for (p1,R1),(p2,R2) in zip(lst,lst[1:]):
        if (R1>0)!=(R2>0): ch.append(1)
        else: ch.append(0)
print(f"Z1232 counterfactual swaps within residue mod 840 (adjacent primes): {len(ch)}, R>0 indicator flips: {sum(ch)}")
# Z1233: boundary = where the simplest selector (residue mod 24 class) changes its prediction 'R>0'
c24=defaultdict(lambda:[0,0])
for p,R in rows: c24[p%24][0 if R>0 else 1]+=1
amb=[(k,v) for k,v in c24.items() if min(v)>0]
print("Z1233 residue classes mod 24 with both R>0 and R=0 primes:",len(amb), "of", len(c24))
print("Z1233 minority-class share by class (R=0 fraction, max):", max((v[1]/(v[0]+v[1])) for v in c24.values()))
