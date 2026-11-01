"""z52d pass2 TO0b, FF batch 1 (uses exists_general = lemma-free complete test, validated vs Lemma-1.3 engine).
 Z0006: constant numerator A=4 (and A=1,2,3) over F_p: fraction of irreducible P of degree n with ES failing.
 Z0010/Z0026: P = Q^2 (Q irreducible of degree m), A = T, q = 3, 7: failure counts by parity of m; for q=3 also the
   Type-of-witness (deg X) distribution over successes.
 Z0041: failing P for A=T^2, q=3, n=3..5: P mod A and constant term."""
import sys, time
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_ff import exists_general, monic_irreducibles, str2poly, s2str, F
out = []
# Z0006
for p in (3, 5, 7):
    for c in ('1', '2', '3', '4'):
        A = (int(c) % p,)
        row = []
        for n in ((1, 2, 3) if p == 7 else (1, 2, 3, 4)):
            Ps = monic_irreducibles(p, n)
            if not Ps: continue
            f = sum(1 for P in Ps if not exists_general(p, A, P, H={1}))
            row.append(f'n={n}:{f}/{len(Ps)}')
        print(f'Z0006 q={p} A={c}:', ' '.join(row), flush=True)
# Z0010 / Z0026
for p, ms in ((3, (1, 2, 3)), (7, (1, 2))):
    A = str2poly('10')
    for m in ms:
        t = time.time()
        Qs = monic_irreducibles(p, m)
        F_ = 0; tot = 0; degX = {}
        for Q in Qs:
            P = F(p).mul(Q, Q)
            tot += 1
            ok, w = exists_general(p, A, P, H={1}, return_witness=True)
            if not ok: F_ += 1
            else:
                dX = len(w[0]) - 1
                degX[dX] = degX.get(dX, 0) + 1
        print(f'Z0010/26 q={p} deg Q={m} (deg P={2*m}) parity={"odd" if m%2 else "even"}: fails {F_}/{tot}; witness deg X dist {dict(sorted(degX.items()))}  t={time.time()-t:.1f}s', flush=True)
# Z0041
A = str2poly('100')
for n in (3, 4, 5):
    fails = []
    for P in monic_irreducibles(3, n):
        if not exists_general(3, A, P, H={1}):
            fails.append(P)
    rem = [F(3).divmod(P, A)[1] for P in fails]
    print(f'Z0041 q=3 A=T^2 n={n}: fails {len(fails)}  P:', [s2str(P) for P in fails], ' P mod T^2 (low->high):', [r for r in rem], ' P(0):', [P[0] for P in fails], flush=True)
