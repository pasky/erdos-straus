# Z57_BFO — tryhard lane BFO (Opus): R_𝔊*(p) ≥ 1 for every large prime p ≡ 1 (mod 4)?

Status: z57 lane BFO (brief `z52bbriefs/z57_lanes.md` "The platform" + §BFO/BFF; rules `z52bbriefs/z55_tryhard.md`).
Internal; hostile-reviewed by a subagent (§7). **ES is OPEN. The target — R_𝔊*(p) ≥ 1 for every sufficiently large
prime p ≡ 1 (mod 4) — is NOT proved here.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment.
Scripts `scripts/z57_bfo_*`, data `data/z57/bfo/`. Definitions only from `Z56_FAMDESIGN.md` §0–§1 (𝔊*, (★), R_𝔊*,
M_𝔊*, Theorem V) and `Z55_CROSSO.md` §1 (Jacobi reformulation).

## 0. Summary

* **Verdict: target not reached.** I attacked the statement directly along every fibration of (★) and through the
  modulus-p form, and each route closed at the same point: after any choice of averaging variable, the event to be
  detected is "a single integer (p + s, or 4Cp + 1) has a divisor in a residue class tied to the fibre", and the only
  pointwise-in-p averaging mechanism I found that reaches it is quadratic reciprocity → characters mod p → Burgess, which
  sees the genus (order ≤ 2) layer only (Assessment; not a theorem about all methods). §2 records the precise PROVED
  pieces (Lemma 2.1 symmetric collapse, Lemma 2.2 genus-exact moduli = {4, 8, 12, 24}, Lemma 2.3 bounded exponent ⇒
  bounded modulus).
* **Banked (PROVED, §3). Theorem W.** For every K ≥ 1, with κ_K := Σ_{C≤K} 1/φ(4C) (≥ ¼ log K):
  #{p ≤ x prime, p ≡ 1 (4) : R_𝔊*(p) = 0} ≪_K x/(log x)^{1+κ_K}; hence ≪_A x/(log x)^A for every A. The proof uses
  only the complete levels C ≤ K of 𝔊* (prime factors ℓ ≡ −1 (mod 4C) of 4Cp + 1), Montgomery's arithmetic large sieve
  and an elementary Rankin-type lower bound for the sieve sum (proved in full). It is weaker than Vaughan-type
  exceptional-set bounds for the whole ES equation (Assessment); its point is that it holds for 𝔊*, even for its
  levels C ≤ K alone.
* **Reformulations (PROVED, §1; all numerically checked, `data/z57/bfo/lemmas_check.txt`).** R(n) = #{(s, t) ∈ ℕ² :
  4st | n + s + t}; R(n) ≥ 1 ⟺ some n + s has a divisor ≡ −1 (mod 4s); level form; levels with 64C³ ≤ p lie in 𝔊*;
  mod-p form: R(p) ≥ 1 ⟺ some (o, e, C) ∈ ℕ³ has p | 4oeC − o − e with 0 < 4oeC − o − e < 2p (k = 1 is forced).
* **Effectivity (Assessment, §4.2).** In the proof architecture of Theorem V the Burgess sums give essentially no saving
  at p ≈ 10¹⁰: even with constant 1 in Burgess (optimising r), the relative bound at length q^{1/3} is 0.995 at q = 10¹⁰,
  and it drops below ½ only near q ≈ 10^{67} (length q^{0.4}: q ≈ 10^{23.7}). So that architecture does not give
  p₀ ≤ 10¹⁰; this is a calibration of the displayed model bound, not a theorem about every Burgess-based argument.
* **CERTIFIED (§5).** Z56's exhaustive decider extended to (10¹⁰, 2·10¹⁰]; result and audit trail in §5. **EVIDENCE:** the 38 𝔊*-zeros ≤ 10¹⁰ are mild pseudo-squares (least prime non-residue
  q(p) ≥ 11 for 20/38, vs ≈ 6 % of random primes), but 8 of them have q(p) = 2, so no "pseudo-square" lemma is available.

## 1. Statement and reformulations

