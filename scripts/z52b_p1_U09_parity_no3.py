# z52b pass1 U09: (Z2233) parity patterns of ES solutions (x<=y<=z) for primes p≡1 (4), p<=N;
#                 (Z0863) general-n check: for n<=NN, does 4/n = 1/x+1/y+1/z have a solution with 3∤xyz ?
# Usage: python3 scripts/z52b_p1_U09_parity_no3.py N NN
import sys, math, collections
import numpy as np
N=int(sys.argv[1]); NN=int(sys.argv[2])
src=open("scripts/z52b_p1_U09_fullf.py").read().split("out=[]")[0].replace("N = int(sys.argv[1]) if len(sys.argv)>1 else 5000","N = %d" % N)
ns={}; exec(compile(src,"ff","exec"),ns)
spf=ns['spf']; divisors_of_b2=ns['divisors_of_b2']
pat=collections.Counter(); per_prime_missing=[]
for p in [q for q in range(5,N+1) if spf[q]==q and q%4==1]:
    seen=set()
    for x in range(math.ceil(p/4),(3*p)//4+1):
        a=4*x-p; b=p*x
        if a<=0: continue
        for d1 in divisors_of_b2(p,x):
            if d1%a==(-b)%a and d1>0:
                d2=(b*b)//d1
                if d2%a==(-b)%a:
                    y=(d1+b); z=(d2+b)
                    if y%a==0 and z%a==0:
                        y//=a; z//=a
                        if x<=y<=z:
                            seen.add(tuple(sorted((x%2,y%2,z%2))))
    for s in seen: pat[s]+=1
print("Z2233 parity patterns (sorted parity of x,y,z) over primes p≡1 (4), p<=%d: " % N, dict(pat))
print("   (0=even,1=odd); count = number of primes having at least one solution with that pattern")
# general n, 3∤xyz
def no3_solution(n):
    for x in range(math.ceil(n/4), (3*n)//4+1):
        if x%3==0: continue
        a=4*x-n; b=n*x
        if a<=0: continue
        ylo=max(x, b//a+1); yhi=(2*b)//a
        if yhi<ylo: continue
        ys=np.arange(ylo,yhi+1,dtype=np.int64)
        ys=ys[ys%3!=0]
        if ys.size==0: continue
        den=a*ys-b
        ok=(den>0)&((b*ys)%np.maximum(den,1)==0)
        if not ok.any(): continue
        zs=(b*ys[ok])//den[ok]
        good=zs[(zs%3)!=0]
        if good.size: return (x,int(ys[ok][0]),int(zs[0]))
    return None
fails=[n for n in range(2,NN+1) if no3_solution(n) is None]
print(f"Z0863: n in [2,{NN}] with NO solution with 3∤xyz: {fails}")
