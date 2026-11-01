"""Independent check of every stored graph certificate (not graph-search coverage)."""
import csv,json
from collections import Counter
from pathlib import Path
from sympy import Matrix,primerange,legendre_symbol
rows=list(csv.DictReader(open('data/z52b/pass2/ZF0/Z2851/witnesses.csv')))
assert [int(r['p']) for r in rows]==list(primerange(3,20000))
byres=Counter()
for r in rows:
 p,a,b,c,d,e,f,h=map(int,r.values())
 L=Matrix([[a+d+e,-d,-e],[-d,b+d+f,-f],[-e,-f,c+e+f]])
 assert L.det()==p
 assert h in [L.cofactor(j,j) for j in range(3)]
 assert legendre_symbol(h,p)==-1
 byres[p%24]+=1
out={'verified_primes':len(rows),'failures':[],'residue24_counts':dict(byres),'max_weight':max(int(r[k]) for r in rows for k in 'abcdef')}
Path('data/z52b/pass2/ZF0/Z2851/verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
