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

## 2. (B) for sequential laws: the tilted pair process

**Setting 2.0 (always-forbid sequential law).** 𝒫 is ordered increasingly,
`Ω_ℓ = ℤ/ℓ^{E_ℓ}`, U the uniform law. A *rough family* is a finite set of
patterns `C = (b_C mod G_C)`, `G_C | M_r`; `top(C)` is the largest prime
of `G_C`. Given `x_{<ℓ}`, the activated set `F_ℓ(x_{<ℓ}) ⊆ Ω_ℓ` is the union
of the classes `b_C mod ℓ^{v_ℓ(G_C)}` over C with `top(C) = ℓ` and
`x_q ≡ b_C (mod q^{v_q(G_C)})` for all other primes q of `G_C`;
`p_ℓ = U(F_ℓ)`. Assume `p_ℓ < 1` on every path (true off K2's leak event
for the fibres of LS3, where `p_ℓ ≤ 1/2`). σ draws `x_ℓ ~ U(·|Ω_ℓ∖F_ℓ)`
in increasing order. It lives on the avoider set (the top of every class is
forbidden when the class is activated), and it is the law of LS3 §3 when
every class has one rough prime. (Differences from K2's capped plain
rule: no caps, heavy steps still forbid.)

**Lemma 2.1 (tilted pair law; PROVED).** Let x, x' be independent copies
of σ, run jointly in increasing ℓ; `p = U(F_ℓ(x_{<ℓ}))`,
`p' = U(F_ℓ(x'_{<ℓ}))`, and

    η_ℓ := E[h_ℓ(x_ℓ,x'_ℓ) | past] = (U(F_ℓ∩F'_ℓ) − pp') / ((1−p)(1−p')).

For `w_ℓ ∈ [0,1]` let Q be the law of the pair under which, given the past,
`(x_ℓ, x'_ℓ) = (a,a')` with probability
`k(a)k'(a')(1 + w_ℓh_ℓ(a,a'))/(1 + w_ℓη_ℓ)`, k, k' the σ-step laws. Then

    E_{σ⊗σ} Π_ℓ(1 + w_ℓh_ℓ) = E_Q Π_ℓ(1 + w_ℓη_ℓ) ≤ E_Q exp(Σ_ℓ w_ℓ ξ_ℓ),
    ξ_ℓ := U(F_ℓ∩F'_ℓ)/((1−p)(1−p')).

Under Q, given the past, `P_Q(x_ℓ = a) ≤ U(a)/((1−p)(1−p')(1+w_ℓη_ℓ))`, and
the same for `x'_ℓ` (per-coordinate inflation, as EK Lemma 2.1(2)).

*Proof.* Given the past, x_ℓ, x'_ℓ are independent with laws
`k = U(·|F^c)`, `k' = U(·|F'^c)`; so
`E[ℓ^{E}1[x_ℓ=x'_ℓ]|past] = ℓ^{E}Σ_a k(a)k'(a) = U(F^c∩F'^c)/((1−p)(1−p'))`
and `U(F^c∩F'^c) = 1 − p − p' + U(F∩F')`, which gives η. Since
`1 + w h ≥ 1 − w ≥ 0`, `1 + wη = E[1+wh | past] ≥ 0`; if `1 + wη = 0` then
`1 + wh = 0` a.s. given the past and both sides of the identity vanish on
that branch (set the Q-step arbitrarily). Otherwise `Z_ℓ = (1+wh)/(1+wη)`
is ≥ 0 with conditional mean 1, `dQ/d(σ⊗σ) = Π_ℓ Z_ℓ`, and
`Π(1+wh) = Π(1+wη)·ΠZ_ℓ` with `Π(1+wη)` predictable step by step, so
`E_{σ⊗σ}Π(1+wh) = E_QΠ(1+wη)`. Drop `−pp' ≤ 0` and use `1+u ≤ e^u`.
Inflation: `Σ_{a'}k'(a')(1+w h(a,a')) = 1 − w + w ℓ^{E}k'(a) ≤ (1−p')^{−1}`
(as `ℓ^{E}k' ≤ (1−p')^{−1}` and `1 − w + w·t ≤ t` for `t ≥ 1`), and
`k(a) ≤ U(a)/(1−p)`. ∎

*Remarks.* (a) `ξ_ℓ ≤ min(p,p')/((1−p)(1−p'))`; the copies interact only
through the **common** activated residues `F_ℓ ∩ F'_ℓ`. Under Q the copies
are glued at ℓ with probability ≈ `w_ℓ` (the factor `1 + wh` rewards
`x_ℓ = x'_ℓ`), so typically `F_ℓ ∩ F'_ℓ ≈ F_ℓ` and ξ_ℓ ≈ p_ℓ: (B) is an
**exponential moment of the damped activated mass** `Σ_ℓ w_ℓ p_ℓ` under a
pair law with bounded per-coordinate inflation. The first moment is the
right size (Cor 1.2 scale remark); what is needed is that the upper tail
is not heavier than `exp(−c·deviation)` at scale `(log N)^{3/4}` — a
large-deviation statement, not a correlation-decay statement.
(b) (Fibres.) In LS3's setting the fibre law at c is Setting 2.0 for the
fibre family 𝔊_c, and Theorem 1.1 needs only `E_{c∼π_s}𝓡_{p'}(π_c)`. Since
`π_s` is K2's law conditioned on an event of probability ≥ 1/2, the
c-average may be taken under the unconditioned sequential law, and bad c
(say `E[Σ_ℓ w_ℓ p_ℓ | c] > 16·mean`) may be put into LS3 Lemma 2.1's
exceptional event E (Markov). So (B) is needed only **fibrewise, for
fibres whose conditional mean damped mass is ≤ 16J** — an exponential
moment over the *rough* coordinates only.

