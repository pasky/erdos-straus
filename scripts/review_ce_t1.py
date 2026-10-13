"""R199: 5.4 check. For n = 9, 25, 49 and every word (t,u,v), tuv-u-v = n: exact 2-power overorders of C_0(L_w):
unique index-2 overorder (discrd 2n), no maximal 2-overorder of discrd n (so E(L_w) is maximal at 2, 2 ramified)."""
import sys
sys.path.insert(0, 'scripts')
from review_ce_lib import Cliff, two_power_overorders, discrd
from review_ce_words import words
tot = bad = 0
for n in (9, 25, 49):
    for (t, u, v) in words(n):
        C = Cliff([[v, -1, 0], [-1, t, -1], [0, -1, u]])
        Bs = C.c0_basis()
        ovs = two_power_overorders(C, Bs)
        idx = sorted(k for k, _ in ovs)
        ok = discrd(C, Bs) == 4 * n and idx == [1, 2] and all(discrd(C, M) == (4 * n) // k for k, M in ovs)
        tot += 1
        bad += not ok
        if not ok:
            print('FAIL', n, (t, u, v), idx)
print('words', tot, 'failures', bad)
