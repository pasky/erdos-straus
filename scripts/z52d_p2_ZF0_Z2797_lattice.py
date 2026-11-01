"""Exact character minima in two repo worst-case examples; O(q) time, O(1) auxiliary memory."""
from sympy import primitive_root, discrete_log
from fractions import Fraction
import math,json
rows=[]
for q,S in [(237971,[3,5,7]),(423883,[3,5,7,11,13])]:
    N=(q-1)//2;k=len(S);g=int(primitive_root(q));h=g*g%q
    logs=[int(discrete_log(q,s*s%q,h)) for s in S]
    best1=N;best2=N*N;j1=j2=0
    for j in range(1,N):
        coords=[min((j*a)%N,N-(j*a)%N) for a in logs]
        s=sum(coords);ss=sum(x*x for x in coords)
        if s<best1:best1=s;j1=j
        if ss<best2:best2=ss;j2=j
    Delta=best1/N;lambda2=math.sqrt(best2)/N
    old=math.isqrt(k**3*N*N//(best1*best1))
    if old*old*best1*best1<k**3*N*N:old+=1
    # ceil(k*N/sqrt(best2)) by exact square comparison.
    direct=math.isqrt(k*k*N*N//best2)
    if direct*direct*best2<k*k*N*N:direct+=1
    rows.append(dict(q=q,S=S,N=N,logs=logs,Delta=str(Fraction(best1,N)),lambda2_squared=str(Fraction(best2,N*N)),old_cap=old,direct_Euclidean_cap=direct,asymptotic_only_ASD_leading_cap_factor=.255*k**1.5/Delta,warning='ASD o(1) is not an explicit bound at this small k'))
print(json.dumps(rows,indent=2))
