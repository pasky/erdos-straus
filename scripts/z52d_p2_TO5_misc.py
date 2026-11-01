"""z52d_p2_TO5_misc.py — numerics for several TO5 items (see outcome_TO5.jsonl for mapping).
(a) Z1687  period of CF(sqrt p) vs R/M_BM ; (b) Z1742 greedy (Fibonacci-Sylvester) length of 4/p vs R/M ;
(c) Z1760 least-squares fit of M0(p) = a L^2 + b L + c (L = log p) ; (d) Z1824 corr(R/M, tau(p+1), tau3(p+1)) ;
(e) Z1823/Z1691/Z1916 divisor residues mod 4C of N=4Cp+1 (C<=30): |D|/phi(4C), -1 in D, subgroup gen. by prime classes ;
(f) Z1838 cell (3/p)(5/p)(7/p) all +1 fraction and hardness; (g) Z1839 least quadratic non-residue n2(p) max ;
(h) Z1926/Z1925 criterion check: B=1 slice success <=> (p+1)/2 has a prime factor ≡3 mod 4 ;
(i) Z1856/Z1927: slice-B success for B<=6 via p+B having a divisor ≡ -1 (mod 4B); joint failure vs product ;
(j) Z1787: number of trial pairs for p=409.  usage: python3 scripts/z52d_p2_TO5_misc.py"""
import math, collections, random, statistics as st
D='data/z52b/pass2/TO5/'
NM=10**6+10
spf=list(range(NM+1))
for i in range(2,int(NM**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,NM+1,i):
            if spf[j]==j: spf[j]=i
def factor(n):
    f={}
    while n>1:
        p=spf[n]; f[p]=f.get(p,0)+1; n//=p
    return f
def tfactor(n):  # trial division (for N > spf range)
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1 if d==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f
def divisors(f):
    ds=[1]
    for p,e in f.items(): ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
isprime=[False]*2+[True]*(NM-1)
for i in range(2,int(NM**0.5)+1):
    if isprime[i]:
        for j in range(i*i,NM+1,i): isprime[j]=False
mbm={}
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6: continue
    n,isp,R,M0,MB=int(a[0]),int(a[1]),int(a[2]),float(a[3]),float(a[4])
    if isp and n%4==1 and n>=5 and MB>0: mbm[n]=(R,M0,MB)
P=sorted(mbm)
def corr(x,y):
    mx,my=st.mean(x),st.mean(y); sx=math.sqrt(sum((a-mx)**2 for a in x)); sy=math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(sx*sy)
# (a) CF period of sqrt(p)
def cf_period(n):
    a0=int(math.isqrt(n)); m,d,a=0,1,a0; per=0
    while True:
        m=d*a-m; d=(n-m*m)//d; a=(a0+m)//d; per+=1
        if a==2*a0: break
    return per
Ps=[p for p in P if p<=10**5]
per=[cf_period(p) for p in Ps]; rr=[mbm[p][0]/mbm[p][2] for p in Ps]
print("(a) Z1687 corr(period(sqrt p), R/M) over p≡1(4) ≤1e5: %+.4f (n=%d)"%(corr([math.log(x) for x in per],rr),len(Ps)))
print("    parity: %d of %d periods odd (for prime p≡1 mod 4 the period is always odd: N(eps)=-1)"%(sum(q%2 for q in per),len(per)))
# size-controlled: partial correlation with log p (residualise both on log p)
lp=[math.log(p) for p in Ps]
def resid(y,x):
    mx,my=st.mean(x),st.mean(y); b=sum((a-mx)*(c-my) for a,c in zip(x,y))/sum((a-mx)**2 for a in x)
    return [c-(my+b*(a-mx)) for a,c in zip(x,y)]
lpp=[math.log(q) for q in per]
print("    partial corr(log period, R/M | log p) = %+.4f"%corr(resid(lpp,lp),resid(rr,lp)))
print("    corr(log period, log p) = %+.4f ; corr(R/M, log p) = %+.4f"%(corr(lpp,lp),corr(rr,lp)))
# (b) greedy Egyptian expansion length of 4/p (Fibonacci-Sylvester): x_1 = ceil(p/4), then remainder
def greedy_len(p):
    num,den=4,p; L=0
    while num>0:
        x=-(-den//num); L+=1
        num,den=num*x-den, den*x
        g=math.gcd(num,den)
        if g>1: num//=g; den//=g
        if L>50: break
    return L
gl=[greedy_len(p) for p in Ps]

print("(b) Z1742 greedy length of 4/p over p≡1(4) ≤1e5: distribution",dict(sorted(collections.Counter(gl).items())),"; corr with R/M %+.4f"%corr([float(x) for x in gl],rr))
lp_=[math.log(p) for p in Ps]
def _res(y,x):
    mx,my=st.mean(x),st.mean(y); b=sum((a-mx)*(c-my) for a,c in zip(x,y))/sum((a-mx)**2 for a in x)
    return [c-(my+b*(a-mx)) for a,c in zip(x,y)]
print("    partial corr(greedy length, R/M | log p) = %+.4f"%corr(_res([float(x) for x in gl],lp_),_res(rr,lp_)))
# (c) M0 fit
Pf=[p for p in P if p>=10**3]
X=[[math.log(p)**2, math.log(p), 1.0] for p in Pf]; Y=[mbm[p][1] for p in Pf]
# normal equations
A=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)]
b=[sum(x[i]*y for x,y in zip(X,Y)) for i in range(3)]
def solve3(A,b):
    import copy
    M=[row[:]+[bb] for row,bb in zip(A,b)]
    for i in range(3):
        piv=max(range(i,3),key=lambda r:abs(M[r][i])); M[i],M[piv]=M[piv],M[i]
        for r in range(3):
            if r!=i:
                f=M[r][i]/M[i][i]
                for c in range(i,4): M[r][c]-=f*M[i][c]
    return [M[i][3]/M[i][i] for i in range(3)]