p ≡ 1 (mod 4) prime; (★): p = 4oeC − o − e with o odd, e even, C ≥ 1; R(p) = 2·#solutions; 𝔊* = {(o, e) : Q⁴ > P·p},
P = min(o, e), Q = max(o, e) (`Z56_FAMDESIGN` §1). **Target:** R_𝔊*(p) ≥ 1 for all p ≥ p₀.

**Lemma 1.1 (shift form; PROVED).** For odd n ≥ 3, R(n) = N(n) := #{(s, t) ∈ ℕ² : 4st | n + s + t}.
*Proof.* A solution (o, e, C) gives the ordered pairs (o, e), (e, o), both with 4st | n + s + t (quotient C). Conversely if
4st | n + s + t, C := (n + s + t)/(4st) ≥ 1 and n = 4stC − s − t; n odd forces s + t odd, so {s, t} = {o, e} with o odd,
e even. The two maps are inverse (each solution ↔ its two orderings). ∎

**Lemma 1.2 (divisor-in-class form; PROVED).** R(n) ≥ 1 ⟺ ∃ s ≥ 1 and a divisor m | n + s with m ≡ −1 (mod 4s).
*Proof.* (⇐) m = 4sC − 1 (C ≥ 1 as m > 0), t := (n + s)/m: n = t(4sC − 1) − s = 4stC − s − t. (⇒) take s = o, m = 4oC − 1:
n + o = e(4oC − 1). ∎

**Lemma 1.3 (level form; PROVED).** For each C, the solutions with this C correspond 1 : 2 to the divisors d of 4Cn + 1 with
d ≡ −1 (mod 4C) (the two divisors 4Co − 1, 4Ce − 1). *Proof.* 4C(4oeC − o − e) + 1 = (4Co − 1)(4Ce − 1); conversely if
d | 4Cn + 1, d ≡ −1 (4C), then d′ = (4Cn + 1)/d ≡ −1 (4C) (since 4Cn + 1 ≡ 1), and (d + 1)/(4C), (d′ + 1)/(4C) are the
entries; parity as in 1.1. ∎ Such d is ≢ 0 (mod p), and ≥ 4C − 1.

**Lemma 1.4 (complete levels lie in 𝔊*; PROVED, = `Z56_FAMDESIGN` §1).** If 64C³ ≤ p, every solution at level C has
(o, e) ∈ 𝔊*. *Proof (repeated for completeness).* If Q⁴ ≤ P·p ≤ Q·p then Q ≤ p^{1/3}, so PQ ≤ p^{2/3}; but
PQ = (p + P + Q)/(4C) > p/(4C) ≥ p^{2/3} when 4C ≤ p^{1/3}, i.e. 64C³ ≤ p. ∎

Lemmas 1.2–1.3 are stated for odd n ≥ 3 (as in 1.1); Lemmas 1.4–1.6 for primes p ≡ 1 (mod 4) (1.5 holds for every odd
prime; 1.6 fails for p ≡ 3 (4), e.g. p = 19, (3, 2, 1)).

