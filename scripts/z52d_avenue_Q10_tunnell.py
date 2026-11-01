"""z52d avenue Q10 (Z0920): correlate Tunnell ternary counts A(p) = #{x²+2y²+8z² = p}, B(p) = #{x²+2y²+32z² = p}
with R(p)/log²p ((★) count) for primes p ≡ 1 (4), 10³ < p ≤ 3·10⁵; A − 2B is the weight-3/2 cusp (Tunnell) part.
Run: timeout 60 python3 scripts/z52d_avenue_Q10_tunnell.py  (needs R from z52d_avenue_Q10_rparity.py logic; recomputed here)"""
import numpy as np
N=300000
R=np.zeros(N+1)
u=1
while 3*u-1<=N:
    B=1
    while 4*u*B-u-B<=N:
        R[4*u*B-u-B::4*u*B]+=1; B+=1
    u+=1
def th(c):
    t=np.zeros(N+1); k=0
    while c*k*k<=N:
        t[c*k*k]+= 1 if k==0 else 2; k+=1
    return t
from numpy.fft import rfft,irfft
def conv(a,b):
    L=1<<(2*N+2).bit_length(); r=irfft(rfft(a,L)*rfft(b,L),L)[:N+1]; return np.rint(r)
t12=conv(th(1),th(2)); A=conv(t12,th(8)); Bc=conv(t12,th(32))
s=np.ones(N+1,bool); s[:2]=0
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=0
ps=np.array([p for p in np.nonzero(s)[0] if p%4==1 and p>1000])
L2=np.log(ps)**2; y=R[ps]/L2
for cls in (1,5):
    m=ps%8==cls
    for name,v in (('A',A[ps]),('B',Bc[ps]),('A-2B',A[ps]-2*Bc[ps])):
        x=v[m]/np.sqrt(ps[m])
        print('p≡%d(8)'%cls,name,'corr with R/L²: %.3f'%np.corrcoef(x,y[m])[0,1] if x.std()>0 else 'const', 'n=%d'%m.sum())
# squares: A at odd squares nonzero while R = 0
sq=[m*m for m in range(31,300,2)]
print('odd squares: R=0 all?',all(R[n]==0 for n in sq),' min A at odd squares',min(A[n] for n in sq))
# Z2030: does R/2 mod 2 depend on (A mod 8, B mod 8) for p = 1 (8)?
m=ps%8==1
from collections import Counter
c=Counter()
for p in ps[m]:
    c[(int(A[p])%8,int(Bc[p])%8,int(R[p]//2)%2)]+=1
keys=sorted(set(k[:2] for k in c))
for k in keys:
    a,b=c[k+(0,)],c[k+(1,)]
    if a+b>50: print(k,'R/2 even',a,'odd',b,'frac odd %.2f'%(b/(a+b)))
