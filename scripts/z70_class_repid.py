# z70 CLASS item 1: explicit decomposition of the small-prime translation overlaps of G_d(n) (observed data only).
# Natural ideal representatives of a good class g = [A-ideal of sigma], sigma = (a,b,c,e) (Lemma FIB, Z70_CLASS.md §1.4):
#   R_A = (A, 2ad + sqrt(-dn)),  N = A = 4acd - 1;   R_B = conj (B, 2bd + sqrt(-dn)),  N = B = 4bcd - 1;
#   R_E = D_d * conj (e, 2ad + sqrt(-dn)),  N = d e.
# For a translation t = [L] (L the reference prime ideal over a translation prime l) an overlap pair (g, g + t) is
#   E-ID   : realised by an e-side ideal identity  R_E' = R_E * L^{+-1}         (what the PSC null preserves)
#   REP-ID : realised by an identity between ANY natural representatives  R' = R * L^{+-1}  (not E-ID)
#   OTHER  : neither (a class coincidence that is not an identity of natural representatives).
# REPID:AA pairs are split by whether the two A-representatives come from the same c (Lemma DL' — c-fibre divisor lattice)
#   and the same a (then they are Lemma-DL pairs seen from the A side).
# Also reported: min-norm statistics (norm of the smallest natural representative) of the classes in REP-ID pairs.
# Usage: python scripts/z70_class_repid.py d range P0 P1 [mod res] | list n1 ...
import sys, math
sys.path.insert(0, 'scripts')
from collections import Counter
from sympy import primerange
from z70_class_core import Fact, ClassData, solutions
from z70_class_null import translations

def vec_of(C, F, N, root, conj=False, D=False):
    v = dict(C.ideal_vector(N, root % N, F)) if N > 1 else {}
    if conj: v = {q: -k for q, k in v.items()}
    if D: v['D'] = 1
    return v

def analyse(n, d, F):
    sols = solutions(n, d, F)
    if not sols: return None
    if any(math.gcd(x, d*n) > 1 for (a, b, c, e) in sols for x in (e, 4*a*c*d - 1, 4*b*c*d - 1)): return 'gcd'
    C = ClassData(n, d); G = C.G
    reps = {}                                    # class -> list of (vector, norm)
    for (a, b, c, e) in sols:
        A = 4*a*c*d - 1; B = 4*b*c*d - 1
        g = G.coords[__import__('z69_twist_i17').reduce(A, 4*a*d, d*e)]
        RA = vec_of(C, F, A, 2*a*d); RB = vec_of(C, F, B, 2*b*d, conj=True); RE = vec_of(C, F, e, 2*a*d, conj=True, D=(d > 1))
        # sanity: the three representatives lie in g
        for R in (RA, RB, RE):
            x = C.vec_class([(q, k) for q, k in R.items() if q != 'D'])
            if 'D' in R: x = G.add(x, C.Td)
            assert x == g, (n, d, (a, b, c, e))
        reps.setdefault(g, []).extend([(RA, A, 'A', (a, c)), (RB, B, 'B', (b, c)), (RE, d*e, 'E', (a, c))])   # (fibre letter, c)
    X = list(reps)
    if len(X) < 2: return None
    tl, tlp = translations(C)
    out = Counter()
    for t, l in zip(tl, tlp):
        tag = 'L1' if l == tlp[0] else 'Lx'
        for g in X:
            y = G.add(g, t)
            if y not in reps: continue
            kind = 'OTHER'
            for (R1, N1, s1, ac1) in reps[g]:
                for (R2, N2, s2, ac2) in reps[y]:
                    diff = dict(R2)
                    for q, k in R1.items(): diff[q] = diff.get(q, 0) - k
                    diff = {q: k for q, k in diff.items() if k}
                    if len(diff) == 1 and l in diff and abs(diff[l]) == 1:
                        if s1 == 'E' and s2 == 'E': kind = 'EID'; break
                        if kind == 'OTHER' or (kind == 'REPID:AA' and s1 + s2 == 'AA' and ac1[1] == ac2[1]):
                            kind = 'REPID:' + ''.join(sorted(s1 + s2))
                            kind += ('_samec' if ac1[1] == ac2[1] else '_diffc') + ('_samea' if ac1[0] == ac2[0] else '_diffa')
                if kind == 'EID': break
            out[tag + '_' + kind] += 1; out[tag] += 1
            if kind.startswith('REPID'):
                out[tag + '_REPID'] += 1
                out[tag + '_REPIDminnorm_le_sqrt'] += int(min(r[1] for r in reps[g]) <= math.isqrt(d*n))
    out['K'] = len(X)
    out['K_small'] = sum(1 for g in X if min(r[1] for r in reps[g]) <= math.isqrt(d*n))
    return out

if __name__ == "__main__":
    d = int(sys.argv[1]); spec = sys.argv[2:]
    if spec[0] == 'range':
        mod, res = (int(spec[3]), int(spec[4])) if len(spec) > 4 else (8, 1)
        nl = [p for p in primerange(int(spec[1]), int(spec[2])) if p % mod == res]
    else: nl = sorted(set(int(x) for x in spec[1:]))
    F = Fact(max(nl)//3 + 10)
    tot = Counter()
    for n in nl:
        o = analyse(n, d, F)
        if o == 'gcd': tot['skipped_gcd'] += 1
        elif o: tot.update(o); tot['nprimes'] += 1
    keys = sorted(tot)
    print(f"# z70 repid d={d} {' '.join(spec[:3])}: " + '; '.join(f"{k}={tot[k]}" for k in keys))