a_,b_,c_=solve3(A,b)
print("(c) Z1760 fit M0(p)=a L^2+b L+c over p∈[1e3,1e6]: a=%.5f (3/(2pi^2)=%.5f) b=%.4f c=%.4f"%(a_,3/(2*math.pi**2),b_,c_))
# (d) tau(p+1), tau3(p+1)
def tau3(n):
    f=factor(n); r=1
    for p,e in f.items():
        # tau3(p^e) = C(e+2,2)
        r*= (e+1)*(e+2)//2
    return r
def tau(n):
    f=factor(n); r=1
    for p,e in f.items(): r*=e+1
    return r
t1=[math.log(tau(p+1)) for p in Ps]; t3=[math.log(tau3(p+1)) for p in Ps]
print("(d) Z1824 corr(R/M, log tau(p+1)) %+.4f ; corr(R/M, log tau3(p+1)) %+.4f (n=%d)"%(corr(t1,rr),corr(t3,rr),len(Ps)))
# (e) divisor residues mod 4C of N=4Cp+1 (C<=30) ; subgroup generated by prime-factor classes
def units(m): return [a for a in range(1,m) if math.gcd(a,m)==1]
hard=[p for p in P if mbm[p][0]/mbm[p][2]<0.25]
fails=[p for p in P if mbm[p][0]==0]
def subgroup_gen(gens,m):
    H={1}
    frontier=[1]
    while frontier:
        x=frontier.pop()
        for g in gens:
            y=(x*g)%m
            if y not in H: H.add(y); frontier.append(y)
    return H
for name,S in (('hard(R/M<0.25)',hard),('(★)-failures',fails)):
    tot=0; minusone=0; fullD=0; sg_has_m1=0; cnt=0; ratio=[]
    for p in S:
        for C in range(1,31):
            m=4*C; N=m*p+1
            f=tfactor(N)
            ds=divisors(f)
            Dres={d%m for d in ds if d%m!=1 or True}
            Dres={d%m for d in ds}
            Du={d for d in Dres if math.gcd(d,m)==1}
            cnt+=1
            ratio.append(len(Du)/len(units(m)))
            if (m-1) in Du: minusone+=1
            if len(Du)==len(units(m)): fullD+=1
            gens=[q%m for q in f if math.gcd(q,m)==1]
            if (m-1) in subgroup_gen(gens,m): sg_has_m1+=1
    print("(e) %s: slices (p,C) = %d ; mean |D|/phi(4C)=%.3f ; -1 in divisor residues: %d (%.3f) ; full unit group: %d ; -1 in subgroup gen by prime classes: %d (%.3f)"%(name,cnt,st.mean(ratio),minusone,minusone/cnt,fullD,sg_has_m1,sg_has_m1/cnt))
