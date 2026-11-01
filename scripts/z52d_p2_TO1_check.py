# z52d pass2 TO1: independent exact check of the C enumerator (sols() from z52b_analogues_constraints.py) for p < N.
# usage: uv run --with sympy python scripts/z52d_p2_TO1_check.py N table.tsv
import sys
from sympy import primerange
N=int(sys.argv[1]); table=sys.argv[2]
src=open('scripts/z52b_analogues_constraints.py').read().split('def sqfree')[0]
g={'sys':type(sys)('s')}; g['sys'].argv=['x',str(N)]
exec(src, g)
sols=g['sols']
rows={int(l.split('\t')[0]):l.split('\t') for l in open(table)}
bad=0; n=0
for P in primerange(5,N):
    if P%4!=1: continue
    S=sols(P); n+=1
    r=rows[P]
    mn=min((max(s) for s in S),default=-1)
    ok = len(S)==int(r[1]) and (not S or (int(r[2])==min(4*s[0]-P for s in S) and int(r[3])==mn))
    if not ok: bad+=1; print('MISMATCH',P,len(S),r[1:4])
print('checked',n,'primes; mismatches',bad)
