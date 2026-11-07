# For zero primes and random primes = 1 mod 8: count case-(ii)-full solutions by m (R^{(m)}), m=1..6,
# and case-(i) solutions by t for t <= TMAX (via divisor pairs of w=(pt+1)/4, t|a+b, a<=b).
import sys, random
from sympy import divisors, isprime, factorint
ZEROS=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
MM=6; TMAX=int(sys.argv[1]) if len(sys.argv)>1 else 63
def Rm(p):
    # count (Y,Z,s) with s|Y+Z, 4YZ | p+s, by m=(Y+Z)/s
    cnt=[0]*(MM+1)
    # enumerate D = 4g'Ym-1 | m p + Y ... simpler: enumerate Y, then Z: 4YZ | p+s with s | Y+Z.
    # Use (B)-form: for d = 3 (4), d | m p + Y with mY | (d+1)/4.  Enumerate d up to bound: d | mp+Y, so d <= mp+Y.
    # Instead enumerate (Y,m): mY | (d+1)/4, d | mp+Y: divisors of mp+Y that are = -1 mod 4mY.
    for m in range(1,MM+1):
        Y=1
        while True:
            # need d >= 4mY-1 and d | mp+Y, d = -1 mod 4mY; smallest d=4mY-1 <= mp+Y => 4mY-1<=mp+Y
            if 4*m*Y-1>m*p+Y: break
            for d in divisors(m*p+Y):
                if d%(4*m*Y)==4*m*Y-1: cnt[m]+=1
            Y+=1
    return cnt
def R1(p,TMAX):
    cnt={}
    for t in range(3,TMAX+1,4):
        w=(p*t+1)//4
        dv=divisors(w)
        c=0
        for i,a in enumerate(dv):
            for b in dv[i:]:
                if (a+b)%t==0: c+=1
        cnt[t]=c
    return cnt
if __name__=="__main__":
    random.seed(3)
    rows=[]
    for p in ZEROS:
        rm=Rm(p); r1=R1(p,TMAX)
        print(f"ZERO p={p}: R^(m) m=1..{MM}: {rm[1:]}  case(i) t=3..{TMAX}: {[r1[t] for t in sorted(r1)]}  total(i)={sum(r1.values())}")
    for p in ZEROS[::3]:
        for _ in range(3):
            q=random.randrange(p//2,2*p)|1
            while not (isprime(q) and q%8==1): q+=2
            rm=Rm(q); r1=R1(q,TMAX)
            print(f"RAND p={q}: R^(m) m=1..{MM}: {rm[1:]}  case(i): {[r1[t] for t in sorted(r1)]}  total(i)={sum(r1.values())}")
