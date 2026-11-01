# Summarise omega_*.txt tables from z52d_p2_ZF1_Z3072_omega.c: P(r_C>0 | Omega=k) (all C, per C-bucket) and parity table.
import sys, collections
for fn in sys.argv[1:]:
    T1=collections.defaultdict(lambda:[0,0,0.0]); T2=collections.defaultdict(lambda:[0,0])
    for line in open(fn):
        if line.startswith('#'): print(line.strip()); continue
        if line.startswith('P ') or line.startswith('T3'): continue
        f=line.split()
        if f[0]=='T1':
            k,b,n,s=int(f[1]),int(f[2]),int(f[3]),int(f[4]); r=float(f[6])*n
            for key in ((k,b),(k,'all')): T1[key][0]+=n; T1[key][1]+=s; T1[key][2]+=r
        else:
            o,t,b,n,s=map(int,f[1:6])
            for key in ((o,t,b),(o,t,'all'),(o,'all','all')): T2[key][0]+=n; T2[key][1]+=s
    print('==',fn); print('k   n(all C)   P(succ)  mean r_C | P by C-bucket [1,10) [10,100) [100,1e3) [1e3,1e4) [1e4,1e5) [1e5,1e6)')
    for k in range(0,24):
        if (k,'all') not in T1: continue
        n,s,r=T1[(k,'all')]
        row=' '.join('%.4f'%(T1[(k,b)][1]/T1[(k,b)][0]) if T1[(k,b)][0]>=200 else '  -   ' for b in range(6))
        print('%2d %10d  %.4f  %.4f | %s'%(k,n,s/n,r/n,row))
    print('parity: Omega(rough) tau(s)-bucket  [P by C-bucket]  (rough = prime factors > N^(1/3))')
    tb=['1','2','3-4','5-8','9-16','17-32','33-64','>64']
    for t in range(8):
        for o in range(3):
            if (o,t,'all') not in T2: continue
            n,s=T2[(o,t,'all')]
            row=' '.join('%.4f'%(T2[(o,t,b)][1]/T2[(o,t,b)][0]) if T2[(o,t,b)][0]>=200 else '  -   ' for b in range(6))
            print('tau(s)=%-6s Om(r)=%d n=%9d P=%.4f | %s'%(tb[t],o,n,s/n,row))
