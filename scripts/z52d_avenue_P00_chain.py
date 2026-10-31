# z52d avenue P00 / Z0216: chain world x|y|z at p≡1 (4) fails iff (p+1)/2 has no prime factor ≡ 3 (mod 4). Checks the derived criterion against the stored failure list.
import json
from sympy import factorint, isprime
d=json.load(open('data/z52b/analogues_constraints_fails_20000.json'))
k=[k for k in d if 'chain' in k][0]; fails=set(d[k])
pred=set(p for p in range(5,20000) if isprime(p) and p%4==1 and all(q%4==1 for q in factorint((p+1)//2)))
print(len(fails),len(pred),fails==pred)
