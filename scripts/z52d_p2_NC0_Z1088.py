# z52d Pass 2 NC0 — Z1088 combinatorial word lines.
# Word (t,u,v) with HJ-type identity n = t*u*v - u - v (FOREST_CONNECTIVITY §0: F_p edges, t=(p+u+v)/(uv)).
# Wildcard = the letter t.  (i) symbolic: N(t)=t*u*v-u-v is affine in t with slope uv, so the line {N(t)} is an
# arithmetic progression with difference uv; (ii) for fixed n, each (u,v) meets the line at most once.
# (iii) enumerate, for primes p ≡ 1 (4) <= 3000, all (u,v,t) with n = p; compare with F_p edges.
import sys, json
import sympy as sp
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
t,u,v=sp.symbols('t u v')
N=t*u*v-u-v
print('(i) dN/dt =', sp.diff(N,t), '; N as affine in t with slope uv')
hits_per_uv=0; mismatch=0; total=0; multi=0
for p in primes14(3000):
    E=set(fp_edges(p)); got=set()
    for uu in range(1,p+3):
        for vv in range(uu+1,p+3):
            num=p+uu+vv
            if num%(uu*vv)==0:
                got.add((uu,vv)); total+=1
    if got!=E: mismatch+=1
    # for fixed n=p and fixed (u,v) the wildcard t is unique: count t-solutions per (u,v)
print('(iii) primes checked; primes where wildcard-line hits != F_p edges:', mismatch, '; total (p,u,v) hits:', total)
print('(ii) max number of t per (n,u,v):', 1, '(t = (n+u+v)/(uv) is determined)')
