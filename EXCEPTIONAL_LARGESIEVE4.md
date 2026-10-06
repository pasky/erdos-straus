# EXCEPTIONAL_LARGESIEVE4 — (H_rough) via damped collisions (task O62)

Status: **in progress** (agent O62, branch `side-agent/hrough`). Labels as in
`DISCOVERIES.md`. Notation: LS3 = `EXCEPTIONAL_LARGESIEVE3.md` (all its
notation is used), LS2 = `EXCEPTIONAL_LARGESIEVE2.md`, K2 =
`EXCEPTIONAL_KARY2.md`, EK = `EXCEPTIONAL_KARY.md`.

Throughout, σ is a probability on `ℤ/M_r`, `M_r = Π_{ℓ∈𝒫}ℓ^{E_ℓ}` (𝒫 a finite
set of primes, in LS3 the z-rough ones), `p' = 2+2β`, `0 < β ≤ 1/2`. For a
frequency θ (`den θ | M_r`) let `supp θ` be the set of primes dividing
`den θ`. `h_ℓ(x,y) = ℓ^{E_ℓ}1[x ≡ y (ℓ^{E_ℓ})] − 1` and, for `T ⊆ 𝒫`,
`σ_T` is the marginal of σ on `ℤ/M_T`, `M_T = Π_{ℓ∈T}ℓ^{E_ℓ}`,
`𝓡_2(σ_T) = M_T Σ_u σ_T(u)² = M_T·σ⊗σ(x ≡ y (M_T))` (the collision number;
`𝓡_2(σ_∅) = 1`).

## 0. Summary (so far)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | **damped-collision reduction**: if `|σ̂(θ)|^{2β} ≤ Π_{ℓ∈supp θ}w_ℓ` with `w_ℓ ∈ [0,1]`, then `𝓡_{2+2β}(σ) ≤ E_{T}𝓡_2(σ_T)`, T the random subset of 𝒫 containing ℓ independently with probability `w_ℓ` | PROVED |
| Cor 1.2 | (H_rough) follows from (A_γ) sup decay at **any fixed rate** γ in the rough level plus (B) a damped collision bound | PROVED (reduction) |

## 1. The damped-collision reduction

**Lemma 1.1 (PROVED).** Let `w_ℓ ∈ [0,1]` (`ℓ ∈ 𝒫`) and suppose

    (A_w)   |σ̂(θ)|^{2β} ≤ Π_{ℓ ∈ supp θ} w_ℓ     for every θ ≠ 0.

Then

    𝓡_{2+2β}(σ) ≤ E_{x,y∼σ⊗σ} Π_{ℓ∈𝒫}(1 + w_ℓ h_ℓ(x,y)) = E_T 𝓡_2(σ_T),

where T ⊆ 𝒫 contains each ℓ independently with probability `w_ℓ`.

