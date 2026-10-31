# Z1449: "prime-divisor certificates": (★) triples (u,B,C) where the divisor d=4uC-1 (or d'=4BC-1) of 4Cp+1 is PRIME.
# Identity: q prime, q ≡ -1 (4C), q | 4Cp+1  <=>  q = 4uC-1 with q | p+u  (u = (q+1)/(4C)).  Count vs log p.
import subprocess, numpy as np, json
from sympy import isprime
out={}
for lo in (10**5,10**6,10**7):
    ps=[p for p in range(lo+1,lo+10**6,4) if isprime(p)][:250]
    Rp=[];R=[]
    for p in ps:
        t=np.array(subprocess.run(['/tmp/h03certs',str(p)],capture_output=True,text=True).stdout.split(),dtype=np.int64).reshape(-1,3)
        R.append(len(t))
        Rp.append(sum(1 for u,B,C in t if isprime(int(4*u*C-1))))   # ordered triples: each unordered pair counted from both sides
    L=np.log(lo)
    out[lo]=dict(mean_R=float(np.mean(R)),mean_Rprime=float(np.mean(Rp)),Rprime_over_logp=float(np.mean(Rp)/L),
                 R_over_log2p=float(np.mean(R)/L**2),frac_Rprime0=float(np.mean(np.array(Rp)==0)),min_Rprime=int(min(Rp)))
print(json.dumps(out,indent=1)); json.dump(out,open('data/z52b/pass1/H03/primecert.json','w'),indent=1)
