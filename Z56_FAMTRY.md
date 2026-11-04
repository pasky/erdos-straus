# Z56 FAMTRY — tryhard attack on "(★) has a solution for every large prime p ≡ 1 (mod 4)"

Lane: FAMTRY (Fable, unprimed). Rules: `z52bbriefs/z55_tryhard.md`. Definitions used: only `FRONTIER.md` §2.1.
Scripts: `scripts/z56_famtry_*`; data: `data/z56/famtry/`.

**Problem.** For an odd n let R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}. Prove: R(p) ≥ 1 for every sufficiently large
prime p ≡ 1 (mod 4). (R(p) ≥ 1 ⇒ 4/p = 1/(uBC) + 1/(pBC) + 1/(puC), so this would prove Erdős–Straus for all large primes.)

**Outcome (honest summary).**
* NOT PROVED for all p. What I could prove is an exceptional-set theorem by the large sieve (Theorem A, §3):
  #{p ≤ X : R(p) = 0} ≪ X·exp(−c√(log X)) — much stronger than a polylog saving, but structurally capped above √X
  because the argument never uses primality and squares n = m² have R(m²) = 0 (§3.5). The 14 known failures ≤ 10¹⁰
  are consistent with this; nothing here distinguishes "finitely many exceptions" from "zero exceptions beyond 8 813 281".
* Reformulations (§1) make the problem a *Linnik-type divisibility* statement: for a prime p, R(p) ≥ 1 iff some modulus
  d ≡ 3 (mod 4) has (−p mod d) dividing (d+1)/4. Every proof route I tried (finite residue coverings, polynomial
  identities in p, consecutive-integer factorisation structure, Jacobi/genus reciprocity) either runs into the square
  obstruction or gives only "almost all" (§4). §5 lists where each line stops.
* Numerics: `scripts/z56_famtry_census.c` re-derives the 14 (★)-zeros ≤ 10⁸ independently and finds R(m²) = 0 for all odd
  m² ≤ 10⁸ (CERTIFIED: zero/non-zero is exact; the counters saturate at 255, so the printed means are lower bounds);
  the sample mean of R(p) over primes p ≡ 1 (4), p ≤ 10⁸, is 0.146·log²(10⁸) (EVIDENCE).

Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE as in the rules.

---

## 1. Exact reformulations (PROVED, elementary)

**Lemma 1.1 (divisor–trial forms).** For odd n ≥ 1,
 R(n) = #{(u, C) ∈ ℕ² : (4uC − 1) | n + u}                              (1.1)
    = #{(m, u) : m ≥ 1, u | m, (4m − 1) | n + u}                            (1.2)
    = #{(d, u) : d ≡ 3 (mod 4), u | (d+1)/4, d | n + u}.                    (1.3)

*Proof.* 4uBC − u − B = n ⟺ B(4uC − 1) = n + u, so for given (u, C) the triples correspond to B = (n+u)/(4uC−1) ∈ ℕ,
i.e. to (4uC − 1) | n + u (B ≥ 1 automatically since n + u ≥ 1). (1.2): m := uC; (1.3): d := 4m − 1. ∎

**Lemma 1.2 (symmetric and C-forms).** Also R(n) = #{(u, B) : 4uB | n + u + B} (since 4uBC = n + u + B), and
R(n) = Σ_{C ≥ 1} #{d | 4Cn + 1 : d ≡ −1 (mod 4C)}, because (4uC − 1)(4BC − 1) = 4Cn + 1 and d·d' ≡ 1 (mod 4C) with
d ≡ −1 forces d' ≡ −1. (This is the "divisor form" of FRONTIER §2.1.)

**Lemma 1.3 (square obstruction; the Jacobi symbol).** If d ≡ 3 (mod 4), u | (d+1)/4 and d | n + u, then the Jacobi
symbol (n | d) = −1. Consequently R(m²) = 0 for every odd m, and for a prime p ≡ 1 (mod 4) every d occurring in (1.3)
satisfies (d | p) = −1.

