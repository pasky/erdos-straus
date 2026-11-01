"""z52d pass2 TO6 fix (Z2095): exact search for sets of distinct integers x_k>=2 with sum 1/x_k = 1 and sum x_k = m,
for m in a range (Graham: exists for all m>=78, fails at m=77 per Graham's survey). DFS over denominators with
reciprocal-sum pruning; denominators bounded by m. Memory tiny."""
import sys
from fractions import Fraction
def exists(m):
    sols=[]
    def dfs(start, rem, sumx, chosen):
        if rem==0:
            if sumx==m: sols.append(list(chosen)); return True
            return False
        if sumx>=m: return False
        # prune: remaining distinct denominators y in [start, m-sumx] give at most sum 1/y reciprocal mass
        cap=sum(1.0/y for y in range(start, m-sumx+1))
        if cap < float(rem)-1e-12: return False
        # any further denominator x>=start, x<=m-sumx ; reciprocal of next must be <= rem
        for x in range(start, m-sumx+1):
            r=Fraction(1,x)
            if r>rem: continue
            # if taking x and rem-r needs more than the max possible from remaining denominators, prune
            chosen.append(x)
            if dfs(x+1, rem-r, sumx+x, chosen): return True
            chosen.pop()
        return False
    return dfs(2, Fraction(1), 0, []), sols
out={}
for m in range(int(sys.argv[1]), int(sys.argv[2])+1):
    ok, s = exists(m)
    out[m]=(ok, s[0] if s else None)
    print(m, ok, s[0] if s else None, flush=True)
