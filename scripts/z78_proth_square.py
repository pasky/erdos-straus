"""A general fixed divisor on s = 2m+2 mod (2m+1). Compress refinements via class CRT."""
from z78_proth_period import root,pa
from math import gcd,lcm
import json,sys

def add(m,H):
    f=root/f'period-{m}-{H}.json';D=json.loads(f.read_text());p=2*m+1;q=int(pa.factor(2**p-1)[0][0]);L=lcm(H,p);j=1
    left=sorted(i for b in D['left'] for i in range(b,L,H) if i%p!=j)
    D['rows'].append([p,j,'D',q]);D.update(period=L,left=left);(root/f'period-{m}-{L}.json').write_text(json.dumps(D,separators=(',',':'))+'\n');print(m,L,len(left),left[:15])
if __name__=='__main__':add(*map(int,sys.argv[1:]))
