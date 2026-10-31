# z52b pass1 U09 (Z1398): for primes p ≡ 1 (4) up to N, the minimal max-denominator over ALL ES solutions 4/p=1/x+1/y+1/z (x<=y<=z),
# i.e. min z. Reuses the divisor enumeration of scripts/z52b_p1_U09_fullf.py (validated vs brute force for p<=400).
# Usage: python3 scripts/z52b_p1_U09_minmax.py N > data/z52b/pass1/U09/minmax_full_le<N>.txt
import sys, math
sys.argv=[sys.argv[0], sys.argv[1]]
import importlib.util
spec=importlib.util.spec_from_file_location("ff","scripts/z52b_p1_U09_fullf.py")
src=open("scripts/z52b_p1_U09_fullf.py").read().split("out=[]")[0]
ns={}; exec(compile(src,"ff","exec"),ns)
N=int(sys.argv[1]); fullcount_src=ns
def minz(p):
    best=None
    for x in range(math.ceil(p/4), (3*p)//4+1):
        a=4*x-p; b=p*x
        if a<=0: continue
        for d1 in ns['divisors_of_b2'](p,x):
            if d1 % a == (-b) % a and d1 > 0:
                d2=(b*b)//d1
                if d2 % a == (-b) % a:
                    y=(d1+b); z=(d2+b)
                    if y%a==0 and z%a==0:
                        y//=a; z//=a
                        if x<=y<=z and (best is None or z<best): best=z
    return best
for p in [q for q in range(5,N+1) if ns['spf'][q]==q and q%4==1]:
    m=minz(p)
    print(p, m if m is not None else 0)
