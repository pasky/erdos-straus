# EXCEPTIONAL_KARY3 — removing the `(log log N)^{3/4}` loss from KARY2 Thm 5.1; truncated weights (task O28)

Status: **checkpoint 2, reviewed.** Self-review
(`reviews/kary3-self-review.md`, D1–D7 applied); independent hostile
review R28 (`reviews/exceptional-kary3-review.md`, branch
`side-agent/review-kary3`): all claims SOUND, MINOR defects 1–5 applied.
**Dependencies (R28 defect 5):** the PROVED labels of Thms 4.1 and 5.1
rest on the K2/EK framework as reviewed there (square base K2 Lemma 2.3,
leak K2 Lemma 4.3, EK Thm 4.1 / Cor 2.6, ETw Prop 4.1 / Cor 4.3) and on
the bodies of EK Lemma 4.2′ and K2 Lemma 3.6, none re-proved here;
i.e. "PROVED given K2/EK as reviewed". Labels follow `DISCOVERIES.md`.
Notation follows `EXCEPTIONAL_KARY2.md` (K2), `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_THETA.md` (ET), `EXCEPTIONAL_TUPLES.md` (TU). **ElT** is
Elsholtz–Tao, arXiv 1107.1010 (J. Aust. Math. Soc. 2013); K2 already uses
its Prop 1.4 for Case A. **Shiu** is Shiu 1980, Theorem 1, in the form
quoted in `paper/es-threequarter-note.tex` §3 (and used in ET Lemma 3.1,
EK Lemma 4.2′, K2 Lemma 4.2).

## 0. Summary

