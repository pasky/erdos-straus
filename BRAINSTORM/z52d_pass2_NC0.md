# z52d Pass 2 — batch NC0 (81 needs-compute items)

Summary: 81/81 items recorded (one line each in data/z52b/pass2/outcome_NC0.jsonl). Outcomes: covered=2, interesting=10, needs-compute=3, nothing=66.
Interesting: Z0739, Z0848, Z0863, Z0814, Z0922, Z0651, Z0353, Z0323, Z0896, Z0961.
Not done (cap or missing infrastructure): Z0272, Z0292 (needs-compute); Z0779 segmented 1e10 and Z0948 3e4 partial sums not finished; Z0687 rank of L(1,χ_p) not run.
Premise corrections: Z0012 (4/P ∈ Frac(A) for every P), Z0357 (relaxation is not lattice-free), Z1188 (Lean project does exist), Z0863 3-adic hypothesis refuted by unit-solvability mod 81, Z0848 independence premise (model predicts a finite tail).
Process: 1 subagent group (G1) was aborted at the cap; its 7 finished items were kept, the remaining items were run by the coordinator. Scripts: scripts/z52d_p2_NC0_*; data: data/z52b/pass2/NC0/.

## Interesting items
### Z0739 — Last-failure sequence by numerator m (7..48) is not in OEIS
Existence-only search (scripts/z52d_p2_NC0_exist.c; every S-line of a 13,200-sample re-verified exactly; every last failure re-checked with the full counter z52b_fingerprint_count) over ALL primes p<=1e7 for m=5..48: last failures m=7..19 unchanged from the <=1e5 list (2,241,19,181,37,12241,281,353,20521,83449,2081,35281,353); beyond 1e5 the tail moves a lot: 20/p 90001->2763601, 24/p 97777->620929, 28/p->1532161, 32/p->3991681, 36/p->8763841, 44/p->7559641, 48/p->9961249 (5/p, 6/p: no failure to 1e7). Prime-only failures lie in (m^2,2m^2) for every m=20..48 (e.g. m=20: 401,421,503,601,641,761), consistent with Pomerance-Weingartner arXiv:2511.16817 (m>=20 numerics). A 10-term OEIS search for the prefix returned no hit.

Evidence: scripts/z52d_p2_NC0_exist.c, scripts/z52d_p2_NC0_verify_exist.py, (uncommitted, 1.8 GB, regenerate: scripts/z52d_p2_NC0_exist.c) /tmp/z52d_big/NC0_exist/m*_p1e7.txt, data/z52b/pass2/NC0/lastfail_m5_48.txt, https://arxiv.org/abs/2511.16817
Next: Push the window for m=36..48 (last failures censored near 1e7) to 1e8 with the existence counter (about 20 s per 1e7 for all m, so ~5 min) and reread PW's tables.

### Z0848 — Independence heuristic predicts unbounded Vmin; data show a plateau at 116 — test it
Computed Vmin(p) (least v in 4Z∪(8Z-p), v>=3, with a divisor d≡-1 mod v of p+v) for all 108,283 primes p≡1 (4), p<=3e6, v<=160: records 3(5),4(17),7(97),8(457),23(1009),87(2521),116(3361) exactly as the repo records. Independence model with empirical per-shift failure frequencies q_v(size bin, p mod 8): expected #{p<=3e6: Vmin>V} = 14.4 (V=23), 3.1 (V=31), 0.36 (V=47), 0.006 (V=116) versus observed 166, 69, 16, 0. So the premise 'independence predicts unbounded Vmin' is wrong (the model predicts a finite, rapidly decaying tail; E#{Vmin>116}≈0.006), but the model under-predicts the mid-range tail 10-50x: failures across shifts are positively correlated.

Evidence: scripts/z52d_p2_NC0_vmin.py, data/z52b/pass2/NC0/vmin_3000000.json, data/z52b/pass2/NC0/vmin_model_3000000.json
Next: Condition the Vmin tail on p mod 3,5,7 (and smooth p-1) and check whether the 10-50x excess disappears, as the joint-census analysis of EXSET_SHIFT_DIVISORS §6.3 suggests.