**Lemma 1.5 (mod-p form; PROVED).** For an odd prime p: R(p) ≥ 1 ⟺ ∃ o, e, C ≥ 1 with p | F := 4oeC − o − e and 0 < F < 2p.
*Proof.* (⇒) F = p. (⇐) F ≡ 0 (mod p) and 0 < F < 2p force F = p; parity as in 1.1. ∎
So the unrestricted problem R(p) ≥ 1 is a *small-solution* statement for the cubic congruence F ≡ 0 (mod p) in the
hyperbolic region {4oeC < 2p + o + e} (for R_𝔊* add the condition Q⁴ > P·p; e.g. p = 37 has the small solution
(1, 2, 5) outside 𝔊*), which has ≍ p log²p lattice points: the expected number of solutions is ≍ log²p — the **critical
volume** (Assessment: pointwise small-solution results at critical volume are not known even for the modular hyperbola
xy ≡ λ (mod p) in boxes of area p^{1+ε}, where Weil's bound needs area p^{3/2+ε}).

**Lemma 1.6 (Jacobi; PROVED, `Z55_CROSSO` §1).** Every solution at a prime p has ((4Co − 1)/p) = ((4Ce − 1)/p) = −1, and
odd squares have no solutions. (Checked: 2 080 solutions at primes < 6000, 0 violations; 0 solutions at 9, 25, …, 79².)

## 2. The attack, step by step

**2.0 Plan.** R_𝔊* ≥ M_𝔊* + X_𝔊*, M_𝔊* ≥ (5/(4π²) − o(1))log²p (Theorem V). I tried to find an averaging variable, at a
fixed p, over which the order-≥3 part X_𝔊* (or the exact count directly) can be shown to be > −(1 − ε)M_𝔊*.

**2.1 The three fibrations collapse (Lemma 2.1; PROVED).** On the surface p = 4stC − s − t (s, t, C ≥ 1):
(a) fixing s, the points ↔ divisors m of p + s with m ≡ −1 (mod 4s) (m = 4sC − 1);
(b) fixing t, the same with s ↔ t;
(c) fixing C, the points ↔ divisors of 4Cp + 1 that are ≡ −1 (mod 4C);
(d) fixing a divisor-modulus m ≡ 3 (mod 4) (in any of (a)–(c)), the points with that m ↔ the divisors s of (m + 1)/4 with
  s ≡ −p (mod m); if m > (m + 1)/4 ≥ s this is the single condition s = r_m := (−p mod m) and r_m | (m + 1)/4.
*Proof.* (a)–(c) are Lemmas 1.2–1.3. (d): m = 4sC − 1 | p + s ⟺ p ≡ −s (mod m) and 4s | m + 1; s ≤ (m + 1)/4 < m so s is
the least positive residue of −p. ∎
*Consequence for the attack.* Summing (a) over s ≤ S, or (c) over C ≤ X, is a sum over shifted integers n = p + s
(resp. over the progression 4Cp + 1) of a divisor-in-class count whose modulus is 4(n − p) (resp. (n − 1)/p = 4C); interchanging
the sums (d) returns to "p mod m lies in the sparse set −Div((m + 1)/4)" for one modulus at a time, and the
condition (d) is, with j := ⌈p/m⌉, the congruence p ≡ −r − j (mod 4rj) — i.e. fibration (a) again with (s, t) = (r, j).
I tried each order of summation; the averaging variable is always a divisor of a p-shifted integer, never a free
variable on which p-dependent phases vary smoothly. (An exponential-sum treatment of Σ_C 1[(4sC − 1) | p + s] by van der
Corput in C is legitimate but bounds a single integer's divisor count, where the error term is ≥ √p, Assessment.)

**2.2 Where the class condition is genus-exact (Lemma 2.2; PROVED).** (ℤ/4m)^× has exponent ≤ 2 iff 4m | 24, i.e.
m ∈ {1, 2, 3, 6}. *Proof.* (ℤ/4m)^× surjects onto (ℤ/ℓ)^× for odd ℓ | m, cyclic of order ℓ − 1, so ℓ ∈ {3}; ℓ² ∤ m since (ℤ/9)^× is
cyclic of order 6; 2-part: (ℤ/2^a)^× has exponent ≤ 2 iff a ≤ 3. ∎ (Checked for m < 2000.)
So in fibrations (a)/(b)/(c) the class condition "≡ −1 (mod 4s)" is decided by quadratic characters only for
s, t ∈ {1, 2, 3, 6} and C ∈ {1, 2, 3, 6}: the eight integers p + 1, p + 2, p + 3, p + 6, 4p + 1, 8p + 1, 12p + 1, 24p + 1.
For these the event is "the classes mod q (q = 4s, 4t or 4C ∈ {4, 8, 12, 24}) of the prime factors of the integer that are
coprime to q generate a subgroup of (ℤ/q)^× containing −1" (exponent 2: a generated element is a product of distinct
eligible primes, so this is equivalent to the existence of the divisor), a statement about the factorisation of eight
fixed integers; Lemma 1.6 constrains only the total product of the classes (it is a reciprocity
identity), so no forcing results. Example of what *is* forced (classical): p ≡ 5 (8) ⇒ (p + 1)/2 ≡ 3 (4) has a prime factor
≡ 3 (4) ⇒ a solution with o = 1 (not necessarily in 𝔊*: if (p + 1)/2 is prime the only one is (1, 2, (p + 3)/8), in the
corner once p ≥ 16; indeed 8 of the 38 𝔊*-zeros are ≡ 5 (8)).

**2.3 Reciprocity for higher orders (Lemma 2.3; PROVED).** For k ≥ 1 the set of moduli q with λ(q) | k (λ = Carmichael's
function: all characters mod q have order dividing k) is finite: it is the set of divisors of
Λ(k) := 2^{a(k)}·∏_{odd primes ℓ with (ℓ − 1) | k} ℓ^{1 + v_ℓ(k)}, a(k) = 2 + v₂(k) for 2 | k (a(k) = 1 for k odd).
*Proof.* λ(ℓ^v) = ℓ^{v−1}(ℓ − 1) for odd ℓ, λ(2^a) = 2^{max(a−2,1)} (a ≥ 2) and λ(lcm) = lcm(λ); λ(q) | k iff each
prime-power factor satisfies these divisibilities. ∎ (Checked by brute force over q < 20000: for k = 2, 4, 6 the
largest such q is 24, 240, 504 = Λ(k); for k = 12 the range does not reach Λ(12) = 65520.)
*Consequence (the PROVED part).* Exact recovery of the class p ≡ −(o + e) (mod 4oe) from characters whose orders lie in a
fixed finite set (lcm k) is possible only for the finitely many moduli dividing Λ(k) — the Mordell-type congruence world.
*Assessment.* Reciprocity laws move bounded-order characters at p to characters modulo primes above p, where
Burgess-type bounds are pointwise; I found no way to make this reach the order-≥ 3 layer for unbounded moduli (it would
have to work with averaged rather than exact class information), so Theorem V's mechanism (order 2, all moduli, only the
*genus* of the class) is as far as I could take this route.

