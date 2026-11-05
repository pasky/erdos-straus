"""z58 WITNESS: semi-local survival P(u_min > U), P(C_min > U), P(s > U) (s = min(u_min, C_min) = least coordinate over all (★) solutions) for 𝔐-primes by decade; bracket = -log P / (log p_mid * log(U+1)). Run in the directory holding the 1e9 scan chunks s_0..s_5.txt."""
import sys, math, bisect
rng=[(1e6,1e7),(1e7,1e8),(1e8,1e9)]
data={r:{'u':[],'C':[],'s':[]} for r in rng}
for fn in ['s_%d.txt'%i for i in range(6)]:
    for line in open(fn):
        if line[0]=='#': continue
        f=line.split()
        if f[2]!='1' or f[3]=='-1': continue
        p=int(f[0])
        for r in rng:
            if r[0]<p<=r[1]:
                u=int(f[7]); C=int(f[9]); data[r]['u'].append(u); data[r]['C'].append(C); data[r]['s'].append(min(u,C))
for r in rng:
    print('range',r, 'N',len(data[r]['u']), 'mean log p', )
    L=math.log(math.sqrt(r[0]*r[1]))
    for k in ('u','C','s'):
        a=sorted(data[r][k]); N=len(a)
        row=[]
        for S in (1,2,4,8,16,32,64,128):
            c=N-bisect.bisect_right(a,S); P=c/N
            row.append(f"{S}:{P:.2e}" + (f"({-math.log(P)/(L*math.log(S+1)):.3f})" if c else ""))
        print(' ',k,' '.join(row))
