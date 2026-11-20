"""Verify positive primary core products from integers, no source/number theory library."""
import json,math
from pathlib import Path
files=['proth/primary-3-199.json','xreview/r2opus_primary-201-209.json','xreview/r2opus_primary-211-261.json']
rows=sum((json.loads((Path('data/z78')/f).read_text()) for f in files),[]);assert [r['h'] for r in rows]==list(range(3,262,2))
for r in rows:
    h=r['h'];M=(1<<h)-1;k=2*M+1;c=r['c'];S=r['T0'];assert c>0 and k%c==0 and c%16==1 and S in [[],[1],[1,3]] and (3 not in S or h%3==0)
    # Both polynomials X+1 and X^2-X+1 evaluate to 3 at X=2.
    prod=c*3**len(S)
    for t,z in r['ratios'].items():
        i=int(t);assert 1<i<h and math.gcd(i,h)==1 and z>=0
        prod=prod*pow((1+(1<<i))*pow(3,-1,M),z,M)%M
    assert (prod+1)%M==0
print('130/130 unit-generator positive products; singletons at most degrees 1 and 3')