| item | statement | label |
|---|---|---|
| §1 | the K2 loss is Rankin's: each dyadic block of smooth moduli is bounded by `e^{−u}` times the *whole* smooth sum (`≍ log y`), forcing `u₀ ≍ log log y`; Hölder variants lose the same | Assessment (inspection) |
| Lemmas 2.1–2.2 | local weight `Z_y(M) = Σ_{p^ν|M, p^ν≤y}Λ(p^ν)/log y`: `≥ u/2` on smooth M of size `y^u` (up to a squarefull part), and its k-th moments against `Γ(D)/D` are `≪_k (log y)^k` | PROVED (elementary) |
| Lemma 2.3, Cor 2.4 | smooth ℛ(M) blocks: `Σ_{K<M≤2K, P(M)≤y}τ(A_M²)Γ(M) ≪ K(log K)²u^{−4}`; hence `𝔐_R(y) ≪ (log y)³` | PROVED (Shiu) |
| Lemma 3.1, Cors 3.2–3.3 | the same for Case A (split by `r ≷ K^{1/4}`; ElT Cor 7.4 resp. Thm 7.1 + (7.10)); all four types: `𝔐(y) ≤ K₃′(W)(log y)³` | PROVED (Case A uses ElT §7, published, not re-proved) |
| **Thm 4.1** | **K2 Thm 5.1 without loss: every mixture of ℛ(M)-, (a,D)-, Case-A and selector classes, arbitrary moduli (no B): `log(1/Eν) ≤ Cλ^{3/4}`** | PROVED (same proviso) |
| Cor 4.2 | coefficient-sum CRT methods: saving `≤ C_A(log N)^{3/4}`; the `(log log N)^{3/4}` of K2 Cor 6.1 / (D)18 is gone | PROVED (same proviso) |
| §4.3 | (D)19 LARGESIEVE, (D)20 INTERFREQ, (D)22 PRIMELAW, (D)21 TU Cor 3.4 lose the same factor (pointers; PRIMELAW's Γ* checked to satisfy the hypotheses used) | PROVED modulo the cited files (pointer-level) |
| **Thm 5.1** | truncated weights `min(log ℓ, L₀)`, `L₀ ≤ λ`: `log(1/Eν) ≤ Cλ^{3/4} + 2d₀log(C(1+Λ³/d₀)) + O(d₀)`, `d₀ = ⌊λ/L₀⌋`, family primes `≤ e^Λ` | PROVED (same proviso) |
| Cor 5.2 | TU Cor 3.4 window closed for **prime order**: (A log N, k)-mixed majorants of any K2 family save `≤ C_A[(log N)^{3/4} + k log log N]` | PROVED (same proviso) |
| Cor 5.3 | class order k when every modulus has `≤ r` primes above the fixed W: `≤ C_A[(log N)^{3/4} + kr log log N]`; open: `max(L^{4θ/3−1}, L^θ/(r log L)) ≲ k ≲ L^θ/log L` for unbounded r | PROVED / open part stated |
| §6 | TW4 middle window: every Λ² sieve over every K2 family saves `≤ CL^{3/4}` for all r (Thm 4.1 applies; no ω-hypothesis) | PROVED (corollary) |
| §7 | Lemma 7.1: TW4's Λ² setting checked at text level (g² is a K2 level-λ majorant; all primes charged), so TW4 Thm 7.1 / middle window are superseded as caps. Lemma 7.2: an `N^A`-prime-power class with `log d ≤ (k−1)A log N/2` is an intersection of `≤ k` classes of modulus `≤ N^A`; so TU Cor 3.4's literal hypothesis is a level-`≍kL` hypothesis and its window cannot be closed from that hypothesis alone | PROVED |
| §8 | smooth first moments `≍ (log y)³` up to `X = 10¹²`, block profile `max u⁴b = 0.385` (all complete blocks) | EVIDENCE |

Constants are absolute but astronomically large (as in K2); everything
is asymptotic only.

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
`Σ* ≤ Σ₁ + (2/u)^k Σ₂`, with `Σ₁` over the **y-smooth** `M ∈ (K,2K]` with
`S_y(M) > K^{1/2}` (smoothness must be kept here: for non-smooth M,
`S_y(M)` need not be squarefull; review D4), and `Σ₂ = Σ_{K<M≤2K, M≡3(4)} τ(A_M²)Γ(M)Z_y(M)^k`
(smoothness dropped).

*Σ₁.* Pointwise `τ(A_M²)Γ(M) ≤ τ(A_M)²·8·3^{ω(M)} ≤ C_εK^ε`. The number
of squarefull `s ≤ t` is `≤ c t^{1/2}`, so `Σ_{s squarefull > Z}1/s ≤ c'Z^{−1/2}`
and, since for y-smooth M the number `S_y(M)` is a squarefull divisor of M
(Lemma 2.1),
`#{M ≤ 2K : P(M) ≤ y, S_y(M) > K^{1/2}} ≤ Σ_{s sqfull > K^{1/2}} 2K/s ≤ c''K^{3/4}`.
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
Z_y(m)log y`, with `S_y(m)` squarefull (same proof). So:

    (2.1′)  m ≥ Y, P(m) ≤ y, S_y(m) ≤ T   ⇒   Z_y(m) log y ≥ log(Y/T).

Lemma 3.1 uses (2.1′) with `(Y,T) = (K^{1/4}, K^{1/8})` (giving
`Z ≥ u/8`) and `(Y,T) = (K^{3/4}, K^{1/4})` (giving `Z ≥ u/2`).

Inputs from ElT §7 (published, not re-proved; the same paper and section
as the Prop 1.4 that K2 already uses, and Prop 1.4 is proved from them):
* **ElT Cor 7.4.** For natural `a, b, N` with `a, b ≤ N^{l}`:
  `Σ_{n≤N} τ(an+b) ≪_l τ(gcd(a,b)) N log N`.
* **ElT Thm 7.1.** For P of degree D, coefficients nonnegative integers
  `≤ N^l`, and `ρ_P(p^j) ≤ C` for all prime powers:
  `Σ_{n≤N} τ(P(n)) ≪_{D,l,C} N Σ_{m≤N} ρ_P(m)/m`.
* **ElT (7.10).** For `A, B ≥ 2` and every positive integer k:
  `Σ_{a≤A} Σ_{m≤B} ρ_{ka}(m)/m ≪ A log B · log(1+k)`, where
  `ρ_{ka}(m) = #{b mod m : kab² + 1 ≡ 0 (mod m)}`. Its proof (ElT
  pp. 30–32: ranges `q < A`, `A ≤ q ≤ kA`, `q > kA` after quadratic
  reciprocity) uses no size condition on k; the condition
  `k ≪ (AB)^{O(1)}` of Prop 1.4 enters only through Thm 7.1.
  *Source caveat (self-review):* ElT p. 31 says the small-q character
  `a ↦ (−ka/q)` has mean zero for every q; this fails for square q
  (including q = 1). Square q contribute at most
  `A log B·Σ_{q square}1/q = O(A log B)`, so (7.10) holds as stated,
  uniformly in k. (Cor 7.4 is used with `N ≥ 2`.) A second slip (review
  R28): in the range `q > kA`, ElT's `c(q)` omits the reciprocity sign
  `(−1)^{((q−1)/2)((k′a−1)/2)}`. For fixed a the corrected factor is still
  8-periodic in q, and `q ↦ (−ka/q)` is the Kronecker character of the
  negative number `−ka`, never principal (even if `k′a` is a square), so
  the mean-zero / partial-summation step holds with an absolute constant,
  uniformly in k.

