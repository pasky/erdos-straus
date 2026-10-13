# brute-force R(n) for n < N (cross-check of bsG_count.c); prints mismatches
import sys, subprocess
N=int(sys.argv[1]); R=[0]*N
for x in range(2,N):
    for y in range(2,N):
        if x*y*2-x-2>=N: break
        for z in range(2,N):
            v=x*y*z-x-z
            if v>=N: break
            R[v]+=1
ns=list(range(2,N))
out=subprocess.run(['/tmp/bsG_count']+[str(n) for n in ns],capture_output=True,text=True).stdout
got={int(l.split('(')[1].split(')')[0]):int(l.split('=')[1]) for l in out.splitlines() if l.startswith('R(')}
bad=[n for n in ns if got[n]!=R[n]]
print("checked",len(ns),"mismatches",bad[:10]); print("zeros",[n for n in ns if R[n]==0])
