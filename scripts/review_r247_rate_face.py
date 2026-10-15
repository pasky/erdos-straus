"""R247: zero set of restricted min_route - 1/2 at q = 3 (G = 60): on / off the face b = 1/2."""
import sys
from math import log
sys.path.insert(0,'scripts'); import fs_rate as F
G=60; lq=log(3); nf=zf=0; other=[]
for i in range(G+1):
  for j in range(G+1-i):
    for k in range(G+1-i-j):
      a,z,y=i/G,j/G,k/G; t=1-a-z-y
      if not(a<=y+t+1e-12 and y+t>=0.5-1e-12 and max(z+2*a,t)>=0.5-1e-12): continue
      v=min(F.routes(a,z,y,t,lq).values())-0.5
      onf=abs(y+t-0.5)<1e-9
      if onf: nf+=1; zf+= v>-1e-9
      elif v>-1e-9: other.append((round(a,3),round(z,3),round(y,3),round(t,3)))
print('face b=1/2: grid pts',nf,'zero',zf); print('zeros off face',len(other),other[:40])
