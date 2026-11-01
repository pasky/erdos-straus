# z52d Pass 2 NC0 — Z1095 carry (digit-by-digit) propagation for the cleared ES equation 4xyz = p(xy+yz+zx).
# LSB-first digit search: S_j = {(a,b,c) in [0,2^j)^3 : E(a,b,c) ≡ 0 mod 2^j}, E = 4xyz - p(xy+yz+zx)  (a 2-adic carry test).
# Every solution with x,y,z < 2^L must survive: (x mod 2^j, ...) in S_j for all j (checked).
# Cost of the diagram = sum_j 8|S_{j-1}| extensions tested; naive = all ordered triples in [1,2^L)^3 (= 2^(3L)).
import sys, json
sys.path.insert(0,'scripts')
from z52d_p2_NC0_allsols import sols
def diagram(p, L):
    S={(0,0,0)}          # level 0: the single empty residue
    sizes=[1]; tests=0
    for j in range(L):
        m=1<<(j+1); new=set()
        bit=1<<j
        for (a,b,c) in S:
            for da in (0,bit):
                for db in (0,bit):
                    for dc in (0,bit):
                        x=a+da; y=b+db; z=c+dc; tests+=1
                        if (4*x*y*z - p*(x*y+y*z+z*x)) % m == 0: new.add((x,y,z))
        S=new; sizes.append(len(S))
    return S, sizes, tests
out=[]
for p in (13,17,29,37):
    for L in (6,8,10):
        S,sizes,tests=diagram(p,L)
        B=1<<L
        sols_in=[s for s in sols(p) if max(s)<B]
        ok=all(tuple(perm) in S for s in sols_in for perm in __import__('itertools').permutations(s))
        out.append(dict(p=p,L=L,survivors_per_level=sizes,diagram_tests=tests,naive_ordered_triples=(B-1)**3,
                        solutions_below_B=len(sols_in),all_solutions_survive=ok))
        print(out[-1])
json.dump(out,open('data/z52b/pass2/NC0/sub/Z1095_carry.json','w'))
