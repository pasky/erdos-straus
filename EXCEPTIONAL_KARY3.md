# EXCEPTIONAL_KARY3 — removing the `(log log N)^{3/4}` loss from KARY2 Thm 5.1; truncated weights (task O28)

Status: **in progress (checkpoint 0).** Labels follow `DISCOVERIES.md`.
Notation follows `EXCEPTIONAL_KARY2.md` (K2), `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_THETA.md` (ET), `EXCEPTIONAL_TUPLES.md` (TU). **ElT** is
Elsholtz–Tao, arXiv 1107.1010 (J. Aust. Math. Soc. 2013); K2 already uses
its Prop 1.4 for Case A. **Shiu** is Shiu 1980, Theorem 1, in the form
quoted in `paper/es-threequarter-note.tex` §3 (and used in ET Lemma 3.1,
EK Lemma 4.2′, K2 Lemma 4.2).

## 0. Summary

(filled in at the end)

## 1. Where the loss comes from, and the idea

K2 Thm 5.1 loses `(log λ)^{3/4}` only through the first moment
(K2 Remark 3.8, §6 item 1):

    𝔐(y) = Σ_{C ∈ 𝔘, W < P(C) ≤ y} Γ(G)/G ≤ K₃(W)(log y)³(log log y)³   (K2 Cor 3.7).

The loss is in the ℛ(M)- and Case-A parts (the (a,D)- and selector parts
are pure Euler products, K2 Lemmas 3.3, 3.3′). There the weight
(`τ(A_M²)`, resp. `τ(4rh²+1)`) is a *shifted* divisor function, so
smoothness of the modulus cannot be exploited multiplicatively. K2
drops smoothness on `M ≤ y^{u₀}` and uses Rankin beyond. Rankin bounds a
dyadic block of y-smooth moduli by `e^{−u}` times the *whole* smooth sum,
which is `≍ log y`. So each block loses a full `log y`, and this forces
`u₀ ≍ log log y`, whence `u₀³ = (log log y)³`. (Hölder in place of
Cauchy–Schwarz, with any exponent, still loses `(log y)^{cε}` against a
gain `e^{−εu}` and gives the same `u₀ ≍ log log y`.)

**The fix: a local moment of the smooth part.** For a y-smooth M,
`log M = Σ_{p^ν | M} Λ(p^ν)`, and the normalised weight

    Z_y(M) = (1/log y) Σ_{p^ν | M, p^ν ≤ y} Λ(p^ν)

has **bounded mean** (`Σ_{p≤y} log p/(p log y) → 1`), unlike `Ω(M)` or
Rankin's `M^η`. For smooth M of size `y^u` it is `≳ u`. So a fixed
moment `E Z^k` gives the decay `u^{−k}`, and `k = 4` beats the
`u²` growth of the block masses. Expanding `Z^k` only imposes
`D | M` with `D ≤ y^k`, a congruence to a *small* modulus, so Shiu
(ℛ(M)) and ElT Thm 7.1 / Cor 7.4 (Case A) apply with no loss. No
Rankin step is needed at all.

## 2. The ℛ(M) first moment without loss

Throughout, `W ≥ 16` is as in K2, `Γ(m) = Π_{p|m}γ'(p)` (K2 §2:
`γ'(2) = 8`, `γ'(p) = 2p/(p−1) ≤ 3` for odd `p ≤ W`,
`γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` for `ℓ > W`), and `Γ = 1 ∗ h` with h
multiplicative, supported on squarefree numbers, `h(p) = γ'(p) − 1`; so
`h(p) ≤ 7` for `p ≤ W` and `h(ℓ) ≤ 2ℓ^{−1/2}` for `ℓ > W`. `𝒫_y` is the set
of prime powers `≤ y`. For `M ≥ 1` put

    Z_y(M) = (1/log y) Σ_{d ∈ 𝒫_y, d | M} Λ(d),
    S_y(M) = Π_{p | M, p^{v_p(M)} > y} p^{v_p(M)}.

**Lemma 2.1 (smooth numbers have a large local weight; PROVED).** Let
`y ≥ 2`, `K ≥ y`, `u = log K/log y`. If `K < M ≤ 2K` and `P(M) ≤ y`, then
`S_y(M)` is squarefull, and `S_y(M) > K^{1/2}` or `Z_y(M) ≥ u/2`. Hence,
for every `k ≥ 1`,

    1[P(M) ≤ y] ≤ 1[S_y(M) > K^{1/2}] + (2Z_y(M)/u)^k     (K < M ≤ 2K).

