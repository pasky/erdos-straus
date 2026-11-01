# z52d pass2 TO1 (Z0275, Z0276): thinned-denominator worlds for 4/p = 1/x+1/y+1/z, p = 1 mod 4, p < N (exact, via sols() of z52b_analogues_constraints.py).
#  W_strict : every denominator has no prime factor = 3 mod 4 (Z0275 'strict' world)
#  W_eis    : every denominator has all primes = 2 mod 3 to even power (norm world; = Z0276)
#  For W_eis survivors: does every solution have 3 | some denominator? (Z0276 3-adic reading)
# usage: uv run --with sympy python scripts/z52d_p2_TO1_worlds.py N
import sys, json
from sympy import primerange, factorint
N=int(sys.argv[1])
src=open('scripts/z52b_analogues_constraints.py').read().split('def sqfree')[0]
g={'sys':type(sys)('s')}; g['sys'].argv=['x',str(N)]
exec(src,g); sols=g['sols']
def strict(n): return all(q%4!=3 for q in factorint(n))
def eis(n): return all(e%2==0 for q,e in factorint(n).items() if q%3==2)
res={'strict':[], 'eis':[]}; surv_eis=[]; surv_eis_all3=[]; surv_eis_some3=[]
tot=0; first_strict_sol={}
for P in primerange(5,N):
    if P%4!=1: continue
    tot+=1
    S=sols(P)
    st=[s for s in S if all(strict(t) for t in s)]
    if not st: res['strict'].append(P)
    else: first_strict_sol[P]=st[0]
    ei=[s for s in S if all(eis(t) for t in s)]
    if not ei: res['eis'].append(P)
    else:
        surv_eis.append(P)
        has3=[any(t%3==0 for t in s) for s in ei]
        if all(has3): surv_eis_all3.append(P)
        else: surv_eis_some3.append(P)
print(f"primes p=1 mod 4 below {N}: {tot}")
print("W_strict (no prime factor = 3 mod 4 in any denominator) fails at", len(res['strict']), "primes; first:", res['strict'][:15], "last:", res['strict'][-8:])
print("W_eis (norm world, = Z0276) fails at", len(res['eis']), "primes; survivors:", len(surv_eis))
print("   survivors where EVERY eis-solution has a denominator divisible by 3:", len(surv_eis_all3), " ; survivors with some eis-solution free of 3 | denominators:", len(surv_eis_some3))
print("   survivor list (first 20):", surv_eis[:20])
print("   survivors with a 3-free eis-solution:", surv_eis_some3[:20])
json.dump({'strict_fail':res['strict'],'eis_fail':res['eis'],'eis_surv':surv_eis,'eis_surv_all3':surv_eis_all3,'eis_surv_some3free':surv_eis_some3}, open(f'data/z52b/pass2/TO1/worlds_{N}.json','w'))
