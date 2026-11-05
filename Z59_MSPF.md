# Z59_MSPF — tryhard lane MSPF (wave z59): the pointwise statement for 4uBC − u − B = n

Status line (updated at every commit): **IN PROGRESS** — no hot lead yet.

Problem (verbatim target). For every sufficiently large non-square n with n mod 840 ∈ 𝔐 = {1, 121, 169, 289, 361, 529}
(n ≡ 1 (24), n a nonzero square mod 5 and mod 7), the equation 4uBC − u − B = n has a solution in positive integers.
Equivalently: some d ≡ 3 (mod 4), d ≥ 3, has k := (−n mod d) dividing (d+1)/4.

## §0 Mandatory falsifiers (stated up front; re-stated in §9 at the end)

Any argument for the target must be run through all four of the following. Where this memo proves something, the
relevant falsifier is answered explicitly next to the proof; where it does not, the memo says so.

* **(F1) Odd squares.** R(m²) = 0 for every odd m (CERTIFIED in data/z58/screens/README.md; re-proved below as Lemma 1.3:
  for every admissible pair (d, k), −k is a Jacobi non-residue mod d). Consequence (Lemma 1.4): *no* argument that uses
  only congruence information about n (n mod M for any fixed M, or any finite set of residue conditions) can prove the
  target, because odd squares occupy every residue class in 𝔐 that the target concerns. A correct proof must use a
  global property of n that distinguishes it from m² — the only such property available in the problem is that the
  Jacobi character χ_n(·) = (·/n) is non-principal (it is principal iff n is a square). Every step of any proof
  below must point to where this is used; the step that fails at n = m² must be identified.
* **(F2) C even alone.** The C-even part of the family (4uBC − u − B = n with C even ⇔ 8u′BC′ … see §1) fails at 4
  primes in 𝔐 ∩ [10¹⁰, 1.1·10¹⁰] (data/z58/screens/r8_zeros_1e10.txt, those with p mod 840 ∈ 𝔐). So any argument that
  only ever produces even C (e.g. only uses moduli 8k | n + k + B) is wrong; the memo must say which parity of C the
  construction produces and why odd C is reachable.
* **(F3) Non-square zeros.** Inside 𝔐 non-square zeros exist up to 17 401 609 and nowhere in (17 401 609, 10¹¹];
  outside 𝔐 non-square zeros continue indefinitely (mostly 3 | n, 5 | n or 7 | n). Any proof must (a) produce an explicit
  threshold n₀ (or explain why it cannot), with n₀ > 17 401 609, and (b) fail for n ∉ 𝔐 — the step that uses
  n ≡ 1 (24), (n/5) = (n/7) = 1 must be identified. (For n with 3 | n, 5 | n or 7 | n the moduli d divisible by 3, 5, 7
  are dead, which is the explanation of most outside-𝔐 zeros; the memo must not rely on those d.)
* **(F4) The nine prime zeros** 5569, 9601, 83449, 102001, 712321, 1724209, 1726201, 5212561, 8813281 (all in 𝔐).
  Any construction (choice of d, k as functions of n) must be evaluated at these nine; it must fail there, and the memo
  must say which hypothesis (size, a "sufficiently large" threshold, or a structural hypothesis) excludes them.

Surviving all four honestly = hot lead, to be flagged in the title and committed at once.

## §1 Reformulations and the obstruction (all PROVED; numerically checked, §6)

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
so d ≥ q₁(n) := min{q prime : (q/n) = −1}; for n ∈ 𝔐 one has q₁(n) ≥ 11.
*Proof.* n ≡ −k (d) and gcd(k, d) = 1 give gcd(n, d) = 1. (n/d) = (−k/d) = −1 by 1.3; Jacobi reciprocity for the
coprime odd positive pair (n, d) with n ≡ 1 (4) gives (d/n) = (n/d) = −1. χ_n is completely multiplicative, so some
prime factor q of d has χ_n(q) = −1. For n ∈ 𝔐: n ≡ 1 (8) gives (2/n) = 1; for q ∈ {3, 5, 7}, (q/n) = (n/q) = 1 by
reciprocity (n ≡ 1 (4)) and the definition of 𝔐. ∎

