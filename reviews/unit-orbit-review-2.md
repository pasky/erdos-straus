# Hostile review 2 (R190) of O186 UNIT_ORBIT_ES.md — focus Thm 2.4 and Thm 5.1

Reviewer 2 of 2, independent (did not read reviews/unit-orbit-review.md). Document reviewed: UNIT_ORBIT_ES.md as merged
from side-agent/unit-orbit-es. From-scratch scripts: `scripts/review_uo2_*.py` (none of the author's `uo_*` code reused).

## Summary verdicts

(filled in progressively below)

| Claim | Verdict |
|---|---|
| Prop 2.1 (orbit-shot ⇒ ES^{(S)} solution, Type II shape, parity) | SOUND |
| Lemma 2.2 (linear sieve on (r−1)/2 in a progression) | SOUND (standard) |
| Lemma 2.3 (few r with small ⟨S⟩ mod r) | SOUND (= Gupta–Murty Lemma 2, k generators) |
| **Thm 2.4(a)** (|S| ≥ 4: every non-square n coprime to 2S solvable) | **SOUND** (minor wording/effectivity repairs m1–m3) |
| Lemma 1.1 / Cor 1.2 / **Thm 2.4(b)** (T1 of ES^{(S)}) | SOUND-AFTER-REPAIRS (m4: quantifier in (b)) |
| **Thm 5.1** (V_φ: ≪ X^{3/4} log²X exceptions) | see §3 |

## 1. Thm 2.4(a): what is sifted, and does it close?

**Reading of the sieve (brief item (c)).** The sifted variable is the PRIME r, not the S-units. The proof is exactly
Gupta–Murty with an extra fixed congruence: Lemma 2.2 sifts the shifted primes (r−1)/2, r ≤ x, r ≡ a (mod M),
M = 4·rad(n), by the primes ℓ ∤ M below x^{1/4−ε}. The polylog-many S-units Q ≤ x are never counted; Q is produced
*after* the fact as a discrete logarithm: once Γ_r := ⟨S⟩ mod r has index ≤ 2 in F_r^*, the element −n/4 (a square
mod r) is Q² for some Q ∈ ⟨S⟩ (exponents ≥ 0 since Γ_r is finite). So the "polylog many shots" objection does not
apply; the infinitely many shots are indexed by r, and Q may be astronomically large in terms of r.

**The Chebotarev condition (n/r) = −1 inside the sieve.** It is not a genuine Chebotarev condition: for n ≡ 1 (mod 4),
(n/r) = (r/n) (Jacobi), which depends only on r mod rad(n); the proof bakes it into the class a mod M together with
r ≡ 3 (mod 4) and a ≢ 0, 1 (mod ℓ) for ℓ | n. Then −n/4 is a square mod r because (−1/r) = (n/r) = −1. Lemma 2.2's
hypothesis "a ≢ 1 mod every odd ℓ | M" is what keeps primes ℓ | M from dividing (r−1)/2; it is compatible with the
Jacobi condition because some ℓ₀ ≥ 5 has odd v_{ℓ₀}(n) (re-derived: if only 3 had odd valuation, n = 3^{odd}m² ≡ 3
mod 4) and F_{ℓ₀} ∖ {0,1} contains both a residue and a non-residue for ℓ₀ ≥ 5 (ℓ₀ = 3 has only the non-residue 2,
which is why ℓ₀ ≠ 3 is needed). Re-derived; correct. The n ≡ 3 (mod 4) branch (Q = 1) is correct.

**Arithmetic closing condition (re-derived).** r ≡ 3 (mod 4) ⇒ (r−1)/2 odd, so [F_r^*:Γ_r] ∈ {1,2} or it has an odd
prime factor, which divides (r−1)/2 and hence is ≥ x^{1/4−ε}; then |Γ_r| ≤ x^{3/4+ε}. Lemma 2.3 (re-derived: (B+1)^k
exponent vectors in [0,B]^k collide; r | N_c for one of (2B+1)^k vectors c ≠ 0, ω(N_c) ≪_S B) bounds such r by
≪ x^{(3/4+ε)(1+1/k)}; for k = 4, ε < 1/20 the exponent is < (4/5)(5/4) = 1, so o(x/log²x). Lemma 2.2: linear sieve
(κ = 1, g(ℓ) = 1/(ℓ−1)), level D = x^{1/2}/log^B x by Bombieri–Vinogradov over moduli Md (one class mod Md by CRT
since gcd(d, M) = 1), s = log D/log z → 2/(1−4ε) > 2, f(s) > 0: ≫_{n,ε} x/log²x primes. Index ≤ 2 ⇒ Γ_r ⊇ (F_r^*)² (the
index-2 subgroup is unique), and (Γ_r)² = (F_r^*)² because squaring is a bijection on the odd-order group (F_r^*)².
Everything checks. k = 3 fails here exactly ((3/4)(4/3) = 1), consistent with the |S| ≥ 4 hypothesis.

**n-uniformity.** None is needed: n is fixed, x → ∞, and all constants may depend on n (through M) — the theorem is
"for each n", proved n by n. Correct as stated.

**From-scratch checks.**
* `scripts/review_uo2_brute.py 100000 10000` (S = {3,5,7,11}): all **20 713** non-squares 3 ≤ n < 10⁵ coprime to 2S are
  solved by Prop 2.1 with a prime r ≡ 3 (mod 4), r | n + 4Q²; each solution verified exactly (equation, x, y ∈ ℤ_{>0},
  z > 0, z ∈ ℤ[1/S] with even negative q-valuations, Type II shape at every prime of n); max Q = 81. All 65 squares
  have no hit for Q ≤ 10⁴. With N = 3·10⁵: 62 224 non-squares, max Q = 99, 0 failures, 112 squares no hit — the
  author's EVIDENCE numbers are reproduced exactly.
* `scripts/review_uo2_index.py 10⁶` (the proof's own route, not a search over Q): for n ∈ {13, 17, 29, 37, 41, 53, 221,
  13³, 17·19², 13²·17·29} the class a mod M is built exactly as in the proof; every prime r < 10⁶ of that class with all
  prime factors of (r−1)/2 ≥ 10^{6·0.2} has index [F_r^*:Γ_r] ≤ 2 (no exception in ~2 700 primes), and for each such r
  an explicit Q ∈ ⟨S⟩ with r | n + 4Q² is found. Also #{13 ≤ r < 10⁶ : |Γ_r| ≤ r^{3/4}} = 0.
* Prop 2.1's identity and parity analysis re-derived by hand (x + Q² = e(r+1)/4; v_q(x) = s if s < 2c, else ≥ 2c), and
  the §2 counterexample 4/9 = 1/449 + 1/18 + 3125/8082 (no parity normalisation) is reproduced by the same formulas.

### Defects for Thm 2.4(a)
* **m1 (MINOR, effectivity, Thm 2.4 / Remark (2)).** The lower-bound sieve uses Bombieri–Vinogradov, whose implied
  constant is ineffective (Siegel). The proof therefore gives no computable bound on r or Q in terms of n. Not an
  error, but "unconditionally" should be accompanied by "ineffective (no bound on Q)". *Repair:* add one sentence.
* **m2 (MINOR, Lemma 2.2 statement).** "every prime factor of (r−1)/2 at least x^{1/4−ε}" — for r ≤ x^{1/4−ε} this
  forces (r−1)/2 = 1; harmless, but say "for all r ≤ x counted" to pre-empt the dyadic objection the proof then
  addresses in Thm 2.4 ("No dyadic restriction is needed"). The implied constant depends on M (hence on n) — already
  indicated by ≫_{M,ε}. Fine.
* **m3 (MINOR, Remark (2)).** |S| = 3 indeed looks reachable: Heath-Brown's sieve lemma (≫ x/log²x primes r in a
  progression with (r−1)/2 = P or P₁P₂, P_i > x^{1/4+δ}) gives index ∈ {1, 2} or ≥ x^{1/4+δ}, so |Γ_r| ≤ x^{3/4−δ} and
  Lemma 2.3 with k = 3 gives ≪ x^{1−4δ/3}. Needs the congruence-class version of Heath-Brown's lemma (not checked by
  me either). Keep "not checked", but the stated reason is right.