**2.4 Mod-p route (Assessment).** By Lemma 1.5 one may count F ≡ 0 (mod p) in boxes o ~ O, e ~ E, C ~ p/(4OE) with additive or
multiplicative characters mod p. For each fixed (o, e) the C-sum is a geometric series detecting a single residue
(o + e)·\overline{4oe} in an interval of length p/(4oe) < p, and the multiplicative-character version factors as
Σ_χ χ(4)·S_C(χ)·T(χ), T(χ) = Σ_{o,e} χ(oe)χ̄(o + e). Bounding Σ_{χ ≠ χ₀}|S_C||T| by Cauchy–Schwarz with mean values gives
≍ p^{3/2}(log p)^{O(1)} against a needed o(p); with Burgess for S_C (C-range ≥ p^{1/4+ε}) it needs OE ≥ p^{2−2δ}, impossible
since OE ≤ p. (These are the standard "square-root barrier" computations at critical volume; recorded only to say that
I tried them; the arithmetic is elementary from Parseval and the collision count oe(o′ + e′) = o′e′(o + e) for
OE(O + E) < p.)

**2.5 Assessment of the wall.** Every route above needs, at one fixed p, equidistribution of order-≥3 class data of
moduli 4oe (or 4s, 4C) over a family whose only free variable is a divisor of a p-shift. The genus layer escapes because
(p/ℓ) = (ℓ/p) moves it to a single character mod p. I found no substitute for unbounded orders. Besides the squares
test (Lemma 1.6), composite zeros constrain any substitute: at n = 810 001 = 241·3361 (non-square, R = 0) the genus mass is 24.3 (`Z56_FAMATTACK` §3.5), so a statement "X ≥ −(1 − ε)M_gen for all large
non-square n" would have to fail at infinitely many composites if the composite zeros persist (they do through 8·10⁶: 285).

## 3. Theorem W (PROVED): the exceptional set of 𝔊* is ≪ x/(log x)^A