*Proof.* n ≡ −u (mod d), gcd(u, d) = 1 (as d ≡ −1 mod 4u). (−u | d) = (−1 | d)(u | d) = −(u | d). For u odd,
quadratic reciprocity for Jacobi symbols gives (u | d) = (d | u)(−1)^{(u−1)(d−1)/4} = (−1 | u)(−1)^{(u−1)/2} = 1 (using
d ≡ −1 mod u and (d−1)/2 odd). For u = 2^k u' with u' odd: (2 | d) = 1 because d ≡ −1 (mod 8), and (u' | d) = 1 as before.
Hence (n | d) = (−u | d) = −1. A square coprime to d has symbol +1, so R(m²) = 0 (gcd(m, d) = 1 is forced: d | m² + u with
gcd(u,d)=1). For p ≡ 1 (mod 4), (p | d) = (d | p) by reciprocity. ∎

**Lemma 1.4 (Linnik-type form).** For an odd n, R(n) ≥ 1 ⟺ there is d ≡ 3 (mod 4), 3 ≤ d ≤ 4(n+1)/3, such that the least
positive residue r_d(n) := (−n mod d) ∈ [1, d−1] divides (d+1)/4.

*Proof.* In (1.3), u ≤ (d+1)/4 < d and n ≡ −u (mod d), so u = r_d(n). Range: d ≤ n + u ≤ n + (d+1)/4 gives d ≤ (4n+1)/3. ∎

So: **R(p) ≥ 1 iff some modulus d ≡ 3 (4) has "−p mod d" a divisor of (d+1)/4.** Heuristically, for each d the chance
is τ((d+1)/4)/d, Σ_d τ((d+1)/4)/d ≈ (1/8)log²D, and the events for different d are nearly independent ⇒ failure
probability ≈ exp(−c log²p) (the lottery picture; data: 14 failures, last 8 813 281). The known census (FRONTIER §2.1)
and my re-derivation (`data/z56/famtry/census_1e7.txt`) agree exactly.

## 2. What cannot work: residue-class coverings and polynomial identities (PROVED)

**Proposition 2.1.** (a) p ≡ 5 (mod 8) ⇒ R(p) ≥ 1 [(u,B,C) = (1, 2, (p+3)/8)]. (b) p ≡ 2 (mod 3) ⇒ R(p) ≥ 1 [d = 3, u = 1,
B = (p+1)/3, C = 1]. (c) p ≡ 5, 6 (mod 7) ⇒ R(p) ≥ 1 [d = 7, u ∈ {2, 1}]. (d) In general, each d ≡ 3 (4) covers the
τ((d+1)/4) classes G_d := {−u mod d : u | (d+1)/4} ⊂ {non-residues mod d}.

**Proposition 2.2 (no finite covering).** Let a_i (mod q_i), 1 ≤ i ≤ k, be residue classes such that every odd n > n₀ with
n ≡ a_i (mod q_i) has R(n) ≥ 1 ("solvable classes"). Then their union misses infinitely many primes p ≡ 1 (mod 8).

*Proof.* Put M := 8·lcm(q_1, …, q_k). The class 1 (mod M) contains odd squares m² (any m ≡ 1 mod M), and R(m²) = 0 by
Lemma 1.3; so no solvable class a_i (q_i) contains the whole class 1 (mod M), i.e. a_i ≢ 1 (mod q_i) for every i. Hence no
n ≡ 1 (mod M) lies in ∪_i {a_i mod q_i}, and by Dirichlet there are infinitely many primes p ≡ 1 (mod M) ⊂ 1 (mod 8). ∎

**Remark 2.3 (polynomial identities).** Any identity of the form "(u, B, C) = polynomials in p, valid for p in a residue
class" (e.g. C = (p+3)/8, (u,B) = (1,2) on p ≡ 5 (8); C = (p+7)/24, (u,B) = (1,6) on p ≡ 17 (24); in general (u,B) fixed,
C = (p+u+B)/(4uB) on p ≡ −(u+B) (4uB)) makes its class a solvable class, so Prop. 2.2 applies: no finite family of such
identities covers the primes ≡ 1 (8), and none is valid on a class containing 1 (mod M). So **any proof must use that p is
not a square in a way that is not a congruence condition** — i.e. the arithmetic of p itself (e.g. its quadratic character
d ↦ (d | p)).

