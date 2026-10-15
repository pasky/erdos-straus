"""se_ff_rate.py (O219): O216 fs_rate.py + Coppersmith interpolation (FF twin of STERILE_EXPLICIT Cor 1.4) + divisibility-averaged pair routes (R5aA, R5bA, R10A, R9A). Grid EVIDENCE only.
fs_rate.py (O216): continuum optimiser (grid) for the per-s Case B exponent max_p min_route phi(p) - 1/2 (units of log q), routes of FF_STERILE_PUSH Lemma 1.6 with asymptotic Coppersmith thresholds. EVIDENCE/steering only; the rigorous version is fs_tail.c. usage: fs_rate.py r[,r..] [cop=1]"""
import numpy as np, sys
from math import log
def H(p):
  if p<=0 or p>=1: return 0.0
  return -p*log(p)-(1-p)*log(1-p)
def Hm(*ps): return -sum(p*log(p) for p in ps if p>0)
COP=True
def ok(n,d,rho,both=True):
  if n<=0: return False
  if d<rho-1e-12: return True
  if both and n-d<rho-1e-12: return True
  if 3*rho>n+1e-9: return True
  if COP:
    if rho>d*(n-d)/n+1e-9: return True
  return False
def okE(n,d,rho):  # E-version only (cofactor class maybe non-unit)
  if d<rho-1e-12: return True
  if 3*rho>n+1e-9: return True
  if COP and rho>d*(n-d)/n+1e-9: return True
  return False
def routes(a,z,y,t,lq):
  b=y+t; dE=a+y+z; dEp=b+y+z
  R={'R1':t+Hm(a,b,z)/lq,'T0':1-t,'R4p':1-y,'X1':1-a,'X2':1-z,
     'R2':y+z+(1+2*y+z)*H(dE/(1+2*y+z))/lq,'R3':a+y+(1+y)*H(dE/(1+y))/lq,'R4':a+z+H(dE)/lq,
     'R3C':b+y+(1+y)*H(dEp/(1+y))/lq,'R4C':b+z+(z+2*b)*H(t/(z+2*b))/lq,
     'R8a':y+t+H(a)/lq,'R8b':y+t+H(b)/lq,'R9a':z+t+(1-z)*H(a/(1-z))/lq}
  if ok(1+2*y+z,dE,y+z): R['R2c']=y+z
  if okE(1+y,dE,a+y): R['R3c']=a+y
  if ok(1,dE,a+z): R['R4c']=a+z
  if okE(1+y,dEp,b+y): R['R3Cc']=b+y
  if ok(z+2*b,dEp,z+b): R['R4Cc']=b+z
  if ok(b+z,b,t): R['R5a']=t+a; R['R6a']=t+H(a)/lq
  if ok(a+z,a,t): R['R5b']=t+b; R['R6b']=t+H(b)/lq
  if ok(a+b,a,t): R['R10a']=t+z; R['R10b']=t+H(z)/lq
  def ci(n,d,rho,both=True):
    v=max(0.0,d*(n-d)/n-rho) if n>0 else 0.0
    return v
  # Coppersmith interpolation (FF analogue of STERILE_EXPLICIT Cor 1.4): pair + (d(n-d)/n - rho)^+
  R['R2i']=y+z+ci(1+2*y+z,dE,y+z); R['R3i']=a+y+ci(1+y,dE,a+y); R['R4i']=a+z+ci(1,dE,a+z)
  R['R3Ci']=b+y+ci(1+y,dEp,b+y); R['R4Ci']=b+z+ci(z+2*b,dEp,z+b)
  R['R5ai']=t+a+ci(b+z,b,t); R['R5bi']=t+b+ci(a+z,a,t); R['R10ai']=t+z+ci(a+b,a,t)
  # divisibility-averaged pairs (Z twin: Sum_a (E/a + 1)): #{(v1,w1): w1 | T^{s-2}+v1} <= q^{max(t,a)} etc.
  R['R5aA']=max(t,a)+min(ci(b+z,b,t),(b+z)*H(b/(b+z))/lq if b+z>0 else 0)
  R['R5bA']=max(t,b)+min(ci(a+z,a,t),(a+z)*H(a/(a+z))/lq if a+z>0 else 0)
  R['R10A']=max(t,z)+min(ci(a+b,a,t),(a+b)*H(a/(a+b))/lq if a+b>0 else 0)
  R['R9A']=max(t,z+a)
  return R
def opt(lq,G=60):
  best=(-9,None); g=np.linspace(0,1,G+1)
  for a in g:
    for z in g:
      if a+z>1: continue
      for y in g:
        t=1-a-z-y
        if t< -1e-12 or a>y+t+1e-12: continue
        v=min(routes(a,z,y,t,lq).values())
        if v>best[0]: best=(v,(a,z,y,t))
  return best
if __name__=='__main__':
  if len(sys.argv)>2: COP=bool(int(sys.argv[2]))
  for r in [int(x) for x in sys.argv[1].split(',')]:
    lq=r*log(3); v,p=opt(lq)
    R=routes(*p,lq)
    print(r,round(v-.5,4),[round(float(x),3) for x in p],' '.join('%s=%.3f'%(k,x) for k,x in sorted(R.items(),key=lambda kv:kv[1])[:6]),flush=True)
