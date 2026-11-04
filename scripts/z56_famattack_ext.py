import sys, time, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load, ols_resid, corr_matrix
cfgs = [(8,3,5,7,11,13,17,19,23,29,31), (16,9,25,49,11,13,17,19,23,29,31),
        (32,27,25,49,121,169,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)]
for fn in sys.argv[1:]:
    p, R, g = load(fn); W = g.sum(2); N = len(p); se = 1/np.sqrt(N)
    for ells in cfgs:
        t = time.time(); Xr, k = ols_resid(W, p, ells); Co = corr_matrix(Xr - Xr.mean(0))
        print(fn, k, "cols: (0,1) %+.4f z=%+.1f  (0,2) %+.4f  (0,4) %+.4f  (1,2) %+.4f (3,4) %+.4f  [%.0fs]" % (Co[0,1], Co[0,1]/se, Co[0,2], Co[0,4], Co[1,2], Co[3,4], time.time()-t), flush=True)
