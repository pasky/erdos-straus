"""Independent direct-y search at n<=200 vs the optimized exact divisor census."""
import math,re,json
stats={q:{r:[0,0,0] for r in range(1,q)} for q in (5,7,11)}
for q in stats:
 for n in range(2,201):
  if n%q==0:continue
  r=(3*n*pow(4,-1,q))%q;rec=stats[q][r];rec[0]+=1;found=False
  for x in range(n//4+1,3*n//4+1):
   if x%q!=r:continue
   A,B=4*x-n,n*x
   # y>=x, positive remainder, and y<=z imply y<=2B/A.
   for y in range(max(x,B//A+1),2*B//A+1):
    if y%q!=r:continue
    num,den=B*y,A*y-B
    if num%den==0 and num//den>=y and num//den%q==r:
     found=True;break
   if found:break
  rec[1]+=found
  if not found and not rec[2]:rec[2]=n
q=None
for line in open('data/z52b/pass2/ZF0/Z0524/small.txt'):
 if line.startswith('q='):q=int(re.search(r'q=(\d+)',line)[1])
 else:
  row={k:int(v) for k,v in re.findall(r'(\w+)=(\d+)',line)};r=row['r']
  assert stats[q][r]==[row['admissible'],row['certified'],row['first_exact_failure']],(q,r,stats[q][r],row)
print('All 20 (q,r) rows agree with independent y enumeration for 2<=n<=200.')
json.dump(stats,open('data/z52b/pass2/ZF0/Z0524/validation.json','w'),indent=1)
