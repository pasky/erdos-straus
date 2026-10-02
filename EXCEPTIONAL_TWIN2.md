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
