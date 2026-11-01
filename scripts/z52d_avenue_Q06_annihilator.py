from math import gcd
import numpy as np
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def divs(n):
    r=[];i=1
    while i*i<=n:
        if n%i==0: r+=[i,n//i]
        i+=1
    return r
cols=[(C,a) for C in range(1,13) for a in range(1,4*C) if gcd(a,4*C)==1]
ps=[p for p in primes(2000) if p%4==1]
M=np.array([[0]*len(cols) for p in ps])
for i,p in enumerate(ps):
    for j,(C,a) in enumerate(cols):
        M[i,j]=any(d%(4*C)==a for d in divs(4*C*p+1))
print(len(cols),M.shape, np.linalg.matrix_rank(M))
triv=sum((sum(1 for a in range(1,4*C) if gcd(a,4*C)==1)-sum(1 for a in range(1,4*C) if gcd(a,4*C)==1 and a*a%(4*C)==1))//2 for C in range(1,13))
print('inverse pairs',triv)
# reduced matrix: keep one rep per {a,a^-1}, drop a=1 cols
keep=[j for j,(C,a) in enumerate(cols) if a!=1 and a<=pow(a,-1,4*C)]
print('reduced cols',len(keep),'rank',np.linalg.matrix_rank(M[:,keep]),'const col rank with ones', np.linalg.matrix_rank(np.c_[np.ones(len(ps)),M[:,keep]]))