**Theorem W.** For K ≥ 1 put κ_K := Σ_{C ≤ K} 1/φ(4C). Then for x ≥ 2
  E_K(x) := #{p ≤ x prime : p ≡ 1 (4), R_𝔊*(p) = 0} ≪_K x/(log x)^{1+κ_K}.
Since κ_K ≥ Σ_{C ≤ K} 1/(4C) ≥ ¼ log K, for every A > 0: E(x) ≪_A x/(log x)^A.
In fact the bound holds for the set of primes p with no hit at any level C ≤ K (no divisor ≡ −1 (mod 4C) of 4Cp + 1),
which contains every 𝔊*-zero p > 64K³ (not the smaller ones: p = 37 is a 𝔊*-zero with the level-5 solution (1, 2, 5)).

*Proof.* Let x be large, Q := x^{1/4}, and 𝒫 the set of primes p ∈ (max(Q, 64K³), x], p ≡ 1 (4), with R_𝔊*(p) = 0.
(Primes ≤ max(Q, 64K³) contribute ≪_K x^{1/4}.)

*Step 1 (sifting conditions).* Let p ∈ 𝒫, C ≤ K, and ℓ a prime with ℓ ≡ −1 (mod 4C). If ℓ | 4Cp + 1, then d = ℓ is a
divisor ≡ −1 (mod 4C), which gives a solution at level C (Lemma 1.3), lying in 𝔊* because 64C³ ≤ 64K³ < p (Lemma 1.4):
contradiction. Hence p ≢ −\overline{4C} (mod ℓ) for every such pair (C, ℓ) with ℓ ∤ 4C (automatic: ℓ ≡ −1 (mod 4C) is coprime
to 4C). Also p ≢ 0 (mod ℓ) for ℓ ≤ Q since p > Q.
For a prime ℓ ≤ Q put Ω(ℓ) := {0} ∪ {−\overline{4C} mod ℓ : C ≤ K, 4C | ℓ + 1} if ℓ > 4K + 1, and Ω(ℓ) := {0} otherwise;
ω(ℓ) := |Ω(ℓ)|. For ℓ > 4K + 1 the residues 4C (C ≤ K) are distinct and non-zero mod ℓ, so
ω(ℓ) = 1 + #{C ≤ K : ℓ ≡ −1 (mod 4C)} ≤ K + 1 < ℓ. Every p ∈ 𝒫 avoids Ω(ℓ) for all primes ℓ ≤ Q.

*Step 2 (large sieve).* By the arithmetic large sieve (Montgomery 1968, with the constant N − 1 + Q² of
Montgomery–Vaughan 1973; also in Iwaniec–Kowalski, *Analytic Number Theory*, Ch. 7), a set of integers in an interval of length x that avoids ω(ℓ) < ℓ classes mod
each prime ℓ ≤ Q has size ≤ (x + Q²)/J, J := Σ_{q ≤ Q} μ²(q)∏_{ℓ|q} ω(ℓ)/(ℓ − ω(ℓ)). So |𝒫| ≤ 2x/J, and
J ≥ G(Q) := Σ_{q ≤ Q} μ²(q)g(q), g multiplicative, g(ℓ) := ω(ℓ)/ℓ.

*Step 3 (prime sums).* By Dirichlet–Mertens in progressions to the fixed moduli 4C ≤ 4K
(Σ_{ℓ≤y, ℓ≡a (q)} (log ℓ)/ℓ = (log y)/φ(q) + O_q(1), gcd(a, q) = 1),
  Σ_{ℓ ≤ y} g(ℓ) log ℓ = Σ_{ℓ≤y} (log ℓ)/ℓ + Σ_{C ≤ K} Σ_{4K+1 < ℓ ≤ y, ℓ ≡ −1 (4C)} (log ℓ)/ℓ = κ log y + O_K(1),
  κ := 1 + κ_K.
By partial summation, Σ_{ℓ ≤ y} g(ℓ) = κ log log y + O_K(1) (y ≥ 3); also Σ_ℓ g(ℓ)² ≤ (K + 1)²Σ_ℓ ℓ^{−2} < ∞, and
0 ≤ g(ℓ) ≤ (K + 1)/ℓ.

