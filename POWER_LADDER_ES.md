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
rational A/B (lowest terms) equals Q^k/Z for some Z ∈ ℤ iff A | Q^k, and A | A^k (take Q = A). (R-self repair: "A | rad(A)^k" was false, e.g. A = 9, k = 1.) So "4/n − 1/x − 1/y has
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
holds for every odd non-square n: for n ≡ 3 (4) by ES itself, for n ≡ 1 (4) by ONE prime r: r ≡ 3 (mod 4), (n/r) = −1,
and r ≢ 1 (mod ℓ) for every prime ℓ | k′ (Type II shape at every prime of n). (Self-review repair: for n ≡ 3 (4) such
an r need not exist, e.g. n = 3, k = 6 forces r ≡ 11 (12), (3/r) = +1; the proof never uses r there.)
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
  8/241 = 1/46 + 1/241 + 3⁴/11086. (Numerator m, odd k: mx = n + Q^k needs Q^k ≡ −n (mod m), solvable at every n prime to m iff
  gcd(k, λ(m)) = 1 (Carmichael λ), e.g. every odd k for m = 2^j; even k: a prime r ≡ −1 (mod m), r ≡ 3 (4), with
  −n/m a non-zero square mod r — a Dirichlet prime again.)

## 3. The correct index calibration (repairs LOWER_TAIL_FABLE §3.2's conclusion)

