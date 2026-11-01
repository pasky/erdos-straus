"""z52d_p2_TO5_fix3.py — lint-fix round for TO5: Z1812/Z1813 (4/(kp) solutions), Z1910 (Z[T] identities),
Z1940 (signed identities, odd squares), Z1946 (Type I/II counts), Z1712 (curve premise + model check), Z1734 (random
multiplicative model), Z1773 (search-order programs), Z1730 (slope), Z1896 (fixed points of the swap involution).
usage: python3 scripts/z52d_p2_TO5_fix3.py  (memory: small arrays; runtime ~ minutes)"""
import math, collections, itertools, statistics as st, random
import numpy as np
D='data/z52b/pass2/TO5/'
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
def sols_3term(N, num=4, signed=False, cap=None):
    """all positive solutions x<=y<=z of num/N = 1/x+1/y+1/z (signed=False)"""
    out=[]
    x0=-(-N//num)            # x >= N/num
    for x in range(x0, 3*N//num+2):
        # rem = num/N - 1/x = (num*x - N)/(N*x)
        rn=num*x-N; rd=N*x
        if rn<=0: continue
        y0=max(x, -(-rd//rn))
        y1=(2*rd)//rn
        for y in range(y0, y1+1):
            # 1/z = rn/rd - 1/y = (rn*y - rd)/(rd*y)
            zn=rn*y-rd
            if zn<=0: continue
            if (rd*y)%zn==0:
                z=rd*y//zn
                if z>=y: out.append((x,y,z))
    return out
# ---------- Z1812 / Z1813: 4/(kp) three-term solutions and descent ----------
print("== Z1812/Z1813: solutions of 4/(kp)=1/x+1/y+1/z, x<=y<=z, for small p and k; 'descent' = k | x,y,z (gives a 4/p solution)")
for p in (13,17,29,37,53,409):
    row=[]
    for k in range(1,21 if p<100 else 8):
        N=k*p
        if N>3000 and p>100: break
        S=sols_3term(N)
        desc=[s for s in S if all(t%k==0 for t in s)] if k>1 else S
        nontriv=[s for s in S if not all(t%k==0 for t in s)]
        row.append((k,len(S),len(desc),len(nontriv)))
    print("  p=%d: (k, #sols, #descent (k|all), #non-descent): %s"%(p,row[:12]))
# ---------- Z1910: identities over Z[T] with x,y,z linear, n quadratic: 4xyz = n(xy+yz+zx) ----------
print("== Z1910: polynomial identities 4xyz = n(T)(xy+yz+zx) over Z[T], x,y,z linear (coeffs in [-3,3]), n quadratic (coeffs in [-3,3], lead≠0)")
lin=[(a,b) for a in range(-3,4) for b in range(-3,4)]           # a*T+b
def pmul(p1,p2): # coeff lists low->high
    r=[0]*(len(p1)+len(p2)-1)
    for i,x in enumerate(p1):
        for j,y in enumerate(p2): r[i+j]+=x*y
    return r
def padd(*ps):
    L=max(len(p) for p in ps); r=[0]*L
    for p in ps:
        for i,x in enumerate(p): r[i]+=x
    return r
found=[]
quads=[(c,b,a) for a in range(-3,4) for b in range(-3,4) for c in range(-3,4) if a!=0]
T=[(b,a) for (a,b) in lin]   # as (const, T) lists
Xs=[[b,a] for (a,b) in lin]
# precompute products pairwise
cnt=0
for xi,X in enumerate(Xs):
    for yi,Y in enumerate(Xs):
        if yi<xi: continue
        for zi,Z in enumerate(Xs):
            if zi<yi: continue
            lhs=[4*c for c in pmul(pmul(X,Y),Z)]
            rhs2=padd(pmul(X,Y),pmul(Y,Z),pmul(X,Z))
            for q in quads:
                rhs=pmul(list(q),rhs2)
                L=max(len(lhs),len(rhs))
                d=padd(lhs+[0]*(L-len(lhs)), [-x for x in rhs]+[0]*(L-len(rhs)))
                if all(v==0 for v in d):
                    cnt+=1
                    if len(found)<5: found.append((X,Y,Z,q))
print("  identities found:", cnt, "; examples (x,y,z as [const,T] ; n as [const,T,T^2]):", found[:5])
# ---------- Z1940: signed identities 4xyz = n(yz+xz-xy) (i.e. 4/n = 1/x+1/y-1/z), linear x,y,z, n quadratic ----------
print("== Z1940: signed identities 4/n = 1/x+1/y-1/z over Z[T] (x,y,z linear, coeffs [-3,3]; n quadratic [-3,3])")
cnt=0; ex=[]
for X in Xs:
    for Y in Xs:
        for Z in Xs:
            lhs=[4*c for c in pmul(pmul(X,Y),Z)]
            rhs2=padd(pmul(Y,Z),pmul(X,Z),[-c for c in pmul(X,Y)])
            for q in quads:
                rhs=pmul(list(q),rhs2)
                L=max(len(lhs),len(rhs))
                d=padd(lhs+[0]*(L-len(lhs)), [-x for x in rhs]+[0]*(L-len(rhs)))
                if all(v==0 for v in d):
                    cnt+=1
                    if len(ex)<3: ex.append((X,Y,Z,q))
print("  signed identities found:", cnt, "; examples:", ex)
# odd squares: signed solutions with x,y,z <= 4n (finite search) vs positive solutions
def signed_sols(n, bound):
    out=[]
    for x in range(1,bound+1):
        for y in range(1,bound+1):
            # 1/z = 1/x + 1/y - 4/n
            num=n*(x+y)-4*x*y; den=4*x*y
            if num<=0: continue
            if den % num==0 or True:
                z=den/num
                if abs(z-round(z))<1e-12 and round(z)>=1 and round(z)<=bound: out.append((x,y,round(z)))
    return out
for n in (9,25,49,81):
    s=signed_sols(n,4*n)
    print("  n=%d (odd square): signed solutions with x,y,z<=4n: %d, e.g. %s"%(n,len(s),s[:3]))
print("  n=9: 4/9 = 1/3 + 1/6 - 1/18 ✓ (T1 is broken by the sign: all three denominators positive but one term negative)")
# ---------- Z1946: Type I / Type II counts f_I, f_II for small p (all positive solutions) ----------
print("== Z1946: Type I (p divides exactly one denominator) vs Type II (exactly two) counts, p≡1(4), p≤500")
rows=[]
for p in [q for q in range(5,501) if q%4==1 and all(q%d for d in range(2,int(q**0.5)+1))]:
    S=sols_3term(p)
    fI=sum(1 for s in S if sum(1 for t in s if t%p==0)==1)
    fII=sum(1 for s in S if sum(1 for t in s if t%p==0)==2)
    f3=sum(1 for s in S if sum(1 for t in s if t%p==0)==3)
    rows.append((p,len(S),fI,fII,f3,mbm[p][0]))
print("  primes:",len(rows),"; all-three-divisible count (should be 0):",sum(r[4] for r in rows))
fI=[r[2] for r in rows]; fII=[r[3] for r in rows]; Rv=[r[5] for r in rows]
print("  corr(f_I, f_II) = %+.4f ; corr(f_I, R) = %+.4f ; corr(f_II, R) = %+.4f"%(corr(fI,fII),corr(fI,Rv),corr(fII,Rv)))
nl=[math.log(r[0])**3 for r in rows]
print("  corr(f_I/log^3p, f_II/log^3p) = %+.4f ; mean f_I/log^3p = %.3f ; mean f_II/log^3p = %.3f"%(corr([a/b for a,b in zip(fI,nl)],[a/b for a,b in zip(fII,nl)]), st.mean([a/b for a,b in zip(fI,nl)]), st.mean([a/b for a,b in zip(fII,nl)])))
print("  R=0 primes among these: ", [r[0] for r in rows if r[5]==0], " their f_I,f_II:", [(r[2],r[3]) for r in rows if r[5]==0])
# ---------- Z1712: curve premise: distinct N per prime; model check C_N vs E_N ----------
print("== Z1712: E_N model check and premise (N = 4(x+y+z)/p depends on the solution, not on n alone)")
def legen(a,q): a%=q; return 0 if a==0 else (1 if pow(a,(q-1)//2,q)==1 else -1)
def count_E(N,q):  # Y^2 = X(X^2+(N^2-6N-3)X+16N) over F_q, affine+infinity
    A=(N*N-6*N-3)%q; B=(16*N)%q; c=1
    for x in range(q):
        c+=1+legen(x*(x*x+A*x+B),q)
    return c
def count_C(N,q):  # (x+y+z)(xy+yz+zx) = N xyz projective over F_q
    c=0
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if x==y==z==0: continue
                if (x+y+z)*(x*y+y*z+z*x)-N*x*y*z ==0 and True: pass
    # projective count: divide by (q-1)
    tot=0
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if (x,y,z)==(0,0,0): continue
                if ((x+y+z)*(x*y+y*z+z*x)-N*x*y*z)%q==0: tot+=1
    return tot//(q-1)
ok=0; tot=0
for q in (5,7,11,13):
    for N in range(2,q):
        if N%q in (0,1,9%q): continue
        tot+=1
        if count_C(N,q)==count_E(N,q): ok+=1
print("  C_N vs E_N point counts agree for %d of %d (N,q) pairs with q∈{5,7,11,13}"%(ok,tot))
for p in (5,13,17,29,37,41):
    S=sols_3term(p)
    Ns=set(sum(s)*4 for s in S)
    print("  p=%d: %d solutions -> %d distinct N=4(x+y+z)/p values (as multiples of 1/p): e.g. %s"%(p,len(S),len(Ns),sorted(Ns)[:4]))
# ---------- Z1734: random multiplicative model vs T(p) ----------
print("== Z1734: T(p) vs random-multiplicative model (Rademacher f replacing (-uB/p)=(uB/p) for p≡1 mod 4)")
import sys
Xmax=250000
spf=np.zeros(Xmax+1,dtype=np.int64)
for i in range(2,Xmax+1):
    if spf[i]==0:
        spf[i::i][spf[i::i]==0]=i
# weights W(m)=2^omega(m)/(4 phi(m)) for even m (pairs u,B coprime with uB=m, u+B odd ⇒ exactly one even) — as in z38_mbm
phi=np.arange(Xmax+1,dtype=np.float64)
omega=np.zeros(Xmax+1,dtype=np.int64)
for i in range(2,Xmax+1):
    if spf[i]==i:
        phi[i::i]*= (1-1.0/i)
        omega[i::i]+=1
W=np.zeros(Xmax+1); ev=np.arange(0,Xmax+1,2)[1:]
W[ev]=(2.0**omega[ev])/(4*phi[ev])
# Legendre-type model: T(p) ≈ sum_m (m/p) W(m) over m ≤ p/4 (even m); compare exact T(p) from data for p in (1e5,2.5e5)
def Tmodel_real(p):
    m=np.arange(2,min(p//4,Xmax)+1,2)
    return float(np.sum(W[m]*np.array([1 if pow(int(x),(p-1)//2,p)==1 else -1 for x in m])))  # slow but exact check on a few p
samp=[p for p in P if 100000<p<=250000][:10]
for p in samp[:3]:
    print("  check p=%d: exact T(p) from z38 = %.4f ; approx sum_m (m/p)W(m) = %.4f"%(p, mbm[p][1]-mbm[p][2], Tmodel_real(p)))