# (f) Legendre cell (3/p)(5/p)(7/p)
def leg(q,p): return 1 if pow(q,(p-1)//2,p)==1 else -1
cell_all=sum(1 for p in P if leg(3,p)==1 and leg(5,p)==1 and leg(7,p)==1)
cell_hard=[p for p in hard if leg(3,p)==1 and leg(5,p)==1 and leg(7,p)==1]
print("(f) Z1838 all-QR cell (3,5,7) fraction among p≡1(4) ≤1e6: %.4f ; hard primes in cell: %d of %d hard"%(cell_all/len(P),len(cell_hard),len(hard)))
# (g) least quadratic non-residue n2(p)
def n2(p):
    q=2
    while True:
        if isprime[q] and q!=p and leg(q,p)==-1: return q
        q+=1
ns=[n2(p) for p in P if p>=5 and p<=2*10**5]
print("(g) Z1839 n2(p) over p≡1(4) ≤2e5: max %d ; mean %.2f ; max/log^2 p %.3f"%(max(ns),st.mean(ns),max(n2(p)/math.log(p)**2 for p in P if p>=5 and p<=2*10**5)))
# (h) B=1 criterion: B=1 slice succeeds <=> (p+1)/2 has a prime factor ≡3 (mod 4)
agree=0; tot_=0
certn1={}
for l in open(D+'certs2_1e6.txt'):
    a=list(map(int,l.split())); certn1[a[0]]=a[4]
for p in P:
    h=(p+1)//2
    crit=any(q%4==3 for q in factor(h))
    succ=certn1[p]>0
    tot_+=1; agree+= (crit==succ)
print("(h) Z1926 B=1 criterion agreement over %d primes p≡1(4) ≤1e6: %d (%.5f)"%(tot_,agree,agree/tot_))
# (i) shift-form slices: B-slice success iff p+B has a divisor ≡ -1 (mod 4B)
def slice_succ(p,B):
    f=factor(p+B)
    return any(d%(4*B)==4*B-1 for d in divisors(f) if d>1)
Bs=range(1,7)
S=[p for p in P]
succ={B:0 for B in Bs}; joint_fail=0; allfail_B={B:0 for B in Bs}
for p in S:
    res=[slice_succ(p,B) for B in Bs]
    for B,r in zip(Bs,res): succ[B]+=r
    if not any(res): joint_fail+=1
    for B,r in zip(Bs,res):
        if not r: allfail_B[B]+=1
n=len(S)
prodfail=1.0
for B in Bs: prodfail*=allfail_B[B]/n
print("(i) Z1856/Z1927 shift-slice success rates p≡1(4)≤1e6: "+", ".join("B=%d %.4f"%(B,succ[B]/n) for B in Bs))
print("    joint failure of B=1..6: %.6f ; product of marginal failures: %.6f ; ratio %.2f"%(joint_fail/n,prodfail,(joint_fail/n)/prodfail if prodfail>0 else float('nan')))
# (j) trial pairs for p=409
p=409
pairs=[(u,B) for u in range(1,p) for B in range(1,p) if math.gcd(u,B)==1 and (u+B)%2==1 and 4*u*B-u-B<=p]
def phi(n):
    return sum(1 for a in range(1,n+1) if math.gcd(a,n)==1)
print("(j) Z1787 p=409: trial pairs in P(409): %d ; distinct moduli 4uB: %d ; M0=sum 1/phi(4uB)=%.4f (z38_mbm: 5.1506)"%(len(pairs),len({4*u*B for u,B in pairs}),sum(1/phi(4*u*B) for u,B in pairs if p%(4*u*B)!=0)))