EVIDENCE (`census_1e7.txt`): among primes p ≡ 1 (8) in [10⁶, 10⁷], R = 0 for 5 of 146 424; restricted to prime moduli
d (any size) the count R_pr = 0 for 143; restricted to prime d ≤ √p (the family the large sieve of §3 uses), R_sq = 0
for 2958 (2.0 %; the proportion falls 8.9 % → 6.7 % → 3.9 % → 2.0 % over the decades 10³…10⁷).

## 3. Theorem A: the exceptional set is ≪ X·exp(−c√log X) (PROVED, via the large sieve)

**Theorem A.** There are absolute constants c > 0 and X₀ (X₀ ineffective, from Bombieri–Vinogradov) such that for X ≥ X₀
 #{p ≤ X prime : R(p) = 0} ≤ X·exp(−c√(log X)),   and one may take c = 0.08.
The same bound holds for #{n ≤ X odd : n ∉ Ω_ℓ (mod ℓ) for all primes ℓ ≤ √X} (defined below), a set containing every
exceptional prime and every odd square.

### 3.1 Sifting sets

For a prime ℓ put Ω_ℓ := {−u mod ℓ : u | (ℓ+1)/4} if ℓ ≡ 3 (mod 4) and Ω_ℓ := ∅ otherwise; ω(ℓ) := |Ω_ℓ|.
Since 1 ≤ u ≤ (ℓ+1)/4 < ℓ, distinct u give distinct classes, so ω(ℓ) = τ((ℓ+1)/4) < ℓ for ℓ ≡ 3 (4).

**Lemma 3.1.** If n ≥ 1 is odd and n mod ℓ ∈ Ω_ℓ for some prime ℓ, then R(n) ≥ 1.
*Proof.* n ≡ −u (mod ℓ) with u | (ℓ+1)/4, i.e. (d, u) = (ℓ, u) is admissible in (1.3): d ≡ 3 (4), u | (d+1)/4, d | n + u.
(Explicitly C = (ℓ+1)/(4u), B = (n+u)/ℓ ≥ 1, and 4uBC − u − B = B(4uC − 1) − u = Bℓ − u = n.) ∎

Hence E(X) := {p ≤ X : R(p) = 0} ⊂ S(X, Q) := {n ≤ X : n mod ℓ ∉ Ω_ℓ for every prime ℓ ≤ Q}, for every Q.

### 3.2 The large sieve (Montgomery)

**Theorem (Montgomery 1968; Montgomery–Vaughan 1973).** Let S ⊂ [1, X] ∩ ℤ and suppose that for each prime ℓ ≤ Q the set S
avoids ω(ℓ) residue classes mod ℓ, with 0 ≤ ω(ℓ) < ℓ. Then
 |S| ≤ (X + Q²)/L(Q),  L(Q) := Σ_{q ≤ Q} μ²(q) Π_{ℓ | q} ω(ℓ)/(ℓ − ω(ℓ)).
(Reference form: Montgomery, *Topics in Multiplicative Number Theory*, LNM 227, Ch. 3, Thm 2 with N − 1 + Q² — we only use
X + Q².) Since ω(ℓ)/(ℓ − ω(ℓ)) ≥ ω(ℓ)/ℓ,
 L(Q) ≥ L₀(Q) := Σ_{q ≤ Q} μ²(q) ω(q)/q, ω multiplicative on squarefree q.              (3.1)

