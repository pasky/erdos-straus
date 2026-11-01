# Lint-fix round for batch TO2 (pass2_fix.md): replaces the flagged records (and two records whose summaries said
# the step was not run: Z0685, Z0686) in data/z52b/pass2/outcome_TO2.jsonl. Steps behind each record: scripts/z52d_p2_TO2_fix1.py,
# z52d_p2_TO2_qsqrt2.py, z52d_p2_TO2_romanoff.py, z52d_p2_TO2_divm1.py, z52d_p2_TO2_d5.py, z52d_p2_TO2_u840.sh, the OEIS fetch
# (A073101 terms vs data/z52b/raw/f4_all_30000.txt), and arXiv API lookups (EKL math/0612721, Romanoff 2302.06551).
import json
P = 'data/z52b/pass2/outcome_TO2.jsonl'
rows = [json.loads(l) for l in open(P)]
R = {}
R['Z0518'] = dict(outcome='nothing', summary=
 "Searched ES over O_K=Z[√2] with totally positive variables: for 18 non-rational totally positive ν (norm ≤20, coefficients |a|,|b|≤6) and ξ,η in the box |a|,|b|≤12 with ζ=1/(4/ν−1/ξ−1/η) required totally positive in O_K, every ν has a solution (exact Fraction check 18/18, e.g. 4/(3+√2) = 1/2 + 1/(2+√2) + 1/(6+2√2)-type identities). Rational ν are trivial (integer ES solutions are totally positive). No failure found in this range, so this is EVIDENCE only.",
 evidence=["scripts/z52d_p2_TO2_qsqrt2.py", "data/z52b/pass2/TO2/qsqrt2_search.json"],
 not_done="Search range is small (norm ≤20); no proof of ES_K for any K.", next="Extend ν to norm ≤200 and K=Q(√5) with the same code.")
R['Z0560'] = dict(outcome='nothing', summary=
 "EKL (arXiv math/0612721, verified abstract) classify A-invariant ergodic measures on SL_k(R)/SL_k(Z) and show Littlewood exceptions have dimension 0. Checked the transfer: ES's certificate is a finite word of bounded length, not a divergent orbit of a diagonal flow, so EKL's exceptional-set argument has no orbit to act on. Computed the orbit-length statistic instead: the HJ/Farey length λ(p) over non-residues takes only the values 2 and 3 for all 2384 primes p≡1 mod 8 in (17,10⁵) (132/54 for p<6000, matching BRAINSTORM/bsA_farey_graph_metric.md), i.e. the cusp-visit statistic is bounded, which is the ES₅ statement itself.",
 evidence=["scripts/z52d_p2_TO2_fix1.py", "data/z52b/pass2/TO2/fix1.json", "arXiv math/0612721", "BRAINSTORM/bsA_farey_graph_metric.md"],
 not_done="No homogeneous-dynamics model with a recurrence/divergence statement was constructed.", next="Ask whether the set of p with λ(p)=3 is a cusp-excursion set for a suitable geodesic flow, and test an EKL-type dimension-zero statement on it.")
R['Z0602'] = dict(outcome='nothing', summary=
 "Romanoff-type density computed exactly for odd n ≤ 10⁷: the fraction representable as p + 2^k (k ≥ 0) is 0.946 on [10³,10⁴), 0.930 on [10⁴,10⁵), 0.920 on [10⁵,10⁶), 0.915 on [10⁶,10⁷), and the mean number of representations is 2.84 in every decade (O(1), not log²). This matches the Romanoff picture (positive density, O(1) count) against ES's log²-count; arXiv 2302.06551 (verified abstract) gives Romanoff-type lower bounds from primes in tuples.",
 evidence=["scripts/z52d_p2_TO2_romanoff.py", "data/z52b/pass2/TO2/romanoff.json", "arXiv 2302.06551"],
 not_done="Limit density of the representable set not determined (decreasing slowly in the computed range).", next="Compare the mean representation count with the expected (log n)/log n·… Poisson prediction to test the O(1) claim beyond 10⁷.")
R['Z0638'] = dict(outcome='nothing', summary=
 "The S-integral relaxation is trivial already for S={2}: for every prime p, 4/p = 1/x+1/y+1/z with x = p/2 ∈ Z[1/2], y = z = p, since 2/p+1/p+1/p = 4/p. So the smallest admissible S is {2} for all p, and the relaxation carries no ES content (any S containing 2 works the same way). Verified by exact identity.",
 evidence=["PROVED elementary identity 4/p = 1/(p/2) + 1/p + 1/p"], not_done="", next="If an S-integral variant is wanted, impose positivity of the S-unit parts or restrict the denominators to Z (the original problem).")
R['Z0640'] = dict(outcome='covered', summary=
 "BRAINSTORM/bsA_farey_graph_metric.md answers the Farey-graph question: the Farey distance d_F equals the positive HJ length λ(p) on the tested range (EVIDENCE, scripts/bsA_fareydist.py 6000), because signed words reach non-residues no earlier than positive ones. Re-computed here: the HJ length minimised over non-residues gives 132 primes with λ=2 and 54 with λ=3 among p≡1 mod 8 below 6000, matching that memo, and λ∈{2,3} for all 2384 such primes up to 10⁵.",
 evidence=["BRAINSTORM/bsA_farey_graph_metric.md", "scripts/z52d_p2_TO2_fix1.py", "data/z52b/pass2/TO2/fix1.json"], not_done="", next="")
