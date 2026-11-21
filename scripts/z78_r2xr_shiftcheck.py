"""Round-2 review (Claude Opus): per-shift sanity check of z78_r2shift.c.
Builds a /tmp variant that also prints every per-shift charge, then for all shifts
e<2^lo and a random sample below 2^J checks   #{h | M^2 : h == -M mod e}  <=  charge,
with M=(N+e)/4 fully factored here (trial division + Pollard rho + Miller-Rabin).
The class count bounds the number of oriented P centres at shift e (PL/z77 §3).
Usage: r K J nsample seed"""
import sys,subprocess,random,math,re
r,K,J,ns,seed=map(int,sys.argv[1:])
src=open('scripts/z78_r2shift.c').read()
src=src.replace('tot+=add;','fprintf(stderr,"%lu %lu\\n",E,add);tot+=add;',1)
assert 'fprintf(stderr' in src
open('/tmp/z78r2rev/shift_pere.c','w').write(src)
subprocess.run(['gcc','-O2','-o','/tmp/z78r2rev/shift_pere','/tmp/z78r2rev/shift_pere.c'],check=True)
p=subprocess.run(['/tmp/z78r2rev/shift_pere',str(r),str(r),str(K),str(J)],capture_output=True,text=True,check=True,timeout=1500)
charge={int(a):int(b) for a,b in (l.split() for l in p.stderr.splitlines())}
def mr(n):
    if n<2:return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0:return n==q
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37,41):
        x=pow(a,d,n)
        if x in(1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def rho(n):
    if n%2==0:return 2
    for c in range(1,1000):
        x=y=2;d=1
        while d==1:
            x=(x*x+c)%n;y=(y*y+c)%n;y=(y*y+c)%n;d=math.gcd(abs(x-y),n)
        if d!=n:return d
def fac(n,out):
    for q in range(2,1000):
        while n%q==0:out[q]=out.get(q,0)+1;n//=q
    st=[n]
    while st:
        m=st.pop()
        if m==1:continue
        if mr(m):out[m]=out.get(m,0)+1;continue
        d=rho(m);st+=[d,m//d]
    return out
def classcount(M,e):
    f=fac(M,{});t=(-M)%e;ds=[1]
    for q,v in f.items():ds=[d*q**i for d in ds for i in range(2*v+1)]
    return sum(1 for d in ds if d%e==t)
N=r**K;rnd=random.Random(seed)
es=sorted(charge);small=[e for e in es if e<1<<10];samp=small+rnd.sample([e for e in es if e>=1<<10],ns)
bad=0;slack=[]
for e in samp:
    M=(N+e)//4;assert 4*M==N+e
    c=classcount(M,e)
    if c>charge[e]:bad+=1;print('VIOLATION',e,c,charge[e])
    slack.append(charge[e]-c)
print('r',r,'K',K,'J',J,'shifts',len(es),'checked',len(samp),'violations',bad,'min slack',min(slack),'tot charge (all e<2^J)',sum(charge.values()))