### 3.3 Dyadic Titchmarsh-type lower bound (needs Bombieri–Vinogradov)

**Lemma 3.2.** There is Y₀ such that for all Y ≥ Y₀:  A(Y) := Σ_{Y < ℓ ≤ 2Y, ℓ prime} ω(ℓ)/ℓ ≥ 1/25.

*Proof.* For every prime ℓ ∈ (Y, 2Y], ω(ℓ) ≥ #{d ≤ Y^{1/3} : 4d | ℓ + 1}: if ℓ ≢ 3 (mod 4) the right side is 0; otherwise
each such d is a divisor of (ℓ+1)/4. Hence
 Σ_{Y<ℓ≤2Y} ω(ℓ) ≥ Σ_{d ≤ Y^{1/3}} [π(2Y; 4d, −1) − π(Y; 4d, −1)].
Bombieri–Vinogradov: for A = 2 there is B = B(2) with Σ_{q ≤ x^{1/2}(log x)^{−B}} max_{(a,q)=1} max_{y ≤ x} |π(y;q,a) − li(y)/φ(q)| ≪ x(log x)^{−2}.
Apply it with x = 2Y and a = −1 (coprime to 4d); all moduli q = 4d ≤ 4Y^{1/3} are ≤ x^{1/2}(log x)^{−B} for Y large. Thus
 Σ_{Y<ℓ≤2Y} ω(ℓ) ≥ (li(2Y) − li(Y))·Σ_{d ≤ Y^{1/3}} 1/φ(4d) − O(Y/(log Y)²).
Now li(2Y) − li(Y) = ∫_Y^{2Y} dt/log t ≥ Y/log(2Y), and Σ_{d ≤ Y^{1/3}} 1/φ(4d) ≥ Σ_{d ≤ Y^{1/3}} 1/(4d) ≥ (1/4)·log(Y^{1/3}) = (log Y)/12.
So Σ_{Y<ℓ≤2Y} ω(ℓ) ≥ (Y/12)·(log Y/log 2Y) − O(Y/(log Y)²) ≥ Y/12.5 for Y ≥ Y₀, and A(Y) ≥ (1/(2Y))·Y/12.5 = 1/25. ∎

(Numerically A(2^j) ≈ 0.43 for j ≥ 15, `data/z56/famtry/c0_2pow29.txt` — its cumulative column omits ℓ = 3 and is not used;
the lemma's 1/25 is a crude but rigorous bound.
Using moduli up to Y^{1/2−ε} in BV would give 1/17; the true value is the Titchmarsh-type constant ≈ 0.43 — EVIDENCE.)

### 3.4 Lower bound for L(Q)

**Lemma 3.3.** Let c₀ ∈ (0, 1], j₀ ≥ 1, and suppose A_j := Σ_{2^j < ℓ ≤ 2^{j+1}} ω(ℓ)/ℓ ≥ c₀ for all j ≥ j₀. Then there is
Q₀ = Q₀(c₀, j₀) such that for Q ≥ Q₀,
 L(Q) ≥ exp( (√(2c₀)/(e√log 2))·√(log Q) − 3 ).

*Proof.* Put J := ⌊log₂ Q⌋ and let k ≥ 1, m ≥ k be integers with k(j₀ + m) ≤ J. For each k-subset T = {j₁ < … < j_k} of
I := {j₀, j₀+1, …, j₀+m−1} and each choice of primes ℓ_i ∈ (2^{j_i}, 2^{j_i+1}] (1 ≤ i ≤ k), the number q = ℓ₁⋯ℓ_k is
squarefree (the dyadic blocks are disjoint, so the primes are distinct) and q ≤ 2^{Σ(j_i+1)} ≤ 2^{k(j₀+m)} ≤ 2^J ≤ Q.
By unique factorisation, distinct pairs (T, (ℓ_i)) give distinct q. Hence by (3.1)
 L(Q) ≥ Σ_T Π_{i=1}^k A_{j_i} ≥ C(m, k)·c₀^k ≥ (m c₀/k)^k.
