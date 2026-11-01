# Z53_UPPER — upper bounds for HC(p) (wave z53, lane UPPER)

Brief: `/home/pasky/projects/math/z52bbriefs/z53_upper.md`, retargeted mid-lane: **main goal HC(p) ≪ p^θ for some fixed
θ < 1 for all large primes p ≡ 1 (mod 4)**; polylog HC(p) ≤ (log p)^A is a bonus. Scripts `scripts/z53_upper_*`,
data `data/z53/upper/`.

Notation. p ≡ 1 (mod 4) prime. A *word* of p is (t, u, v) ∈ ℕ³ (ℕ = {1, 2, …}) with tuv − u − v = p.
𝒞_p := {x ∈ ℕ : x ≡ 0 (mod 4) or x ≡ −p (mod 8)}. HC(p) := least element of 𝒞_p that is a coordinate of a word of p
(∞ if none). By Theorem 1 of `LOWERTAIL_ROUND2_FABLE.md` §1.1, a word with a coordinate in 𝒞_p yields a solution of
4/p = 1/x + 1/y + 1/z. (·/p) is the Legendre symbol, (·/n) the Jacobi symbol for odd n > 0.

---------------------------------------------------------------------------------------------------------------------

## 0. Verdict

**The target is not proved.** The pointwise statement "HC(p) ≪ p^θ for all large p" (any θ < 1, a fortiori polylog)
implies the Erdős–Straus conjecture for every sufficiently large prime p ≡ 1 (mod 4) (Theorem 1 of LOWERTAIL_ROUND2_FABLE
§1.1), and by Lemma 1.2 below HC(p) < ∞ already forces HC(p) ≤ p − 1. So the retargeted goal is "HC(p) < ∞ for all
large p (which implies ES there), plus a saving of p^{1−θ} in the size of one coordinate"; it is at least as hard as ES
for large primes p ≡ 1 (4), which is open. I did not
find a pointwise argument, and §5 records exactly where the direct route stops and which statement would be needed.

What is proved here:

| # | statement | status |
|---|-----------|--------|
| L1.1 | c ∈ 𝒞_p is a coordinate ⟺ p + c or cp + 1 has a positive divisor ≡ −1 (mod c) | PROVED |
| L1.2 | every coordinate of every word of p is ≤ p + 2; so HC(p) < ∞ ⟹ HC(p) ≤ p + 2 | PROVED |
| L1.3 | words ⟷ pairs (m, e) with e ∣ m + 1, m ∣ p + e (u = e, t = (m+1)/e, v = (p+e)/m) | PROVED |
| P2.1 | HC(p) = 3 iff p ≡ 5 (mod 8); for p ≡ 1 (8): HC(p) ≥ 4, and HC(p) = 4 iff (p+4)(4p+1) has a prime factor ≡ 3 (mod 4) | PROVED |
| L3.1 | **reciprocity constraint**: every divisor d certifying a coordinate c ∈ 𝒞_p (as in L1.1) has (d/p) = −1 | PROVED |
| C3.2 | no certificate divisor is composed of primes dividing 2m when p ≡ 1 (mod 8m); no finite set of certificate divisors serves all p | PROVED |
| P3.3 | for infinitely many p every certificate divisor (any c) has a prime factor > (1/(1.02 L₀) − o(1)) log p (L₀ = Linnik exponent) | PROVED (Linnik) |
| **T4.1** | **for 0 < θ ≤ 1/2: #{p ≤ x : HC(p) > x^θ + 1} ≤ 16 x exp(−0.15 √(θ log x)) for x ≥ x₀(θ); hence HC(p) ≤ p^θ for all p ≤ x outside ≪_θ x exp(−0.1 √(θ log x)) primes** | PROVED (Bombieri–Vinogradov, ineffective x₀) |
| T4.2 | for fixed K: #{p ≤ x : HC(p) > 4K} ≪_K x (log x)^{−1−κ(K)}, κ(K) = 2Σ_{k≤K} 1/φ(4k) ≥ log(K+1) | PROVED |
| T4.3 | polylog bonus: #{p ≤ x : HC(p) > (log x)^A} ≪_{A,ε} x exp(−(1−ε) A (log log x)²) | PROVED (Siegel–Walfisz, ineffective) |
| §5 | the exact pointwise statement needed; why congruence data and prime-level certificates cannot suffice | PROVED parts + EVIDENCE |
| §6 | HC(p) ≤ 64 for all primes p ≡ 1 (4) below 10⁸; lemma checks; prime-level statistics | CERTIFIED |

So the brief's "weaker milestone" is reached in the *exceptional-set* form: HC(p) ≤ p^θ for every fixed θ > 0 outside a
set of relative density ≪ exp(−c√(θ log x)) (T4.1), and HC(p) ≤ (log p)^A outside a set of relative density
exp(−(1−ε)A(log log x)²) (T4.3). The exceptional sets are explicit (they are contained in the explicit sieve-survivor sets
𝒮 of §4). Comparison: Vaughan (1970) proved that ES fails for ≪ x exp(−c (log x)^{2/3}) integers n ≤ x — a better rate,
but with no control of the size of a 𝒞-coordinate (I have not checked whether his solutions have one).

