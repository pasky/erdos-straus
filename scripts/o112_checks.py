# O112 checks: (1) section 8.0 identities for w_c-tuples; (2) e-cusp local density = f-cusp density.
from math import gcd
bad=0; cnt=0
for c in range(1,6):
  for a in range(1,40):
    for d in range(1,60):
      M=4*a*a*d+1
      for f in range(1,M+1):
        if M%f: continue
        n=4*a*c*d-f
        if n<=0 or f>2*n: continue
        cnt+=1
        e=M//f; b=c*e-a
        ok = (4*a*b*d==n*e+1) and (b*f==n*a+c) and b>0 and 2*b>=a and (a+b)%e==0 and gcd(e,4*a*b)==1 and gcd(f,2*a)==1
        if not ok: bad+=1
print("tuples",cnt,"failures",bad)
# (2) densities mod l: #{B^2-4dAC'=-4d, cB=A} vs #{..., cB=C'} over quadric size
for l in [3,5,7,11,13]:
  for d in [1,2,5,7,13]:
    if d%l==0: continue
    for c in [1,2,3,5]:
      Q=[(A,B,C) for A in range(l) for B in range(l) for C in range(l) if (B*B-4*d*A*C+4*d)%l==0]
      g1=sum(1 for A,B,C in Q if (c*B-A)%l==0); g2=sum(1 for A,B,C in Q if (c*B-C)%l==0)
      if g1!=g2: print("MISMATCH",l,d,c,g1,g2)
print("density check done")