*Remark (where non-squareness lives).* χ_n is principal exactly when n is a square, and then Lemma 1.5 says no hit
modulus exists — this is the second proof of 1.4. Conversely, for a non-square n ≡ 1 (4), χ_n is a non-principal real
character of conductor f(n) | n (f(n) = the squarefree kernel of n, up to the factor at 2 which is absent for n ≡ 1 (4)),
and **the whole content of the target is: the structured set S(n) := {d ≡ 3 (4) : (−n mod d) | (d+1)/4} meets the
coset {χ_n = −1}**. Note that S(n) ⊂ {χ_n = −1} automatically (1.5), so the target is simply S(n) ≠ ∅; what Lemma 1.5
adds is the *necessary* shape of any witness: d must contain an odd number (with multiplicity) of prime factors from
{q : (q/n) = −1}.

**Lemma 1.6 (Jacobi signs of the two cofactors).** Let n ≡ 1 (4) and (k, B) a solution with gcd(kB, n) = 1 (automatic
for prime n, since k, B ≤ (n+1)/3 < n). Then (B/n) = −(k/n).
*Proof.* dB = n + k ≡ k (mod n) ⇒ (d/n)(B/n) = (k/n), and (d/n) = −1. ∎

**Lemma 1.7 (R(n) is even for odd n).** For odd n the swap (k, B) ↦ (B, k) is a fixed-point-free involution of the
solution set of 1.1(b); hence R(n) ≡ 0 (mod 2), and the target is equivalent to R(n) ≥ 2.
*Proof.* The condition 4kB | n + k + B is symmetric. A fixed point k = B has 4k² | n + 2k, so k | n and
n/k + 2 ≡ 0 (mod 4k); the latter forces n/k even, impossible for odd n. ∎
(Checked: R(p) is even for all 20 513 primes p ∈ 𝔐, p ≤ 10⁷, and for the 12 primes of r8_zeros_1e10.txt.)

**Lemma 1.8 (no congruence proof; moduli ≥ D are unavoidable).** Let D ≥ 1, L := lcm(1, …, D). If n ≡ m² (mod L)
for some m with gcd(m, L) = 1, then every hit modulus d of n satisfies d > D. Such n exist in every class of 𝔐: for
any odd m coprime to 840L with m² in the prescribed class, every n = m² + 840L·t (t ≥ 1) qualifies, and all but
O(√X/L) of those ≤ X are non-squares.
*Proof.* If d ≤ D then d | L, so n ≡ m² (mod d) and (n/d) = (m/d)² = 1 (gcd(m, d) = 1), contradicting Lemma 1.5. ∎
Consequence: no argument that only uses n modulo a fixed M (Mordell-type identities, finite covering systems of
residue classes, "local" sieving at bounded moduli) can prove the target on any class containing a square mod M —
and every class of 𝔐 refined by congruences mod M contains such n unless the refinement itself is a χ-non-residue
condition mod M. In other words: the only congruence conditions that can ever *finish* a case are of the form
"n ≡ r (mod M) with r a non-square mod M", and the n that are squares modulo every d ≤ D (with D ≈ log n allowed,
since L ≤ n suffices... precisely L = e^{D(1+o(1))}) must be handled by moduli d > D.

## §2 What a proof must deliver (consequence of §1)

For every large non-square n ∈ 𝔐 one needs an explicit d ≡ 3 (4) with (i) χ_n(d) = −1 and (ii) (−n mod d) | (d+1)/4.
By 1.8, for infinitely many n in every class the witness has d > D for any prescribed D ≤ (1+o(1))·log n, i.e. the
witness cannot be read off from n modulo any bounded modulus; by 1.5 it cannot be read off from n modulo any set of
moduli on which χ_n looks principal. Any construction d = d(n) therefore has to use a global datum of n: a prime q with
(q/n) = −1 (least such: q₁(n), which is ≪ n^{1/(4√e)+ε} by Burgess and ≪ log² n under GRH — but nothing is known
unconditionally below n^{1/(4√e)}), or the factorisation of n + k for small k, or the near-square structure n = a² + r.
§3 records what each of these gives and where each stops.
