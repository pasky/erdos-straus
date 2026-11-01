"""Z0687: U/log^3 p vs L(1,chi_p) for primes p = 1 mod 360360 (<=1.5e8: 8 lowest-L and 8 highest-L), vs lcm(1..19)+1."""
import json, math
D='data/z52b/pass2/ZF0/Z0687/'
L={int(a):float(b) for a,b in (l.split() for l in open(D+'L_rank_1e10.txt'))}
U={}
for l in open(D+'U_targets_out.txt'):
    x=l.split(); U[int(x[0])]=(int(x[1]),int(x[10]),int(x[11]))
U[232792561]=(276,193,83)   # Pass 1, data/z52b/pass2/NC0/U_lcm19plus1.txt
rows=sorted(((L[p],p,u,k1,k2,u/math.log(p)**3) for p,(u,k1,k2) in U.items()))
for r in rows: print('L=%.3f p=%d U=%d k1=%d k2=%d U/log^3=%.4f'%r)
import statistics as st
lo=[r[5] for r in rows[:8]]; hi=[r[5] for r in rows[8:] if r[1]!=232792561]
xs=[math.log(r[0]) for r in rows]; ys=[math.log(r[5]) for r in rows]
mx,my=st.mean(xs),st.mean(ys); b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
def rank(v): s=sorted(v); return [s.index(x) for x in v]
rx,ry=rank(xs),rank(ys); n=len(xs); rho=1-6*sum((a-c)**2 for a,c in zip(rx,ry))/(n*(n*n-1))
out=dict(rows=[dict(L=r[0],p=r[1],U=r[2],k1=r[3],k2=r[4],U_log3=r[5]) for r in rows],mean_Ulog3_lowL=st.mean(lo),mean_Ulog3_highL=st.mean(hi),
         loglog_slope=b,spearman=rho,lcm19_L_percentile_among_6587=0.899)
json.dump(out,open(D+'summary.json','w'),indent=1)
print('mean U/log3 lowL',st.mean(lo),'highL',st.mean(hi),'slope dlog(U/log3)/dlogL',b,'spearman',rho)
