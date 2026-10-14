# STERILE_EXPLICIT — the function-field class-divisor machinery over ℤ: explicit sterile Mordell points (O219, spark relay Y9)

Status: in progress (O219). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on DEPTH_ASPECT.md §3 ((J)26 Thm 3.1, reviews R178/R187), FF_STERILE_PUSH.md (O216, Lemmas 1.1–1.6, 2.1),
POINTWISE_MORDELL17*.md (= M17, M17B, M17C, M17D), STERILE_STEER.md. Scripts `scripts/se_*`.

## 0. Iteration log

* (I1) Dictionary. O216's Case B tuples (m', g', w, C, v) with m'wC = T^s + v, w + C = g'v are *literally* the ℤ
  P-data of M17 (N-points of Σ^II_N, N = r^K): 4d·a·b = N + e, a + b = c·e. So (m', g', w, C, v) ↔ (4d, c, a, b, e),
  E = L'w − 1 ↔ f = 4acd − 1, Lemma 1.1(i) Ev = T^s + m'w² ↔ ef = N + 4a²d (ET (2.19)), and the FF degree identity
  y + t = max(a, b) ↔ the size relation ce = a + b ∈ (b, 2b]. Every FF route has a ℤ twin (§1, Table 1.2).
* (I2) Continuum steering (`scripts/se_rate.py`, EVIDENCE/Assessment). With sizes a = N^α, c = N^γ, d = N^δ, e = N^ε
  (α + γ + δ + ε = 1 up to O(1/log N), 2α + δ ≤ 1), and a divisor loss τ(m) ≤ C(η)m^η charged where no class
  bound applies, the best route exponent θ*(η) = max_pattern min_route is 0.400 (η = 0), 0.417 (0.1), 0.467 (0.2),
  0.500 (0.25), 0.533 (0.3). ET's four-regime argument tolerates only η ≈ 1/18 (its loss is η·(1 + 4/5) on top of 2/5),
  which is why (J)26's r₀ is a tower. The transplant tolerates η < 1/4. The binding corner is
  a ≈ b ≈ d ≈ N^{1/3}, e ≈ N^{1/6}: balanced triple factorisations of (N + e)/4 with a ≡ −b (mod e), exactly at the
  Coppersmith threshold for the class route (modulus e vs divisor b ≈ m^{1/2} of m = (N+e)/(4a), threshold m^{1/4}).
* (I3) Steering by the barrier: the hypothesis that binds in (I2) is "a class-divisor bound exists only above the
  Coppersmith threshold, below it one pays τ". Violate it: split the size window of the divisor into short
  subintervals. Coppersmith's lattice works in each subinterval once modulus × (number of pieces) exceeds the threshold,
  so the count of divisors of size n^β in a class mod n^ρ is ≤ n^{max(0, β(1−β)−ρ)+o(1)} (Lemma 1.3 below, elementary;
  "Coppersmith interpolation"). With it (`scripts/se_rate2.py`, `se_rate2_subsets.py`; grid EVIDENCE):
  **θ* = 2/5 exactly — ET's exponent — using no divisor bound at all except one: τ₃(N + e) ≤ C₃(η)N^η for single
  integers N + e, tolerated up to η = 0.3** (θ* = 0.400, 0.417, 0.450, 0.500 at η = 0.3, 0.35, 0.4, 0.5).
  Five class routes + the τ₃ route suffice (dropping any one raises θ* to ≥ 0.425). The only τ-dependent corner is
  e = N^{o(1)}, a ≈ b ≈ d ≈ N^{1/3}: literally the balanced triple factorisations of the integers (N + e)/4.

## 1. P-data over ℤ: identities, sizes, and the class-divisor lemma

Notation (M17 §2, DEPTH_ASPECT §3). r an odd prime, N = r^K (K odd). A *P-datum* is a positive integer tuple (a, b, c, d, e)
with **4abd = N + e, a + b = ce**, r ∤ cd, r ∤ ab (in-cell data are primitive: M17 §6 and Lemma 5.1, r-free; R187),
counted with a ≤ b; D_P(N) is their number. f := 4acd − 1, f' := 4bcd − 1. Each datum and its reflection give the P-boxes
−f, −f' (mod r^{(K+1)/2}) (M17 Lemma 2.3). The FF twin is O216's Case B tuple with (m', g', w, C, v) ↔ (4d, c, a, b, e).