---------------------------------------------------------------------------------------------------------------------

## 1. Lines (PROVED)

**Lemma 1.1.** Let c ∈ ℕ, c ≥ 2.
(U) c is the u-coordinate (equivalently, by the symmetry (t,u,v) ↦ (t,v,u), the v-coordinate) of some word of p iff
p + c has a positive divisor d ≡ −1 (mod c). The word is (t, u, v) = ((d+1)/c, c, (p+c)/d).
(T) c is the t-coordinate of some word iff cp + 1 has a positive divisor d ≡ −1 (mod c). The word is
(c, (d+1)/c, ((cp+1)/d + 1)/c).

*Proof.* (U) tcv − c − v = p ⟺ v(tc − 1) = p + c. If (t, c, v) is a word, d := tc − 1 ≥ c − 1 ≥ 1 is a divisor of p + c
with d ≡ −1 (mod c). Conversely, given such d, t := (d+1)/c ∈ ℕ (d + 1 is a positive multiple of c) and
v := (p+c)/d ∈ ℕ satisfy v(tc−1) = p + c. (T) (cu − 1)(cv − 1) = c(cuv − u − v) + 1, so cuv − u − v = p ⟺
(cu−1)(cv−1) = cp + 1. A word gives the divisor d = cu − 1 ≡ −1 (mod c), d ≥ c − 1 ≥ 1. Conversely given d, put
e := (cp+1)/d; de ≡ 1 and d ≡ −1 (mod c) give e ≡ −1 (mod c), e ≥ 1, so u := (d+1)/c and v := (e+1)/c are in ℕ and
(cu−1)(cv−1) = cp + 1. ∎

So HC(p) = min{c ∈ 𝒞_p : (U) or (T) holds for c}. (1, 2 ∉ 𝒞_p: 1, 2 ≢ 0 (4), and −p is odd and ≢ 1 (8) since p ≢ 7 (8).)

**Lemma 1.2.** Every coordinate of every word of p is ≤ p + 2. Hence HC(p) < ∞ implies HC(p) ≤ p + 2.

*Proof.* t = (p + u + v)/(uv) ≤ p + 1/v + 1/u ≤ p + 2. By the symmetry u ↔ v assume u ≤ v; it suffices to show
v ≤ p + 2. From v(tu − 1) = p + u ≤ p + v we get v(tu − 2) ≤ p. If tu ≥ 3 this gives v ≤ p. tu = 1 is impossible
(then tuv − u − v = −1). If tu = 2, (t, u) ∈ {(1, 2), (2, 1)} and v = p + 2 resp. v = p + 1. ∎

**Lemma 1.3 (all words).** The map (t, u, v) ↦ (m, e) := (tu − 1, u) is a bijection from words of p onto pairs
(m, e) ∈ ℕ² with e ∣ m + 1 and m ∣ p + e; the inverse is (m, e) ↦ ((m+1)/e, e, (p+e)/m).

*Proof.* For a word, tu ≥ 2 (else tuv − u − v = −1), so m ≥ 1; e = u ∣ tu = m + 1; and v·m = p + u by the proof of
L1.1(U). Conversely the triple ((m+1)/e, e, (p+e)/m) is in ℕ³ and t·u·v − u − v = (m+1)v − e − v = mv − e = p. The two
maps are mutually inverse. ∎

In particular (m prime, the mechanism of §4): **if q is a prime, e ∣ q + 1 and q ∣ p + e, then
((q+1)/e, e, (p+e)/q) is a word; if e ∈ 𝒞_p (e.g. 4 ∣ e) then HC(p) ≤ e ≤ q + 1.**

---------------------------------------------------------------------------------------------------------------------

## 2. Small values (PROVED)

**Proposition 2.1.** (i) HC(p) ≥ 3 for all p, and HC(p) = 3 iff p ≡ 5 (mod 8).
(ii) If p ≡ 1 (mod 8) then HC(p) ≥ 4, and HC(p) = 4 iff (p + 4)(4p + 1) has a prime factor ≡ 3 (mod 4).
(iii) If a prime q ≡ 3 (mod 4) divides p + 1 then HC(p) ≤ q + 1.

*Proof.* (i) 1, 2 ∉ 𝒞_p (above). 3 ∈ 𝒞_p iff 3 ≡ −p (8) iff p ≡ 5 (8). For p ≡ 5 (8), p + 3 is even, d = 2 ≡ −1 (mod 3),
so L1.1(U) gives the word (1, 3, (p+3)/2). (ii) For p ≡ 1 (8): 3 ∉ 𝒞_p, 4 ∈ 𝒞_p. p + 4 and 4p + 1 are odd and ≡ 1 (mod 4);
an odd number has a divisor ≡ 3 (mod 4) iff it has a prime factor ≡ 3 (mod 4) (a product of primes ≡ 1 (4) is ≡ 1 (4)).
Apply L1.1 with c = 4. (iii) L1.3 with m = q, e = q + 1 (e ∣ q + 1, q ∣ p + q + 1): the word (1, q+1, (p+q+1)/q) has
u = q + 1 ≡ 0 (mod 4). ∎

