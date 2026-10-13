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

**EVIDENCE for the T1 of ES^{(S)} (`scripts/uo_mute_t1.py 3 300 n…`, S = {3,5,7,11}; box x ≤ 3n, y ≤ 300n; local
invariants by Hilbert symbols at ∞, 2, q ∈ S, ℓ | n).** n = 13, 29, 37: 121, 186, 174 solutions (most with z ∉ ℤ),
all Type I or II, invariants (inv_∞, inv_p) = (½, ½). n = 13², 17², 19²: 491, 566, 745 solutions, **all of "other"
shape**, (½, ½). On all 2283 solutions inv_q = 0 for q ∈ S (Lemma 1.1) and the product formula holds.
*Control (`uo_mute_t1.py -3 300 169 289`: parity normalisation dropped):* 4002 / 4922 solutions, of which
1344 + 428 / 1860 + 527 have Type I/II shape at the square, with inv_{13} resp. inv_{17} = 0 and some inv_q = ½
(3004 / 3710 solutions have a nonzero q-invariant): the mute normalisation is exactly what keeps the T1.

## 3. Two reductions valid for every unit-orbit variant

**Proposition 3.1 (p ≡ 3 mod 4 is free; PROVED).** In V_φ, in ES over any K with one real place, and in ES^{(S)}, if
n ≡ 3 (mod 4) then the shot a = n + 4η (any η in the orbit) works with g = a, e = 1 (a ≡ −1 (mod 4), positive at
the anchor): x = (n + 1)/4. (The ES analogue x = (p + 1)/4.)

**Proposition 3.2 (no reciprocity proof for n ≡ 1 mod 8; PROVED).** Let K be any number field, n ≡ 1 (mod 8)
a positive rational integer, η ∈ O_K^* (or η = Q² with Q an S-unit, S odd) and a = n + 4η, coprime to n. Then
∏_{𝔮 | a} (n/𝔮)^{v_𝔮(a)} = 1, the value it has for n = m². So the existence of a prime 𝔮 | a with (n/𝔮) = −1
can never be forced by Jacobi symbols / the product formula; every existence proof needs an input that sees
individual primes (Chebotarev, sieve).
*Proof.* Quadratic reciprocity in K: (n/a)(a/n) = ∏_{v | 2∞}(n, a)_v. n > 0 and n ∈ ℚ₂^{*2} (n ≡ 1 (8)), so all
these symbols are 1. (a/n) = (4η/n) = ∏_{ℓ | n}(N_{K/ℚ}(η)/ℓ)^{v_ℓ(n)} = 1 (residue symbols of a unit at the primes
over ℓ multiply to the Legendre symbol of its norm ±1, and (−1/ℓ) cancels as n ≡ 1 (4); for η = Q² it is a square). ∎

## 4. Why the number-field versions resist an unconditional proof (the Kummer obstruction)

