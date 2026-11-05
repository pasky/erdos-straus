# Z59_MSPF — tryhard lane MSPF (wave z59): the pointwise statement for 4uBC − u − B = n

Status line: **FINISHED (time-boxed) — NOT A HOT LEAD.** Target not proved in any range. Contents: equivalent
reformulations, the Jacobi obstruction, necessary conditions on any witness (χ_n(d) = −1, d ≥ q₁(n), R(n) even, no
bounded-modulus proof), a record of the routes tried and where each stops, and certified numerics to 10⁷. Hostile
review applied (see commit log).

Problem (verbatim target). For every sufficiently large non-square n with n mod 840 ∈ 𝔐 = {1, 121, 169, 289, 361, 529}
(n ≡ 1 (24), n a nonzero square mod 5 and mod 7), the equation 4uBC − u − B = n has a solution in positive integers.
Equivalently: some d ≡ 3 (mod 4), d ≥ 3, has k := (−n mod d) dividing (d+1)/4.

## §0 Mandatory falsifiers (stated up front; re-stated in §9 at the end)

Any argument for the target must be run through all four of the following. Where this memo proves something, the
relevant falsifier is answered explicitly next to the proof; where it does not, the memo says so.

* **(F1) Odd squares.** R(m²) = 0 for every odd m (CERTIFIED in data/z58/screens/README.md; re-proved below as Lemma 1.3:
  for every admissible pair (d, k), −k is a Jacobi non-residue mod d). Consequence (Lemma 1.4): *no* argument that uses
  only congruence information about n (n mod M for any fixed M, or any finite set of residue conditions) can prove the
  target on a class containing squares, because odd squares occupy every residue class in 𝔐 that the target concerns.
  A correct proof must use some global property of n that distinguishes it from m²; the one made visible by the
  structure here (Lemma 1.5) is that the Jacobi character χ_n(·) = (·/n) is non-principal (it is principal iff n is a
  square), but other global properties (e.g. the factorisation of n + k) are also non-congruential and are not
  excluded. Any proof must identify the step that fails at n = m².
* **(F2) C even alone.** The C-even part of the family (4uBC − u − B = n with C even ⇔ 8uB | n + u + B ⇔ d ≡ −1
  (mod 8u), see §1) fails at 4 primes in 𝔐 ∩ [10¹⁰, 1.1·10¹⁰] (data/z58/screens/r8_zeros_1e10.txt, those with
  p mod 840 ∈ 𝔐; recomputed in §4). So an argument that only ever produces even C must exclude those primes by its
  threshold or hypotheses; the memo must say which parity of C a construction produces.
* **(F3) Non-square zeros.** Inside 𝔐 the known non-square zeros are the 15 composites ≤ 7 999 801 of
  data/z58/screens/composite_zeros_le8e6.txt that lie in 𝔐, the three composites 8 725 201, 12 538 801, 17 401 609, and
  the nine primes of F4 (all recomputed here, §4); the lane brief states, with Z58_LADDER.md as the certified source,
  that there is no non-square zero in 𝔐 ∩ (17 401 609, 10¹¹] — this memo does not recompute that census. Outside 𝔐
  the data contain 270 composite zeros ≤ 7 999 801 (many with 3 | n, 5 | n or 7 | n) and the five (★)-prime zeros
  409, 577, 23 929, 329 617, 1 134 241; the memo makes no claim about whether outside-𝔐 zeros are infinite (no such
  theorem is available here) and therefore draws no inference about whether an eventual proof must use membership
  in 𝔐. What is required of any proof: (a) an explicit threshold n₀ > 17 401 609 (or an explanation why none can be
  given), and (b) a statement of exactly where, if anywhere, n ≡ 1 (24), (n/5) = (n/7) = 1 is used. For n with 3 | n,
  5 | n or 7 | n every modulus d divisible by 3, 5, 7 is unavailable (Lemma 1.5: gcd(d, n) = 1), which removes the
  small-modulus witnesses but does not by itself explain any particular zero (n = 21 has the witness d = 11).
* **(F4) The prime screens.** The 14 (★)-zeros of data/z58/screens/star_prime_zeros.txt (R(p) = 0; nine in 𝔐:
  5569, 9601, 83449, 102001, 712321, 1724209, 1726201, 5212561, 8813281) and the 38 𝔊*-zeros of gstar_zeros.txt
  (zeros of a *subfamily*; 20 in 𝔐, of which 11 have R(p) > 0 for the full family — §4). Any construction (choice of
  d, k as functions of n) must be evaluated at the nine in-𝔐 full-family zeros; it must fail there, and the memo
  must say which hypothesis (size, a "sufficiently large" threshold, or a structural hypothesis) excludes them.

Surviving all four honestly = hot lead, to be flagged in the title and committed at once.

## §1 Reformulations and the obstruction (all PROVED; numerically checked, §5)

Notation. ℕ = {1, 2, …}. R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}. (·/·) is the Jacobi symbol. For n ≡ 1 (4) put
χ_n(d) := (d/n) (Jacobi symbol with lower entry n; a real Dirichlet character mod n, principal iff n is a perfect square).