---------------------------------------------------------------------------------------------------------------------

## 3. The reciprocity constraint (PROVED)

Call d a **certificate divisor** of p (for c) if c ∈ 𝒞_p, c < p, and d is a positive divisor of p + c or of cp + 1 with
d ≡ −1 (mod c) — i.e. d witnesses c as a coordinate in L1.1.

**Lemma 3.1.** Every certificate divisor d of p satisfies (d/p) = −1.

*Proof.* gcd(d, p) = 1: if p ∣ d ∣ p + c then p ∣ c < p, impossible; p ∤ cp + 1. Also gcd(d, c) = 1 since d ≡ −1 (mod c).
Write d = 2^a d′, d′ odd. Since p ≡ 1 (mod 4), Jacobi reciprocity gives (d′/p) = (p/d′), so
(d/p) = (2/p)^a (p/d′). In case (U), p ≡ −c (mod d′); in case (T), cp ≡ −1 (mod d′), so p ≡ −c^{−1} and
(p/d′) = (−c^{−1}/d′) = (−c/d′) (as (c^{−1}/d′)(c/d′) = 1). In both cases **(d/p) = (2/p)^a (−c/d′).**

*Case 4 ∣ c,* c = 4k. Then d ≡ −1 (mod 4) is odd, a = 0, d′ = d, and (−c/d) = (−1/d)(k/d) = −(k/d). Write k = 2^b k′,
k′ odd. If b ≥ 1 then 8 ∣ c ∣ d + 1, d ≡ 7 (mod 8), (2/d) = 1. By reciprocity, since d ≡ 3 (mod 4),
(k′/d) = (d/k′)(−1)^{(k′−1)/2}, and d ≡ −1 (mod k′) gives (d/k′) = (−1/k′) = (−1)^{(k′−1)/2}; so (k′/d) = 1. Hence
(k/d) = 1 and (d/p) = −1.

*Case c odd,* c ≡ −p (mod 8), so c ≡ 3 (mod 4) (c ≡ 7 (8) if p ≡ 1 (8); c ≡ 3 (8) if p ≡ 5 (8)). Then
(−c/d′) = (−1/d′)(c/d′) = (−1)^{(d′−1)/2} · (d′/c)(−1)^{((c−1)/2)((d′−1)/2)} = (d′/c), because (c−1)/2 is odd.
From 2^a d′ = d ≡ −1 (mod c) and multiplicativity of (·/c): (2/c)^a (d′/c) = (−1/c) = −1, so (d′/c) = −(2/c)^a. Hence
(d/p) = −((2/p)(2/c))^a. If p ≡ 1 (8) and c ≡ 7 (8): (2/p) = (2/c) = 1. If p ≡ 5 (8) and c ≡ 3 (8): (2/p) = (2/c) = −1.
In both cases (2/p)(2/c) = 1 and (d/p) = −1. ∎

(For coprime words this is the content of Theorem A of FOREST_DEEP_FABLE, (uv/p) = −1, read on the divisor: in case (U),
dv = p + c gives (d/p)(v/p) = (c/p).) CERTIFIED: 45 499 504 certificate divisors (all c ≤ 64, all p ≤ 2·10⁷), 0
violations (§6).

**Corollary 3.2 (no congruence covering).** Let m ∈ ℕ and p ≡ 1 (mod 8m). Then no certificate divisor of p has all its
prime factors in {primes dividing 2m}. In particular for every finite set D ⊂ ℕ there are infinitely many primes p
(all p ≡ 1 mod 8·lcm(D), Dirichlet) for which no d ∈ D is a certificate divisor, for any c.

*Proof.* (2/p) = 1 as p ≡ 1 (8); for odd primes ℓ ∣ m, (ℓ/p) = (p/ℓ) = (1/ℓ) = 1. So (d/p) = 1 for such d, contradicting
L3.1. ∎

**Proposition 3.3 (smooth certificates are blocked at scale log p).** Let L₀ be any admissible Linnik exponent (least
prime ≡ 1 (mod M) is ≤ C₀ M^{L₀}; L₀ = 5.5 is admissible, Heath-Brown 1992). There are infinitely many primes p ≡ 1 (mod 8)
such that every certificate divisor of p (for every c) has a prime factor ℓ > Y with Y ≥ log p/(1.02 L₀) − O(1).

*Proof.* For Y ≥ 3 let M = 8∏_{ℓ ≤ Y} ℓ ≤ 8e^{1.02Y} (Chebyshev/Rosser–Schoenfeld θ(Y) < 1.02Y) and take p ≡ 1 (mod M),
p ≤ C₀M^{L₀} (Linnik). By L3.1 a certificate divisor d has (d/p) = −1, so some prime ℓ ∣ d has (ℓ/p) = −1; by C3.2
(m = ∏_{ℓ≤Y} ℓ), ℓ > Y. log p ≤ log C₀ + L₀(log 8 + 1.02Y). The primes obtained are > M → ∞, so infinitely many. ∎

