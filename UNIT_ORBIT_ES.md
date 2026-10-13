# UNIT_ORBIT_ES — infinite unit orbits as "infinitely many shots" (task O186, spark relay L)

Status: in progress (O186). **ES is not solved here, nor any infinite case of ES itself.** Labels as in DISCOVERIES.md.
Builds on T1_TEMPLATE.md (O183, CLAIMED, under review R183): its Thm 2.1 (local invariants on integral points) and
Cor 2.2 (T1 for sign-pattern ES) are used below and re-derived where the setting changes. Scripts `scripts/uo_*`,
memos `BRAINSTORM/bsL_*.md`, literature `sources/uo/LITERATURE.md` (research subagent; statements marked
READ/SEC/RECALL there).

## 0. Plan and iteration log

(L1) **Reduction.** In every unit-Type-II mechanism (T1_TEMPLATE Prop 1.2) the case p ≡ 3 (mod 4) is trivial
(g = a_k itself, §3). For p ≡ 1 (mod 8) no Jacobi-symbol/reciprocity argument can produce the required prime,
because the product formula sees p exactly as it sees m² (§3, Prop 3.2). So an analytic input (Chebotarev + an
Artin-type sieve) is unavoidable; the target is an *unconditional* sieve.

(L2) **First screen: number fields (V_φ, ES over r₁ = 1 fields).** The unconditional Artin-type sieves
(Gupta–Murty, Heath-Brown, Harper–Murty) need (a) unit rank ≥ 4 (≥ 3 with level > ½) and (b) a level-½
Bombieri–Vinogradov theorem for *every* Frobenius condition imposed. I show (§4) that every number-field
unit-orbit variant forces a quadratic Kummer condition `(u/𝔮) = prescribed` for a unit u, which is not a
condition on N𝔮; the best known level for such conditions (Murty–Petersen) is 1/([K:ℚ] − 2), and the
arithmetic of the threshold then never closes. Hypothesis of the barrier that the variant satisfied: *the orbit
is a coset ηU² with η not a square* (forced by a mute REAL place, which needs η < 0 there).

(L3) **Modification: make the mute place FINITE.** A finite prime q can be muted by a parity normalisation
(only one denominator may contain q, and only to an even power). Then the orbit is Q², Q ∈ ⟨S⟩ — inside the
squares — and everything happens over ℚ, where all Frobenius conditions are congruences. Result (§1–§2): a
T1-bearing ℤ-equation ES^{(S)} containing ES, solvable at every prime **unconditionally** for |S| ≥ 4.

(L4) Unconditional statements for V_φ itself: almost-all with power saving and an exact-T1 failure set under
GRH (§5).

## 1. The q-mute variant ES^{(S)} over ℤ

Let S be a finite set of odd primes and ⟨S⟩ the multiplicative monoid it generates.

**Definition.** For n ∈ ℤ_{>0} with gcd(n, 2S) = 1:
`ES^{(S)}(n):  4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℤ[1/S]_{>0},  v_q(z) ∈ 2ℤ for every q ∈ S with v_q(z) < 0.`
Equivalently `4/n = 1/x + 1/y + Q²/Z` with x, y, Z ∈ ℤ_{>0}, Q ∈ ⟨S⟩, gcd(Z, Q) = 1. For S = ∅ (or Q = 1) this
is ES; every ES solution is an ES^{(S)} solution.

**Lemma 1.1 (q-adic invariant on normalised points; PROVED).** Let q ∈ S, q ∤ n, and u = (x, y, z) a solution as
above, α(u) = (−u₁/u₃, −u₂/u₃) ∈ Br ℚ[2] (T1_TEMPLATE §2; permutation invariant). Then inv_q α(u) = 0.
*Proof.* If v_q(z) ≥ 0 all three are q-integral and T1_TEMPLATE Thm 2.1(b) applies. Let v_q(z) = −w, w > 0 even;
x, y are q-integral and 1/z ≡ 0 (mod q^w). Use x as denominator: α = (a, b), a = −y/x, b = −z/x.
(i) v(x) = v(y) = 0: v(a) = 0, v(b) = −w, tame symbol a^{v(b)}·b^{−v(a)}·(−1)^{v(a)v(b)} = a^{−w}, a square
(w even): inv_q = 0.
(ii) v(x) = V > 0: 1/x has valuation −V while 1/z ≡ 0 and 4/n is a unit, so v(y) = V and v(x + y) ≥ 2V > V,
i.e. a = −y/x ≡ 1 (mod q): the tame symbol a^{−w−V} is trivial.
(iii) v(x) = 0 < v(y): then 1/y is the only term of negative valuation — impossible. ∎
(For w odd case (i) gives inv_q = ((−y/x)/q), which is unconstrained: the parity normalisation is exactly what
mutes q. Without it — plain ES over ℤ[1/q] — the T1 dies; explicit example in §2.)