## 2. T1 of ES^{(S)}: Lemma 1.1, Cor 1.2, Thm 2.4(b)

**Re-derivation of Lemma 1.1.** Fix q ∈ S, q ∤ n, v_q(z) = −w < 0, w even (x, y ∈ ℤ so v_q(x), v_q(y) ≥ 0).
(iii) v(x) = 0 < v(y): 1/y is the unique term of negative valuation — impossible. (ii) v(x) = V > 0: the minimum
valuation −V must be attained twice, so v(y) = V; 1/x + 1/y = 4/n − 1/z is q-integral, so v(x+y) ≥ 2V, i.e.
a = −y/x ≡ 1 (mod q^V); v(a) = 0, so the tame symbol is a^{v(b)} ≡ 1. (i) v(x) = v(y) = 0: v(a) = 0, v(b) = −w, tame
symbol a^{−w}, a square for w even. In all cases (a,b)_q = 1. Case v_q(z) ≥ 0: Thm 2.1(b), whose proof is purely local
(only q-integrality used) — correct. For w odd the symbol is the Legendre symbol (a/q), which is unconstrained —
correct, and confirmed by the control run below.

**Cor 1.2.** inv_∞ = ½ (all positive); inv_2 = 0 (z ∈ ℤ_{(2)}, n odd; Thm 2.1(c) is local); inv_q = 0 (Lemma 1.1);
inv_ℓ = 0 for ℓ ∤ 2nS (Thm 2.1(b)); Hilbert reciprocity ⇒ Σ_{ℓ|n} inv_ℓ = ½; Thm 2.1(d) (re-derived: Type II gives
symbol (−u₂/u₃)^V, a square if V even and ≡ 1 if V odd since then V > 2s; Type I forces v₁ = 2s, symbol a
2s-th power) applies at ℓ | m because ℓ ∉ S makes all three variables ℓ-integral. SOUND.