**Proposition 3.1 (PROVED, elementary group theory).** (a) For U odd squarefree and G = (ℤ/4U)^×,
[G : G^k] = gcd(k, 2)·∏_{ℓ | U} gcd(k, ℓ − 1); for k = 3 this is 3^{#{ℓ | U : ℓ ≡ 1 (3)}} ≤ τ₃(U) = 3^{ω(U)}, with
equality iff every prime of U is ≡ 1 (3). (b) For a single shot prime g, the fixed-modulus-4 shot event
"g | n + 4Q^k for some Q" is −n/4 ∈ (F_g^×)^k, of index i_k(g) = gcd(k, g − 1); with g ≡ 3 (4) forced by the shot,
i_k(g) = gcd(k, 2)·gcd(k, (g − 1)/2).
(c) Hence: i_k(g) = 1 is attainable (g = 3, or any g ≡ 3 (4) with (g−1)/2 prime to k) iff k is odd ⟹ ONE fixed shot
prime covers all n prime to g (the g = 3 shot is 4/n = 1/n + 1/x + Q^k/(nx), 3x = n + Q^k; Thm 2.1 uses the even
simpler two-term identity 4x = n + Q^k, i.e. index 1 of odd k-th powers in (ℤ/4)^×); for k even the minimum is i_k(g) = 2, attained
on a positive-density set of g, and the square class is decided by (n/g) — one Dirichlet prime (Thm 2.3). An index
≥ 3 at EVERY admissible g never occurs over ℤ for the k-ladder.

*Why §3.2's reading failed (Assessment).* It priced the k-th-power target in a large pooled group (ℤ/4U)^× with U
built from many primes, where [G : G^k] grows like k^{π(y)/φ(k)}. But the relaxation lets the solver CHOOSE the
modulus: the cheapest modulus has index 1 (odd k) or 2 (even k). Index calibration must be done at the
best single modulus, not at a pooled one. For ES itself the "coset" is {−1} (Q = 1), which no choice of modulus
enlarges — this is B2's "the modulus is part of the solution", and the k-ladder never touches it.

**Remark 3.2 (where a genuinely cubic rung lives; Assessment).** In ES-type shot families the shot prime satisfies
g ≡ −1 (mod 4M) for the shot's modulus 4M; if 3 | M then g ≡ 2 (3) and cubing is bijective on F_g^× — cubic residue
symbols are invisible. A rung where the cubic symbol decides needs shots forced into g ≡ 1 (3) with no index-1
alternative; over ℤ the k-ladder has none. The genuinely cubic analogue is the order-3 variant TES over ℤ[ω]
(SYNTHESIS_SPARKS2 §3: T1₃ at cubes, TES^{□₃} via one Chebotarev prime), where the Brauer/T1 class itself has order 3.
This matches TWO_POWER_LADDER (z41_stickelberger_dictionary): "BM layer and T1 are the m = 2 coincidence".

## 4. Relation to the cap relaxation and the known pointwise results

* ES^{(y,e)} ((J)34/(J)64, CAP_POINTWISE normalisation): den z = r², rad r | y, v_ℓ(r) ≤ e. So ES^{(y,e)} ⊂ ES_(2) = ES^□
  for every e, and ES^{(y,e)} ∩ ES_(4) = solutions with den z = s⁴, rad s | y, v_ℓ(s) ≤ e/2. **ES_(k) is NOT a special
  case of a bounded cap**: Thm 2.1's solutions have Q ∤ y = 2x, and Thm 2.3's have gcd(Q, (r+1)) = 1 by construction,
  hence rad Q ∤ y = n(r+1)/4 — the cap's "rad r | y" (the condition that ties the mute primes to the solution, B2) is
  exactly what the k-ladder drops. (PROVED, by inspection of the constructions.)
* The gradients that DO interpolate between ES^□ and ES are those that shrink or tie Q: the box Q ≤ B, the fixed mute
  set S ((J)23: sieve, ineffective), the cap e with rad Q | y ((J)64/(J)66: cap ≪ n^{1/4+ε} via windows), and the
  phase-diagram band ((J)43). Thm 2.1 drops ALL of these constraints at once; it does
  NOT follow that odd exponents trivialise the constrained rungs (self-review repair; the earlier blanket claim is
  withdrawn). Counter-indications: (i) the box Q ≤ 1 is ES for every k; (ii) with the cap tie rad Q | y, UNIT_ORBIT_ES
  Lemma 1.1(iii) forces q | x at every denominator prime q, so case (ii) of that lemma applies and inv_q = 0 WHATEVER
  the parity of v_q(z) — T1 survives odd exponents under the cap tie. Only the free-Q, untied rungs collapse; the
  one-mute-prime case is treated separately in §5.

## 5. Deep push 1: one mute prime — the parity bit is the whole gap between a covering and an Artin problem

Construction-first iteration: the k-ladder dropped B2's tie (rad Q | y) AND enlarged Q to all odd integers. Which of
the two made odd k trivial? Shrink Q to the powers of ONE prime q and keep the exponent free.

**Definition 5.0.** For an odd prime q ∤ n, ES^{⟨q⟩,*}(n): 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, den z a power of q
(any exponent). With parity (den z an even power of q) it is ES^{({q})} of UNIT_ORBIT_ES §1.

**Theorem 5.1 (PROVED, elementary; per q).** Suppose q ≡ 3 (4), or q ≡ 2 (3), or some prime g ≡ 3 (mod 4) has q as a
primitive root. Then ES^{⟨q⟩,*}(n) holds for every n ≥ 2 prime to q, by a finite covering plus scaling.
*Proof.* q ≡ 3 (4): n ≡ 3 (4) is ES; n ≡ 1 (4): 4x = n + q, 4/n = 1/(2x) + 1/(2x) + q/(nx), and q ∤ x (else q | n),
so den z = q. q ≡ 2 (3): n ≡ 2 (3) is ES (3x = n + 1, 4/n = 1/n + 1/x + 1/(nx)); n ≡ 1 (3): 3x = n + q,
4/n = 1/n + 1/x + q/(nx). Witness g: for g ∤ n pick c ∈ [0, g−2] with 4q^c ≡ −n (mod g) (q generates F_g^×) and apply
UNIT_ORBIT_ES Prop 2.1's formulas with Q² → q^c (r = g ≡ 3 (4); its identity does not use the exponent): den z | q^c.
Remaining n (divisible by 3, resp. g, or even): n = t^a·m with t ∈ {2, 3, g}; scale a solution for m > 1 by t^a
(denominators stay q-powers), or use ES at t^a (t ≡ 3 (4) or t ∈ {2, 3}). ∎
**CERTIFIED (`scripts/z44_one_mute.py 1000000 1000000`, log `logs/z44_one_mute.txt`).** Every prime q ≤ 10⁶ satisfies a
hypothesis of Thm 5.1: the 19 564 primes q ≡ 1 (12) all have a witness g ≡ 3 (4) with q a primitive root, least g ≤ 179
(q = 432 793). Exact check for q = 13, g = 11 (13 ≡ 2 is a primitive root mod 11): all 78 494 primes p ≤ 10⁶ (p ≠ 11, 13)
and all odd squares ≤ 10⁶ prime to 143 solved, exponent c ≤ 9.
*For all q:* Thm 5.1's last hypothesis is an Artin-in-progression statement; it holds for every non-square q under GRH
(Lenstra, Invent. Math. 42 (1977), primitive roots in Chebotarev sets; the condition g ≡ 3 (4) is compatible since q
must then be a non-residue mod g, (q/g) = (g/q) for q ≡ 1 (4)) — CONDITIONAL, citation-level; but it is never needed
in practice, since a single witness per q proves the theorem for that q.

**Proposition 5.2 (with parity the g-shot condition; PROVED; the Artin reading is a sufficient route only).** With parity
(exponent 2c), the g-shot fires iff −n/4 ∈ ⟨q²⟩_g ⊆ (F_g^×)² — exact condition; q need not be a primitive root (e.g.
q = 13, g = 3: 4/5 = 1/58 + 1/5 + 13²/290, 13 ≡ 1 (3)). It suffices that ⟨q²⟩_g = (F_g^×)² (ord_g(q²) = (g−1)/2) and
(n/g) = −1. Hence a sufficient route to ES^{({q})}(n) via g-shots is a prime g ≡ 3 (4) with ord_g(q²) = (g−1)/2 AND
(n/g) = −1 (n-dependent): an Artin-type problem with an n-dependent Chebotarev condition. (Self-review repair: this
is NOT a proved reduction showing the relaxation REQUIRES Artin; other g with smaller ⟨q²⟩ can fire at a given n.) (open unconditionally for a fixed q; FF_MUTE's function-field theorem
is the case where Artin is Bilharz's theorem). T1 at squares: −m²/4 is a non-square mod every g ≡ 3 (4), so no
square is ever reached by any g-shot (this part is exact).
**Reading (Assessment).** For ONE mute place, the parity normalisation is the entire difference between a finite
covering (odd exponents allowed: index of ⟨q⟩ in F_g^× is 1 at one witness g) and (via the natural route) an Artin-type problem
(even exponents: index ≥ 2 at every g, and the residual quadratic condition depends on n). This is (J)28's "orbit size" recalibration
refined: orbit size matters only on the parity-constrained side; on the odd side one witness suffices for all n.

## 6. Deep push 2: the order-3 variant separates the two bits (T1 order vs shot index)

Over ℤ two different "bits" coincide: the Brauer/T1 class has order 2, and the 2-part of every shot index
gcd(k, g − 1) is 2 (g ≡ 3 (4)). The order-3 variant TES over O = ℤ[ω] (SYNTHESIS_SPARKS2 §3, Prop 3.1 shots
g | n + 18D, g ≡ 10 + ω (18)) separates them. Define TES_(k) as TES with D = Q^k (Q odd, prime to 6n, Q^k/Z in lowest
terms, no further normalisation).
* **T1₃ bit (PROVED from SPARKS2 Lemma 3.2's computation):** the tame symbol at a mute q with v_q(z) = −w, q ∤ x is
  (ωx/y)^w up to cubes — trivial for 3 | w, unconstrained otherwise. So 3 | k ⟹ T1₃ (Thm 3.3 applies verbatim:
  no Type I/II-shaped solution at cubes); 3 ∤ k ⟹ no T1₃ constraint from the mute places.
* **Index bit (PROVED, elementary):** for a fixed shot prime g of norm ℓ (≡ 1 (3), odd), the shot fires at n iff
  −n/18 ∈ (O/g)^{×k}, index gcd(k, ℓ − 1), always even for even k. So k prime to 6: ONE fixed g covers every n prime
  to 6g (a covering, like odd k over ℤ; g = −8 + ω of norm 73 serves every k prime to 6, as 72 = 2³·3²). k = 3: T1₃ +
  a cubic Chebotarev condition (SPARKS2 Thm 3.5). k = 2: NO T1₃, and at g of norm 73 the shot fires exactly on the
  quadratic-residue half; for other even k at most half (index gcd(k, ℓ−1) ≥ 2, e.g. 4 for k = 4, 8 for k = 8 at
  ℓ = 73). Every admissible g has ℓ ≡ 1 (18) (N(10 + ω) = 91), so 9 | index for 9 | k at every shot prime.
  (Self-review repair: only the T1₃-divisibility bit and the index-parity bit are claimed; no complete classification of
  TES_(k) for k ∉ {1, 2, 3} or k prime to 6 is claimed — SPARKS2 Thm 3.5's cubic argument does not cover higher powers.)
* **EVIDENCE (`scripts/z44_tes_ladder.py 3000`, log `logs/z44_tes_ladder.txt`; exact verification in O).** Fixed
  g = −8 + ω (N = 73). Over the 412 2-primary split primes π with N(π) ≤ 3000 and their cubes π³: k = 1 fires for
  412/412 primes AND 412/412 cubes (all Type II-shaped at π: T1₃ dead); k = 2 fires for 209/412 primes and 209/412
  cubes (≈ ½, cubes not obstructed); k = 3 fires for 134/412 primes (≈ ⅓) and 0/412 cubes (T1₃).
* **Reading (Assessment).** TES_(2) is a T1-free rung (no mute-place T1₃) that a single fixed shot does not cover; finitely many fixed
  shots g₁, …, g_s never cover either (CRT: choose −n/18 a non-square mod every g_i). So "no T1 ⟹ finite covering"
  is FALSE within fixed-modulus shot families as soon as T1's order and the shot index's prime differ. Whether
  another identity family covers TES_(2) is OPEN (spark). Over ℤ the k-ladder is "flat" precisely because
  ord(T1) = 2 = the unavoidable 2-part of the shot index — a coincidence of the prime 2 (cf. z41_stickelberger:
  "BM layer and T1 are the m = 2 coincidence").

## 7. The direct test (parent note after R286 D7/D8): does ES^□'s own mechanism lift to Q³?

R286 D7: ES^□'s proof is the fixed-modulus-4 shot family g | n + 4Q² with Q free and ONE Dirichlet prime r ≡ 3 (4),
(n/r) = −1, solving 4Q² ≡ −n (mod r); the index calibration is only a heuristic. The test: replace Q² by Q³.
**Answer (PROVED; this is Prop 2.1 of UNIT_ORBIT_ES with Q² → Q^k, exactly as used in Thm 2.3):** yes, and the
reciprocity step disappears. The shot prime must be r ≡ 3 (4); choose it ALSO with r ≢ 1 (3) (e.g. r = 3, 11, 23, …).
Then cubing is a bijection of F_r^×, so 4Q³ ≡ −n (mod r) is solvable for EVERY n prime to r — no condition on n, no
dependence of r on n. Valuation side condition: v_q(z) = 2v_q(r+1) − 3v_q(Q) must be ≡ 0 (3) or ≥ 0; take
gcd(Q, r+1) = 1 (CRT). So ONE FIXED prime (r = 3: 4/n = 1/x + 1/n + Q³/(nx), 3x = n + Q³, Q ≡ −n (3)) solves
ES_(3)(n) for every n prime to 3, and r = 11 for 3 | n. The cubic-non-residue variant suggested in the brief
(r ≡ 1 (3), p a cubic non-residue) is the WRONG direction: it raises the shot index from 1 to 3 (then one needs
(−n/4 | r)₃ = 1 — a Chebotarev condition that also works, but is unnecessary).
**EVIDENCE (`scripts/z44_ladder.py 1000000`, appended section, log `logs/z44_ladder_1e6.txt`).** Fixed shots
(k, r) = (3, 3), (3, 11), (5, 3), (5, 23): all primes 13 ≤ p ≤ 10⁶ with r ∤ p, all 302 odd squares and 29 odd cubes
≤ 10⁶ prime to 33 solved with Type II shape at every prime, exact check; max Q = 11, 109, 11, 217.
**On D8's arithmetic.** R286's formula [G : G^k] = ∏ gcd(k, |C_i|) agrees with Prop 3.1(a), and its primorial ratios
(0.50, 0.94, 1.13, 1.10 for k = 3, 4, 6, 8) are correct (e.g. k = 4: ½(log₃2 + log₃4) = 0.946). But for the actual
mechanism the pooled index is irrelevant: the shot index at one prime is gcd(k, r − 1) = gcd(k, 2)·gcd(k, (r−1)/2),
minimised to 1 (odd k) or 2 (every even k, including the "borderline" k = 4 and the "above the line" k = 6, 8) by
choosing r. So k = 4, 6, 8 are all ES^□-easy (Thm 2.3; k = 4, 6 verified in §2.3), and the pooled-count borderline does
not correspond to any change in provability.