Choose k := ⌊√(c₀J/2)/e⌋ and m := ⌊J/k⌋ − j₀. For J ≥ J₀(c₀, j₀) we have k ≥ 1, m ≥ J/k − j₀ − 1 ≥ J/(2k) (as k ≤ J/(2(j₀+1))),
and m ≥ k (as J ≥ 2k²). Then m c₀/k ≥ c₀J/(2k²) ≥ e², so L(Q) ≥ e^{2k} ≥ exp(2√(c₀J/2)/e − 2) = exp((√(2c₀)/e)√J − 2).
Finally J ≥ log Q/log 2 − 1 gives √J ≥ √(log Q/log 2) − 1, and (√(2c₀)/e) ≤ 1, whence the claim. ∎

### 3.5 Proof of Theorem A

Take Q := √X. By Lemma 3.1, E(X) ∖ [1, Q] ⊂ S(X, Q) (we don't even need p > Q, but it costs nothing). By §3.2,
|S(X, Q)| ≤ 2X/L(Q). Lemma 3.2 gives the hypothesis of Lemma 3.3 with c₀ = 1/25 (and some j₀), so for X ≥ X₀
 |E(X)| ≤ √X + 2X·exp(3 − (√(2/25)/(e√log 2))·√(log √X)) = √X + 2e³·X·exp(−0.0884…·√log X) ≤ X·exp(−0.08√log X)
for X ≥ X₀ (the constant: √(2/25)/(e·√(log 2)) = 0.2828/(2.7183·0.8326) = 0.1250, divided by √2 for log Q = ½ log X gives 0.0884). ∎

**Remarks.** (i) The argument never uses that p is prime (only that the sifted integers are odd), and the sifted set
S(X, √X) contains all odd squares ≤ X (Lemma 1.3), so **no refinement of this sieve can push the bound below √X**; the
Montgomery bound (X + Q²)/L(Q) is also ≥ X/Q² ≥ 1 regardless — the sieve is structurally unable to give "all p".
(ii) The exponent ½ in exp(−c√log X) is the natural limit of the prime-modulus large sieve here: Σ_{ℓ ≤ t} ω(ℓ)/ℓ ≍ log t
(growing "dimension"), and Σ_{q≤Q} μ²(q)ω(q)/q = exp((1+o(1))·κ√log Q)-type for such ω. Numerically (`data/z56/famtry/L_1e8.txt`)
log L(Q)/√log Q ≈ 0.92–0.95 for Q = 10⁷–10⁸ and still rising slowly — versus 0.125 proved (for L(Q); 0.088 after Q = √X).
(iii) Composite moduli d ≡ 3 (4) in (1.3) carry τ((d+1)/4) further classes with Σ_{d≤Q} τ((d+1)/4)/d ≍ log²Q, which
heuristically would give exp(−c log²X) — but these class sets are not products of classes modulo the prime factors of d, so
neither Montgomery's inequality nor the Selberg sieve applies to them (the Cauchy–Schwarz lower bound
Σ_{a mod d}|S(a/d)|² ≥ d|S|²/(d − ω(d)) holds for every d, but after removing the non-reduced fractions no usable lower bound
for Σ*_{a mod d} survives; see §4.3). This is exactly where the "almost all" → "all" gap sits.
(iv) Concretely at X = 10⁸: L(10⁴) = 11.03, bound 2X/L ≈ 1.8·10⁷, whereas |S(10⁸, 10⁴) ∩ {primes ≡ 1 (4)}| ≤ 32 971
(`census_1e8.txt`, column R_sq = 0 counts primes with no hit at prime moduli ≤ √p, a superset) — the inequality is far
from tight at computable sizes, as expected.
(v) The constant: |E(X)| ≤ √X + 2e³X·exp(−0.0884√log X) is ≤ X·exp(−0.08√log X) only once exp(0.0084√log X) > 41, i.e.
log X > 2·10⁵; X₀ is in any case ineffective (BV). The statement is purely asymptotic.