*Proof.* If `p | S_y(M)` then `p ≤ y < p^{v_p(M)}`, so `v_p(M) ≥ 2`. If
`p^{v_p(M)} ≤ y`, then all `p^ν`, `ν ≤ v_p(M)`, lie in `𝒫_y` and
`v_p(M)log p = Σ_{ν≤v_p(M)}Λ(p^ν)`. Since every prime of M is `≤ y`,
`log M ≤ log S_y(M) + Z_y(M)log y`. If `S_y(M) ≤ K^{1/2}`, then
`Z_y(M)log y ≥ log K − ½log K`. ∎

**Lemma 2.2 (moments of the local weight; PROVED, elementary).** For
`k ≥ 1` there is `C_k(W)` such that for `y ≥ 2`,

    Σ_{d₁,…,d_k ∈ 𝒫_y} Λ(d₁)⋯Λ(d_k) · Γ(D)/D ≤ C_k(W) (log y)^k,    D = lcm(d₁,…,d_k).

*Proof.* Group the indices by the prime of `d_i`: a set partition π of
`{1,…,k}` into blocks b, distinct primes `p_b ≤ y`, and exponents
`ν_i ≥ 1`. Then `Γ(D)/D = Π_b γ'(p_b) p_b^{−max_{i∈b}ν_i}`. For a block of
size m, `Σ_{ν∈ℕ^m} p^{−max ν} ≤ Σ_{t≥1} m t^{m−1} p^{−t} ≤ c_m/p` (as
`p^{−t} ≤ p^{−1}2^{1−t}`). Dropping distinctness, the partition π
contributes at most `Π_b c_{|b|} Σ_{p≤y} γ'(p)(log p)^{|b|}/p ≤
Π_b c_{|b|}(log y)^{|b|−1}Σ_{p≤y}γ'(p)log p/p`. By Mertens and
`γ'(p) ≤ 1 + 2p^{−1/2}` for `p > W`, `Σ_{p≤y}γ'(p)log p/p ≤ log y + c(W)
≤ c'(W) log y`. Summing over the Bell(k) partitions gives the claim. ∎

**Lemma 2.3 (smooth ℛ(M) blocks decay; PROVED, using Shiu).** Fix
`k ≥ 1`. There are `C_k(W)`, `y₀(k,W)` such that for `y ≥ y₀`,
`K ≥ y^{16k}` and `u = log K/log y`,

    Σ_{K<M≤2K, M≡3 (4), P(M)≤y} τ(A_M²)Γ(M) ≤ C_k(W) · K (log K)² · u^{−k}.

*Proof.* Write `Σ*` for the sum. By Lemma 2.1,
`Σ* ≤ Σ₁ + (2/u)^k Σ₂`, with `Σ₁` over `M ∈ (K,2K]` with
`S_y(M) > K^{1/2}`, and `Σ₂ = Σ_{K<M≤2K, M≡3(4)} τ(A_M²)Γ(M)Z_y(M)^k`
(smoothness dropped).

*Σ₁.* Pointwise `τ(A_M²)Γ(M) ≤ τ(A_M)²·8·3^{ω(M)} ≤ C_εK^ε`. The number
of squarefull `s ≤ t` is `≤ c t^{1/2}`, so `Σ_{s squarefull > Z}1/s ≤ c'Z^{−1/2}`
and `#{M ≤ 2K : S_y(M) > K^{1/2}} ≤ Σ_{s sqfull > K^{1/2}} 2K/s ≤ c''K^{3/4}`.
So `Σ₁ ≤ CK^{4/5}`.

*Σ₂.* Expanding `Z^k` and `Γ = 1∗h`,

    Σ₂ = (log y)^{−k} Σ_{d₁..d_k ∈ 𝒫_y} ΠΛ(d_i) Σ_{e} h(e) T(lcm(D,e)),
    T(q) = Σ_{K<M≤2K, M≡3(4), q | M} τ(A_M²).

