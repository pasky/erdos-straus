"""T4 helper (z52 bank): run from the repo root."""
import sys, math
rows=[]
for f in sys.argv[1:]:
    for line in open(f):
        a,b,N,c=map(int,line.split()); rows.append((a,b,N,c))
def norm_rep(a,b):
    # representative with even real part (a+bi ~ b+ai)
    return (a,b) if a%2==0 else (b,a)
by={}
for a,b,N,c in rows:
    A,B=norm_rep(a,b); key=(A%4,B%4)
    L=math.log(N)**2
    by.setdefault(key,[]).append((c/L, c, N))
for key in sorted(by):
    v=by[key]; print(key, 'n=',len(v),' mean c/log^2N = %.3f'%(sum(x[0] for x in v)/len(v)), ' zeros:', [x[2] for x in v if x[1]==0], ' min c:',min(x[1] for x in v))
allm=[c/math.log(N)**2 for a,b,N,c in rows]; print('overall mean c/log^2 N = %.3f over %d primes'%(sum(allm)/len(allm),len(allm)))
