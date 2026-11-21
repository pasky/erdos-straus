"""Round-2 review (Claude Opus): per-shift check of z78_r2q5shift.c at one prime.
Patched /tmp build prints sampled per-shift charges (mode 0: small e, M=(eF+1)/4,
class -M mod e; mode 1: small f, M=(F+f)/4, class -1/4 mod f [z77 §5]); verify
#{h|M^2 : h in class} <= charge.  Usage: r nsample seed"""
import sys,subprocess,random
sys.path.insert(0,'scripts')
from z78_r2xr_shiftcheck_lib import fac
r,ns,seed=map(int,sys.argv[1:])
src=open('scripts/z78_r2q5shift.c').read()
src=src.replace('assert(UINT64_MAX-sum>=add);','assert(UINT64_MAX-sum>=add);if(e<(1u<<16)||e%100003==7)fprintf(stderr,"%d %lu %lu\\n",mode,e,add);',1)
assert 'fprintf(stderr' in src
open('/tmp/z78r2rev/q5_pere.c','w').write(src)
subprocess.run(['gcc','-O2','-o','/tmp/z78r2rev/q5_pere','/tmp/z78r2rev/q5_pere.c'],check=True)
p=subprocess.run(['/tmp/z78r2rev/q5_pere',str(r),str(r),'0'],capture_output=True,text=True,check=True,timeout=1500)
rows=[tuple(map(int,l.split())) for l in p.stderr.splitlines()]
F=r**5;rnd=random.Random(seed);samp=rnd.sample(rows,min(ns,len(rows)))
bad=0;mins=None
for mode,e,ch in samp:
    if mode==0:M=(e*F+1)//4;assert 4*M==e*F+1;mod=e;cl=(-M)%e
    else:
        M=(F+e)//4;assert 4*M==F+e;mod=e
        if e%r==0:continue
        cl=(-pow(4,-1,e))%e if e>1 else 0
    f=fac(M,{});ds=[1]
    for q,v in f.items():ds=[d*q**i for d in ds for i in range(2*v+1)]
    c=sum(1 for d in ds if d%mod==cl)
    if c>ch:bad+=1;print('VIOLATION',mode,e,c,ch)
    mins=ch-c if mins is None else min(mins,ch-c)
print('r',r,'sampled',len(samp),'of',len(rows),'violations',bad,'min slack',mins)
