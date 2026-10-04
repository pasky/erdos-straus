# EXCEPTIONAL_KARY2 — the 3/4 cap without the B-hypothesis, for ℛ(M), (a,D) and Case-A classes (task O14)

Status: **checkpoint 1 (draft, not yet reviewed).** Labels follow
`DISCOVERIES.md`. Notation follows `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_TWIN.md` (ETw), `EXCEPTIONAL_TWIN4.md` (TW4) and
`EXCEPTIONAL_THETA.md` (ET).

## 0. Summary

(filled in at the end)

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
  4.2(3) and 4.3): the pointwise bound `τ(A_q²) ≤ ℓ^{o(1)}`, valid because
  the cofactor q of the top prime power is `≤ ℓ^B`; and the constants
  `W₀(B)`, `C(B)`.

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
To add (a,D)- and Case-A classes, the base must also avoid their
W-smooth classes; that is §2.

## 2. The three class types and the square base

**Definition 2.0 (forced-class families).** A *class* is `n ≡ b (mod G)`.
The three types, with the multiplicity bounds used below:

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

Every class of each type is forced for every `n ≥ 1` (notes Lemmas 16.1,
18.1; ET Lemma 3.2; ET §3 Case A). A *family* 𝔊 is any finite set of
classes of these types, mixed arbitrarily, with **no condition on the
moduli** (no B, no dominant prime, any number of primes at any scale).

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

**Lemma 2.3 (square base; PROVED).** Fix `W ≥ 3`. Let `Q₀` be a common
multiple of `8·P_W` and of the W-smooth parts of all moduli of 𝔊 (`P_W`
the product of the primes ≤ W). Put

    R_W^□ = { c mod Q₀ : c mod p^e is a unit square for every p^e ∥ Q₀ }.

1. (R1) Every `c ∈ R_W^□` avoids every class of 𝔊 whose modulus is
   W-smooth.
2. `log(Q₀/|R_W^□|) = 3 log 2 + Σ_{3≤p≤W} log(2p/(p−1)) ≤ 2W`.
3. (R2) Under the uniform law on `R_W^□`, residues at distinct primes are
   independent, and `P(c ≡ a (mod p^e)) ≤ γ(p)/p^e` for `p^e | Q₀`, with
   `γ(p) = 2p/(p−1)` for odd p and `γ(2) = 8`.

*Proof.* 1. Let the class be `b (mod G)`, G W-smooth, so every `p^e ∥ G`
divides `Q₀`. If `c ≡ b (mod G)` and c is a unit square mod every
`p^e ∥ Q₀`, then by CRT `b ≡ c` is a square mod G, contradicting Lemma 2.1
or 2.2. 2. By CRT `R_W^□` is a product. Unit squares mod `p^e` (p odd)
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

where 𝔘 is the *universe* of all classes of the three types (each class
counted once per parametrisation; this only over-counts). EK Lemma 4.2′
Step 1 bounds the expected (light or not) block mass by this sum:
`E_{Q'} Σ_{ℓ ∈ V} p_ℓ ≤ 𝔐(max V)`, for every family 𝔊 ⊆ 𝔘 (Step 1 uses
only the chain rule, now with the square base, and `Γ(q)ℓ^{−v} ≤ Γ(G)/G`
for `G = qℓ^v`). The three types are bounded separately:
`𝔐 ≤ 𝔐_R + 𝔐_{aD} + 𝔐_A`.

**Lemma 3.1 (smooth Euler products, Rankin; PROVED, standard).** Let
`F ≥ 0` be multiplicative with `F(p^e) ≤ H(e+1)^a` for all p, e, and
`F(p) ≤ κ + H p^{−1/2}` for `p > W`. Let `y ≥ y₀(W)`, `η ∈ {0, 1/log y}`.
Then

    Σ_{P(m) ≤ y} F(m) m^{−1+η} ≤ C(H,a,κ,W) (log y)^κ,

and for `K ≥ 1`, with `u = log K/log y`,

    Σ_{K < m ≤ 2K, P(m) ≤ y} F(m)/m ≤ C(H,a,κ,W) e^{−u} (log y)^κ.

*Proof.* The sum is `Π_{p≤y}(1 + Σ_{e≥1}F(p^e)p^{−e(1−η)})`. Since
`p ≤ y`, `p^{eη} ≤ e^e`, so for `p ≥ 3` the terms `e ≥ 2` total
`≤ C(H,a)p^{−2}`; for `p = 2` the series converges since
`2^{1−η} ≥ 2e^{−ln2/ln y₀} > 1`. The finitely many `p ≤ W` give a
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
(`log 2K ≤ 2u log y` as `u ≥ 1`). The function `φ(u) = e^{−u/2}u^4`
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

    Σ_{r, h ≥ 1, rh ≤ K} τ(k r h² + 1)^q ≤ C_q K (log 2kK)^{c_q},    c_q = 2^{7q+1} + 2.

*Proof.* `N = krh² + 1` is odd, so all its divisors are odd. Cover
`{rh ≤ K}` by dyadic boxes `r ∈ [R,2R)`, `h ∈ [H,2H)` (`R, H` powers of 2,
`RH ≤ K`); `Σ_{boxes} RH ≤ K(log₂K + 1)`.
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

**Lemma 3.6 (Case-A first moment without B; PROVED modulo Elsholtz–Tao
Prop. 1.4).** For `y ≥ y₀(W)`,

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
the tail is `≤ C(log y)^{2+c₂/2}u₀^{c₂/2}e^{−u₀/2}·(log y) ≤ C`. ∎

*On the citation.* ET Prop. 1.4 (Elsholtz–Tao 2013) is used only for the
body, exactly as in ET Lemma 3.7; it is what gives the exponent 2 of
`log x`. Lemma 3.5 is self-contained but its exponent `c₂ = 2^{15}+2` is
useless except against Rankin's `e^{−u/2}`. So the ℛ(M)- and (a,D)-parts
of everything below are unconditional, and the Case-A part carries the
same external dependence as ET Lemma 3.7 (DISCOVERIES (D)11).

**Corollary 3.7 (all three types; PROVED, Case A modulo ET Prop 1.4).**
`𝔐(y) ≤ K₃(W)(log y)³(log log y)³` for `y ≥ y₀(W)`.

**Remark 3.8 (where the `(log log y)³` comes from).** Heuristically
`𝔐_R(y) ≍ (log y)³`: `τ(A_M²)` should average `≍ log² M` also over
y-smooth M, and `Σ_{P(M)≤y}(log M)²/M ≍ (log y)³`. Our proof drops the
smoothness on `M ≤ y^{u₀}` and pays `u₀³`; the decay that kills the tail
comes from Rankin, which costs a full `log y` per block and forces
`u₀ ≍ log log y`. A bound `Σ_{M≤x, P(M)≤y}τ(A_M²) ≪ Ψ(x,y)(log x)²`
(shifted smooth numbers, Fouvry–Tenenbaum type) would remove the loss in
𝔐_R; it is not needed for the exponent.
