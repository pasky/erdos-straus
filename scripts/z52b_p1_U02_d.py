"""Z2478 / Z2615 (bounded version): n S-smooth (S={2,3,5,7}), n <= 20000; find all ES solutions (x<=y<=z) of 4/n with
x,y,z all S-smooth. Uses esols() from z52b_p1_U02_lib. Exhaustive within the bound only (not Baker/Chabauty)."""
import sys, json
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
S = (2, 3, 5, 7)
def smooth(m):
    for q in S:
        while m % q == 0: m //= q
    return m == 1
Ns = [n for n in range(2, 20001) if smooth(n)]
hits = []
for n in Ns:
    for s in esols(n):
        if all(smooth(v) for v in s):
            hits.append((n, s))
json.dump({'n_smooth_tested': len(Ns), 'hits': hits}, open('data/z52b/pass1/U02/Z2478_Ssmooth.json', 'w'))
print('n tested', len(Ns), 'hits', len(hits), hits[:20])
