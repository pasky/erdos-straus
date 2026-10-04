# EXCEPTIONAL_KARY2 — the 3/4 cap without the B-hypothesis, for ℛ(M), (a,D), Case-A and selector classes (task O14)

Status: **checkpoint 2 (reviewed).** Reviews:
* an internal self-review (repairs applied: Cor 6.1 direction of the
  saving inequality and a projection step before ET Lemma 2.9; `Q₀`
  W-smooth; a transcription error in §3);
* two independent hostile reviews: `reviews/exceptional-kary2-review.md`
  (branch `side-agent/review-kary2`) and `reviews/exceptional-kary2-review-2.md`
  (branch `side-agent/review-kary2b`). Both find Theorem 5.1 SOUND. All
  their defects are applied here:
  * review 1: D1 selector scope, D2 the Lemma 3.1 step, D3, D4;
  * review 2: D1 selector classes as a fourth type, D2 notation and
    labels, D3–D5 scope and constants, D6 a Schinzel pointer.

Labels follow `DISCOVERIES.md`. Notation follows `EXCEPTIONAL_KARY.md`
(EK), `EXCEPTIONAL_TWIN.md` (ETw), `EXCEPTIONAL_TWIN4.md` (TW4) and
`EXCEPTIONAL_THETA.md` (ET). **ElT** is Elsholtz–Tao, *Counting the number
of solutions to the Erdős–Straus equation on unit fractions*, J. Aust.
Math. Soc. 2013 (arXiv 1107.1010). "ElT Prop 1.4" is their divisor-sum
bound; it is used, as in ET Lemma 3.7, as a published input that is not
re-proved here.

## 0. Summary