## 4. Attempts at "every p" and where each one stops

### 4.1 What R(p) = 0 forces (PROVED; checked on the 14 known zeros, `data/z56/famtry/struct14.txt`)

**Lemma 4.1.** Let p be prime, p ≡ 1 (mod 4), R(p) = 0. Write S₄ := {n : every prime factor of n is ≡ 1 (mod 4)}. Then
 (a) p ≡ 1 (mod 24), p mod 7 ∈ {1, 2, 3, 4}, p mod 11 ∉ {8, 10}, p mod 15 ∉ {11, 13, 14}, p mod 19 ∉ {14, 18}, …
   (p mod d ∉ G_d for every d ≡ 3 (4));
 (b) (p+1)/2 ∈ S₄ (u = 1) and 4p + 1 ∈ S₄ (C = 1);
 (c) every prime factor of p + 2 is ≡ 1 or 3 (mod 8) (u = 2; note p + 2 ≡ 3 mod 8, so a factor ≡ 3 occurs);
 (d) 3 | 8p + 1 and every prime factor of 8p + 1 is ≡ 1 or 3 (mod 8) (C = 2);
 (e) with w = (p+3)/4 (odd): the prime factors of w all lie in {1, 5} or all in {1, 7} (mod 12) (u = 3);
 (f) in general, for every u ≥ 1 the set of divisors of p + u misses the class −1 (mod 4u), and for every C ≥ 1 the set of
   divisors of 4Cp + 1 misses −1 (mod 4C).

*Proof.* (a) p ≡ 5 (8) and p ≡ 2 (3) are Prop. 2.1; the rest is Lemma 1.4 for d = 7, 11, 15, 19. (b)–(f) are the
divisor forms (1.1)/Lemma 1.2 for the stated u or C; for (c)–(e) one lists the subset products in (ℤ/8)^×, (ℤ/12)^×:
e.g. in (c), 7 is a product of the classes present iff some factor is ≡ 7 or both 3 and 5 occur; the product of all factors
is ≡ 3, so "no 7 and not both 3, 5" ⟺ all factors in {1, 3}. (d): p ≡ 1 (3) ⇒ 3 | 8p + 1, and 3 ≡ 3 (8) excludes the
{1, 5} option. ∎

These are strong (each has density ≍ (log p)^{−1/2}-type), but the underlying no-hit conditions — (f) in full, and
"n mod d ∉ G_d for all d" in (a) — are **satisfied by every odd square n = m²** (Lemma 1.3); only the cosmetic
reformulations that use gcd(p, 6·7⋯) = 1 (such as "p ≡ 1 (mod 3)" or "3 | 8p + 1") fail for squares divisible by 3 or 7.
Hence no finite or infinite list of such local/factorisation conditions can ever be contradictory by itself.
**A proof must use a global property of p that squares lack.** The only such handle I see is the quadratic character
d ↦ (d | p): for p prime half of the d ≡ 3 (4) have (d | p) = −1 and then p mod d is one of the φ(d)/2 non-residues, of
which G_d is a subset of size τ((d+1)/4); for a square (d | m²) ∈ {0, +1} and G_d is unreachable. But "(d | p) = −1 for about half of all d" is far from forcing p mod d ∈ G_d for a single d (§4.2).

### 4.2 The genus/Jacobi handle (where it stops)

