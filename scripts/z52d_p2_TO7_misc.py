# Z2440 (absorbing gadget: aux slices always contain a solvable member?), Z2586 (Halász max-character ratio for failing M),
# Z2805 (CRT union of fixed-(t,u) families p ≡ -u mod (tu-1)), Z2855 (bounded-generator Schreier graph on P^1(F_p)),
# Z2870 (joint failure of levels t in {3,4,6,8,12}), Z2878 (primitive solution counts P(m)), Z2445 (degrees of ES parametrisations), Z2778 (main term)
import sys, math, random
from collections import Counter
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_TO7_load import load, bits
which=sys.argv[1]
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; nI=tsv['nI']; nII=tsv['nII']; minI=tsv['minI']
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
if which=='Z2440':
    H=nI[hard]
    print(f"Z2440 hard primes ≤1e6 (n={len(H)}): min #successful Type-I slices among k≤399 = {H.min()}, #primes with nI≤2: {(H<=2).sum()}, nI=0 count {(H==0).sum()}")
    for K in [15,31,63,127]:
        a=load(); B=bits(a)
        m0=(a['type']==0)&(a['k']<=K)&np.isin(a['p'],P[hard])
        cnt=Counter(a['p'][m0][B['dh'][m0]].tolist())
        allp=set(P[hard].tolist())
        zero=sum(1 for p in allp if cnt.get(p,0)==0)
        print(f"  aux family = Type-I slices k≤{K}: hard primes with no solvable member = {zero}/{len(allp)} = {zero/len(allp):.4f}")
