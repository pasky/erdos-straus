# FUNCTIONFIELD_ES2 — function-field Erdős–Straus: extinction mechanisms, open cases q = 3, 4 (O166)

Status: in progress (O166). Hostile review R166 (`reviews/functionfield-es2-review.md`): no FATAL defects. The
repairs D1 to D13 are applied in place, marked "(R166 repair)". Builds on FUNCTIONFIELD_ES.md (O161 + R161), notation and Lemma numbers from there
(ES_q(A,P), NC, Lemma 1.3 e-slice criterion, linear families §6.2, Lemma 6.2, Prop 4.1 of O140).
Scripts `scripts/ff2_*`. ES is not solved anywhere; nothing here bears on ES over Z except as a model.

Plan (task O166): (a) non-linear / non-formal families in char ≥ 5 (class P ≡ 1 mod W); (b) geometric control
at fixed q, n → ∞; (c) q = 3, A = T² and q = 4, A = T²; (d) degree-parity obstructions for q ≡ 3 (mod 4).

## 0. Iteration log (constructions tried, which barrier hypothesis they hit, the modification)

### 0.1 (c) q = 3, A = T²: the covering tree plateaus — hunting an obstructed profinite point

*Framework (PROVED, compactness; makes "is there a finite linear covering" a pointwise question).* Let
R̂ = lim R/W and R̂^* its unit group. A linear family F is valid at x ∈ R̂^* if x mod W_F lies in its validity set
(Lemma 6.2; a congruence condition, independent of n ≥ n_F). (R166 repair, D3: Lemma 6.2 as stated only says
"depends on P mod W". Independence of n follows from its proof. The congruences A·a0, A·b0 | P + E, the residue
of s mod E (from P mod E and X mod a0E, b0E, LE), lc(s) (1 for distinct types, lc(a0 + b0) or lc(L/a0 + L/b0)
for equal types) and "s ≠ 0" contain no n. So the validity set V_F ⊂ R̂^* is a well-defined clopen set.) The
obstructed set
O(q, A) := {x ∈ R̂^* : no linear family is valid at x} is closed. A finite covering exists iff O(q, A) = ∅: if O = ∅, the validity sets (open) cover the compact R̂^*,
so finitely many do; conversely if x ∈ O, every class mod W containing x contains irreducible P of every large
degree (Dirichlet, Fact 5.2) and no family of a finite covering is valid there. O140 Prop 4.1 is the statement
1 ∈ O(q, A) for char ≥ 5. (R166 repair, D2: a finite covering proves ES_q(A, P) for all P of degree ≥ max n_F
by Lemma 6.2. The smaller degrees need a finite check, and that check can find failures: for q = 3, A = T², ES
fails at n = 3, 4, 5.)

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
obstruction. *Assessment* (R166 repair, D4: label added): **the plateau of the ffl_tree search is (at least partly)
an artefact of E | W**. The tree data are therefore neither evidence for nor against O(3, T²) having positive
measure. (R166 repair, D4) "Valid deterministically" holds only on the measure-0 slice x ≡ 1 off T. At a generic
point of an uncovered leaf, a family with a new prime ℓ | E is valid only on a sub-class mod ℓ.

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
**Case A is impossible (PROVED; full proof below, R166 repair D1).** *Original sketch (superseded; its step
"forces b1 = 1, L' = a1' = 1" is false before the leading-coefficient condition is used. For example q = 3,
k = 2, c = 1, a0 = 1, b0 = T³ + T, E = −(T³ + T + 1) satisfies every congruence and is excluded only by lc. The
original sketch read:) with g removed (a1 = a0/g, b1 = b0/g, E | a1 + b1),
E + 1 = T·L'·H forces deg E ≥ 1 + deg a1' + deg b1' (primes-to-T parts), hence T^α ∥ a1 with α ≥ 1 (WLOG) and
T ∤ b1; comparing EF = a1 + b1 with E ≡ −(1 + cT) (mod T^{α+2}) forces b1 = 1, L' = a1' = 1, E = −(1 + cT) and
(−c)^α = −1; then lc(E) = −c while all Case A sums have two terms of distinct degree (lc 1), so c = −1,
contradicting (−c)^α = −1.*
*Proof (R166 repair D1; checked by R166).* Validity at x*_c forces T^{k+j} | u + E and L' | 1 + E. Hence T ∤ E,
x ≡ 1 (mod E), gcd(E, L) = 1, and in Case A, E | a1 + b1 (a0 = g a1, b0 = g b1). Let s be the family sum.
(1) E + 1 ≡ −cT (mod T^{k+j}) with k + j ≥ 2, so E + 1 = T·L'·H with T ∤ H ≠ 0. Hence
deg E ≥ 1 + deg L' = 1 + deg g' + deg a1' + deg b1' (' = prime-to-T part). Take deg a1 ≥ deg b1 (WLOG) and
T^α ∥ a1. Then deg E ≤ deg(a1 + b1) ≤ α + deg a1' gives α ≥ 1 + deg g' + deg b1' ≥ 1. So T ∤ b1,
j = v_T(L) = γ + α, and k + j ≥ α + 2.
(2) F := (a1 + b1)/E has deg F ≤ α − 1 − deg b1 − deg g'. Mod T^α we have −(1 + cT)F ≡ b1. So
(1 + cT)F + b1 ≡ 0 (mod T^α) has degree ≤ α, i.e. (1 + cT)F + b1 = μT^α with μ ∈ F_q, and μ = 0 if deg b1 ≥ 1.
(3) a1 = EF − b1 = F(E + 1 + cT) − μT^α with T^{α+2} | E + 1 + cT, so a1' ≡ −μ (mod T²). T ∤ a1' gives μ ≠ 0.
Hence b1 = 1, (1 + cT) | μT^α − 1, μ = (−c)^α, F = (μT^α − 1)/(1 + cT), deg F = α − 1 and lc F = μ/c.
(4) deg a1 ≥ 1 > deg b1, so lc(s) = 1 for every Case A type combination. Then lc(E) = 1, and
lc(E)·lc(F) = lc(a1) = 1 gives μ = c. Also deg E = deg a1 − deg F = 1 + deg a1', so (1) forces g' = 1, deg H = 0
and E = T a1' − 1.
(5) a1 = EF − 1 gives a1'(T^α − TF) = −(F + 1). Using μ = c, (1 + cT)(T^α − TF) = T(T^{α−1} + 1) and
(1 + cT)(F + 1) = cT(T^{α−1} + 1). So a1' = −c, and a1' monic forces c = −1. Then μ = (−c)^α = 1 ≠ −1 = c
(q odd), a contradiction. ∎
Independent check (R166, `scripts/review_ff2_caseA.py`, all divisors E of every leading coefficient,
deg a0, deg b0 ≤ 4 / 3 / 2 for q = 3 / 5 / 7, k = 2, 3): congruence-valid Case A divisors occur, but none
has an admissible lc (`data/review_ff2_caseA_log.txt`).
**Case B** reduces to: for some L' (monic, T ∤ L'), j ≥ 0, g | T^j L' with T^γ ∥ g, γ ≤ j, N := k + j − 1, the
polynomial D := 1 + T^{N+1}L'g has a monic divisor E with E ≡ −(1+cT) (mod T^{N+1}), E ≡ −1 (mod L') and monic
cofactor. Since deg D < 2·deg(T^{N+1}L'), E or its cofactor is the least CRT representative (ρ resp. ρ'). Search:
`scripts/ff2_caseB.py`.
Case B normal form (PROVED algebra, q odd, k = 2 written; general k: N = k + j − 1): writing
E = T^{N+1}Z − (1 + cT) and E' = (T^{N+1}Z' − 1)/(1 + cT) (Z monic, lc Z' = c; Z, Z' ≠ 0 forced), Case B is
equivalent to the identity
  (1 + cT)·L'g = T^{N+1}ZZ' − Z − (1 + cT)Z'   (****)
