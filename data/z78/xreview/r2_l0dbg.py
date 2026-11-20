from r2_check import *
from collections import Counter
res, allt = part_a(7)
census = load_census('census_s4_17.txt')
tl = [(n,t) for n,T in allt.items() for t in T] + [x for x in census if x[0] > 7]
hist = Counter(); ex=[]
for n,t in tl:
    m,w,C,g,V = t
    for K in range(2,n+1):
        u = trunc(mul(neg(w), inv_ser(C,K)),K)
        for o in 'AB':
            if o=='A': X,B,p,q = w,C,[1],u
            else: X,B,p,q = C,w,u,[1]
            N=K-1; b=n-K; dl=N-b
            if b<0 or dl<1 or 2*K-n<0: continue
            M=mul(m,X); kap=exq(sub(q,p),Tp(1))
            H=exq(add(mul(p,X),mul(q,B)),Tp(K)); J=exq(add(mul(p,M,X),mul(q,V)),Tp(K)); S=exq(add(mul(p,M,g),kap),Tp(N))
            W=exq(add(mul(Tp(dl),S,J),mul(kap,q)),M)
            A0=sub(mul(q,B),mul(p,X))
            CGG=add(mul(der(m),A0,u,V),sc(2,mul(m,der(A0),u,V)),neg(mul(m,A0,der(mul(u,V)))))
            if not CGG or val(CGG)<n-1: continue
            L0=CGG[n-1:]
            e=min(dl,2*K-n,K)
            E=e+3
            Wi=inv_ser(W,E+1); pi=inv_ser(p,E+1); Xi=inv_ser(X,E+1)
            lg=add(mul(der(p),pi),neg(mul(der(W),Wi)),mul(der(X),Xi))
            br=sub([n%3],mul(Tp(1),trunc(lg,E)))
            R=trunc(mul(kap,u,u,Wi,br),E)
            agree = val(sub(trunc(L0,E),R))
            agree=min(agree,E)
            hist[(agree>=e, min(agree,9), e)] +=1
            if agree<e and len(ex)<5: ex.append((n,K,o,e,agree,dl,2*K-n,P2s(L0[:6]),P2s(R[:6])))
print(sorted(hist.items())); print(ex)
