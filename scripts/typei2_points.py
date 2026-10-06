import sys
boxes=[]
for line in open('/tmp/s27_3e8.txt'):
    t=line.split(); M2,r2,M7,r7=map(int,t[9:13]); boxes.append((M2,r2,M7,r7,line.strip()))
ws=[w for w in range(-200,400) if w%16==9]
zs=[z for z in range(-60,60) if z%7 in (3,5,6)]
res=[]
for w in ws:
  for z in zs:
    hit=None
    for (M2,r2,M7,r7,l) in boxes:
      if (w-r2)%M2==0 and (z-r7)%M7==0:
        L=None; hit=l; break
    if hit is None: res.append((w,z))
print(len(ws)*len(zs), "points;", len(res), "uncovered up to 3e8:", res[:60])