with T^N Z ≡ c, T^N Z' ≡ −c (mod L'), (1 + cT) | T^{N+1}Z' − 1, g | T^{N−1}L'. Consequences (R166 repair, D5: claimed by O166; proofs not written, not re-derived by R166, and used
nowhere below):
j = 0 impossible; Z + Z' = 0 impossible; L' | Z + Z'; z ≠ z' and z + z' + 1 ≤ 2 deg L' ≤ 2 max(z, z');
g = T·H'·Z − (Z + Z')/L' where E' = −1 + T L' H'. No contradiction in general yet.
Search (`scripts/ff2_caseB.py`, sanity-checked: it re-finds the family E = T²+2T+2, a0 = 1, b0 = T² for
u = 1+T+2T²): **no Case B family for u = 1 + cT, c = ±1, with deg L' ≤ 5, j ≤ 5** (EVIDENCE).
Observation: the covered T²-digit is d = 2 = −c² in u ≡ 1 + cT + dT² (mod T³), via the single family
E = T² − cT − 1 = −(1 + cT − T²) (a0 = b0 = T, j = 1, D = 1 + T⁴ = (T²+T−1)(T²−T−1)), which covers the whole
cylinder.

(R166 repair) Independently reproduced by `scripts/review_ff2_caseB.py`, which uses its own arithmetic, enumerates
(L', j, g) directly, and brute-forces all divisors of D for small cases: 0 Case B families at u = 1 + T and
u = 1 + 2T for deg L' ≤ 7, j ≤ 8 (`data/review_ff2_caseB_log.txt`).

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
(R166 repair, D6) Strength of the evidence. Two generic lifts in the same cylinders also get 0 Case B families
in the same search range (§3). The search therefore does not distinguish x* from generic points, and the EVIDENCE
for Conjecture 0.2 amounts to "no counterexample in a range where generic points have none either". Since the
divergence heuristic predicts that generic u *are* covered, Conjecture 0.2 asserts that x* is non-generic, and
nothing proved here establishes that.

## 1. (a) Non-linear families in char ≥ 5: what they must look like

**Proposition 1.1 (n-dependent linear families need a common modulus of degree ≥ n/2 − O(log n); PROVED,
char ≥ 5).** (R166 repair, D9: title rescoped. The hypothesis bounds deg lcm_F W_F, not the individual W_F.)
Fix q (char ≥ 5) and A of degree k. For each large n let 𝓕(n) be any collection (of any size) of linear families
(E; t_a, a0; t_b, b0), whose data may depend on n, such that every W_F (F ∈ 𝓕(n)) divides one modulus W(n) with
D(n) := deg W(n) ≤ n/2 − log_q(D(n) + 2) − 1. Then for every large n some irreducible P of degree n is not
covered by 𝓕(n).
*Proof.* By Fact 5.2 the number of irreducible P ≡ 1 (mod W(n)) of degree n is
≥ q^n/(nΦ(W)) − (D + 2)q^{n/2}/n > 0, because Φ(W) ≤ q^D and q^{n/2} > (D + 2)q^D. Fix such a P and F ∈ 𝓕(n).
Since k + deg a0 + deg b0 ≤ k + 2 deg L ≤ 2D − k < n (R166 repair, D8: formerly "deg a0 + deg b0 + k ≤ D",
which is false in general because deg a0 + deg b0 = deg L + deg g) and deg E ≤ D, the four types have pairwise distinct degrees and lc(s) is as
in Lemma 6.2, so F is valid at P iff it is valid on the class P ≡ 1 (mod W_F) — and O140 Prop 4.1 says it is
not (its proof uses only W_F | W and the degree comparisons above). ∎
(R166 repair, D7: Fact 5.2 is needed with a constant uniform in W, i.e. only D = deg W enters. That uniform form
follows from Rosen Prop 4.3 (L(u, χ) is a polynomial of degree ≤ D − 1 for χ ≠ χ0 mod W) and Weil's RH (Rosen
Thm 5.10), as derived in FUNCTIONFIELD_ES §5. It gives |nπ(n; W, 1) − q^n/Φ(W)| ≤ (D + 1)q^{n/2} + D. The textbook
Thm 4.8 is usually stated with an O-constant that depends on the modulus. R166 could not access Rosen and
re-derived the bound.)
(R166 repair, D9: the interpretation below is rescoped; the earlier text claimed a bound on individual moduli and
"B2/B3 proved".) So any proof of ES_q(A, ·) in char ≥ 5 that certifies all P of degree n by families whose
moduli divide **a common modulus** W(n) needs deg W(n) ≥ n/2 − O(log n). This is the common-modulus version of the
size barrier, proved unconditionally (Weil supplies the needed prime P ≡ 1 mod W(n)). It says **nothing** about
collections whose individual moduli are small but whose lcm has degree ≥ n/2. For example, families with
deg W_F ≤ n/10 each and lcm of degree ≫ n are not covered by Prop 1.1, since no P ≡ 1 modulo the lcm need
exist. The lottery-scale statement (B2/B3: individual data need moduli of size ≈ |P|^{1/2}) therefore remains
unproved in F_q[T]. *Open question (CONJECTURE-level, not studied):* does every collection of linear families
with max_F deg W_F ≤ (1/2 − ε)n miss some irreducible P of degree n, for large n?
Over Z the common-modulus analogue would need a prime p ≡ 1 (mod m) with m ≈ √p. Unconditionally Linnik gives
only p ≪ m^L (L ≈ 5), and GRH gives p ≪ m² log⁴ m, i.e. m ≈ √p up to log factors (R166 repair, D10: formerly
"Linnik/GRH").

