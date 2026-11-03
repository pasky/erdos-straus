# Z54_UPPER2 — upper bounds for HC(p): what can and cannot be proved (lane UPPER2, wave z54)

Target of the lane: **HC(p) ≤ (log p)³ for every sufficiently large prime p ≡ 1 (mod 4).**

Definitions (as in the brief). For n ≡ 1 (mod 4) a *word* of n is (t, u, v) ∈ ℕ³ with tuv − u − v = n;
𝒞_n := {x ∈ ℕ : x ≡ 0 (mod 4) or x ≡ −n (mod 8)}; HC(n) := least element of 𝒞_n occurring as a coordinate of a word of n
(∞ if none). Input taken from the repo (the brief's Theorem 1, LOWERTAIL_ROUND2_FABLE §1.1): a word of p with a
coordinate in 𝒞_p yields a solution of 4/p = 1/x + 1/y + 1/z. Nothing else from the repo is used; all other statements
below are proved here from first principles or from named standard theorems of analytic number theory.

Labels: PROVED (complete proof here, possibly citing standard published theorems, each named), CERTIFIED (exact
computation, script + data named), EVIDENCE (numerics/heuristics, not proofs).

---------------------------------------------------------------------------------------------------------------------

## 0. Verdict

1. **The target is not proved, and cannot be expected to be proved by the methods available here.** By the repo's
   Theorem 1 the target implies the Erdős–Straus conjecture for all but finitely many primes p ≡ 1 (mod 4) (hence, with
   the trivial p ≡ 3 (4) and p = 2 cases, for all but finitely many primes) — an open problem since 1948. The same is true
   for *every* weaker uniform bound "HC(p) ≤ F(p) for all large p" (F = p^θ with 0 < θ < 1 included): any finite
   bound for all large p already implies eventual Erdős–Straus. So the brief's milestone "HC(p) ≤ p^θ for all p" would
   also resolve that open problem (only the forward implications are proved; the relative difficulty of the polynomial
   and polylogarithmic bounds is not established). §6 states exactly which pointwise statement is missing (it is
   *equivalent* to the target, (★) in §6.1) and proves two structural obstructions: fixed-level congruence coverings
   cannot work, and the integer sifted set of §4 is never empty (Props 6.2, 6.3).
2. **PROVED, for all p in explicit residue classes (§3):** HC(p) = 3 for p ≡ 5 (8); HC(p) ≥ 4 for p ≡ 1 (8); HC(p) ≤ 8 for
   every prime p ≡ 1 (8), p > 7, that is a quadratic non-residue modulo at least one of 3, 5, 7 — i.e. for all primes
   p ≡ 1 (4) outside the six classes 1, 121, 169, 289, 361, 529 (mod 840) (Mordell's classes) — with six explicit words.
3. **PROVED, for almost all p (§4):**
   * (Thm 4.3) For every K > 0 there is X₀(K) (explicitly X₀ = 4⌈e^{2K+2}⌉) such that
     #{p ≤ N : p ≡ 1 (4), HC(p) > X₀} ≪_K N/(log N)^K. In particular HC(p) is *bounded* off a set of primes of size
     O_K(N/(log N)^K).
   * (Thm 4.4 + Cor 4.5) #{p ≤ N : p ≡ 1 (4), HC(p) > (log p)³} ≤ N·exp(−0.8 (log log N)²) + √N for N ≥ N₀
     (N₀ ineffective, via Siegel–Walfisz). So the target holds for all primes outside a set that is sparser than
     N/(log N)^K for every K.
4. **PROVED structural obstructions (§2, §6):** (Lemma J) for p ≡ 1 (mod 8) every certificate carries a Jacobi symbol
   −1: if x ∈ 𝒞_p is a coordinate via a divisor d (of p + x or of xp + 1, d ≡ −1 mod x), then (p/d′) = −1 for the odd part d′ of d.
   Consequences: (Prop 6.2) **no odd square n = m² has any word with a coordinate in 𝒞_n**, so any proof of the target
   must use the non-squareness of p (in particular the integer sifted sets of §4 are never empty); (Prop 6.3) no finite
   set of fixed-level tests (congruence rules p ≡ −x mod d, xp ≡ −1 mod d) covers all primes, and there are infinitely
   many primes every certificate of which uses a level with a prime factor > c·log p.
5. **CERTIFIED (§5):** HC(p) ≤ 64 and HC(p) ≤ (log p)³ for all primes 5 ≤ p ≤ 10⁹, p ≡ 1 (4) (25 423 491 primes; max HC = 64 at
   p = 21 841 only; max HC/(log p)³ = 0.72 at p = 5). So the target statement holds for every p ≤ 10⁹.

---------------------------------------------------------------------------------------------------------------------

## 1. The divisibility form of "x is a coordinate" (PROVED)

**Lemma 1.1 (word identities).** For t, u, v ∈ ℕ and n: tuv − u − v = n ⟺ (tu − 1)v = n + u ⟺ (tu − 1)(tv − 1) = tn + 1
(the last when t ≥ 1).
*Proof.* (tu−1)v − u = tuv − u − v. (tu−1)(tv−1) = t²uv − tu − tv + 1 = t(tuv − u − v) + 1, and t ≠ 0. ∎

**Lemma 1.2 (Lemma R).** Let n ≥ 1 and x ≥ 2. Then x is a coordinate of some word of n iff
 (U) n + x has a positive divisor d ≡ −1 (mod x), or
 (T) xn + 1 has a positive divisor d ≡ −1 (mod x).
Explicitly, (U) gives the word ((d+1)/x, x, (n+x)/d) and (T) gives (x, (d+1)/x, (d*+1)/x) with d* = (xn+1)/d.
*Proof.* (⇐, U) d ≡ −1 (mod x), d ≥ 1, x ≥ 2 ⇒ d ≥ x − 1, so t := (d+1)/x ∈ ℕ, tx − 1 = d, v := (n+x)/d ∈ ℕ and
(tx−1)v = n + x; by Lemma 1.1 (t, x, v) is a word. (⇐, T) d·d* = xn + 1 ≡ 1 (mod x) and d ≡ −1 give d* ≡ −1 (mod x);
u := (d+1)/x, v := (d*+1)/x are positive integers with (xu−1)(xv−1) = xn + 1, so (x, u, v) is a word by Lemma 1.1.
(⇒) If x = u is the middle coordinate of (t, u, v) then d := tu − 1 ≥ 1 divides n + u = n + x and d ≡ −1 (mod x): (U).
The case x = v is the same after the symmetry (t, u, v) ↦ (t, v, u). If x = t then d := tu − 1 divides tn + 1 = xn + 1
(Lemma 1.1) and d ≡ −1 (mod x): (T). ∎

Hence **HC(n) = min{x ∈ 𝒞_n : (U) or (T) holds for x}** (note 1 ∉ 𝒞_n for n ≡ 1 (4)). Since a positive integer has a
divisor ≡ 3 (mod 4) iff it has a prime factor ≡ 3 (mod 4), the case x = 4 reads: *4 is a coordinate iff n + 4 or 4n + 1
has a prime factor ≡ 3 (mod 4).*

CERTIFIED (`scripts/z54_upper2_lemmas.py`, L1; `data/z54/upper2/lemmas_4000.txt`): for all n ≡ 1 (4), 5 ≤ n ≤ 4000, and all
2 ≤ x ≤ n + 2 (every coordinate of a word of n is ≤ n + 2: t = (n+u+v)/(uv) ≤ n + 2; if t ≥ 2 then (t−1)u ≤ n + 1 by
(tu−1)v = n + u; if t = 1 then (u−1) | n + 1; v symmetrically), the predicate (U)∨(T) equals "x is a coordinate of a word
found by brute-force enumeration" (50 968 words, 0 mismatches).

The "level" of the certificate is d (in (U): d = tu − 1 with u = x; in (T): d = tu − 1, and also d* = tv − 1).

## 2. The Jacobi law of certificates (Lemma J, PROVED)

**Lemma 2.1 (Lemma J).** Let n ≡ 1 (mod 8) and x ∈ 𝒞_n (x ≡ 0 (4) or x ≡ 7 (8)). Let d be a divisor as in (U) or (T)
for x, and d′ the odd part of d. Then gcd(n, d′) = 1 and the Jacobi symbol (n/d′) = −1. (In particular d′ > 1.)

*Proof.* In case (U), n ≡ −x (mod d); in case (T), xn ≡ −1 (mod d), so x is invertible mod d and n ≡ −x⁻¹ (mod d). Since
(x⁻¹/d′) = (x/d′) (their product is (1/d′) = 1), in both cases it suffices to show (−x/d′) = −1 (then (n/d′) = −1 ≠ 0
also forces gcd(n, d′) = 1). Note gcd(x, d) = 1 since d ≡ −1 (mod x).
*Case 4 | x.* Then d ≡ −1 (mod 4), so d is odd, d′ = d ≡ 3 (mod 4) and (−1/d) = −1. Write x = 2^e·m, m odd, e ≥ 2.
By quadratic reciprocity for the odd coprime positive m, d, using (d−1)/2 odd:
(m/d) = (d/m)·(−1)^{(m−1)/2} = (−1/m)·(−1)^{(m−1)/2} = 1, because d ≡ −1 (mod m) (for m = 1 trivially (1/d) = 1).
If e is even, (2/d)^e = 1; if e is odd then e ≥ 3, 8 | x, d ≡ −1 (mod 8) and (2/d) = 1. So (x/d) = 1 and (−x/d) = −1.
*Case x ≡ 7 (mod 8).* Write d = 2^f d′. Reciprocity with (x−1)/2 odd: (x/d′) = (d′/x)·(−1)^{(d′−1)/2} = (d′/x)(−1/d′), so
(−x/d′) = (−1/d′)²(d′/x) = (d′/x). From 2^f d′ ≡ −1 (mod x): (2/x)^f (d′/x) = (−1/x) = −1, and (2/x) = 1 as
x ≡ 7 (mod 8); so (d′/x) = −1. ∎

For a prime p ≡ 1 (mod 8) reciprocity turns (p/d′) = −1 into (d′/p) = −1: *every certificate level has a prime factor
that is a quadratic non-residue mod p.* (This is the elementary mechanism behind the repo's Jacobi form of Theorem 1; it
is self-contained here.)

CERTIFIED (`lemmas.py` L2): all 29 820 (coordinate in 𝒞_p, level) pairs of all words of all primes p ≡ 1 (8), p < 12 000:
0 violations.

## 3. Results for every prime in explicit classes (PROVED)

**Proposition 3.1.** Let p > 7 be prime.
(a) If p ≡ 5 (mod 8) then HC(p) = 3, witnessed by the word (1, 3, (p+3)/2).
(b) If p ≡ 1 (mod 8) then HC(p) ≥ 4, and
  * p ≡ 2 (mod 3) ⇒ HC(p) = 4, word (1, 4, (p+4)/3);
  * p ≡ 3 (mod 7) ⇒ HC(p) = 4, word (2, 4, (p+4)/7);
  * p ≡ 5 (mod 7) ⇒ HC(p) = 4, word (4, 2, ((4p+1)/7 + 1)/4);
  * p ≡ 3 (mod 5) ⇒ HC(p) ≤ 7, word (3, 7, (p+7)/20);
  * p ≡ 2 (mod 5) ⇒ HC(p) ≤ 7, word (7, 3, ((7p+1)/20 + 1)/7);
  * p ≡ 6 (mod 7) ⇒ HC(p) ≤ 8, word (1, 8, (p+8)/7).
(c) Consequently HC(p) ≤ 8 for every prime p ≡ 1 (mod 4), p > 7, with p ≢ 1, 121, 169, 289, 361, 529 (mod 840); the
excluded classes are exactly the p ≡ 1 (8) that are quadratic residues modulo 3, 5 and 7.

*Proof.* (a) For p ≡ 5 (8), 𝒞_p = 4ℕ ∪ (8ℤ_{≥0} + 3), whose least element is 3. p + 3 ≡ 0 (mod 8), so v = (p+3)/2 ∈ ℕ and
1·3·v − 3 − v = 2v − 3 = p. (b) For p ≡ 1 (8), 𝒞_p = 4ℕ ∪ (8ℤ_{≥0} + 7), and 1, 2, 3 ∉ 𝒞_p, so HC(p) ≥ 4. Each listed word
is checked by expanding tuv − u − v, and its integrality from the congruence: (1,4,v): 3v − 4 = p, 3 | p + 4 ⟸ p ≡ 2 (3).
(2,4,v): 7v − 4 = p, 7 | p + 4 ⟸ p ≡ 3 (7). (4,2,v): this is Lemma 1.2 (T) with x = 4, d = 7: 7 | 4p+1 ⟸ p ≡ 5 (7), and
d* = (4p+1)/7 ≡ 3 (mod 4) because 4p+1 ≡ 1 and 7 ≡ 3 (mod 4), so v = (d*+1)/4 ∈ ℕ. (3,7,v): 20v − 7 = p, 20 | p + 7 ⟸
p ≡ 1 (4) and p ≡ 3 (5) (then p ≡ 13 (20)). (7,3,v): (T) with x = 7, d = 20: 7p + 1 ≡ 0 (mod 20) ⟸ p ≡ 17 (20), i.e.
p ≡ 1 (4), p ≡ 2 (5); d* = (7p+1)/20 satisfies 20d* ≡ 1 (mod 7) and 20 ≡ −1, so d* ≡ −1 (mod 7) and v = (d*+1)/7 ∈ ℕ.
(1,8,v): 7v − 8 = p, 7 | p + 8 ⟸ p ≡ 6 (7). The coordinates 4, 8 ∈ 4ℕ and 7 ≡ −p (mod 8) lie in 𝒞_p. (c) The quadratic
non-residues are {2} mod 3, {2,3} mod 5, {3,5,6} mod 7; for p > 7 a prime p ≡ 1 (8) that is a non-residue mod 3, 5 or 7 is
covered by (b). The six classes are those with p ≡ 1 (8), p ≡ 1 (3), p ≡ ±1 (5), p ≡ 1, 2, 4 (7). ∎

CERTIFIED (`lemmas.py` L5): the six words verified for all primes p ≡ 1 (8), p < 3·10⁵ (9 745 words), and "no word listed"
⟺ "QR mod 3, 5, 7". The covering computation `scripts/z54_upper2_cover.py` (`data/z54/upper2/cover.txt`) recovers
exactly these six residual classes mod 840 from *all* fixed-level tests with level d | 840 and x ≤ 10⁵; mod 9240 (·11)
and 120120 (·11·13) the residual sets have 38/480 and 242/5760 classes and always contain the quadratic-residue classes
(as Lemma J forces, §6.3), with the least covering x ≤ 71 on every covered class.

## 4. Almost all primes (PROVED)

Throughout, q denotes primes. Standard inputs (all classical):
* **(LS)** Arithmetic large sieve (Montgomery 1968; with N + Q² as in Gallagher / Montgomery–Vaughan 1973; e.g.
  Iwaniec–Kowalski Thm 7.14): if 𝒮 ⊆ ℤ ∩ [1, N] and for every prime q the set 𝒮 avoids ω(q) < q residue classes mod q,
  then for every Q ≥ 1, |𝒮| ≤ (N + Q²)/J(Q), J(Q) := Σ_{m≤Q} μ²(m) ∏_{q|m} ω(q)/(q − ω(q)).
* **(M)** Mertens in progressions: for fixed k and gcd(a,k) = 1, Σ_{q≤z, q≡a (k)} 1/q = (log log z)/φ(k) + O_k(1)
  (effective for each fixed k).
* **(BT)** Brun–Titchmarsh (Montgomery–Vaughan 1973): π(t; k, a) ≤ 2t/(φ(k) log(t/k)) for t > k.
* **(SW)** Siegel–Walfisz: for every A > 0 there are c_A, C_A > 0 with
  |π(t; k, a) − Li(t)/φ(k)| ≤ C_A t·exp(−c_A √log t) for all t ≥ 2, k ≤ (log t)^A, gcd(a,k) = 1 (ineffective).
* Σ_{n≤X} 1/φ(n) ≤ C₀ log X (X ≥ 2) (Landau); d(n) ≤ C₁ n^{1/4}.

**Lemma 4.1 (the sieve input).** Let q be an odd prime, x ∈ 4ℕ with x | q + 1, and n ≡ −x (mod q), n ≥ 1. Then
((q+1)/x, x, (n+x)/q) is a word of n; x ∈ 𝒞_n for n ≡ 1 (4). For a fixed q the classes −x (mod q), x ∈ 4ℕ, x | q+1,
are pairwise distinct, and their number ω(q) satisfies ω(q) ≤ (q+1)/4 ≤ q/2.
*Proof.* Lemma 1.2 (U) with d = q ≡ −1 (mod x). Two distinct x, x′ ∈ [1, q+1] are congruent mod q only if {x, x′} = {1, q+1};
1 ∉ 4ℕ. The multiples of 4 dividing q+1 are among 4, 8, …, q+1. ∎

For a finite D ⊂ 4ℕ put ω_D(q) := #{x ∈ D : x | q + 1} and
𝒮_N(D) := {n ≤ N : n ≡ 1 (4), no word of n has a coordinate in D}.
By Lemma 4.1, 𝒮_N(D) avoids ω_D(q) classes mod q for every prime q (ω_D(2) = 0). Put g(q) := ω_D(q)/(q − ω_D(q)); by
ω_D(q) ≤ q/2, ω_D(q)/q ≤ g(q) ≤ 2ω_D(q)/q.

**Lemma 4.2 (lower bound for J).** Let z ≥ 2, G(z) := ∏_{q≤z}(1 + g(q)). If log Q ≥ log z·((e−1)·log G(z) + log 2), then
J(Q) ≥ G(z)/2.
*Proof.* h(m) := μ²(m)∏_{q|m} g(q) ≥ 0, so J(Q) ≥ Σ_{m | P(z), m ≤ Q} h(m) = G(z) − Σ_{m|P(z), m>Q} h(m), P(z) = ∏_{q≤z} q.
With σ = 1/log z (Rankin): Σ_{m|P(z), m>Q} h(m) ≤ Q^{−σ} Σ_{m|P(z)} h(m) m^σ = Q^{−σ} ∏_{q≤z}(1 + g(q)q^σ)
≤ Q^{−σ} ∏_{q≤z}(1 + e·g(q)) ≤ Q^{−σ} G(z)^e (q^σ ≤ e; 1 + e·g ≤ (1+g)^e by Bernoulli). By hypothesis
Q^{−σ}G(z)^{e−1} = exp(−log Q/log z + (e−1) log G(z)) ≤ 1/2. ∎

**Theorem 4.3 (bounded HC off a sparse set).** Let K > 0, X₀ := 4⌈e^{2K+2}⌉, D := 4ℕ ∩ [1, X₀]. Then
|𝒮_N(D)| ≪_K N (log log N)^{K+1}/(log N)^{K+1} ≤ N/(log N)^K for N ≥ N₀(K). Consequently
#{p ≤ N prime : p ≡ 1 (4), HC(p) > X₀} ≪_K N/(log N)^K, and (since X₀ ≤ (log p)³ for p ≥ exp(X₀^{1/3}))
#{p ≤ N : p ≡ 1 (4), HC(p) > (log p)³} ≪_K N/(log N)^K.

*Proof.* Let κ := Σ_{x∈D} 1/φ(x). Since φ(4j) ≤ 2j, κ ≥ ½Σ_{j≤X₀/4} 1/j ≥ ½ log(X₀/4) ≥ K + 1. Let B := X₀/4 ≥ ω_D(q).
By (M) applied to the finitely many moduli x ∈ D (note q ≡ −1 (mod x) with 4 | x forces q odd):
Σ_{q≤z} ω_D(q)/q = Σ_{x∈D} Σ_{q≤z, q≡−1 (x)} 1/q = κ log log z + O_K(1).
Hence log G(z) ≤ Σ g(q) ≤ 2κ log log z + C₁(K), and, using log(1+g) ≥ g − g²/2, g(q) ≤ 2B/q and Σ_q q^{−2} < ½,
log G(z) ≥ κ log log z − C₂(K) − B².
Take Q = √N and log z := log Q / ((e−1)(2κ log log N + C₁) + 1). Then z ≤ N, so (e−1) log G(z) + log 2 ≤ log Q/log z and
Lemma 4.2 gives J(Q) ≥ G(z)/2. Also log log z = log log N − log log log N − O_K(1), so
G(z) ≫_K (log N)^κ/(log log N)^κ. By (LS), |𝒮_N(D)| ≤ 2N/J ≤ 4N/G(z) ≪_K N(log log N)^κ/(log N)^κ, and κ ≥ K + 1.
Every prime p ≡ 1 (4), p ≤ N, with HC(p) > X₀ has no coordinate in 𝒞_p ∩ [1, X₀] ⊇ D, so lies in 𝒮_N(D). For the last
claim add the O_K(1) primes p < exp(X₀^{1/3}). ∎

**Theorem 4.4 (growing window).** Let D_N := 4ℕ ∩ [1, (log N)²]. For N ≥ N₀ (ineffective),
|𝒮_N(D_N)| ≤ N·exp(−0.8 (log log N)²).

*Proof.* Write L₂ := log log N, X := (log N)², ω := ω_{D_N}, and let N be large.
*(i) Upper bound for Σ ω(q)/q.* For x ∈ D_N, the primes q ≡ −1 (mod x) with q ≤ x² are among jx − 1, 1 ≤ j ≤ x, so
contribute ≤ Σ_{j≤x} 2/(jx) ≤ (2/x)(1 + log x). For q > x² use (BT) with log(t/x) ≥ ½ log t (t ≥ x²) and partial summation:
Σ_{x²<q≤z, q≡−1(x)} 1/q ≤ π(z;x,−1)/z + ∫_{x²}^{z} π(t;x,−1) t^{−2} dt ≤ (4/φ(x))(1 + log log z)
(for z ≤ x² this sum is empty and the bound is trivial; z ≥ e assumed).
So Σ_{q≤z} ω(q)/q ≤ Σ_{x∈D_N} (6 + 2 log x + 4 log log z)/φ(x) ≤ (6 + 2 log X + 4L₂)·C₀ log X ≤ C₃ L₂² for z ≤ N, and
log G(z) ≤ 2Σ ω(q)/q ≤ 2C₃ L₂².
*(ii) Choice of z.* Q = √N, log z := log Q/(2(e−1)C₃L₂² + 1). Then Lemma 4.2 applies: J(Q) ≥ G(z)/2, and
log log z = L₂ − 2 log L₂ − O(1).
*(iii) Lower bound.* Fix A = 40 and put T_x := exp(x^{1/A}). For t ≥ T_x, x ≤ (log t)^A, so (SW) applies to π(t; x, −1).
log T_x ≤ X^{1/A} = (log N)^{1/20} < log z, so T_x < z. Partial summation from T_x to z with π = Li/φ(x) + E,
|E(t)| ≤ C_A t e^{−c_A√log t}:
Σ_{T_x<q≤z, q≡−1(x)} 1/q ≥ (log log z − log log T_x)/φ(x) − R(x), with
R(x) := 2C_A e^{−c_A x^{1/(2A)}} + C_A∫_{x^{1/A}}^{∞} e^{−c_A√s} ds ≪_A (1 + x^{1/(2A)}) e^{−c_A x^{1/(2A)}},
and Σ_{x≥1} R(x) =: R_A < ∞. Since log log T_x = (log x)/A ≤ (2/A)L₂ = L₂/20 and Σ_{x∈D_N} 1/φ(x) ≥ ½ log(X/4) =
L₂ − log 2:
Σ_{q≤z} ω(q)/q ≥ (log log z − L₂/20)(L₂ − log 2) − R_A ≥ (19/20 − o(1)) L₂².
Moreover Σ_q g(q)² ≤ 4Σ_q ω(q)²/q² ≤ 4C₁² Σ_q (q+1)^{1/2}/q² = O(1) (ω(q) ≤ d(q+1)), so
log G(z) ≥ Σ ω(q)/q − ½Σ g(q)² ≥ 0.9 L₂² for large N.
*(iv)* By (LS): |𝒮_N(D_N)| ≤ (N + N)/J(Q) ≤ 4N/G(z) ≤ 4N e^{−0.9L₂²} ≤ N e^{−0.8L₂²}. ∎

**Corollary 4.5 (the target for almost all p).** For N ≥ N₀,
#{p ≤ N prime : p ≡ 1 (4), HC(p) > (log p)³} ≤ N·exp(−0.8 (log log N)²) + √N.
*Proof.* Primes p ≤ √N contribute ≤ √N. If √N < p ≤ N then (log p)³ > (log N)³/8 ≥ (log N)² (log N ≥ 8), so
HC(p) > (log p)³ implies that no word of p has a coordinate in D_N ⊆ 𝒞_p ∩ [1, (log p)³], i.e. p ∈ 𝒮_N(D_N). ∎

*Remarks.* (1) Only the u-coordinates x ∈ 4ℕ and prime levels d = q are used; the T-tests, composite levels and the
8ℤ_{≥0} + 7 part of 𝒞_p are not used (their effect on the bounds is not analysed here). (2) This construction is
capped: with the classes of Lemma 4.1 and a window D of polylogarithmic size, J(Q) ≤ ∏_{q≤Q}(1 + g(q)) ≤
exp(O((log log N)²)) (by §4(i)-type bounds), so N·exp(−O((log log N)²)) is the limit of this large-sieve argument, and
no bound for the integer set can reach 0: 𝒮_N(D) contains every odd square ≤ N (Prop 6.2), so |𝒮_N(D)| ≥ ½√N − 1.
(3) The known Erdős–Straus exceptional-set bounds (Vaughan: N·exp(−c(log N)^{2/3})) are about the existence of *some*
solution and do not by themselves bound HC; the bound of Cor 4.5 is weaker in size but controls HC ≤ (log p)³.

## 5. Census (CERTIFIED)

`scripts/z54_upper2_hc.c` (Lemma 1.2 predicate; 64-bit Miller–Rabin + Pollard rho factorization of p + x and xp + 1;
x scanned in increasing order through 𝒞_p): `data/z54/upper2/hc_1e8.txt`, `hc_1e9.txt`.

| range | primes p ≡ 1 (4) | max HC | argmax | max HC/(log p)³ | #{HC > (log p)³} |
|---|---|---|---|---|---|
| p ≤ 10⁸ | 2 880 504 | 64 | 21 841 | 0.7196 (p = 5) | 0 |
| p ≤ 10⁹ | 25 423 491 | 64 | 21 841 | 0.7196 (p = 5) | 0 |

Record progression: 3 (p=5), 4 (17), 7 (97), 15 (2521), 64 (21841); no new record in (21 841, 10⁹]. HC distribution to
10⁹: 3: 12 712 271; 4: 11 724 820; 7: 891 590; 8: 69 654; 12: 15 624; 15: 6 042; 16: 1 856; 20: 1 022; 23: 374;
24: 130; 28: 32; 31: 37; 32: 12; 36: 8; 39: 6; 40: 2; 44: 5; 47: 3; 52, 56, 64: 1 each. Every p ≡ 5 (8) has HC = 3
(consistency with Prop 3.1(a), 0 anomalies). Which test fires at x = HC: (U) only 1.86M, (T) only 1.87M, both 21.7M.
The p ≤ 10⁸ counts agree with the brief's census (2 880 504 primes, max 64).

## 6. What is missing, exactly

### 6.1 The equivalent pointwise statement (PROVED equivalence)

By Lemma 1.2 the target is **equivalent** to:

(★) for every sufficiently large prime p ≡ 1 (mod 8) there are x ≤ (log p)³ with x ≡ 0 (4) or x ≡ 7 (8), and a divisor
d ≡ −1 (mod x) of p + x or of xp + 1.

(p ≡ 5 (8) is settled by Prop 3.1(a).) This is the statement I would need. It is a *pointwise* statement about the
multiplicative structure of the ≍ (log p)³ integers p + x, xp + 1 attached to one prime p. Unconditionally, for an
individual prime one cannot even guarantee that a single shifted number p + x has a prime factor in a prescribed
residue class (e.g. "p + 4 or 4p + 1 has a prime factor ≡ 3 (4)", which is (★) for x = 4, is expected to fail for
≍ N/(log N)² primes p ≤ N). (★) needs the *disjunction* over many x; proving that a disjunction of such events holds for
*every* prime is a sifted-set-is-empty statement, and §4 shows exactly how far sieve upper bounds go (the sifted set is
small, Thm 4.4, but never shown empty). Two proved obstructions, limiting what congruence coverings and integer sieves
can give:

### 6.2 Squares have no certificate at all (Proposition 6.2, PROVED)

**Proposition 6.2.** For every odd m and n = m², no word of n has a coordinate in 𝒞_n (HC(m²) = ∞).
*Proof.* n ≡ 1 (mod 8). A coordinate x ∈ 𝒞_n gives, by Lemma 1.2, a divisor d as in (U) or (T), and Lemma 2.1 gives
(n/d′) = −1; but (m²/d′) ∈ {0, 1}. ∎
CERTIFIED (`lemmas.py` L6): all odd squares 9 … 2025, all x ≤ n + 2: no 𝒞-coordinate.

*Consequence.* Any proof of (★) must use that p is not a square — more precisely the existence, for each p, of a prime
q with (p/q) = −1 *dividing one of the numbers p + x, xp + 1 in the right way*. In particular, any argument that proves
the conclusion for every n ≡ 1 (8) in a set defined only by conditions also satisfied by odd squares (e.g. the integer
sifted set 𝒮_N(D) of §4) is impossible; an argument must use non-squareness (or primality) of p essentially.
(For primes the existence of non-residues q is trivial; the content of (★) is their appearance as divisors of the
shifted numbers.)

### 6.3 No finite congruence covering; certificates need large primes (Proposition 6.3, PROVED)

Call a *fixed-level test* a triple (kind, x, d) with kind ∈ {U, T}, x ≡ 0 (4) or x ≡ 7 (8), d ≡ −1 (mod x); it fires on
p if d | p + x (U) or d | xp + 1 (T) — a condition on p mod d.

**Proposition 6.3.** (a) For every finite set 𝒯 of fixed-level tests, no test of 𝒯 fires on any n ≡ 1 (mod 8L),
L := lcm of the levels in 𝒯; by Dirichlet there are infinitely many such primes. Hence no finite set of fixed-level
tests proves HC(p) < ∞ (let alone ≤ (log p)³) for all p ≡ 1 (8). (This excludes covering by fixed-level tests only, not
every argument that uses congruences.)
(b) There is an absolute c > 0 and infinitely many primes p ≡ 1 (8) such that the level d of *every* certificate of p
(any x ∈ 𝒞_p, any size) has a prime factor q > c log p with (p/q) = −1.
*Proof.* (a) n ≡ 1 (mod d′) for each level, so (n/d′) = (1/d′) = 1, contradicting Lemma 2.1. (b) Let y be large,
M := 8·lcm(1, …, y) = e^{(1+o(1))y}. By Linnik's theorem (least prime in a progression ≤ C·M^{L₀}, L₀ absolute) there is a
prime p ≡ 1 (mod M) with log p ≤ L₀ log M + O(1) ≤ 2L₀ y. For such p and any certificate level d, Lemma 2.1 gives a prime
q | d′ with (p/q) = −1; since p ≡ 1 (mod q) for q ≤ y, q > y ≥ (log p)/(2L₀). Letting y → ∞ gives infinitely many p. ∎

So the certificates required by (★) cannot all come from a bounded set of small levels; any proof must control the
*large* prime factors of p + x or xp + 1, individually for each p.

### 6.4 Size of the best congruence certificate (EVIDENCE)

Fixing two coordinates (a ≤ b) of a word fixes the word and turns its existence into one congruence for p modulo
ab − 1 or ab. Let μ(p) := min over words of p with a coordinate in 𝒞_p ∩ [1, (log p)³] of the product of its two
smallest coordinates (`scripts/z54_upper2_modulus.c`, `data/z54/upper2/mu.txt`; cross-checked against the independent
factorization-based `scripts/z54_upper2_modulus_fac.c` for all p ≤ 10⁶: same records, same max 288, same mean,
`data/z54/upper2/mu_crosscheck_1e6.txt`):
* all p ≤ 10⁸: max μ = 2320 (p = 58 649 809), at successive μ-records μ/(log p)² is
not monotone (it first falls from 0.77 to 0.25 and later climbs to 7.25 at the last record); mean log μ/log p = 0.088;
* samples of 10⁵ consecutive primes p ≡ 1 (4) from 10¹⁰, 10¹², 10¹⁴, 10¹⁶, 10¹⁸: max μ = 693, 1302, 1524, 576, 635; μ(p) < ∞
  for every sampled prime, i.e. HC(p) ≤ (log p)³ held for all 5·10⁵ sampled primes (EVIDENCE beyond 10⁹).
So in the observed range every prime has a "small" congruence certificate. Heuristically (each pair (a, b) removes one
class of density ≍ 1/(ab), so certificates with ab ≤ Y leave density ≈ exp(−c(log Y)²)), the worst-case μ(p) should
eventually exceed every power of log p, i.e. for the worst primes the certificate of (★) will have its x small but its
other two coordinates large — the "middle factorization" regime of 6.1–6.3. This is a heuristic, not a proof.

### 6.5 Status of the brief's milestones

| milestone | status |
|---|---|
| HC(p) ≤ (log p)³ for all large p | open; equivalent to (★); implies Erdős–Straus for all but finitely many primes |
| HC(p) ≤ p^θ (0 < θ < 1) for all large p | open; would also imply ES for all large primes (any finite bound does) |
| HC(p) ≤ 8 on explicit classes | PROVED (Prop 3.1): all p ≡ 1 (4) outside 6 classes mod 840 |
| HC(p) bounded off a set of size N/(log N)^K | PROVED (Thm 4.3), any K, X₀ = 4⌈e^{2K+2}⌉ |
| HC(p) ≤ (log p)³ off a set of size N e^{−0.8(log log N)²} + √N | PROVED (Cor 4.5) |
| all p ≤ 10⁹ | CERTIFIED (§5) |

## 7. Reproduction

All with `ulimit -v 6000000` and `timeout`.
* `gcc -O2 -o z54hc scripts/z54_upper2_hc.c -lm; ./z54hc 1000000000` → `data/z54/upper2/hc_1e9.txt` (~2 min; `hc_1e8.txt` 11 s).
* `uv run --with sympy python scripts/z54_upper2_lemmas.py 4000` → `lemmas_4000.txt` (L1–L6, ~40 s).
* `uv run --with sympy python scripts/z54_upper2_cover.py m X` for (m, X) ∈ {105, 1155, 15015} × {64, large} → `cover.txt`;
  per-class rules mod 840 in `rules_840.txt`.
* `gcc -O2 -o z54mu scripts/z54_upper2_modulus.c -lm; ./z54mu all 100000000; ./z54mu sample 10^k 100000` → `mu.txt`.