### Z0863 — No-3 solutions (3 ∤ xyz) fail only at 3 and 241
Exact avoidance search over all primes p<=1e7 (existence with q∤xyz, scripts/z52d_p2_NC0_exist.c mode 1): no solution with 3∤xyz fails only at p=3 and p=241; 'no 5' fails only at 5, 'no 7' only at 7; 'no 4', 'no 8', 'no 9' never fail. 4/241 has exactly 8 unordered solutions, all containing a multiple of 3 (exact check). But 3-adic unit-solvability is not obstructed: for p mod 81 every unit residue class is reached by some unit triple (241 ≡ 79 mod 81 is in the solvable set), so the 3-adic obstruction hypothesis is not supported; the exception looks global and sporadic.

Evidence: scripts/z52d_p2_NC0_exist.c, scripts/z52d_p2_NC0_allsols.py, (uncommitted, 1.8 GB, regenerate: scripts/z52d_p2_NC0_exist.c) /tmp/z52d_big/NC0_exist/avoid{3,4,5,7,8,9}_p1e7.txt
Next: Test whether 4/241's eight solutions are explained by a global reason (e.g. Mordell–Schinzel / a quadratic-form genus obstruction over Q(sqrt(-3)) ) and whether 241 is the only prime with no unit-denominator solution mod 3-adic and mod 2-adic data together.

### Z0814 — Proth-type primes k·2^n + 1 with small k as an ES-hardness test bed
Proth primes k·2^n+1 (k odd ≤15, p≤1e7; 38 primes, 30 of them ≤1e5) vs U(p)/log²p: median 0.56 for the 30 small ones against 1.07 for all p≡1 (4) in (1e3,1e5]; against controls matched on p mod 840 at the same size (≤1e5) the ratio is 0.54, and matched on (p mod 105, v2(p-1)) it is 0.71. Against random controls in [5e6,1e7] the naive ratio is 0.40 but that is a size artefact. The deficit persists after 2-adic matching, so it is not only v2(p-1); interpret cautiously (n=30).

Evidence: scripts/z52d_p2_NC0_proth.py, scripts/z52d_p2_NC0_proth2.py, data/z52b/pass2/NC0/proth_10000000.json, data/z52b/pass2/NC0/proth_v2matched.json, data/z52b/raw/var_pr_1e5.txt (U column for small controls)
Next: Compare U/log²p for primes with p-1 = k·2^n·(smooth) against p-1 with a large odd prime factor, at fixed size ≤1e6, residue-matched mod 840.

### Z0922 — Exceptions are about dispersion, not mean: squarefree-ES (mean 19.8) has 3 exceptions, 20/p (mean 26.4) has 60 still occurring at 9·10⁴
Per family (16 repo families, p≡1 (4), p∈(5e4,1e5]): among the 10 families with an exception ≤1e5, Spearman(CV, last exception) = +0.86 (p=0.002), i.e. the high-dispersion families have later last exceptions, which is the direction the item predicts; but Spearman(mean, last) = −0.94 (p=5e-5), so mean and CV are confounded across these 10 points and the item's 'dispersion, not mean' claim is not separated. Families with mean 19–32 and no exception at all (x|y, z≤n²) show the mean alone does not decide.

Evidence: scripts/z52d_p2_NC0_families.py, data/z52b/pass2/NC0/families_summary.json, data/z52b/raw/var_pr_1e5.txt
Next: Get the family table for all 50+ families over p≤1e6 and fit log(last exception) on (log mean, CV) jointly.

### Z0651 — Result: least certificate-family size s(p) has a p-independent distribution (median 22, 99% ≤ ~200) and the CRT model predicts its maximum
Chunked least-family computation for all hard-class primes (p≡1,121,169,289,361,529 mod 840) in [1e7,1e9): ~1.57 M primes, all solved with s≤5000 (0 unsolved). Median s = 22 and 99% quantile 197–230 in every 1e7 block, matching the 1e8 values in the item. Maximum over [1e7,1e8) was 2814 at 53049049 (as in the item); the new maximum in [1e8,1e9) is s = 3092 at p = 393858721 (second 2451 at 486915361). The CRT model predicts ≈3·10³ for 1e9, consistent with this.