**What a non-linear family would need (Assessment).** By Lemma 1.3 a, b | PX, so only P, X and divisors of X
can occur; Frobenius twists P^σ ≠ P (q = p^r) and powers P^m (m ≥ 2) cannot divide PX (degree n each, coprime to
P). (R166 repair, D13: if P has coefficients in a proper subfield then P^σ = P, which divides PX trivially and
gives nothing new.) Non-formal input can therefore enter only (i) through E (deg E < n; e.g. E built from P − P^σ, or from the
Frobenius residues T^{q^j} mod P), or (ii) through a factorisation of X = (P + E)/A that is forced by an identity.
(ii) is the only deterministic source of divisors; I found no identity forcing X to factor for P ≡ 1 (mod W)
other than congruences (which give back linear families). (i): with E | P^σ − P one has P ≡ P^σ (mod E), which
gives nothing at P ≡ 1. Recorded as sparks, not pursued.

## 2. (b) What grows with n (Assessment)

Exactly the number of Type II data with deg(Aab) ≤ n, ≈ n³ (per unit of q^{−k} weight); each datum is a
congruence of modulus degree ≈ n − deg d, so the solution count of a fixed P is a sum of ~q^{n} indicator
functions with mean C·n³/q^k (FUNCTIONFIELD_ES §7). Any equidistribution/cohomological count at fixed P has an
error at least the square root of the number of data it averages over, i.e. ≥ q^{cn}, against a main term
poly(n): B3 in its sharpest form. Prop 1.1 shows that the deterministic (congruence) alternative needs a common modulus (lcm of the moduli) of
degree ≥ n/2 − O(log n) (R166 repair, D9: formerly "moduli of degree ≥ n/2"; the per-family version is open). The only regimes left are a structural (non-counting, non-congruence) mechanism, or the special
small characteristics where O(q, A) = ∅ (§0).

