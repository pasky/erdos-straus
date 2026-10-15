"""z17_ffpairs.py (O242): sibling-pair statistics of q = 3 tuple balls (all balls, alive or not) per depth and slice,
against the Poisson expectation. usage: python3 scripts/z17_ffpairs.py data/z16/balls_d9.txt"""
import sys
from collections import defaultdict, Counter
balls=defaultdict(set)
for line in open(sys.argv[1]):
    d,u=line.split(); balls[int(d)].add(u)
for d in sorted(balls):
  for c in '12':
    B=[u for u in balls[d] if u[1]==c]
    par=Counter(u[:-1] for u in B)
    pairs=sum(k*(k-1)//2 for k in par.values()); trip=sum(1 for k in par.values() if k==3)
    npar=3**(d-3); b=len(B)
    print(d,c,b,"pairs",pairs,"exp %.3f"%(b*(b-1)/2/npar),"triples",trip, "exp %.4f"%(b*(b-1)*(b-2)/6/npar**2))
