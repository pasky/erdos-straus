# O72: brute-force check of Prop 5.3 congruence F = 1 (mod c_o) at levels alpha+2gamma in {5,6} (any delta)
from sympy import divisors
cnt=bad=0
for al in range(0,7):
  for ga in range(0,4):
    s=al+2*ga
    if s not in (5,6) or al+ga<3: continue
    t=2+al+ga
    for co in range(1,120,2):
      for ko in range(1,120,2):
        c=(2**al)*co; k=(2**ga)*ko; N=1+4*c*k*k; n=(4*c*k)>>t
        for F in divisors(N):
          e=N//F
          if F<e and (e-F)%(16*n)==0:
            cnt+=1
            if (F-1)%co!=0: bad+=1; print('bad',c,k,F,e)
print(cnt,bad)