**Thm 2.4(b), first half** ("no such (Q, r)"): m² + (2Q)² with gcd(m, 2Q) = 1 is a sum of two coprime squares — SOUND.

**From-scratch check** (`scripts/review_uo2_t1.py`, own Hilbert symbols at ∞, 2, q ∈ S, ℓ | n; box n/4 < x ≤ 3n,
x ≤ y ≤ 300n; product formula asserted on every solution):
| n | mode | solutions | Σ_{ℓ|n} inv | shapes at primes of n | some inv_q = ½ |
|---|---|---|---|---|---|
| 13 | mute | 121 | ½ always | I 62, II 59 | 0 |
| 29 | mute | 186 | ½ always | I 101, II 85 | 0 |
| 169 | mute | 491 | ½ always | **o 491** | 0 |
| 289 | mute | 566 | ½ always | **o 566** | 0 |
| 361 (box 2n, 100n) | mute | 497 | ½ always | **o 497** | 0 |
| 221 = 13·17 (box 2n, 100n) | mute | 1405 | ½ always ((½,0) 766, (0,½) 639) | all patterns incl. o/I, II/o | 0 |
| 169 | free (no parity) | 4002 | ½: 1264, 0: 2738 | I 1344, II 428, o 2230 | 3004 |
| 289 | free | 4922 | ½: 1527, 0: 3395 | I 1860, II 527, o 2535 | 3710 |
inv_2 = 0 on every solution of both modes. The author's counts (121/186/491/566, control 4002/4922, 1344+428,
1860+527, 3004/3710) are reproduced exactly by independent code.

