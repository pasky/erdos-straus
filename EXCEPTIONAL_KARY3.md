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

