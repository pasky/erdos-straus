import sys, runpy
sys.argv=['x','4','/tmp/o95/run']
g=runpy.run_path('scripts/m13b_cell.py')
cov,R=g['cov'],g['R']
from sympy.ntheory.modular import crt
from fractions import Fraction as Fr
k=4; A,B=11**k,13**k
rats=sorted({Fr(p,q) for p in range(-40,41) for q in range(1,41) if p and p%11 and p%13 and q%11 and q%13}, key=lambda f: max(abs(f.numerator),f.denominator))
def red(f,m): return f.numerator*pow(f.denominator,-1,m)%m
c11=[f for f in rats if red(f,11)==2]; c13=[f for f in rats if red(f,13)==2]
out=[]
for f in c11[:60]:
    for h in c13[:60]:
        v=int(crt([A,B],[red(f,A),red(h,B)])[0])
        if not cov[(v-2)//143]: out.append((str(f),str(h)))
print(len(out), out[:30])