**Lemma 1.1 (four equivalent descriptions).** For n ∈ ℕ the following four finite sets are in explicit bijection:
(a) triples (u, B, C) ∈ ℕ³ with 4uBC − u − B = n;
(b) pairs (k, B) ∈ ℕ² with 4kB | n + k + B;
(c) moduli d ≡ 3 (mod 4) with d ∤ n and k := (−n mod d) ∈ [1, d−1] dividing (d+1)/4;
(d) pairs (C, x) ∈ ℕ² with x | 4Cn + 1 and x ≡ −1 (mod 4C).
In (c) the triple is (u, B, C) = (k, (n+k)/d, (d+1)/(4k)); in (d) it is x = 4uC − 1 and (4Cn+1)/x = 4BC − 1.

*Proof.* (a)⇔(b): 4uBC − u − B = n ⇔ 4uB · C = n + u + B with C ∈ ℕ (k = u). (a)⇒(c): put d := 4uC − 1 ≡ 3 (4). Then
dB = 4uBC − B = n + u, so d | n + u; as 1 ≤ u ≤ (d+1)/4 < d, u is the least positive residue of −n mod d (in particular
d ∤ n), and u | (d+1)/4 = uC. (c)⇒(a): u := k, C := (d+1)/(4k) ∈ ℕ, B := (n+k)/d ∈ ℕ; then 4uBC − u − B = (d+1)B − u − B
= dB − u = n. The two maps are mutually inverse (d = 4uC − 1 is recovered). (a)⇒(d): x := 4uC − 1, y := 4BC − 1:
xy = 16uBC² − 4uC − 4BC + 1 = 4C(4uBC − u − B) + 1 = 4Cn + 1, and x ≡ −1 (4C). (d)⇒(a): x ≡ −1 (4C) and x > 0 give
x = 4uC − 1 with u ≥ 1; y := (4Cn+1)/x satisfies xy ≡ 1 (4C) hence y ≡ −1 (4C), y = 4BC − 1, B ≥ 1 (y > 0); expanding,
n = 4uBC − u − B. Inverse maps again. ∎

So R(n) = #{d ≡ 3 (4) : (−n mod d) | (d+1)/4} = #{(k,B) ∈ ℕ² : 4kB | n+k+B}, and the C-even sub-count is
#{d : d ≡ −1 (mod 8k)}; C odd ⇔ d ≡ 4k − 1 (mod 8k).

**Lemma 1.2 (sizes).** In every solution, 2kB ≤ n, so min(k, B) ≤ √(n/2); also 4k − 1 ≤ d ≤ n + k and k, B ≤ (n+1)/3.
*Proof.* n = 4kBC − k − B ≥ 4kB − k − B = 2kB + ((2k−1)(2B−1) − 1)/2 ≥ 2kB. d = (n+k)/B ≤ n + k and d = 4kC − 1 ≥ 4k − 1.
From k ≤ (d+1)/4 ≤ (n+k+1)/4 we get 3k ≤ n + 1; symmetric in B. ∎

**Lemma 1.3 (every admissible class is a Jacobi non-residue).** If d ≡ 3 (mod 4), k ≥ 1 and 4k | d + 1, then
(−k/d) = −1.
*Proof.* Write k = 2^a k′, k′ odd. Since 4k | d + 1, gcd(k, d) = 1, d ≡ −1 (mod k′), and if a ≥ 1 then d ≡ −1 (mod 8).
(−1/d) = −1 because d ≡ 3 (4). If a ≥ 1, (2/d) = 1 because d ≡ 7 (8). For the odd part, Jacobi reciprocity gives
(k′/d)(d/k′) = (−1)^{((k′−1)/2)((d−1)/2)} = (−1)^{(k′−1)/2} (as (d−1)/2 is odd), while (d/k′) = (−1/k′) = (−1)^{(k′−1)/2}
(as d ≡ −1 mod k′). Hence (k′/d) = 1 and (−k/d) = (−1/d)(2/d)^a(k′/d) = −1. ∎

**Corollary 1.4 (F1, squares).** R(m²) = 0 for every m ∈ ℕ.
*Proof.* Let d be as in 1.1(c) for n = m². Then −k ≡ m² (mod d) and gcd(k, d) = 1, so gcd(m, d) = 1 and
(−k/d) = (m/d)² = 1, contradicting Lemma 1.3. ∎

**Lemma 1.5 (every hit modulus is a χ_n-non-residue).** Let n ≡ 1 (mod 4) and let d be a hit modulus for n
(1.1(c)). Then gcd(d, n) = 1 and χ_n(d) = (d/n) = −1. Consequently d is divisible by some prime q with χ_n(q) = −1,
so d ≥ q₁(n) := min{q prime : (q/n) = −1} (defined for non-square n; for squares no such prime exists, consistent
with Cor. 1.4); for non-square n ∈ 𝔐 one has q₁(n) ≥ 11.
*Proof.* n ≡ −k (d) and gcd(k, d) = 1 give gcd(n, d) = 1. (n/d) = (−k/d) = −1 by 1.3; Jacobi reciprocity for the
coprime odd positive pair (n, d) with n ≡ 1 (4) gives (d/n) = (n/d) = −1. χ_n is completely multiplicative, so some
prime factor q of d has χ_n(q) = −1. For n ∈ 𝔐: n ≡ 1 (8) gives (2/n) = 1; for q ∈ {3, 5, 7}, (q/n) = (n/q) = 1 by
reciprocity (n ≡ 1 (4)) and the definition of 𝔐. ∎

