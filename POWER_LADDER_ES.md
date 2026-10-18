# POWER_LADDER_ES — the k-th power relaxation ladder ES_(k) (task O276; relay of O274 SHARP 1 / spark 1)

**ES is not solved; nothing below proves ES or an infinite case of ES.** Everything below is about relaxations.

## 0. Iteration log
* v0 (brief's question): is the cube rung ES_{Q³} (4/p = 1/x + 1/y + Q³/z, Q free) provable pointwise by a cubic
  analogue of ES^□'s one-Dirichlet-prime argument (cubic residue symbol, r ≡ 1 (3))?
* v1 (making the definition exact, §1): "Q³/z with z unrestricted" is vacuous (any numerator divides a cube), so the
  third term must be in lowest terms: the denominator of z is a k-th power. This is the parity normalisation of
  UNIT_ORBIT_ES §1 with 2 replaced by k.
* v2 (construction-first, §2): no cubic reciprocity is needed — the rung collapses. For odd k, ES_(k) is a FINITE
  CONGRUENCE COVERING (mod 4): 4/n = 1/(2x) + 1/(2x) + Q^k/(nx), 4x = n + Q^k, Q ≡ −n (mod 4). T1 dies (odd squares
  and cubes are solved with Type I shape). For even k the rung is ES^□ again (one Dirichlet prime, T1 intact).
* v3: the O274 §3.2 index calibration ("only k = 2 is provable; k ≥ 3 needs equidistribution") is therefore wrong in
  its conclusion; the correct calibration is the index of k-th powers in (ℤ/4)^× (and (ℤ/3)^×), §3.

## 1. Definitions (exact)

**Definition 1.1.** For k ≥ 1 and n ≥ 2 let
`ES_(k)(n):  4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℚ_{>0},  den(z) = Q^k with Q odd, gcd(Q, n) = 1.`
Equivalently 4/n = 1/x + 1/y + Q^k/Z with x, y, Z ∈ ℤ_{>0}, **gcd(Q, Z) = 1**, Q odd, gcd(Q, n) = 1; equivalently
v_q(z) ∈ kℤ for every prime q with v_q(z) < 0, and such q are odd and prime to n.
* ES_(1) = "third denominator any odd integer prime to n"; ES_(2) = ES^□ of (J)28 (SYNTHESIS_SPARKS2 §2);
  ES = the per-solution intersection (Q = 1).
* Monotonicity: ES ⊂ ES_(k) ⊂ ES_(j) whenever j | k. The ladder is the divisibility lattice, not a chain:
  ES_(2) and ES_(3) are incomparable, both contain ES_(6).

**Remark 1.2 (why "lowest terms" is forced).** Without gcd(Q, Z) = 1 the rung is independent of k: a positive
rational A/B (lowest terms) equals Q^k/Z for some Z ∈ ℤ iff A | Q^k, and A | rad(A)^k. So "4/n − 1/x − 1/y has
numerator dividing a k-th power" = "numerator odd and prime to n", the same for all k.

**Remark 1.3 (target-coset reading).** In the fixed-modulus-4 shot family (UNIT_ORBIT_ES Prop 2.1 with Q² → Q^k,
§2.2 below) the event is "n + 4Q^k has a divisor g ≡ 3 (mod 4)" with Q free; mod a prime g this asks
−n/4 ∈ (F_g^×)^k, a coset of the k-th powers of index gcd(k, g − 1). That index — not [ (ℤ/4U)^× : k-th powers ]
for a large pooled U — is what decides the rung (§3).

## 2. The ladder collapses to the parity of k

### 2.1 Odd k: a finite congruence covering mod 4

**Theorem 2.1 (PROVED, elementary).** Let k ≥ 1 be odd. Then ES_(k)(n) holds for every n ≥ 2. Explicitly, for odd n
let Q be the least positive integer with Q ≡ −n (mod 4) and gcd(Q, n) = 1 (so Q = 1 if n ≡ 3 (4); Q = 3 if
n ≡ 1 (4) and 3 ∤ n), and x = (n + Q^k)/4. Then
`4/n = 1/(2x) + 1/(2x) + Q^k/(nx)    (distinct-denominator variant: 1/x = 1/(x+1) + 1/(x(x+1)))`
with gcd(Q^k, nx) = 1, and the solution has Type I shape at every prime ℓ | n (ℓ ∤ 2x, v_ℓ(nx) = v_ℓ(n)).
In particular ES_(k)(p) holds at every prime p with Q ∈ {1, 3}; e.g. k = 3: 4/p = 2/(2x) + 27/(px), x = (p + 27)/4
for p ≡ 1 (4), p ≠ 3.
*Proof.* Q is odd, so Q^k ≡ Q ≡ −n (mod 4) (Q² ≡ 1 (8), k odd): x ∈ ℤ_{>0}. Then 1/x + Q^k/(nx) = (n + Q^k)/(nx) =
4/n. If a prime q divides Q and x then q | 4x − Q^k = n, contradicting gcd(Q, n) = 1; so the third term is in lowest
terms, den(z) = Q^k with Q odd and prime to n. Shape: ℓ | n, ℓ | x ⇒ ℓ | Q^k, impossible; ℓ odd. Even n = 2^a m:
for m > 1 odd scale a solution for m by 2^a (Q odd keeps lowest terms); for m = 1, ES holds at 2^a
(4/2 = 1/1 + 1/2 + 1/2; 4/2^a = 1/2^{a−1} + 1/2^a + 1/2^a for a ≥ 2). ∎

**Corollary 2.2 (T1 dies at odd k; PROVED).** For odd k every odd square m² (and every odd cube m³) has an ES_(k)
solution of Type I shape at every prime of m. The obstruction B5/T1 is absent, and — as B5 predicts for T1-free
variants — the rung is a finite covering: the two classes n ≡ 1, 3 (mod 4) with the identity of Thm 2.1 (the
coprimality side-condition gcd(Q, n) = 1 is the only further n-dependence: Q = 3 serves every n ≡ 1 (4) with 3 ∤ n,
Q = 7 every n ≡ 1 (4) with 3 | n, 7 ∤ n, …; for primes Q ∈ {1, 3} always).
*Mechanism (UNIT_ORBIT_ES Lemma 1.1(i) with w = k odd):* inv_q of the BL/Hilbert class at a prime q | Q equals the
Legendre sign ((−y/x)/q), unconstrained, so a muted place with ODD exponent can absorb the anchor's ½.

### 2.2 Even k: the rung is ES^□ again

**Theorem 2.3 (PROVED, relative to Dirichlet's theorem only).** Let k = 2^a k′ with a ≥ 1, k′ odd. Then ES_(k)(n)
holds for every odd non-square n, by ONE prime r: r ≡ 3 (mod 4), (n/r) = −1, and r ≢ 1 (mod ℓ) for every prime ℓ | k′.
The solution has Type II shape at every prime of n.
*Proof.* n ≡ 3 (4): ES (Q = 1, 4/n = 1/((n+1)/4) + 1/(n(n+1)/4) split). n ≡ 1 (4): n = n₀m², n₀ > 1 squarefree,
n₀ ≡ 1 (4), so n₀ has a prime factor ≥ 5. Choose a class a mod 4n₀L (L = product of the odd primes of k′ not dividing
n₀) with a ≡ 3 (4); a ≡ 2 (mod ℓ) for ℓ | L; for ℓ | n₀: a ≢ 0, 1 (mod ℓ) when ℓ | k′, with Legendre signs (a/ℓ)
chosen so that (a/n₀) = −1 (possible: at ℓ = 3 the only admissible class 2 has sign −1, at ℓ ≥ 5 both signs occur
among classes ≠ 0, 1 (4 is a residue ≢ 1), and n₀ has a prime ≥ 5 to fix the total sign). Dirichlet gives a prime
r ≡ a, r ∤ m. Then (n/r) = (n₀/r) = (r/n₀) = −1, so −n/4 is a non-zero square mod r ((−1/r) = −1). As (r−1)/2 is odd
and prime to k′, gcd(k, r−1) = 2 and (F_r^×)^k = (F_r^×)²: there is Q₀ with 4Q₀^k ≡ −n (mod r). Lift to Q ≡ Q₀ (mod r)
with Q odd and gcd(Q, n(r+1)) = 1 (CRT; r ∤ 2n(r+1)). Put e = (n + 4Q^k)/r, x = (n + e)/4, y = n(r+1)/4,
z = nx(r+1)/(4Q^k) (UNIT_ORBIT_ES Prop 2.1 with Q² → Q^k; its identity 4rx = n(r+1) + 4Q^k and the equation check
do not use the exponent). A prime q | Q dividing x(r+1) would divide n(r+1) — excluded — so den(z) = Q^k. Shape as
in Prop 2.1. ∎

**Lemma 2.4 (T1 persists at even k; PROVED).** For even k every ES_(k) solution is an ES^□ solution (den(z) = (Q^{k/2})²),
so SPARKS2 Lemma 2.1 applies: Σ_{ℓ|n} inv_ℓ = ½, and at n = m² (m odd) no ES_(k) solution has Type I/II shape at
every prime of m. In the fixed-modulus-4 family, m² + 4Q^k = m² + (2Q^{k/2})² (coprime) has no prime factor ≡ 3 (4),
so no finite covering by such shots exists (every class mod L containing an odd square is uncovered at that square).

**Corollary 2.5 (every rung holds everywhere; PROVED).** For every k ≥ 1, ES_(k)(n) holds for every n ≥ 2.
*Proof.* Odd k: Thm 2.1. Even k: write odd n > 1 as s^{2^j} with j maximal, so s > 1 is a non-square; Thm 2.3 gives
ES_(k)(s); multiplying all denominators by n/s (prime to Q) gives ES_(k)(n). Even n: scale from the odd part / ES at 2^a. ∎
(The same scaling shows ES^□ holds at every odd n > 1, not only at non-squares — the ledger's "non-square" is the
scope of the Type II-shaped construction, which T1 genuinely forbids at squares.)

**Reading (Assessment).** The k-th power ladder carries exactly one bit: k mod 2. Odd rungs are B1-trivial
(congruence covering, no T1); even rungs are ES^□ (one Dirichlet prime, T1 intact). No rung is "strictly between ES^□
and ES" in difficulty: ES_(6) ⊂ ES_(2) ∩ ES_(3) is ES^□-like, ES_(2^a) is ES^□-like for all a. The headline candidate
"pointwise ES_{Q³}" is TRUE but for a trivial reason, and does not interpolate towards ES. The difficulty of ES is not
in the exponent of the allowed denominator but in its SIZE (Q = 1), as (J)28's recalibration already said.

### 2.3 Numerics (EVIDENCE; `scripts/z44_ladder.py 1000000`, 8 s, log `logs/z44_ladder_1e6.txt`)
Every solution checked exactly (Fraction equality, gcd(Q, Z) = 1, Q odd and prime to n, Type I/II shape by valuations).
* k = 3, 5: all 78 496 primes 5 ≤ p ≤ 10⁶ solved by Thm 2.1, max Q = 3; all 499 odd squares and 49 odd cubes ≤ 10⁶
  solved with Type I shape at every prime (T1 control: T1 is DEAD at odd k, as Cor 2.2 says).
* k = 2, 4, 6: all primes p ≡ 1 (4) ≤ 10⁶ solved by Thm 2.3 (p ≡ 3 (4) by ES), Type II shape. The prime r(p): for
  k = 2, 4 identical (max r = 131, r = 3, 7, 11, 19, … for 19 611, 9 825, 4 948, 2 444, … primes — R193's numbers);
  for k = 6 the extra condition r ≢ 1 (3) gives r ∈ {3, 11, 23, 47, 59, 71, …}, max r = 251.
  T1 control: 0 modulus-4 shots m² + 4Q^k with a prime factor ≡ 3 (4) for all odd m² ≤ 10⁶, odd Q ≤ 99 prime to m
  (forced: sum of two coprime squares; the trial division is only a sanity check).
* For comparison, the ES shot Q = 1 (p + 4 has a prime factor ≡ 3 (4)) fails at 9 841 primes p ≡ 1 (4) ≤ 10⁶.
* Numerator 8 at p = 131, 241 (ladder hard cases): odd k by the mod-8 version of Thm 2.1 (8x = p + Q^k, Q ≡ −p (8);
  odd k-th powers are bijective on (ℤ/8)^×): 8/131 = 1/64 + 1/64 + 5³/4192, 8/241 = 1/146 + 1/146 + 7³/17593.
  Even k by Thm 2.3 with r ≡ 7 (8), (p/r) = −1: 8/131 = 1/20 + 1/131 + 3²/2620, 8/131 = 1/956 + 1/131 + 9⁴/125236,
  8/241 = 1/46 + 1/241 + 3⁴/11086. (Numerator m in general: odd k is a covering whenever odd k-th powers are
  bijective on (ℤ/m)^×-classes reachable, e.g. m = 2^j; even k needs a prime r ≡ −1 (m) with (−n/m·r⁻¹…) a square — a
  Dirichlet prime again.)
