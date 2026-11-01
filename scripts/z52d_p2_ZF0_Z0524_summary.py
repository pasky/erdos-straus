import json,re,csv,math
rows=[];q=None
for line in open('data/z52b/pass2/ZF0/Z0524/exact_stratified.txt'):
 if line.startswith('q='):
  h=dict(re.findall(r'(\w+)=([\d.]+)',line));q=int(h['q']);row=dict(q=q,N=int(h['N']),seconds=float(h['seconds']),residues=[]);rows.append(row)
 else:
  a={k:int(v) for k,v in re.findall(r'(\w+)=(\d+)',line)};a['failures']=a.pop('unresolved');a['coprime6_failures']=a['coprime6_admissible']-a['coprime6_certified'];row['residues'].append(a)
assert {r['q'] for r in rows}=={5,7,11},'Run not finished'
for row in rows:
 q=row['q'];assert len(row['residues'])==q-1
 fs=list(csv.DictReader(open(f'data/z52b/pass2/ZF0/Z0524/failures_q{q}_N1000000_steps0.csv')))
 for f in fs:
  n,r,c=int(f['n']),int(f['r']),int(f['coprime6'])
  assert 2<=n<=1000000 and math.gcd(n,q)==1 and (3*n-4*r)%q==0 and c==int(math.gcd(n,6)==1)
 for r in row['residues']:
  sub=[f for f in fs if int(f['r'])==r['r']]
  assert len(sub)==r['failures'] and sum(int(f['coprime6']) for f in sub)==r['coprime6_failures']
 row['admissible']=sum(r['admissible'] for r in row['residues']);row['failures']=len(fs)
 row['coprime6_admissible']=sum(r['coprime6_admissible'] for r in row['residues']);row['coprime6_failures']=sum(r['coprime6_failures'] for r in row['residues'])
 print(q,row['admissible'],row['failures'],row['coprime6_admissible'],row['coprime6_failures'],row['seconds'])
json.dump(rows,open('data/z52b/pass2/ZF0/Z0524/summary.json','w'),indent=1)