Meaning: for infinitely many p, every certificate divisor (for every c, of any size) has a prime factor larger than
≍ log p; a pointwise argument cannot get by with certificate divisors supported on the primes ≤ Y ≍ log p (nor on any
fixed finite set of primes, C3.2). This is the reciprocity form of the "square classes" (Mordell–Schinzel) obstruction,
written for the HC lines. (It is *not* a claim about all congruence-based reasoning: p itself is determined by its
residue modulo 2^{⌈log₂ p⌉+1}, say.)

---------------------------------------------------------------------------------------------------------------------

## 4. Exceptional sets (PROVED)

Tool: **Montgomery's arithmetic large sieve** (Montgomery 1968; Montgomery–Vaughan 1973; Iwaniec–Kowalski Thm 7.14).
Let 𝒩 be a set of integers in an interval of length N; suppose for each prime q ≤ Q a set Ω_q of ω(q) < q residue classes
mod q is given (Ω_q = ∅ allowed) with n mod q ∉ Ω_q for all n ∈ 𝒩. Then
  |𝒩| ≤ (N + Q²)/L,  L := Σ_{d ≤ Q} μ²(d) ∏_{q ∣ d} g(q),  g(q) := ω(q)/(q − ω(q)).

### 4.1 The p^θ theorem

For a prime q put E_q := {e ∈ ℕ : 4 ∣ e, e ∣ q + 1} (empty unless q ≡ 3 (mod 4)), τ*(q) := |E_q|,
Ω_q := {−e mod q : e ∈ E_q}.

*Distinctness.* Elements of E_q lie in [4, q+1]; −e ≡ −e′ (mod q) with 4 ≤ e < e′ ≤ q + 1 would force q ∣ e′ − e ∈ [1, q−3].
So ω(q) = τ*(q). Also τ*(q) < q: τ*(2) = 0, τ*(3) = 1, and τ*(q) ≤ τ(q+1) ≤ 2√(q+1) < q for q ≥ 7 (q = 5: τ* = 0).

*Sieve property.* If p ≡ −e (mod q) for some e ∈ E_q, then q ∣ p + e, e ∣ q + 1, and by L1.3 the word
((q+1)/e, e, (p+e)/q) has u = e ∈ 4ℕ ⊂ 𝒞_p: HC(p) ≤ e ≤ q + 1. Hence if HC(p) > Q + 1 then p mod q ∉ Ω_q for every prime
q ≤ Q. (No condition p > q is needed.)

**Lemma 4.1 (Bombieri–Vinogradov input).** There are an absolute y* and c₁ = 1/20 such that for y ≥ y*:
  S(y) := Σ_{q ≤ y prime} τ*(q)/q ≥ c₁ log y.

*Proof.* Let T be large and B_T := Σ_{T<q≤2T} τ*(q)/q. Every e ∈ ℕ with 4 ∣ e and e ∣ q + 1 lies in E_q, so
  B_T ≥ (1/2T) Σ_{e ≤ T^{1/3}, 4∣e} (π(2T; e, −1) − π(T; e, −1)).
Bombieri–Vinogradov (A = 2): Σ_{m ≤ T^{1/2}(log T)^{−B}} max_{(a,m)=1} max_{y ≤ 2T} |π(y; m, a) − li(y)/φ(m)| ≪ T/(log T)²;
T^{1/3} is in range for large T. Hence the inner sum is ≥ (li(2T) − li(T)) Σ_{e} 1/φ(e) − O(T/log²T). Now
li(2T) − li(T) ≥ T/log 2T, and with e = 4k, φ(4k) ≤ 2k, Σ_{k ≤ K} 1/k ≥ log K:
Σ_{e ≤ T^{1/3}, 4∣e} 1/φ(e) ≥ (1/2) log(T^{1/3}/4). So B_T ≥ (1/(2 log 2T))·((1/6) log T − log 2) − O(1/log² T)
= 1/12 − O(1/log T) ≥ 1/13 for T ≥ T₀. Summing B_T over T = y/2^j, j = 1, …, J with y/2^J ≥ √y (J ≥ (log₂ y)/2 − 1
blocks, all disjoint, all with T ≥ √y ≥ T₀): S(y) ≥ ((log y)/(2 log 2) − 1)/13 ≥ (1/20) log y for y ≥ y*. ∎

**Lemma 4.2 (elementary symmetric functions).** For a_i ≥ 0 with S = Σ a_i, T = Σ a_i², and r ≥ 2:
r! e_r(a) ≥ S^r − (r choose 2) T S^{r−2}.

*Proof.* S^r = Σ over ordered r-tuples of indices of ∏ a. Tuples with distinct entries contribute exactly r! e_r. Every
other tuple has i_j = i_k for some pair j < k; for a fixed pair the sum over such tuples is T·S^{r−2}; a union bound over
the (r choose 2) pairs bounds the rest. ∎

**Theorem 4.1.** Let 0 < θ ≤ 1/2. For x ≥ x₀(θ):
  #{p ≤ x prime, p ≡ 1 (4) : HC(p) > x^θ + 1} ≤ 16 · x · exp(−0.15 √(θ log x)).
