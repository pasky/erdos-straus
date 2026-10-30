import sys, math, random, subprocess
import numpy as np
N=10**6; top=math.sqrt(2*N)
M=2*N+10
spf=np.arange(M+1)
for i in range(2,int(M**0.5)+1):
    if spf[i]==i:
        s=spf[i*i::i]; msk=s==np.arange(i*i,M+1,i); s[msk]=i; spf[i*i::i]=s
def pf(x):
    fs=set()
    while x>1:
        p=int(spf[x]); fs.add(p)
        while x%p==0: x//=p
    return fs
random.seed(5)
ns=[]
while len(ns)<150:
    n=random.randrange(N//2,N); n-= (n-1)%8
    if math.isqrt(n)**2!=n: ns.append(n)
out=subprocess.run(["/tmp/dbreak_0046/cand",str(N),"0","1"]+[str(n) for n in ns],capture_output=True,text=True).stdout.split("\n")
bad=0
for n,line in zip(ns,out):
    X=0
    for e in range(1,(n+3)//8+1):
        for l in pf(n+4*e):
            if l>top and (l+1)%(4*e)==0: X+=1
    Xc=int(line.split()[2])
    if X!=Xc: bad+=1; print("MISMATCH",n,X,Xc)
print("checked",len(ns),"mismatches",bad)