By Lemma 1.3 the hits are the pairs (d, u) with d ≡ 3 (4), (d | p) = −1, u | (d+1)/4, d | p + u. Fix a prime ℓ ≡ 3 (4)
with (ℓ | p) = −1. The residue p mod ℓ is a non-residue; it lies in G_ℓ for "probability" τ((ℓ+1)/4)/((ℓ−1)/2). One can
average this over ℓ (that is what the large sieve of §3 exploits, and also what gives M_gen-type main terms), but for a
*fixed* p there is no mechanism tying the actual residue p mod ℓ to the divisor set of (ℓ+1)/4: the map ℓ ↦ p mod ℓ (ℓ
over primes with (ℓ|p) = −1) is as "random" as anything in analytic number theory, and no equidistribution statement
in ℓ gives information for a single p beyond what the large sieve already extracts. I could not find any identity
linking p mod ℓ₁ and p mod ℓ₂ to (ℓ₁+1)/4, (ℓ₂+1)/4 (tried: ℓ₂ = (ℓ₁+1)/4·k − 1 chains — "if u | (ℓ₁+1)/4 then also
u | (ℓ₂+1)/4 when 4u | ℓ₂ + 1" — these only re-express that u is fixed and C varies, i.e. (1.1) with u fixed: p + u must
have a prime factor ≡ −1 (mod 4u); nothing forces it).

### 4.3 Consecutive integers p + 1, …, p + U