Consequently, for every θ ∈ (0, 1), #{p ≤ x prime, p ≡ 1 (4) : HC(p) > p^θ} ≪_θ x exp(−0.1 √(θ log x)).

*Proof.* Q := x^θ ≤ √x, N := x, 𝒩 := {p ≤ x prime, p ≡ 1 (4) : HC(p) > Q + 1}. By the sieve property and the large sieve,
|𝒩| ≤ (x + Q²)/L ≤ 2x/L. Put a_q := τ*(q)/q ≤ g(q). For r ≥ 2 and y_r := Q^{1/r}, every product of r distinct primes
≤ y_r is a squarefree d ≤ Q, and all terms of L are ≥ 0, so L ≥ e_r(a_q : q ≤ y_r). Put T₀ := Σ_{n≥4} τ(n)²/(n−1)²
≤ (16/9)ζ(2)⁴/ζ(4) < 12.1 (τ*(q)² ≤ τ(q+1)², q² ≥ (q+1−1)², and (n/(n−1))² ≤ 16/9 for n ≥ 4); then Σ a_q² ≤ T₀.
Let Λ := c₁ θ log x and r := ⌊√Λ/2⌋ (≥ 2 for large x). Then log y_r = θ log x/r ≥ 2√(θ log x/c₁) → ∞, so for
x ≥ x₀(θ) Lemma 4.1 gives S := Σ_{q ≤ y_r} a_q ≥ c₁ log y_r = Λ/r. Since r ≤ √Λ/2, S²/r² ≥ Λ²/r⁴ ≥ 16 > T₀, hence
(r choose 2) T₀ S^{r−2} ≤ (r²T₀/(2S²)) S^r ≤ S^r/2 and Lemma 4.2 gives e_r ≥ S^r/(2·r!) ≥ (S/r)^r/2 ≥ (Λ/r²)^r/2 ≥ 4^r/2
(r! ≤ r^r; Λ/r² ≥ 4). With r ≥ √Λ/2 − 1: L ≥ 2^{2r−1} ≥ 2^{√Λ − 3} = exp((log 2)√Λ)/8.
√Λ = √(c₁)√(θ log x) ≥ 0.2236 √(θ log x), and (log 2)·0.2236 > 0.15. So |𝒩| ≤ 2x/L ≤ 16 x exp(−0.15 √(θ log x)).
For the consequence (any θ ∈ (0,1)): a prime p ∈ (2√x, x] with HC(p) > p^θ has HC(p) > (2√x)^θ ≥ x^{θ/2} + 1, so it
lies in the set of the theorem with parameter θ/2 ∈ (0, 1/2); the primes ≤ 2√x are O(√x). 0.15/√2 > 0.1. ∎