**Proposition 4.1 (the forced Kummer condition; PROVED).** Let ES_{P,M} be a T1-bearing sign-pattern variant over K
(T1_TEMPLATE Cor 2.2: |P| odd, F = ∅), 𝔪 = 4∞_P, c₀ ∈ Cl_𝔪(K) the class of (g) with g ≡ −1 (mod 4), g ≫_P 0, and
U_𝔪 = {u ∈ O_K^* : σ_v(u) > 0 for all real v ∉ P}. A unit-Type-II shot at a prime 𝔮 ∤ 2n (𝔮 | n + 4η with
[𝔮] = c₀) forces, for every u ∈ U_𝔪,
`(u/𝔮) = χ_u(c₀) = (−1)^{#{v ∈ P : σ_v(u) < 0}}.`
*Proof.* K(√u)/K has conductor dividing 𝔪 (unit radicand: discriminant | 4; real ramification only at v ∈ P), so
χ_u factors through Cl_𝔪 and (u/𝔮) = χ_u(c₀). By reciprocity χ_u((g)) = ∏_{v | 2∞}(u, g)_v. At real v ∉ P, u > 0;
at v ∈ P, g > 0: archimedean factors are 1. At v | 2, (u, g)_v = (u, −1)_v (u, −g)_v and −g ≡ 1 (mod 4) makes
K_v(√−g)/K_v unramified, so (u, −g)_v = 1 for the unit u. Finally ∏_{v|2}(u, −1)_v = ∏_{v real}(u, −1)_v by the
product formula (odd places: two units). ∎
*Consequences.* (a) V_φ (K = ℚ(√5), P = {σ₁}): U_𝔪 = ⟨−φ⟩U², the forced condition is (−φ/𝔮) = −1, a Frobenius
condition in K(√−φ), which is not Galois over ℚ (σ₁(−φ) < 0 < σ₂(−φ)), hence not a condition on N𝔮. For
ℓ = N𝔮 ≡ 3 (mod 4) and ⟨−1, φ⟩ of index ≤ 2 mod 𝔮 the shot condition is exactly "(−φ/𝔮) = −1 and (n/ℓ) = −1".
(b) ES over K with r₁ = 1: U_𝔪 = O_K^*, and the forced condition is "every positive unit is a square mod 𝔮" —
consistent with the T1 (if some positive unit were a non-square mod a c₀-prime, −m²/4 would be in the orbit).
(c) ES^{(S)} over ℚ: Cl_{4∞}(ℚ) has order 2, c₀ = "r ≡ 3 (mod 4)", the orbit Q² lies in the squares, and every
condition is a congruence — the reason Theorem 2.4 is unconditional.
**Assessment 4.2 (sieve arithmetic; uses Murty–Petersen, Trans. AMS 365 (2013), Thm 0.2, as read in
sources/uo/LITERATURE.md).** An Artin-type sieve for a number-field variant must count degree-1 primes of K with a
non-norm Frobenius condition; then E ⊇ K and the known level is 1/η, η = max{[K:ℚ] − 2, 2}. The closing condition of
the Gupta–Murty argument is 2η < r + 1 with r ≤ [K:ℚ] − 1 the unit rank: for [K:ℚ] ≤ 4 it needs r ≥ 4 > [K:ℚ] − 1,
for [K:ℚ] ≥ 5 it needs 2[K:ℚ] − 4 < r + 1 ≤ [K:ℚ]. It never closes. Hypothesis responsible: the mute place is REAL,
which forces η < 0 there, so the orbit is a non-square coset ηU² and a non-norm quadratic character enters. Making the
mute place FINITE (§1) removes exactly this hypothesis.

*Galois case (R183 M2: Harper–Murty needs K/ℚ Galois, impossible for r₁ = 1).* The T1-bearing variants over Galois
fields with rank ≥ 4 are totally positive ES over totally real Galois K of odd degree d ≥ 5 (P = all real places,
|P| = d odd). There U_𝔪 = O_K^* and Prop 4.1 forces (u/𝔮) = sgn N(u) for every unit u: a Frobenius condition c in
N = Gal(K(√O_K^*)/K) ≅ (ℤ/2)^d. c is G-invariant (sgn N(u^σ) = sgn N(u)), hence central in Gal(K(√O_K^*)/ℚ), so it lies
in every maximal abelian subgroup; but the largest abelian subgroups have index ≥ d (N itself; N^G is small since
O_K^*/O_K^{*2} ≅ 𝔽₂ ⊕ (augmentation module)). Murty–Murty/Murty–Petersen then give η = d − 2 against the required
2η < r + 1 = d: fails for every d ≥ 5 (Assessment, same caveats as 4.2).
## 5. What can be proved for V_φ itself: power-saving almost-all, and an exact-T1 failure set under GRH