`scripts/largesieve4_checks.py` checks (EVIDENCE): the identity
`Σ_S w_S P_S = E_T𝓡_2(σ_T)` and the η formula by exact enumeration
(random toy families over primes 3, 5, 7, 11; errors ≤ 3·10⁻¹⁴).

## 3. (A_γ) for sequential laws: Fourier coefficients and pivotal coins

**Coin representation.** In Setting 2.0 let `c_ℓ ~ U(Ω_ℓ)` and `π_ℓ` (a
uniformly random ordering of `Ω_ℓ`) be independent over ℓ and of each
other. Put `x_ℓ = c_ℓ` if `c_ℓ ∉ F_ℓ(x_{<ℓ})`; otherwise ℓ is *replaced*
(`ℓ ∈ R`) and `x_ℓ` is the first element of `π_ℓ` outside `F_ℓ`. Given the
past, `P(x_ℓ = a) = U(a) + p·U(a)/(1−p) = U(a)/(1−p)` for `a ∉ F_ℓ`, so x
has law σ (this is EK's coupling without caps). Write `x = X(c, π)`.

**Lemma 3.1 (pivotal bound; PROVED).** Let θ ≠ 0, `S = supp θ`,
`θ = Σ_{ℓ∈S}θ_ℓ` (`θ_ℓ ≠ 0` with denominator a power of ℓ). Let `c'_S`
be an independent copy of `c_S`, and for `A ⊆ S` let `c^A` be c with
`c_A` replaced by `c'_A`, `x^A = X(c^A, π)`, and
`Ψ(A) = Π_{ℓ∈S} e((x^A_ℓ − c^A_ℓ)θ_ℓ)`. Call ℓ ∈ S *pivotal* if
`Ψ(A) ≠ Ψ(A∪{ℓ})` for some `A ⊆ S∖{ℓ}`. Then

    |σ̂(θ)| ≤ 2^{|S|} · P(every ℓ ∈ S is pivotal).

Moreover ℓ can be pivotal only if, for some A, ℓ is replaced in `x^A` or
`x^{A∪ℓ}`, or the two paths differ at some replaced coordinate of S∖{ℓ}
or in the replacement status of some coordinate of S∖{ℓ}.

*Proof.* Condition on `c_{𝒫∖S}` and π; then `c_S` is uniform on
`Π_{ℓ∈S}Ω_ℓ` and `e(x·θ) = χ(c_S)Ψ(∅)` with `χ(c_S) = Π_ℓ e(c_ℓθ_ℓ)`
(`x_ℓ − c_ℓ = 0` off R). Write Ψ as a function of `c_S` and expand
`Ψ = Σ_{B⊆S} Π_{ℓ∈B}(I−E_ℓ)Π_{ℓ∉B}E_ℓ Ψ` (`E_ℓ` = average over `c_ℓ`).
A term with `B ≠ S` does not depend on `c_ℓ`, `ℓ ∈ S∖B`, and
`E_{c_ℓ}e(c_ℓθ_ℓ) = 0`; so `E[χΨ] = E[χ·Π_{ℓ∈S}(I−E_ℓ)Ψ]` and
`|E[χΨ]| ≤ E|Π_{ℓ∈S}(I−E_ℓ)Ψ|`. Now
`Π_{ℓ∈S}(I−E_ℓ)Ψ = E_{c'_S}Σ_{A⊆S}(−1)^{|A|}Ψ(A)`. If some ℓ is not
pivotal, the terms A and A∪{ℓ} (A ∌ ℓ) cancel in pairs; otherwise the sum
has `2^{|S|}` terms of modulus 1. The last sentence: `Ψ(A)` depends only
on which coordinates of S are replaced and on `x_q − c_q` there. ∎

*Remarks.* (a) Lemma 3.1 converts the signed quantity `σ̂(θ)` into the
probability of an event on a **product** probability space (coins `c`,
`c'_S`, orderings π), at the cost `2^{|S|}`; Cor 1.2 tolerates any loss
`K^{|S|}` with `K ≤ z^{γ/2}`, and `|S| ≤ log M_r/log z`, so `2^{|S|}` is
harmless.
(b) A single prime: ℓ pivotal needs ℓ replaced in some corner, or the
change `c_ℓ → c'_ℓ` to propagate (through classes containing ℓ) to a
replacement in S. Both require `c_ℓ` or `c'_ℓ` to lie in a set of
residues determined by **classes through ℓ**, of expected size
`≲ |Ω_ℓ|·(mass of classes through ℓ)`. So each prime of S costs, in
expectation, the mass through ℓ — `(log N)^{O(1)}/ℓ` for moduli `≤ N^A`.
The content of (A_γ) is that these costs **multiply** over S up to
`K^{|S|}`: a correlation-decay statement for *events*, with an enormous
slack (`ℓ^{1−γ}/K` per prime), in contrast with LS3 §4.3 / LS2 §5 where
the signed one-step bounds lose.