Remarks. (a) x₀(θ) is ineffective (Bombieri–Vinogradov rests on Siegel's theorem); a Brun–Titchmarsh/Siegel–Walfisz
version with moduli ≤ (log y)^N gives only a (log log)² exponent, cf. T4.3. (b) Only u-coordinates in 4ℕ and *prime*
moduli m = q of L1.3 were used; the excluded classes all lie among the quadratic non-residues mod q (L3.1), about
τ(q+1) of the (q−1)/2. The √log rate looks like the natural limit of a prime-modulus large sieve with ω(q) ≈ τ(q+1) classes
(heuristically this L is itself exp(O(√log Q)); not proved); improving it presumably needs composite moduli m in L1.3,
whose excluded classes are not of CRT-product form. (c) The exceptional set is contained in the explicit set
𝒮_θ(x) := {p ≤ x : for every prime q ≤ x^θ, (−p mod q) ∤ q + 1 or 4 ∤ (−p mod q)} (with −p mod q taken in [1, q]).

### 4.2 Fixed K and the polylog window

For K ∈ ℕ and a prime q > 16K² let τ_K(q) := #{k ≤ K : 4k ∣ q + 1} and
  Ω_q := {0} ∪ {−4k mod q : 4k ∣ q+1, k ≤ K} ∪ {−(4k)^{−1} mod q : 4k ∣ q+1, k ≤ K}.
If p ≡ −4k (q) with 4k ∣ q + 1, L1.1(U) with d = q gives c = 4k as a coordinate; if p ≡ −(4k)^{−1} (q), then q ∣ 4kp + 1
and L1.1(T) gives c = 4k. So for primes p > q with HC(p) > 4K, p mod q ∉ Ω_q. The 1 + 2τ_K(q) classes are distinct:
−4k ≡ −4k′ forces k = k′ (4k, 4k′ < q); −4k ≡ −(4k′)^{−1} forces q ∣ 16kk′ − 1 ∈ [15, 16K² − 1]; inverses likewise; and 0
differs from all. ω(q) = 1 + 2τ_K(q) ≤ 1 + 2K < q/2, so g(q) ≤ 2ω(q)/q.

κ(K) := 2Σ_{k≤K} 1/φ(4k) ≥ Σ_{k≤K} 1/k ≥ log(K+1) (φ(4k) ≤ 2k). (Asymptotically κ(K) ~ (2/3)(ζ(2)ζ(3)/ζ(6)) log K
≈ 1.296 log K, from Σ_{n≤y}1/φ(n) ~ (ζ(2)ζ(3)/ζ(6)) log y split by the 2-adic valuation; not needed.)

**Rankin step (used in T4.2, T4.3).** Let P be a set of primes in (16K², z], Π := ∏_{q∈P} q, z ≤ Q, σ := 1/log z, and
suppose Σ_{q∈P} g(q) log q ≤ G log z. Then
  L ≥ Σ_{d ∣ Π, d ≤ Q} g(d) ≥ ∏_{q∈P}(1 + g(q)) · (1 − exp(−log Q/log z + (e−1)G)).
*Proof.* Σ_{d∣Π, d>Q} g(d) ≤ Q^{−σ} Σ_{d∣Π} g(d) d^σ = Q^{−σ} ∏(1 + g(q)q^σ), and
1 + g q^σ ≤ (1 + g)(1 + g(q^σ − 1)) ≤ (1+g) exp(g (e−1) σ log q) because q^σ − 1 ≤ (e−1)σ log q for σ log q ∈ [0, 1]. ∎
So with z := Q^{1/s}, s := (e−1)G + 1, L ≥ (1 − 1/e) ∏_{q∈P}(1 + g(q)) ≥ (1−1/e) exp(Σ_P ω(q)/q − Σ_P g(q)²/2)
(log(1+y) ≥ y − y²/2, g ≥ ω/q). And Σ_{q>16K²} g(q)² ≤ 4(1+2K)²Σ_{n>16K²} n^{−2} ≤ 36K²/(16K² − 1) ≤ 2.4.

**Theorem 4.2.** For fixed K ≥ 1: #{p ≤ x prime : HC(p) > 4K} ≪_K x (log x)^{−1−κ(K)}.

*Proof.* Q = √x, P = primes in (16K², z]. G: Σ_{q≤z} g(q) log q ≤ (2 + 4K) Σ_{q ≤ z} log q/q ≤ (4 + 8K) log z (Mertens,
z ≥ z₀); s = (e−1)(4+8K) + 1 depends on K only. Mertens in progressions for the fixed moduli 4k ≤ 4K:
Σ_{q ∈ P} ω(q)/q = Σ_{q∈P} 1/q + 2Σ_{k≤K} Σ_{q∈P, q≡−1 (4k)} 1/q = (1 + κ(K)) log log z − O_K(1), and
log log z = log log x − log(2s). So L ≫_K (log x)^{1+κ(K)}; the primes p ≤ Q are ≤ √x. ∎

So HC(p) ≤ 4K for all p outside an explicit set of relative density ≪_K (log x)^{−κ(K)} with κ(K) ≥ log(K+1): for
every B, HC(p) ≤ 4⌈e^B⌉ outside ≪_B π(x)(log x)^{−B} primes.

**Theorem 4.3 (polylog window).** For A > 0, 0 < ε < 1 (for ε ≥ 1 the bound is trivial): #{p ≤ x : HC(p) > (log x)^A} ≪_{A,ε} x exp(−(1 − ε)A (log log x)²).

*Proof.* K := ⌊(log x)^A/4⌋, Q = √x, κ := κ(K) ≥ log K = A log log x − O(1); κ ≤ 2Σ_{k≤K}1/k ≤ 2 log K + 2.
*Upper bound G.* For m = 4k ≤ 4K and t > 16K² ≥ m², Brun–Titchmarsh (Montgomery–Vaughan) π(t; m, a) ≤ 2t/(φ(m) log(t/m))
≤ 4t/(φ(m) log t); partial summation gives Σ_{16K² < q ≤ z, q ≡ −1 (m)} (log q)/q ≤ 4(1 + log z)/φ(m). Hence
Σ_P ω(q) log q/q ≤ 2 log z + 2Σ_k 4(1+log z)/φ(4k) ≤ (2 + 8κ) log z, G ≤ 4 + 16κ, s ≤ 28κ + 8 = O(A log log x).
*Lower bound.* Siegel–Walfisz with exponent N := ⌈2A/ε⌉: π(t; m, a) = li(t)/φ(m) + O_N(t exp(−c_N√log t)) for
m ≤ (log t)^N. For m = 4k put y₁(m) := max(16K², exp(m^{1/N})); partial summation gives
Σ_{y₁ < q ≤ z, q ≡ −1 (m)} 1/q ≥ (log log z − log log y₁)/φ(m) − O_N(exp(−(c_N/2) m^{1/(2N)})).
log log y₁ ≤ max(log(3 + 2 log K), (1/N) log 4K) ≤ (ε/2) log log x + O(1) for large x. Summing 2× over k ≤ K (the error
terms sum to O_N(1)): Σ_P ω(q)/q ≥ κ (log log z − (ε/2) log log x − O(1)) − O_N(1), with
log log z = log log x − log(2s) = log log x − O(log log log x). So Σ_P ω/q ≥ (1 − ε/2 − o(1)) A (log log x)², and
L ≥ (1−1/e) e^{−1.2} exp((1 − ε/2 − o(1)) A (log log x)²). The large sieve, applied to the primes p ∈ (Q, x] (Ω_q ∋ 0, so p = q must be excluded; the primes ≤ Q add
O(√x)), gives the claim (z ≥ y₁ holds since
log z = log x/(2s) ≫ (log x)/(log log x) while log y₁ ≤ (log x)^{A/N} + O(log log x)). ∎

---------------------------------------------------------------------------------------------------------------------

## 5. The pointwise problem: where the direct route stops

### 5.1 What has to be shown (exact statement)

By L1.1, the target T_θ is literally:

> **(S_θ)** For every sufficiently large prime p ≡ 1 (mod 8) there is c ∈ 𝒞_p, c ≤ p^θ, such that p + c or cp + 1 has a
> positive divisor d ≡ −1 (mod c). (p ≡ 5 (8) is done by P2.1.)

Equivalently (L1.3): there is a modulus m ∈ ℕ and e ∣ m + 1 with m ∣ p + e such that e or (m+1)/e lies in 𝒞_p ∩ [1, p^θ]
(the third coordinate (p+e)/m could also be the small 𝒞-element). By L1.2, "≤ p^θ" may be replaced by "< ∞" at the cost
of θ = 1; S_1 is "HC(p) < ∞ for all large p", which implies ES for all large p ≡ 1 (4) (the converse — every
ES-soluble p has a word with a 𝒞_p-coordinate — is not used or proved here). Since p, p + 1, p + 2 ∉ 𝒞_p, L1.2 even gives
HC(p) < ∞ ⟹ HC(p) ≤ p − 1.

### 5.2 Why each natural route stops (PROVED statements + EVIDENCE)

1. **Fixed c is a single-integer divisor-in-class problem.** For fixed c the line is "p + c (or cp + 1) has a divisor
   ≡ −1 (mod c)"; it fails whenever p + c and cp + 1 are prime (or products of primes in a subgroup of (ℤ/c)^× missing −1).
   No unconditional statement controls the factorisation of p + c for a *given* p, so the argument must use the growing
   family {p + c, cp + 1 : c ≤ p^θ}.
2. **Small-prime certificates are provably insufficient** (C3.2, P3.3): for any fixed finite set of primes, and for
   the primes up to ≍ log p, there are infinitely many p where no certificate divisor is supported on those primes. So a
   proof of S_θ must produce certificate divisors with prime factors > (log p)/(1.02 L₀) − O(1) for such p; it cannot
   consist of finitely many fixed-divisor congruence families.
3. **Prime-level certificates do not cover all tested primes** (the mechanism of T4.1 alone does not even work
   pointwise in the tested range). EVIDENCE (`data/z53/upper/primecert_1e8.txt`): among the 1 439 970 primes p ≡ 1 (8) below 10⁸, 760 have no
   prime q < p with q ∣ p + e, e ∣ q + 1, 4 ∣ e (the T4.1 mechanism), and 4 (p = 3361, 66529, 1095481, 85664329) have no
   prime-level certificate of *any* 𝒞-type (e or (q+1)/e ∈ 𝒞_p), although their HC is 7, 8, 15, 15 — witnessed by
   composite divisors, e.g. 7·3361 + 1 = 34·692 with 34 ≡ −1 (mod 7). Tail
   statistics (Q₄, Q_C := least prime q giving a prime-level certificate of the respective type): the Q_C tail
   #{p : Q_C(p) ≥ 2^b} roughly halves per doubling of 2^b; the Q₄ tail decays more slowly (ratios ≈ 0.68–0.71 per
   doubling at b = 10…13). The data *suggest* (not proved) that infinitely many p have no prime-level certificate with
   q < p, in which case a pointwise proof must exploit composite divisors d of p + c / cp + 1, i.e. *how several prime
   factors of one shifted integer combine in (ℤ/c)^×*.
