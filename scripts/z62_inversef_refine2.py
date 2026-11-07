import sys, time
import z62_inversef_cover as ZC
from z62_inversef_cover import classes, is_square_class
from math import gcd
M0=int(sys.argv[1]); k=int(sys.argv[2]); T=[int(x) for x in sys.argv[3].split(',')]
M=M0*k
if len(sys.argv)>4 and sys.argv[4]=='5': ZC.F13=False   # 4th arg '5' = five families (A),(B),(C),(A'),(B') only; default seven
t0=time.time(); cl=classes(M); t1=time.time()
cov=bytearray(M)
for c,D,_ in cl:
    cov[c::D]=b'\x01'*len(range(c,M,D))
print(f"M={M} classes={len(cl)} ({t1-t0:.0f}s)")
for a in T:
    sub=[b for b in range(a,M,M0) if gcd(b,M)==1 and not cov[b]]
    tot=sum(1 for b in range(a,M,M0) if gcd(b,M)==1)
    print(f"class {a} mod {M0}: {len(sub)}/{tot} coprime sub-classes mod {M} uncovered; e.g. {sub[:5]}")
