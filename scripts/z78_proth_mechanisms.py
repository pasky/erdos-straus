"""Classify the two *specific* hand mechanisms; bounded certificate is fallback, not nonexistence."""
import csv
from pathlib import Path

def orbit(h):
    x=1;seen={}
    while x not in seen:seen[x]=len(seen);x=x*2%h
    return seen

def classify(m):
    h=2*m-1;orb=orbit(h);g=len(orb);aa=[a for a in range(4,h+2) if (h+1)%a==0 and -a%h in orb]
    if h%3==0:kind='primary-3' if h%9 else 'primary-9';a=None
    elif h-1 in orb:kind='I';a=h+1
    elif aa:kind='II';a=aa[0]
    else:kind='primary';a=None
    b=None if a is None else orb[-a%h];return [m,h,g,int(h-1 in orb),kind,a,b]
if __name__=='__main__':
    rows=[classify(m) for m in range(2,132)];dest=Path('data/z78/proth/mechanisms.tsv')
    with dest.open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(('m','h','ord_h(2)','minus_in_orbit','first_applicable','a','b'));w.writerows([('-' if v is None else v) for v in r] for r in rows)
    for K in ('I','II','primary','primary-3','primary-9'):
        rr=[r for r in rows if r[4]==K];print(K,len(rr),', '.join(str(r[0])+(f':{r[5]}' if K=='II' else '') for r in rr))
