import json,gzip,sys
from sympy import factorint
from fractions import Fraction as Fr
T=json.load(gzip.open(sys.argv[1],'rt'))
ex={}
for r in T['roots']:
    om=Fr(0); n=0; st=[(r,Fr(1))]
    while st:
        nd,m=st.pop()
        if 'children' in nd:
            for c in nd['children']: st.append((c,m/len(nd['children'])))
        elif nd.get('open'):
            om+=m; n+=1
            for p,e in factorint(nd['L']).items(): ex[p]=max(ex.get(p,0),e)
    print(r['x'], n, float(om))
print(sorted(ex.items()))
