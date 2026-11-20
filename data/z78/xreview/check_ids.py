# Independent check of F3_CONJ identities/lemmas on genuine tuples (any depth), F_3[T].
import re,sys
def P(s): return [int(ch) for ch in s] if s!='0' else []
def nrm(a):
    a=[x%3 for x in a]
    while a and a[-1]==0: a.pop()
    return a
def add(a,b,sb=1):
    n=max(len(a),len(b)); return nrm([(a[i] if i<len(a) else 0)+sb*(b[i] if i<len(b) else 0) for i in range(n)])
def mul(*ps):
    r=[1]
    for b in ps:
        if not r or not b: return []
        o=[0]*(len(r)+len(b)-1)
        for i,x in enumerate(r):
            if x:
                for j,y in enumerate(b): o[i+j]+=x*y
        r=nrm(o)
    return r
def divmod_(a,b):
    a=a[:]; q=[0]*max(0,len(a)-len(b)+1); il=1 if b[-1]==1 else 2
    while len(a)>=len(b) and a:
        s=len(a)-len(b); f=(a[-1]*il)%3; q[s]=f
        for i,y in enumerate(b): a[i+s]=(a[i+s]-f*y)%3
        a=nrm(a)
    return nrm(q),a
def exact(a,b):
    q,r=divmod_(a,b); assert not r,'non-exact division'; return q
def Tp(k): return [0]*k+[1]
def deg(a): return len(a)-1
def val(a):
    if not a: return 10**6
    i=0
    while a[i]==0: i+=1
    return i
def der(a): return nrm([(i*a[i]) for i in range(1,len(a))])
def gcd(a,b):
    while b: a,b=b,divmod_(a,b)[1]
    return a
def degR3(A,B):
    # F=A/B (T-units); deg of reduced denominator of F'/F = deg(AB) - deg gcd(A'B-AB', AB)
    num=add(mul(der(A),B),mul(A,der(B)),-1)
    if not num: return None   # F'=0
    AB=mul(A,B); return deg(AB)-deg(gcd(num,AB))
fails={}; stats={}
def chk(name,cond):
    stats[name]=stats.get(name,0)+1
    if not cond: fails[name]=fails.get(name,0)+1
for fn in sys.argv[1:]:
  for line in open(fn):
    kv=dict(re.findall(r'(\w+)=(\S+)',line))
    n=int(kv['n']); c=int(kv['c']); e2=int(kv.get('e','0'))
    m,w,C,g,V=[P(kv[k]) for k in 'm w C g V'.split()]
    u=nrm([1,c,e2]); Tn=Tp(n)
    # tuple identities
    chk('tuple', add(mul(m,w,C),add(Tn,V),-1)==[] and add(add(w,C),mul([0,1],g,V),-1)==[])
    dep=val(add(w,mul(u,C)))
    for ori in (0,1):
        X,B=(w,C) if ori==0 else (C,w)
        p,q=([1],u) if ori==0 else (u,[1])
        kap=exact(add(q,p,-1),[0,1])
        M=mul(m,X)
        K=min(dep,n)
        if K<1: continue
        chk('L31_depth_pMX+qV', val(add(mul(p,M,X),mul(q,V)))>=K)
        H=exact(add(mul(p,X),mul(q,B)),Tp(K)); J=exact(add(mul(p,M,X),mul(q,V)),Tp(K))
        N_=K-1; b=n-K; d_=N_-b
        S=exact(add(mul(p,M,g),kap),Tp(N_))
        chk('MH', add(mul(M,H),add(mul(q,Tp(b)),J),-1)==[])
        chk('VS', add(mul(V,S),add(mul(p,Tp(b)),J),-1)==[])
        # log-derivative / ABC: deg R3(F)>=K if F'!=0
        r3=degR3(mul(p,M,X),mul(q,V))
        if r3 is None: chk('Fprime_zero_seen',False)
        else: chk('R3F>=K', r3>=K)
        if d_>=0:
            Wn=add(mul(Tp(d_),S,J),mul(kap,q))
            Wq,Wr=divmod_(Wn,M); chk('W_integral', Wr==[]); W=Wq
            chk('VW', add(mul(V,W),add(mul(Tp(d_),H,J),mul(kap,p,X),-1),-1)==[])
            chk('pXS', add(mul(p,X,S),add(mul(Tp(b+1),W),mul(q,H),-1),-1)==[])
            chk('TdSH-W=pqg', add(add(mul(Tp(d_),S,H),W,-1),mul(p,q,g),-1)==[])
            chk('pgJ', add(mul(p,g,J),add(mul(Tp(b),W),mul(kap,H),-1),-1)==[])
            chk('W_Tunit(delta>0)' if d_>0 else 'W_Tunit(delta=0)', W!=[] and W[0]!=0)
        if 2*K>=n:
            A0=add(mul(q,B),mul(p,X),-1)
            D=add(mul(m,Tp(2*K-n),H,H),u,-1)
            chk('second_contact', add(add(mul(m,A0,A0),mul(u,V)),mul(Tp(n),D),-1)==[])
            rg=degR3(mul(m,A0,A0),mul(u,V))
            if rg is None:
                chk('Gprime_zero_seen',False)
                pq1=add(p,q); R3sup=deg(m)+deg(X)+2
                chk('Gcube=>R3F<=d+2', (r3 is not None and r3<=R3sup) or r3 is None)
            else: chk('R3G>=n', rg>=n)
for k in sorted(stats): print(f'{k}: tested {stats[k]} failed {fails.get(k,0)}')