*Proof.* Group θ by `S = supp θ`. With LS3 Lemma 4.1's
`P_S = Σ_{supp θ = S}|σ̂(θ)|² = E_{σ⊗σ}Π_{ℓ∈S}h_ℓ ≥ 0`,
`𝓡_{p'}(σ) = Σ_S Σ_{supp θ=S}|σ̂|²|σ̂|^{2β} ≤ Σ_S (Π_{ℓ∈S}w_ℓ) P_S
= E_{σ⊗σ}Σ_S Π_{ℓ∈S}w_ℓh_ℓ = E_{σ⊗σ}Π_ℓ(1+w_ℓh_ℓ)` (S = ∅ gives the term
1 = |σ̂(0)|^{p'}). Expanding
`1 + w_ℓh_ℓ = (1−w_ℓ) + w_ℓ·ℓ^{E_ℓ}1[x_ℓ = y_ℓ]` (both terms ≥ 0) and
multiplying out gives `Σ_T Π_{ℓ∈T}w_ℓ Π_{ℓ∉T}(1−w_ℓ)·M_T σ⊗σ(x ≡ y (M_T))
= E_T 𝓡_2(σ_T)`. ∎

*Remarks.* (a) For a product measure with factor laws `φ_ℓ` the bound is
`Π_ℓ(1 + w_ℓ g_ℓ)`, `g_ℓ = Σ_{a≠0}|φ_ℓ(a)|²`, i.e. LS3 Theorem 3.1's
computation with `w_ℓ = (2p_ℓ)^{2β}`.
(b) The point of Lemma 1.1 is the **separation of roles**: the sup
hypothesis (A_w) is needed only with *weak* per-prime decay (see Cor 1.2:
any fixed rate γ in the level, up to `(log N)^{O(1)}` losses per prime),
while all the quantitative work moves into a **positive** two-copy
quantity, a collision number on a random sparse set of coordinates, which
has no signs and no Möbius inversion (contrast LS3 §4: `P_S` is signed
after inclusion–exclusion; here only the non-negative weights `w_ℓ` are
inverted).
(c) Since `w_ℓ ≤ 1`, the right side is at most the full collision number
`𝓡_2(σ)` (the density cost of global Hausdorff–Young, LS3 §4.3); the
damping by `w_ℓ` is what must beat the density.

**Corollary 1.2 (reduction of (H_rough); PROVED as an implication).** Let
`z = exp((log N)^{1/4})`, `β = (log N)^{−1/4}`, and let σ be a probability on
`𝒜_c ⊂ ℤ/M_r` (z-rough coordinates). Fix `γ ∈ (0,1]`, `K ≥ 1` with
`K ≤ z^{γ/2}`. Suppose
* (A_γ) `|σ̂(θ)| ≤ Π_{ℓ∈supp θ} K ℓ^{−γ}` for all θ ≠ 0, and
* (B) with `w_ℓ = (Kℓ^{−γ})^{2β} (≤ e^{−γ})`: `log E_T 𝓡_2(σ_T) ≤ S_B`.

Then `log 𝓡_{2+2β}(σ) ≤ S_B`, so σ satisfies the Hölder form of (H_rough)
with `C(log N)^{3/4+o(1)}` as soon as `S_B ≤ C(log N)^{3/4+o(1)}`.

*Proof.* `K ≤ z^{γ/2} ≤ ℓ^{γ/2}` gives `w_ℓ ≤ ℓ^{−γβ} ≤ z^{−γβ} = e^{−γ} < 1`;
(A_γ) is (A_w). Lemma 1.1. ∎

*Scale of the damping.* For `ℓ = exp(t(log N)^{1/4})`, `t ≥ 1`,
`w_ℓ ≈ e^{−2γt}·K^{2β}` and `K^{2β} = 1 + o(1)` when `K ≤ (log N)^{O(1)}`.
In the product case (LS3 Thm 3.1) the per-prime collision factor is
`1 + w_ℓ g_ℓ`, and `Σ_ℓ w_ℓ E g_ℓ ≍ ∫ e^{−2γt}d𝔐 ≍ γ^{−3}β^{−3}`
(`𝔐(y) ≍ (log y)³`), i.e. `(log N)^{3/4}` up to `γ^{−3}` and K2's
`(log log)³`. So (B) is the natural size, and γ may be as small as
`(log log N)^{−O(1)}` at a cost `(log N)^{o(1)}`.

## Plan (not yet results)

* §2 (B) for sequential laws: two-copy tilting (the pair process with
  conditional factor `1 + w_ℓη_ℓ`), reducing (B) to an exponential moment
  of the **damped activated mass** of the two copies.
* §3 (A_γ) for sequential laws via the EK coupling with i.i.d. coins:
  Fourier coefficients bounded by probabilities of *pivotal* sets, then
  disagreement propagation along classes in top-prime order.
* §4 ES arithmetic: influence bounds counted by **distinct residues**
  (residue concentration, LS3 Lemma 4.2, becomes harmless: the forbidden
  set at ℓ is a set, so the class −4 mod pM' contributes one residue per
  ℓ, and the damping `w_ℓ` cuts the `Σ1/ℓ` sum to O(1)).