**Corollary 1.2 (T1 for ES^{(S)}; PROVED).** For every solution of ES^{(S)}(n), Σ_{ℓ | n} inv_ℓ α = ½. Hence for
n = m² (gcd(m, 2S) = 1) no solution has Type I/II shape at every prime of m.
*Proof.* inv_∞ = ½ (x, y, z > 0; Thm 2.1(a)); inv_2 = 0 (z ∈ ℤ_{(2)} as S is odd; Thm 2.1(c)); inv_q = 0 for
q ∈ S (Lemma 1.1); inv_ℓ = 0 for odd ℓ ∉ S, ℓ ∤ n (Thm 2.1(b)). Hilbert reciprocity gives the sum; Thm 2.1(d)
(ℓ ∉ S, so the variables are ℓ-integral) gives 0 at every ℓ | m for Type I/II shapes, contradicting ½. ∎
Anchor = ∞ (positivity), partner = 2 (numerator 4), mute places = S (parity normalisation).

## 2. Infinitely many shots p + 4Q², and an unconditional theorem

**Proposition 2.1 (the S-unit-orbit mechanism; PROVED, explicit).** Let gcd(n, 2S) = 1, Q ∈ ⟨S⟩, and r a prime
with r ≡ 3 (mod 4), r | a := n + 4Q². Put e = a/r,
`x = (n + e)/4,  y = n(r + 1)/4,  z = n·x·(r + 1)/(4Q²).`
Then (x, y, z) solves ES^{(S)}(n) and has Type II shape at every prime of n.
*Proof.* a ≡ n (mod 4) and r ≡ −1 give e ≡ −n (mod 4), so x ∈ ℤ_{>0}; y ∈ ℤ_{>0}. Since x + Q² = (a + e)/4 =
e(r + 1)/4: 1/y + 1/z = 4(x + Q²)/(n x (r+1)) = e/(nx) = 4/n − 1/x. *Parity at q ∈ S:* let c = v_q(Q) ≥ 1 (if c = 0,
z is q-integral) and s = v_q(r + 1); note q ∤ a, so r ≠ q. From 4rx = n(r + 1) + 4Q²: if s < 2c then v_q(x) = s
and v_q(z) = 2s − 2c is even; if s ≥ 2c then v_q(x) ≥ 2c and v_q(z) ≥ 0. *Shape:* for ℓ | n, a ≡ 4Q² ≢ 0 (mod ℓ), so
ℓ ∤ e, ℓ ∤ x = (n + e)/4, while n | y and n | n x (r+1)/4. ∎
*So ES^{(S)}(n) has a unit-orbit solution as soon as some n + 4Q², Q ∈ ⟨S⟩, has a prime factor ≡ 3 (mod 4).* For
S = ∅ this is ES's one-shot family "p + 4 has a prime factor ≡ 3 (mod 4)" (fails at 13, 17, 29, …); with S the shots
are indexed by the infinite monoid ⟨S⟩ and each has the FIXED modulus 4 (B2's hypothesis "the modulus is part of the
solution" is violated: the B2 condition "D | x(x + D)/e" is replaced by the automatic parity condition on v_q(z)).
*Mechanism T1:* for n = m², m² + (2Q)² is a sum of two coprime squares, so it has no prime factor ≡ 3 (mod 4).

**Without the parity normalisation the T1 dies (example, verified exactly).** Over ℤ[1/5] with no parity condition,
n = 9, Q² replaced by 5⁵: 9 + 4·5⁵ = 12509 = 7·1787, and Prop 2.1's formulas give
`4/9 = 1/449 + 1/18 + 3125/8082`, Type II shape at 3 (449 prime to 3; 9 | 18, 9 | 8082), with v₅(z) = −5 odd — a
Type II solution at a square. Lemma 1.1 case (i) with w odd: inv₅ = ((−18/449)/5) = ½ absorbs the anchor.

**Lemma 2.2 (shifted primes with rough (r−1)/2 in a progression; PROVED, standard).** Let 4 | M and let a mod M be a
class with gcd(a, M) = 1, a ≡ 3 (mod 4), a ≢ 1 (mod ℓ) for every odd prime ℓ | M. For every ε > 0 there are
≫_{M,ε} x/log²x primes r ≤ x with r ≡ a (mod M) and every prime factor of (r − 1)/2 at least x^{1/4−ε}.
*Proof.* Linear lower-bound sieve (Rosser–Iwaniec; Halberstam–Richert Ch. 8) on 𝒜 = {(r−1)/2 : r ≤ x, r ≡ a (M)},
sifting by primes ℓ ∤ M, ℓ < z = x^{1/4−ε} (primes ℓ | M never divide (r−1)/2: ℓ = 2 by r ≡ 3 (4), odd ℓ by
a ≢ 1 (ℓ)). Local density g(ℓ) = 1/(ℓ − 1), dimension 1. The remainders Σ_{d ≤ D} μ²(d)|π(x; Md, ·) − π(x)/φ(Md)| are
≪ x/log^A x for D = x^{1/2}/log^B x by Bombieri–Vinogradov (moduli Md ≤ M x^{1/2}/log^B x). With s = log D/log z
→ 2/(1 − 4ε) > 2 the lower sieve function f(s) is positive, giving S(𝒜, z) ≫ (x/log x)·(1/log z). ∎
(This is the sieve input of Gupta–Murty, Invent. Math. 78 (1984), with an extra fixed congruence; see
sources/uo/LITERATURE.md Q2.)

**Lemma 2.3 (few primes with a small S-image; PROVED).** Let S = {q₁, …, q_k} be distinct primes and Γ_r the subgroup of
F_r^* generated by S. Then #{r prime : |Γ_r| ≤ y} ≪_S y^{1+1/k}.
*Proof.* Let B = ⌊y^{1/k}⌋. The (B+1)^k > y products ∏q_i^{a_i}, 0 ≤ a_i ≤ B, collide mod r, so r divides
N_c := ∏_{c_i>0} q_i^{c_i} − ∏_{c_i<0} q_i^{−c_i} for some c ∈ ℤ^k ∖ {0}, |c_i| ≤ B. N_c ≠ 0 (unique factorisation),
log|N_c| ≪_S B, so N_c has ≪ B prime factors; there are ≤ (2B+1)^k ≪ y vectors c. Total ≪ y·y^{1/k}. ∎

**Theorem 2.4 (ES^{(S)} at every non-square, unconditionally; PROVED relative to Lemma 2.2's standard sieve).** Let S be
a set of odd primes with 3 ∈ S and |S| ≥ 4. For every n > 1 with gcd(n, 2S) = 1:
(a) if n is not a square, there are Q ∈ ⟨S⟩ and a prime r ≡ 3 (mod 4) with r | n + 4Q²; hence ES^{(S)}(n) holds, with a
solution of Type II shape at every prime of n (Prop 2.1). In particular **ES^{(S)}(p) holds for every prime p ∉ S ∪ {2}.**
(b) if n is a square, no such (Q, r) exists, and ES^{(S)}(n) has no solution of Type I/II shape at all (Cor 1.2).
*Proof of (a).* If n ≡ 3 (mod 4), Q = 1: n + 4 ≡ 3 (mod 4) has a prime factor ≡ 3 (mod 4). Let n ≡ 1 (mod 4). Every
prime ℓ | n is ≥ 5 (3 ∈ S). Pick ℓ₀ | n with v_{ℓ₀}(n) odd; choose residues a_ℓ ≢ 0, 1 (mod ℓ) for ℓ | n, ℓ ≠ ℓ₀,
then a_{ℓ₀} ≢ 0, 1 (mod ℓ₀) such that the Jacobi symbol (a/n) = −1 (possible: there are residues and non-residues
≠ 1 mod ℓ₀ ≥ 5); with a ≡ 3 (mod 4) this defines a class a mod M = 4·rad(n) satisfying Lemma 2.2. For r ≡ a (M),
(n/r) = (r/n) = −1 (reciprocity, n ≡ 1 (4)) and (−1/r) = −1, so −n/4 is a square mod r. Take x large, r ∈ [x/2, x]
from Lemma 2.2. If [F_r^* : Γ_r] ∉ {1, 2} it has an odd prime factor, which divides (r−1)/2 and so is ≥ x^{1/4−ε},
whence |Γ_r| ≤ x^{3/4+ε}; by Lemma 2.3 (k = |S| ≥ 4) there are ≪ x^{(3/4+ε)(5/4)} = o(x/log²x) such r. So some r has
[F_r^* : Γ_r] ≤ 2, i.e. Γ_r ⊇ (F_r^*)² (r ≡ 3 (mod 4): F_r^* = {±1} × squares of odd order), hence
{Q² : Q ∈ ⟨S⟩} ⊇ (Γ_r)² = (F_r^*)² ∋ −n/4 (exponents can be taken ≥ 0 as Γ_r is finite): r | n + 4Q². (b) is the
mechanism T1 above plus Cor 1.2. ∎
*Remarks.* (1) The theorem is "exact-T1": the mechanism succeeds at n iff n is not a square. (2) The only analytic
inputs are Bombieri–Vinogradov and the linear sieve; no GRH. The condition 3 ∈ S only avoids n = 3m² (where 3 | r − 1
for every admissible class); |S| = 3 should follow from Heath-Brown's sieve (Quart. J. Math. 37 (1986)), not checked.
(3) The variant is weaker than ES (more solutions); the point is the *mechanism*: a T1-respecting existence proof
whose T1-sensitive step is the Chebotarev condition (n/r) = −1 and whose "infinitely many shots" come from the
infinite S-orbit with fixed modulus.

**EVIDENCE (`scripts/uo_mute.py`, S = {3, 5, 7, 11}).** All 78 493 primes 13 ≤ p < 10⁶ are solved by Prop 2.1, every
solution verified exactly (equation, positivity, parity of v_q(z), Type II shape); smallest Q = 1 for 68 652 primes
(ES's own family), largest needed Q = 81. All 62 224 odd non-squares n < 3·10⁵ coprime to 3·5·7·11 are solved
(largest Q = 99); no square has a hit (as proved).