Evidence: scripts/z52d_p2_NC0_leastfam_chunk.py, data/z52b/pass2/NC0/leastfam_*.json, data/z52b/pass2/NC0/leastfam_*.log
Next: Check whether 393858721 and 53049049 are near-square (cf. NEAR_SQUARE.md) and whether their minimal certificate families are the same type.

### Z0353 — FF analogue of hard-prime structure: P with P − 1 'smooth' (many small-degree factors)
Ran the F_q[T] ES engine (A=T, 3 monic denominators) over all monic irreducible P with T∤P: q=5 deg≤6 (failures 2,2,1,0,0), q=7 deg≤5 (failures 6,21,25,16 of 21,112,588,3360). At q=7, n=4,5 the failure rate rises monotonically with the number of irreducible factors of P−1 (n=5: 0/560 at 1 factor, 2/1162, 6/1057, 5/448, 3/133 at 5 factors; mean #factors 3.56 failing vs 2.53 ok). The 'P−1 has an F_5-root' pattern found at q=5 fails at q=7 (9 of 68 failing P have no root), and there is no degree-matched control yet.

Evidence: scripts/z52d_p2_NC0_Z0353.py, scripts/bs_ff_es.py, data/z52b/pass2/NC0/sub/Z0353_out.txt, data/z52b/pass2/NC0/sub/Z0353_q7_out.txt, data/z52b/pass2/NC0/sub/md_G1.md
Next: Port es_solutions to C and run q=7 and q=11 at n=6 with a profile-matched control on P−1 factor degrees.

### Z0323 — k-term FF: ES_q with 4 monic terms — does an FF finite covering exist for all q?
Over F_5 (A=T), the 3-term engine fails on 5 irreducible P (deg 2: 2, deg 3: 2, deg 4: 1) and succeeds for all deg 5,6 (2580). A 4-term search with X1,X2 of degree ≤ n−1 (sufficient, not complete) finds nothing, but widening to degree ≤3 (n=2,3) and ≤4 (n=4) gives exact 4-term witnesses for all 5 (identity checked by assert), e.g. T/(T²+2) = 1/T + 3/(T(T²+2)) (repeated denominators, using 5=0); for P=T⁴+T²+2T+2 the witness has denominators of degrees 3, 4, 7 and 13. So the 3-term failures are removed by 4 terms at this size, with largest witness denominator degree ≈ 3n for n=4.

Evidence: scripts/z52d_p2_NC0_Z0323.py, scripts/z52d_p2_NC0_Z0323_wide.py, data/z52b/pass2/NC0/sub/Z0323_wide_out.txt, scripts/bs_ff_es.py
Next: Check whether the 5 witnesses can be chosen with pairwise-distinct denominators (apply the Z0047 distinctness filter to the 4-term search at deg ≤ n+1).

### Z0896 — Signed sibling 4/n = 1/x + 1/y − 1/z: count fingerprint
Exact divisor-form counter (scripts/z52d_p2_NC0_Z0896.c: (d-cy)(cz+d)=d^2 with c=4x-p, d=px; brute-force check on p<=37 passes) gives S(p)=#{x<=y, z<=p^2} for all 8977 primes p=1 mod 4 up to 2e5, with S(p)>=1 always. Regressing log(S+1) on (1, log p, loglog p, alpha*log L_Q(chi_p)) gives alpha=+0.33 (R^2-gain 0.42, Q=31), while the ES count U gives alpha=-0.30 (R^2-gain 0.49): the signed count follows the chi_p law with opposite sign. Residuals of S and U are anticorrelated (Spearman -0.59 after growth removal, -0.34 after the chi_31 adjustment, p~3e-247).

Evidence: scripts/z52d_p2_NC0_Z0896.c, scripts/z52d_p2_NC0_Z0896_fit.py, data/z52b/pass2/NC0/sub/Z0896_fit.json, data/z52b/pass2/NC0/sub/Z0896_S_2e5.txt, data/z52b/pass2/NC0/sub/md_G2.md (section Z0896)
Next: Vary the z-cap (p^1.5, p^3) and split by p mod 8 to see whether the opposite-sign chi_p law and the residual anticorrelation survive.

### Z0961 — Hardness vs the order of 10 mod p (decimal period) — category check
Partial Spearman of the U-residual (8966 primes p=1 mod 4, p<=2e5) with ord_p(10)/(p-1), given (2/p),(5/p): +0.135 (p~8e-38; 200 shuffled nulls sd 0.01). Given all 15 quadratic symbols (q/p), q<=47, it is still +0.068 (p~1e-10), so the signal is not carried by quadratic characters. The U-residual is much lower where 10 has index 8 in (Z/p)^* (mean -0.20, 273 primes; index 6: -0.088; index 1: +0.038), pointing at higher power-residue structure of 10; the same partial for ord_p(3) is +0.36 given (2/p),(5/p) and needs the same controls.

Evidence: scripts/z52d_p2_NC0_Z0961.py, data/z52b/pass2/NC0/sub/Z0961_partial.json, data/z52b/pass2/NC0/sub/md_G2.md (section Z0961)
Next: Add mod-840 fixed effects and quartic/octic residue symbols of 10 (and 3) as controls; if partial >=0.05 survives, write it up as a higher-character signature (FRONTIER 2.1).

## All outcomes
- Z0739 [needs-compute→interesting] Last-failure sequence by numerator m (7..48) is not in OEIS
- Z0752 [needs-compute→nothing] Last 16/p failure 83449 and last 12/p failure 12241: next-term prediction
- Z0848 [needs-compute→interesting] Independence heuristic predicts unbounded Vmin; data show a plateau at 116 — test it
- Z0863 [needs-compute→interesting] No-3 solutions (3 ∤ xyz) fail only at 3 and 241
- Z0814 [needs-compute→interesting] Proth-type primes k·2^n + 1 with small k as an ES-hardness test bed
- Z0949 [needs-compute→nothing] Targeted count at A400619's 119 945 383 009 (too big for exhaustive count): partial certif
- Z0474 [needs-compute→nothing] Feature: independence of witness events
- Z0922 [needs-compute→interesting] Exceptions are about dispersion, not mean: squarefree-ES (mean 19.8) has 3 exceptions, 20/
- Z0877 [needs-compute→nothing] Primitive-failure primes vs R-zeros and Type-A failures
- Z0651 [needs-compute→interesting] Result: least certificate-family size s(p) has a p-independent distribution (median 22, 99
- Z0687 [needs-compute→needs-compute] U(232 792 561) = 276: the lcm(1..19)+1 prime is hard but not extreme
- Z0264 [needs-compute→nothing] Categorified ES over N[T]: identities with non-negative coefficient polynomials, evaluated
- Z0524 [needs-compute→nothing] Between: Ternary Egyptian for numerators m with all denominators in an AP
- Z0470 [needs-compute→nothing] Feature: finite escalation / certificate threshold (290, 451, Graham's 77)
- Z0609 [needs-compute→nothing] Feature: structure of the exceptional set at composite n
- Z0353 [needs-compute→interesting] FF analogue of hard-prime structure: P with P − 1 'smooth' (many small-degree factors)
- Z0047 [needs-compute→nothing] ES over F_q[T] with the extra condition 'distinct denominators' — equivalent or not?
- Z0323 [needs-compute→interesting] k-term FF: ES_q with 4 monic terms — does an FF finite covering exist for all q?
- Z0773 [needs-compute→nothing] ESC(p) as a certificate count at primes — calibrate ESC(p)/log²p
- Z0779 [needs-compute→nothing] A segmented word sieve to 10¹⁰ for per-n counts
- Z0786 [needs-compute→nothing] Number of elliptic curves of conductor p (or 4p, 8p, 16p) vs U(p)
- Z0896 [needs-compute→interesting] Signed sibling 4/n = 1/x + 1/y − 1/z: count fingerprint
- Z0917 [needs-compute→covered] Type number of quaternion orders vs ES counts
- Z0961 [needs-compute→interesting] Hardness vs the order of 10 mod p (decimal period) — category check
- Z0989 [needs-compute→nothing] Resultants between identities
- Z1013 [needs-compute→nothing] Rational reconstruction
- Z1017 [needs-compute→nothing] Semigroup holes
- Z1060 [needs-compute→nothing] Polynomial recurrence selectors
- Z1064 [needs-compute→nothing] CRT covering radius
- Z1069 [needs-compute→nothing] Logarithmic weights tuned to rare witnesses
- Z1078 [needs-compute→nothing] Determinantal matching encodings
- Z1058 [needs-compute→nothing] Spectral gaps of certificate transitions
- Z1082 [needs-compute→nothing] Epsilon-net search portfolios
- Z1083 [needs-compute→nothing] Discrepancy-balanced family splits
- Z1088 [needs-compute→nothing] Combinatorial word lines
- Z1089 [needs-compute→nothing] Residue graph homomorphisms
- Z1090 [needs-compute→nothing] Base-digit automata
- Z1093 [needs-compute→nothing] Weighted automata for word height
- Z1094 [needs-compute→nothing] Synchronizing words for congruences
- Z1095 [needs-compute→nothing] Carry cellular automata
- Z1107 [needs-compute→nothing] Toric ideals of monomial substitutions
- Z1110 [needs-compute→nothing] Sandpile groups as residue containers
- Z1112 [needs-compute→nothing] Nonbacktracking certificate walks
- Z1114 [needs-compute→nothing] Graph covers and congruence refinement
- Z1115 [needs-compute→nothing] Random spanning-tree exploration
- Z1116 [needs-compute→nothing] Discrete Morse reductions
- Z1118 [needs-compute→nothing] Nerves of parametrization charts
- Z1120 [needs-compute→nothing] Termination orders for identity search
- Z1122 [needs-compute→nothing] Scheduling complementary searches
- Z1123 [needs-compute→nothing] Combinatorial games on residual fractions
- Z1131 [needs-compute→nothing] Cavity messages on factor graphs
- Z1136 [needs-compute→nothing] Modular energy landscapes
- Z1143 [needs-compute→nothing] Arithmetic spectral outliers
- Z1145 [needs-compute→nothing] Adiabatic encodings of bounded ES search
- Z1146 [needs-compute→nothing] Tensor-network contraction of residue constraints
- Z1148 [needs-compute→nothing] Holographic changes of basis
- Z1164 [needs-compute→nothing] Adelic height bookkeeping
- Z1167 [needs-compute→nothing] Convex relaxations of bounded searches
- Z1174 [needs-compute→nothing] Finite Fourier uncertainty
- Z1176 [needs-compute→nothing] SAT encodings of bounded denominator search
- Z1177 [needs-compute→nothing] SMT over mixed integer structures
- Z1179 [needs-compute→nothing] Counterexample-guided identity synthesis
- Z1181 [needs-compute→nothing] Equality saturation for rational identities
- Z1183 [needs-compute→nothing] Constraint propagation on factor domains
- Z1185 [needs-compute→nothing] Proof complexity of bounded failures
- Z1188 [needs-compute→covered] Trusted-kernel pipelines
- Z1190 [needs-compute→nothing] Algorithmic simplicity of difficult instances
- Z1196 [needs-compute→nothing] Parameterized complexity by factor count
- Z1197 [needs-compute→nothing] Treewidth of arithmetic factor graphs
- Z1198 [needs-compute→nothing] Meet-in-the-middle divisor selection
- Z1200 [needs-compute→nothing] Bitset propagation of attainable residues
- Z1201 [needs-compute→nothing] Decision diagrams for factor subsets
- Z1204 [needs-compute→nothing] Arithmetic-circuit complexity
- Z0012 [needs-compute→nothing] Genus-1 coordinate rings: ES over F_q[x,y]/(E) with sign at the point at infinity
- Z0093 [needs-compute→nothing] ES in rings of integers of CM fields with cone from the maximal real subfield
- Z0154 [needs-compute→nothing] Riemann–Hurwitz integrality: a surface subgroup of Δ(x,y,z) of index d needs n | d(n − 4)
- Z0157 [needs-compute→nothing] Brieskorn links: ES solutions never give integral homology spheres
- Z0272 [needs-compute→needs-compute] ES on average over number fields: for random real quadratic K, how often does rational ES 
- Z0292 [needs-compute→needs-compute] Spectral world: ES as a statement about eigenvalues of the Laplacian on the triangle orbif
- Z0357 [needs-compute→nothing] ES as an integer-programming feasibility problem: divisor enumeration per p; flatness idea
- Z0948 [needs-compute→nothing] Σ_{n ≤ N} f(n) grows faster than N log³N in range (ratio 7.6 → 19.6 for N = 10³ → 3·10⁴)