*Remark (where non-squareness lives).* χ_n is principal exactly when n is a square, and then Lemma 1.5 says no hit
modulus exists — this is a second proof of 1.4 for odd squares (Lemma 1.5 assumes n ≡ 1 (4)). Conversely, for a
non-square n ≡ 1 (4), χ_n is a non-principal real character mod n; it is induced by the primitive character of
conductor f(n) := ∏_{p : v_p(n) odd} p (the squarefree part of n, ≡ 1 (4)), and additionally vanishes at the primes
dividing n/f(n). (Caution: "χ_n(d) = −1" is not the same as "d is a non-square residue mod n": e.g. 11 mod 121 is not
a square but χ_{121}(11) = 0.) The set S(n) := {d ≡ 3 (4) : (−n mod d) | (d+1)/4} satisfies S(n) ⊂ {χ_n = −1}
automatically (1.5), so saying "S(n) meets {χ_n = −1}" is just S(n) ≠ ∅ — no progress; what Lemma 1.5 adds is only
the *necessary* shape of any witness: d must contain an odd number (with multiplicity) of prime factors from
{q : (q/n) = −1}. Non-principality of χ_n is one available encoding of non-squareness; a proof may of course use
non-squareness through other data (factorisations of n + k, n = a² + r, …).

**Lemma 1.6 (Jacobi signs of the two cofactors).** Let n ≡ 1 (4) and (k, B) a solution with gcd(kB, n) = 1 (automatic
for prime n, since k, B ≤ (n+1)/3 < n). Then (B/n) = −(k/n).
*Proof.* dB = n + k ≡ k (mod n) ⇒ (d/n)(B/n) = (k/n), and (d/n) = −1. ∎

**Lemma 1.7 (R(n) is even for odd n).** For odd n the swap (k, B) ↦ (B, k) is a fixed-point-free involution of the
solution set of 1.1(b); hence R(n) ≡ 0 (mod 2), and the target is equivalent to R(n) ≥ 2.
*Proof.* The condition 4kB | n + k + B is symmetric. A fixed point k = B has 4k² | n + 2k, so k | n and
n/k + 2 ≡ 0 (mod 4k); the latter forces n/k even, impossible for odd n. ∎
(Checked: R(p) is even for all 20 513 primes p ∈ 𝔐, p ≤ 10⁷, and for the 12 primes of r8_zeros_1e10.txt.)

**Lemma 1.8 (no congruence proof; moduli ≥ D are unavoidable).** Let D ≥ 1, L := lcm(1, …, D). If n ≡ m² (mod L)
for some m with gcd(m, L) = 1, then every hit modulus d of n satisfies d > D. Such n exist in every class of 𝔐: pick
m ∈ [1, 840L] with m ≡ m₀ (mod 840), m₀ ∈ {1, 11, 13, 17, 19, 23} the root of the prescribed class, and m ≡ 1 (mod qᵉ)
for every prime power qᵉ ∥ L with q ≥ 11 (CRT, the moduli are coprime); then gcd(m, L) = 1 (m is coprime to 2, 3, 5, 7
because m₀ is), and every n = m² + 840L·t (t ≥ 1) satisfies n ≡ m² (mod L) and n ≡ m₀² (mod 840). Up to X there are ≥ X/(840L) − 1 − (840L)²/(840L)
of them (m² ≤ (840L)²), and at most √X of them are squares; so for L ≤ X^{1/2−ε} and X large, non-square ones exist
(and their number → ∞ with X).
*Proof of the first sentence.* If d ≤ D then d | L, so with k := (−n mod d) we get −k ≡ n ≡ m² (mod d), and
gcd(m, d) = 1, so (−k/d) = (m/d)² = 1, contradicting Lemma 1.3 (exactly as in Cor. 1.4). ∎
Consequence (precise scope). (i) A *bounded witness menu* fails: for every D, infinitely many non-square n in every
class of 𝔐 have no witness d ≤ D. (ii) A *fixed-modulus witness selector* fails: any rule that assigns to n a witness
d(n) ≤ D depending only on n mod M (for fixed M, D) fails on every n of (i). (iii) A *class-wide identity* (a witness valid for all n ≡ r (mod M)) exists only if the class
r contains no square (Cor. 1.4). Since L = lcm(1..D) = e^{(1+o(1))D}, one may take D = (1/2 − ε)·log X and still
find the non-square n ≤ X of (i) in every class, so for infinitely many n in every class every witness exceeds
(1/2 − ε)·log n. Nothing more is claimed: a proof combining congruence information with a global non-square
hypothesis is not excluded by this lemma.