| item | statement | label |
|---|---|---|
| §1 | EK Thm 4.5 uses B only in the block/singleton first moments and in the second moment (pointwise τ-bound, lcm range, v ≤ 1+B); the number of primes per modulus never enters | PROVED (inspection) |
| Lemmas 2.1, 2.2 | no (a,D)-class and no Case-A class contains a square mod its modulus (Mordell/Jacobi); this proves ETw Remark 1.4's observation | PROVED |
| Lemma 2.3 | square base: product measure, R-term `≤ 2W`, avoids every W-smooth class containing no unit square mod its modulus, hence every W-smooth class of all four types (selector classes `0 mod p` included) | PROVED |
| Lemma 3.2 | ℛ(M): `Σ_{P(M)≤y}τ(A_M²)Γ(M)/M ≪ (log y)³(log log y)³`, no B (body: EK Lemma 4.2′; tail: Rankin + Cauchy–Schwarz) | PROVED |
| Lemma 3.3 | (a,D): first moment `≪ (log y)³`, a pure Euler product; selector classes: `≪ log log y` | PROVED |
| Lemmas 3.4–3.6 | Case A: small-divisor domination, box moments of `τ(krh²+1)^q`, first moment `≪ (log y)³(log log y)³` | PROVED; Lemma 3.6 uses ElT Prop 1.4 (published, not re-proved) |
| Lemmas 4.1–4.3 | cofactor second moments, `E p_ℓ² ≪ ℓ^{−7/4+o(1)}` for all four types, leak `≤ 1/2` with W absolute | PROVED |
| **Thm 5.1** | **every mixture of ℛ(M)-, (a,D)-, Case-A and selector classes, arbitrary moduli: `log(1/Eν) ≤ Cλ^{3/4}(log λ)^{3/4}` for ν ≥ 1 on the whole avoider set** | PROVED; Case-A part uses ElT Prop 1.4 (published, not re-proved) |
| Thm 5.2 | with `G ≤ P(G)^{1+B}`: `≪_B λ^{3/4}` for all four types (EK Thm 4.5 extended; covers the 3/4 note's selector majorant) | PROVED (same proviso) |
| Cor 6.1 | for nonnegative CRT majorants of the avoider set of such a family, with rounding `Σ|a_i| < N` and family primes `≤ N^{O(1)}`: saving `≪ (log N)^{3/4}(log log N)^{3/4}`; so no method *of this class* gives θ > 3/4 (exclusions: §6) | PROVED (same proviso) |
| §7 | brute-force checks of Lemmas 2.1(2), 2.2, 3.4; smooth first moments `≍ (log y)³` numerically | EVIDENCE |

All constants (W, λ₀, C) are absolute but astronomically large (review 2
estimates log W ≈ 10^{10–11}, through the Case-A exponents). Every
statement here is asymptotic only.

The B-removal follows TW4 §11's sketch in spirit, with one simplification.
No (D)/(H)/(G) split is needed: Rankin's trick, applied to the whole
modulus in dyadic blocks above `y^{u₀}` (`u₀ ≍ log log y`), combined with
Cauchy–Schwarz against crude polylogarithmic second moments of the
shifted divisor weight, makes the smooth-dominated tail `O(1)`. The body
`G ≤ y^{u₀}` is the old B-bounded sum with `B = u₀`. The price is
`u₀³ = O((log log y)³)` in the first moment, hence `(log λ)^{3/4}` in the
cap. The prediction of TW4 §11 (`λ^{3/4}log λ`) was slightly too
pessimistic. The singleton range must shrink to `s₁ = λ^{1/4}(log λ)^{−3/4}`;
with `s₁ = λ^{1/4}` the singletons alone would cost `λ^{3/4}(log λ)^3`.

## 1. Where EK Theorem 4.5 uses B, and where it does not

EK Thm 4.5 is assembled from EK Thm 4.1 (abstract sequential limit with
random costs), the base (ETw Lemma 1.3), singleton steps below `e^{s₁}`
(ETw Prop 4.1), sequential blocks `(e^s, e^{2s}]` with EK Thm 2.5 as the
step inequality, one linear block `(e^{λ/2}, e^λ]` (ETw Cor 4.3), and the
leak (EK Lemma 4.3). The hypothesis `M ≤ P(M)^{1+B}` enters at exactly
three places:

* **(B1) block first moment** (EK Lemma 4.2′, Step 3): the partial
  summation runs over `M ≤ e^{2(1+B)s}`;
* **(B2) singleton first moment** (ETw Prop 4.1): the same over
  `M ≤ e^{(1+B)s₁}`;
* **(B3) second moment / leak** (ETw Lemmas 2.4, 4.0, used in EK Lemma
  4.2(3) and 4.3). The cofactor q of the top prime power is `≤ ℓ^B`, and
  this is used three ways (review 1):
  * the pointwise bound `τ(A_q²) ≤ ℓ^{o(1)}`;
  * the lcm range `m ≤ ℓ^{2B}` (the factor `(1+2B log ℓ)^9`);
  * the finite range `v ≤ 1+B` (the factor `(2+B)²`).

  Through these it also enters the constants `W₀(B)`, `C(B)`. All three
  uses go away in §4: the AM–GM reduction sums over all cofactors, and
  `Σ_v ℓ^{−7v/8}` converges.

Everything else is B-free:
* EK Thm 2.5 is arithmetic-free and has no arity bound;
* EK Thm 4.1, ETw Thm 2.3′, ETw Cor 4.3 are B-free;
* the base: `Q₀` may be astronomically large; only `log(Q₀/|R|) = O(W)`
  enters (ETw Lemma 1.3(2));
* the leak mechanism (Lemma 2.1′ of ETw: every class is decided at its
  top prime) is B-free.

**The number of large primes per modulus never enters.** The level
gives d-locality (`d = ⌊λ/s⌋` block primes per term of ν), and EK Thm 2.5
accepts patterns of any arity. The arithmetic inputs are first moments
(sums over *all* classes with top prime in a range) and the second moment
of `p_ℓ` (a sum over cofactors). Neither sees `ω(M)`. This is the
difference from the Λ² route of TW4, where `ω_L(M)` controls the
noise-stability losses (`2^r`, `(log L)^r`).

So, to drop B, it suffices to replace (B1)–(B3) by bounds over *all*
classes with `P(G) ≤ y`, and over all cofactors of `ℓ^v`. That is §§3–4.
To add (a,D)-, Case-A and selector classes, the base must also avoid
their W-smooth classes (§2), and their first and second moments must be
bounded (§§3–4).

## 2. The four class types and the square base

**Definition 2.0 (forced-class families).** A *class* is `n ≡ b (mod G)`.
The four types, with the multiplicity bounds used below:

* **ℛ(M)** (notes Lemma 18.1): `M ≡ 3 (mod 4)`, `A = A_M = (M+1)/4`,
  classes `−4D (mod M)`, `D | A²`. At most `τ(A²)` classes per M.
* **(a,D)** (ET Lemma 3.2): `a, D ≥ 1`, `g = g(D) = Π p^{⌈v_p(D)/2⌉}`,
  class `−(4D+a) (mod G)`, `G = 4a·g`. Since `#{D : g(D) = g} ≤ 2^{ω(g)}`,
  a given pair `(a,g)` carries at most `2^{ω(g)}` classes, and a given
  modulus G at most `μ_{aD}(G) := Σ_{ag = G/4} 2^{ω(g)} ≤ τ(G)²` classes.
* **Case A** (ET §3, "Case A"): `d = r h²` with r squarefree, `g(d) = rh`,
  `m | 4d+1`, class `−m^{−1} (mod G)`, `G = 4rh`. At most `τ(4rh²+1)`
  classes per pair `(r,h)`, and
  `μ_A(G) := Σ_{4rh = G} τ(4rh²+1)` per modulus.
* **Selector** (reviews 1 D1, 2 D1): `0 (mod p)`, p prime. One class per
  prime.

Every class of the first three types is forced for every `n ≥ 1` (notes
Lemmas 16.1, 18.1; ET Lemma 3.2; ET §3 Case A). Selector classes are not
forced. They encode prime or rough-number restrictions: removing
`0 mod p` for all `p ≤ y` turns `𝒜` into `𝒜 ∩ {(n,P_y) = 1}`, which is
the selector of ET §1 and of the 3/4 note (`S_y = 1[(n,P_y)=1]`). A
*family* 𝔊 is any finite set of classes of these types, mixed
arbitrarily, with **no condition on the moduli** (no B, no dominant
prime, any number of primes at any scale).

**Lemma 2.1 (no squares in ℛ(M)- and (a,D)-classes; PROVED).**
1. No residue of an ℛ(M)-class is a square mod M.
2. No (a,D)-class contains a perfect square `x² ≥ 1`. Hence no residue of
   an (a,D)-class is a square mod G.

*Proof.* 1. Let `c ≡ −4D (mod M)`. By ETw Lemma 1.1, `gcd(D,M) = 1` and
`(−4D|M) = −1`. If `c ≡ x² (mod M)`, then `gcd(x,M) = 1` and the Jacobi
symbol would be `(x²|M) = 1`.
2. Let `n = x² ≥ 1` lie in the class. By ET Lemma 3.2, with
`n + 4D + a = 4agj` (`j ≥ 1` as `n ≥ 1`), `M = (n+4D)/a = 4gj − 1` is
`≡ 3 (mod 4)`, `D | A_M²` and `n ≡ −4D (mod M)`. By part 1, n is not a
square mod M; but n is a perfect square. Contradiction. If a residue c of
the class were a square mod G, say `c ≡ x² (mod G)` with `1 ≤ x ≤ G`, then
the perfect square `x² ≥ 1` would lie in the class. ∎

**Lemma 2.2 (no squares in Case-A classes; PROVED).** Let `d = rh²`,
r squarefree, `m | 4d+1`, `G = 4rh`. Then `−m^{−1} (mod G)` is not a
square mod G.

*Proof.* `gcd(m, 2rh) = 1` since `m | 4rh²+1`, so `m^{−1}` exists mod G.
Suppose `−m^{−1} ≡ y² (mod G)`. Then `y²m ≡ −1 (mod 4rh)`, so
`gcd(y, G) = 1`.
* *Mod 4:* y is odd, `y² ≡ 1 (mod 8)`, so `m ≡ −1 (mod 4)`. In particular
  `m ≥ 3` and `(−1|m) = −1`. If r is even, `8 | G` and `m ≡ −1 (mod 8)`,
  so `(2|m) = 1`.
* *Mod p, p | r odd:* `y²m ≡ −1 (mod p)` gives `−m ≡ (y^{−1})² (mod p)`, so the Legendre symbol
  `(−m|p) = 1`. Let `r_o` be the odd part of r (squarefree). Then the
  Jacobi symbol `(−m|r_o) = 1`.
* *Mod m:* `4rh² ≡ −1 (mod m)` gives `−r ≡ ((2h)^{−1})² (mod m)`, with
  `gcd(2h, m) = 1`. So the Jacobi symbol `(−r|m) = 1`.

Now compute `(−r|m)` otherwise. `(−r|m) = (−1|m)(2|m)^{[r even]}(r_o|m)
= −(r_o|m)`. By reciprocity for coprime odd positive `r_o, m`, with
`(m−1)/2` odd, `(r_o|m) = (m|r_o)(−1)^{(r_o−1)/2}`, and
`(m|r_o) = (−1|r_o)(−m|r_o) = (−1)^{(r_o−1)/2}`. So `(r_o|m) = 1` and
`(−r|m) = −1`, a contradiction. (`r_o = 1` is included: both symbols are
then 1.) ∎

**Lemma 2.3 (square base; PROVED).** Fix `W ≥ 3`. Let `Q₀` be the least common
multiple of `8·P_W` and of the W-smooth parts of all moduli of 𝔊 (`P_W`
the product of the primes ≤ W). So `Q₀` is W-smooth (review: an extra
prime above W in `Q₀` would add its own factor to the R-term). Put

    R_W^□ = { c mod Q₀ : c mod p^e is a unit square for every p^e ∥ Q₀ }.

1. (R1) Every `c ∈ R_W^□` avoids every class `b (mod G)` with G W-smooth
   that contains no unit square mod G. In particular it avoids every
   W-smooth class of 𝔊 of all four types.
2. `log(Q₀/|R_W^□|) = 3 log 2 + Σ_{3≤p≤W} log(2p/(p−1)) ≤ 2W`.
3. (R2) Under the uniform law on `R_W^□`, residues at distinct primes are
   independent, and `P(c ≡ a (mod p^e)) ≤ γ(p)/p^e` for `p^e | Q₀`, with
   `γ(p) = 2p/(p−1)` for odd p and `γ(2) = 8`.

*Proof.* 1. Let the class be `b (mod G)`, G W-smooth, so every `p^e ∥ G`
divides `Q₀`. If `c ≡ b (mod G)` and c is a unit square mod every
`p^e ∥ Q₀`, then by CRT `b ≡ c` is a unit square mod G. For the first
three types this contradicts Lemma 2.1 or 2.2, which exclude even
non-unit squares. A selector class `0 (mod p)` contains the square 0 but
no unit, so it contains no unit square either. 2. By CRT `R_W^□` is a product. Unit squares mod `p^e` (p odd)
are a fraction `(p−1)/(2p)` of the residues; mod `2^e`, `e ≥ 3`, a
fraction `1/8`. And `Σ_{3≤p≤W}log(2p/(p−1)) ≤ π(W)log 3 + O(1)`.
3. As ETw Lemma 1.3(3): a single residue `a mod p^e` has probability at
most `1/(#unit squares mod p^e) = γ(p)/p^e`. ∎

ETw Remark 1.4 observed this numerically for (a,D) and Case-A classes
(no square mod G in 12,000 resp. 16,406 classes) and said no proof was
written. Lemmas 2.1(2) and 2.2 are that proof. `scripts/kary2_square_check.py`
re-checks both lemmas by brute force (§7).

From here on `Γ(m) = Π_{p | m} γ'(p)`, with `γ'(p) = γ(p)` for `p ≤ W`
and `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` for `ℓ > W`. So `Γ(m) ≤ 8·3^{ω(m)}`,
Γ is submultiplicative, and by the chain rule (ETw Lemma 2.2, with Lemma
2.3(3) at the base) `Q'(n ≡ b (mod m)) ≤ Γ(m)/m` for every m and b.

## 3. First moments without B

For a class `C = (b mod G)` write `G = G(C)`, `P(C) = P(G)` (largest prime
factor). For `y ≥ 3` put

    𝔐(y) = Σ_{C ∈ 𝔘, W < P(C) ≤ y} Γ(G)/G,

where 𝔘 is the *universe* of all classes of the four types (each class
counted once per parametrisation; this only over-counts). EK Lemma 4.2′
Step 1 bounds the expected (light or not) block mass by this sum:
`E_{Q'} Σ_{ℓ ∈ V} p_ℓ ≤ 𝔐(max V)`, for every family 𝔊 ⊆ 𝔘 (Step 1 uses
only the chain rule, now with the square base, and
`(Γ(q)/q)ℓ^{−v} ≤ Γ(G)/G` for `G = qℓ^v`). The four types are bounded separately:
`𝔐 ≤ 𝔐_R + 𝔐_{aD} + 𝔐_A + 𝔐_S`.

**Lemma 3.1 (smooth Euler products, Rankin; PROVED, standard).** Let
`F ≥ 0` be multiplicative with `F(p^e) ≤ H(e+1)^a` for all p, e, and
`F(p) ≤ κ + H p^{−1/2}` for `p > W`. Let `y ≥ y₀(W)`, `η ∈ {0, 1/log y}`.
Then

    Σ_{P(m) ≤ y} F(m) m^{−1+η} ≤ C(H,a,κ,W) (log y)^κ,

and for `K ≥ 1`, with `u = log K/log y`,

    Σ_{K < m ≤ 2K, P(m) ≤ y} F(m)/m ≤ C(H,a,κ,W) e^{−u} (log y)^κ.

*Proof.* The sum is `Π_{p≤y}(1 + Σ_{e≥1}F(p^e)p^{−e(1−η)})`. Take
`y₀ ≥ e^{10}`, so `η ≤ 1/10` and `p^{−e(1−η)} ≤ p^{−0.9e}` for every p
(review 1, D2: the earlier bound `p^{eη} ≤ e^e` does not give convergence
at small p). Then `Σ_{e≥2}H(e+1)^a p^{−e(1−η)} ≤ C(H,a)p^{−1.8}` for all
`p ≥ 2`, and these terms contribute a bounded factor overall. For
`p ≤ W` the e = 1 term is `≤ H2^a p^{η}/p ≤ eH2^a/p` (as `p ≤ y`), so
the primes `p ≤ W` contribute a factor `≤ C(H,a)(log W)^{eH2^a}`, a
constant. For `W < p ≤ y`, the e = 1 term is
`≤ (κ + Hp^{−1/2})p^{−1+η}`, and `p^η ≤ 1 + (e−1)log p/log y` (convexity
on `[0,1]`), so `Σ_{p≤y}p^{−1+η} ≤ log log y + (e−1)(log y + 2)/log y + O(1)`
(Mertens). Hence the product is `≤ C(log y)^κ`. For the second bound,
`1/m ≤ m^{−1+η}K^{−η}` for `m > K` and `K^{−η} = e^{−u}`. ∎

**Lemma 3.2 (ℛ(M) first moment without B; PROVED).** For `y ≥ y₀(W)`,

    𝔐_R(y) = Σ_{M ≡ 3 (4), P(M) ≤ y} τ(A_M²) Γ(M)/M ≤ K_R(W) (log y)³ (log log y)³.

*Proof.* Put `u₀ = 12 log log y` and `X = y^{u₀}`.
*Body `M ≤ X`.* Drop `P(M) ≤ y`. EK Lemma 4.2′ Steps 2–3 (Shiu; the
partial summation needs no B) give `≤ 1.3K₀(W)(log X)³ = 1.3K₀·12³
(log y)³(log log y)³`.
*Tail `M > X`.* Split into blocks `(K, 2K]`, `K = 2^t ≥ X/2`, and apply
Cauchy–Schwarz in each block:

    Σ_{K<M≤2K, P(M)≤y} τ(A²)Γ(M)/M ≤ (Σ_{K<M≤2K, P(M)≤y} Γ(M)²/M)^{1/2} (Σ_{K<M≤2K} τ(A_M²)²/M)^{1/2}.

The first factor is `≤ C e^{−u/2}(log y)^{1/2}` by Lemma 3.1 (`F = Γ²`,
`F(p) = γ'(p)² ≤ 1 + 5p^{−1/2}` for `p > W ≥ 16`, so κ = 1). For the
second, `A = (M+1)/4 ≤ K`, so it is `≤ K^{−1}Σ_{A≤K}τ(A²)²`. With
`g = τ(·²)² ∗ μ ≥ 0` (`g(p^k) = (2k+1)² − (2k−1)² = 8k`),
`Σ_{A≤x}τ(A²)² ≤ xΣ_{d≤x}g(d)/d ≤ xΠ_{p≤x}(1 + Σ_k 8k p^{−k}) ≤ C x(log 2x)^8`.
So a block contributes `≤ C e^{−u/2}(log y)^{1/2}(2u log y)^4`
(`log 2K ≤ 2u log y` as `u ≥ u₀ − δ ≥ 1`). The function `φ(u) = e^{−u/2}u^4`
decreases for `u ≥ 8`, and consecutive blocks have u-spacing
`δ = log 2/log y`, so `Σ_{t} φ(u_t) ≤ φ(u₀ − δ) + δ^{−1}∫_{u₀−δ}^∞ φ`.
Hence the tail is `≤ C(log y)^{5.5}u₀^4 e^{−u₀/2} = C·12⁴(log log y)^4
(log y)^{−1/2} ≤ C`. ∎

**Lemma 3.3 ((a,D) first moment; PROVED).** For `y ≥ y₀(W)`,

    𝔐_{aD}(y) ≤ Σ_{a, g : P(ag) ≤ y} 2^{ω(g)} Γ(4ag)/(4ag) ≤ K_{aD}(W) (log y)³.

*Proof.* `Γ(4ag) ≤ γ'(2)Γ(a)Γ(g) = 8Γ(a)Γ(g)` (Γ is submultiplicative).
So the sum is at most `2·(Σ_{P(a)≤y}Γ(a)/a)(Σ_{P(g)≤y}2^{ω(g)}Γ(g)/g)`.
Lemma 3.1 with `η = 0` gives `(log y)¹` and `(log y)²` (κ = 1, 2). ∎

No shifted divisor function occurs here: the (a,D)-grouping counts its
classes by `(a, g)` and a bounded multiplicity, so its mass is a pure
Euler product. This is why ET Lemma 3.2 already had a clean profile.

**Lemma 3.3′ (selector first moment; PROVED).**
`𝔐_S(y) = Σ_{W<p≤y} Γ(p)/p ≤ Σ_{W<p≤y}(1+2p^{−1/2})/p ≤ log log y + O(1)`.
This is negligible against `(log y)³`.

**Lemma 3.4 (small-divisor domination; PROVED, standard, cf. Landreau).**
For every `n ≥ 1`, `τ(n) ≤ 8·max{τ(d)^7 : d | n, d ≤ n^{1/4}}`. Hence, for
every integer `q ≥ 1`, `τ(n)^q ≤ 8^q Σ_{d | n, d ≤ n^{1/4}} τ(d)^{7q}`.

*Proof.* Let `n_L` be the part of n composed of primes `p > n^{1/4}`; it
has at most 3 prime factors with multiplicity, so `τ(n_L) ≤ 8`. List the
prime factors of `n_S = n/n_L` with multiplicity and cut the list greedily
into consecutive chunks `c_1, …, c_m`: each chunk is the longest
continuation whose product stays `≤ n^{1/4}`. Every `c_i` divides n and is
`≤ n^{1/4}`, and `c_i c_{i+1} > n^{1/4}` (otherwise `c_i` would have
absorbed the first prime of `c_{i+1}`). The `⌊m/2⌋` disjoint products
`c_1c_2, c_3c_4, …` are each `> n^{1/4}` and multiply to at most n, so
`⌊m/2⌋ ≤ 3` and `m ≤ 7`. Since τ is submultiplicative,
`τ(n) ≤ τ(n_L)Π_iτ(c_i) ≤ 8 max_i τ(c_i)^7`. ∎

**Lemma 3.5 (Case-A box moments; PROVED).** For integers `q ≥ 1`,
`k ≥ 4` with `4 | k`, and `K ≥ k³`,

    Σ_{r, h ≥ 1, rh ≤ K} τ(k r h² + 1)^q ≤ C_q K (log 2kK)^{c_q},    c_q = 2^{7q+1} + 1.

*Proof.* `N = krh² + 1` is odd, so all its divisors are odd. Cover
`{rh ≤ K}` by dyadic boxes `r ∈ [R,2R)`, `h ∈ [H,2H)` (`R, H` powers of 2,
`RH ≤ K`); `Σ_{boxes} RH ≤ 2K(log₂K + 1)`.
*Boxes with `max(R,H) ≥ 10k`.* In the box `N ≤ 8kRH² + 1 =: X`, and
`X^{1/4} ≤ max(R,H)` (as `X ≤ 10k·max(R,H)³`). By Lemma 3.4,
`Σ_{box}τ(N)^q ≤ 8^q Σ_{d ≤ X^{1/4}} τ(d)^{7q}·#{(r,h) ∈ box : d | N}`.
If `p | d` and `p | kh`, then `N ≡ 1 (mod p)`; so only h with
`gcd(d, kh) = 1` count. If `d ≤ R`: for each such h, r lies in one class
mod d, at most `2R/d` values. If `d ≤ H`: for each r, h lies in at most
`ρ(d) ≤ 2^{ω(d)}` classes mod d (d odd, Hensel), at most `2^{ω(d)}·2H/d`
values. Either way the count is `≤ 2^{ω(d)+2}RH/d`, and
`Σ_{d≤X}τ(d)^{7q}2^{ω(d)}/d ≤ Π_{p≤X}(1 + 2^{7q+1}/p + O_q(p^{−2}))
≤ C_q(log X)^{2^{7q+1}}`.
*Boxes with `max(R,H) < 10k`.* They contain at most `(20k)²` pairs, each
with `N ≤ 8000k⁴` and `τ(N)^q ≤ C_q N^{1/8} ≤ C_q k^{1/2}`; total
`≤ C_q k^{2.5} ≤ C_q K`.
Summing, `≤ C_q K (log 2K)(log 2kK)^{2^{7q+1}} + C_qK`. ∎

**Lemma 3.6 (Case-A first moment without B; PROVED, using ElT Prop. 1.4,
published, not re-proved).** For `y ≥ y₀(W)`,

    𝔐_A(y) ≤ Σ_{r,h : P(rh) ≤ y} τ(4rh²+1) Γ(4rh)/(4rh) ≤ K_A(W) (log y)³ (log log y)³.

*Proof.* Put `u₀ = (c₂ + 8) log log y`, `X = y^{u₀}`.
*Body `rh ≤ X`.* Drop `P(rh) ≤ y`. ET Lemma 3.7 with its γ-weight
clause applies to `Γ(4rh) ≤ 8Γ(r)Γ(h) = 8Σ_{s|r}h(s)Σ_{t|h}h(t)`, h
multiplicative, squarefree-supported, `h(p) = γ'(p) − 1 ≤ 7` for `p ≤ W`
and `≤ 2p^{−1/2}` for `p > W`. Its two conditions,
`Σ_{s,t}h(s)h(t)log(2+st)/(st) < ∞` and `Σ_n h(n)n^{−3/4} < ∞`, hold.
So `Σ_{rh≤x}τ(4rh²+1)Γ(4rh) ≤ C(W)x(log 2x)²`, and partial summation gives
`≤ C(W)(log X)³ = C(W)(c₂+8)³(log y)³(log log y)³`.
*Tail `rh > X`.* Blocks `K < rh ≤ 2K`, `K = 2^t ≥ X/2`; Cauchy–Schwarz over
pairs `(r,h)`. First factor: there are `τ(n)` pairs with `rh = n`, so it
is `≤ (64Σ_{K<n≤2K, P(n)≤y}τ(n)Γ(n)²/n)^{1/2} ≤ C e^{−u/2}(log y)` by
Lemma 3.1 (`F = τΓ²`, κ = 2). Second factor: by Lemma 3.5 (q = 2, k = 4),
`(K^{−1}Σ_{rh≤2K}τ(4rh²+1)²)^{1/2} ≤ C(log 2K)^{c₂/2} ≤ C(2u log y)^{c₂/2}`.
Summing over blocks as in Lemma 3.2,
the tail is `≤ C(log y)^{2+c₂/2}u₀^{c₂/2}e^{−u₀/2} = C(c₂+8)^{c₂/2}(log log y)^{c₂/2}(log y)^{−2} ≤ C`
(one `log y` is the first factor, one counts the blocks per unit of u). ∎

*On the citation.* ElT Prop. 1.4 is used only for the body, exactly as
in ET Lemma 3.7; it is what gives the exponent 2 of
`log x`. Lemma 3.5 is self-contained but its exponent `c₂ = 2^{15}+1` is
useless except against Rankin's `e^{−u/2}`. So the ℛ(M)- and (a,D)-parts
of everything below (and the selector part) use no external input; the
Case-A part uses ElT Prop. 1.4 in the same way as ET Lemma 3.7
(DISCOVERIES (D)11).

**Corollary 3.7 (all four types; PROVED, the Case-A part using ElT
Prop. 1.4).**
`𝔐(y) ≤ K₃(W)(log y)³(log log y)³` for `y ≥ y₀(W)`.

**Remark 3.8 (where the `(log log y)³` comes from).** Heuristically
`𝔐_R(y) ≍ (log y)³`: `τ(A_M²)` should average `≍ log² M` also over
y-smooth M, and `Σ_{P(M)≤y}(log M)²/M ≍ (log y)³`. Our proof drops the
smoothness on `M ≤ y^{u₀}` and pays `u₀³`; the decay that kills the tail
comes from Rankin, which costs a full `log y` per block and forces
`u₀ ≍ log log y`. A bound `Σ_{M≤x, P(M)≤y}τ(A_M²) ≪ Ψ(x,y)(log x)²`
(shifted smooth numbers, Fouvry–Tenenbaum type) would remove the loss in
𝔐_R; it is not needed for the exponent.

## 4. Second moments and the leak without B

Fix a prime `ℓ > W` and `v ≥ 1`. Let `𝒞_{ℓ,v}` be the classes of 𝔊 with
`ℓ^v ∥ G` and `P(G/ℓ^v) < ℓ` (top prime ℓ), and write `G = qℓ^v`. Such a
class is active at a history iff `n ≡ b (mod q)`, a condition on the
base and the primes `< ℓ`; it then forbids one class mod `ℓ^v`. So

    p_ℓ ≤ Σ_{v≥1} ℓ^{−v} N_{ℓ,v},   N_{ℓ,v}(n) = #{C ∈ 𝒞_{ℓ,v} : n ≡ b_C (mod q_C)}.

Let `μ_{ℓ,v}(q)` be the number of classes in `𝒞_{ℓ,v}` with cofactor q.

**Lemma 4.1 (reduction to a cofactor sum; PROVED).**

    E_{Q'} N_{ℓ,v}² ≤ C(W) log ℓ · Σ_{P(q) < ℓ, ℓ ∤ q} μ_{ℓ,v}(q)² τ(q)Γ(q)/q.

*Proof.* `E N² = Σ_{C,C'} Q'(n ≡ b_C (q_C), n ≡ b_{C'} (q_{C'}))`. Each
term is 0 or the probability of one class mod `lcm(q_C, q_{C'})`, so it is
`≤ Γ(lcm)/lcm` (§2). Group by cofactors and use
`μ(q)μ(q') ≤ (μ(q)² + μ(q')²)/2` and symmetry:
`E N² ≤ Σ_q μ(q)² Σ_{q'} Γ(lcm(q,q'))/lcm(q,q')`. Write `g = gcd(q,q')`,
`q' = gq''`; then `lcm = qq''` and `Γ(lcm) ≤ Γ(q)Γ(q'')`, and
`q' ↦ (g, q'')` is injective. So the inner sum is
`≤ τ(q)Γ(q)/q · Σ_{P(q'')<ℓ}Γ(q'')/q'' ≤ τ(q)Γ(q)/q · C(W)log ℓ`
(Lemma 3.1, η = 0, κ = 1). ∎

(This is ETw Lemma 2.4's expansion, with the pointwise τ-bound replaced
by AM–GM; nothing is assumed about the size of q.)

**Lemma 4.2 (cofactor sums for the four types; PROVED, Case A included,
with no external input).** For every `κ ∈ (0, 1]` there are `c` (absolute) and
`C_κ(W)` such that for each type

    Σ_{P(q)<ℓ} μ_{ℓ,v}(q)² τ(q)Γ(q)/q ≤ C_κ(W) (v+1)^c [ (log ℓ)^c + ℓ^{κv} ].

*Proof.* Blocks `K < q ≤ 2K` (`K = 2^t`), `u = log K/log ℓ`. In each case a
block is either *long* (K above a power of `ℓ^v`), where Cauchy–Schwarz
with Lemma 3.1 (`y = ℓ`) gives `e^{−u/2}` times a polylog, or *short*,
where pointwise divisor bounds cost `ℓ^{κv}`.

*Selector.* Only `v = 1`, `q = 1`, `μ(1) = 1`: the sum is 1. (The class
`0 mod ℓ` is always active and adds `1/ℓ` to `p_ℓ` deterministically.)

*(a,D).* `μ(q) ≤ μ_{aD}(qℓ^v) ≤ τ(qℓ^v)² ≤ (v+1)²τ(q)²`. So the sum is
`≤ (v+1)⁴Σ_{P(q)<ℓ}τ(q)⁵Γ(q)/q ≤ C(v+1)⁴(log ℓ)^{32}` (Lemma 3.1, κ = 32). No
blocks needed.

*ℛ(M).* `μ(q) ≤ τ(A²)`, `A = (qℓ^v+1)/4`. Long blocks, `K ≥ 4ℓ^{v/3}`:

    Σ_{block} τ(A²)²τ(q)Γ(q)/q ≤ (Σ_{block, P(q)<ℓ} τ(q)²Γ(q)²/q)^{1/2} (Σ_{block} τ(A²)⁴/q)^{1/2}.

The first factor is `≤ Ce^{−u/2}(log ℓ)²` (Lemma 3.1, `F = τ²Γ²`,
κ = 4). In the second, A runs over the class `4^{−1} (mod ℓ^v)` in an
interval of length `ℓ^vK/4`, and `ℓ^v < (ℓ^vK/4)^{3/4}`. Shiu's theorem
(as in ET Lemma 3.1; `F = τ(·²)⁴`, `F(p) = 81`, β = 1/4) gives
`Σ ≪ (ℓ^vK/φ(ℓ^v))(log 2ℓ^vK)^{80}`, so the factor is
`≤ C((v+u+1)log ℓ)^{40}`. Summing over blocks as in Lemma 3.2:
`≤ C(v+1)^{40}(log ℓ)^{43}`. Short blocks, `K < 4ℓ^{v/3}`: `A ≤ 4ℓ^{2v}`,
`q ≤ 8ℓ^{v/3}`, so `τ(A²)²τ(q)Γ(q) ≤ C_κℓ^{κv/2}`, and
`Σ_{q ≤ 8ℓ^{v/3}}1/q ≤ v log ℓ + 3 ≤ C_κℓ^{κv/2}`.

*Case A.* Here `4rh = qℓ^v` with r squarefree, so `v_ℓ(r) = v₁ ∈ {0,1}`,
`v_ℓ(h) = v₂ = v − v₁`. Cauchy–Schwarz over the at most `τ(qℓ^v)` pairs
gives `μ(q)² ≤ (v+1)τ(q)Σ_{4rh=qℓ^v}τ(4rh²+1)²`. Long blocks,
`K ≥ 128ℓ^{6v}`: Cauchy–Schwarz over pairs (r,h) with q in the block,

    first factor ≤ ((v+1)Σ_{block, P(q)<ℓ} τ(q)⁵Γ(q)²/q)^{1/2} ≤ C(v+1)^{1/2}e^{−u/2}(log ℓ)^{16},

    second factor ≤ (Σ_{v₁} (4/K)Σ_{r'h' ≤ K/2} τ(k r'h'² + 1)⁴)^{1/2},   k = 4ℓ^{v₁+2v₂} ≤ 4ℓ^{2v},

writing `r = ℓ^{v₁}r'`, `h = ℓ^{v₂}h'` (then `r'h' = q/4`); the factor
`(v+1)` from the preliminary bound on `μ(q)²` is carried into the
polynomial `(v+1)^c`. Since
`K/2 ≥ k³`, Lemma 3.5 (q = 4) bounds the second factor by
`C(log 2kK)^{c₄/2} ≤ C((2v+u+2)log ℓ)^{c₄/2}`. Summing over blocks:
`≤ C(v+1)^{c}(log ℓ)^{c}`. Short blocks, `K < 128ℓ^{6v}`: `4rh² + 1 ≤
ℓ^{O(v)}` and `q ≤ ℓ^{O(v)}`, so pointwise
`μ(q)²τ(q)Γ(q) ≤ C_κℓ^{κv/2}`, and `Σ_{q≤256ℓ^{6v}}1/q ≤ C_κℓ^{κv/2}`. ∎

**Lemma 4.3 (second moment and leak without B; PROVED, Case A included,
with no external input).** For every prime `ℓ > W`,
`E_{Q'} p_ℓ² ≤ C(W) ℓ^{−7/4}(log ℓ)^{c}`, with `C(W) ≤ C(log W)^{c}`. Hence
there is an absolute `W₀` such that for `W ≥ W₀`, every family 𝔊 ⊆ 𝔘,
and the block structure of §5, `𝔏 ≤ 1/2`.

*Proof.* Split `N_{ℓ,v}` by type; Minkowski over types and over v:
`(E p_ℓ²)^{1/2} ≤ Σ_v ℓ^{−v}Σ_{type}(E N_{ℓ,v,type}²)^{1/2}`. By Lemmas
4.1–4.2 with `κ = 1/4`, `E N² ≤ C(W)(v+1)^{c}(log ℓ)^{c+1}ℓ^{v/4}`, so
`(E p_ℓ²)^{1/2} ≤ C(W)Σ_{v≥1}ℓ^{−7v/8}(v+1)^{c}(log ℓ)^{c+1} ≤ C(W)ℓ^{−7/8}(log ℓ)^{c+1}`.
*W-dependence.* The constants of Lemma 3.1 depend on W only through the
Euler factors at `p ≤ W`, each `1 + O_{H,a}(1/p)`; their product is
`≤ C(log W)^{c}`. Shiu's constant is uniform. So `C(W) ≤ C(log W)^c`.
*Leak.* Every class is decided at its top prime in the order of §5, so
EK Lemma 4.3 (ETw Lemma 2.1′ and Markov, `E[p1{p>δ}] ≤ E p²/δ`) gives
`𝔏 ≤ Σ_{ℓ>W}ℓ^{1/2}E p_ℓ² ≤ C(log W)^{c}Σ_{ℓ>W}ℓ^{−5/4}(log ℓ)^{2c+2}
≪ W^{−1/4}(log W)^{3c+2}`, which is `≤ 1/2` for `W ≥ W₀`. ∎

So W, and every constant below, is absolute: there is no B left to
depend on.

## 5. The cap

**Theorem 5.1 (3/4 cap for all forced-class families, no B; PROVED; the
Case-A part uses ElT Prop. 1.4, published, not re-proved).** There are
absolute constants `W, λ₀, C` such that the following holds. Let 𝔊 be
any finite family of ℛ(M)-, (a,D)-, Case-A and selector classes
(Definition 2.0), mixed arbitrarily, with arbitrary moduli. Let
`𝒜 = 𝒜(𝔊)` be the set of **all** integers in none of its classes, and
let ν be a majorant of level `λ ≥ λ₀` of 𝒜 (ET §1:
`ν = Σ a_i 1[n ≡ b_i (d_i)] ≥ 0` on ℤ, `≥ 1` on all of 𝒜,
`Σ_{ℓ | d_i, ℓ > W} log ℓ ≤ λ`). Then

    log(1/Eν) ≤ C λ^{3/4} (log λ)^{3/4}.

If 𝔊 contains no Case-A classes, no external input is used. The
constants are astronomically large (§0), so the statement is asymptotic
only.

*Proof.* EK Theorem 4.1 with the following data.
* *Base:* `R_W^□` (Lemma 2.3); (R1) holds for every W-smooth class of 𝔊
  (selector classes `0 mod p`, `p ≤ W`, included), and the R-term is
  `≤ 2W`. Selector classes with `p > W` are ordinary classes decided at
  p (`q = 1`, `v = 1`).
* *Blocks, in increasing order of primes,* with
  `s₁ = λ^{1/4}(log λ)^{−3/4}` (`λ₀` such that `s₁ > 2 log W`):
  singletons `{ℓ}`, `W < ℓ ≤ e^{s₁}`; sequential blocks
  `V_i = {ℓ : 2^is₁ < log ℓ ≤ 2^{i+1}s₁} ∩ (·, e^{λ/2}]`, `0 ≤ i ≤ I`
  (I maximal with `2^Is₁ < λ/2`); one linear block `(e^{λ/2}, e^λ]`;
  singletons above `e^λ`. This is EK Thm 4.5's structure with a smaller
  `s₁`.
* *Leak:* every class is decided at its top prime (its modulus is
  `qℓ^v`, `P(q) < ℓ`), and `𝔏 ≤ 1/2` by Lemma 4.3.

*Costs.* Write `𝔐(y) ≤ K₃(log y)³(log log y)³` (Cor 3.7).
* Singletons (ETw Prop 4.1: `Φ ≤ (4/3)p_ℓ` if light, 0 if heavy;
  doubled by Thm 4.1): `≤ (8/3)𝔐(e^{s₁}) ≤ (8/3)K₃s₁³(log λ)³
  = (8/3)K₃λ^{3/4}(log λ)^{3/4}`.
* Block `V_i`, `s = 2^is₁`, `d_i = ⌊λ/s⌋ ≥ λ/(2s) ≥ 1`. By EK Cor 2.6 for
  each history and Jensen (as in EK Thm 4.5),
  `E Φ_i ≤ d_i log(C₀(E M_{V_i} + 4d_i)/d_i) + (4/3)d_i + ½log(22d_i+22) + 3`.
  Here `E M_{V_i} ≤ 𝔐(e^{2s}) ≤ 8K₃s³(log λ)³` (as `2s ≤ λ`), so
  `(E M_{V_i} + 4d_i)/d_i ≤ 16K₃s⁴(log λ)³/λ + 4 = 16K₃·16^i + 4`, using
  `s⁴ = 16^iλ(log λ)^{−3}`. Hence
  `E Φ_i ≤ (λ/(2^is₁))(c₁ + i log 16) + O(log λ)`, and
  `2Σ_i EΦ_i ≤ Cλ/s₁ + O(log²λ) = Cλ^{3/4}(log λ)^{3/4} + O(log²λ)`.
* Linear block: `2log(1 + 3e^{−λ/4})` (ETw Cor 4.3). Above `e^λ`: 0.

Summing, `log(1/Eν) ≤ 2W + log 2 + Cλ^{3/4}(log λ)^{3/4}`. Since W is
absolute, `2W + log 2` is absorbed into C for `λ ≥ λ₀` (review 2, D5). ∎

**Theorem 5.2 (bounded B, all four types, no log loss; PROVED; the
Case-A part uses ElT Prop. 1.4).** Fix `B ≥ 0`. If every modulus of 𝔊
satisfies `G ≤ P(G)^{1+B}` (automatic for selector classes), then `log(1/Eν) ≤ C(B)λ^{3/4}` for `λ ≥ λ₀(B)`.

*Proof.* As EK Thm 4.5 (`s₁ = λ^{1/4}`), with Lemma 2.3 for the base and
Lemma 4.3 for the leak (both B-free). The first moment of classes with
`P(G) ≤ y` is now `≤ C(B)(log y)³`: drop smoothness and sum over
`G ≤ y^{1+B}`; for ℛ(M) by EK Lemma 4.2′, for (a,D) by Lemma 3.3, for
selectors by Lemma 3.3′, for Case A by the body part of Lemma 3.6 with
`X = y^{1+B}`. ∎

So EK Thm 4.5 extends verbatim to (a,D)-, Case-A and selector classes,
and with Theorem 5.1 the B-hypothesis costs at most a factor
`(log λ)^{3/4}`.

**Remark 5.4 (the 3/4 note's majorant is covered; reviews 1 D1, 2 D1).**
The 3/4 note's majorant is `ν_X = S_y·Q_r(H_X)`, with selector
`S_y = 1[(n,P_y) = 1]`, `y = Bt³ > W`. It is `≥ 1` only on y-rough
avoiders, so it is *not* a majorant of `𝒜(𝔊₀)` for the note's atom
family 𝔊₀. That was the gap in the checkpoint-1 claim, inherited from
EK Thm 4.5. It *is* a majorant of `𝒜(𝔊₀ ∪ {0 mod p : p ≤ y})`. The atoms
`−uv^{−1} mod kℓ` are ℛ(kℓ)-classes with `kℓ ≤ ℓ^{1+2κ}`, `κ < 1/240`
(review 2, check (3), on 124,464 atoms). So the note's majorant lies in
Theorem 5.2's class with `B < 1/120`, and its saving `c(log N)^{3/4}`
matches the cap `C(log N)^{3/4}` in order. The constants cannot be
compared: the note's are ineffective (Bombieri–Vinogradov), and ours
are astronomically large. The R-term here is `≤ 2W`, smaller than ET's
`log(P/φ(P))` for selectors. The note's transfer from `E_pr(N)` to
`E(N)` by the multiplicative semigroup is non-CRT post-processing that
only loses, so it does not affect this reading.

**Remark 5.3 (number of primes; goal (1) of the brief).** Nowhere in
§§2–5 does `ω(G)`, or the number of primes of G at one scale, enter. The
k-ary step (EK Thm 2.5) has no arity bound; the first moments are sums
over all classes with `P(G)` in a range; the second moment is a sum over
all cofactors of `ℓ^v`. This is the structural reason the KARY route has
no analogue of the middle window `r ≍ log L` of TW4 §§9.3, 12 (there the
Λ² noise-stability losses `2^r`, `(log L)^r` are per prime). The TW4
(D)/(H)/(G) split is not needed either: Rankin's trick is applied to
the whole modulus, uniformly.

## 6. The final statement, and what remains excluded

**Corollary 6.1 (exceptional-set reading; PROVED; the Case-A part uses
ElT Prop. 1.4).** Let a method bound `#(𝒜(𝔊) ∩ [1,N])` by
`N·Eν + Σ_i|a_i|`, where:
* 𝔊 is any finite family of ℛ(M)-, (a,D)-, Case-A and selector classes
  (arbitrary moduli; no B, no dominant prime, any number and
  multiplicity of prime factors);
* ν is a CRT majorant of any level: `ν = Σ a_i 1[n ≡ b_i (d_i)]`, `≥ 0` on
  ℤ and `≥ 1` on **all of** `𝒜(𝔊) ⊂ ℤ`;
* every prime dividing a modulus of 𝔊 is `≤ N^A` (in particular, moduli
  `≤ N^{O(1)}` suffice);
* `Σ|a_i| < N` (otherwise the bound is trivial).

Then the saving `s = log(N/bound)` satisfies
`s ≤ C_A (log N)^{3/4}(log log N)^{3/4}` for N large (asymptotic only;
§0). With `G ≤ P(G)^{1+B}` for all moduli (B fixed),
`s ≤ C_{A,B}(log N)^{3/4}` (Thm 5.2). In particular **no method of this
class** proves `E(N) ≪ N exp(−(log N)^θ)` with `θ > 3/4`. Methods
outside the class are listed under "Still excluded" below.

*Proof.* *Projection (review).* Let `Q` be the lcm of the moduli of 𝔊;
`𝒜(𝔊)` is Q-periodic. Replace ν by its conditional average
`ν̄(n) = E[ν(n') | n' ≡ n (mod Q)]`. A term `a·1[n ≡ b (d)]` becomes
`a·(d'/d)·1[n ≡ b (d')]` with `d' = gcd(d,Q)` (or vanishes if the two
congruences are incompatible). So `ν̄ ≥ 0`, `ν̄ ≥ 1` on 𝒜, `Eν̄ = Eν`,
`T̄ = Σ|ā_i| ≤ T`, and every prime of every modulus of `ν̄` divides some
modulus of 𝔊, hence is `≤ N^A`.
*Coarsening.* Put `S = log(1/Eν)`; since the bound is `≥ N·Eν`, `s ≤ S`.
ET Lemma 2.9 applied to `ν̄` with `Λ₀ = A log N` and
`λ = Λ₀ + log T̄ + S ≤ (A+1)log N + S` gives a majorant ν' of 𝒜 of level
λ with `Eν' ≤ 2Eν`. Theorem 5.1 (resp. 5.2) gives
`S ≤ log 2 + Cλ^{3/4}(log λ)^{3/4}`. If `S ≤ (A+1)log N`, then
`λ ≤ 2(A+1)log N` and `S ≤ C_A(log N)^{3/4}(log log N)^{3/4}`. Otherwise
`λ ≤ 2S` and `S ≤ log 2 + C(2S)^{3/4}(log 2S)^{3/4}`, which bounds S by an
absolute constant, contradicting `S > (A+1)log N` for N large. ∎

*Side note on ET (review 1).* ET's "Consequence" after Lemma 2.9 writes
`λ ≤ (A+1)log N + s` with s the saving. Lemma 2.9 actually needs
`S = log(1/Eν) ≥ s` there. ET's conclusion survives by the same case
analysis as above.

**Architecture class covered.** Nonnegative CRT majorants of the *whole*
avoider set of any finite mixture of the four class types, used with the
coefficient-sum rounding bound. This includes (review 2, (C)):
* Bonferroni / inclusion–exclusion truncations;
* Selberg Λ² over any set system of these classes;
* β-/Rosser and any combinatorial upper-bound sieve on the class system;
* moment / variance methods evaluated by CRT (NONCRT Prop 4.1);
* the 3/4 note's selector majorant (Remark 5.4);
* the sequential, Λ² and Selberg-type majorants of ET, ETw, TW2–TW4 and EK.

In each case the rounding error is at least the merged `Σ|a_i|`.
Compared with EK Thm 4.5, the class drops `M ≤ P(M)^{1+B}` and adds
(a,D)-, Case-A and selector classes.

*Not transferred from the earlier files (review 2, D3).*
* **Montgomery's large sieve** is capped only fibrewise over ET prime
  slices (ET Remark 2.6; ET §6.1 item 8). It is not a pointwise
  majorant, and nothing here extends it to mixtures or composite
  moduli.
* **NONCRT Thm 2.3** (per-frequency rounding with weights `w ≥ 1`) is
  proved for ET Cor 3.4 families via ET's product/fibre argument, not
  for the KARY sequential construction. Cor 6.1 needs `Σ|a_i|` rounding.

**Still excluded:**
1. *Exact exponent vs. `(log log N)^{3/4}`.* Theorem 5.1 leaves a factor
   `(log λ)^{3/4}`, which comes only from smooth-dominated moduli
   (Remark 3.8). For unbounded-B families, a method saving
   `(log N)^{3/4}·ω(N)` with `ω ≤ (log log N)^{3/4}` is not excluded. It
   is expected not to exist (Remark 3.8), but that is unproved. Under
   bounded B it is excluded (Thm 5.2).
2. *Other class types.* The proof uses only three properties:
   * (i) no **W-smooth** class contains a *unit* square mod its modulus
     (for the base);
   * (ii) first moments `≪ (log y)³·polylog(log y)` over `P(G) ≤ y`;
   * (iii) cofactor second moments `≪ ℓ^{o(1)}`.

   Any family with (i)–(iii) is covered by the same proof.
   *Pointer, not checked here (review 2, D6):* Schinzel's theorem, as
   quoted in the introduction of ElT, says that no polynomial identity
   covers a class `b mod a` with b a quadratic residue mod a. That
   would make (i) automatic for polynomial-identity families, leaving
   (ii)–(iii) family-specific.
3. *Weaker majorant conditions (review 2, D4).* Theorem 5.1 needs `ν ≥ 1`
   on all of `𝒜(𝔊) ⊂ ℤ`. Excluded are majorants with:
   * `ν ≥ 0` only on `[1,N]`;
   * `ν ≥ 1` only on `𝒜 ∩ [1,N]`, or only on the exceptional set;
   * `ν ≥ 1` only on exceptional *primes*, used through prime
     equidistribution beyond a selector (ET §6.1 item 3).

   Selector classes cap the mean side of such prime-law methods by the
   same proof, but the BV-type error accounting is open and not claimed.
4. *Other methods:*
   * bounds using cancellation between frequencies (direct interval
     counts, Kloosterman / dispersion, Erdős–Turán / Vaaler; NONCRT
     §2.4);
   * per-frequency weights below 1;
   * the large sieve beyond prime slices;
   * non-CRT tuple counts or other genuinely arithmetic input (Type I/II,
     Halász);
   * slice primes beyond `N^{O(1)}`;
   * signed sieves whose error is not `Σ|a_i|`.
5. *External input.* The Case-A part uses ElT Prop. 1.4 (published, not
   re-proved), as ET Lemma 3.7 does. Families without Case-A classes use
   no external input.

## 7. Numerics (EVIDENCE only)

* `scripts/kary2_square_check.py`: Lemmas 2.1(2) and 2.2 by brute force.
  All 36,000 (a,D)-classes with `a ≤ 60`, `D ≤ 600` and all 34,884 Case-A
  classes with `d ≤ 6000` contain no square mod G; a control (shifted
  residues `c+1`) finds 280 squares among 2000, so the test is live.
  Output `data/kary2/square_check.txt`.
* `scripts/kary2_moments.py`: (1) Lemma 3.4 holds for all `n ≤ 10⁶`;
  the exponent actually needed there is ≤ 2.59 (the lemma uses 7).
  (2) The truncated smooth first moment
  `S(y,X) = Σ_{M≤X, M≡3(4), P(M)≤y}τ(A_M²)/M` with `X = 10⁷`: for
  `y ≤ 100` it changes by < 4% from `X = 10⁶` to `10⁷` (consistent with,
  not a bound on, a small remaining tail) and
  `S/(log y)³ ≈ 0.17–0.19`, consistent with Remark 3.8's heuristic
  `≍ (log y)³`. For `y ≥ 200` the truncation `X = 10⁷` is not converged
  (u ≤ 3), so those rows are lower bounds. Output `data/kary2/moments.txt`.

## Replay

```
cd scripts
# Lemmas 2.1(2), 2.2: no squares in (a,D)/Case-A classes (~1 s)
uv run --with sympy python kary2_square_check.py 60 600 6000 > ../data/kary2/square_check.txt
# Lemma 3.4 to 1e6; smooth first moments to X = 1e7 (~3 s, < 1 GB)
uv run --with numpy python kary2_moments.py 1000000 10000000 > ../data/kary2/moments.txt
```