4. **The sieve itself is not pointwise**: Montgomery's sieve bounds the *number* of survivors; it cannot show that a
   given p is not a survivor, and by item 3 survivors of the prime-level sieve with q < p exist in the tested range.
5. **Least non-residue tools do not directly help.** L3.1 needs (d/p) = −1, and Burgess provides a prime
   ℓ ≤ p^{1/(4√e)+ε} with (ℓ/p) = −1. But a certificate with d = ℓ needs p ≡ −e (mod ℓ) for one of the ≤ τ(ℓ+1)
   admissible e, a set of size ℓ^{o(1)} inside the (ℓ−1)/2 non-residues, with no interval or algebraic structure that
   the known character-sum estimates (Burgess, Weil) could exploit to force a hit. With composite d the needed event is
   again "p mod d in a sparse divisor-defined set".

### 5.3 The weakest statement that would suffice (and what I could prove about it)

The cleanest sufficient statement suggested by 5.2.3 is a **divisor-subproduct statement**: for N ∈ ℕ and c ≥ 3 coprime
to N let Σ_c(N) ⊂ (ℤ/c)^× be the set of classes of the positive divisors of N (= subproducts of the multiset of classes of
the prime factors of N, with multiplicity). Then S_θ ⟺ "∃ c ∈ 𝒞_p ∩ [3, p^θ] with −1 ∈ Σ_c(p + c) ∪ Σ_c(cp + 1)".
A zero-sum/additive-combinatorics route would need a precise theorem of the form "a sequence in a finite abelian group
G that is long and *not concentrated on a proper subgroup or its cosets* has all of a subgroup H ∋ −1 among its subproducts".
Length plus bounded multiplicity alone is not enough (referee's example: in (ℤ/52)^× of order 24, four copies of each
element of H₀ = {1, 3, 9, 27, 29, 35} plus one 15 has length 25, multiplicity ≤ 4, generates the group, yet all
subproducts lie in H₀ ∪ 15H₀ ∌ −1). One *stronger* sufficient condition would then be: *for some c ≤ p^θ with small
φ(c) (c = 4, 8, 12, …), p + c or cp + 1 has ≳ φ(c) prime factors whose classes are spread (not concentrated on a coset
structure missing −1).* That is a lower bound on ω(p + c) for a
single p and some small c, which is out of reach (Sylvester–Schur-type theorems give one large prime factor per block of
consecutive integers, not many prime factors of one), and P2.1(ii) shows that already c = 4 is exactly "p + 4 or 4p + 1
has a prime factor ≡ 3 (mod 4)" — a statement that fails for ≈ 8.7% of the primes p ≡ 1 (8) below 10⁸ (125 059 of
1 439 970; Landau-type heuristic ≍ 1/log p, T4.2 upper bound ≪ (log x)^{−1} relative density). I could not prove any instance of the subproduct statement pointwise.

