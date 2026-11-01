"""z52d pass2 TO0b Z0010: ES_q(T, Q^2) (monic, lemma-free exists_general) by q and deg Q (q = 3,5,7,11; Q monic irreducible).
Control: q=5,13 (q = 1 mod 4, no colour layer) vs q=3,7,11 (q = 3 mod 4). Prints failing Q for each (q, deg Q)."""
import sys, time
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_ff import exists_general, monic_irreducibles, str2poly, s2str, F
A = str2poly('10')
for p, ms in ((3, (1, 2, 3)), (5, (1, 2)), (7, (1, 2)), (11, (1,)), (13, (1,))):
    for m in ms:
        t = time.time()
        Qs = monic_irreducibles(p, m)
        fails = []
        for Q in Qs:
            P = F(p).mul(Q, Q)
            if not exists_general(p, A, P, H={1}):
                fails.append(s2str(Q))
        print(f'q={p} (q mod 4 = {p%4}) deg Q={m}: fails {len(fails)}/{len(Qs)} Q in {fails[:10]}  t={time.time()-t:.1f}s', flush=True)
