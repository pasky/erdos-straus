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
**Caveat (found later, §0.2):** this test, like ffl_tree, only uses families with E | W, i.e. E built from the
primes of W. At points x ≡ 1 off T, families with E having large prime factors are valid deterministically
(P ≡ 1 mod E), and they do cover many lifts (random search: Case B families with L' = T² − 1 cover e.g.
u ≡ 1 + 2T + 2T³ + T⁴ + 2T⁵ + 2T⁶ mod T⁷). So the slice 'uncovered' counts and the tree plateau overstate the
obstruction: **the plateau of the ffl_tree search is (at least partly) an artefact of E | W**, not evidence of an
obstruction of positive measure.

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

**Status of x* (CONJECTURE + EVIDENCE).** For the exact point u = 1 + cT, `ff2_caseB.py 3 2 c 7 8` finds **no**
Case B family with deg L' ≤ 7, j ≤ 8, for both c = 1 and c = 2 (`ff2_caseB.py 3 2 c 7 8`). With Case A
excluded (proved), this is evidence for **Conjecture 0.2: x*_c ∈ O(3, T²); hence ES₃(T², ·) has no finite linear
covering** (char 3 would then share the "lottery" status of char ≥ 5 for k = 2, although its failures die out
at n = 6 in the data). A proof needs: no monic E ≡ −(1 + cT) (mod T^{N+1}), E ≡ −1 (mod L') dividing
D = 1 + T^{N+1+γ}L'g' (g' | L', 0 ≤ γ ≤ N − 1) with monic cofactor; equivalently (TL'H' − 1) | T^{N+γ}g' + H'
with L'H'(1 + cT) ≡ c (mod T^N), lc H' = 1. Why u = 1 + cT is special: x ≡ 1 at every prime ≠ T makes
validity of every family a deterministic (non-lottery) condition, and the T-adic class −(1 + cT) is "small"
(as −1 is in O140 Prop 4.1); generic lifts u are heuristically covered (expected number of covering Case B
families Σ_{N,ℓ} poly(N+ℓ)·q^{−N} diverges over ℓ).

## 1. (a) Non-linear families in char ≥ 5: what they must look like

**Proposition 1.1 (n-dependent linear families need moduli of degree ≥ n/2 − O(log n); PROVED, char ≥ 5).**
Fix q (char ≥ 5) and A of degree k. For each large n let 𝓕(n) be any collection (of any size) of linear families
(E; t_a, a0; t_b, b0), whose data may depend on n, such that every W_F (F ∈ 𝓕(n)) divides one modulus W(n) with
D(n) := deg W(n) ≤ n/2 − log_q(D(n) + 2) − 1. Then for every large n some irreducible P of degree n is not
covered by 𝓕(n).
*Proof.* By Fact 5.2 the number of irreducible P ≡ 1 (mod W(n)) of degree n is
≥ q^n/(nΦ(W)) − (D + 2)q^{n/2}/n > 0, because Φ(W) ≤ q^D and q^{n/2} > (D + 2)q^D. Fix such a P and F ∈ 𝓕(n).
Since deg a0 + deg b0 + k ≤ D < n/2 and deg E ≤ D, the four types have pairwise distinct degrees and lc(s) is as
in Lemma 6.2, so F is valid at P iff it is valid on the class P ≡ 1 (mod W_F) — and O140 Prop 4.1 says it is
not (its proof uses only W_F | W and the degree comparisons above). ∎
So any proof of ES_q(A, ·) in char ≥ 5 through families whose validity is a congruence condition must use
moduli of degree ≥ (1/2 − o(1))·n, i.e. of size ≥ |P|^{1/2 − o(1)}. At that scale a class mod W_F contains
≤ q^{n/2} polynomials of degree n, and the families are individual Type II data in disguise: this is B2/B3
(the lottery scale) proved, not assumed, in F_q[T]. It is the function-field form of "no covering with moduli
below √p"; over Z the corresponding statement would need primes ≡ 1 (mod m) below p with m ≈ √p (Linnik/GRH),
which Weil supplies here unconditionally.

**What a non-linear family would need (Assessment).** By Lemma 1.3 a, b | PX, so only P, X and divisors of X
can occur; Frobenius twists P^σ (q = p^r) and powers P^m (m ≥ 2) cannot divide PX (degree n each, coprime to
P). Non-formal input can therefore enter only (i) through E (deg E < n; e.g. E built from P − P^σ, or from the
Frobenius residues T^{q^j} mod P), or (ii) through a factorisation of X = (P + E)/A that is forced by an identity.
(ii) is the only deterministic source of divisors; I found no identity forcing X to factor for P ≡ 1 (mod W)
other than congruences (which give back linear families). (i): with E | P^σ − P one has P ≡ P^σ (mod E), which
gives nothing at P ≡ 1. Recorded as sparks, not pursued.

## 2. (b) What grows with n (Assessment)

Exactly the number of Type II data with deg(Aab) ≤ n, ≈ n³ (per unit of q^{−k} weight); each datum is a
congruence of modulus degree ≈ n − deg d, so the solution count of a fixed P is a sum of ~q^{n} indicator
functions with mean C·n³/q^k (FUNCTIONFIELD_ES §7). Any equidistribution/cohomological count at fixed P has an
error at least the square root of the number of data it averages over, i.e. ≥ q^{cn}, against a main term
poly(n): B3 in its sharpest form. Prop 1.1 shows the deterministic (congruence) alternative needs moduli of
degree ≥ n/2. The only regimes left are a structural (non-counting, non-congruence) mechanism, or the special
small characteristics where O(q, A) = ∅ (§0).

## 3. (d) Degree parity for q ≡ 3 (mod 4)

**Proposition 3.1 (PROVED).** No finite linear covering can distinguish degree parities: by Lemma 6.2 the
validity of a linear family at P depends only on P mod W_F once n ≥ n_F. Hence "parity obstruction classes"
(a class mod W covered for one parity of n and not the other) do not exist for linear coverings; O(q, A) is a
subset of R̂^* with no degree data. The Jacobi sign of Prop 4.1 (FUNCTIONFIELD_ES) does depend on n, but it is
a property of the individual Type II datum, not a validity condition, so it cannot obstruct a congruence family.
EVIDENCE: failures for q = 7, A = T (6, 21, 25, 16, 4, 0 at n = 2..7) and q = 3, A = T² (3, 2, 2, 0 at n = 3..6, 0
to n = 15) show no parity pattern.
Independent brute-force check of Case A (`scripts/ff2_caseA_check.py`, all monic a0, b0 of degree ≤ 4, all E | a0+b0
with the achievable leading coefficients): 0 Case A families at u = 1 + T and u = 1 + 2T; sanity: 6 hits at
u = 2 + T (degree ≤ 3).
Necessary condition from quadratic reciprocity (PROVED, q = 3): in Case B at x*, E(0) = E'(0) = −1 and
T^{N+1+γ}L'g' ≡ −1 (mod E) give (deg E + 1)·deg D ≡ deg E (mod 2); hence deg D, deg E, deg E' are all even.
All further Jacobi-symbol relations I tried (e.g. ((1 + cT)/E) computed via reciprocity and via
1 + cT ≡ T^{N+1}Z mod E) are automatically consistent, so quadratic symbols alone will not kill Case B.
Control (EVIDENCE): two *generic* lifts in the same cylinders, u = 1 + T + T³ + 2T⁴ + ... (digits
10120120121011) and u = 1 + 2T + T³ + ... (digits 20211012201021), also get **0** Case B families for
deg L' ≤ 6, j ≤ 8. So x* is not visibly special inside its cylinder: within the searched range the whole
cylinders u ≡ 1 + cT + dT² (mod T³), d ∈ {0, 1}, are almost entirely uncovered at x ≡ 1 off T, while
individual lifts are covered by sporadic large families (e.g. L' = T² − 1, g' = T − 1, N = 6). If the number
of covering families of a generic u is finite on average, O(3, T²) has positive Haar measure inside this slice and
the ≈ 1 % tree plateau would be genuine; if it diverges, O may be empty or null. Both are open (Assessment:
the measure question is the right next computation — count covered cylinder mass by (N, deg L')).
**Covered mass (EVIDENCE, `scripts/ff2_caseB_measure.py 3 1 0 LMAX 5`).** Fraction of the cylinder
C = {u ≡ 1 + T (mod T³)} covered by Case B families (union of the cylinders u ≡ −E mod T^{N+1}), j ≤ 5:
deg L' ≤ 1: 0.037; ≤ 2: 0.111; ≤ 3: 0.185; ≤ 4: 0.198; ≤ 5: 0.198 (sum with multiplicity 0.43; 10 cylinders).
So generic lifts are covered with probability ≈ 0.2 at this size; whether the union tends to full mass as
deg L', j → ∞ decides whether O(3, T²) ∩ slice has positive measure. (Case A cannot cover this slice for u near
1 + cT by the §0.2 argument only at u = 1 + cT exactly; for general lifts Case A is checked by ff2_caseA_check.)