Notation of T1_TEMPLATE §1 (K = ℚ(√5), a_k = n + 4φ^{2k+1}). Call odd n > 1 *orbit-solved* if some a_k has a prime factor
𝔮 with (n/𝔮) = −1 (then V_φ(n) holds, T1_TEMPLATE Thm 1.3(b)). Let T = {m², 5m² : m odd} (the odd n that are squares
in O; 5 = (2φ − 1)²). By Thm 1.3(a) no n ∈ T is orbit-solved.

**Theorem 5.1 (unconditional, power saving; PROVED relative to the arithmetic large sieve and Chebotarev).**
#{odd n ≤ X : n not orbit-solved} ≪ X^{3/4} log²X. In particular V_φ(p) holds for all primes p ≤ X with ≪ X^{3/4}log²X
exceptions. (The exceptional set contains T, of size ≍ X^{1/2}.)
*Proof.* Let 𝔮 be a degree-1 prime, 𝔮 ∤ 10, ℓ = N𝔮, m = ord_𝔮(φ), C = φ⟨φ²⟩ ⊂ F_ℓ^*, and
S_ℓ = {n mod ℓ : −n/4 ∈ C, (n/ℓ) = −1}. If n mod ℓ ∈ S_ℓ then 𝔮 | a_k for some k and (n/𝔮) = (n/ℓ) = −1, so n is
orbit-solved. Call 𝔮 *good* if [ℓ ≡ 1 (4) and (φ/𝔮) = −1] or [ℓ ≡ 3 (4) and (φ/𝔮) = 1]. For good 𝔮 every element of C
qualifies (in the first case C consists of non-squares and (n/ℓ) = (−1/ℓ)(−n/4 /ℓ) = −1; in the second C consists of
squares and (−1/ℓ) = −1), so |S_ℓ| = |C| ≥ m/2. Good primes have density ½ among degree-1 primes (Chebotarev in
K(i, √φ), [K(i,√φ):K] = 4). Primes with m ≤ y divide ∏_{j ≤ y} N(φ^j − 1), whose logarithm is ≪ y², so there are ≪ y² of
them; with y = ℓ^{1/2}/log ℓ this is o(π(x)) in [x/2, x]. Hence a set 𝒫 of rational primes of positive lower density
has |S_ℓ| ≥ ℓ^{1/2}/(2 log ℓ) (choose one good 𝔮 above each). The arithmetic large sieve (Montgomery) gives, for any set
𝒩 ⊂ [1, X] avoiding S_ℓ mod every ℓ ∈ 𝒫, ℓ ≤ L: |𝒩| ≤ (X + L²)/J, J ≥ Σ_{ℓ ∈ 𝒫, ℓ ≤ L} |S_ℓ|/(ℓ − |S_ℓ|) ≫ L^{1/2}/log²L.
The non-orbit-solved odd n avoid all S_ℓ; take L = X^{1/2}. ∎
*Contrast with ES.* For ES the campaign proved that every CRT-admissible large-sieve bound saves at most
C(log N)^{3/4}(log log N)^{3/4} (DISCOVERIES (A)19–20; ES slices forbid boundedly many classes per prime). The unit orbit
forbids ≍ ord_𝔮(φ) ≥ ℓ^{1/2−o(1)} classes per prime, and the saving becomes a power. With |S_ℓ| ≍ ℓ (e.g. φ a primitive root
for a positive proportion of ℓ, known under GRH) the same sieve gives ≪ X^{1/2+o(1)}: the large-sieve barrier X^{1/2}
coincides with the size of the T1 set T. The squares *saturate* the large sieve.