*Step 4 (lower bound G(Q) ≫_K (log Q)^κ; Rankin-type, elementary).* Let s ≥ 1 (chosen below), z := Q^{1/s},
P(z) := ∏_{ℓ ≤ z}ℓ, σ := 1/log z. Then
  G(Q) ≥ Σ_{q | P(z), q ≤ Q} g(q) = Π − Σ_{q | P(z), q > Q} g(q),  Π := Σ_{q | P(z)} g(q) = ∏_{ℓ ≤ z}(1 + g(ℓ)),
and Σ_{q|P(z), q>Q} g(q) ≤ Q^{−σ}Σ_{q|P(z)} g(q)q^σ = e^{−s}∏_{ℓ≤z}(1 + g(ℓ)ℓ^σ). For ℓ ≤ z, u := σ log ℓ ∈ [0, 1] and
ℓ^σ − 1 = e^u − 1 ≤ (e − 1)u, so
  ∏_{ℓ≤z}(1 + g(ℓ)ℓ^σ)/Π ≤ ∏_{ℓ≤z}(1 + g(ℓ)(ℓ^σ − 1)) ≤ exp((e − 1)σΣ_{ℓ≤z} g(ℓ)log ℓ) = exp((e − 1)κ + O_K(σ)) ≤ B_K,
a constant. Choosing s := max(1, log(2B_K)) gives the tail ≤ Π/2, so G(Q) ≥ Π/2. Finally
log Π = Σ_{ℓ≤z} log(1 + g(ℓ)) ≥ Σ_{ℓ≤z}(g(ℓ) − g(ℓ)²/2) = κ log log z − O_K(1), so Π ≫_K (log z)^κ ≫_K (log Q)^κ
(s depends on K only).

*Step 5.* |𝒫| ≤ 2x/G(Q) ≪_K x/(log x)^κ = x/(log x)^{1+κ_K}. The bound κ_K ≥ ¼ log K follows from φ(4C) ≤ 4C. ∎

*Remarks.* (i) Only levels C ≤ K and prime divisors are used; the sifted set contains every p whose levels C ≤ K are all
empty, so W also bounds the zeros of the tiny subfamily {C ≤ K} (⊂ 𝔊* for p ≥ 64K³) (context: H3 = {64C³ ≤ p} has 873 zeros
≤ 10¹⁰, `Z56_FAMDESIGN` §4.3). (ii) Letting K grow with x inside the large sieve gives at best exp(−c√(log x)) savings
(Assessment, heuristic J ≈ exp(2√(c log Q)) from Σ_{ℓ} τ((ℓ + 1)/4)ℓ^{−1−s} ≈ c/s), still weaker than the classical
exp(−c(log x)^{2/3}) bound for the full ES equation. (iii) T1 audit: W is an upper bound for a count, and its analogue
for odd squares is trivially true (there are ≪ √x of them), so the squares test is vacuous here; primality enters only
through 0 ∈ Ω(ℓ) (one extra factor log x).
(iv) W does not touch the pointwise target: it bounds how many primes can be exceptional, not whether any is.
(v) EVIDENCE for the rate (`scripts/z57_bfo_levelK.py`, `data/z57/bfo/levelK.txt`; 3000 random primes p ≡ 1 (4) in
[10^k, 2·10^k], k = 6, 8, 10, 12): the fraction with no hit at levels C ≤ K falls from 0.231 to 0.170 (K = 1), 0.049 to
0.022 (K = 3), 0.009 to 0.0007 (K = 8); fitted exponents −d log P/d log log p = 0.45, 0.89, 1.19 for K = 1, 2, 3 against
κ_K = 0.5, 0.75, 1.0 (larger K: faster than κ_K, as composite divisors also count; few events).

## 4. Two calibrations