`T(q) = 0` for even q. For odd q, `q | M` iff `A_M ≡ 4^{−1} (mod q)`, a
reduced class, and A runs over `((K+1)/4, (2K+1)/4]`. For `2 ≤ q ≤ K^{1/2}`
Shiu (`F(A) = τ(A²)`, `F(p) = 3`, `F(p^a) = 2a+1 ≤ 3^a`; `V = (2K+1)/4`,
`Y = K/4`, `α_s = β_s = 1/4`, K large) gives
`T(q) ≪ (K/(φ(q)log K))exp(Σ_{p≤K, p∤q}3/p) ≪ (K/q)(log K)²·(q/φ(q))Π_{p|q}e^{−3/p}
≤ C_S(K/q)(log K)²`, since `(1−1/p)^{−1}e^{−3/p} ≤ 1`. For q = 1,
`Σ_{A≤x}τ(A²) ≤ xΣ_{d≤x}2^{ω(d)}/d ≪ x(log x)²` (as `τ(·²) = 1∗2^ω`). For
every q, `T(q) ≤ (K/q + 1)C_εK^ε ≤ 3C_εK^{1+ε}/q` (`T(q) = 0` if `q > 2K`).

Now `D ≤ y^k ≤ K^{1/16}`, so `lcm(D,e) ≤ K^{1/2}` whenever `e ≤ K^{1/4}`.
* `e ≤ K^{1/4}`: `Σ_e h(e)/lcm(D,e) = D^{−1}Σ_e h(e)gcd(D,e)/e
  = D^{−1}Π_{p|D}(1+h(p))Π_{p∤D}(1+h(p)/p) ≤ c₁(W)Γ(D)/D`.
* `e > K^{1/4}`: `Σ_{e>Z}h(e)gcd(D,e)/e ≤ Z^{−1/4}Π_{p|D}(1+h(p)p^{1/4})
  Π_{p∤D}(1+h(p)p^{−3/4}) ≤ c₂(W)2^k Z^{−1/4}` (for `p > W`,
  `h(p)p^{1/4} ≤ 1`; `ω(D) ≤ k`; `h(p)p^{−3/4} ≤ 2p^{−5/4}`).

So `Σ_e h(e)T(lcm(D,e)) ≤ c₃(W)[Γ(D)K(log K)² + 2^kK^{1−1/16+ε}]/D`, and
Lemma 2.2 (with `Γ ≥ 1` for the second term) gives
`Σ₂ ≤ C_k(W)[K(log K)² + K^{1−1/20}]`.

Finally `K^{4/5} + K^{1−1/20} ≤ K(log K)²u^{−k}` once `K ≥ K₀(k)`
(`u ≤ log K`), which holds for `y ≥ y₀(k,W)`. ∎

**Corollary 2.4 (ℛ(M) first moment; PROVED, using Shiu).** For
`y ≥ y₀(W)`,

    𝔐_R(y) = Σ_{M ≡ 3 (4), P(M) ≤ y} τ(A_M²)Γ(M)/M ≤ K_R(W) (log y)³.

*Proof.* Take `k = 4`, `X = y^{64}`. *Body `M ≤ 2X`:* EK Lemma 4.2′
Steps 2–3 (smoothness dropped; no B used) give `≤ 1.3K₀(W)(log 2X)³ ≤
c(W)(log y)³`. *Tail:* the blocks `(K,2K]`, `K = 2^t ≥ X`, cover
`M > 2X`. By Lemma 2.3 a block contributes `≤ K^{−1}C₄K(log 2K)²u_t^{−4}
≤ 4C₄(log y)²u_t^{−2}`, `u_t = t log 2/log y`. Summing over
`t ≥ t₀ = ⌈log X/log 2⌉`:
`4C₄(log y)^4(log 2)^{−2}Σ_{t≥t₀}t^{−2} ≤ 8C₄(log y)⁴/(log 2·log X) =
(C₄/(8 log 2))(log y)³`. ∎

Remark 3.8 of K2 predicted exactly this order. No Rankin step and no
Cauchy–Schwarz is needed; the decay `u^{−4}` is crude (the truth is
`ρ(u)`-like) but sufficient, since the body masses grow only like `u²`.

## 3. The Case-A first moment without loss

Lemma 2.1 holds for any y-smooth m in the form: `log m ≤ log S_y(m) +
Z_y(m)log y`; so if `m ≥ Y` and `S_y(m) ≤ m^{1/2}` then
`Z_y(m) ≥ log Y/(2 log y)` (same proof).

Inputs from ElT §7 (published, not re-proved; the same paper and section
as the Prop 1.4 that K2 already uses, and Prop 1.4 is proved from them):
* **ElT Cor 7.4.** For natural `a, b, N` with `a, b ≤ N^{l}`:
  `Σ_{n≤N} τ(an+b) ≪_l τ(gcd(a,b)) N log N`.
