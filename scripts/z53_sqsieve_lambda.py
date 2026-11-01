"""Falsifier F3 (EVIDENCE): signal vs noise of the square-sieve detection statistic.
For N_EACH primes p = 1 (24) and N_EACH odd squares m^2 near X, run z53strip on the cube-type strip (W, s-range scaled
to n^(1/3)) and collect  Z := (Lambda - P0|A|)/P0^2  (each square contributes ~1, non-squares give noise ~ sqrt(2|A|)/P0).
usage: python z53_sqsieve_lambda.py BIN X N_EACH P
"""
import sys, subprocess, re, statistics as st
from sympy import nextprime
BIN,X,NE,P=sys.argv[1],int(float(sys.argv[2])),int(sys.argv[3]),sys.argv[4]
T=round(X**(1/3)); W=T//3; S1=T//2; S2=4*T
def run(n):
    o=subprocess.run([BIN,str(n),str(W),str(S1),str(S2),P],capture_output=True,text=True,timeout=600).stdout
    A=int(re.search(r'\|A\|=(\d+)',o).group(1)); sq=int(re.search(r'squares=(\d+)',o).group(1))
    Z=float(re.search(r'\(Lambda-P0\|A\|\)/P0\^2=(-?[\d.]+)',o).group(1)); P0=int(re.search(r'P0=(\d+)',o).group(1))
    return A,sq,Z,P0
res={'prime':[],'square':[]}
p=X
while len(res['prime'])<NE:
    p=nextprime(p)
    if p%24==1: res['prime'].append(run(p))
m=int(X**0.5)|1
while len(res['square'])<NE:
    res['square'].append(run(m*m)); m+=2
for k,v in res.items():
    A=st.mean(a for a,_,_,_ in v); P0=v[0][3]
    Z=[z for _,_,z,_ in v]; S=[s for _,s,_,_ in v]; R=[z-s for _,s,z,_ in v]
    withsq=[z for _,s,z,_ in v if s>0]; nosq=[z for _,s,z,_ in v if s==0]
    print(f"{k}: N={len(v)} mean|A|={A:.0f} P0={P0} mean#squares={st.mean(S):.3f} mean Z={st.mean(Z):.3f} sd Z={st.pstdev(Z):.3f} "
          f"(noise model sqrt(2|A|)/P0={ (2*A)**0.5/P0:.3f}); mean Z on strips with squares={st.mean(withsq) if withsq else float('nan'):.3f} (n={len(withsq)}), without={st.mean(nosq):.3f} (n={len(nosq)})")
