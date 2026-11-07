# Track uncovered sub-classes of a target class a mod M0 under refinement to M = M0*k, memory O(k).
import sys, time
import z62_inversef_cover as ZC
from z62_inversef_cover import classes
from math import gcd
M0=int(sys.argv[1]); k=int(sys.argv[2]); T=[int(x) for x in sys.argv[3].split(',')]
M=M0*k
if len(sys.argv)>4 and sys.argv[4]=='5': ZC.F13=False   # 4th arg '5' = five families (A),(B),(C),(A'),(B') only; default seven
t0=time.time(); cl=classes(M); t1=time.time()
print(f"M={M} classes={len(cl)} ({t1-t0:.0f}s)")
for a in T:
    cov=bytearray(k)
    for c,D,_ in cl:
        g=gcd(M0,D)
        if (c-a)%g: continue
        Dg=D//g
        # j with a + M0 j = c mod D  <=> (M0/g) j = (c-a)/g mod Dg
        j0=((c-a)//g)*pow(M0//g,-1,Dg)%Dg if Dg>1 else 0
        cov[j0::Dg]=b'\x01'*len(range(j0,k,Dg))
    sub=[j for j in range(k) if not cov[j] and gcd(a+M0*j,M)==1]
    tot=sum(1 for j in range(k) if gcd(a+M0*j,M)==1)
    print(f"class {a} mod {M0}: {len(sub)}/{tot} coprime sub-classes mod {M} uncovered ({len(sub)/tot:.4f})")