* **ElT Thm 7.1.** For P of degree D, coefficients nonnegative integers
  `≤ N^l`, and `ρ_P(p^j) ≤ C` for all prime powers:
  `Σ_{n≤N} τ(P(n)) ≪_{D,l,C} N Σ_{m≤N} ρ_P(m)/m`.
* **ElT (7.10).** For `A, B > 1` and every positive integer k:
  `Σ_{a≤A} Σ_{m≤B} ρ_{ka}(m)/m ≪ A log B · log(1+k)`, where
  `ρ_{ka}(m) = #{b mod m : kab² + 1 ≡ 0 (mod m)}`. Its proof (ElT
  pp. 30–32: ranges `q < A`, `A ≤ q ≤ kA`, `q > kA` after quadratic
  reciprocity) uses no size condition on k; the condition
  `k ≪ (AB)^{O(1)}` of Prop 1.4 enters only through Thm 7.1.

**Lemma 3.1 (smooth Case-A blocks decay; PROVED, using ElT §7).** Fix
`k ≥ 1`. There are `C_k(W)`, `y₀(k,W)` such that for `y ≥ y₀`,
`K ≥ y^{64k}`, `u = log K/log y`,

    Σ_{r,h ≥ 1, K<rh≤2K, P(rh)≤y} τ(4rh²+1)Γ(4rh) ≤ C_k(W) · K (log K)² · u^{−k}.

*Proof.* `Γ(4rh) ≤ 8Γ(r)Γ(h)` (Γ submultiplicative, `γ'(2) = 8`).
Pointwise `τ(4rh²+1)Γ(4rh) ≤ C_εK^ε` (`4rh²+1 ≤ 17K²`). Split the pairs.

*(i) `r ≥ K^{1/4}`.* Then `h ≤ 2K^{3/4}`, r is y-smooth, and
`1 ≤ 1[S_y(r) > K^{1/8}] + (8Z_y(r)/u)^k`. The pairs with
`S_y(r) > K^{1/8}` number `≤ Σ_{h≤2K}Σ_{s sqfull > K^{1/8}} 2K/(hs) ≪
K^{1−1/16}log K`; with the pointwise bound they give `≪ K^{1−1/20}`. The
moment part, smoothness and the lower bound `rh > K` dropped, is at most

    8(8/u)^k (log y)^{−k} Σ_{d₁..d_k∈𝒫_y} ΠΛ(d_i) Σ_{s,t} h(s)h(t)
        Σ_{h≤2K^{3/4}, t|h} Σ_{r ≤ 2K/h, L | r} τ(4h²r + 1),    L = lcm(D, s).

Take first `s ≤ K^{1/16}`. Then `D ≤ y^k ≤ K^{1/64}`, `L ≤ K^{1/8}`, and
with `r = Lr'`, `r' ≤ R' = 2K/(hL)`, `R' ≥ K^{1/8}`. The linear form
`ar' + 1`, `a = 4h²L ≤ 16K^{13/8} ≤ R'^{14}`, has `gcd(a,1) = 1`, so ElT
Cor 7.4 (l = 14) gives `≪ R' log R' ≤ 2K log K/(hL)`. Summing over
`h = th'`: `Σ_{h'≤2K}1/(th') ≤ 2log K/t`. So these terms give
`≪ K(log K)²·(h(t)/t)·(h(s)/lcm(D,s))`, and
`Σ_t h(t)/t ≤ c(W)`, `Σ_s h(s)/lcm(D,s) ≤ c₁(W)Γ(D)/D` (§2). For
`s > K^{1/16}`, bound the inner sum trivially by `(2K/(hL))C_εK^ε` and use
`Σ_{s>Z}h(s)gcd(D,s)/s ≤ c₂(W)2^kZ^{−1/4}` (§2): total
`≪ 2^kK^{1+ε−1/64}(log K)/D`. Lemma 2.2 then bounds part (i) by
`C_k(W)[K(log K)²u^{−k} + K^{1−1/80}]`.

*(ii) `r < K^{1/4}`.* Then `h > K^{3/4}/2 ≥ K^{1/2}`, h is y-smooth, and
`1 ≤ 1[S_y(h) > K^{1/4}] + (4Z_y(h)/u)^k`. The squarefull pairs give
`≪ K^{1−1/20}` as in (i). The moment part is at most

    8(4/u)^k (log y)^{−k} Σ_{d} ΠΛ(d_i) Σ_{s,t} h(s)h(t)
        Σ_{r<K^{1/4}, s|r} Σ_{h' ≤ 2K/(rL)} τ(4rL²h'² + 1),    L = lcm(D, t).