**Lemma 1.1 (identities; PROVED, elementary).** For every P-datum:
(i) ef = N + 4a²d, ef' = N + 4b²d; (ii) bf = Nc + a, af' = Nc + b; (iii) ff' = 4c²dN + 1;
(iv) gcd(e, abd) = 1 and e is odd.
*Proof.* (i) e(4acd − 1) = 4ad(a + b) − e = 4a²d + 4abd − e = 4a²d + N. (ii) b(4acd − 1) = c(N + e) − b = cN + ce − b = cN + a.
(iii) (4acd − 1)(4bcd − 1) = 4c²d·4abd − 4cd(a + b) + 1 = 4c²d(N + e) − 4c²de + 1. (iv) A prime p | e with p | abd divides
4abd − e = N = r^K, so p = r, contradicting r ∤ abd; e = 4abd − N is odd. ∎
(i) is the ℤ twin of O216 Lemma 1.1(i) (Ev = T^s + m'w²); (iii) is O173/DEPTH_ASPECT (R2).

**Lemma 1.2 (sizes; PROVED).** If a ∈ [A, 2A), c ∈ [C, 2C), d ∈ [D, 2D) and a ≤ b, then
N/(16AD) < b ≤ N/(2AD), N/(32ACD) < e ≤ N/(ACD), 4ACD − 1 ≤ f < 32ACD, 4a²d ≤ 2N, and 2A²D ≤ N.
*Proof.* 4abd = N + e > N gives b > N/(4ad) > N/(16AD). e ≤ a + b ≤ 2b gives b(4ad − 2) ≤ N, and 4ad − 2 ≥ 2ad, so
b ≤ N/(2ad) ≤ N/(2AD). Then e = (a + b)/c ∈ [b/c, 2b/c]. 4a²d ≤ 4abd = N + e ≤ N + 2b ≤ 2N (b ≤ N/2). A ≤ a ≤ b ≤ N/(2AD). ∎

**Lemma 1.3 (divisors of bounded size in a residue class — Coppersmith/Howgrave-Graham by Minkowski; PROVED, elementary).**
Let n ≥ 1, s ≥ 1, σ ∈ ℤ with gcd(σ, s) = 1, and 1 ≤ D₀ ≤ D₁ real. Let m ≥ 1, k ≥ 0, w = m + k and
X := (D₁ − D₀)/(2s) + 1/2. If
  w^w · n^{m(m+1)/2} · X^{w(w−1)/2} < D₀^{mw},                                                     (Cop)
then n has at most w − 1 divisors E with D₀ ≤ E ≤ D₁ and E ≡ σ (mod s).
*Proof.* Every such E is prime to s, so E | n₁ := ∏_{p∤s} p^{v_p(n)}. Let σ₀ ∈ [0, s) be σ mod s and x̂ an integer nearest to
the midpoint of [(D₀ − σ₀)/s, (D₁ − σ₀)/s]; every E in question is E = σ₀ + s(x̂ + y) with y ∈ ℤ, |y| ≤ X. Take t ∈ ℤ with
st ≡ 1 (mod n₁) and F(y) := y + x̂ + σ₀t. Then sF(y) ≡ E (mod n₁), so E | sF(y), and E | F(y) as gcd(E, s) = 1. Hence E^m
divides g(y) for every g in the ℤ-span 𝓛 of g_i = n₁^{m−i}F^i (0 ≤ i < m) and h_j = y^jF^m (0 ≤ j < k). These have degrees
0, …, w − 1 and leading coefficients n₁^m, …, n₁, 1, …, 1, so the vectors (g_l X^l)_{l<w} of g ∈ 𝓛 form a lattice of
determinant n₁^{m(m+1)/2}X^{w(w−1)/2} in ℝ^w. By Minkowski's convex body theorem (cube [−λ, λ]^w, λ = det^{1/w}) some g ≠ 0
in 𝓛 has |g_l|X^l ≤ det^{1/w} for all l, so |g(y)| ≤ w·det^{1/w} < D₀^m ≤ E^m for |y| ≤ X, by (Cop) and n₁ ≤ n. Since
E^m | g(y), g(y) = 0. g has at most w − 1 roots and E ↦ y is injective. ∎
(m = 1, k = 1 gives: at most one such divisor if 4nX < D₀². The ℤ twin of O216 Lemma 1.5; over ℤ Minkowski replaces
LLL, as we count and do not search.)

**Corollary 1.4 (Coppersmith interpolation; PROVED).** Under the hypotheses of Lemma 1.3 except (Cop), for every integer
J ≥ 1 the number of such divisors is at most J·(w − 1) as soon as (Cop) holds with X replaced by X_J := (D₁ − D₀)/(2sJ) + 1/2.
Asymptotically (n → ∞, D₀ = n^β, s = n^ρ, D₁ = 2D₀) this gives **≤ n^{max(0, β(1−β) − ρ) + o(1)}**: a class-divisor bound
with no divisor-function loss that interpolates between the trivial bound (window/s + 1) and the Coppersmith range
ρ > β(1 − β) (O216 Lemma 1.5's ℤ form; for ρ ≤ 1/4 it is new to the campaign, and it is what removes the binding corner
of (I2)).
*Proof.* Cut [D₀, D₁] into J intervals of length (D₁ − D₀)/J and apply Lemma 1.3 to each, with the common lower bound D₀.
Asymptotics: with w = τm, (Cop) reads (1/2 + o(1)) + τ²(β − ρ − j)/2 < τβ, j = log J/log n; optimising τ = β/(β − ρ − j)
gives the condition ρ + j > β(1 − β). ∎
*Check (EVIDENCE):* `scripts/se_cop_check.py` evaluates (Cop) in exact rational arithmetic and compares J·(w − 1) with
the true count on random highly composite n ≤ 10^{10}, random s, σ, windows: 200 tests, 0 violations (69 tight).

## 2. Route table over ℤ (the twin of O216 Lemma 1.6) and the exponent 2/5

For a dyadic box a ∈ [A, 2A), c ∈ [C, 2C), d ∈ [D, 2D) put E₀ = N/(32ACD), E₁ = N/(ACD) (Lemma 1.2) and
L(A) = Σ_{A≤a<2A} 1/a ≤ ln 2 + 1/(2A). The number of P-data in the box is at most each of (PROVED from Lemmas 1.1–1.4):
| route | data enumerated | then | bound | FF twin |
|---|---|---|---|---|
| H | (a, c, d) | b = (Nc + a)/f | ACD | T0 |
| A | (a, d), e ≡ −N (4ad) | b = (N+e)/(4ad), c = (a+b)/e | (E₁ − E₀)L(A)L(D)/4 + AD | R9a |
| C | (a, d) | f ∣ N + 4a²d, f ≡ −1 (4ad), f ∈ [4ACD−1, 32ACD) | AD·cop(3N, 4AD, f-window) | R4 |
| D | (c, d) | f ∣ 4c²dN + 1, f ≡ −1 (4cd) | CD·cop(32C²DN+1, 4CD, f-window) | R2 |
| E | (a, c) | f ∣ Nc + a, f ≡ −1 (4ac) | AC·cop(2CN+2A, 4AC, f-window) | R3 |
| F | (e, a), 4a ∣ N + e | b ∣ (N+e)/(4a), b ≡ −a (e) [or d, cofactor] | ((E₁−E₀)L(A)/4 + A)·cop(…, E₀, b- or d-window) | R5a/R6a |
| G | (e, d), 4d ∣ N + e | a² ≡ −(N+e)/(4d) (e): ≤ 2^{ω(e)} classes; a ∣ (N+e)/(4d) | ((E₁−E₀)L(D)/4 + D)·2^{ω}·cop(…) | R10a |
| τ₃ | e ≡ −N (4) | (a, d) with ad ∣ (N+e)/4 | ((E₁−E₀)/4 + 1)·τ₃((N+E₁)/4) | R1 |
| I, J | c, then (e, a) resp. (e, d) as in F, G | loss-free | C·(pairs of F), 2C·(pairs of G) | R8a, X1 |
Here cop(n, s, window) is the least of: window/s + 1, J(w − 1) over admissible (m, k, J) of Cor 1.4, and the monotone envelope
min_η C₂(η)n^η ≥ τ(n') for every integer n' ≤ n (review repair m2: τ and τ₃ themselves are not monotone; the τ₃ row means the
envelope min_η C₃(η)((N+E₁)/4)^η, and n is always an upper bound for the integer actually factored).
Units: the classes −1 (mod 4ad), (4cd), (4ac) and −a (mod e) are units (Lemma 1.1(iv)); the cofactor class of d in
route F is (N+e)/(4a)·(−a)^{−1} mod e, a unit. *Proof:* each row's data and the displayed divisibility determine the
datum (Lemma 1.1); the pair counts are Σ_a #{e ∈ (E₀, E₁] : e ≡ −N (mod 4a)} ≤ Σ_a ((E₁ − E₀)/(4a) + 1). ∎

**Proposition 2.1 (continuum exponent; Assessment from a grid, EVIDENCE — to be replaced by the certificate of §3).**
In normalised sizes (α, γ, δ, ε) the minimum over the routes of Table 2 is ≤ 2/5 everywhere when τ₃(m) ≤ C₃(η)m^η is
used with η ≤ 0.3, and equals 2/5 at ET's point (1/5, 1/5, 1/5, 2/5). For Q-data (Type I N-points of 4/r^k, weight r^{−k})
the analogous routes give 0.65 (grid; `/tmp`-prototype, to be committed), margin ≈ 1/3, with no divisor bound at all.
*Prototype (non-rigorous floating point, `scripts/se_proto.py`):* the box sum bound for D_P(N) is 48, 7.6·10³, 3.8·10⁵,
1.2·10⁷, 2.5·10⁸ at N = 17, 17³, 17⁵, 17⁷, 17⁹ (true: 2, 32, 121, 258, 604) and 2.2·10¹⁰, 3.8·10¹² at N = 10¹⁵, 10²⁰;
bound/√N peaks ≈ 7·10² near N ≈ 10¹⁵ and then decays (local exponent 0.45 between 10¹⁵ and 10²⁰). Since each P-box of
level (K+1)/2 weighs N^{−1/2}r^{−1/2}, this predicts an explicit r₀ around 10⁸–10⁹ once certified (§3).

## 3. The certificate: an explicit r₀

**3.1 Measure criterion (PROVED from M17 and (J)26's inputs, r-free).** For an odd prime r, the boxes of the seven ET
families meeting the non-residue cells are P-boxes (level (K+1)/2, K odd) and Q-boxes (level k, k odd): √Q = ∅, Q⁻¹ = Q
as sets, U ⊂ P (M17 Lemmas 1.1, 1.3, 5.1, 5.2; their proofs use only that r is an odd prime — R187's general-r re-derivation
and brute force for r ≤ 23, DEPTH_ASPECT §3). Each P-datum (a ≤ b) gives ≤ 2 boxes, each Q-datum ≤ 2 (M17B Lemma 1.1). Hence if
  S(r) := Σ_{k odd} 2D_Q(r^k) r^{−k} + Σ_{K odd} 2D_P(r^K) r^{−(K+1)/2} < (r − 1)/(2r),                         (S)
some non-residue u is in no box, x(u) is sterile, and (M17 Cor 4.2 with 17 ↦ r) **no finite set of ET Prop 1.9 classes covers
all sufficiently large primes whose least quadratic non-residue is r**. Here D_Q(F) = #{N-points of Σ^I_F, a ≤ b, r ∤ abcde}
and D_P(N) as in §1 (in-cell data are primitive; M17 §6, Lemma 5.1).

**3.2 Explicit tables (`scripts/se_box.c`; CERTIFIED by fail-closed outward-rounded computation).** For every odd N in a
range [2^{j/q}, 2^{(j+1)/q}), se_box bounds D_P(N) (mode P) and D_Q(N) (mode Q) by a sum over boxes of ratio 2^t of the minimum
of the route bounds of Table 2 (P) resp. Table 3.2Q (below), with cop() = min(trivial, Cor 1.4 with (Cop) re-verified for the
chosen J, explicit τ(n) ≤ C₂(η)n^η), plus *row aggregation*: for a whole row of boxes with the same (a, d) (P) resp. (c, d) (Q)
the data are divisors of one integer N + 4a²d resp. F² + 4c²d, so the row is also bounded by #pairs·τ (taken when smaller).
Q-routes (Q-datum: 4abcd = F(a+b) + c, e = (a+b)/c, f = 4acd − F, ef = 4a²d + 1, 4abd = eF + 1, fb = aF + c,
f(4bcd − F) = F² + 4c²d; boxes in (c, d, f), a = (f + F)/(4cd)): (AD) ≤ 2 data per (a, d) (M17C Lemma 2.1(iv));
(fa) (a, f) then d ≡ −(4a²)^{−1} (mod f); (AC) f ∣ aF + c, f ≡ −F (4ac); (CD) f ∣ F² + 4c²d, f ≡ −F (4cd); (Ea), (Ed), (τ₃) as
F, G, τ₃ of Table 2 with N ↦ eF; and three new **f-routes**: from 4acd ≡ F and 4a²d ≡ −1 (mod f) one gets
**c ≡ −aF, d ≡ −(4a²)^{−1}, a ≡ −cF^{−1} (mod f)** (gcd(f, F) = 1 in-cell, as r ∤ c), so (fac) pairs (f, a) with 4a ∣ f + F,
then c or d in one class mod f; (fca) pairs (f, c) with 4c ∣ f + F, then a in one class mod f; (fda) pairs (f, d), 2^{ω(f)}
square-root classes for a.

**3.3 Tails (`scripts/se_tail.py`; PROVED by an exact-in-structure computation).** On boxes a ∈ [N^{x_a}, N^{x_a+1/M}) etc.
(capped by 2a²d ≤ N, acd ≤ N), every route bound is a finite sum Σ c N^e (ln N)^p valid for all N ≥ N₀ (the Coppersmith
condition is linear in L = ln N: slope ≤ 0 and value < 0 at ln N₀ are checked). P (M = 32, N₀ = 2^{600}, routes H, A, C, D,
E, F, G, τ₃ (η = 0.3), I; 2^{ω(e)} ≤ C_ω(0.1)e^{0.1}): every chosen term has e ≤ 0.4797 < 1/2 and is decreasing relative to
√N for N ≥ N₀. Q (M = 16, N₀ = 2^{100}, routes AD, AC, CD, fac, fca): every term has e ≤ 0.7500001 < 1, decreasing relative to N.

## 5. Feedback to F_q[T] (O216's open q = 27; EVIDENCE, grid steering only)

Two ℤ ingredients have F_q[T] twins that O216 did not use. (i) Coppersmith interpolation: fixing the top j coefficients of
the unknown x in E = σ₀ + xQ splits the class into q^j sub-classes, each above the O216 Lemma 1.5 threshold once
ρ + j > d(n − d)/n, so the class count is ≤ q^{(d(n−d)/n − ρ)⁺ + o(s)}. (ii) Divisibility-averaged pairs:
#{(v₁, w₁) : w₁ ∣ T^{s−2} + v₁} ≤ q^{max(deg v₁, deg w₁)} (v₁ is fixed mod w₁), not q^{deg v₁ + deg w₁} — the twin of
Σ_a (E/(4a) + 1) in route F. Adding both to O216's continuum optimiser (`scripts/se_ff_rate.py`, grid 60):
max_p min_route − 1/2 = **0.000 (q = 3), 0.000 (q = 9), −0.083 (q = 27)**, against +0.167, +0.096, 0.000 in O216 §3.
So at the exponent level the union bound now *closes q = 27* (O216's r = 3 gap), and q = 3, 9 sit exactly on the
square-root line at the thirds corner (1/3, 1/3, 1/3, 0) (deg v₁ = o(s)), where O216's cyclotomic family shows the true
count is exp(Ω(s/log s)) — so q = 3, 9 need a sub-exponential refinement there. Not certified (needs an fs_tail-type
rigorous version with the FF Lemma 1.5 split); flagged as a spark.
**3.4 Theorem (explicit r₀; PROVED, computer-assisted, relative to the same inputs as (J)26 Thm 3.1 minus Browning–Elsholtz
and minus ET's non-explicit divisor bound: M17 Lemmas 1.1, 1.3, 2.1–2.3, 5.1, 5.2, M17B Lemma 1.1, M17C Lemma 2.1(iv), M17 Cor 4.2,
all with r-free proofs (R83, R93, R187)).** **For every prime r ≥ 2³² ≈ 4.3·10⁹, (S) holds; hence the r-generic line contains
a sterile point x(u), u a quadratic non-residue mod r, and no finite set of ET Prop 1.9 classes covers all sufficiently large
primes whose least quadratic non-residue is r.** The uncovered measure in the non-residue cells is ≥ (r−1)/(2r) − 0.4851 > 0.0148
(worst at r ≈ 2³²), and → 1/2 as r → ∞.
*Proof (certificate).* `scripts/se_r0.py 32 600` (log `data/se/r0_certify.txt`): for every range r ∈ [2^b, 2^{b+1/4}),
b = 32, 32.25, …, 600, it bounds each term of (S) by the certified table values (`data/se/P_q4.txt` (N ∈ [2^{31}, 2^{200}), quarter
octaves), `P_q1.txt` + `P_q1_hi.txt` (2^{200}..2^{600}, octaves), `Q_q4.txt` (2^{31}..2^{100})) taken at the worst N-cell of the range
and the largest weight, and by the §3.3 tail term lists (top of the N-range) for N ≥ 2^{600} (P), 2^{100} (Q); K, k odd; every tail term
is increasing in N (review repair m1: seven Q terms have negative exponents; the combiner caps them at 0, c·N^e ≤ c) and, multiplied by its weight, decreasing in r (e < 1/2 resp. < 1 and p ≤ (h − e)·ln N₀), which also covers
r ≥ 2^{600}. Result: max S = 0.48501 (b = 32), no failure; with b = 31 it fails (S = 0.58 at b = 31.5), so 2³² is where *this*
certificate stops. Dominant terms at r ≈ 2³²: Q at level 1 (k = 1) 0.350, P at K = 1 0.023, P at K = 3 0.002, P tail (N ≥ 2^{600}) ≈ 0.1.
Validation of the engine (EVIDENCE): `scripts/se_box_check.py` enumerates all P- resp. Q-data exactly for N = 17³, 3¹¹, 17⁵, 10⁶ + 3,
999983, 2·10⁶ + 3 (P) and 17³, 17⁴, 17⁵, 10⁶ + 3 (Q), buckets them into se_box's boxes and rows, and finds every per-box and per-row
bound ≥ the true count (0 violations; it reproduces D_P = 32, 121 and D_Q = 73, 245 of M17 at 17³, 17⁵). ∎
*Before:* (J)26 gave "r ≥ r₀" with r₀ effectively a tower (log log r₀ ≈ 20C); R187 noted the level-1 term alone exceeds 1/2 for many
r ≈ 10⁴. *Now:* r₀ = 2³². *What limits it:* the level-1 Q term 2D_Q(r)/r — Type I solutions of 4/r counted with exponent 0.6–0.65
but with polylog many boxes; at r ≈ 10⁹ the bound is ~0.7r against a true count of a few hundred. r = 13, 17 are far out of reach:
at r = 13 *all* non-residue cells are covered at level 1 (POINTWISE_MORDELL §1), so no 13-generic point in a non-residue cell is sterile;
at r = 17 two of eight cells survive level 1, and any union bound needs a P-count with constant ≲ 2.5 at θ = 0.4 (M17D §1).
*Note (O220 "division trick", relayed by the orchestrator):* its ℤ analogue — a divisor 4a > e-window of N + e fixes e mod 4a — is
exactly the divisibility averaging Σ_a ((E₁ − E₀)/(4a) + 1) already used by routes A, F, G, I, J and Q's fac/fca/fda.