if which=='Z2586':
    from z52d_p2_TO7_load import load as ld
    a=ld(); B=bits(a)
    spf=np.zeros(250001,dtype=np.int64)
    for i in range(2,501):
        if spf[i]==0:
            idx=np.arange(i*i,250001,i); m=spf[idx]==0; spf[idx[m]]=i
    def divisors_tau(n):
        ds=[1]; m=n
        while m>1:
            q=int(spf[m]) or m; e=0
            while m%q==0: m//=q; e+=1
            ds=[d*q**j for d in ds for j in range(e+1)]
        return ds
    out={}
    for k in [19,23,31]:
        # primitive root mod k
        g=next(g for g in range(2,k) if all(pow(g,(k-1)//q,k)!=1 for q in range(2,k) if (k-1)%q==0 and all(q%r for r in range(2,q))))
        logt={pow(g,j,k):j for j in range(k-1)}
        sel=(a['type']==1)&(a['k']==k)&(~B['dh'])&(a['p']>=1000)&(a['p']<=250000)
        vals_fail=[]; vals_rand=[]
        rng=random.Random(2)
        for p,ok in zip(a['p'][sel][:800],np.ones(sel.sum(),bool)[:800]):
            M=(int(p)+k)//4
            if M<2 or M>250000: continue
            D=divisors_tau(M); tau=len(D)
            best=0
            for s in range(1,k-1):
                tot=0
                for d in D:
                    if d%k==0: continue
                    tot+=np.exp(2j*np.pi*s*logt[d%k]/(k-1))
                best=max(best,abs(tot))
            vals_fail.append(best/tau)
            # random control: divisors of random integer of same size with dh-analogue ignored
            R=rng.randrange(M//2,M)
            Dr=divisors_tau(R); best=0
            for s in range(1,k-1):
                tot=sum(np.exp(2j*np.pi*s*logt[d%k]/(k-1)) for d in Dr if d%k)
                best=max(best,abs(tot))
            vals_rand.append(best/len(Dr))
        print(f"Z2586 k={k}: failing (no a=1 witness) Type-II M, n={len(vals_fail)}: max_chi |sum_{{d|M}} chi(d)|/tau(M) mean {np.mean(vals_fail):.3f} median {np.median(vals_fail):.3f}; random-integer control mean {np.mean(vals_rand):.3f}")
if which=='Z2805':
    primes=[p for p in range(5,10**6) if isprime(p) and p%4==1][:]  # 78k primes
    primes=np.array([p for p in primes if p>1000][:20000])
    def cover_set(T):
        mods=[]
        for t in range(2,T+1):
            for u in range(2,T//t+1):
                mods.append((t*u-1,u))
        return mods
    for T in [10,30,100,300]:
        mods=cover_set(T)
        covered=np.zeros(len(primes),bool)
        for m,u in mods:
            covered|=((primes+u)%m==0)
        print(f"Z2805 T={T}: #(t,u) families={len(mods)}, uncovered density among primes p≡1(4), p∈(1e3,~2e5): {1-covered.mean():.5f}")
if which=='Z2855':
    # Schreier graph of generators g_b=[[1,b],[0,1]], h_b=[[1,0],[b,1]] (1≤b≤B) acting on P^1(F_p); distance from ∞ to QNR points (x/p)=-1 (x in F_p) 
    from collections import deque
    for p in [101,211,401,997]:
        qnr=set(x for x in range(1,p) if pow(x,(p-1)//2,p)==p-1)
        for Bd in [1,2,3,5,8]:
            # vertices: 0..p-1 (finite points x) and p (infinity)
            INF=p
            def act(M,v):
                a_,b_,c_,d_=M
                if v==INF:
                    if c_%p==0: return INF
                    return a_*pow(c_,-1,p)%p
                num=(a_*v+b_)%p; den=(c_*v+d_)%p
                if den==0: return INF
                return num*pow(den,-1,p)%p
            gens=[]
            for b in range(1,Bd+1):
                gens.append((1,b,0,1)); gens.append((1,0,b,1))
            dist={INF:0}; dq=deque([INF]); hit=None
            while dq:
                v=dq.popleft()
                if v!=INF and v in qnr: hit=dist[v]; break
                for M in gens:
                    w=act(M,v)
                    if w not in dist: dist[w]=dist[v]+1; dq.append(w)
            print(f"Z2855 p={p} B={Bd}: distance from ∞ to nearest QNR point = {hit}")
if which=='Z2870':
    a=load()
    levels=[3,4,6,8,12]
    def has_level(p,t):
        # exists u,v>=2 with t*u*v-u-v = p
        for u in range(2,p+2):
            if u*(t*2)-u-2 > p and u>2: break
            for v in range(2,p+2):
                s=p+u+v
                if u*v*t>s: break
                if s%(u*v)==0 and s//(u*v)==t: return True
        return False
    ps=[int(p) for p in P if p>=1000 and p<=20000][:400]
    fails=Counter(); allfail=0
    for p in ps:
        f=[t for t in levels if not has_level(p,t)]
        for t in f: fails[t]+=1
        allfail+= (len(f)==len(levels))
    n=len(ps)
    print(f"Z2870 primes p∈[1e3,2e4) sample n={n}: failure freq per level {{t: frac}} = {{ {', '.join(f'{t}:{fails[t]/n:.3f}' for t in levels)} }}; all five levels fail: {allfail} ({allfail/n:.4f})")
if which=='Z2878':
    # primitive solutions of 4/m = 1/x+1/y+1/z with gcd(x,y,z)=1; P(m) for m≤120, and all solutions F(m)
    from math import gcd
    def sols(m):
        out=[]
        for x in range(m//4+1, 3*m//4+2):
            # 1/y+1/z = 4/m-1/x = (4x-m)/(m x)
            num=4*x-m; den=m*x
            if num<=0: continue
            for y in range(x, 2*den//num+2):
                rem_num=num*y-den
                if rem_num<=0: continue
                z_num=den*y
                if z_num%rem_num==0:
                    z=z_num//rem_num
                    if z>=y: out.append((x,y,z))
        return out
    Pm={}; Fm={}
    for m in range(2,121):
        S=sols(m); Fm[m]=len(S); Pm[m]=sum(1 for (x,y,z) in S if gcd(gcd(x,y),z)==1)
    prime_vals=[(m,Pm[m]) for m in range(2,121) if all(m%d for d in range(2,int(m**.5)+1))]
    comp_vals=[(m,Pm[m]) for m in range(4,121) if not all(m%d for d in range(2,int(m**.5)+1))]
    print("Z2878 P(m) at primes (m,P):",prime_vals[:12])
    print("Z2878 P(m) at composites m=..:",comp_vals[:12])
    print("Z2878 mean P at primes", round(np.mean([v for _,v in prime_vals]),3), "mean P at composites", round(np.mean([v for _,v in comp_vals]),3))
    # Möbius: F(m)=sum_{d|m} P(m/d)?  test identity F(m)=sum over k|m of P(m/k) (solutions of 4/m scaled from primitive ones of 4/(m/k)? check)
    bad=0
    for m in range(2,121):
        s=sum(Pm[m//k] for k in range(1,m+1) if m%k==0 and m//k>=2)
        if s!=Fm[m]: bad+=1
    print("Z2878 identity F(m)=sum_{k|m} P(m/k) (k=m/d) violations among m≤120:", bad)
if which=='Z2445':
    import sympy as sp
    c,f,g,d,b,t,nn=sp.symbols('c f g d b t n',integer=True)
    # Lemma 1.1 parametrisation: d=(fg-1)/4, b=(n+c)/f with n=c(fg-1)-f ; denominators of Type-I solution (b d n, c d, b c d)
    n_expr=c*(f*g-1)-f
    dd=(f*g-1)/4; bb=(n_expr+c)/f
    dens=[sp.simplify(bb*dd*n_expr), sp.simplify(c*dd), sp.simplify(bb*c*dd)]
    for e in dens:
        num,den=sp.fraction(sp.together(e))
        print("Z2445 denominator:", sp.factor(e), " total degree of numerator:", sp.Poly(sp.expand(num),c,f,g).total_degree() if num.is_polynomial(c,f,g) else 'n/a')
    # Type-II slice a=1 (Lemma 1.2): n is fixed prime p, e, b with b | (p+e)/4: denominators (a b d, a c d n, b c d n) -> degrees
    print("Z2445 type-II Lemma 1.2 denominators (abd, acdn, bcdn) are products of parameters with n: degree in parameters ≥2 (no linear system unless e fixed)")
if which=='Z2778':
    # main term of mean r(n) over n≤N: sum_{u,v≥3, uv≤N} 1/(uv)  (triples with t≥3 per (u,v) contribute ~N/(uv) to the N values)
    N=10**7
    S=0.0
    for u in range(3,N):
        if 9*u>N: break
        vmax=N//(3*u)
        S+=sum(1.0/(u*v) for v in range(3,min(vmax,N)+1))
    print(f"Z2778 Σ_{{u,v≥3, 3uv≤N}} 1/(uv) for N=1e7 = {S:.3f} (observed mean r over n≤1e7 ≈ 83 at top bin; check: (log N)^2/2 = {math.log(N)**2/2:.1f})")
