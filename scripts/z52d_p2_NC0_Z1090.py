# z52d Pass 2 NC0 — Z1090 base-2 carry automaton for a certificate equation (LSB-first, 3-track).
# Language: words w = (x_0..x_{L-1}) over 3-bit columns encoding (x,y,z) in [0,2^L)^3 with 4xyz = p(xy+yz+zx).
# Myhill-Nerode: after reading the first j columns (low bits), the residual language = {suffixes accepted}.
# We count distinct residuals per level j (= states of the minimal DFA for this finite length-L language, per level),
# for several L, and report the total. A bounded-width carry automaton would give a bound independent of L and j.
import sys, json
import numpy as np
def run(p, L):
    B=1<<L
    g=np.arange(B,dtype=np.int64)
    Y,Z=np.meshgrid(g,g,indexing='ij')
    sol=np.zeros((B,B,B),dtype=bool)
    for x in range(B):                       # slab-wise to bound memory
        sol[x]=(4*x*Y*Z - p*(x*Y+Y*Z+Z*x))==0
    per_level=[]
    for j in range(L):          # j=L (single-bit residuals: accept/reject) is 2 states by construction
        s_=1<<j; R=B>>j
        M=sol.reshape(R,s_,R,s_,R,s_).transpose(1,3,5,0,2,4).reshape(s_**3,R**3)   # rows: prefixes (a,b,c); cols: residual
        per_level.append(len({M[i].tobytes() for i in range(M.shape[0])}))
    per_level.append(2)
    return per_level
out={}
for p in (13,17):
    for L in (3,4,5,6,7,8):
        pl=run(p,L)
        out[f'{p}_{L}']=pl
        print('p',p,'L',L,'distinct residuals per level j=0..L:',pl,'max',max(pl),'sum',sum(pl))
json.dump(out,open('data/z52b/pass2/NC0/sub/Z1090_mn.json','w'))
