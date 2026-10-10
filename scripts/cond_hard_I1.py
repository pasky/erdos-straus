import sys
sys.path.insert(0, "scripts")  # usage: PYTHONPATH=scripts uv run python scripts/cond_hard_I1.py X
from cond_divisor_forms import typeI_a1
from sympy import primerange
X=int(sys.argv[1]); sq={(x*x)%840 for x in range(840)}
mx=(0,0); cnt=0; fails=[]
for p in primerange(3,X):
    if p%840 not in sq: continue
    cnt+=1
    r=typeI_a1(p)
    if r is None: fails.append(p); continue
    if r[0]>mx[0]: mx=(r[0],p)
print(cnt,"hard primes; fails",fails,"max t",mx)
