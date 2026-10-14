# NON-RIGOROUS prototype of the per-box route sum for D_P(N) (floating point), to estimate constants.
import math, sys, functools
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR=primes(10**5)
def Ck(eta,kk):  # tau_kk(n) <= Ck * n^eta
    lc=0.0
    for p in PR:
        best=0.0; k=0
        while True:
            k+=1
            v=math.log(math.comb(k+kk-1,kk-1))-eta*k*math.log(p)
            if v>best: best=v
            if k>200 or (v<best-5 and k>10): break
        if best==0.0 and math.log(kk)-eta*math.log(p)<0: break
        lc+=best
    return lc
ETAS=[0.15,0.2,0.25,0.3,0.35,0.4,0.5]
LC2={e:Ck(e,2) for e in ETAS}; LC3={e:Ck(e,3) for e in ETAS}
def taub(ln,tab): return min(tab[e]+e*ln for e in ETAS)  # log bound
def cop(ln, ls, D0, D1, W=14):
    """log-free count bound for divisors of n (log n = ln) in a unit class mod s (log s = ls) within [D0,D1]."""
    if D1<D0: return 0.0
    Delta=D1-D0; s=math.exp(ls)
    best=math.floor(Delta/s)+1
    lD0=math.log(D0)
    for w in range(2,W+1):
        for m in range(1,w+1):
            Lmax=(m*w*lD0 - w*math.log(w) - m*(m+1)/2*ln)/(w*(w-1)/2)
            if Lmax<=math.log(0.5)+1e-12: continue
            J=max(1,math.ceil(Delta/(2*s*(math.exp(Lmax)-0.5))*(1+1e-9)))
            best=min(best,J*(w-1))
    return best
def Lsum(A): return sum(1.0/a for a in range(A,2*A)) if A<64 else math.log(2)+1.0/(2*A)
def box(N,A,C,D):
    lN=math.log(N)
    b0,b1=N/(16*A*D),N/(2*A*D)
    E0,E1=N/(32*A*C*D),N/(A*C*D)
    if E1<1 or 2*A*A*D>N: return 0.0,'-'
    E0=max(E0,0.0); f0,f1=4*A*C*D-1,32*A*C*D
    R={}
    R['H']=A*C*D
    R['A']=(E1-E0)/4*Lsum(A)*Lsum(D)+A*D
    nC=math.log(3*N); R['C']=A*D*min(cop(nC,math.log(4*A*D),f0,f1), (E1/(4*A*D))+1, math.exp(taub(nC,LC2)))
    nD=math.log(32*C*C*D*N+1); R['D']=C*D*min(cop(nD,math.log(4*C*D),f0,f1),math.exp(taub(nD,LC2)))
    nE=math.log(2*C*N+2*A); R['E']=A*C*min(cop(nE,math.log(4*A*C),f0,f1),math.exp(taub(nE,LC2)))
    pairF=(E1-E0)/4*Lsum(A)+A; nF=math.log((N+E1)/(4*A)); sF=math.log(max(E0,1))
    R['F']=pairF*min(cop(nF,sF,max(b0,1),b1),cop(nF,sF,D,2*D),D/max(E0,1)+1,math.exp(taub(nF,LC2)))
    pairG=(E1-E0)/4*Lsum(D)+D; nG=math.log((N+E1)/(4*D)); om=2**len([p for p in PR[:12] if math.prod(PR[:PR.index(p)+1])<=E1])
    R['G']=pairG*om*min(cop(nG,sF,A,2*A),cop(nG,sF,max(b0,1),b1),A/max(E0,1)+1,math.exp(taub(nG,LC2)))
    R['tau3']=((E1-E0)/4+1)*math.exp(taub(math.log((N+E1)/4),LC3))
    R['I']=C*pairF; R['J']=2*C*pairG*om
    k=min(R,key=R.get); return R[k],k
def DP(N,full=False):
    tot=0.0; who={}
    L=int(math.log2(N))+1
    for i in range(L):
        A=2**i
        if 2*A*A>N: break
        for l in range(L):
            D=2**l
            if 2*A*A*D>N: break
            for j in range(L):
                C=2**j
                if A*C*D>N: break
                v,k=box(N,A,C,D); tot+=v; who[k]=who.get(k,0)+v
    return tot,who
if __name__=='__main__':
    for N in map(eval,sys.argv[1:]):
        t,w=DP(N); print(N, '%.3e'%t, 'N^0.4=%.3e'%(N**0.4), {k:'%.2e'%v for k,v in sorted(w.items(),key=lambda x:-x[1])})
