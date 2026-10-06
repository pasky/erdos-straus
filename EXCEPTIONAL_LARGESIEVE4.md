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
| Lemma 2.1 | tilted pair law: the damped collision is `E_Q Π(1+w_ℓη_ℓ)`, η explicit | PROVED |
| Lemma 3.1, 3.2 | Fourier coefficients ≤ `2^{|S|}`·P(all of S pivotal) (coin coupling); one class per modulus | PROVED |
| Prop 4.1 | (B) is free: for the K2 fibre law conditioned on a good path event, the damped collision is `≤ e^{2B}/Q'(G)²` — **first moments only** | PROVED |
| Thm 4.2 | **H_LS∞ for all forced families ⟸ (A\*)**: sup decay of the conditioned fibre laws at any fixed rate γ (losses up to `z^{γ/2}` per prime allowed); cap `(log N)^{3/4} + Cγ^{−3}(log N)^{3/4}(log log N)³` | PROVED (implication) |
| Lemma 5.1 | pinned pivotal bound with a **deterministic** residue set per prime: exact product decay `Π_{ℓ∈S}4U(R_ℓ)/(1−δ_ℓ)` | PROVED |
| Thm 5.2 | **3/4 cap at every frequency level for mixtures whose multi-rough classes are residue-sparse** (`U(Res_ℓ) ≤ ℓ^{−γ}` at primes > z); one-rough-prime classes arbitrary. Extends LS3 Thm 3.1 | PROVED (K2 inputs; Case A via ElT) |
| Cor 5.3 | the same for all **small-height** classes `−r/s`, `r,s ≤ z^{1/4}/2` (incl. LS3 Lemma 4.2's `−4 mod M` for all M): residue concentration is the *easy* case | PROVED |
| §3.2 (CC) | what is left: residue-dense multi-rough classes — a covering count for random-path relevance | CONJECTURE (Assessment of difficulty) |

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

### 3.2 What (A_γ) needs: a covering count (Assessment; Lemma 3.2 PROVED)

**Lemma 3.2 (one class per modulus; PROVED, trivial).** For a modulus Q
and an assignment v of residues to the primes of Q, at most one class
mod Q is consistent with v (namely v mod Q). For ℛ(Q) (`Q ≡ 3 (4)`,
`A = (Q+1)/4`): `v mod Q ∈ ℛ(Q)` iff `r̃ | A²` or `s̃ | A²`, where r̃, s̃
are the least positive residues of `−v/4` and `−1/(4v)` mod Q.

*Proof.* The first claim is CRT. For the second: `−4D ≡ v` with
`D | A²`, `D·(A²/D) = A²` and `4A ≡ 1 (Q)`, so `A²/D ≡ −1/(4v)`; one of
`D, A²/D` is `≤ A < Q`, hence equal to its least residue. ∎

*Pinned form of Lemma 3.1.* Pinning the S-coordinates to `v ∈ Ω_S` and
running the coin process on the other coordinates gives
`M_S σ(x_S = v) = E[Λ(v)]`, `Λ(v) = Π_{ℓ∈S}1[v_ℓ ∉ F_ℓ]/(1−p_ℓ)`, so
`σ̂(θ) = E_{coins}E_{v∼U_S}[χ_θ(v)Λ(v)]` and, as in Lemma 3.1, `|σ̂(θ)|` is
at most `2^{|S|}·sup Λ` times the probability (v, v' uniform on `Ω_S`,
coins outside S) that **every** ℓ ∈ S is pivotal for Λ. Pivotality of ℓ
needs `v_ℓ` or `v'_ℓ` to be the ℓ-residue of a class through ℓ whose other
coordinates are matched (S-coordinates by the pinned values in some
corner, outside coordinates by the path) — a **covering** event.

*The covering count.* Ignoring outside coordinates, the event is
`E_S = {v : every ℓ ∈ S lies in some Q ⊆ S with v mod Q a class of 𝔊}`,
and the target is `|E_S| ≤ Π_{ℓ∈S}K ℓ^{1−γ}` (`P(E_S) = |E_S|/M_S`).
* *Small supports.* Each ℓ has at most `2^{|S|−1}` candidate moduli Q and
  each Q one consistent class (Lemma 3.2), so the trivial encoding
  (a minimal cover by ≤ |S| moduli plus their classes) gives
  `|E_S| ≤ (2^{|S|})^{|S|}`, i.e. a per-prime factor `2^{|S|}`. This is
  within the slack of Cor 1.2 iff `|S| ≤ (1−2γ)log₂ z ≈ 1.44(log N)^{1/4}`.
* *Beyond `log₂ z` primes the union bound over covers is false in the
  right direction.* Example (structured family): primes of S all
  `≡ −1 (mod F)`, 𝔊 ⊇ {−4d mod Q : Q ⊆ S of odd size, d | F²/16}
  (forced: `F | 4A_Q`). Every v ≡ −4d on S is covered by
  `2^{Θ(|S|²)}` minimal covers, while `|E_S|` stays `≤ τ(F²)^{O(1)}·|S|^{|S|}`
  (the classes are constant across Q, so they act as **product**
  constraints; e.g. with singletons present they forbid `−4d` at every
  coordinate). For "random-like" residues the compatibility of
  overlapping covers costs `1/q` per shared prime and the expected number
  of minimal covers is `≤ Π_ℓ (τ+|S|)/ℓ` (Assessment: computed under the
  random-residue model).
* So the missing input is a count of **assignments**, not of covers:
  > **(CC)** for every finite set S of primes `> z` and every family 𝔊 of
  > forced classes, `|E_S| ≤ Π_{ℓ∈S} K ℓ^{1−γ}` with `K = (log N)^{O(1)}`
  > (and the analogue with outside coordinates matched by the path).
  (CC) is a CONJECTURE. Structured coincidences (equal integers d across
  moduli) collapse to few assignments; unstructured ones are rare in the
  random model; a proof must interpolate between these, i.e. control
  divisors of `(Q+1)/4` over subset products Q ⊆ S. No counterexample is
  known; the residue-concentration mechanism of LS3 Lemma 4.2 is of the
  structured (harmless) type.

## 4. (B) is free: conditioning on a good path event

The tilting identity of Lemma 2.1 holds with any non-negative path
functional inserted: `E_{σ⊗σ}[Φ(x,x')Π_ℓ(1+w_ℓh_ℓ)] = E_Q[Φ Π_ℓ(1+w_ℓη_ℓ)]`
(same proof: `dQ/d(σ⊗σ) = Π_ℓ Z_ℓ`). Inserting the indicator of a good
event makes the exponential-moment problem of §2 disappear.

**Setting 4.0 (capped fibre law).** As in Setting 2.0 but with K2's capped
plain rule: caps `δ_ℓ ∈ (0,1/2]`; ℓ is *light* if `p_ℓ ≤ δ_ℓ`; then
`x_ℓ ~ U(·|Ω_ℓ∖F_ℓ)`, otherwise (heavy) `x_ℓ ~ U`. Call this law Q'.
Put `p̃_ℓ = p_ℓ1[ℓ light]`. For `B > 0` let

    G_B = {x ∈ 𝒜(family)} ∩ {Σ_ℓ w_ℓ p̃_ℓ(x) ≤ B},     σ_B := Q'(· | G_B).

σ_B lives on the avoider set (G_B contains "no leak").

**Proposition 4.1 (damped collision of the conditioned law; PROVED).**
For `w_ℓ ∈ [0,1]`,

    E_T 𝓡_2((σ_B)_T) ≤ e^{2B} / Q'(G_B)².

*Proof.* By Lemma 1.1's identity,
`E_T𝓡_2((σ_B)_T) = E_{Q'⊗Q'}[1_{G_B}(x)1_{G_B}(x')Π_ℓ(1+w_ℓh_ℓ)]/Q'(G_B)²`.
The step laws of Q' are `k = U(·|Ω_ℓ∖F̃_ℓ)` with `F̃_ℓ = F_ℓ` (light) or ∅
(heavy), `U(F̃_ℓ) = p̃_ℓ ≤ 1/2`. Lemma 2.1 applies verbatim with F̃ in
place of F, with Φ inserted, and gives
`E_Q[1_{G_B}(x)1_{G_B}(x')Π_ℓ(1+w_ℓη_ℓ)]`. Since
`1 + η_ℓ = ℓ^{E}Σ_a k(a)k'(a) ≤ ℓ^{E}max_a k(a) = (1−p̃_ℓ)^{−1}`,
`η_ℓ ≤ p̃_ℓ/(1−p̃_ℓ) ≤ 2p̃_ℓ(x)`, so `Π(1+wη) ≤ exp(2Σw_ℓp̃_ℓ(x)) ≤ e^{2B}`
on `G_B(x)`. ∎

So in (B) only the **first moment** of the damped activated mass enters
(through `Q'(G_B) ≥ 1/2` by Markov). No large-deviation input is needed.

**Theorem 4.2 (H_rough ⟸ sup decay; PROVED as an implication).** Let
`z = exp((log N)^{1/4})`, `β = (log N)^{−1/4}`, 𝔊 any finite mixture of
ℛ(M)-, (a,D)-, Case-A and selector classes, and Q' K2's sequential law
(square base, caps `δ_ℓ = ℓ^{−1/2}`), run on all coordinates. For a
z-smooth part c let `Q'_c` be the conditional law of the z-rough
coordinates given c (a capped fibre law, Setting 4.0, for the fibre family
𝔊_c), `m_c = E_{Q'_c}Σ_{ℓ>z}w_ℓp̃_ℓ`, `B_c = 8m_c`, `σ_c = Q'_c(·|G_{B_c})`.
Fix `γ ∈ (0,1]`, `1 ≤ K ≤ z^{γ/2}`, `w_ℓ = (Kℓ^{−γ})^{2β}`. Suppose

    (A*)  for every c outside an event of Q'-probability ≤ 1/32 and every
          θ ≠ 0 with z-rough denominator: |σ̂_c(θ)| ≤ Π_{ℓ∈supp θ} K ℓ^{−γ}.

Then every CRT-admissible N-large-sieve bound for 𝒜(𝔊) (any rational
frequencies, any denominators, any weights) saves

    log(N/B) ≤ (log N)^{3/4} + C γ^{−3}(log N)^{3/4}(log log N)^3.

*Proof.* Define LS3 Lemma 2.1's exceptional smooth event as
`E = E₀ ∪ {leak_c > 1/4} ∪ {m_c > 32J}`, where E₀ is the event of (A*),
`leak_c = Q'_c(x ∉ 𝒜_c)` and `J = E_{Q'}Σ_{ℓ>z}w_ℓp̃_ℓ`. By K2 Lemma 4.3
the rough part of the leak is `Σ_{ℓ>z}E[p_ℓ1{p_ℓ>δ_ℓ}] ≤ Cz^{−1/4}(log z)^c`,
so `Q'(leak_c > 1/4) ≤ 4Cz^{−1/4}(log z)^c`; Markov gives
`Q'(m_c > 32J) ≤ 1/32`. Hence `Q'(E) ≤ 1/8` for N large, and LS3 Lemma
2.1 yields `π_s` with `log ρ ≤ 16𝔐(z) + O(1)` supported off E. For
`c ∈ supp π_s`: `Q'_c(G_{B_c}) ≥ 1 − 1/4 − 1/8 ≥ 1/2` (Markov for
`Σwp̃ > 8m_c`), so by (A*), Lemma 1.1 and Prop 4.1,
`log 𝓡_{2+2β}(σ_c) ≤ 2B_c + log 4 ≤ 512J + log 4`. Theorem 1.1 (LS3) with
`π_c = σ_c` gives `log(N/B) ≤ β log N + 16𝔐(z) + 512J + O(1)`. Finally
`E_{Q'}p̃_ℓ ≤ E p_ℓ ≤ Σ_{C: P(G_C) = ℓ}Γ(G_C)/G_C` (K2 (Q4)) and
`w_ℓ ≤ K^{2β}ℓ^{−2βγ}` with `K^{2β} ≤ e^{γ}`, so by partial summation as
in LS3 Thm 3.1 (with `α = 2βγ`),
`J ≤ e·K₃α^{−3}·C(log(e+1/α))³ ≤ Cγ^{−3}(log N)^{3/4}(log log N)³`, and
`𝔐(z) ≤ K₃(log N)^{3/4}(log log N)³`. ∎

*Remarks.* (a) **Everything quantitative is now proved**; the only
open input is the *qualitative-looking* sup decay (A*), at **any fixed
rate** γ (even `γ = (log log N)^{−1}` costs only `(log log N)^3` more) and
with per-prime losses `K` up to `z^{γ/2} = exp(γ(log N)^{1/4}/2)` —
far weaker than LS2's (H_LS∞)(b) (`|π̂|² ≤ e^{S}/N` with `S ≍ (log N)^{3/4}`)
in the per-prime sense, and with **no comparison-at-level hypothesis**
(LS2 Prop 5.2(a) is replaced by Prop 4.1).
(b) If the large sieve uses only frequencies whose z-rough parts have
support in a class 𝒮 of prime sets, (A*) is needed only for `supp θ_r ∈ 𝒮`
(Theorem 1.1's Hölder step and Lemma 1.1 only see the frequencies used).
(c) By §3, (A*) reduces to a covering count; for supports of size
`≤ (1−2γ)log₂ z` the count is trivially within the slack (§3.2), modulo
the outside-coordinate bookkeeping (to be written, §5).

## 5. Sup decay from deterministic residue sets

For a family 𝔊 and a prime ℓ let `Res_ℓ(𝔊) ⊆ ℤ/ℓ^{E_ℓ}` be the union of
the classes `b_C mod ℓ^{v_ℓ(G_C)}` over all C ∈ 𝔊 with `ℓ | G_C`.

**Lemma 5.1 (pinned pivotal bound; PROVED).** In Setting 4.0 let G be any
event (path functional) with `Q'(G) > 0` that depends on the path only
through the activated sets, the light/heavy status and membership of the
path in the avoider set (e.g. `G_B`), and `σ = Q'(·|G)`. For θ ≠ 0 with
`S = supp θ`, and any sets `R_ℓ ⊇ F̃_ℓ`-candidates as below,

    |σ̂(θ)| ≤ Q'(G)^{−1} Π_{ℓ∈S} 4U(R_ℓ)/(1−δ_ℓ),

where `R_ℓ` is any **deterministic** set containing the ℓ-residues of all
classes of the (fibre) family having ℓ in their modulus; in particular
`R_ℓ = Res_ℓ`.

*Proof.* (Pinned representation.) Integrating out the coordinates outside
S, `Q'(x_S = v, G) = E^{(v)}[1_G Π_{ℓ∈S}k_ℓ(v_ℓ | past)]`, where `E^{(v)}`
is the law of the path in which the S-coordinates are set to v and the
others follow Q' (coins `c_q`, orderings `π_q` as in §3). So with
`Φ(v) = 1_G(path(v))Π_{ℓ∈S}|Ω_ℓ|k_ℓ(v_ℓ|past)` (coins fixed),
`σ̂(θ) = Q'(G)^{−1}E_{coins}E_{v∼U_S}[χ_θ(v)Φ(v)]`, and
`0 ≤ Φ ≤ Π_{ℓ∈S}(1−δ_ℓ)^{−1}`. As in Lemma 3.1,
`|E_v[χΦ]| ≤ 2^{|S|}‖Φ‖_∞ P_{v,v'}(every ℓ ∈ S pivotal)`, v, v' independent
uniform on `Ω_S`. (Pivotal ⇒ residue.) Fix A ∌ ℓ and compare the pinned
paths for `v^A` and `v^{A∪ℓ}`, which differ only in the pinned value at ℓ
(`v_ℓ` vs `v'_ℓ`). If neither value lies in `R_ℓ`: before ℓ the paths
agree; at ℓ the factor `1[v_ℓ ∉ F̃_ℓ]/(1−p̃_ℓ)` is the same (`F̃_ℓ ⊆ R_ℓ`);
after ℓ, by induction over coordinates, every activated set agrees
(a class through ℓ is never matched, since its ℓ-residue is in `R_ℓ`;
classes not through ℓ see equal coordinates), hence so do light/heavy
status, coin decisions, fresh draws, Λ-factors, avoider-membership (no
class through ℓ is completed) and `Σw p̃`. So Φ agrees and ℓ is not
pivotal. Hence `P(all pivotal) ≤ Π_{ℓ∈S}P({v_ℓ,v'_ℓ} ∩ R_ℓ ≠ ∅)
≤ Π_ℓ 2U(R_ℓ)`, by independence of the coordinates of (v, v'). ∎

The point: the residue set is **deterministic**, so the S-coordinates
are independent and no correlation-decay statement is needed. What is
lost is the randomness of activation: `R_ℓ` contains the residues of
*all* classes through ℓ, not only of the activated ones.

**Theorem 5.2 (residue-sparse mixtures; PROVED, inputs as LS3 Thm 3.1).**
Let `z = exp((log N)^{1/4})`, `γ ∈ (0,1]`, and let 𝔊 be any finite mixture
of ℛ(M)-, (a,D)-, Case-A and selector classes (any moduli, no B). Split
𝔊 = 𝔊₁ ∪ 𝔊₂, 𝔊₁ the classes with at most one prime factor `> z`. Suppose
the multi-rough classes are residue-sparse:

    (RS_γ)   U(Res_ℓ(𝔊₂)) ≤ ℓ^{−γ}   for every prime ℓ > z.

Then every CRT-admissible N-large-sieve bound for 𝒜(𝔊) — any rational
frequencies, any denominators, any weights — saves
`log(N/B) ≤ (log N)^{3/4} + Cγ^{−3}(log N)^{3/4}(log log N)³`.

*Proof.* Theorem 4.2 with (A*) verified as follows. In the fibre at c,
the classes through a rough ℓ are (i) classes of 𝔊₂ (residues in
`Res_ℓ(𝔊₂)`), and (ii) classes of 𝔊₁ with rough prime ℓ whose smooth part
is matched by c; the latter are decided at ℓ (top prime) and their
residues form the set `F^r_ℓ(c)` of LS3 Thm 3.1, deterministic given c.
Take `R_ℓ(c) = Res_ℓ(𝔊₂) ∪ F^r_ℓ(c)` in Lemma 5.1. Add to the exceptional
smooth event the event `E₁ = {∃ℓ > z : U(F^r_ℓ(c)) > ℓ^{−1/4}}`, of
probability `≤ Σ_{ℓ>z}ℓ^{1/2}E p_ℓ² ≤ CΣ_{ℓ>z}ℓ^{−5/4}(log ℓ)^c ≤ 1/64`
(K2 Lemma 4.3, as in LS3 Thm 3.1). Off E₁,
`U(R_ℓ(c)) ≤ ℓ^{−γ} + ℓ^{−1/4} ≤ 2ℓ^{−min(γ,1/4)}`, and Lemma 5.1 with
`Q'_c(G) ≥ 1/2`, `δ_ℓ ≤ 1/2` gives
`|σ̂_c(θ)| ≤ 2Π_{ℓ∈S}16ℓ^{−γ'}`, `γ' = min(γ, 1/4)`: (A*) with
`K = 32` (the factor 2 is absorbed at one prime of S ≠ ∅;
`K ≤ z^{γ'/2}` for N large). Theorem 4.2 (with γ' for γ) concludes. ∎

**Corollary 5.3 (structured and residue-concentrated classes; PROVED).**
Call a class `b mod G` *H-small* if `b ≡ −r/s (mod G)` for some
integers `0 ≤ r ≤ H`, `1 ≤ s ≤ H`, `gcd(s,G) = 1` (e.g. ℛ(M)-classes
`−4 = −4/1`, `−1`, `−1/4`, `−4d`, `−1/(4d)`, `−d/e`; (a,D)-classes with
`4D + a ≤ H`; Case-A classes `−m^{−1}` with `m ≤ H`; selector classes
`0 = −0/1`).
If every class of 𝔊 with two or more prime factors `> z` is H-small with
`H ≤ z^{1/4}/2`, the conclusion of Theorem 5.2 holds with γ = 1/4.

*Proof.* The ℓ-residue of an H-small class is `−r/s mod ℓ`
(`ℓ > z > H`), so `Res_ℓ(𝔊₂)` has at most `(H+1)H ≤ z^{1/2}` elements and
`U(Res_ℓ(𝔊₂)) ≤ z^{1/2}/ℓ ≤ ℓ^{−1/2}`. ∎ (Note: the TUPLES2 form
`−r/s` with `rsm = A_M` is *not* the relevant height; e.g. `−4 ≡ −1/A_M`.)

*Remarks.* (a) Corollary 5.3 contains the family of LS3 Lemma 4.2
(`−4 = −4/1` for all `M ≡ 3 (4)`), and likewise `−1` (`D = A`), `−1/4`, `−d`, `−4d`, `−1/(4d)`, and any mixture of such classes
over **all** moduli (any number of rough primes per modulus, unbounded
moduli), together with arbitrary one-rough-prime classes. So **residue
concentration is not an obstruction**: the concentrated classes are
exactly the easy (deterministic-residue) case. LS3 §4.2's difficulty
came from summing class masses at a residue; Lemma 5.1 never sums masses
at the S-primes — it only uses that the residues lie in a fixed small set.
(b) Theorem 5.2 strictly extends LS3 Theorem 3.1 (the case 𝔊₂ = ∅).
(c) What remains for H_LS∞ over *all* forced families is the
**residue-dense, multi-rough** part: classes with two or more primes
`> z` whose residues at some rough ℓ fill a fraction `> ℓ^{−γ}` of
`ℤ/ℓ`. For generic ℛ(M) with many moduli through ℓ this happens
(`|Res_ℓ|` up to `(ℓ−1)/2`, the non-squares), and then the
deterministic set must be replaced by the random set of residues of
classes whose *other* coordinates are matched: the covering problem
(CC) of §3.2, now only for "large-height" classes (Cor 5.3 removes the
small-height ones).