**Lemma 3.1 (smooth Case-A blocks decay; PROVED, using ElT §7).** Fix
`k ≥ 1`. There are `C_k(W)`, `y₀(k,W)` such that for `y ≥ y₀`,
`K ≥ y^{64k}`, `u = log K/log y`,

    Σ_{r,h ≥ 1, K<rh≤2K, P(rh)≤y} τ(4rh²+1)Γ(4rh) ≤ C_k(W) · K (log K)² · u^{−k}.

*Proof.* `Γ(4rh) ≤ 8Γ(r)Γ(h)` (Γ submultiplicative, `γ'(2) = 8`).
Pointwise `τ(4rh²+1)Γ(4rh) ≤ C_εK^ε` (`4rh²+1 ≤ 17K²`). Split the pairs.

*(i) `r ≥ K^{1/4}`.* Then `h ≤ 2K^{3/4}`, r is y-smooth, and
`1 ≤ 1[S_y(r) > K^{1/8}] + (8Z_y(r)/u)^k` (by (2.1′)). The pairs with r y-smooth and
`S_y(r) > K^{1/8}` (so r has a squarefull divisor `> K^{1/8}`) number `≤ Σ_{h≤2K}Σ_{s sqfull > K^{1/8}} 2K/(hs) ≪
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

*(ii) `r < K^{1/4}`.* Then `h > K^{3/4}` (as `rh > K`), h is y-smooth, and
`1 ≤ 1[S_y(h) > K^{1/4}] + (2Z_y(h)/u)^k` (by (2.1′)). The pairs with h y-smooth and
`S_y(h) > K^{1/4}` (squarefull divisor of h) give
`≪ K^{1−1/20}` as in (i). The moment part is at most

    8(2/u)^k (log y)^{−k} Σ_{d} ΠΛ(d_i) Σ_{s,t} h(s)h(t)
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
* **TUPLES Cor 3.4 ((D)21)** (under its hypothesis that the intersected
  class moduli are `≤ N^A`): `log(1/Eν) ≤ C(kA log N)^{3/4}`, so saving
  `(log N)^θ` needs `k ≥ c(log N)^{4θ/3−1}` exactly (no `−o(1)`). The
  remaining gap is §5.

## 5. Truncated weights: closing the TUPLES Cor 3.4 window (TU §6 item 2)

**Definition 5.0.** Fix `L₀ > 0` and weights `s_ℓ = min(log ℓ, L₀)` on
primes `ℓ > W`. A term `a·1[n ≡ b (mod d)]` has *truncated level*
`Σ_{ℓ|d, ℓ>W} s_ℓ` and *prime order* `ω_{>W}(d)`. ν has truncated level
`≤ λ` if every term does. ν is *(λ₀, k)-mixed* (TU Def 3.0, for K2
families) if every term has level `≤ λ₀` or prime order `≤ k`. With
`L₀ = λ₀/k`, a (λ₀,k)-mixed ν has truncated level `≤ λ₀`.

**Theorem 5.1 (truncated-weight cap; PROVED; Case A via ElT §7).** Let
W, λ₀ (the threshold), `K₃′` be as in Theorem 4.1. Let 𝔊 be any finite
K2 family whose moduli have all prime factors `≤ e^Λ`, and ν ≥ 0 on ℤ,
`≥ 1` on `𝒜(𝔊)`, of truncated level `≤ λ` with `λ₀ ≤ λ ≤ Λ` and
`L₀ ≤ λ`. Put `d₀ = ⌊λ/L₀⌋ ≥ 1`. Then

    log(1/Eν) ≤ C λ^{3/4} + 2d₀ log(C₀(K₃′Λ³ + 4d₀)/d₀) + (8/3)d₀ + log(22d₀+22) + 6.

In particular, if `d₀ ≤ Λ³`, `log(1/Eν) ≤ Cλ^{3/4} + C′d₀ log(Λ+2)`.
(For `L₀ > λ` no prime with `log ℓ > λ` can occur in a term, the truncated
level is the ordinary level, and Theorem 4.1 applies. At `L₀ = λ` the
proof below works with `d₀ = 1`; review D7.)

*Proof.* EK Thm 4.1 holds for any class 𝓕 of functions that is closed
under `f ↦ E_U[f | coordinates before a block]` and under fixing earlier
coordinates, provided (S_w) holds for every `f ≥ 0` in 𝓕. Take 𝓕 = sums
of terms each depending on the coordinates of a prime set T with
`Σ_{ℓ∈T} s_ℓ ≤ λ`. Conditioning on coordinates only shrinks T, so 𝓕 is
closed; the induction of EK Thm 4.1 (ETw Thm 2.3′) uses nothing else
about "λ-level". Order the primes increasingly:
* singletons `W < ℓ ≤ e^{min(s₁,L₀)}`, `s₁ = λ^{1/4}`;
* sequential blocks `V_i = {ℓ : 2^is₁ < log ℓ ≤ min(2^{i+1}s₁, L₀, λ/2)}`
  (nonempty ones only); for `ℓ ∈ V_i`, `s_ℓ = log ℓ > 2^is₁ = s`, so
  every `f ∈ 𝓕` is `⌊λ/s⌋`-local on `V_i`;
* if `L₀ > λ/2`, the linear block `(e^{λ/2}, e^{L₀}]` (every f is 1-local
  there; ETw Cor 4.3 applied to this sub-block of K2's `(e^{λ/2}, e^λ]`,
  pointer-level as in K2/EK);
* one **top block** `V_top = {ℓ : log ℓ > L₀}` (all remaining primes);
  there `s_ℓ = L₀`, so every `f ∈ 𝓕` is `d₀`-local on `V_top`.

The costs of the first three kinds are bounded by Theorem 4.1's ledger
(only a subset of its blocks occurs, with the same d's):
`≤ Cλ^{3/4} + O(log²λ)`. The top block is an EK sequential step
(Thm 2.5 is arithmetic-free: any ordered block, any d-local f) with
`d = d₀`, `m̄ = 𝔐(e^Λ) ≥ E M_{V_top}` (K2 §3: `E Σ_{ℓ∈V}p_ℓ ≤ 𝔐(max V)`;
primes above `e^Λ` carry no class and add nothing),
and `𝔐(e^Λ) ≤ K₃′Λ³` (Cor 3.3). As in K2 §5, t is chosen per history,
`t(h) = d₀/(E[M|h] + 4d₀)`, and EK Cor 2.6 plus Jensen over histories
(concavity in `E[M|h]`) gives
`EΦ_top ≤ d₀log(C₀(K₃′Λ³+4d₀)/d₀) + (4/3)d₀ + ½log(22d₀+22) + 3`, doubled
by EK Thm 4.1. *(R28 defect 4.)* When `L₀ > λ/2`, `d₀ = 1` and every
prime of `V_top` exceeds `e^{λ/2}`, so `V_top` may instead be treated as a
linear block: ETw Cor 4.3's argument uses only 1-locality and the caps
`δ_ℓ ≤ e^{−λ/4}` (not the width of the block), giving cost
`≤ 2log(1+3e^{−λ/4})` in place of `≈ 2log(C₀(K₃′Λ³+4))` (pointer-level).
The leak bound K2 Lemma 4.3 is per prime (`𝔏 ≤ Σ_{ℓ>W}
ℓ^{1/2}E p_ℓ²`, every class decided at its top prime under any
increasing-order block structure with caps `ℓ^{−1/2}`), so `𝔏 ≤ 1/2` still.
The base adds `2W + log 2`. ∎

**Corollary 5.2 (TU Cor 3.4 at full strength for prime order; PROVED).**
Let 𝔊 be any finite K2 family with all family primes `≤ N^A`, and ν a
majorant of `𝒜(𝔊)` every term of which has level `≤ A log N` or prime
order `≤ k` (`1 ≤ k ≤ (A log N)^3`). Then

    log(1/Eν) ≤ C_A [ (log N)^{3/4} + k log log N ].

So for methods with `B ≥ ½N·Eν` (CRT-main-term evaluation, TU Cor 3.3),
a saving `(log N)^θ`, θ > 3/4, needs prime order `k ≥ c_A(log N)^θ/log log N`:
the TU Cor 3.2/3.3 conclusion, now for **all** K2 families
(ℛ(M), (a,D), Case A, selector; arbitrary composite moduli), with no
selector term `log(P/φ(P))`.

*Proof.* Project first as in K2 Cor 6.1, so that all moduli divide the
family lcm; this shrinks every prime set, so both term types are
preserved, and all primes are then `≤ N^A = e^Λ`, `Λ = A log N`. For
`k = 1` every term has level `≤ Λ` (a single prime `≤ e^Λ`, or level
`≤ A log N`), and Theorem 4.1 with `λ = Λ` applies. For `k ≥ 2` apply
Theorem 5.1 with `λ = Λ`, `L₀ = λ/k < λ`, `d₀ = k`. If `k > λ` then
`L₀ < 1 < log W` and every prime is in the top block; the bound still
holds. ∎

**Corollary 5.3 (class order with boundedly many large primes; PROVED).**
Suppose every modulus of 𝔊 has at most r prime factors `> W` (W the
absolute constant of Theorem 4.1, **not** a moving cutoff). Then an
intersection of k classes of 𝔊 (or of any residue classes whose moduli
have `≤ r` primes `> W`) has prime order `≤ kr`. Hence (λ₀ = A log N,
class order k) majorants satisfy
`log(1/Eν) ≤ C_A[(log N)^{3/4} + kr log log N]` (family primes `≤ N^A`),
and a saving `(log N)^θ` needs `kr ≥ c(log N)^θ/log log N`. For bounded r
this is the full TU Cor 3.2/3.3 conclusion.

*Scope warning (review D1).* Bounded r is measured above the fixed W.
The twin / η-twin moduli of TW2–TW4 and the `ℛ(kℓ)` atoms of the 3/4
note have two (resp. one) primes above a **moving** cutoff (`(log X)^8`,
resp. `ℓ`), with a cofactor that may contain arbitrarily many primes
above W; they are covered by Theorem 4.1, but **not** by Corollary 5.3
unless their cofactors are W-smooth or have bounded `ω_{>W}`.

**What is still open (exact scope; reviews D2, D3).** Assume, as TU Cor
3.4 does, that the intersected classes have moduli `≤ N^A` (this, not
merely family primes `≤ N^A`, is what bounds the level of a k-fold
intersection by `kA log N`). Put `L = log N`, `r = max_G ω_{>W}(G)`
(`r ≤ AL/log W`). The proved necessary conditions for a saving `L^θ`
under CRT-main-term evaluation are then

    k ≳ max( L^{4θ/3−1}, L^θ/(r log L) )      (TU Cor 3.4 + §4.3; Cor 5.3).

The prime-slice benchmark is `k ≳ L^θ/log L` (TU Cor 3.3, and Cor 5.2
for prime order). So what is not excluded is class order k in

    max( L^{4θ/3−1}, L^θ/(r log L) ) ≲ k ≲ L^θ/log L,

nonempty only when r → ∞. The obstruction is structural: EK Thm 2.5's
locality is in prime coordinates, and a class with many large primes is
many-local; a class-coordinate version would need a k-ary comparison for
the dependent indicators `1[n ∈ C]`. Not attempted.

## 6. Goal (3): the TW4 middle window is subsumed (for the cap)

TW4 §§9.3, 12 leave open a per-prime-efficient Λ² bound for ℛ(M)-families
whose moduli have `r ≍ log L` large primes. A Selberg Λ² majorant
`ν = (Σ_S λ_S 1[n ∈ ∩_{C∈S}C])²` with `λ_∅ = 1` equals 1 at every avoider
`n ∈ ℤ` (all class indicators vanish), is ≥ 0, and is a CRT majorant whose
level is at most twice the sieve level. So it is in the class of
Theorem 4.1, which has no hypothesis on `ω(M)`, on B, or on the number of
primes at one scale. Hence **every Λ² sieve over every K2 family saves at
most `C L^{3/4}` at level L, for all r**, superseding TW4 Thm 7.1's
`L^{3/4}(log L)^{3r+O(1)}` and Prop 9.1 / Cor 9.3 as far as the cap is
concerned (PROVED, as a corollary of Thm 4.1). What remains open in TW4
§12 is only the *Λ²-internal* route (hub count, off-diagonal pair sum);
it no longer bears on any ES cap. Not pursued. ("Saving" here is the
mean saving `log(1/Eν)`, TW4's convention; the exceptional-set reading
still needs Cor 4.2's evaluation hypotheses.)

## 7. Goal (3) continued: §6 at text level, and the class-order window

**Lemma 7.1 (§6 checked against TW2/TW4's definitions; PROVED).** In TW4
Setting 3.0^{(r)} (= TW2 Setting 3.0 with "at most two" replaced by "at
most r" large primes, any r), every admissible g (`g ∈ V_{λ/2}`, `g ≥ 1`
on the avoiders, `λ ≤ A₀L`) gives a K2 majorant `ν = g²` of level `≤ λ`
of the avoider set of a family of ℛ(M)-classes, and TW's
`saving(g²) = log(1/E g²)`. Hence Theorem 4.1 gives
`saving(g²) ≤ Cλ^{3/4} ≤ C A₀^{3/4} L^{3/4}` for **every** r, every B,
and also without B (TW4's families need `M ≤ P(M)^{1+B}`; Thm 4.1 does not).

*Proof.* (i) *Family.* TW2 Setting 3.0's classes are Case-B classes
`−4D mod M`, `M ≡ 3 (4)`, `D | A²`: ℛ(M)-classes (K2 Def 2.0). TW4
changes only the number of primes above `w₂ = L^8`. (ii) *Level.* TW2
Setting 3.0: "All primes are charged (`s_ℓ = log ℓ`)", so `g ∈ V_{λ/2}`
is a CRT combination of residue classes whose moduli have
`Σ_{ℓ|d} log ℓ ≤ λ/2` over **all** primes, in particular over primes
`> W`. A product of two such indicators is 0 or one residue class modulo
the lcm, whose prime set is the union; so `g²` is a CRT combination of
level `≤ λ` in K2's sense (which charges only primes `> W`). (iii) *Sign
and majorisation.* `g² ≥ 0` on ℤ, and `g² ≥ 1` wherever `g ≥ 1`, i.e. on
the whole (periodic) avoider set. (iv) *Saving.* TW Lemma 6.6 / TW2
Lemma 2.1 measure `saving(g²) = log(1/E_U g²)` under the uniform law on
`ℤ/Q`, which is K2's Eν. So Theorem 4.1 applies with `λ ≤ A₀L`. ∎

So TW4 Thm 7.1 (`L^{3/4}(log L)^{3r+O(1)}`), Prop 9.1, Cor 9.3 and the
open middle window `r ≍ log L` are all superseded, as caps, by
`C A₀^{3/4}L^{3/4}`. The only thing Theorem 4.1 does not reproduce is
TW4's *mechanism* (fibre tilting + star sums, per-prime efficient); the
TW4 §12 hub-count question is a question about that mechanism and has no
consequence for any cap.

**Lemma 7.2 (the literal TU Cor 3.4 hypothesis is a level hypothesis;
PROVED, elementary).** Let `Z ≥ 2` and `k ≥ 1`. Every residue class
`b mod d` such that every prime power `p^e ∥ d` is `≤ Z` and
`log d ≤ (k−1)log Z/2` is an intersection of at most k residue classes
of moduli `≤ Z`.

*Proof.* List the prime powers `p^e ∥ d` in any order and pack them
greedily (next-fit) into bins whose products stay `≤ Z`; each prime
power fits into an empty bin. If there are m bins `b_1, …, b_m`, then
`b_ib_{i+1} > Z` for `i < m`, so `d ≥ Π_{j<m/2} b_{2j+1}b_{2j+2} > Z^{⌊m/2⌋}`
and `m ≤ 2log d/log Z + 1 ≤ k`. The bins are pairwise coprime with
product d, so by CRT `{n ≡ b (d)} = ∩_i {n ≡ b (b_i)}`. ∎

**Consequence (exact status of the TU Cor 3.4 window).** With
`Z = N^A`, TU Cor 3.4's literal hypothesis ("each term an intersection
of at most k classes of modulus `≤ N^A`, or of level `≤ A log N`")
contains **every** majorant whose moduli have all prime powers `≤ N^A`
and `log d ≤ (k−1)A log N/2`, i.e. every such majorant of level
`λ ≍ kA log N`. Conversely such intersections have level `≤ kA log N`.
So, up to a factor 2 in k, the literal Cor 3.4 class **is** the class
of level-`λ` majorants, `λ ≍ kL` (L = log N), built from primes `≤ N^A`,
and TU's bound `C(kAL)^{3/4}` is Theorem 4.1 at that level. Hence:
1. No argument that uses only the literal hypothesis can close the
   window `L^{4θ/3−1} ≲ k ≲ L^θ/log L`. Closing it would bound level-λ
   majorants (λ ≫ L, primes `≤ e^{AL}`) by `C[L^{3/4} + (λ/L)·polylog L]`
   instead of `Cλ^{3/4}`. The KARY method cannot do this: its cost
   ledger at level λ is minimised at `s₁ = λ^{1/4} ≤ AL` (for
   `k ≤ L³`), where the truncation of primes at `e^{AL}` is invisible.
   Whether `λ^{3/4}` is *attained* at such levels is the attainability
   question of ET §2.5 (EVIDENCE only there), not settled here.
2. The window therefore makes sense only for a **structured** notion of
   order: TU Def 3.0's prime order (closed by Cor 5.2), or intersections
   of k **family** classes (forced classes of 𝔊). For the latter,
   Cor 5.3 closes it when the family's moduli have boundedly many primes
   above W; otherwise it is open.

**Assessment (family-class order with many large primes; not a proof).**
In the abstract pattern model of EK §1 (independent coordinates
`x_ℓ ~ Bern(p_ℓ)`), let the family consist of conjunction patterns on
m-sets of block coordinates. A polynomial of class degree k in the
pattern indicators is a polynomial of degree `≤ km` in the `x_ℓ`, and
for symmetric patterns every degree-`km` polynomial in `K = Σx_ℓ` that
is `≡ 1` on `{K < m}` is available. Binomial extrapolation (EK Lemma 2.3)
is then tight in the same regime as for prime order `km`. So nothing in
the *k-ary architecture* distinguishes class order k from prime order
km. If this persists for forced classes, intersections of k family
classes with `m ≍ AL/s` primes at scale s behave like prime order
`km ≍ kAL/s`. That is the level-λ ledger again (`d = λ/s`), and the
window would be genuine, not an artefact. Deciding this needs
ES-specific input on how forced classes with many large primes intersect.
That is the TC-type question of O24 and is not pursued here.

## 8. Numerics (EVIDENCE only)

`scripts/kary3_moments.py` enumerates all y-smooth `M ≡ 3 (mod 4)` up to
`X = 10¹²` for `y ∈ {7, 13, 23, 31}` and factors `A_M`
(`data/kary3/moments.txt`, ~25 s):
* the smooth first moment `S(y) = Σ τ(A_M²)/M` stabilises (it changes
  by `< 1%` from `X^{1/2}` to X; this is not a bound on the infinite
  tail), and `S/(log y)³ = 0.264, 0.211, 0.200, 0.192`; with the K2
  weight Γ (W = 16) `1.38, 1.35, 1.17, 1.08`. A `(log log y)³` factor
  would multiply these by ≈ 6 over this range; they decrease instead.
  (The range of y is tiny; this is consistent with Cor 2.4, not a test of
  its constant.)
* the dyadic block profile `b(K) = Σ_{K<M≤2K smooth}τ(A²)/(K log²K)`:
  over **all** complete blocks `K ≥ y` the maximum of `u⁴b(K)` is
  `0.385, 0.293, 0.251, 0.248` for `y = 7, 13, 23, 31` (at u ≈ 2–2.5;
  the script now computes it), and `u⁴b` decays fast for `u ≥ 3`
  (y = 31: `5·10⁻⁵` at u = 7.7). This is heuristic consistency with
  Lemma 2.3 only: the lemma needs `u ≥ 16k = 64` and large y, far
  outside this range; the true decay is `ρ(u)`-like.

## Replay

```
mkdir -p data/kary3
# §8: smooth first moments and block profiles (~25 s, < 1 GB)
uv run --with sympy python scripts/kary3_moments.py 1e12 7,13,23,31 > data/kary3/moments.txt
```
