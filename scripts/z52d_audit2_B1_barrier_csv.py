# Z1867: export FRONTIER §3 barrier map + §6 dead-end list as CSV (approach, fails_at, pointer, category)
import csv,re,sys
L=open('FRONTIER.md',encoding='utf8').read().split('\n')
def sec(a,b):
    i=[k for k,l in enumerate(L) if l.startswith(a)][0]; j=[k for k,l in enumerate(L) if l.startswith(b)][0]; return L[i:j]
out=csv.writer(open('data/z52d/audit2/B1/barriers.csv','w',newline='',encoding='utf8'))
out.writerow(['kind','category','approach_or_barrier','fails_at_or_statement','pointer'])
nb=0
for l in sec('## 3.','## 4.'):
    m=re.match(r'\*\*(.+?)\*\*\s*(.*)',l)
    if m: out.writerow(['barrier','§3',m.group(1).strip(' .'),'',m.group(2).strip()]); nb+=1
cat=None; nd=0; cur=None; rows=[]
for l in sec('## 6.','## 7.'):
    if l.startswith('*') and l.endswith('*') and not l.startswith('* '): cat=l.strip('*'); continue
    if l.startswith('* '): cur=[cat,l[2:]]; rows.append(cur)
    elif l.startswith('  ') and cur: cur[1]+=' '+l.strip()
for cat,t in rows:
    parts=[s.strip() for s in t.split('→')]
    appr=parts[0]; fail=' → '.join(parts[1:-1]) if len(parts)>2 else (parts[1] if len(parts)==2 else ''); ptr=parts[-1] if len(parts)>2 else ''
    out.writerow(['dead-end',cat,appr,fail,ptr]); nd+=1
print('barriers',nb,'dead-ends',nd)