Form (1.1) with small u says: some p + u (u ≤ U) has a divisor ≡ −1 (mod 4u). Primes > U divide at most one of the
p + u, and heuristically each p + u has about one prime factor > U. But their classes mod 4u are unconstrained, and
squares m² show that *all* of m² + u (u ≤ U, any U) can avoid the class −1 (mod 4u). I found no inequality (e.g. of Erdős–Woods / "consecutive
integers with the same prime factors" type, or via Størmer/Pell) that distinguishes p from m² here. STOPS.

### 4.4 Sieve limits ((i), (ii) PROVED; (iii), (iv) are failed attempts, not theorems)

(i) Any sieve that uses only the hit classes (prime or composite moduli) bounds the full sifted set S(X, Q) of integers, and
|S(X, Q)| ≥ #{odd squares ≤ X} ≍ √X (Lemma 1.3). So no such argument can show that the exceptional *primes* are finite in
number; Montgomery's bound (X + Q²)/L(Q) with Q ≤ √X cannot even reach below X/Q² ≥ 1.
(ii) Prime moduli only: Σ_{ℓ ≤ t} ω(ℓ)/ℓ ≍ log t (lower bound Lemma 3.2; upper bound Σ_{ℓ≤t} τ((ℓ+1)/4) ≤ 2Σ_{d≤√t} π(t;4d,−1)
≪ t by Brun–Titchmarsh), so log L(Q) ≍ √log Q: the upper bound is Rankin's trick, Σ_{q ≤ Q} μ²(q)ω(q)/q ≤ Q^{σ} Π_ℓ (1 + ω(ℓ)/ℓ^{1+σ})
≤ exp(σ log Q + c/σ) with σ = √(c/log Q), and ω(ℓ)/(ℓ − ω(ℓ)) ≤ 2ω(ℓ)/ℓ for ℓ ≥ 7 changes only c. So Theorem A's shape is best
possible for this sieve; only the constant (0.08 proved vs ≈ 0.95/√2 observed at 10⁸, `L_1e8.txt`) can improve.
(iii) Composite moduli d ≡ 3 (4) carry non-product class sets (one class −u mod d per divisor u of (d+1)/4). Attempt: with
F(q) := Σ_{d|q} J(d), J(d) := Σ*_{a (d)} |Ŝ(a/d)|², Cauchy–Schwarz gives F(q) ≥ |S|²·q/(q − ω(q)) for *every* q with ω(q)
excluded classes; combining these with non-negative weights c_q and the large-sieve inequality Σ_{d ≤ Q} J(d) ≤ (X + Q²)|S|
requires Σ_{q ≤ Q, d | q} c_q ≤ 1 for all d > 1 and yields |S| ≤ (X+Q²)/Σ_q c_q ω(q)/(q−ω(q)). This is a linear programme;
I did not solve it, but with weights supported on primes it gives only Σ_ℓ ω(ℓ)/(ℓ−ω(ℓ)) ≍ log Q, and every composite
weight I tried helped less than that — i.e. this route is *worse* than Montgomery's multiplicative L(Q) = exp(≍√log Q),
because the multiplicative structure is what produces the products over several primes. I found no way to make either the large sieve or the Selberg Λ² sieve see
the composite classes; this is an unsolved obstacle, not a proved impossibility. STOPS.
(iv) Moment method (E[(R_Q − λ)^{2k}]/λ^{2k}) with composite moduli (sketch, not a theorem): the main terms look
manageable (shared prime factors are tempered by the compatibility condition u ≡ u′ (mod ℓ)), but the error terms need
Bombieri–Vinogradov weighted by τ(q)^{2k}, which I can only justify for fixed k, giving (log X)^{−2k}; k → ∞ with the
needed uniformity is out of reach. STOPS at polylog, worse than Theorem A.

### 4.5 Conditional routes considered

* Elliott–Halberstam / GRH do not change the picture: they improve c in Theorem A (moduli up to X^{1−ε}, better BV
  levels) but cannot remove the √X floor of §4.4(i).
* A Cramér-type hypothesis ("the residues −p mod ℓ, ℓ ≡ 3 (4), ℓ ≤ p, behave like independent uniform non-residues")
  would give R(p) ≥ 1 for all p ≥ p₀ with failure probability Σ_p exp(−c log²p) < ∞ — but this is a model, not a hypothesis
  one can state as a theorem input. Not pursued as a "CONDITIONAL" result because the hypothesis is not standard.

## 5. Status and what would be needed

| Claim | Status |
|---|---|
| R(n) = #{(d,u) : d ≡ 3 (4), u ∣ (d+1)/4, d ∣ n+u}; R(m²) = 0; (d ∣ p) = −1 at every hit | PROVED (§1) |
| p ≡ 5 (8), p ≡ 2 (3), p ≡ 5,6 (7) ⇒ R(p) ≥ 1; no finite covering of the primes ≡ 1 (8) by solvable classes | PROVED (§2) |
| #{p ≤ X : R(p) = 0} ≤ X exp(−0.08√log X) for X ≥ X₀ (ineffective, via BV) | PROVED (§3) |
| Same for #{odd n ≤ X with no hit at prime moduli ≤ √X} (contains all odd squares) | PROVED (§3) |
| R(p) ≥ 1 for all large p ≡ 1 (4) | OPEN — not proved here |
| 14 zeros ≤ 10⁸ (independent engine), R(m²) = 0 for all odd 3 ≤ m ≤ 9999 | CERTIFIED (`census_1e8.txt`) |
| sample mean R(p) ≈ 0.146 log²X over p ≤ 10⁸; A(2^j) ≈ 0.43; log L(Q)/√log Q ≈ 0.95 at Q = 10⁸ | EVIDENCE |

**Where it stops.** Every local condition implied by R(p) = 0 is shared with odd squares, and every sieve-type counting
argument is blind to the difference between a prime and a square at the level of X^{1/2}. The missing ingredient is a
*single-p* argument that exploits (d | p) = −1 for many d — i.e. a statement about the joint distribution of p mod ℓ over
primes ℓ with (ℓ | p) = −1 that is not an average over p. I know no tool that does this. If one only wants "all but
finitely many" from a *different* input, the cleanest sufficient statement is: for every large p there is a prime
ℓ ≡ 3 (mod 4), ℓ < p, with (−p mod ℓ) ∣ (ℓ+1)/4 (Lemma 1.4 restricted to prime d) — a Linnik-type assertion about the
sequence of least residues of −p, and the natural target for any future attempt.