## 3. (d) Degree parity for q ≡ 3 (mod 4)

**Proposition 3.1 (PROVED; R166 repair, D12: really a Remark that restates the definition of a linear covering).**
(R166 repair, D3/D12: the argument needs the validity set V_F to be the same for all n at least n_F, not merely a function of P mod W (see the D3 note in §0.1). With that, a
finite linear covering is a covering for every large n at once. The statement is restricted to fixed
(n-independent) linear families and says nothing about n-dependent collections (Prop 1.1's setting).) No finite
linear covering can distinguish degree parities: by Lemma 6.2 the
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
T^{N+1+γ}L'g' ≡ −1 (mod E) give (deg E + 1)·deg D ≡ deg E (mod 2); hence deg D, deg E, deg E' are all even. (R166 repair: re-derived and SOUND. The argument uses only u(0) = 1 and
E = -1 mod L', so it holds at every slice point x = 1 off T, not only at x*. It belongs logically to §0.2.)
All further Jacobi-symbol relations I tried (e.g. ((1 + cT)/E) computed via reciprocity and via
1 + cT ≡ T^{N+1}Z mod E) are automatically consistent, so quadratic symbols alone will not kill Case B.
Control (EVIDENCE): two *generic* lifts in the same cylinders, u = 1 + T + T³ + 2T⁴ + ... (digits
10120120121011) and u = 1 + 2T + T³ + ... (digits 20211012201021), also get **0** Case B families for
deg L' ≤ 6, j ≤ 8. So x* is not visibly special inside its cylinder: within the searched range the whole
cylinders u ≡ 1 + cT + dT² (mod T³), d ∈ {0, 1}, are almost entirely uncovered at x ≡ 1 off T, while
individual lifts are covered by sporadic large families (e.g. L' = T² − 1, g' = T − 1, N = 6). If the number
of covering families of a generic u is finite on average, O(3, T²) has positive Haar measure inside this slice
(R166 repair, D11: the slice itself has Haar measure 0 in R̂^*, so this would not by itself make the ≈ 1 % tree
plateau genuine; that is a mass in R̂^*); if it diverges, O may be empty or null. Both are open (Assessment:
the measure question is the right next computation — count covered cylinder mass by (N, deg L')).
**Covered mass (EVIDENCE, `scripts/ff2_caseB_measure.py 3 1 0 LMAX 5`).** Fraction of the cylinder
C = {u ≡ 1 + T (mod T³)} covered by Case B families (union of the cylinders u ≡ −E mod T^{N+1}), j ≤ 5:
deg L' ≤ 1: 0.037; ≤ 2: 0.111; ≤ 3: 0.185; ≤ 4: 0.198; ≤ 5: 0.198 (sum with multiplicity 0.43; 10 cylinders).
So generic lifts are covered with probability ≈ 0.2 at this size; whether the union tends to full mass as
deg L', j → ∞ decides whether O(3, T²) ∩ slice has positive measure. (Case A cannot cover this slice for u near
1 + cT by the §0.2 argument only at u = 1 + cT exactly; for general lifts Case A is checked by ff2_caseA_check.)
(R166 repair, D11: the §0.2 Case A proof uses u = 1 + cT exactly, through T^{α+2} | E + 1 + cT. For other lifts
Case A families are not excluded, so these masses are **lower bounds** for the covered mass, even within the
searched range. R166 reproduced the Case B union masses 0.037, 0.111, 0.185, 0.198 (deg L' at most 1..4, j at
most 5) with `scripts/review_ff2_mass.py`; see `data/review_ff2_mass_log.txt`.)
Extended run (j ≤ 8): union mass 0.042, 0.117, 0.195, 0.210, 0.219, 0.229 for deg L' ≤ 1..6 (sums with
multiplicity 0.06 … 0.53; 58 cylinders). Increments for deg L' = 4, 5, 6: 0.015, 0.009, 0.010 — not clearly
decaying, not clearly summable. Undecided (EVIDENCE either way is weak).

### 0.3 q = 4, A = T² (EVIDENCE)
`ff2_tree 4 100 "100*11*12*13" refine T, T+1, T+ω, T+ω², then the six monic irreducible quadratics, NTH = 13,
depth 6`: 672277 leaves, uncovered density 0.259 (vs 0.43 at depth 3 in O161). Still far from a covering, and
subject to the same E | W limitation; the slice x ≡ 1 off T is fully covered (§0.1), so if O(4, T²) ≠ ∅ its
points are elsewhere. Status: OPEN.
