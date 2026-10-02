# EXCEPTIONAL_TWIN2 — the two-prime Λ² cap (task O3)

Status: **checkpoint 2 (task O3), for parent review.** Labels follow
`DISCOVERIES.md`. PROVED means proved here and checked internally only.
Notation follows `EXCEPTIONAL_TWIN.md` (TW), `EXCEPTIONAL_THETA.md` (ET),
`POINTWISE_OMEGA2.md` (PO2).

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| Lemma 1.1, Cor 1.2 | conditional local lemma `P(B\|A_𝓢) ≤ P(B)Π(1−x_F)^{−1}`; for binary systems `≤ P(B)e^{5Σ_{ℓ∈T}w_ℓ}` | PROVED (standard) |
| Lemma 1.3 | `∂_{κ_j} log Z₂ = E[Cov_j 1_{A₋ⱼ}]/Z₂` (unconditioned rest law; no `1/J` pointwise) | PROVED |
| **Thm 1.4** | **log form of TW target (6.2)** (what Lemma 6.6 needs; TW's non-log (6.2), a bound on `Z₂/Z₁²−1`, is false for large systems, see Remark 1.6): `log(Z₂/Z₁²) ≤ (1+25δ)[Σ_e ρ̃ρ̃′π_e + Σ_j ρ̃_j q_j]` if every prime mass `w_ℓ ≤ δ ≤ 1/16`. TW's factorisation (6.3), KP and Penrose are **not needed**; vertex degrees unrestricted | PROVED; exact check 1200 systems |
| Lemma 2.1 | fibre tilting with an arbitrary fibre law P: `saving ≤ αλ/2 + log‖dP/dU‖_∞ + E_PΞ`; `ρ = 0` above `e^{λ/2}` | PROVED |
| Lemma 2.2 | hub quarantine at degree 1 is free; per-fibre bound (2.1) with `S_ℓ = Σν min(deg,1)²` | PROVED |
| Lemmas 3.1–3.4 | fibre law: QR base `≤ L^{1/2}`, local lemma on `(L^{1/2}, L^8]`, good fibres; cost `≤ 4L^{1/2}`; inflation `4Γ(k)/k` (product form) — **Reduction 6.7 steps 1, 2, 2′ (T12)** | PROVED |
| Lemma 3.3 | Shiu along the top prime (B-hypothesis `M ≤ P(M)^{1+B}`) | PROVED |
| **Lemma 4.1** | unary and diagonal binary profiles over the real fibre law `≪ α^{−3}(log L)^{O(1)}` (T14 repaired) | PROVED |
| **Thm 5.1** | Λ² saving `≤ C_B L^{3/4}(log L)^C + 11E_PΣ_jρ_jS_j` for ℛ(M)-families, `M ≤ X = e^L`, `M ≤ P(M)^{1+B}`, ≤ 2 primes above `(log X)^8`, twins included | PROVED |
| (H_O) | off-diagonal / deadly-value term `E_PΣρ_jS_j ≪ α^{−3}(log L)^{O(1)}` | OPEN |
| Lemma 5.3 | the residue of `−4D mod M` at `j \| M` is `−u′/v′`, `D = Au′/v′` | PROVED (the canonical-label remarks after it are heuristic bookkeeping) |
| **Lemma 5.4** | (H_O^=): same-canonical-label part `≪ (log L)^{O(1)}` (Brun–Titchmarsh in the partner prime, first elements charged to their m, Shiu with j innermost when j is top) | PROVED (prime powers via pointwise bound; checkpoint 2) |
| (H_O^≠) | different-label agreements mod j; reduced (§5.4) to a three-condition incidence count `#{(j,θ,θ′): d_θ \| A_{kjm}, d_{θ′} \| A_{k′jm′}, j \| a_θb_{θ′}−a_{θ′}b_θ ≠ 0}`; the j-independent version has margin L | OPEN; EVIDENCE: at or below random in all 6 tested rows |
| Cor 5.2 | Λ² cap `≪ L^{3/4}(log L)^{O(1)}` for that family | CONDITIONAL on (H_O^≠) |

**Bottom line.** The two-prime Λ² cap is reduced from TW's analytic
factorisation problem (6.3) plus unwritten Reduction steps to a single
arithmetic inequality about divisors of `(kjm+1)²/16` in residue classes
mod the large prime j. Its same-label half (the deadly values) is PROVED
(Lemma 5.4); its cross-label half (H_O^≠) is open, reduced to an incidence
count (§5.4), with numerics at or below the random prediction. The cap is stated in `L = log X` (moduli
`≤ X`, level `λ ≤ A₀L`), as in ET Cor 3.4, not in λ alone.

## 1. The binary noise-stability bound (log form of (6.2)), without the factorisation (6.3)

TW §6.8 reduced the two-prime Λ² cap to target (6.2) and proposed to prove it
through an approximate factorisation (6.3) of the pinned density. Here the
logarithmic form of (6.2) — the form Lemma 6.6 uses — is proved directly, with constant `1+O(δ)`, by differentiating in the
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

This is the logarithmic form of TW target (6.2), with `C = 1 + 25δ`; it is
what TW Lemma 6.6 consumes (`Ξ_c` is a logarithm). The factorisation (6.3) is
not needed.

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
in `q_ℓ`. The `−ν(F)ν(F′)` term was discarded. (Replacing `q_j` by the
variance of `deg_j` is *not* justified in general: two residues of equal
degree can have different avoidance probabilities; cf. TW review T15.)

**Remark 1.6 (TW's (6.2) as literally stated is false; review of this file).**
TW (6.2) bounds `E_S E(r−1)² = Z₂/Z₁² − 1`. For n disjoint edges with
endpoint masses 1/16 and `ρ̃ ≡ 1`, `Z₂/Z₁² = (256/255)^n`, so `Z₂/Z₁² − 1`
grows exponentially while the right side of (6.2) is linear in n. Only the
logarithmic form (1.2) can hold uniformly, and only it is needed.

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
1. for every `k | Q_F` and residue b, `P(c ≡ b mod k) ≤ 4Γ(k)/k`, and
   the same with `P′` and 2 in place of 4;
2. `log ‖dP/dU_F‖_∞ ≤ 4L^{1/2}`.

*Proof.* (1) `P(c ≡ b mod k) ≤ P′(…)/P′(G_L)`, and
`P′(…) ≤ P_QR(c_s ≡ b mod k₁)/P_QR(G_s) · sup_{c_s∈G_s} P(c_m ≡ b mod k₂ | Av(c_s))`.
TW Lemma 1.3(3) gives `≤ Π γ(p)/k₁`; Lemma 3.1(2) gives the medium factor;
Lemma 3.4 gives `P_QR(G_s), P′(G_L) ≥ 1/2` (dependency order:
`G_s` → inflation of `P′` (factor 2) → `G_L` → P; Lemma 3.4 uses only the
`P′` bound). (2) The density of P against
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

**Lemma 3.4 (good events are likely; PROVED).** For L large,
`P_QR(G_s) ≥ 1/2` and `P′(G_L) ≥ 1/2`.

*Proof.* Small classes have `M ≤ w₂^{1+B}` (B-hypothesis), so
`τ(A²) ≤ C_ε w₂^{(1+B)ε} = C_ε L^{1/32}`.

*T.* `E_QR T ≤ C_ε L^{1/32} Σ_k Γ(k)2^{ω(k)}/k ≪ L^{1/32}(log L)^{O(1)}`
(TW Lemma 1.3(3) for the activity probability; Euler product), so
`P(T > L^{1/2}) = o(1)`.

*μ_p.* Expanding the square, a pair of active classes through p has
probability `≤ Γ(lcm(k₁,k₁′))/lcm(k₁,k₁′)`. With (3.1) and
`Σ_{k₂: p|k₂} 2^{ω(k₂)}/k₂ ≤ (2/(p−1))(log L)^{O(1)}`,
`E_QR μ_p² ≪ L^{1/16}(log L)^{O(1)} p^{−2}`. Markov at `p^{−1/4}`:
`Σ_{p>W₁} p^{1/2}E μ_p² ≪ L^{1/16+o(1)} W₁^{−1/2} = L^{−3/16+o(1)}`.

*p_j.* Unary moduli `kj^v ≤ j^{1+B}` have `τ(A²) ≤ C_ε j^{1/256}`. With
Lemma 3.2(1) for P′ and (3.1),
`E′p_j² ≪ j^{−2+1/128}(log L)^{O(1)}`, and `Σ_{j>w₂} 64E′p_j² = o(1)`.

*w^U_j.* Split the binary classes at j by their top prime.
* j is the top prime: `M ≤ j^{1+B}`, the same pointwise bound, and
  `Σ_{m<j,u} m^{−u} ≪ log log j`, give second moment `≪ j^{−2+1/64}`.
* the partner m is the top prime, exponent `u ≥ 2`: `τ(A²) ≤ C_ε m^{1/256}`
  and `Σ_{m>j} m^{−2+1/256} ≪ j^{−1+1/256}`; second moment `≪ j^{−4+1/64}`.
* the partner m is the top prime, `u = 1`: for fixed `(k, v)` put
  `q = kj^v ≤ m^B`. Lemma 3.3 on dyadic blocks `(y, 2y]`, `y ≥ j/2`, gives
  `Σ_m τ(A²)/m ≪ (q/φ(q))L³`. Expanding the square as for μ_p,
  `E′(w^{>,1})² ≪ L⁶ j^{−2}(log L)^{O(1)}`.

So `Σ_{j>w₂} 64²E′(w^U_j)² ≪ L^{6+o(1)}/w₂ = o(1)`. ∎

This completes Reduction 6.7 steps 1, 2 and 2′ (TW review T12): the fibre
law P costs `≤ 4L^{1/2}` (Lemma 3.2(2)), every fibre in its support
satisfies the hypotheses of Lemma 2.2, and averages over P of products of
congruence indicators carry only the multiplicative inflation `4Γ(k)/k`
(Lemma 3.2(1)). The cost `L^{1/2}` is below the target `L^{3/4}`; the
choice `W₁ = L^{1/2}` is where the QR base (cost `π(W₁)log 2`) and the
medium Markov step (`W₁^{−1/2}`) meet.

## 4. Summability of the unary and diagonal binary profiles

Primes sums: by Chebyshev and partial summation, for `i ≥ 1`,
`Σ_{ℓ>w₂} ℓ^{−1−2α}(log ℓ)^i ≪ (i−1)!(2α)^{−i}`, and for `i = 0` it is
`≪ log L`. Also `Σ_{t≥0}(a + t log 2)² 2^{−αt} ≪ a²/α + a/α² + 1/α³` for
`a ≥ 1`, `0 < α ≤ 1`.

**Lemma 4.1 (profiles; PROVED).** In Setting 3.0, with `ρ_ℓ ≤ ℓ^{−α}`,

    E_P Σ_{j>w₂} ρ_j p_j(c) ≪_B α^{−3}(log L)^{O(1)},
    E_P Σ_{e={ℓ,m}} ρ_ℓ ρ_m π_e(c) ≪_B α^{−3}(log L)^{O(1)}.

*Proof.* By Lemma 3.2(1) and `ν ≤ (8/7)U` (as `p ≤ 1/8` on supp P), each
class `−4D mod M` contributes at most `4(8/7)²Γ(k)/M`, k the w₂-smooth part,
times its ρ-factor; per modulus there are `≤ τ(A²)` classes.

*Unary, `M = kj`.* j is the top prime and `k ≤ j^B`. Lemma 3.3 (`q = k`) on
dyadic blocks of j gives
`Σ_j τ(A²) j^{−1−α} ≪ (k/φ(k))(a²/α + a/α² + 1/α³)`, `a = log(2kw₂)`.
Sum against `Γ(k)/k` with (3.1).
*Unary, `M = kj^v`, v ≥ 2.* `M ≤ j^{1+B}`, `τ ≤ C_εj^{1/256}`, total
`≪ w₂^{−1/2}(log L)^{O(1)}`.

*Binary, `M = kℓ^v m^u`, m the top prime, u = 1.* Lemma 3.3 with
`q = kℓ^v ≤ m^B` on dyadic blocks `y ≥ ℓ/2` gives
`Σ_m τ(A²)m^{−1−α} ≪ (q/φ(q)) ℓ^{−α}(a²/α + a/α² + 1/α³)` with
`a ≪ log 2k + v log ℓ`. Multiply by `ℓ^{−v−α}` and sum over ℓ with the prime
sums above: the three terms give `α^{−3}`, `α^{−3}`, `α^{−3}log L` (and
`(log 2k)^i` times lower powers of `1/α`); v ≥ 2 gains a further `ℓ^{−1}`.
Sum over k with (3.1).
*Binary, `u ≥ 2`.* `τ ≤ C_εm^{1/256}`; `Σ_m m^{−2+1/256}Σ_{ℓ<m}ℓ^{−1} ≪
w₂^{−1/2}`. ∎

Both bullets of TW "What (6.2) would give" are now proved *for the diagonal
and unary terms*, over the actual fibre law (T12/T14 repaired). The
γ-weighted Lemma 3.1 that T12 asks for is replaced by (i) the product
inflation of Lemma 3.2(1), which only involves w₂-smooth k, and (ii) Shiu
along the top prime (Lemma 3.3), which needs no weights at all. The
B-hypothesis `M ≤ P(M)^{1+B}` is what makes (ii) available (`k ≤ P^B`), and
it removes TW Lemma 2.6's large-divisor constant `exp(O(W₁^{1/4}))`.

## 5. Assembly; the remaining inequality (H_O)

For a fibre c in supp P, a prime `j > w₂` and `a ∈ ℤ/j^{e_j}`, recall
`deg_c(j,a) = Σ ν_m(partner residues)` over the binary classes through the
vertex `(j,a)` that are active in c, and
`S_j(c) = Σ_a ν_j(a) min(deg_c(j,a), 1)²` (Lemma 2.2).

**Theorem 5.1 (two-prime Λ² cap, reduced to (O); PROVED).** In Setting 3.0,
for L large, every `g ∈ V_{λ/2}` with `g ≥ 1` on the avoiders of 𝓕 satisfies

    saving(g²) ≤ A₀L^{3/4}/2 + C_B L^{3/4}(log L)^{C} + 11 E_P Σ_{j>w₂} ρ_j S_j(c),

with `ρ_j = j^{−α}`, `α = L^{−1/4}`, and C an absolute exponent.

*Proof.* Lemma 2.1 with the fibre law P of §3 and `A⁺_c` = the quarantined
avoiders of Lemma 2.2 (nonempty: `Z₁ > 0` by Lemma 1.1, unary densities
`≤ 1/4`). `αλ/2 ≤ A₀L^{3/4}/2`; `log‖dP/dU_F‖ ≤ 4L^{1/2}` (Lemma 3.2);
fibre by fibre (2.1) applies (supp P ⊆ G_L, Lemma 3.4); its unary and
diagonal parts are Lemma 4.1, and its S-parts total `≤ 11 Σ_j ρ_j S_j`. ∎

**Hypothesis (H_O) (off-diagonal / deadly-value term; OPEN).**
`E_P Σ_{j>w₂} j^{−α} S_j(c) ≪_B α^{−3}(log L)^{O(1)}` in Setting 3.0.

**Corollary 5.2 (CONDITIONAL on H_O).** In Setting 3.0,
`saving(g²) ≪_{A₀,B} L^{3/4}(log L)^{O(1)}`: the Λ² cap for ℛ(M)-families
with at most two prime factors above `w₂ = (log X)^8`, twins included.

**What (H_O) is.** S_j is ET Assessment 5.8's off-diagonal quantity
`Σ_b min(1,m_b)²` (divided by j), restricted to two-prime classes, and
quarantined at 1. Bounds available:
* `S_j ≤ w_j`, so the trivial bound is `E_PΣρ_jS_j ≪ Σ_j ρ_j L³/j ≪ L³ log L`
  (useless, = total mass);
* if the active classes through j had residues `−4D mod j` spread with the
  same Γ-inflation as their moduli, `E S_j ≪ (E w_j)² j·… ≪ L^{6}/j²`
  (summable);
* the obstruction is concentration: hubs `−4D mod j` for small `D`
  (`deg ≈ (log L)/g(D)`, ET's "deadly values"), and agreements
  `D ≡ D′ (mod j)` between divisors of different `A²`. Heuristically the
  hubs give `E S_j ≈ (log L)^{O(1)}/j`, hence `Σρ_jS_j ≈ α^{−1}(log L)^{O(1)}`,
  far below the budget `α^{−3}`.

(H_O) is a statement about divisors of the shifted numbers `(kjm+1)²/16` in
residue classes mod the large prime j, averaged over the partner m and over
the fibre. It is the arithmetic content left after §§1–4; the
probabilistic part (noise stability, convergence, empty fibres, good fibres,
inflation, the diagonal profile) is closed.

### 5.1 Structure of the vertex residues, and the split of (H_O)

**Lemma 5.3 (rational labels; PROVED).** Let j be a prime dividing
`M = kj^v m^u` (Case B, `4A = M+1`). The divisors D of `A²` are exactly
`D = A·u′/v′` with `u′, v′` coprime divisors of A, and the class `−4D mod M`
has residue `−u′/v′ mod j`. In particular the residue at j depends only on
the rational `r = u′/v′`, not on k, m, or the size of D.

*Proof.* `u′/v′ := D/A` in lowest terms. `A²/D = Av′/u′ ∈ ℤ` and
`(u′,v′) = 1` give `u′ | A`; `D ∈ ℤ` gives `v′ | A`. Conversely such a pair
gives `D | A²`. Since `j | M`, `4A ≡ 1 (mod j)`, so `−4D = −4A·u′/v′ ≡ −u′/v′`
(`v′ | A` is prime to j). ∎

So, for vertices modulo j (when `e_j = 1`; for prime-power vertices modulo
`j^{e_j}`, sharing a vertex implies agreement mod j, so the following are
upper bounds), `deg_c(j,a) ≤ Σ_{r ≡ −a (mod j)} δ_r(j,c)`, where for `r = u′/v′`

    δ_r(j,c) = Σ_{(k,v,m,u): u′v′ | A_{kj^vm^u}, class active in c} ν_m(partner residue).

D = A is `r = 1` (the class `n ≡ −1 mod M`, present for every M), D = 1 is
`r = 1/A` (residue −4). The deadly values of ET §5.7 are the residues
`−r mod j` of small-height rationals r. Two classes through j share a vertex
only if their labels satisfy `u′v″ ≡ u″v′ (mod j)`; if both products are `< j`
this forces equal labels.

**Canonical labels.** Because `4A ≡ 1 (mod j)`, the residue `−4D` equals
`−4D·(4A)^{−t}` for every t, so the label should be taken up to this
relation. For `D | A²` the three candidates `t = 0,1,2` are `4D`, `D/A = u′/v′`
and `1/(4D̄)` (`D̄ = A²/D`); let `λ(D)` be the one of least height
`max(|num|, den)`. Each canonical label `λ = a/b` is realised by a single
divisibility condition on A of modulus `≪ height(λ)²` (e.g.
`A = n(n+1)`, `D = n²`, label `n/(n+1)`, needs `n(n+1) | A`) (t = 0: `D = a/(4b)` fixed;
t = 1: `ab | A`; t = 2: `D̄` fixed). Two classes with *different* canonical
labels agree at j only if `j` divides a nonzero integer `a b′ − a′ b`.

Accordingly, with `δ_λ(j,c)` the active partner mass carrying label λ,
`j·q_j ≤ (8/7)·[Σ_λ δ_λ² + Σ_{λ≠λ′, λ≡λ′ (j)} δ_λ δ_{λ′}]`, and `S_j ≤ q_j`:
* **(H_O^=) same canonical label.** `E_P Σ_j ρ_j j^{−1}Σ_λ δ_λ(j,c)²`.
  SKETCH: label λ is one congruence on A modulo some `d ≪ height(λ)²`, i.e.
  for fixed `(k, v)` one class of the *prime* m modulo d; Brun–Titchmarsh gives
  `Σ_m 1/m ≪ 1/w₂ + (log L)/φ(d)`; there are `≪ 2^{ω(d)}` labels per d;
  in δ_λ² the pairs with `d | A, A′` force
  `d | kj^v m − k′j^{v′} m′` (so `d | m−m′` only for equal `(k,v)`; the
  cross-cofactor pairs need a separate argument — a substantive gap, not
  bookkeeping), and the diagonal `m = m′` is Lemma 3.3. This would give
  `(H_O^=) ≪ α^{−1}(log L)^{O(1)}`. Not written at proof level (k-sums,
  prime powers, activity inflation, the three label types).
* **(H_O^≠) different canonical labels (OPEN).** `E_P Σ_j ρ_j j^{−1}
  Σ_{λ≠λ′, λ≡λ′ (j)} δ_λδ_{λ′} ≪ α^{−3}(log L)^{O(1)}`. The "random"
  prediction is `Σ_j ρ_j (j w_j)²/j² ≪ L^{6+o(1)}/w₂ = o(1)`, against a
  trivial bound `≍ L⁶/α`. What is missing is equidistribution of the
  residues of the canonical labels mod j, uniformly in j, with the label sets
  depending on j.

### 5.2 Numerics for (H_O) on the real system (EVIDENCE)

`scripts/twin2_offdiag.py`: moduli `M = kjm ≡ 3 (4)`, `M ≤ X`, partners m
prime `> 30`, k odd 30-smooth `≤ 45` (19 values), one random fibre c, all
`D | A²`. Columns: `jw = j·w_j`; `jq = j·q_j`; `jS = j·S_j`; `same`/`cross` =
same / different canonical label part of jq; `rand` = `((jw)² − same)/j`, the cross
part if each canonical label had an independent uniform residue.

| X | j | jw | jq | jS | same | cross | rand |
|---|---|---|---|---|---|---|---|
| 1e7 | 1009 | 83.6 | 18.3 | 16.6 | 12.9 | 5.43 | 6.91 |
| 1e7 | 10007 | 54.8 | 4.05 | 4.05 | 3.90 | 0.147 | 0.299 |
| 1e7 | 100003 | 15.5 | 0.527 | 0.527 | 0.527 | 0.000 | 0.002 |
| 1e8 | 1009 | 121.3 | 34.5 | 27.7 | 22.2 | 12.3 | 14.57 |
| 1e8 | 10007 | 103.5 | 12.2 | 11.2 | 11.6 | 0.670 | 1.07 |
| 1e8 | 100003 | 63.0 | 4.04 | 4.04 | 4.03 | 0.009 | 0.040 |

Caveats (review of this file): the toy uses one *unconditioned* random
fibre, uniform weights `1/m` (not ν, not the law P of §3), vertices mod j,
and counts repeated active edges; it is a multiplicity profile of the real
class system, not an average over P.

Reading (EVIDENCE only, toy scale, one fibre):
* the cross-label part is *at or below* the random prediction in every row.
  Without the canonical reduction (labels `u′/v′` only) it was 2–60× above
  random (e.g. 2.44 vs 0.04 at X = 1e8, j = 100003): the pairs `D = 1`,
  `D = 4A` etc. are one canonical label. This supports (H_O^≠);
* all the excess over random is same-label, i.e. the deadly values
  `−λ mod j` of small-height canonical labels — the (H_O^=) part, whose
  mechanism is identified;
* `jS` does not decay with j at fixed `X/j`-range: compare (1e7, 10007) and
  (1e8, 100003), both `jS ≈ 4.0` with similar `jw`. So `S_j ≍ F(log(X/j))/j`,
  the shape (H_O) needs; whether F is polylogarithmic cannot be decided at
  this scale (F grows from 4 to 11 as jw goes 55 → 103 at j = 10007).

## Replay

```
# Thm 1.4 exact check (3 seeds x 400 trials, each < 5 min, < 1 GB)
for s in 1 2 3; do PYTHONPATH=scripts uv run --with numpy python scripts/twin2_binary_check.py 400 $s; done
# §5.2 table (X=1e8: ~2 min, < 2 GB for the spf sieve)
for X in 1e7 1e8; do uv run --with numpy python scripts/twin2_offdiag.py $X 30 45 1 1009 10007 100003; done
```

### 5.3 (H_O^=) at proof level

**Label data.** For a class `−4D mod M` through j put `D̄ = A²/D`,
`D/A = u′/v′` (Lemma 5.3). Its *datum* is one of: `(0, D)` with modulus
`d = g(D)`; `(1, (u′,v′))` with `d = u′v′`; `(2, D̄)` with `d = g(D̄)` —
namely the one realising the least-height candidate of `λ(D)`. In each case
"the datum occurs for M" is the single condition `d | A_M` (TW/ET:
`D | A² ⇔ g(D) | A`; Lemma 5.3 for type 1), and for each d there are at most
`3·2^{ω(d)}` data with modulus d. Each canonical label is the image of at
most three data (one per type), so `Σ_λ δ_λ² ≤ 3 Σ_{data} δ_θ²`, where
`δ_θ(j,c) = Σ ν_m(partner)` over active binary classes through j with
datum θ.

**Lemma 5.4 ((H_O^=); PROVED modulo the Brun–Titchmarsh/Shiu inputs
stated).** In Setting 3.0,
`E_P Σ_{j>w₂} ρ_j j^{−1} Σ_λ δ_λ(j,c)² ≪_B (log L)^{O(1)}`.

*Proof.* Fix j. Only u = v = 1 is treated; prime powers (`m^u`, `j^v`, `u`
or `v ≥ 2`) carry an extra factor `≤ m^{−1}` or `j^{−1}` and are absorbed by
the pointwise bound `τ ≤ C_ε(top prime)^{1/256}` as in Lemma 3.4.

*(i) One class of m.* For a datum θ of modulus d and a cofactor k (with
`(k j, d) = 1`; otherwise `d | A` is impossible since `(A, kj) = 1`), `d | A`
⇔ `kjm ≡ −1 (mod 4d)`: one reduced class `s_θ(k)` of m modulo `4d`. Let
`m₀ = m₀(θ,k)` be its least prime element `> w₂` (if any, with `kjm₀ ≤ X`).
The next element exceeds `4d`; on dyadic blocks `(y,2y]`, `y ≥ 4d`,
Brun–Titchmarsh gives `≪ y/(φ(d)log(y/4d))` primes, and blocks with
`y < 8d` hold `O(1)` elements of size `≥ 4d`. Hence

    Σ_{m ≡ s_θ(k), m prime} 1/m ≤ 1/m₀(θ,k) + C (log L)/φ(d).

*(ii) Expanding the square.* With Lemma 3.2(1),
`E_P δ_θ² ≤ C Σ_{k,k′} (Γ(lcm)/lcm)(k,k′) · b_θ(k) b_θ(k′)`,
`b_θ(k) = 1/m₀(θ,k) + C(log L)/φ(d)`. By `xy ≤ (x²+y²)/2` and
`Σ_{k′}Γ(lcm(k,k′))/lcm(k,k′) ≤ (Γ(k)/k)·h(k)`, with
`h(k) = Σ_{k′}Γ(k′)gcd(k,k′)/k′ ≪ (log L)^{O(1)}τ_Γ(k)` (Euler product;
`τ_Γ(k) = Π_{p^e∥k}(1+Γ(p)e)`),

    E_P δ_θ² ≪ Σ_k (Γ(k)h(k)/k) [ m₀(θ,k)^{−2} + (log L)²/φ(d)² ].

*(iii) The BT part.* `Σ_θ (log L)²/φ(d_θ)² ≤ 3(log L)²Σ_d 2^{ω(d)}/φ(d)²
≪ (log L)²`, uniformly in j; `Σ_k Γ(k)h(k)/k ≪ (log L)^{O(1)}` (Euler
product over `p ≤ w₂`); and `Σ_{j>w₂} ρ_j/j ≪ log L`.

*(iv) The first-element part.* Charge θ to `m₀(θ,k)`: θ occurs for
`M = kjm₀`, so for fixed `(k, m)` at most `3τ(A_{kjm}²)` data have
`m₀ = m` (data are determined by divisors of `A²`, or by coprime divisor
pairs of A, which number `3^{ω(A)} ≤ τ(A²)`). So the part is at most
`Σ_k (Γ(k)h(k)/k) Σ_j (ρ_j/j) Σ_m 3τ(A_{kjm}²)/m²`, summed over binary
moduli `kjm` of the family.
* m the top prime: Lemma 3.3 (`q = kj ≤ m^B`) on dyadic blocks `y ≥ j/2`
  gives `Σ_{m>j} τ/m² ≪ (k/φ(k))L²/j`; then `Σ_j L²/j² ≪ L²/w₂`.
* j the top prime (`m < j`, `k ≤ j^B`): sum over j innermost. Lemma 3.3
  with `q = km ≤ j^{B+1}` on dyadic blocks of j gives
  `Σ_{j>m} τ(A²) j^{−1−α} ≪ (km/φ(km)) L³`; then
  `Σ_{m>w₂} L³/m² ≪ L³/w₂`.
Both are `o(1)` after the k-sum ((3.1)-type Euler products). ∎

So the same-label part of (H_O) is `≪ (log L)^{O(1)}`, far below the budget
`α^{−3} = L^{3/4}`. The gap flagged in §5.1 (cross-cofactor pairs) is closed
by (ii): the pair `(k,k′)` is controlled by the activity inflation and AM–GM,
and the label condition is used for each cofactor separately, never through
`d | m − m′`.

### 5.4 (H_O^≠) via the n-side picture: what it gives, where it stops

Write the cross part as `Σ_j ρ_j j^{−1}Σ_{θ≠θ′, λ_θ ≡ λ_{θ′} (j)} E_P δ_θδ_{θ′}`.
On the n-side (n ≡ c, two classes through j both containing n) agreement is
`j | gcd(n+4D, n+4D′)`, hence `j | D − D′ ≠ 0` (equivalently, for the
labels, `j | a b′ − a′b`). Summing over j innermost:

* **Counting heuristic, and why it does not close.** For two data θ ≠ θ′
  the label difference `ab′ − a′b` is a nonzero integer of size `≤ X^{O(1)}`,
  so it has `≤ O(L/log w₂)` prime divisors `j > w₂`, each costing
  `ρ_j/j ≤ 1/w₂`. If the masses `δ_θ` did not depend on j, the cross part
  would be `≪ (L/w₂)(Σ_θ δ_θ)² ≈ (L/w₂)·L⁶ = L^{−1}` (with `w₂ = L⁸`): a
  margin of L. But `δ_θ(j,·)` does depend on j: θ occurs at j only if
  `d_θ | A_{kjm}` for some m, and the first element `m₀(θ,k)` moves with j.
  Replacing `δ_θ(j)` by `sup_j δ_θ(j) ≤ 1/w₂ + (log L)/φ(d)` loses
  finiteness: `Σ_θ` then runs over all `≍ X^{2}` data with weight `≥ 1/w₂`.
* **The sharp remaining form.** Precisely: the bound above uses
  `δ_θ(j,c) ≤ sup_j δ_θ`, but the first-element mass `1/m₀(θ,k)` depends on j
  (θ occurs at j only if `kjm₀ ≡ −1 (mod 4d)`). Keeping the j-dependence, the
  cross part is at most `o(1)` plus

      Σ_{(k,m),(k′,m′)} (Γ(lcm)/lcm)/(m m′) · Σ_{θ | A_{kjm}, θ′ | A_{k′jm′}} Σ_{j | a_θ b_{θ′} − a_{θ′}b_θ ≠ 0} ρ_j / j,

  where now the inner j-sum is over primes j that *simultaneously* make the
  data occur (`d_θ | A_{kjm}`, `d_{θ′} | A_{k′jm′}`) and divide the label
  difference. Dropping the occurrence conditions gives `L·L⁶/w₂ = L^{−1}`,
  **but** the data range is then not finite: for fixed `(k,m,k′,m′)` the data
  θ range over divisor-labels of `A_{kjm}`, which change with j. The missing
  step is a bound for

      #{ (j, θ, θ′) : j > w₂, d_θ | A_{kjm}, d_{θ′} | A_{k′jm′}, j | a_θb_{θ′} − a_{θ′}b_θ ≠ 0 }

  weighted by `ρ_j/j`, of size `≪ L^{O(1)}/w₂^{c}` on average over
  `(k,m,k′,m′)`. This is a three-condition divisor problem in which j enters
  linearly in both `A`s and the label difference is fixed once θ, θ′ are.
  Not done.

Status: (H_O^≠) remains OPEN, reduced to the displayed incidence count.
Lenstra / Coppersmith–Howgrave-Graham–Nagaraj (divisors of N in a residue
class mod `s ≥ N^{1/4+ε}` are `O(1)`) applies only when j is the top prime
and `km ≤ j^{1−ε}`, and even then gives `O(1)` per residue, not the needed
`τ/j`; it does not close the gap.
