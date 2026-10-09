"""R121B: EVIDENCE check of black box (B3): |S_chi(m,n;c)| <= C_W tau(c)^{B_W} (m,n,c)^{1/2} (c r)^{1/2},
chi even mod r, r|c. Computes max ratio with C_W=1,B_W=1 over all c<=CMAX (FFT over (m,n))."""
import numpy as np, math, sys
from sympy import factorint, primitive_root, divisor_count
CMAX=int(sys.argv[1]) if len(sys.argv)>1 else 150
def local_chars(p,a):
    """list of (values dict on units mod p^a) for all chars mod p^a"""
    q=p**a; units=[u for u in range(q) if math.gcd(u,q)==1]
    if p!=2 or a<=2:
        if q==2: return [{1:1+0j}]
        g=primitive_root(q); n=len(units); log={}
        x=1
        for k in range(n): log[x]=k; x=x*g%q
        return [{u:np.exp(2j*np.pi*j*log[u]/n) for u in units} for j in range(n)]
    # 2^a, a>=3: u = (-1)^e 5^k
    n2=q//4; log={}
    for e in range(2):
        x=1
        for k in range(n2):
            log[((-1)**e*x)%q]=(e,k); x=x*5%q
    return [{u:((-1)**(s*log[u][0]))*np.exp(2j*np.pi*t*log[u][1]/n2) for u in units} for s in range(2) for t in range(n2)]
def all_chars(r):
    if r==1: return [lambda d:1.0]
    fs=factorint(r); locs=[(p**a,local_chars(p,a)) for p,a in fs.items()]
    out=[[]]
    for q,L in locs: out=[o+[(q,ch)] for o in out for ch in L]
    return [ (lambda comb: (lambda d: np.prod([ch[d%q] for q,ch in comb])))(comb) for comb in out]
worst=(0,None)
for c in range(1,CMAX+1):
    units=[d for d in range(c) if math.gcd(d,c)==1]
    inv={d:pow(d,-1,c) for d in units} if c>1 else {0:0}
    if c==1: units=[0]
    G=np.array([[math.gcd(math.gcd(m,n),c) for n in range(c)] for m in range(c)],dtype=float)
    tau=divisor_count(c)
    for r in [r for r in range(1,c+1) if c%r==0]:
        for chi in all_chars(r):
            if r>1 and abs(chi(r-1)-1)>1e-9: continue  # even only
            Mx=np.zeros((c,c),dtype=complex)
            for d in units: Mx[inv[d],d]=np.conj(chi(d)) if r>1 else 1
            # S(m,n)=sum_d conj(chi(d)) e((m dbar + n d)/c) = c^2 * ifft2(Mx)[m,n]
            S=np.fft.ifft2(Mx)*c*c
            ratio=np.abs(S)/(tau*np.sqrt(G)*math.sqrt(c*r))
            m=ratio.max()
            if m>worst[0]: worst=(m,(c,r))
print("CMAX",CMAX,"max |S_chi|/(tau(c)(m,n,c)^{1/2}(cr)^{1/2}) =",worst)
