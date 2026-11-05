# z59 MSPLUS: write the 840-level mean-model coefficients (lead = S_840(a)/8, c1, c0) for every a mod 840, a = 1 (4),
# using model() from z59_msplus_mean.py.  Output lines "a lead c1 c0".
import sys
sys.path.insert(0, 'scripts')
from z59_msplus_mean import model
avals = [a for a in range(840) if a % 4 == 1]
m = model(840, avals)
for a in avals:
    print(a, "%.12f %.12f %.12f" % m[a])
