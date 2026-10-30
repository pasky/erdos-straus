"""T4 helper (z52 bank): run from the repo root."""
import math
def gmod(a, m):  # Gaussian a mod m via rounding
    ar,ai=a; mr,mi=m; n=mr*mr+mi*mi
    qr=(ar*mr+ai*mi); qi=(ai*mr-ar*mi)
    qr=round(qr/n); qi=round(qi/n)
    return (ar-(qr*mr-qi*mi), ai-(qr*mi+qi*mr))
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def gpow(a,e,m):
    r=(1,0); a=gmod(a,m)
    while e:
        if e&1: r=gmod(gmul(r,a),m)
        a=gmod(gmul(a,a),m); e>>=1
    return r
def unit_of(r,m):
    for u,name in (((1,0),'1'),((0,1),'i'),((-1,0),'-1'),((0,-1),'-i')):
        d=(r[0]-u[0],r[1]-u[1])
        if gmod(d,m)==(0,0): return name
rows=[tuple(map(int,l.split())) for l in open('data/z52_bank/gauss_q1_counts_le2e4.txt')]
fails={(2,5),(4,5),(5,6),(10,13),(2,17),(8,73)}
from collections import Counter
for alpha,nm in (((1,1),'1+i'),((3,0),'3'),((2,1),'2+i')):
    allc=Counter(); fc=[]
    for a,b,N,c in rows:
        if N in (3,5) : continue
        A,B=(a,b) if a%2==0 else (b,a)
        if B%4!=1: continue
        m=(A,B); s=unit_of(gpow(alpha,(N-1)//4,m),m)
        allc[s]+=1
    for a,b in fails:
        A,B=(a,b) if a%2==0 else (b,a); N=A*A+B*B; m=(A,B)
        fc.append(unit_of(gpow(alpha,(N-1)//4,m),m))
    print('quartic symbol of',nm,': failures',fc,' class Im=1(4) population <=2e4:',dict(allc))
print('--- class means by (Im mod 4 after normalisation, [3/pi]_4)')
for f in ['data/z52_bank/gauss_q1_counts_le2e4.txt','data/z52_bank/gauss_q1_counts_1e5_window.txt','data/z52_bank/gauss_q1_counts_98e4_1e6.txt']:
    R=[tuple(map(int,l.split())) for l in open(f)]
    grp={}
    for a,b,N,c in R:
        if N<1000: continue
        A,B=(a,b) if a%2==0 else (b,a); m=(A,B)
        s=unit_of(gpow((3,0),(N-1)//4,m),m)
        grp.setdefault((B%4,s),[]).append(c/math.log(N)**2)
    print(f, {k:(len(v), round(sum(v)/len(v),3)) for k,v in sorted(grp.items())})