Take `t ≤ K^{1/16}`, so `L ≤ K^{1/8}`. Fix r and put
`P(n) = 4rL²n² + 1`, `N = ⌊2K/(rL)⌋ ≥ K^{1/2}`; its coefficients are
`≤ 4K^{1/2} ≤ N²`. For `p | 2rL`, `P ≡ 1 (mod p)`, so `ρ_P(p^j) = 0`. For odd
`p ∤ rL`, `n ↦ Ln` is a bijection mod `p^j` carrying the roots of P to the
roots of `4rb² + 1`, so `ρ_P(p^j) = ρ_{4r}(p^j) ≤ 2` (Hensel: at a root,
`P'(n) = 8rL²n` is a unit). By CRT `ρ_P(m) ≤ ρ_{4r}(m)` for all m. ElT
Thm 7.1 (degree 2, l = 2, C = 2) gives
`Σ_{n≤N}τ(P(n)) ≪ (2K/(rL))Σ_{m≤2K}ρ_{4r}(m)/m`.
Write `r = sa`, so `ρ_{4r} = ρ_{ka}` with `k = 4s`, and split
`a ∈ [R, 2R)` dyadically (`≤ log K` ranges). By ElT (7.10) each range
gives `≪ (2K/(sRL))·2R·log(2K)·log(1+4s)`. So these terms give
`≪ K(log K)²·(h(s)log(1+4s)/s)·(h(t)/lcm(D,t))`, and
`Σ_s h(s)log(1+4s)/s ≤ c(W)` (as `log(1+4s) ≪ s^{1/4}` and
`Σ_s h(s)s^{−3/4} < ∞`). The terms `t > K^{1/16}` are bounded trivially
as in (i). Lemma 2.2 bounds part (ii) by
`C_k(W)[K(log K)²u^{−k} + K^{1−1/80}]`.

Finally `K^{1−1/80} ≤ K(log K)²u^{−k}` for `K ≥ K₀(k)`. ∎

**Corollary 3.2 (Case-A first moment; PROVED, using ElT §7).** For
`y ≥ y₀(W)`,
`𝔐_A(y) ≤ Σ_{r,h: P(rh)≤y} τ(4rh²+1)Γ(4rh)/(4rh) ≤ K_A(W)(log y)³`.

*Proof.* As Cor 2.4 with `k = 4` and `X = y^{256}`. The body `rh ≤ 2X`
is K2 Lemma 3.6's body (ET Lemma 3.7 with its γ-weight clause, which
rests on ElT Prop 1.4; partial summation): `≤ C(W)(log 2X)³`. The tail
blocks `(K,2K]`, `K = 2^t ≥ X`, sum to `≤ C(W)(log y)³` by Lemma 3.1
exactly as in Cor 2.4. ∎

**Corollary 3.3 (all four types; PROVED; Case A via ElT).**
`𝔐(y) ≤ 𝔐_R + 𝔐_{aD} + 𝔐_A + 𝔐_S ≤ K₃′(W)(log y)³` for `y ≥ y₀(W)`
(Cor 2.4, K2 Lemmas 3.3, 3.3′, Cor 3.2).

## 4. The cap with no B and no log loss

