"""Z0005: ES_q(A,P) with leading coefficients of X,Y,Z restricted to H = squares of F_q^* (vs monic H={1}).
Lemma-free existence test (exists_general). Counts failing irreducible P of degree n for A=T (k=1)."""
import sys, time
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_ff import exists_general, monic_irreducibles, str2poly, s2str, F
p = int(sys.argv[1]); ns = [int(x) for x in sys.argv[2].split(',')]
A = str2poly("10")
H_sq = {(x * x) % p for x in range(1, p)}
for n in ns:
    t = time.time()
    Ps = monic_irreducibles(p, n)
    fm = [s2str(P) for P in Ps if not exists_general(p, A, P, H={1})]
    fs = [s2str(P) for P in Ps if not exists_general(p, A, P, H=H_sq)]
    print(f"q={p} A=T n={n} irr={len(Ps)} fails_monic={len(fm)} fails_squareLC={len(fs)} "
          f"monic_only_fail={len(set(fm)-set(fs))} sq_only_fail={len(set(fs)-set(fm))} H={sorted(H_sq)} t={time.time()-t:.1f}s",
          flush=True)
    if set(fs) != set(fm):
        print('  sq_only:', sorted(set(fs) - set(fm))[:12], ' monic_only:', sorted(set(fm) - set(fs))[:12])
