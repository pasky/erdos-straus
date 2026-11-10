# Validation of z69_mine_gen.c: candidate roles vs brute-force enumeration of all words (x,y,z), p = 1 mod 8 < 1500, c <= 40.
import subprocess, random
from sympy import primerange
ps=[p for p in primerange(17,1500) if p%8==1]
inp=''.join('%d %d %s\n'%(p,40,' '.join(map(str,range(1,41)))) for p in ps)
out=subprocess.run(['/tmp/z69mine/gen'],input=inp,capture_output=True,text=True).stdout
got=set()
for l in out.split('\n'):
    a=l.split()
    if len(a)==6: got.add((int(a[0]),int(a[1])+1,int(a[2])))
exp=set()
for p in ps:
    for x in range(1,p+3):
        for z in range(1,p+3):
            s=p+x+z
            if s%(x*z)==0:
                y=s//(x*z)
                if (x*y)%8==0:
                    for c,role in ((x,0),(y,1),(z,2)):
                        if c<=40: exp.add((p,c,role))
print(len(got),len(exp),'mismatch',len(got^exp), list(got^exp)[:5])