### 5.4 Heuristic size (EVIDENCE, not used)

The expected number of pairs (c, d) witnessing a coordinate c ≤ X is ≍ log X · log p (divisor counting in the classes
−1 mod c, Σ_{c ≤ X} τ(N_c)/φ(c)). A Dickson-type model — all of p + c, cp + 1 (c ∈ 𝒞_p, c ≤ X) equal to their forced
small-prime parts times a single large prime, the small parts chosen admissibly so that no certificate arises from
them (literal simultaneous primality is impossible: odd c ∈ 𝒞_p makes both even, and 3 divides p + 4 or p + 8 for every
prime p > 3, …) — has probability ≈ (log p)^{−c′X} for some c′ > 0, summable over p once X ≳ log p/log log p. So the
natural CONJECTURE is HC(p) ≪ log p (or a bit less) in the worst case; data: HC(p) ≤ 64 for p < 10⁸ (§6). In particular any θ > 0 is a huge margin heuristically; the
difficulty of T_θ is entirely the pointwise nature, not the window.

---------------------------------------------------------------------------------------------------------------------

## 6. Computations (CERTIFIED)

`scripts/z53_upper_hc.c` (Miller–Rabin + Pollard rho; HC via L1.1 over c ∈ 𝒞_p ascending):
- all 2 880 504 primes p ≡ 1 (4), p ≤ 10⁸: HC(p) ≤ 64, record HC = 64 at p = 21 841 (word (64, 9, 38));
  histogram 3:1 440 534, 4:1 314 911, 7:111 635, 8:9 425, 12:2 352, 15:986, 16:342, 20:190, 23:78, 24:23, 28:7, 31:10,
  32:3, 36:2, 39:1, 44:1, 47:2, 56:1, 64:1 (`data/z53/upper/hc_1e8.txt`).
- P2.1(i), (ii): 0 violations to 10⁸.
- L3.1: all certificate divisors for all c ∈ 𝒞_p, c ≤ 64, all p ≤ 2·10⁷: 45 499 504 checked, 0 violations.
- Sieve sets (T4.2 mechanism, p ≡ 1 (8), p ≤ 2·10⁶, `hc_1e7.txt`): #𝒮_K (no prime q ≡ −1 (4k) divides (p+4k)(4kp+1),
  k ≤ K) vs #{HC > 4K}: K=1: 4010/4010; K=2: 1332/196; K=4: 436/27; K=8: 174/5; K=16: 75/0; K=24: 52/0. The containment
  {HC > 4K} ⊂ 𝒮_K holds (0 violations); the gap comes from composite certificate divisors *and* from odd coordinates
  c ≡ −p (8) that 𝒮_K ignores (e.g. p = 6841 ∈ 𝒮_2 has HC = 7 via the prime divisor 41 ≡ −1 (mod 7) of 7p + 1).
`scripts/z53_upper_primecert.c`: prime-level certificates to 10⁸ (§5.2.3), `primecert_1e8*.txt`.
`scripts/z53_upper_hcpoint.py`: HC(p) with witnessing word for given p (spot checks in §5.2.3).

## 7. Reproduction

```
ulimit -v 6000000
gcc -O2 -o /tmp/z53u_hc scripts/z53_upper_hc.c && timeout 1800 /tmp/z53u_hc 100000000 24 20000000   # ~3 min
gcc -O2 -o /tmp/z53u_pc scripts/z53_upper_primecert.c -lm && timeout 600 /tmp/z53u_pc 100000000 100000000
timeout 120 uv run --with sympy python scripts/z53_upper_hcpoint.py 3361 66529 1095481 85664329 21841
```
