"""R184 reviewer 2: for which periods L can odd m mod L be covered by fixed-pair families (x,y) [d=xy-1, shift x]
or (x,z) [d=xz, shift x+z] with d <= D, for n = 2^m - 2 (large m)? A family covers class r mod L iff
d | 2^m - 2 + shift for ALL large m = r mod L (exact periodic check over a window)."""
import sys
D = int(sys.argv[1]) if len(sys.argv)>1 else 3000
Lmax = int(sys.argv[2]) if len(sys.argv)>2 else 72
fams=set()
for x in range(2,D):
    for y in range(2,D):
        d=x*y-1
        if d>D: break
        fams.add((d,x%d))
        if y>=x: fams.add((x*y,(x+y)%(x*y)))
fams=sorted(fams)
M0=60  # base offset so 2-adic conditions are stable
# for each family: set of m in window [M0, M0+W) with d | 2^m - 2 + s
W=2*Lmax*36
hits=[]
for d,s in fams:
    S=[m for m in range(M0,M0+W) if (pow(2,m,d)-2+s)%d==0]
    if S: hits.append(set(S))
print('families with any hit:',len(hits))
for L in range(2,Lmax+1):
    covered=set()
    for S in hits:
        for r in range(L):
            ms=[m for m in range(M0,M0+W) if m%L==r]
            if all(m in S for m in ms): covered.add(r)
    miss=[r for r in range(1,L,2) if r not in covered] if L%2==0 else [r for r in range(L) if r not in covered]
    if not miss: print('L =',L,'works'); break
    elif L in (12,18,24,30,36): print('L =',L,'misses (odd m classes if L even):',miss[:10])
