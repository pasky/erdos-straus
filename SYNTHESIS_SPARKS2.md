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

## 3. Attack B (seed (iii)): an explicit fixed-modulus shot family for the order-3 TES, and TES with cubic mute places

Setting of TWISTED_T1 §3: O = ℤ[ω], λ = 1 − ω, TES(n): 9/n = ω/x + ω²/y + 2/z, x, y, z 2-primary (≡ 1 mod 2O);
n 2-primary, gcd(n, 6) = 1; α(u) = (−u₁/u₃, −u₂/u₃)_ω, u = (x/ω, y/ω², z/2). Put **g₀ := 10 + ω** (the class mod 18 with
g₀ ≡ −ω² (mod 9), g₀ ≡ ω (mod 2)).

**Proposition 3.1 (TES shot identity; PROVED, elementary).** Let D ∈ O with D ≡ 1 (mod 2) and gcd(D, 6n) = 1, and let
g ∈ O with g | n + 18D and g ≡ g₀ (mod 18). Put E := (n + 18D)/g, a := (g + ω²)/9, x := (ωn + E)/9, y := na, z := nxa/D.
Then x, a ∈ O, 9/n = ω/x + ω²/y + 2/z, x and y are 2-primary, z = Z/D with Z = nxa ≡ 1 (mod 2), and for every prime
π | n the solution has Type II shape at π (π ∤ x, v_π(y), v_π(z) ≥ v_π(n)).
*Proof.* x ∈ O: −ω²E ≡ gE = n + 18D ≡ n (mod 9), so E ≡ −ωn and 9 | ωn + E. a ∈ O by g ≡ −ω² (mod 9). Since
ωg + 1 = ω(g + ω²) = 9ωa: 9gx = ωng + n + 18D = 9ωna + 18D, i.e. **gx = ωna + 2D**. Then ω²x + 2D = x(g + ω²) − ωna
= a(9x − ωn) = aE, so ω²/y + 2/z = (ω²x + 2D)/(nxa) = E/(nx) = (9x − ωn)/(nx) = 9/n − ω/x. Mod 2: g ≡ ω, so
a ≡ ω + ω² ≡ 1, y ≡ 1, E ≡ g⁻¹ ≡ ω², x ≡ ω + ω² ≡ 1, Z ≡ 1. Shape: π ∤ 18D, so π ∤ n + 18D, π ∤ E, π ∤ x. ∎
For D = 1 this is a single shot n + 18 (TES's analogue of Mordell's p + 4); for D = Q³ it is an orbit with FIXED
modulus 18 (Q³ ≡ 1 (mod 2) automatically, as F₄^* has exponent 3 — the cube is invisible to the anchor).

**Definition (cubic mute variant).** For a set S of primes of O not dividing 6, **TES^{(S)}(n)**: 9/n = ω/x + ω²/y + 2/z
with x, y ∈ O 2-primary, z ∈ O[1/S] with z ∈ 1 + 2O₂, and for each q ∈ S the normalisation
`(N_q)  if v_q(z) < 0 and q ∤ x, then 3 | v_q(z).`
TES^{□₃} := TES^{(S)} with S = all primes not dividing 6n. (Shot solutions satisfy (N_q): q | Q, c = v_q(Q),
s = v_q(a); q ∤ g, so gx = ωna + 2Q³ gives v_q(x) = s if s < 3c and v_q(x) ≥ 3c otherwise; then v_q(z) = 2s − 3c
(s < 3c) and the case q ∤ x is s = 0, v_q(z) = −3c.)

**Lemma 3.2 (cubic mute lemma; PROVED).** For q ∈ S, q ∤ n, every TES^{(S)} solution has inv_q α = 0 in ⅓ℤ/ℤ.
*Proof.* If v_q(z) ≥ 0 all u_i are q-integral and TWISTED_T1 Thm 3.2's tame case applies. Let v_q(z) = −w < 0. Then
2/z ≡ 0 (mod q^w) and 9/n is a unit, so ω/x + ω²/y is q-integral; with x, y ∈ O this forces v_q(x) = v_q(y) =: V
(one of them positive and the other zero is impossible). A := −u₁/u₃, B := −u₂/u₃ have v(A) = v(B) = V + w =: v and
A/B = ωx/y; the tame symbol is (−1)^{v²}(A/B)^v = (−1)^v(ωx/y)^v, and −1 is a cube. (i) V = 0: (N_q) gives 3 | w = v,
so the symbol is a cube. (ii) V > 0: integrality of (ωy + ω²x)/(xy) gives v(ωy + ω²x) ≥ 2V, so y/x ≡ −ω (mod q^V) and
ωx/y ≡ −1: the symbol is (−1)^{2v} = 1. ∎ (The same computation with ω ↦ 1 and cubes ↦ squares shows that
UNIT_ORBIT_ES Lemma 1.1 needs its parity condition only when q ∤ x.)

