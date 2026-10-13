"""T1 control: for odd squares n, every word's C0 has no maximal 2-overorder of discrd n (anisotropic at 2)."""
from ce_lib import *
from cf_lib import words
for n in (9, 25, 49):
    cnt = bad = 0
    for (t, u, v) in words(n):
        al = Alg(c0_table(path_gram(t, u, v))); ov = maximal_overorders_2(al, ident_basis())
        ds = sorted(d for k, (B, d) in ov.items())
        cnt += 1; bad += (ds != [2 * n, 4 * n])
    print('n', n, 'words', cnt, 'not [2n,4n] ladder:', bad)
