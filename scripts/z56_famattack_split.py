import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load, within_center, corr_matrix
for fn in sys.argv[1:]:
    p, R, g = load(fn); N = len(p); strata = p % 840
    for lab, cs in (("C<p^.6 (ic 0-2)", slice(0, 3)), ("C>=p^.6 (ic 3-4)", slice(3, 5)), ("C<p^.4 (ic 0-1)", slice(0, 2))):
        Wp = g[:, :, cs].sum(2)
        C = corr_matrix(within_center(Wp, strata))
        print(fn, lab, "means", np.round(Wp.mean(0), 2), "within-840 corr:", " ".join(f"({i}{j}){C[i,j]:+.3f}" for i in range(5) for j in range(i+1, 5) if Wp[:, i].std() > 0 and Wp[:, j].std() > 0))
    # cross: W0 non-congruence vs W1 congruence etc
    A = g[:, 0, 0:3].sum(1); B_ = g[:, 0, 3:5].sum(1); Cc = g[:, 1, 0:3].sum(1); D = g[:, 1, 3:5].sum(1)
    X = within_center(np.column_stack([A, B_, Cc, D]), strata); M = corr_matrix(X)
    print("  W0nc,W0c,W1nc,W1c corr:\n", np.round(M, 3), " se", round(1/np.sqrt(N), 4))
