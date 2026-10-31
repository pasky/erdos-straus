"""Z0409: analyse largest exceptional primes of m/p (m=8..40) from PW Table 1 (m<=15, to 10^12-10^13)
and our scans (m=16..40, p<=3e6, data/z52b/pass1/H02/schinzel_m*.txt).  Fits log N_m ~ A m^beta."""
import math, numpy as np, glob
from math import gcd
PMAX=3_000_000
# PW Table 1 (sources/pw.txt l.~860): largest exceptional n (all n, incl. composite) ≤ N; prime ones listed
pw={8:[2,3,11,17,131,241],9:[2,5,11,19],10:[2,3,7,11,43,61,67,181],11:[2,3,37],
    12:[2,3,5,7,13,29,31,37,73,97,193,433,577,1129,1657,1873,2521,2593,3433,10369,12049,12241],
    13:[2,3,5,7,53,61,67,79,211,281],14:[2,3,5,17,19,29,59,257,353],
    15:[2,3,17,19,23,31,47,53,61,79,113,137,151,197,233,271,541,1103,1171,1367,4201,6301,12601,16831,20521]}
data={}
for m,l in pw.items():
    ps=[p for p in l if all(p%q for q in range(2,int(p**.5)+1)) and m%p]
    data[m]=(ps,False)
for m in range(16,41):
    E=[int(l.split()[1]) for l in open(f"data/z52b/pass1/H02/schinzel_m{m}.txt") if l.startswith("E")]
    data[m]=(E, max(E)>PMAX/2)   # censored if the largest is in the top half of the scanned range
def issq(r,m): return any((x*x-r)%m==0 for x in range(m))
print(" m  phi  #E  maxE        lnN   ln N/sqrt(m) cens  maxE mod m  sq-class?  frac_E_in_sq_classes(p>m^2)")
rows=[]
for m in sorted(data):
    E,c=data[m]; N=max(E); ph=sum(1 for a in range(1,m+1) if gcd(a,m)==1)
    big=[p for p in E if p>m*m]
    fsq=(sum(issq(p%m,m) for p in big)/len(big)) if big else float('nan')
    # proportion of unit classes that are squares
    sqfrac=sum(issq(a,m) for a in range(1,m) if gcd(a,m)==1)/ph
    print("%2d %4d %4d %9d %6.2f %6.2f   %s   %4d   %s   %.2f (sq classes %.2f of units)"%(m,ph,len(E),N,math.log(N),math.log(N)/math.sqrt(m),"C" if c else " ",N%m,issq(N%m,m),fsq,sqfrac))
    rows.append((m,ph,math.log(N),c))
for name,sel in [("odd m, uncensored",lambda r: r[0]%2==1 and not r[3]),("m≡2 mod 4, uncensored",lambda r: r[0]%4==2 and not r[3]),("m≡0 mod 4, uncensored",lambda r: r[0]%4==0 and not r[3]),("all uncensored",lambda r: not r[3])]:
    R=[r for r in rows if sel(r)]
    if len(R)<3: continue
    x=np.log([r[0] for r in R]); y=np.log([r[2] for r in R])
    b,a=np.polyfit(x,y,1)
    print("%-24s n=%2d  log N_m ≈ %.3f · m^%.3f   -> predicted N_4 = exp(%.2f)"%(name,len(R),math.exp(a),b,math.exp(a)*4**b))
    x2=np.log([r[1] for r in R]); b2,a2=np.polyfit(x2,y,1)
    print("%-24s        log N_m ≈ %.3f · φ(m)^%.3f -> predicted N_4 = exp(%.2f)"%("",math.exp(a2),b2,math.exp(a2)*2**b2))
# restricted fits m >= 16 (avoid small-m finite-size effects)
for name,sel in [("m>=16 odd, uncensored",lambda r: r[0]>=16 and r[0]%2==1 and not r[3]),("m>=16 all, uncensored",lambda r: r[0]>=16 and not r[3])]:
    R=[r for r in rows if sel(r)]
    x=np.log([r[0] for r in R]); y=np.log([r[2] for r in R]); b,a=np.polyfit(x,y,1)
    resid=y-(a+b*x); se=math.sqrt((resid**2).sum()/(len(R)-2)/((x-x.mean())**2).sum())
    print("%-24s n=%2d  log N_m ≈ %.3f · m^%.3f (slope SE %.3f)"%(name,len(R),math.exp(a),b,se))
