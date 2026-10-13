# FUNCTIONFIELD_ES2 — function-field Erdős–Straus: extinction mechanisms, open cases q = 3, 4 (O166)

Status: in progress (O166). Builds on FUNCTIONFIELD_ES.md (O161 + R161), notation and Lemma numbers from there
(ES_q(A,P), NC, Lemma 1.3 e-slice criterion, linear families §6.2, Lemma 6.2, Prop 4.1 of O140).
Scripts `scripts/ff2_*`. ES is not solved anywhere; nothing here bears on ES over Z except as a model.

Plan (task O166): (a) non-linear / non-formal families in char ≥ 5 (class P ≡ 1 mod W); (b) geometric control
at fixed q, n → ∞; (c) q = 3, A = T² and q = 4, A = T²; (d) degree-parity obstructions for q ≡ 3 (mod 4).

## 0. Iteration log (constructions tried, which barrier hypothesis they hit, the modification)

### 0.1 (c) q = 3, A = T²: the covering tree plateaus — hunting an obstructed profinite point

*Framework (PROVED, compactness; makes "is there a finite linear covering" a pointwise question).* Let
R̂ = lim R/W and R̂^* its unit group. A linear family F is valid at x ∈ R̂^* if x mod W_F lies in its validity set
(Lemma 6.2; a congruence condition, independent of n ≥ n_F). The obstructed set
O(q, A) := {x ∈ R̂^* : no linear family is valid at x} is closed. A finite covering (hence a proof of ES_q(A,·)
by Lemma 6.2 + a finite check) exists iff O(q, A) = ∅: if O = ∅, the validity sets (open) cover the compact R̂^*,
so finitely many do; conversely if x ∈ O, every class mod W containing x contains irreducible P of every large
degree (Dirichlet, Fact 5.2) and no family of a finite covering is valid there. O140 Prop 4.1 is the statement
1 ∈ O(q, A) for char ≥ 5.

*Tree data (EVIDENCE).* `ffl_tree 3 100 "100*11*12" refine T,T+1,T+2,T²+1,T²+T+2,T²+2T+2,T,T+1,T+2,T²+1`:
uncovered density 0.0115 at depth 6 (NTH = 13) and 0.0106 at depth 8 (NTH = 17). Plateau. The 3829 uncovered
classes at depth 6 (`scripts/ff2_tree.c`, FFL_ALLUNC) concentrate on P ≡ 1 at the non-A primes
(mod (T±1)², T²+1, ...: residue 1 is the most frequent in every component), with P mod T³ spread over
1+T, 1+2T, 2+T+T², 2+2T+T², ... .

*Slice test (EVIDENCE).* x_u := (x ≡ u mod T^∞, x ≡ 1 at every prime ≠ T). `scripts/ff2_crtpoint.py` +
`scripts/ff2_point.c` test every u mod T^e against all linear families with W_F | T^e·W' (W' = (T+1)³(T+2)³
(T²+1)(T²+T+2)(T²+2T+2)·four cubic primes, NTH = 20). For e = 5, **every** lift of u ≡ 1+T, 1+T+T², 1+2T,
1+2T+T² (mod T³) is uncovered, as are most lifts of 2+T+T², 2+2T+T², 2+2T+2T². Candidate obstructed points.
