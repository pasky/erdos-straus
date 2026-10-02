# EXCEPTIONAL_TWIN2 — the two-prime Λ² cap (task O3)

Status: **in progress.** Labels follow `DISCOVERIES.md`. PROVED means proved
here and checked internally only. Notation follows `EXCEPTIONAL_TWIN.md`
(TW), `EXCEPTIONAL_THETA.md` (ET), `POINTWISE_OMEGA2.md` (PO2).

## 1. The binary noise-stability bound (6.2), without the factorisation (6.3)

TW §6.8 reduced the two-prime Λ² cap to target (6.2) and proposed to prove it
through an approximate factorisation (6.3) of the pinned density. Here (6.2)
is proved directly, with constant `1+O(δ)`, by differentiating in the
coupling and using the *unconditioned* rest law (no division by ET's `J_ℓ`)
plus a conditional local lemma. No cluster expansion is needed.

**Setting 1.0 (one good fibre).** Finitely many independent coordinates
`y_ℓ ∈ Ω_ℓ` (ℓ in a finite index set; in applications ℓ runs over primes
`> w` and `Ω_ℓ` is the set of residues mod `ℓ^{e_ℓ}` not in the unary set),
with laws `ν_ℓ`. A *vertex* is a pair `(ℓ,a)`, `a ∈ Ω_ℓ`; an *edge* is an
unordered pair `e = {(ℓ,a),(m,c)}` of vertices with `ℓ ≠ m`; it *occurs*
(is *hit*) at y iff `y_ℓ = a` and `y_m = c`. Edges form an arbitrary finite set
𝓔 (no simplicity or degree hypothesis beyond (1.1)). Put

    π_e = ν_ℓ(a)ν_m(c),   deg(ℓ,a) = Σ_{(m,c): {(ℓ,a),(m,c)}∈𝓔} ν_m(c),
    w_ℓ = Σ_a ν_ℓ(a) deg(ℓ,a) = Σ_{e∋ℓ} π_e,   q_ℓ = Σ_a ν_ℓ(a) deg(ℓ,a)²,

and assume

    w_ℓ ≤ δ  for every ℓ,   δ ≤ 1/16.                                  (1.1)

(This is implied by TW Lemma 6.9's vertex bound `deg ≤ δ`, and is weaker.)
`Z₁ = P_ν(no edge occurs)`.

*Doubled system.* For `κ ∈ [0,1]^{index set}` let `μ̃_ℓ(κ_ℓ) =
κ_ℓ·Diag_{ν_ℓ} + (1−κ_ℓ)·ν_ℓ⊗ν_ℓ` be the law of `Y_ℓ = (y_ℓ, y′_ℓ)`, the
`Y_ℓ` independent. Both marginals of `μ̃_ℓ` are `ν_ℓ`. The bad events are
`E_e = {e occurs in y}` and `E′_e = {e occurs in y′}`, each of probability
`π_e`, each a function of `(Y_ℓ, Y_m)` for `e` at ℓ, m. Put
`Z₂(κ) = P(no bad event)`. Then `Z₂(0) = Z₁²`, and with `κ = ρ̃` (TW §6.8's
unary-conditioned coupling) `Z₂(ρ̃)` is TW's `Z₂`.

**Lemma 1.1 (conditional local lemma; PROVED, standard).** Let `(Y_ℓ)` be
independent, and 𝓑 a finite family of "bad" events, each a function of
`Y_{T(E)}` for a finite set `T(E)`. For an event B depending on `Y_{T(B)}`
let `Γ(B) = {F ∈ 𝓑 : T(F) ∩ T(B) ≠ ∅}` (for `B = E ∈ 𝓑`, excluding E itself).
Suppose `x : 𝓑 → [0,1)` satisfies `P(E) ≤ x_E Π_{F∈Γ(E)}(1 − x_F)` for all
`E ∈ 𝓑`. Then for every `𝓢 ⊆ 𝓑` with `A_𝓢 := ∩_{F∈𝓢} F̄`:
1. `P(E | A_𝓢) ≤ x_E` for `E ∉ 𝓢`;
2. for every event B, `P(B | A_𝓢) ≤ P(B) · Π_{F∈Γ(B)∩𝓢}(1 − x_F)^{−1}`.

*Proof.* (1) is the Erdős–Lovász induction (Alon–Spencer, *The Probabilistic
Method*, Lemma 5.1.1): induct on |𝓢|; split `𝓢 = 𝓢₁ ⊔ 𝓢₂` with
`𝓢₁ = Γ(E) ∩ 𝓢`; then `P(E|A_𝓢) = P(E ∩ A_{𝓢₁} | A_{𝓢₂})/P(A_{𝓢₁}|A_{𝓢₂})`.
The numerator is `≤ P(E|A_{𝓢₂}) = P(E)` (E is independent of the
coordinates of 𝓢₂). Writing `𝓢₁ = {F₁,…,F_k}`, the denominator is
`Π_i (1 − P(F_i | A_{𝓢₂ ∪ {F₁..F_{i−1}}})) ≥ Π_i (1 − x_{F_i})` by induction.
(2) is the same computation with B in place of E (B need not be in 𝓑, and
only the induction hypothesis (1) is used). ∎

**Corollary 1.2.** In Setting 1.0 (any κ), take 𝓑 = all `E_e, E′_e`,
`x_F = 2P(F)`. The hypothesis of Lemma 1.1 holds. If B depends on the
coordinates `Y_ℓ, ℓ ∈ T`, then for every `𝓢 ⊆ 𝓑`

    P(B | A_𝓢) ≤ P(B) · exp(5 Σ_{ℓ∈T} w_ℓ) ≤ P(B) e^{5|T|δ}.

*Proof.* `Σ_{F∈Γ(E_e)} x_F ≤ 2·2(w_ℓ + w_m) ≤ 8δ ≤ 1/2` (each edge at ℓ
gives two events, each of probability π), so
`Π_{Γ(E)}(1−x_F) ≥ 1 − 8δ ≥ 1/2` and `P(E) = x_E/2 ≤ x_EΠ(1−x_F)`. For
(2): `Σ_{F∈Γ(B)} x_F ≤ 4Σ_{ℓ∈T} w_ℓ`, each `x_F ≤ 2δ ≤ 1/8`, and
`−log(1−x) ≤ x/(1−x) ≤ (8/7)x`, so the product is `≤ exp((32/7)Σw_ℓ)`. ∎

**Lemma 1.3 (derivative identity; PROVED).** Fix κ and an index j. Let
`A_{−j}` be "no bad event at an edge not containing j" (a function of
`Y_{−j}`), and given `Y_{−j}` let

    F = {a ∈ Ω_j : some edge {(j,a),(m,c)} has y_m = c},   F′ = same with y′.

Then, with all expectations under `⊗_{m≠j} μ̃_m(κ_m)`,

    ∂_{κ_j} log Z₂(κ) = E[(ν_j(F∩F′) − ν_j(F)ν_j(F′)) 1_{A_{−j}}] / Z₂(κ),
    Z₂(κ) = E[μ̃_j(κ_j)(F^c × F′^c) 1_{A_{−j}}] ≥ E[(1 − ν_j(F) − ν_j(F′)) 1_{A_{−j}}].

*Proof.* "No bad event" is `A_{−j} ∩ {y_j ∉ F, y′_j ∉ F′}`. Integrate out
`Y_j` first: this gives the formula for Z₂. `μ̃_j` is affine in `κ_j` with
slope `Diag − ν⊗ν`, and `Diag(F^c×F′^c) − ν⊗ν(F^c×F′^c) = 1 − ν(F∪F′) −
(1−ν(F))(1−ν(F′)) = ν(F∩F′) − ν(F)ν(F′)`. The lower bound is the union
bound, since both marginals of `μ̃_j` are `ν_j`. ∎

This is ET Prop 5.7 *before* conditioning: ET divides by `J_ℓ` inside a
conditioned expectation (ET's missing ingredient 2, "`J ≥ c` fails on rare
configurations"). Here the division is by `E[J 1_{A_{−j}}]`, a single number,
so no pointwise lower bound on J is needed.

**Theorem 1.4 (binary noise stability; PROVED).** In Setting 1.0, for every
`ρ̃ ∈ [0,1]^{index set}`,

    log (Z₂(ρ̃)/Z₁²) ≤ (1 + 25δ) [ Σ_{e={ℓ,m}} ρ̃_ℓ ρ̃_m π_e + Σ_j ρ̃_j q_j ].       (1.2)

This is TW target (6.2) with `C = 1 + 25δ`; the factorisation (6.3) is not
needed.

*Proof.* Put `κ = tρ̃`. Then `log Z₂(ρ̃) − log Z₂(0) = ∫₀¹ Σ_j ρ̃_j
(∂_{κ_j} log Z₂)(tρ̃) dt`, and `Z₂ > 0` throughout by Lemma 1.1. Fix j, t.

*Numerator.* `ν_j(F∩F′) − ν(F)ν(F′) ≤ ν_j(F∩F′) ≤ Σ_a ν_j(a) N_a N′_a`,
where `N_a` (`N′_a`) is the number of partners `(m,c)` of `(j,a)` with
`y_m = c` (`y′_m = c`). Hence the numerator is at most
`P(A_{−j}) Σ_a ν_j(a) Σ_{(m,c),(m′,c′)} P(B | A_{−j})`, with
`B = {y_m = c, y′_{m′} = c′}`, the sum over ordered pairs of partners of
`(j,a)`. B depends on `Y_m, Y_{m′}` (with m, m′ ≠ j), and `A_{−j} = A_𝓢` for
the bad events off j. Corollary 1.2 gives `P(B|A_{−j}) ≤ e^{10δ}P(B)`, and

* `m = m′, c = c′`: `P(B) = κ_mν_m(c) + (1−κ_m)ν_m(c)² ≤ ν_m(c)(tρ̃_m + ν_m(c))`;
* `m = m′, c ≠ c′`: `P(B) = (1−κ_m)ν_m(c)ν_m(c′) ≤ ν_m(c)ν_m(c′)`;
* `m ≠ m′`: `P(B) = ν_m(c)ν_{m′}(c′)`.

Summing, the pair sum is `≤ t Σ_{(m,c)} ν_m(c)ρ̃_m + deg(j,a)²`. So the
numerator is `≤ e^{10δ} P(A_{−j}) [t Σ_{e∋j} π_e ρ̃_{e∖j} + q_j]`, where
`ρ̃_{e∖j}` is ρ̃ at the other end of e.

*Denominator.* `E[ν_j(F) | A_{−j}] ≤ Σ_a ν_j(a) Σ_{(m,c)} P(y_m = c | A_{−j})
≤ e^{5δ} w_j ≤ e^{5δ}δ`, likewise for F′, so `Z₂ ≥ P(A_{−j})(1 − 2e^{5δ}δ)`.

Hence `∂_{κ_j} log Z₂(tρ̃) ≤ e^{10δ}(1−2e^{5δ}δ)^{−1}[tΣ_{e∋j}π_eρ̃_{e∖j} + q_j]`.
For `δ ≤ 1/16`, `e^{10δ}/(1 − 2e^{5δ}δ) ≤ 1 + 25δ`. Multiply by `ρ̃_j`,
sum over j (each edge is counted from both ends) and integrate
(`∫₀¹ t dt = 1/2`). ∎

*Check (EVIDENCE that the algebra is right, not part of the proof).*
`scripts/twin2_binary_check.py` computes `log(Z₂/Z₁²)` exactly (Kronecker
contraction) on random systems with 3–5 coordinates of size 5–13, random
non-uniform ν, random or hub-concentrated edges, random ρ̃. Seeds 1–3,
1200 trials, 617 within (1.1): `lhs ≤ (1+25δ)·rhs` always; the largest
`lhs/((1+25δ)rhs)` is 0.989, and `lhs/rhs` (constant 1) stays ≤ 1.03 even
outside (1.1). The bound is sharp to leading order: one edge with `ρ̃ ≡ 1`
has `lhs = −log(1−π_e)`, `rhs = π_e(1 + ν(a) + ν(c))`.

**Remark 1.5 (what was used).** Only the prime-level masses `w_ℓ ≤ δ` enter;
TW Lemma 6.9's vertex bound `deg ≤ δ`, the Mayer/KP expansion and Penrose
are not needed. Hub vertices (`deg(ℓ,a) ≫ 1`) are allowed; they show up only
in `q_ℓ`. The `−ν(F)ν(F′)` term was discarded; keeping it would replace `q_j`
by a variance (TW Lemma 6.11), which is not needed below.

## 2. Fibre tilting with an arbitrary fibre law; free hub quarantine

**Lemma 2.1 (tilting with a fibre law; PROVED).** In the setting of TW
Lemma 6.6 (F a set of coordinates, fibres `c ∈ ℤ/Q_F`), let P be any
probability on fibres, and for each `c ∈ supp P` let `A⁺_c ⊆ A_c` be
nonempty. Put `Ξ_c = log[P(A⁺_c ∩ A⁺′_c | c)/P(A⁺_c | c)²]` (copy
ρ-correlated off F, fibre shared). Then every `g ∈ V_{λ/2}` with `g ≥ 1`
on A satisfies

    saving(g²) ≤ αλ/2 + log ‖dP/dU_F‖_∞ + E_P Ξ_c,

`U_F` uniform on `ℤ/Q_F`. Moreover ρ may be taken `ρ_i = e^{−αs_i}` for
`s_i ≤ λ/2` and `ρ_i = 0` for `s_i > λ/2`.

*Proof.* TW's proof with `σ̃ = Σ_c π_c U(·|c, A⁺_c)` (supported in A, so
`E_U[g·dσ̃/dU] ≥ 1`) gives `saving ≤ αλ/2 + log(Q_F Σ_c π_c² e^{Ξ_c})`.
Take `π_c = P(c)e^{−Ξ_c}/Z`, `Z = E_P e^{−Ξ}`. Then
`Q_F Σ π_c² e^{Ξ_c} = Z^{−2} Σ_c (Q_F P(c)) P(c) e^{−Ξ_c} ≤ ‖dP/dU_F‖_∞/Z`,
and `Z ≥ e^{−E_PΞ}` (Jensen). For the last sentence: in ET Thm 5.5,
`‖Π_V h‖² = Σ_{c(T)≤λ/2}‖h_T‖²`, and every such T has all `s_i ≤ λ/2`, so
`Π_{i∈T}ρ_i = e^{−αc(T)} ≥ e^{−αλ/2}` for these T with the stated ρ. ∎

Lemma 6.6 is the case `P = U_F|R`, `A⁺ = A`. The point of a general P is that
the fibre law can be a *product-type* law with controlled inflation
(§3), instead of the uniform law on an avoidance set (review T12/T14).

**Lemma 2.2 (free hub quarantine; PROVED).** In Setting 1.0 with unary sets
`U_ℓ ⊆ ℤ/ℓ^{e_ℓ}` of uniform density `p_ℓ ≤ 1/8` and `ν_ℓ` uniform off
`U_ℓ`, suppose `w_ℓ ≤ δ/2 ≤ 1/32` for all ℓ. Let `H_ℓ = {a : deg(ℓ,a) ≥ 1}`
and `U⁺_ℓ = U_ℓ ∪ H_ℓ`, deleting the edges at hub vertices. The resulting
system has `A⁺ ⊆ A`, unary density `p⁺_ℓ ≤ p_ℓ + w_ℓ ≤ 1/4`, and (with
`ν⁺` uniform off `U⁺`) `w⁺_ℓ ≤ (16/9) w_ℓ ≤ δ`. With
`S_ℓ := Σ_a ν_ℓ(a) min(deg(ℓ,a), 1)²`, and for the fibre log-ratio of
§1 (unary factor times `Z₂/Z₁²`),

    Ξ⁺ ≤ 2 Σ_ℓ ρ_ℓ (p_ℓ + S_ℓ) + 9 Σ_{e={ℓ,m}} ρ_ℓ ρ_m π_e + 9 Σ_j ρ_j S_j,     (2.1)

where π_e, deg, S are computed in the original ν.

*Proof.* `ν(H_ℓ) ≤ Σ_a ν(a)deg(a) = w_ℓ` (Markov at 1), and `U(H) ≤ ν(H)`.
Hubs have `min(deg,1)² = 1`, so also `ν(H_ℓ) ≤ S_ℓ`. Passing from ν to ν⁺
multiplies point masses by `(1−p)/(1−p⁺) ≤ 4/3`. Hence `π⁺ ≤ (16/9)π`,
`w⁺ ≤ (16/9)w ≤ δ`, and, as non-hub vertices have `deg < 1`,
`q⁺_j ≤ (4/3)³ Σ_{a∉H} ν(a)deg(a)² ≤ (4/3)³ S_j`. The unary factor (TW
§6.8, exact) is `≤ (4/3)Σ ρ_ℓ p⁺_ℓ ≤ 2Σρ_ℓ(p_ℓ+S_ℓ)`, and `ρ̃ ≤ (4/3)ρ`.
Theorem 1.4 (δ ≤ 1/16, constant `1+25δ ≤ 2.57`) gives at most
`2.57·(16/9)²[Σρρ′π + Σρ_jS_j] ≤ 9[…]`. ∎

(Hubs are deterministic
in part — the "deadly values" `−4D mod j`, D small, of ET §5.7 — and the
quarantine turns them into unary conditions at no hypothesis cost.)

## 3. The fibre law (Reduction 6.7 steps 1, 2, 2′ at proof level)

**Setting 3.0.** Fix `B ≥ 0`, `A₀ ≥ 1`. Let `X` be large, `L = log X`, and

    W₁ = L^{1/2},   w₂ = L^8,   α = L^{−1/4},   ε = ε(B) = 1/(256(1+B)).

The family 𝓕 is any set of Case-B classes `−4D mod M` (`M ≡ 3 (4)`,
`D | A²`, `A = (M+1)/4`) with `M ≤ X`, `M ≤ P(M)^{1+B}`, and **at most two
distinct prime factors of M exceed w₂**. Twin moduli `kℓ₁ℓ₂` (`ℓ_i > w₂`,
k w₂-smooth) are included; so are dominant moduli and prime powers. All
primes are charged (`s_ℓ = log ℓ`); the majorant has level `λ ≤ A₀L`.
The fibre coordinates F are the primes `≤ w₂`. Write `k₁(k)`, `k₂(k)` for
the `W₁`-smooth part and the part with primes in `(W₁,w₂]` of a w₂-smooth k,
and (with `γ(p) = 2p/(p−1)`)

    Γ(k) = Π_{p | k, p ≤ W₁} γ(p) · Π_{p | k, W₁ < p ≤ w₂} (1 + 2p^{−1/4}).

In a fibre c, a class whose modulus is w₂-smooth is *small*; a class
`kℓ^v` (`ℓ > w₂`) is *unary* at ℓ; a class `kℓ^v m^u` is a binary edge.
Every class with `N(M) ≤ τ(A²)` classes per modulus; we use only this
count, so all bounds hold for every subfamily of the maximal family.

**The fibre law P.** Three stages.
1. `c_s := c mod (W₁-smooth part)` has the QR law of TW Lemma 1.3 at the
   odd primes `≤ W₁`, conditioned on a "small-good" event `G_s` (below). By
   TW Lemma 1.3(1) every class with `W₁`-smooth modulus is avoided.
2. Given `c_s`, `c_m := c mod (part at (W₁, w₂])` is uniform, conditioned on
   avoiding every small class C with `k₂(M_C) > 1` that is *active*
   (`c_s ≡ −4D mod k₁(M_C)`). Call this event `Av(c_s)`.
3. Condition the resulting law P′ on a "large-good" event `G_L` (below).

Then every small class is avoided by every `c ∈ supp P`.

**Lemma 3.1 (medium local lemma; PROVED).** Fix `c_s`. For each active small
class C let `E_C = {c_m ≡ −4D mod k₂(M_C)}`, `P(E_C) = 1/k₂`, and for each
prime `p ∈ (W₁,w₂]` put `μ_p(c_s) = Σ_{active C, p | M_C} 2^{ω(k₂)}/k₂`,
`T(c_s) = Σ_{active C} 2^{ω(k₂)}/k₂`. If `μ_p(c_s) ≤ 1/2` for every p, then
1. `P(Av(c_s)) ≥ e^{−2T(c_s)}`;
2. for every event `B = {c_m ≡ b mod k₂}`,
   `P(B | Av(c_s)) ≤ k₂^{−1} Π_{p | k₂}(1 + 2μ_p(c_s))`.

*Proof.* Lemma 1.1 with `x_C = 2^{ω(k₂)}/k₂ ≤ 1/2`. Every `F ∈ Γ(E_C)`
contains a prime of `k₂(M_C)`, so
`Π_{F∈Γ(E_C)}(1−x_F) ≥ Π_{p|k₂}(1 − μ_p) ≥ 2^{−ω(k₂)}`, which is the LLL
hypothesis `P(E_C) ≤ x_C Π(1−x_F)`. (1) is the usual consequence
`P(Av) ≥ Π(1−x_C) ≥ e^{−2Σx_C}`. (2) is Lemma 1.1(2) with the same
product bound and `(1−μ)^{−1} ≤ 1+2μ`. ∎

**Definition (good events).** `G_s`: `μ_p(c_s) ≤ p^{−1/4}` (`≤ 1/2`) for
every `p ∈ (W₁, w₂]`, and `T(c_s) ≤ L^{1/2}`. `G_L`: for every prime
`j > w₂`, the unary density `p_j(c) ≤ 1/8` and the binary mass
`w^U_j(c) := Σ_{binary C at j, c fits C} j^{−v}m^{−u} ≤ 1/64`.
(Then `w_j ≤ (8/7)² w^U_j ≤ 1/32 = δ/2` with δ = 1/16, as Lemma 2.2 needs.)

**Lemma 3.2 (inflation and density; PROVED given Lemma 3.3).** For L large:
1. for every w₂-smooth k and residue b, `P(c ≡ b mod k) ≤ 4Γ(k)/k`, and
   the same with `P′` and 2 in place of 4;
2. `log ‖dP/dU_F‖_∞ ≤ 4L^{1/2}`.

*Proof.* (1) `P(c ≡ b mod k) ≤ P′(…)/P′(G_L)`, and
`P′(…) ≤ P_QR(c_s ≡ b mod k₁)/P_QR(G_s) · sup_{c_s∈G_s} P(c_m ≡ b mod k₂ | Av(c_s))`.
TW Lemma 1.3(3) gives `≤ Π γ(p)/k₁`; Lemma 3.1(2) gives the medium factor;
Lemma 3.3 gives `P_QR(G_s), P′(G_L) ≥ 1/2`. (2) The density of P against
`U_F` is at most `(Q/|R_{W₁}|) · 2 · e^{2T(c_s)} · 2`; TW Lemma 1.3(2)
(`π(W₁)log 2 + O(log log W₁) ≤ L^{1/2}`) and `T ≤ L^{1/2}` on `G_s` give the
claim. ∎

**Lemma 3.3 (shifted divisor sums along the top prime; PROVED, Shiu).** For
odd `q ≥ 1` and `y ≥ 2` with `q ≤ (2y)^{B+2}`,

    Σ_{y < m ≤ 2y, qm ≡ 3 (4)} τ(((qm+1)/4)²) ≪_B y · (q/φ(q)) · (log 2qy)².

*Proof.* `A = (qm+1)/4` runs over the integers `A ≡ a (mod q)`, `4a ≡ 1`, in an
interval `(x−Y, x]` with `Y = qy/4`, `x ≤ 2Y + 1`. Shiu's theorem (Shiu,
J. reine angew. Math. 313 (1980), Thm 1; as used in ET Lemma 3.1) for
`F(A) = τ(A²)` (`F(p^l) = 2l+1 ≤ 3^l`, `F(n) ≪_η n^η`) gives
`≪ (Y/φ(q))(log x)^{−1}exp(Σ_{p≤x}3/p) ≪ (Y/φ(q))(log x)²`, provided
`q < Y^{1−β}` and `x^β < Y` with `β = 1/(2B+6)`. Both hold for `y ≥ y₀(B)`
since `q^β ≤ (2y)^{1/2}`; for `y < y₀(B)`, q and m are bounded. ∎

We also use the pointwise bound `τ(A²) ≤ C_ε A^{ε}` (ε as in 3.0), and two
Euler-product facts, valid for L large (all products over `p ≤ w₂`):

    Σ_{k w₂-smooth} Γ(k)(log 2k)^i / φ(k) ≪_i (log L)^{O(1)},
    Σ_{k,k′ w₂-smooth} Γ(lcm(k,k′))/lcm(k,k′) ≪ (log L)^{O(1)}.          (3.1)

*Proof.* `(log 2k)^i ≤ i!·(log w₂)^i·(2k)^{1/log w₂}` and `p^{1/log w₂} ≤ e`, so
the first is `≤ i!(log w₂)^i·e·Π_{p≤w₂}(1 + eΓ(p)/(p−1) + O(p^{−2}))`, with
`Γ(p) ≤ 3`. The second has Euler factors
`1 + Γ(p)Σ_{(e,e′)≠(0,0)}p^{−max(e,e′)} = 1 + 3Γ(p)/p + O(p^{−2})`. Both
products are `≪ (log w₂)^{9e} ≪ (log L)^{O(1)}`. ∎