**4.1 Least quadratic non-residue of the 𝔊*-zeros (EVIDENCE; `data/z57/bfo/lqnr.txt`).** For the 38 𝔊*-zeros ≤ 10¹⁰,
q(p) := least prime with (q/p) = −1 is ≥ 11 for 20 of 38 and ≥ 17 for 8 (random p ≡ 1 (4) in [10⁷, 10⁸): 6.3 % and
1.9 %); but eight zeros have q(p) = 2 (p ≡ 5 (8)) and log q(p)/log p ranges over 0.05–0.32. So the zeros lean towards
pseudo-squares, as the genus mechanism predicts. A lemma "R_𝔊*(p) = 0 ⇒ (ℓ/p) = 1 for every prime ℓ ≤ f(p)" would finish
if f(p) eventually exceeded the unconditional bound q(p) ≪_ε p^{1/(4√e)+ε}; the data refute any such lemma that is
uniform down to these small zeros with f ≥ 2 there, but say nothing about an eventual version (a growing f may be small on
any finite set). 57 of the 285 non-square composite (★)-zeros ≤ 8·10⁶ are sums of two squares (26 with all prime factors ≡ 1 (4)), so composite zeros
are not explained by a 3 (mod 4)-prime obstruction either.

**4.2 Effective p₀ through Burgess (Assessment).** Theorem V's error terms come from Burgess sums of length N = q^θ to
conductors q ≈ p·P with θ > 1/4. Even granting the favourable shape |S| ≤ c·N^{1−1/r}q^{(r+1)/(4r²)}(log q)^{1/(2r)} with
c = 1 (published explicit versions have c > 1), the relative saving is f = q^{−θ/r + (r+1)/(4r²)}(log q)^{1/(2r)}.
Minimising over 2 ≤ r < 400 (`scripts/z57_bfo_burgess_calib.py`, `data/z57/bfo/burgess_calib.txt`):
* at q = 10¹⁰: min_r f = 0.995 for θ = 1/3, 0.857 for θ = 0.4, 0.469 for θ = 1/2;
* min_r f = ½ at q ≈ 10^{67.2} (θ = 1/3), 10^{23.7} (θ = 0.4), 10^{9.4} (θ = 1/2) (continuous thresholds, hostile
  review; the script reports the first integer decade).
So in Theorem V's architecture the Burgess sums of length ≈ q^{1/3}–q^{0.4} give almost no saving at 10¹⁰ and that
architecture does not give p₀ ≤ 10¹⁰. The θ ≥ 1/2 range, i.e. pairs with max(o, e) ≳ (min(o, e)·p)^{1/2}, is where
explicit tools of Pólya–Vinogradov strength (|S| ≤ (2/π²)√q log q + O(√q log log q) type) also work: in log-coordinates
the region max > (1 + min)/2, area 1/6 of the triangle (vs 5/12 for G), density main term (3/π²)·(1/6) = 1/(2π²) ≈ 0.051 per log²p — and even there the saving at p ≈ 10¹⁰ is only a
constant factor. (This calibrates the brief's "ideally p₀ ≤ 10¹⁰"; it is not a theorem about all possible proofs.)

## 5. Certification extension (CERTIFIED; `scripts/z57_bfo_certrun.sh`, `data/z57/bfo/decide_1e10_2e10_*.txt`)

`scripts/z56_famdesign_decide.c` (unchanged; validated in `Z56_FAMDESIGN` §4.1) run over all primes p ≡ 1 (4) in
(10¹⁰, 2·10¹⁰] in four chunks. Result: RESULT_PENDING.

## 6. What is proved, what is not

| item | status |
|---|---|
| R_𝔊*(p) ≥ 1 for all large p (target) | **not proved** |
| Lemmas 1.1–1.6 (reformulations, Jacobi) | PROVED + checked |
| Lemmas 2.1–2.3 (collapse, genus-exact moduli, bounded exponent) | PROVED + checked |
| Theorem W: zeros of 𝔊* ≪_A x/(log x)^A | PROVED |
| Burgess route not effective at 10¹⁰ | Assessment |
| zeros as mild pseudo-squares | EVIDENCE |
| (10¹⁰, 2·10¹⁰] has no 𝔊*-zero | CERTIFIED (see §5) |

## 7. Review log

(pending)