## §2 What a proof must deliver (consequence of §1)

For every large non-square n ∈ 𝔐 one needs an explicit d ≡ 3 (4) with (i) χ_n(d) = −1 and (ii) (−n mod d) | (d+1)/4.
By 1.8, for infinitely many n in every class every witness has d > (1/2 − ε)·log n, i.e. the
witness cannot be read off from n modulo any bounded modulus; by 1.5 it cannot be read off from n modulo any set of
moduli on which χ_n looks principal. Any construction d = d(n) therefore has to use some non-congruential datum of n,
for instance: a prime q with (q/n) = −1 (least such: q₁(n); viewing χ_n as a non-principal character mod the
squarefree modulus rad(n) ≤ n, the least integer with χ_n ∉ {0, 1} is ≪_ε n^{1/(4√e)+ε} by the Burgess-type theorem
for cubefree moduli (Lau–Wu, *On the least quadratic non-residue*, Thm 1), and it is prime by multiplicativity, so
q₁(n) ≪_ε n^{1/(4√e)+ε}; under GRH q₁(n) ≪ log² n; no smaller uniform power exponent is claimed or used here), or
the factorisation of n + k for small k, or the near-square structure n = a² + r.
§3 records what each of these gives and where each stops.

## §3 Attack routes tried, and the exact point where each stops (analysis; nothing here is a proof of the target)

Every route below is a way to produce, for a given non-square n ∈ 𝔐, a witness d (equivalently (k, B) with
4kB | n + k + B, or C with a divisor of 4Cn + 1 in the class −1 mod 4C). The four descriptions of Lemma 1.1 are used
interchangeably; the one that makes the difficulty visible is (b)/(c): **the target says that one of the consecutive
integers n + 1, n + 2, n + 3, … has a divisor in the residue class −1 (mod 4k), where k is the shift**. Lemma 1.3 says
this class is a non-residue class for the character (−k/·), and the squares n = m² (where m² + k ≡ m² + k·1² is
represented by the principal form of discriminant −4k, so all its divisors coprime to 2k are (−k/·)-residues) show that
the shifting class makes the usual "one of four consecutive integers is ≡ 3 (mod 4)" trick unavailable.

**3.1 Polynomial (Mordell-type) identities.** Any identity n ↦ (k(n), B(n), C(n)) valid on a residue class r (mod M)
would produce a witness for the squares in that class, so by Cor. 1.4 it exists only for classes r containing no
square, i.e. r a non-square mod M. All six
classes of 𝔐 are square classes mod 840, and any refinement by a further modulus M′ leaves square sub-classes
(n ≡ m² mod M′ with m coprime to M′) uncovered. So identities can at best peel off non-residue sub-classes
(e.g. n ≡ 8, 10 (mod 11) by d = 11, k ∈ {1, 3}; n ≡ 41, 48, 53, 54 (mod 55) by d = 55, k ∈ {14, 7, 2, 1}), never finish.
*Stops at:* Lemma 1.8 — for every D there are non-square n ∈ 𝔐 (in every class) all of whose witnesses exceed D.

**3.2 Near-square structure.** n non-square ⇒ n = a² + r, 1 ≤ r ≤ 2a (a = ⌊√n⌋). Choosing the shift to make n + k a
square ((a+j)², k = 2aj + j² − r) or a product (n + k = a(a+t) with k = at − r) turns the target into "the divisors of
(a+j)² or of a(a+t) contain one ≡ −1 (mod 4k)". Each explicit choice of which divisor (d = a, a + 1, a + t, e²f, …)
produces a two- or three-parameter polynomial family, e.g. n = a(a+1) − k with a ≡ 3 (4), k | (a+1)/4 (witness d = a),
or n = (4st − 1)² − s (witness d = 4st − 1, k = s). These are correct (checked numerically) but cover O(√X·log X) integers
≤ X. *Stops at:* a thin family; to go further one needs a divisor of (a+j)² in a prescribed class, i.e. the
factorisation of a + j — uncontrolled.

**3.3 The least non-residue.** By Lemma 1.5 every witness d has χ_n(d) = −1, hence d ≥ q₁(n), and d is a product
q·t with χ_n(q) = −1 for some prime q | d. Taking d = q itself requires (−n mod q) | (q+1)/4 — a condition on the
residue of n modulo q that we cannot steer (q is given by n). Taking d = q·t: the condition becomes
(n + k)/q has a divisor t ≡ −q⁻¹ (mod 4k), again a "divisor in a class" condition on a shifted number. The freedom
k ≡ −n (mod q) does not help pointwise. *Stops at:* the same divisor-in-class problem one level down. (Numerically
d_min = q₁(n) for 22.6 % of the primes p ∈ 𝔐 ≤ 10⁷ and d_min ≤ 10·q₁ for 85 %; max q₁ = 53, max d_min = 64 255.)