**Theorem 3.3 (T1₃ for TES^{(S)}; PROVED from TWISTED_T1 Thm 3.2's proof + Lemma 3.2).** For every solution of
TES^{(S)}(n), Σ_{π|n} inv_π α = −⟨ω, 2⟩₂ ≠ 0. Hence at n = π^{3k} (π ∤ 6 prime, π ∉ S) no solution has Type I/II
shape at π. *Proof.* The place-by-place computation of TWISTED_T1 Thm 3.2 needs: x, y, z ∈ 1 + 2O₂ (anchor; ✓), u_i
λ-integral (partner; S ∌ λ ✓), integrality at tame v ∉ S, v ∤ n (✓); places in S contribute 0 (Lemma 3.2). ∎

**Corollary 3.4 (a cubic-character identity forced by T1₃; PROVED relative to Hecke's theorem on prime ideals in ray
classes).** For every prime element r ≡ 10 + ω (mod 18), 18 is not a cube modulo r.
*Proof.* If −18 ≡ t³ (mod r) (−1 is a cube), pick (Hecke) a prime π ≡ t (mod r), π ≡ 1 (mod 2), π ∤ 6. Then
r | π³ + 18, and Prop 3.1 (D = 1, g = r) gives a Type II-shaped solution of TES(π³), contradicting Thm 3.3. ∎
(By the cubic supplementary laws (18/r)₃ depends only on r mod 18, so it is a constant ≠ 1 on the class; numerically
(18/r)₃ = ω² for all 27 such r with N(r) ≤ 6000. A direct derivation from the supplements was not done.)

**Theorem 3.5 (TES^{□₃} at every non-cube; PROVED relative to Chebotarev for the abelian extension L·K(∛n)/K, L the
ray class field of K mod 18).** Let n ∈ O be 2-primary, gcd(n, 6) = 1, n not a cube. Then TES^{□₃}(n) has a solution
of Type II shape at every prime of n; if n is a cube, none of Type I/II shape at every prime (Thm 3.3).
*Proof.* As h_K = 1 and μ₆ → (O/18)^* is injective, "(𝔯) has a generator ≡ g₀ (mod 18)" is one class c₀ of the ray
class group mod 18. If all v_π(n) were ≡ 0 (mod 3), n = u·m³ with a unit u ≡ 1 (mod 2), i.e. u = ±1, and n would be a
cube; so some π | n (π ∤ 6) has 3 ∤ v_π(n), and M = K(∛n) is ramified at π while L is unramified outside 6. Hence
L ∩ M = K, Gal(LM/K) = Gal(L/K) × Gal(M/K), and Chebotarev gives a degree-1 prime 𝔯 = (r), r ≡ g₀ (mod 18), r ∤ n,
with (n/r)₃ = (18/r)₃. Then −n/18 ≡ Q³ (mod r) for some Q ∈ O, which may be taken ≡ 1 (mod 2) and prime to 6n (CRT),
and Prop 3.1 with D = Q³, g = r gives the solution; it satisfies (N_q) (remark after the Definition). ∎

**EVIDENCE (`scripts/syn2_tes_shots.py 6000 200`, 1.4 s; ℤ[ω] arithmetic from `scripts/tw_eis.py`, factorisation via sympy).**
(1) All 27 prime elements r ≡ 10 + ω (mod 18) with N(r) ≤ 6000 have cubic class of 18 equal to ω² (Cor 3.4).
(2) All 1536 2-primary split primes π (both 2-primary associates of each of the 768 split primes 7 ≤ N(π) ≤ 6000) are solved by
Thm 3.5's recipe with the least admissible r (max N(r) = 3187, max Q = 3671 ∈ ℤ): equation verified exactly in O,
2-primarity checked, Type II shape at π in all 1536, inv_π α = ω²-class "2" in all 1536 (matches TWISTED_T1's census
value (1, 2, 0)), and the cubic tame invariant at every mute prime above every q | Q is 0 (2908 places; Lemma 3.2).
(3) T1₃ control: for the 2-primary cubes π³, N(π) ≤ 200, and Q ≤ 39 prime to 6N(π) (267 shots), no divisor of
π³ + 18Q³ (any associate) lies in the class g₀.
(4) The plain single shot π + 18 (D = 1, TES itself) fires for only 52 of the 768 2-primary split primes with N(π) ≤ 6000.
(TES itself is not claimed at any prime here.)

**Reading (Assessment): the uniform principle and what it says about ES.**
* Order 2 and order 3 now behave identically: anchor (positivity / 2-primary) + wild partner (4 = 2², 9 = λ⁴·unit) +
  mute places normalised by m-th powers in the free slot. With infinitely many mute places, one Dirichlet/Hecke prime
  proves the variant at every non-m-th-power (ES^□: Prop 2.2; TES^{□₃}: Thm 3.5); with a fixed finite S, it is an
  Artin problem (m = 2: (J)23 for |S| ≥ 4, unconditional; m = 3: not attempted — a Gupta–Murty sieve over ℚ(ω) with
  the condition −n/18 ∈ ⟨S⟩³ mod 𝔯 is the natural route, CONJECTURE); with S = ∅ it is a finite search ((J)25).
* The T1 is never the difficulty: the T1-sensitive step is always a single character value ((n/r) = −1, resp.
  (n/r)₃ = (18/r)₃ ≠ 1), and Chebotarev supplies it whenever n is not an m-th power. The entire difficulty of ES
  is the size of the shot orbit, and over ℤ with S = ∅ it is one point plus the growing-modulus lines of the
  certificate cube.
* So the "exact obstruction for ES" in seed (iii) is not a missing mute place per se but the absence of any
  equivalence ES ⟺ (variant with a mute place) + (cheap condition): the extra condition is O186 Prop 6.1's
  g ≡ −1 (mod 4Q), which is B2. A T1-bearing variant being provable carries no information about ES.
