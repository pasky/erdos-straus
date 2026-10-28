import sys; sys.path.insert(0,'scripts')
from z49_i3fable_cells import words
from collections import defaultdict
for k in (3,5):
  for par in (1,0):
    cells=defaultdict(int); tot=0
    for m in range(3,241):
        if m%2!=par: continue
        for (t,u,v) in words(k*m*m):
            cells[(t%k==0, t%8, u%8)]+=1; tot+=1
    for div in (True,False):
        print(f"\n# n={k}m^2, m {'odd' if par else 'even'}, levels t {'≡0' if div else '≢0'} mod {k}: rows t mod 8, cols u mod 8 (total {tot})")
        for r in range(8): print(f"{r:2d} "+" ".join(f"{cells[(div,r,c)]:5d}" for c in range(8)))
