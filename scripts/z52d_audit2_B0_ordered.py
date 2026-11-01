# Z2238: unordered (x<=y<=z) vs ordered ES solution counts at primes, by repeated-coordinate stratum.
import sys, math
def sols(N):
    out=[]
    for x in range(N//4+1, 3*N//4+1):
        num=4*x-N; den=N*x
        g=math.gcd(num,den); num//=g; den//=g
        for y in range(max(x,den//num+1), 2*den//num+1):
            n2=num*y-den
            if n2>0 and (den*y)%n2==0: out.append((x,y,den*y//n2))
    return out
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
P=int(sys.argv[1]); agg={1:[0,0,0,0],3:[0,0,0,0]}
for p in range(5,P,2):
    if not isprime(p): continue
    s=sols(p); distinct=sum(1 for a in s if len(set(a))==3); rep=len(s)-distinct
    ordered=6*distinct+3*rep  # a triple with exactly two equal coords has 3 orderings (all-equal impossible: 4/p=3/x)
    A=agg[p%4]; A[0]+=1; A[1]+=len(s); A[2]+=rep; A[3]+= (ordered!=6*len(s))
    if p%4==3 and rep and p<60: print('p',p,'repeated-coordinate triples:',[a for a in s if len(set(a))<3])
for r,(np,ns,rep,diff) in agg.items():
    print(f"p≡{r} (4), p<{P}: primes={np} unordered sols={ns} with a repeated coordinate={rep}; primes where ordered≠6·unordered: {diff}")
