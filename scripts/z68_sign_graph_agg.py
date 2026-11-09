import re,sys
rows=[]
lines=open(sys.argv[1]).read().split('\n')
for i,l in enumerate(lines):
    if 'giant=' in l:
        d=dict(re.findall(r'(\w[\w+]*)=([-\d./]+)',l))
        m=re.search(r'S1comp:(\d) S1comp\+:(\d) S1D:(\d) S1D\+:(\d) S2comp:(\d) S2comp\+:(\d) S2D:(\d) S2D\+:(\d)',l)
        nxt=lines[i+1]
        d2=dict(re.findall(r'(\w[\w+]*)=([-\d.]+)',nxt))
        rm=re.search(r'S1 q=\d+ len=\d+ Rmin:(\S+)\(len\d+\) Rmin\+:(\S+)',nxt.replace('|',''))
        rows.append((int(d['n']),d,list(map(int,m.groups())),d2,rm.groups() if rm else None))
import statistics as st
def band(lo,hi):
    R=[r for r in rows if lo<r[0]<=hi]
    if not R: return
    n=len(R)
    g=[float(r[1]['giant']) for r in R]; gp=[float(r[1]['giant+']) for r in R]
    sgn=sum(1 for r in R if r[1]['giant+sign']=='-1')
    allL3=sum(1 for r in R if r[1]['L3inGiant'].split('/')[0]==r[1]['L3inGiant'].split('/')[1])
    gl3=sum(1 for r in R if int(r[1]['goodL3inGiant'])>0)
    gl3p=sum(1 for r in R if int(r[1]['goodL3inGiant+'])>0)
    S=[r[2] for r in R]
    print(f"({lo},{hi}] n={n} giant mean {st.mean(g):.3f} min {min(g):.3f}; giant+ mean {st.mean(gp):.3f}; giant+ good-signed {sgn}/{n}; all L3 in giant {allL3}/{n}; good L3 in giant {gl3}/{n}; good L3 in giant+ {gl3p}/{n}")
    print("   S1 (least QNR word): inGoodComp %d inGoodComp+ %d D %d D+ %d | S2: %d %d %d %d" % tuple(sum(s[i] for s in S) for i in range(8)))
    s1r=sum(1 for r in R if r[4] and r[4][0]=='GOOD-L3'); print("   Rmin from S1 success:",s1r,"/",n, " mean D(good len>=4):",round(st.mean(float(r[3]['D']) for r in R),4))
import sys as _s
B=[(0,1000),(1000,10000),(10000,30000),(30000,60000),(60000,100000),(100000,700000),(700000,1000000)]
for lo,hi in B: band(lo,hi)
