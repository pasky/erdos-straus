# Z1328: where do (★) divisors d = 4uC-1 | N = 4Cp+1 (d ≡ -1 mod 4C) sit on the log scale, vs DDT arcsine law?
# Also: compare with all divisors of the same N (arcsine benchmark), and the distribution of log C/log p.
import subprocess, numpy as np, json
from sympy import isprime, divisors
ps=[p for p in range(10**6+1,10**6+40000,4) if isprime(p)][:300]
T=[];Cl=[];Tall=[]
for p in ps:
    out=np.array(subprocess.run(['/tmp/h03certs',str(p)],capture_output=True,text=True).stdout.split(),dtype=float).reshape(-1,3)
    for u,B,C in out:
        N=4*C*p+1; d=4*u*C-1
        T.append(np.log(d)/np.log(N)); Cl.append(np.log(C)/np.log(p))
for p in ps[:60]:
    for C in [1,2,3,5,8,13,30,100,300,1000]:
        N=4*C*p+1
        for d in divisors(N): Tall.append(np.log(d)/np.log(N))
T=np.array(T);Cl=np.array(Cl);Tall=np.array(Tall)
bins=np.linspace(0,1,11)
arc=np.diff(2/np.pi*np.arcsin(np.sqrt(bins)))
hT=np.histogram(T,bins)[0]/len(T); hA=np.histogram(Tall,bins)[0]/len(Tall)
hC=np.histogram(Cl,np.linspace(0,1.0001,11))[0]/len(Cl)
out=dict(nprimes=len(ps),ncert=len(T),bins=bins.tolist(),hist_cert_logd=hT.round(3).tolist(),hist_alldiv=hA.round(3).tolist(),arcsine=arc.round(3).tolist(),hist_logC_over_logp=hC.round(3).tolist(),mean_cert_per_prime=len(T)/len(ps))
print(json.dumps(out,indent=0))
json.dump(out,open('data/z52b/pass1/H03/arcsine.json','w'))
