"""R184 reviewer 2: Prop 8.1 / Cor 8.2 check, from scratch.
For n = 1 mod 4, 3 !| n, 13 <= n < N: check the explicit word; for primes also compute the HJ (negative) CF of n/A
for A = x*y-1 and A* = z*y-1 (middle letter y), confirm length 3 and compute Legendre (A/p)."""
import sys
N = int(sys.argv[1]) if len(sys.argv)>1 else 10**6
def hj(n,A):
    out=[]
    while A:
        b=-(-n//A); out.append(b); n,A=A,b*A-n
    return out
def leg(a,p):
    r=pow(a%p,(p-1)//2,p); return -1 if r==p-1 else r
sieve=bytearray([1])*N; sieve[0]=sieve[1]=0
for i in range(2,int(N**.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(range(i*i,N,i)))
bad=0; sg={1:{},5:{}}; cnt=0
for n in range(13,N,4):
    if n%3==0: continue
    w=(2,2,(n+2)//3) if n%3==1 else (3,(n+7)//12,4)
    x,y,z=w
    ok = min(w)>=2 and x*y*z-x-z==n
    if not ok: bad+=1; print('BAD',n,w)
    if sieve[n]:
        cnt+=1
        A=x*y-1; As=z*y-1
        assert A*As==y*n+1
        c=hj(n,A)
        assert c==[z,y,x], (n,A,c)
        s=leg(A,n); r=n%12; sg[r][s]=sg[r].get(s,0)+1
print('words checked, bad =',bad,'; primes',cnt,'; sign census by p mod 12:',sg)
# n=5 (the only p=1 mod 4 below 13 that is prime and 3!|): no word
print('n=5 has word?', any(x*y*z-x-z==5 for x in range(2,8) for y in range(2,8) for z in range(2,8)))