### Defects for the T1 part
* **m4 (MINOR, quantifier, Thm 2.4(b)).** "ES^{(S)}(n) has no solution of Type I/II shape at all (Cor 1.2)" overstates
  Cor 1.2, which only excludes solutions that are Type I/II-shaped *at every prime of m simultaneously*. For a square
  with ≥ 2 prime factors, solutions that are Type I/II at one prime and "other" at another are not excluded by the
  invariant argument (they do occur for V_φ at 121 = 𝔮²𝔮'², T1_TEMPLATE §1 table: 615 such). I could not test a
  two-prime square for ES^{(S)} (smallest coprime to 2S is (13·17)² = 48 841, box too large). *Repair:* "no solution
  of Type I/II shape at every prime of n".
* **m5 (MINOR, presentation, Cor 1.2 proof).** T1_TEMPLATE Thm 2.1 is stated for u ∈ O_K³, but here z ∉ ℤ in general.
  The proofs of 2.1(b),(c),(d) are local and only use v-integrality, which holds at v = 2, ℓ ∉ S. Say so once
  ("Thm 2.1(b)–(d) are local: they hold for u ∈ O_v³") instead of relying on the parenthetical remarks.

## 3. Thm 5.1 (V_φ: #{odd n ≤ X not orbit-solved} ≪ X^{3/4} log²X) — SOUND

**Re-derivation.** For a degree-1 𝔮 ∤ 10 (ℓ = N𝔮) and n with ℓ ∤ n: 𝔮 | a_k ⟺ −n/4 ≡ φ^{2k+1} (mod 𝔮), k ∈ ℤ, so
"some a_k has a prime factor 𝔮 with (n/𝔮) = −1" holds whenever n mod ℓ ∈ S_ℓ = {n : −n/4 ∈ C, (n/ℓ) = −1},
C = φ⟨φ²⟩ (|C| = m if m = ord(φ) is odd, m/2 if even, so |C| ≥ m/2); (n/𝔮) = (n/ℓ) for degree 1, and 𝔮 ∤ 2n, so
T1_TEMPLATE Thm 1.3(b) applies. |S_ℓ| = #{c ∈ C : (−c/ℓ) = −1}; for good 𝔮 every c qualifies (ℓ ≡ 1 (4), C ⊂
non-squares; or ℓ ≡ 3 (4), C ⊂ squares), and for non-good 𝔮 S_ℓ = ∅ (so restricting to good 𝔮 loses nothing).
[K(i, √φ) : K] = 4 (i ∈ K(√φ) is impossible: K(√φ) has a real place above σ₁), so good 𝔮 have Chebotarev density ½
among degree-1 primes. 𝔮 with m ≤ y divide ∏_{j ≤ y} N(φ^j − 1) (all non-zero), log ≪ y², so ≪ y² such ℓ; with
y = x^{1/2}/log x this is ≪ x/log²x = o(π(x)) per dyadic block. Hence ≫ x/log x primes ℓ ∈ [x/2, x] carry a good 𝔮
with |S_ℓ| ≥ ℓ^{1/2}/(2 log ℓ) (≤ (ℓ−1)/2 < ℓ). Montgomery's large sieve, restricted to prime moduli:
|𝒩| ≤ (X + L²)/J, J ≥ Σ_{ℓ ∈ 𝒫, ℓ ≤ L} ω(ℓ)/(ℓ − ω(ℓ)) ≥ Σ ℓ^{−1/2}/(2 log ℓ) ≫ L^{1/2}/log²L (partial summation over
dyadic blocks). L = X^{1/2} ⇒ |𝒩| ≪ X^{3/4} log²X. Every step checks; no uniformity issue (φ fixed, constants absolute).
The label "PROVED relative to the arithmetic large sieve and Chebotarev" is accurate (both are theorems, so plain
PROVED would also be fair).

**From-scratch check** (`scripts/review_uo2_phi.py 100000 3000 20000`): sieving all odd n ≤ 10⁵ by the local criterion
over every split 𝔮 with ℓ ≤ 3000 plus 𝔮 = (√5) (φ ≡ 3) leaves exactly 228 survivors, which are exactly T ∩ [3, 10⁵]
(T = {m², 5m²}, m odd). (The survivors of a finite sieve are a superset of the true exceptional set, and T ⊆ exceptions
by Thm 1.3(a), so the exceptional set below 10⁵ is exactly T — consistent with Thm 5.2, much stronger than 5.1's
bound.) Among the 2 244 split 𝔮 with ℓ ≤ 20 000, 1 127 (0.502) are good; on every good 𝔮, |S_ℓ| = |C| ≥ m/2 holds and
|S_ℓ| ≥ 4.65 · ℓ^{1/2}/(2 log ℓ). The final remark of §5 ((√5) | a_k for n ≡ ±2 mod 5) re-derived: φ ≡ 3 (mod √5),
−4·3^{2k+1} ∈ {2, 3} = the non-residues mod 5.

### Remarks on Thm 5.1 (no defects)
* **r1 (suggestion, not a defect).** The order bound m ≥ ℓ^{1/2}/log ℓ is the weakest available; any positive-density
  set of good primes with ord_𝔮(φ) ≥ ℓ^θ gives ≪ X^{1−θ/2+o(1)}. Large-prime-factor-of-ℓ−1 results (Baker–Harman type,
  θ ≈ 0.677) would need to be available inside the Chebotarev class "good" of the non-abelian field K(i, √φ, √φ̄) —
  not checked; leave the X^{3/4} statement as is or flag the improvement as an Assessment.
* **r2.** The "Contrast with ES" paragraph (|S_ℓ| ≍ ℓ ⇒ X^{1/2+o(1)}, "squares saturate the large sieve") is
  arithmetic-correct as a conditional remark; the reference to DISCOVERIES (A)19–20 was not re-checked here.