**3.4 Prime witnesses only.** One might hope to use primes q ≡ −1 (mod 4k) dividing n + k (Linnik/Bombieri–Vinogradov
territory). But witnesses with d prime are *not* enough in the tested range: 136 primes p ∈ 𝔐 ≤ 10⁷ (the largest
9 831 889) have R(p) > 0 but no prime witness, decaying slowly (53 of 2365 in (0, 10⁶], 5–13 per million above
3·10⁶, 11 in the last million; §4). So a prime-witness
theorem would need a threshold beyond those, and the composite (Jacobi, not Legendre) structure of Lemma 1.3 looks
essential; in any case I know no method that produces a prime in a progression dividing a *specific* number n + k.

**3.5 Parity / involution arguments (Zagier-style).** The only natural involution, (k, B) ↦ (B, k), is fixed-point
free for odd n (Lemma 1.7), so it gives R(n) ≡ 0 (mod 2) — the wrong parity for an existence proof, and R(p) = 0 does
occur. Companion counts: with d′ ≡ +1 (mod 4k) instead of −1 (i.e. n = 4kBC + k + B, or 4Cn + 1 = xy with
x ≡ y ≡ 1 (4C)), the analogue of Lemma 1.6 gives (B/n) = +(k/n): so solutions of n = 4kBC + k + B pair k, B of
*equal* χ_n-sign and those of the target pair *opposite* signs. The relaxed equation n = 2bkB − k − B (b of either
parity; b = 2C recovers the target) is trivially solvable (b = 1, k = 1, B = n + 1), and in SL₂(ℤ)-language the target is
#{M = [[x, b],[2n, y]] ∈ Γ(2) : x, y, b > 0, 2b | x + 1} ≥ 1 versus the trivial count in Γ₀(2). I found no involution or
group action on these matrices that moves odd b to even b while preserving the divisibility 2b | x + 1
(right-multiplication by [[1, t],[0, 1]] preserves the lower-left entry but destroys the divisibility unless t = 0).
*Stops at:* no sign-changing structure was found; the squares show R can be 0 with everything else in place.

**3.6 Fixed small C (genus conditions).** For C ∈ {1, 2, 3, 6}, (ℤ/4C)* is an elementary 2-group and
"x ≡ −1 (mod 4C)" is a pure quadratic-residue condition: C = 1: 4n + 1 has a divisor with (−1/x) = −1; C = 2: 8n + 1
has x with (−1/x) = (−2/x) = −1; C = 3: 12n + 1 has x with (−1/x) = (−3/x) = −1; C = 6: 24n + 1 has x ≡ 23 (24).
For n ∈ 𝔐 there are forced small factors (3 | 8n + 1 always; 5 | 24n + 1 when n ≡ 1 (5); 7 | 12n + 1 when n ≡ 4 (7);
4n + 1 always has a prime factor ≡ 2 (mod 3) since 4n + 1 ≡ 2 (3)), but they only reduce the condition to a
residue condition on the *cofactor's* prime factors. *Stops at:* same problem for the cofactor. (The 4n + 1 remark gives
the only unconditional pointwise fact of this kind I found: **if the prime factor q ≡ 2 (mod 3) of 4n + 1 guaranteed above
happens to be ≡ 3 (mod 4), then C = 1 works**; this is not steerable.)

**3.7 The analytic side (HEURISTIC analysis throughout; nothing here is proved).** R(n) is the number of
representations of n by the trilinear form 4kBC − k − B, or equivalently R(n) = Σ_{N = n+1}^{⌊4n/3⌋+1}
#{d | N : d ≡ −1 (mod 4(N − n))} — a sum over an interval of N, but with the residue class tied to N − n and the
modulus 4(N − n) as large as N for most N. A naive "singular series" model, Σ_d τ((d+1)/4)/d · (local densities)
≍ log² n, is wrong pointwise: at n = m² the truth is 0 (Cor. 1.4). Lemma 1.5 restricts the support of every term to
d with χ_n(d) = −1, so any model must carry the global factor [χ_n(d) = −1] = (χ_n(d)² − χ_n(d))/2 (which is 0 when
gcd(d, n) > 1 and at every d when n is a square); writing
  M_χ(n) := Σ_{d ≤ 4n/3, d ≡ 3 (4), gcd(d,n)=1} ((1 − χ_n(d))/2)·τ((d+1)/4)/d · (local densities at the primes dividing
  4k, left unspecified)
