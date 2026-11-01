# Z0803 check: are the 14 (★)-zeros low in h(-4p)/sqrt(p) ∝ L(1,χ_{-4p}) only because they are ≡ 1 (mod 3)?
# Truncated Euler product over primes q ≤ Q (ranking proxy). Compares quantiles vs neighbours in the same class mod 8
# (item's control) and vs neighbours ≡ 1 (mod 24).
import math
Z=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
Q=20000
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PQ=primes(Q)
def isprime(n):
    if n<2: return False
    for q in PQ:
        if q*q>n: return True
        if n%q==0: return n==q
    return True
def logL(p):
    s=0.0
    for q in PQ:
        if q==2 or q==p: continue
        chi4 = 1 if q%4==1 else -1
        leg = pow(q,(p-1)//2,p); leg = 1 if leg==1 else -1
        s -= math.log(1-chi4*leg/q)
    return s
def neigh(p,cond,k=60):
    out=[];d=2
    while len(out)<k:
        for c in (p-d,p+d):
            if c>5 and cond(c) and isprime(c): out.append(c)
        d+=2
    return out
qa=[];qb=[]
for p in Z:
    v=logL(p)
    A=[logL(c) for c in neigh(p,lambda c:c%8==p%8)]
    B=[logL(c) for c in neigh(p,lambda c:c%24==1)]
    qa.append(sum(x<v for x in A)/len(A)); qb.append(sum(x<v for x in B)/len(B))
    print(p, p%24, round(qa[-1],2), round(qb[-1],2))
print('mean quantile vs same mod 8:',round(sum(qa)/len(qa),3),' below median:',sum(x<0.5 for x in qa))
print('mean quantile vs p≡1 (24):',round(sum(qb)/len(qb),3),' below median:',sum(x<0.5 for x in qb))
