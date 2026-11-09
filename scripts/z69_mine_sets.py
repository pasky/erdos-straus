# Build hard set H (with tags) and size-matched random controls (primes p = 1 mod 8). Deterministic seed.
import random, sympy
D='data/'
H={}
def add(p,tag):
    p=int(p); assert p%8==1 and sympy.isprime(p), p
    H.setdefault(p,set()).add(tag)
for l in open(D+'z69/mine/Hlow_w030_1e8.txt'): add(l.split()[0],'low')
for l in open(D+'z68/u7f/noprime_primes_1e9.txt'): add(l.split()[0],'np')
for p in (3361,21841,76441): add(p,'C')
for l in open(D+'z68/u7o/deep_m16_4e9.txt'): add(l.split()[0],'deep')
for fn in ('dickson_C3.txt','dickson_C4.txt'):
    for l in open(D+'z68/u7o/'+fn):
        if int(l.split()[0])<=10**12: add(l.split()[0],'dick')
for l in open(D+'z68/u7f/u8zero_primes_1e8.txt'): add(l.split()[0],'u8')
random.seed(69)
with open(D+'z69/mine/H.txt','w') as fo:
    for p in sorted(H): fo.write('%d %s\n'%(p,','.join(sorted(H[p]))))
C=set()
for p in sorted(H):
    for k in range(3):
        wid=0.25
        while True:
            wid*=1.05
            q=random.randint(int((1-wid)*p)+1,int((1+wid)*p)+50)
            q=sympy.nextprime(q)
            while q%8!=1: q=sympy.nextprime(q)
            if q not in H and q not in C: break
        C.add(q)
with open(D+'z69/mine/CTRL.txt','w') as fo:
    for q in sorted(C): fo.write('%d\n'%q)
print(len(H),len(C))