is only a *model*, not a theorem. (Heuristic remark: for non-square n the χ_n-part of such a model is
Σ_{d ≤ Y} χ_n(d)τ((d+1)/4)/d. *If* one assumes cancellation in the weighted sums Σ_{d ~ Y} χ_n(d)τ((d+1)/4) for
Y ≥ n^{1/4+ε} — a weighted Burgess-type hypothesis which is NOT known (the divisor weight can correlate with χ_n:
τ((d+1)/4) = #{(a,b): 4ab − 1 = d}, and Σ_{a,b mod p} χ_p(4ab − 1) = p·χ_p(−1) = p ≠ 0 for p ≡ 1 (4), the a = 0 row) — then, since the harmonic
weight gives the range d ≤ n^{1/4} the share (1/4)² = 1/16 of the log²n mass, the χ_n-correction could cancel at most
about 1/16 of the model's main term. This is a conditional statement about the model only.) What would have to be proved is R(n) − M_χ(n) = o(log² n) *for the individual n*, i.e. equidistribution of the
single residue n mod d over d ≤ 4n/3 in the thin target set −Div((d+1)/4) with divisor weights. The k-slices of this
error, #{d | n + k : d ≡ −1 (4k)} − (mean), are each of the size of their mean on a set of n of relative density
≍ (log n)^{−1/2} (e.g. k = 1: (n+1)/2 free of primes ≡ 3 (4)), so the pointwise bound is a large-deviation statement
about the divisors of the shifted integers n + k. Averaging over n (circle method over n, or Bombieri–Vinogradov-type
level-of-distribution results, which average over moduli for sums over the integers in a range) gives mean-value
information; I do not see how to convert it into a bound for the single n, and the squares show the error is as large
as the naive main term on a (sparse) set. *Stops at:* pointwise control of the residues of one n modulo all d, or of
the divisors of n + k in moving classes — the same wall as every other route, seen from the analytic side.

**Summary.** All routes reduce to the single statement "some n + k has a divisor ≡ −1 (mod 4k)", a pointwise
assertion about the multiplicative structure of a specific integer in a residue class that moves with k. Lemma 1.8
shows the moduli involved exceed (1/2 − ε)·log n for infinitely many n in every class; 3.4 shows prime moduli do not
suffice up to 10⁷;
3.1–3.2 show every construction I found is either a congruence class (which cannot cover 𝔐, by 1.8) or a thin
polynomial family. I could not find a mechanism that uses the non-principality
of χ_n *pointwise* other than through the factorisation of n + k, which is the open problem.

## §4 Numerical record (data/z59/mspf/, engines scripts/z59_mspf_hits.c and z59_mspf_single.c; all CERTIFIED by
recomputation, cross-checked against a brute-force enumeration of (u, B, C) for n ≤ 3000 and against data/z58/screens)

* `zeros_all_2e5.txt`: all n ≡ 1 (4), n ≤ 2·10⁵ with R(n) = 0 (348, of which 224 squares and 124 non-squares; squares
  carry the sentinel q₁ = 0); the non-square entries coincide with the z58 lists (57, 105, 177, …, 409, 577, …).
* `primes_M_1e7.txt`: the 20 513 primes p ∈ 𝔐, p ≤ 10⁷, with R, R_odd (C odd), R_even (C even), d_min, k at d_min,
  q₁(p), whether d_min is prime, R_prime (witnesses with d prime), k_min (least k over all witnesses). Facts:
  the zeros are exactly the nine of F4; R(p) is even throughout (Lemma 1.7). Among the 20 504 primes with R(p) > 0:
  d_min ≥ q₁(p) throughout (Lemma 1.5), d_min = q₁(p) in 22.6 %; R_even = 0 for 186 (largest 9 965 881) and R_odd = 0
  for 118 (largest 9 744 001), so neither parity of C suffices alone up to 10⁷ (F2); R_prime = 0 for 136 (largest
  9 831 889); per million these counts decay from (91, 60, 53) in (0, 10⁶] to ≤ 11 above 5·10⁶ but have not
  reached 0 ((10, 6, 8) in (8·10⁶, 9·10⁶], (9, 4, 11) in (9·10⁶, 10⁷]); k_min ≤ 10 for 98.1 % but reaches 410 (p = 4 160 641); mean R ≈ 30 in
  (5·10⁶, 10⁷]. (The nine zero rows carry d_min = 0, q₁ as computed, R_prime = k_min = 0.) Reproduce:
  `gcc -O2 -o hits scripts/z59_mspf_hits.c -lm && ./hits 10000000 1` (≈ 1 min, ≈ 60 MB).
* `zeros_profile.txt`: for each of the nine prime zeros and k ≤ 8, the factorisation of p + k and the residues of its
  prime factors mod 4k, with the check that no sub-multiset product is −1 mod 4k (F4, concrete).
* Single-n engine at 10¹⁰: for the 12 primes of r8_zeros_1e10.txt the values R and R_even (= R₈) agree with the
  certified file (e.g. 10 532 106 649: R = 12, R_even = 0, d_min = 1559 at k = 30); four of the twelve lie in 𝔐
  (10 301 993 881, 10 529 331 121, 10 532 106 649, 10 868 474 401) — the C-even failures of F2.
* **Screens (added after cross-model review).** `zeros_all_8e6.txt` (engine mode 2 to 8·10⁶): the composite zeros
  n ≡ 1 (4), n ≤ 7 999 801 are exactly the 285 of composite_zeros_le8e6.txt, 15 of them in 𝔐 and 270 outside; the
  three further in-𝔐 composites 8 725 201, 12 538 801, 17 401 609 have R = 0 (single-n engine).
  `star_recomputed.txt`: all 14 primes of star_prime_zeros.txt have R = 0 (nine in 𝔐, five outside: 409, 577, 23 929,
  329 617, 1 134 241). `gstar_recomputed.txt`: of the 38 primes of gstar_zeros.txt (zeros of the 𝔊* *subfamily*),
  exactly the 14 (★)-primes have R = 0; the other 24 have R > 0. Of the 20 in 𝔐, 11 have R > 0 for the full family
  (e.g. 23 041: R = 2; 564 661 441: R = 2, both C odd, d_min = 2 741 075 at k = 9) — these are subfamily failures, not
  full-family zeros, and the lemmas of §1 hold at all of them without forcing existence.
## §5 Numerical checks of the lemmas (CERTIFIED, small ranges)

* Lemma 1.1: R(n) computed as #{(u,B,C)} by brute force equals #{d ≡ 3 (4) : (−n mod d) | (d+1)/4} for all n ≡ 1 (4),
  n < 3000 (scripts/z59_mspf_bruteforce.py; 0 mismatches), and the k ≤ √(n/2) + symmetry engine reproduces the
  z58 zero lists and the certified (R, R₈) values at 10¹⁰.
* Lemma 1.3 (scripts/z59_mspf_lemmacheck.py): all 7069 admissible pairs (d, k) with d < 4000 have (−k/d) = −1.
* Lemma 1.6: all 1998 solutions (k, B) for primes p ≡ 1 (4), p < 3000, have (B/p) = −(k/p).
* Lemma 1.7: R(p) even for all 20 513 primes p ∈ 𝔐 ≤ 10⁷ and for the 12 primes at 10¹⁰.
* Lemma 1.5: d_min ≥ q₁(p) for all 20 504 primes p ∈ 𝔐 ≤ 10⁷ with R(p) > 0 (0 violations).
* §3.2 families: n = a(a+1) − k (a ≡ 3 (4), k | (a+1)/4; witness d = a) and n = (4st−1)² − s (witness d = 4st − 1, k = s)
  verified for a < 400 and s, t < 40 (0 failures). §3.1 classes: d = 11 covers n ≡ 8, 10 (11); d = 55 covers
  n ≡ 41, 48, 53, 54 (55).

## §9 Falsifiers, re-stated against what this memo actually contains

The memo proves **no part of the target**. What it proves is a set of structural constraints (§1) that any proof must
satisfy, and it documents why each route I tried stops (§3). Running the four falsifiers against the *lemmas*:

* **(F1) Odd squares.** Lemma 1.3 + Cor. 1.4 prove R(m²) = 0 for *all* m. One available encoding of the
  non-squareness of n is the non-principality of χ_n (Lemma 1.5: every witness has χ_n(d) = −1); no step of this memo
  claims to exploit it (or any other encoding) to produce a witness, and §3.7 explains why the natural analytic
  main-term *model* must carry the support factor [χ_n(d) = −1].
  The "4n + 1 has a prime factor ≡ 2 (mod 3)" observation (§3.6) is congruential and correctly gives nothing at
  squares: at n = m², 4m² + 1 has all odd prime factors ≡ 1 (mod 4), so that prime factor is ≡ 5 (mod 12) — consistent.
* **(F2) C even alone.** C even ⇔ d ≡ −1 (mod 8k) (Lemma 1.1). The memo contains no general construction, so there
  is nothing that produces only even C; the special families of §3.2 have C = (a+1)/(4k) (n = a(a+1) − k) and C = t (the
  (4st − 1)² − s family), so both parities occur. The data (§4) show both R_even = 0 and R_odd = 0 occur for primes in 𝔐 up to
  10⁷ and R_even = 0 at four primes in 𝔐 near 10¹⁰ (recomputed), so a single-parity argument must exclude those by its
  threshold or hypotheses.
* **(F3) Non-square zeros / outside 𝔐.** No threshold is produced because no proof is produced. Nothing in the memo
  uses membership in 𝔐 except the bound q₁(n) ≥ 11 (Lemma 1.5), which is not used for anything further. What the
  lemmas say about n ∉ 𝔐 is only this: gcd(d, n) = 1 is forced (Lemma 1.5), so for 3 | n (5 | n, 7 | n) every modulus
  divisible by 3 (5, 7) is unavailable; this removes the small witnesses d = 3, 7, 15, 35, 63, … but does not by itself
  produce or explain any zero (n = 21 has the witness d = 11), and zeros outside 𝔐 also occur at n coprime to 840
  (409 ≡ 3 (mod 7), 577 ≡ 2 (mod 5)) in classes that the small-d identities do not cover. Screen counts: 285
  composite zeros ≤ 7 999 801 (15 in 𝔐), three more in-𝔐 composites up to 17 401 609, 14 (★)-primes (9 in 𝔐) — all
  recomputed (§4). The statement "no non-square zero in 𝔐 ∩ (17 401 609, 10¹¹]" is prior certified work
  (Z58_LADDER.md, via the lane brief), not recomputed here; whether zeros outside 𝔐 are infinite is not known to
  this memo and nothing is inferred from it. Finite outside-𝔐 zeros do not exclude an eventual theorem on a larger
  domain with a higher threshold.
* **(F4) The prime screens.** All 14 (★)-zeros have R = 0 (nine in 𝔐, reproduced as exactly the zeros among the
  20 513 primes in 𝔐 up to 10⁷); of the 38 𝔊*-zeros, 14 are full-family zeros and 24 have R > 0 (11 of the 20 in 𝔐),
  i.e. 𝔊*-zeros are subfamily failures (§4). `zeros_profile.txt` exhibits for each of them and k ≤ 8 that no product of a sub-multiset of the prime
  factors of p + k (respecting multiplicities) is ≡ −1 (mod 4k). (The *group* generated by the residues can contain
  −1: p = 5569, k = 8, p + k = 3·11·13², and 3·13³ ≡ −1 (mod 32) needs a third factor 13 that is not there.) The
  memo contains no general construction to evaluate at them; the special families of §3.2 do not contain them
  (they are not of the form a(a+1) − k with k | (a+1)/4 or (4st−1)² − s, since R = 0 there). No "sufficiently large"
  hypothesis in this memo excludes them, because no statement in this memo has such a hypothesis.

Verdict: **not a hot lead**. Nothing here survives the falsifiers *as a proof*, because nothing here is a proof of
the target; all PROVED items are necessary conditions and reformulations.

## §9a Provenance (from the cross-model review; this lane was run unprimed and did not read the memos named)

The reviewer maps the §1 content to prior work as follows, and I record it so that nothing here is sold as new:
Lemmas 1.1–1.4 (divisor/pair/C forms, square obstruction, prime-character sign) are rederivations of Z56_FAMTRY.md
Lemmas 1.1–1.4 and Z57_SYNTH.md Lemma A.1; Lemma 1.5 extends Z58_WITNESS.md Lemma 1.1 (non-residue prime factor,
d_min ≥ least non-residue at primes) to non-square composite n ≡ 1 (4); Lemma 1.6 is a specialisation of
LOWER_TAIL_ASTRA.md Lemma 2.2; Lemma 1.7 is FRONTIER.md §2.1 / BRAINSTORM/z45_interlacing_stable.md §1; Lemma 1.8 is
an incremental (all-six-classes CRT, logarithmic size) strengthening of the finite-covering exclusions in
Z56_FAMTRY.md Prop. 2.2 and Z58_WITNESS.md §0 F1; the C-even = R₈ identification and the twelve 10¹⁰ primes are
Z57_SYNTH.md §2.1; prime-only failures and the divisor-in-moving-class wall are Z56_FAMTRY.md §§4.2–4.6. The
contribution of this memo is a consolidated attempt record, the elementary extensions just listed, and a refreshed
𝔐-restricted census; it is not a new positivity mechanism.

## §9b Cross-model review (data/z59/xreview/REVIEW_MSPF.md, verdict ACCEPT-WITH-FIXES) — what was fixed

* F3: removed the unsupported "zeros outside 𝔐 continue indefinitely" and the inference that an eventual proof must
  use membership in 𝔐; the 10¹¹ census is attributed to Z58_LADDER.md and marked as not recomputed (§0, §9).
* Screens: recomputed and recorded all 285 composite zeros (15 in 𝔐), the three further in-𝔐 composites, the 14
  (★)-zeros and the 38 𝔊*-zeros with the full-family/subfamily distinction (§4, §0 F4, §9 F4; new data files
  zeros_all_8e6.txt, star_recomputed.txt, gstar_recomputed.txt).
* Scope: Lemma 1.8's consequence restated as three precise exclusions (bounded menu, fixed-modulus selector,
  class-wide identity) with an explicit "nothing more is claimed"; the "only through non-principality" language
  replaced by "one available encoding" (§1 remark, §9 F1); the Jacobi-value-(−1) vs non-square-residue distinction
  noted (11 mod 121).
* Provenance: §9a added.
* Citations/notation: squarefree part f(n) = ∏_{v_p(n) odd} p defined; the q₁ bound cited to Lau–Wu (cubefree-modulus
  Burgess) via the rad(n) reduction; "nothing is known below" replaced by "no smaller uniform exponent is claimed".

## §10 Status

* PROVED: Lemmas 1.1–1.8 (reformulations; the Jacobi obstruction; every witness modulus is a χ_n-non-residue, hence
  ≥ q₁(n); the two cofactors have opposite χ_n-signs; R(n) even for odd n; moduli ≤ D are useless for n ≡ m² (mod
  lcm(1..D)), such n exist in every class of 𝔐).
* CERTIFIED: all numerics in §4–§5.
* NOT PROVED: the target, in any range or any weakened pointwise form beyond the trivial "k = 1 works iff (n+1)/2 has
  a prime factor ≡ 3 (mod 4)"-type statements.
* Assessment: the pointwise statement is equivalent to "some n + k has a divisor ≡ −1 (mod 4k)", which is a
  pointwise divisor-in-progression statement about shifted integers; I see no mechanism other than factorisation of
  n + k through which non-squareness could act, and no known method controls that pointwise.