**Theorem 4.1 (K2 Thm 5.1 without the `(log λ)^{3/4}`; PROVED; the
Case-A part uses ElT §7, published, not re-proved).** There are absolute
constants `W, λ₀, C` such that for every finite family 𝔊 of ℛ(M)-,
(a,D)-, Case-A and selector classes, mixed arbitrarily, with arbitrary
moduli, and every majorant ν of level `λ ≥ λ₀` of the whole avoider set
`𝒜(𝔊) ⊂ ℤ` (K2 Thm 5.1's definitions),

    log(1/Eν) ≤ C λ^{3/4}.

If 𝔊 has no Case-A classes, the only external input is Shiu's theorem
(as in K2).

*Proof.* K2 Thm 5.2's proof verbatim, i.e. EK Thm 4.5's block structure
with `s₁ = λ^{1/4}`, the square base (K2 Lemma 2.3) and the B-free leak
(K2 Lemma 4.3), with the first moment `𝔐(y) ≤ K₃′(log y)³` of Cor 3.3 in
place of the B-bounded one. Explicitly (K2 §5's ledger with
`(log λ)³` deleted):
* singletons `W < ℓ ≤ e^{s₁}`: `≤ (8/3)𝔐(e^{s₁}) ≤ (8/3)K₃′λ^{3/4}`;
* block `V_i` (`s = 2^is₁`, `d_i = ⌊λ/s⌋`): `E M_{V_i} ≤ 𝔐(e^{2s}) ≤ 8K₃′s³`,
  so `(E M_{V_i} + 4d_i)/d_i ≤ 16K₃′s⁴/λ + 4 = 16K₃′·16^i + 4`, and by EK
  Cor 2.6 and Jensen `EΦ_i ≤ (λ/(2^is₁))(c₁ + i log 16) + O(log λ)`;
  `2Σ_iEΦ_i ≤ Cλ^{3/4} + O(log²λ)`;
* linear block `(e^{λ/2}, e^λ]`: `2log(1+3e^{−λ/4})`; above `e^λ`: 0;
* base and Jensen: `2W + log 2`.

W is fixed by the leak (K2 Lemma 4.3, `𝔏 ≤ 1/2` for `W ≥ W₀`), and
`K₃′ = K₃′(W)` is then absolute. ∎

**Corollary 4.2 (K2 Cor 6.1 without the loss; PROVED; same proviso).**
For every method in the class of K2 Cor 6.1 (coefficient-sum rounding
`N·Eν + Σ|a_i|`, `Σ|a_i| < N`, ν a nonnegative CRT majorant of the whole
avoider set of any finite mixture of the four types, family primes
`≤ N^A`), the saving is `s ≤ C_A(log N)^{3/4}` for N large. No
B-hypothesis, no dominant prime, no bound on the number of prime factors.

*Proof.* K2 Cor 6.1's proof (projection, ET Lemma 2.9, case analysis)
with Theorem 4.1 in place of K2 Thm 5.1: if `S ≤ (A+1)log N` then
`λ ≤ 2(A+1)log N` and `S ≤ log 2 + C(2(A+1)log N)^{3/4}`; otherwise
`λ ≤ 2S` and `S ≤ log 2 + C(2S)^{3/4}` bounds S absolutely. ∎

So K2 §6 "Still excluded" item 1 is closed: **the 3/4 note's exponent is
sharp for every coefficient-sum CRT majorant of any forced-class
mixture, with no `(log log N)^{3/4}` slack.** The saving of the 3/4 note
is `c(log N)^{3/4}` and the cap is `C(log N)^{3/4}`; only the constants
differ (and are incomparable: ineffective vs astronomically large).

### 4.3 Downstream statements that improve the same way

Each of these used K2 Thm 5.1 (or its first moment) only through the cap
`Cλ^{3/4}(log λ)^{3/4}`; with Theorem 4.1 the factor `(log λ)^{3/4}`
(resp. `(log log N)^{3/4}`) disappears. Not re-reviewed here; the parent
should re-check each pointer.
* **PRIMELAW Thm 3.1 / Cor 4.2 ((D)22).** Its first moment `𝔐*` is K2's
  with Γ replaced by `Γ*` (`γ*(ℓ) = (ℓ/(ℓ−1))(1−ℓ^{−1/2})^{−1}`). §§2–3
  above use Γ only through: `h(p) ≤ 7` for `p ≤ W`, `h(ℓ) ≤ 2ℓ^{−1/2}` and
  `γ'(ℓ) ≤ 1 + 2ℓ^{−1/2}` for `ℓ > W`, `Γ(m) ≤ 8·3^{ω(m)}`, and
  submultiplicativity. PRIMELAW Lemma 2.3 gives all of these for `Γ*`.
  So `𝔐*(y) ≪_W (log y)³` and PRIMELAW's cap becomes `Cλ^{3/4}`, i.e.
  `C_A(log N)^{3/4}` for prime-law methods with moduli `≤ N^A`.
  (PRIMELAW Cor 4.2's coarsening adds `2log log(·)` to the level, which
  is harmless.)
* **LARGESIEVE Thm 3.1 / Cor 3.2 ((D)19):** `C(log N)^{3/4}` for
  polynomial denominators, no B.
* **INTERFREQ Cor 2.3 ((D)20):** majorants from forced classes of modulus
  `≤ N/2`, any evaluation of the interval sum: `C(log N)^{3/4}`.
* **TUPLES Cor 3.4 ((D)21):** `log(1/Eν) ≤ C(kA log N)^{3/4}`, so saving
  `(log N)^θ` needs `k ≥ c(log N)^{4θ/3−1}` exactly (no `−o(1)`). The
  remaining gap is §5.