**Theorem 5.2 (exact-T1 failure set; CONDITIONAL on GRH, same input and compatibility check as T1_TEMPLATE Thm 3.1).**
An odd n > 1 is orbit-solved iff n ∉ T.
*Proof.* "Only if": Thm 1.3(a). "If": as in T1_TEMPLATE Thm 3.1 with p replaced by n: a degree-1 𝔮 with ℓ ≡ 1 (4),
(n/ℓ) = −1 and φ a primitive root mod 𝔮 gives −n/(4φ) ∈ ⟨φ²⟩. Lenstra's theorem applies because K(√n) ≠ K (n ∉ T) and
K(√n) ⊄ K(i, √φ) (as in O183's check; K(√φ)/ℚ is not abelian). ∎
**EVIDENCE (`scripts/uo_phi_all.py 10000 6`).** Among all odd 3 ≤ n < 10⁴, exactly 71 are not orbit-solved with |k| ≤ 6,
and they are exactly the 71 elements of T below 10⁴.
*Remark (R183 m4).* For n with (n/5) = −1 (e.g. primes p ≡ ±2 mod 5) V_φ(n) is unconditional by a congruence:
(√5) | a_k for a suitable parity of k (φ ≡ 3 mod √5, and −4·3^{2k+1} runs through {2, 3} mod 5). The GRH/large-sieve
content of Theorems 5.1–5.2 is the case (n/5) = 1.

## 6. The ℤ-analogue question: what replaces the unit orbit over ℤ (S4)

**Proposition 6.1 (ES-integrality of an orbit shot is a growing-modulus condition; PROVED).** In Prop 2.1 (any g | a
with g ≡ −1 (mod 4), g > 0, in place of the prime r), the solution has z ∈ ℤ — i.e. is an ES solution — iff
**g ≡ −1 (mod 4Q)**.
*Proof.* For q | Q with c = v_q(Q), s = v_q(g + 1): if s < 2c then v_q(x) = s (from 4gx = n(g + 1) + 4Q²) and
v_q(z) = 2s − 2c, which is ≥ 0 iff s ≥ c; if s ≥ 2c, v_q(z) ≥ 0. So z ∈ ℤ iff v_q(g + 1) ≥ v_q(Q) for all q | Q. ∎
*Check (`scripts/uo_zint.py 3000 400 3 5 7 11`):* on all 51 558 shots (every n < 3000 coprime to 2·3·5·7·11, Q ≤ 400,
every divisor g ≡ 3 (mod 4) of n + 4Q²), z ∈ ℤ in 3100 cases, and "g ≡ −1 (mod 4Q)" agrees in all 51 558.

**Theorem 6.2 (the three ways to an infinite orbit over ℚ; PROVED, scope: the unit-Type-II recipe x = (n+e)/4,
y' = (x+D)/e, z' = x(x+D)/(eD) with D in a multiplicative orbit).**
(i) Over ℤ the orbit is {1} (units ±1, positivity): one shot, n + 4. Allowing D ∈ ℤ_{>0} arbitrary turns the shot
condition into "n + 4D has a divisor g ≡ −1 (mod 4·(D-part))" — for D = Q², exactly Prop 6.1, i.e. B2's "divisor in a
residue class whose modulus is part of the solution"; the expected number of successful shots Σ_Q τ(n+4Q²)/φ(4Q) is the
usual polylog lottery (B3).
(ii) Over ℤ[1/S] with no normalisation the orbit is infinite with fixed modulus 4, but the T1 dies: inv_q is free
(Lemma 1.1 (i), w odd) and Type II solutions at squares exist (§2 example; control run of `uo_mute_t1.py`).
(iii) Over ℤ[1/S] with the parity normalisation (ES^{(S)}) the orbit is infinite ({Q²}), the modulus is fixed (4), the
T1 holds (Cor 1.2), and existence at all non-squares is a theorem (Thm 2.4). ES sits inside as the sub-condition
g ≡ −1 (mod 4Q).
So the precise ℤ-analogue of a mute place is a **finite prime muted by a parity normalisation**. It exists and
behaves better than the real mute place of V_φ (no Kummer obstruction, §4). It is **not an opening for ES itself**
(Assessment): passing from ES^{(S)} back to ES is exactly the growing-modulus condition of Prop 6.1, which is B2.
What the construction isolates is that B2's growing modulus, and nothing else, separates ES from a T1-bearing equation
that is provably solvable at every prime: **ES = ES^{(S)} + "g ≡ −1 (mod 4Q)"**.
