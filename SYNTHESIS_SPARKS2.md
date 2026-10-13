# SYNTHESIS_SPARKS2 — cross-pollinating (J)13–(J)25 (task O192, spark synthesis II)

Status: in progress (O192). ES is not solved, here or anywhere; nothing below proves a case of it.
Scripts `scripts/syn2_*`. Inputs: DISCOVERIES (J)11–(J)25 and the documents behind them; O178 DEPTH_ASPECT and O188
STERILE_STEER read from their branches (under review); SYNTHESIS_SPARKS.md (O171).

## 0. Iteration log

* (S1) Read the (J)13–(J)25 headlines and UNIT_ORBIT_ES §§1–2, 6, FIXED_MODULUS_SHOTS §§1–6, TWISTED_T1 §3.
  Common thread of the three newest provable variants (V_φ, ES^{(S)}, and the order-3 TES): anchor + wild partner +
  an *orbit* of shots with fixed modulus. The thread of (J)25: ES has no orbit (finite search, moduli O(p²)).
* (S2) Barrier question for (J)23: which hypothesis of its proof is load-bearing? The sieve (Bombieri–Vinogradov +
  Rosser–Iwaniec + Gupta–Murty) is needed only because S is FIXED. Letting S grow with n (seed (ii)) the variant becomes
  elementary (§2). This recalibrates what a "provable T1-bearing variant" is worth.
* (S3) Seed (iii) built concretely: an explicit fixed-modulus Type II shot family for the order-3 TES over ℤ[ω]
  (shot n + 18Q³, class condition mod 18), and a cubic mute normalisation (§3).

## 1. Cross-combinations (≥ 8), each with a sketch and a barrier pre-screen

(filled in below, one entry per step)

## 2. Attack A (seed (ii) pushed to the end): with a growing mute set the T1-bearing variant is elementary

Notation of UNIT_ORBIT_ES §1. Let **ES^□(n)** be ES^{(S)}(n) with S = all odd primes not dividing n, i.e.
`4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℚ_{>0} whose denominator is an odd square coprime to n.`
ES ⊂ ES^{(S)} ⊂ ES^□ for every finite S.

**Lemma 2.1 (T1 for ES^□; PROVED).** UNIT_ORBIT_ES Lemma 1.1 and Cor 1.2 hold verbatim for ES^□: every solution has
Σ_{ℓ|n} inv_ℓ α = ½, so at n = m² (m odd) no solution has Type I/II shape at every prime of m.
*Proof.* Lemma 1.1 is a statement at one place q; a given solution involves finitely many q, each muted (v_q(z) even
when negative); inv_2 = 0 because the denominator of z is odd; inv_∞ = ½. Cor 1.2's proof is then unchanged. ∎

**Proposition 2.2 (ES^□ at every non-square, elementary; PROVED, relative to Dirichlet's theorem only).** Let n > 1 be
odd and not a square.
(a) If n ≡ 3 (mod 4), Q = 1 and g = n + 4 give an ES solution (O186 Prop 3.1).
(b) If n ≡ 1 (mod 4), there is a prime r ≡ 3 (mod 4), r ∤ n, with Jacobi symbol (n/r) = −1. For the least such r
(call it r(n)) there is an odd Q, 0 < Q < 2r, gcd(Q, n) = 1 (enlarge Q by multiples of 2r if needed), with
4Q² ≡ −n (mod r), and UNIT_ORBIT_ES Prop 2.1 with g = r gives an explicit ES^□ solution of Type II shape at every
prime of n, with denominator of z dividing Q².
*Proof of (b).* n = n₀m², n₀ > 1 squarefree, n₀ ≡ 1 (mod 4) (as n ≡ 1 (mod 4) and m odd). The Jacobi character
(·/n₀) is non-trivial, so CRT gives a class a mod 4n₀ with a ≡ 3 (mod 4), (a/n₀) = −1; Dirichlet gives a prime
r ≡ a, r ∤ m. Then (n/r) = (n₀/r) = (r/n₀) = −1 (reciprocity, n₀ ≡ 1 (mod 4)). As (−1/r) = −1, −n/4 is a square mod r;
the two roots ±s give one odd representative in (0, 2r); the class s + 2rℤ contains elements prime to n (CRT, no prime
of n divides 2r). Prop 2.1 of UNIT_ORBIT_ES needs only g ≡ 3 (mod 4), g | n + 4Q², Q odd and prime to n. ∎
*Quantitative remark (Assessment; standard inputs, not re-derived).* r(n) is the least prime in a union of classes of
density ¼ for the pair of characters (χ₋₄, (·/n₀)); under GRH r(n) ≪ (log n)² (Bach-type bound), unconditionally
r(n) ≪ n^{O(1)} (Linnik). So under GRH one may take S = {odd primes < 2r(n)}, |S| ≪ (log n)²/log log n, and
Q < 2r(n) ≪ (log n)².

**EVIDENCE (`scripts/syn2_sqden.py 1000000`, < 1 s).** All 78 496 primes 5 ≤ p ≤ 10⁶ solved by Prop 2.2, every solution
checked exactly (equation, positivity, odd square denominator coprime to p, Type II shape). For p ≡ 1 (mod 4):
max r(p) = 131 (p = 880 993); r(p) = 3, 7, 11, 19, 23, 31, … for 19 611, 9 825, 4 948, 2 444, 1 191, 624, … primes (each
next value roughly halves, as for a least non-residue). T1 control: for all odd squares m² ≤ 10⁶ and all odd Q ≤ 99
prime to m, m² + 4Q² has no prime factor ≡ 3 (mod 4) (0 found, as forced: a sum of two coprime squares).

**Reading (Assessment, the point of Attack A).**
1. The T1-bearing variant ES^□ is *trivially* true at every non-square: one Dirichlet prime, no sieve. The whole
   analytic content of (J)23 Thm 2.4 (Bombieri–Vinogradov + Rosser–Iwaniec + Gupta–Murty, ineffective) is the
   restriction to a FIXED finite S. Hence "a T1-bearing ES variant is provable" is, by itself, weak evidence for
   anything about ES: T1 is respected automatically by every shot mechanism whose firing condition is the quadratic
   character (n/r) = −1, and existence of such r is Dirichlet. What made (J)21/(J)23 non-trivial is the *size* of the
   orbit (rank 1 or fixed |S|), i.e. an Artin-type problem — not the T1.
2. The hierarchy ES = ES^{(∅)} ⊂ ES^{(S)} (fixed S, ineffective theorem) ⊂ ES^{(S_n)} (S_n = primes < 2r(n), elementary)
   ⊂ ES^□ is a scale of "how many mute places", and ES sits at the bottom, where the orbit is one point. Seed (ii)'s
   question "S = primes ≤ log p with Q ≤ p^{O(1)}" is answered positively (under GRH, S = primes ≪ log²p, Q ≪ log²p),
   and the conversion to an ES triple is still exactly "g ≡ −1 (mod 4Q)" (O186 Prop 6.1): for g = r(p) prime this
   needs Q | (r+1)/4, i.e. Q ≤ (r+1)/4 — a box condition (FIXED_MODULUS_SHOTS Cor 3.2) on the specific root
   Q ≡ √(−p/4) (mod r), the least-non-residue lottery in another dress. Minimal change: none exists between "z ∈ ℤ"
   and "denominator of z ∈ ⟨S⟩²"; the mute normalisation is all-or-nothing per prime.
