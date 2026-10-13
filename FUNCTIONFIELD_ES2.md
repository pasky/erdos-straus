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

Slice tests for other (q, A) (same tool `scripts/ff2_slice.c`, x ≡ 1 off the A-primes): q = 3, A = T²+1: 28/72
units u mod (T²+1)² uncovered; A = T³: 35/54 mod T⁴; A = T: 0/54 (consistent with Thm 6.4). q = 4, A = T²: 0/192
mod T⁴ (W' = all primes of degree ≤ 2): the q = 4 obstruction, if any, is not in this slice.

### 0.2 Towards a proof that x* ∈ O(3, T²) (work in progress)

Point: x*_c ≡ 1 at every prime ℓ ≠ T, x*_c ≡ u := 1 + cT (mod T^∞) (u a polynomial; c ∈ F_q^*). q odd, A = T^k,
k ≥ 2. A family F = (E; t_a, a0; t_b, b0) valid at x*, L = lcm(a0,b0) = T^j L', T ∤ L', g = gcd(a0,b0) = T^γ g'.
(F1) T^{k+j}L' | P + E, so E ≡ −1 − cT (mod T^{k+j}) and E ≡ −1 (mod L'); T ∤ E; P ≡ 1 (mod E).
(F2) mod E: P ≡ 1, X ≡ T^{−k}; a ≡ a0 (types 0,1) or (T^k a0)^{−1} (types 2,3). So E | a0 + b0 (Case A, both
types on the same side) or E | T^k a0 b0 + 1 (Case B, mixed; then lc(E) = 1 since the two terms have distinct
degrees).
**Case A is impossible (PROVED, sketch to be written out):** with g removed (a1 = a0/g, b1 = b0/g, E | a1 + b1),
E + 1 = T·L'·H forces deg E ≥ 1 + deg a1' + deg b1' (primes-to-T parts), hence T^α ∥ a1 with α ≥ 1 (WLOG) and
T ∤ b1; comparing EF = a1 + b1 with E ≡ −(1 + cT) (mod T^{α+2}) forces b1 = 1, L' = a1' = 1, E = −(1 + cT) and
(−c)^α = −1; then lc(E) = −c while all Case A sums have two terms of distinct degree (lc 1), so c = −1,
contradicting (−c)^α = −1.
**Case B** reduces to: for some L' (monic, T ∤ L'), j ≥ 0, g | T^j L' with T^γ ∥ g, γ ≤ j, N := k + j − 1, the
polynomial D := 1 + T^{N+1}L'g has a monic divisor E with E ≡ −(1+cT) (mod T^{N+1}), E ≡ −1 (mod L') and monic
cofactor. Since deg D < 2·deg(T^{N+1}L'), E or its cofactor is the least CRT representative (ρ resp. ρ'). Search:
`scripts/ff2_caseB.py`.
Case B normal form (PROVED algebra, q odd, k = 2 written; general k: N = k + j − 1): writing
E = T^{N+1}Z − (1 + cT) and E' = (T^{N+1}Z' − 1)/(1 + cT) (Z monic, lc Z' = c; Z, Z' ≠ 0 forced), Case B is
equivalent to the identity
  (1 + cT)·L'g = T^{N+1}ZZ' − Z − (1 + cT)Z'   (****)
with T^N Z ≡ c, T^N Z' ≡ −c (mod L'), (1 + cT) | T^{N+1}Z' − 1, g | T^{N−1}L'. Consequences proved so far:
j = 0 impossible; Z + Z' = 0 impossible; L' | Z + Z'; z ≠ z' and z + z' + 1 ≤ 2 deg L' ≤ 2 max(z, z');
g = T·H'·Z − (Z + Z')/L' where E' = −1 + T L' H'. No contradiction in general yet.
Search (`scripts/ff2_caseB.py`, sanity-checked: it re-finds the family E = T²+2T+2, a0 = 1, b0 = T² for
u = 1+T+2T²): **no Case B family for u = 1 + cT, c = ±1, with deg L' ≤ 5, j ≤ 5** (EVIDENCE).
Observation: the covered T²-digit is d = 2 = −c² in u ≡ 1 + cT + dT² (mod T³), via the single family
E = T² − cT − 1 = −(1 + cT − T²) (a0 = b0 = T, j = 1, D = 1 + T⁴ = (T²+T−1)(T²−T−1)), which covers the whole
cylinder.