R['Z0649'] = dict(outcome='covered', summary=
 "The character escape is Mordell's identity. For d=5, the single family (a,d)=(1,5) (M=21) gives a Type-I witness for every prime p≡1 mod 24 with (5/p)=−1 (528/528 in [10⁴,10⁵)); explicitly f=7 for p≡13 mod 20 with c=(p+7)/20, and f=3 for p≡17 mod 20. Those classes avoid the Mordell-hard square classes mod 840, which are exactly the squares mod 5, i.e. (p/5)=+1. For d=7, 11, 13, … the (ℓ/p)=−1 primes are covered only partly by bounded-a families (d=7: 78 of 535 still uncovered at a≤200; d=13: 144 of 533), and the (ℓ/p)=+1 primes are never covered (Type I needs (d/p)=−1 empirically, 0 counterexamples in all ℓ tested). The square classes mod 840 are where the remaining difficulty sits.",
 evidence=["scripts/z52d_p2_TO2_d5.py", "data/z52b/pass2/TO2/d_ell_minimal_a.json", "scripts/z52d_p2_TO2_fix1.py", "data/z52b/pass2/TO2/fix1.json", "FRONTIER.md:30-31", "AMPLIFY_EXCEPTION.md:7-12"], not_done="", next="")
R['Z0660'] = dict(outcome='nothing', summary=
 "Statistic over all n ≤ 10⁵: the fraction having a divisor d ≡ −1 (mod m) is 0.864 (m=3), 0.801 (m=4), 0.730 (m=5), 0.718 (m=6), 0.618 (m=7), 0.563 (m=9), 0.483 (m=11), 0.509 (m=12) (m=2 is trivially 1). arXiv searches for the Erdős–Hall divisor-in-residue-class paper returned no hit, so the literature side is unresolved.",
 evidence=["scripts/z52d_p2_TO2_divm1.py", "data/z52b/pass2/TO2/divm1.json"], not_done="The Erdős–Hall theorem itself was not located on arXiv.", next="Locate Erdős–Hall (Hall–Tenenbaum 'Divisors' book) and compare the m-dependence with the ES divisor form.")
R['Z0677'] = dict(outcome='nothing', summary=
 "OEIS A073101 (D(n): solutions with 0<x<y<z) is fetched; its 72 listed terms (n=2..73) equal our distinct-solution column D from data/z52b/raw/f4_all_30000.txt exactly. Cross-references: A192787 (U, x≤y≤z) and A292581 (with multiplicity). Over 2≤n≤30000, D(n)=0 only at n=2, while U(n)=0 never occurs, so D is strictly positive for 3≤n≤30000. Vaughan's bound (quoted in A192787) is for U=0; D=0 is a weaker event (isosceles-only solutions), so the bound does not transfer automatically.",
 evidence=["https://oeis.org/A073101 (fetched)", "https://oeis.org/A192787 (fetched)", "data/z52b/raw/f4_all_30000.txt (column D)"], not_done="", next="")
R['Z0685'] = dict(outcome='needs-compute', summary=
 "Extension of the U(p)/log²p record list to p≡1 mod 840 in (10⁶, 10⁷]: 2384 of 3031 primes computed with the repo count program (4 cores, 30-min cap reached). No record: min U/log²p = 0.42 at p=3830401 (U=97), far above the record 0.147 (p=2521); min U = 88 at p=1007161. Remaining 647 primes lie in (8.02·10⁶, 10⁷] with per-prime times of 30–60 s, so about 15 more minutes on 4 cores (≈45 min total) — above the cap.",
 evidence=["scripts/z52d_p2_TO2_u840.sh", "data/z52b/pass2/TO2/U_p840_1e6_1e7.txt"],
 not_done="Primes ≡1 mod 840 in (8.02·10⁶, 10⁷] (647 primes) and non-(1 mod 840) classes.", next="Run the remaining 647 primes (≈15 min on 4 cores) with a 45-min cap.")
R['Z0686'] = dict(outcome='nothing', summary=
 "232792561 = lcm(1..19)+1 is prime (Miller–Rabin, 12 bases). U = 276 (computed in 3.5 min with the repo count program, memory <6 GB): D=276, O=1656, k1=193 (exactly one denominator divisible by p), k2=83 (exactly two). R = 22 (so not a (★) failure). U/log²p = 0.74, so not a record. The b=1 (López Type A) test was not run.",
 evidence=["data/z52b/pass2/TO2/U_232792561.txt", "data/z52b/pass2/TO2/fIfII_232792561.txt", "scripts/z52d_p2_TO2_rsingle.c"],
 not_done="The b=1 Type-A test is a separate check.", next="Run the b=1 test (p+4d has a divisor ≡ −1 mod 4d) on this prime.")
n = 0
for r in rows:
    if r['mid'] in R:
        keep = dict(mid=r['mid'], prev_outcome=r['prev_outcome'], **R[r['mid']])
        for k in ['outcome','summary','evidence','not_done','next']: r[k] = keep[k]
        n += 1
assert n == len(R), (n, len(R))
with open(P, 'w') as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('replaced', n)
