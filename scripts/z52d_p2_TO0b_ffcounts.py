"""z52d pass2 TO0b: per (q, A, n) table of ES_q(A,P) solution-multiset counts over all monic irreducible P of degree n.
Engine: scripts/z52d_p2_TO0b_ff.py count_solutions (Lemma 1.3 of FUNCTIONFIELD_ES.md; cross-checked vs data/ffl fail files).
usage: python3 scripts/z52d_p2_TO0b_ffcounts.py q A_string n_list(comma) > out.tsv
prints: q A n irr fails meanN maxN  + failing P list to stderr-free second line"""
import sys, time
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_ff import count_solutions, monic_irreducibles, str2poly, s2str
q = int(sys.argv[1]); As = sys.argv[2]; ns = [int(x) for x in sys.argv[3].split(',')]
A = str2poly(As)
for n in ns:
    t = time.time()
    rows = []
    for P in monic_irreducibles(q, n):
        c, _ = count_solutions(q, A, P)
        rows.append((s2str(P), c))
    fails = [P for P, c in rows if c == 0]
    cs = [c for _, c in rows]
    print(f"{q}\t{As}\t{n}\t{len(rows)}\t{len(fails)}\t{sum(cs)/len(cs):.3f}\t{max(cs)}\t{round(time.time()-t,1)}\t{' '.join(fails)}", flush=True)
