# Z0113: lcm world (x|z, y|z) for p ≡ 1 (4).  z = a x = b y, 4/p = (a+b+1)/z.
# Branch (ii) p|a, p∤b: a=p a', b+1 = a' k, 4 | p+k, b | p+k, 4b | a'(p+k).
# Branch (iv) p|a, p|b: a=p a', b=p b', a' | p b'+1, b' | p a'+1, a'+b' ≡ 3 (4).
import sys
N=int(sys.argv[1]); KMAX=int(sys.argv[2]) if len(sys.argv)>2 else 10**9
spf=list(range(2*N+2))
i=2
while i*i<=2*N+1:
    if spf[i]==i:
        for j in range(i*i,2*N+2,i):
            if spf[j]==j: spf[j]=i
    i+=1
def divs(n):
    ds=[1]
    while n>1:
        q=spf[n];e=0
        while n%q==0: n//=q;e+=1
        ds=[d*q**t for d in ds for t in range(e+1)]
    return ds
def branch2(p):
    k=(-p)%4 or 4
    while k<=min(p,KMAX):
        n=p+k
        for m in divs(n):
            if (m+1)%k==0:
                a1=(m+1)//k
                if (a1*n)%(4*m)==0: return (k,m)
        k+=4
    return None
fails=[];found_k=[]
for p in range(5,N+1,4):
    if spf[p]!=p: continue
    r=branch2(p)
    if r is None: fails.append(p)
    else: found_k.append(r[0])
print("N",N,"branch(ii) fails:",len(fails),fails[:40])
print("max k used",max(found_k))
def branch4(p):
    # 4a' | s and 4b' | s with s = p(a'+b')+1; gcd(a',b')=1 forces min(a',b') <= ~p/2, complete search
    for a1 in range(1,p+2):
        n=p*a1+1
        for b1 in divs(n) if n<len(spf) else _divs_big(n):
            s=p*(a1+b1)+1
            if s%(4*a1)==0 and s%(4*b1)==0: return (a1,b1)
    return None
def _divs_big(n):
    ds=[];d=1
    while d*d<=n:
        if n%d==0: ds+= [d] if d*d==n else [d,n//d]
        d+=1
    return ds
print("branch(iv) on branch(ii)-failures:",{p:branch4(p) for p in fails})
