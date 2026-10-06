# EXCEPTIONAL_LARGESIEVE5 — the covering count (CC) for residue-dense multi-rough classes (task O67)

Status: **in progress** (agent O67, branch `side-agent/astar-dense`).
Labels as in `DISCOVERIES.md`. Notation: LS4 = `EXCEPTIONAL_LARGESIEVE4.md`
(all its notation is used: Setting 4.0, Lemma 5.1, (A*), (CC)), LS3, LS =
`EXCEPTIONAL_LARGESIEVE.md`, K2 = `EXCEPTIONAL_KARY2.md`.

## 0. Plan and summary (updated as the work proceeds)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | caps are inherited by subfamilies: it suffices to prove the all-level cap for the **full** forced family `𝔊_X` (all classes of the four types with modulus ≤ X), uniformly in X | PROVED (trivial) |
| Lemma 1.2 | **rational labels**: every forced class is `−r/s mod G` with `r, s ≤ G²`; two classes with *different* labels that agree mod g have height product `≥ g/2` | PROVED (elementary) |

## 1. Two elementary reductions

**Lemma 1.1 (monotonicity in the family; PROVED).** Let `𝔊 ⊆ 𝔊'` be finite
families. If every CRT-admissible N-large-sieve bound for `𝒜(𝔊')` saves
at most `S`, then so does every CRT-admissible bound for `𝒜(𝔊)`.
Likewise for the Hölder/(H_rough) route of LS3–LS4: a measure π on
`𝒜(𝔊')` with the required Rényi bounds serves for 𝔊.

*Proof.* `𝒜(𝔊') ⊆ 𝒜(𝔊)`. Let `M'` be a common multiple of the periods
and of the frequency denominators. A CRT-admissible bound `Z ≤ 1/L` for
𝔊 has `L ≤ F_w(π)` for every probability π on `𝒜(𝔊) mod M'` (LS §1), in
particular for every π on `𝒜(𝔊') mod M'`; so `L ≤ F*_w(𝔊')`, and the cap
for 𝔊' (which is a lower bound on `1/F*_w(𝔊')` relative to N) applies.
For the Hölder route the cap is proved by exhibiting one π supported on
the avoider set; a π on `𝒜(𝔊')` is supported on `𝒜(𝔊)`, and projecting
to a coarser modulus does not change `π̂` at frequencies whose
denominators divide it. ∎

So (A*) is needed only for the fibre laws of the **full** family `𝔊_X`
(every ℛ(M), (a,D), Case-A class with modulus ≤ X, plus selectors), with
bounds uniform in X. In particular no adversarial sub-selection of
moduli has to be handled: every sum over classes through a prime is a
complete sum over cofactors (this is what makes divisor-in-progression
averages over moduli available below). Fibres at a smooth part c are
still full in the rough direction (all rough cofactors occur).

**Lemma 1.2 (rational labels and compatibility; PROVED).** Every class of
the four types can be written `b ≡ −r/s (mod G)` with integers `r ≥ 0`,
`s ≥ 1`, `gcd(s,G) = 1`; call the rational `λ = −r/s` (in lowest terms) a
*label* of the class and `H(λ) = max(|r|, s)` its height. Labels can be
chosen with:
* ℛ(M), `A = (M+1)/4`, class `−4D`, `D | A²`, `D' = A²/D`:
  `λ = −4D` if `D ≤ A`, else `λ = −1/(4D')` (then `D' < A`); `H(λ) ≤ M+1`.
  (`4A ≡ 1 (M)` gives `D' ≡ 1/(16D)`, so `−1/(4D') ≡ −4D (mod M)`.)
* (a,D), `G = 4ag`, class `−(4D+a)`: `λ = −(4D+a)`, `H ≤ 4g² + a ≤ G²`.
* Case A, `G = 4rh`, `m·m' = 4rh² + 1`, class `−1/m`: since
  `4rh² ≡ 0 (G)`, `m m' ≡ 1` and `−1/m ≡ −m' (mod G)`; take
  `λ = −1/m` if `m ≤ m'`, else `λ = −m'`; `H ≤ √(4rh²+1)+1 ≤ G`.
* selector `0 mod p`: `λ = 0`, `H = 1`.

**Compatibility.** If two labels `λ₁ = −r₁/s₁ ≠ λ₂ = −r₂/s₂` (as rationals)
satisfy `λ₁ ≡ λ₂ (mod g)` (with `gcd(s₁s₂, g) = 1`), then
`g | r₁s₂ − r₂s₁ ≠ 0`, so `H(λ₁)H(λ₂) ≥ g/2`. Consequently a residue class
`c mod g` contains **at most one** label of height `< √(g/2)`.

*Proof.* The label formulas are the displayed congruences (for ℛ(M):
`16DD' = 16A² ≡ 1 (M)`; for Case A: `m m' ≡ 1 (G)`). Compatibility:
`λ₁ ≡ λ₂` means `r₁s₂ ≡ r₂s₁ (g)`, and `|r₁s₂ − r₂s₁| ≤ 2H₁H₂`. Two labels
of height `< √(g/2)` in one class would have `H₁H₂ < g/2`. ∎

*Why labels.* Classes with the **same** label λ (any moduli) have the same
residue at every common prime; at a point `y` their membership is
governed by the single set `Z_λ(y) = {p : y ≡ λ (mod p^{e_p})}`. So
coincidences between classes are of two kinds: *same label* (exact,
product-type, the "structured" case of LS4 §3.2) and *different labels*,
which by Lemma 1.2 cost height: one of the two labels is `≥ √(g/2)`.

## 2. Replacing the threshold conditioning by an exponential tilt

LS4 obtains (B) by conditioning the capped fibre law on the global event
`G_B = {Σ_ℓ w_ℓp̃_ℓ ≤ B} ∩ 𝒜` (Prop 4.1). For (A*) at large support this
is a bad choice (§3): `Σ_ℓ w_ℓp̃_ℓ` is moved by *every* coordinate (see
Remark 3.1), so a sharp threshold couples all coordinates, and the
pivotal method of LS4 (which takes absolute values pointwise in the coins)
cannot see the smoothing that makes the true correlation small. An
exponential tilt gives (B) equally cheaply and has **product structure**.

**Setting 2.0.** Q' is the capped fibre law of LS4 Setting 4.0 (caps
`δ_ℓ ≤ 1/2`), `Y(x) = Σ_ℓ w_ℓ p̃_ℓ(x)` with `w_ℓ ∈ [0,1]`, `𝒜` the avoider
set, and

    σ_tilt(x) := Q'(x)·1_𝒜(x)·e^{−2Y(x)} / Z,    Z = E_{Q'}[1_𝒜 e^{−2Y}].

**Proposition 2.1 ((B) for the tilted law; PROVED).**
`E_T 𝓡_2((σ_tilt)_T) ≤ Z^{−2}`, and `Z ≥ Q'(𝒜)·exp(−2E_{Q'}[Y]/Q'(𝒜))`.
In particular if `Q'(𝒜) ≥ 3/4` then
`log E_T𝓡_2((σ_tilt)_T) ≤ (16/3)E_{Q'}Y + 2 log(4/3)`.

*Proof.* By Lemma 1.1 of LS4,
`E_T𝓡_2 = E_{σ⊗σ}Π_ℓ(1+w_ℓh_ℓ) = Z^{−2}E_{Q'⊗Q'}[Φ(x)Φ(x')Π_ℓ(1+w_ℓh_ℓ)]`,
`Φ = 1_𝒜e^{−2Y} ≥ 0`. The tilting identity of LS4 Lemma 2.1 holds with any
non-negative functional of the pair path inserted (LS4 §4: `dQ/d(Q'⊗Q') =
Π_ℓZ_ℓ`), so this equals `Z^{−2}E_Q[Φ(x)Φ(x')Π_ℓ(1+w_ℓη_ℓ)]`. As in Prop
4.1, `η_ℓ ≤ p̃_ℓ(x)/(1−p̃_ℓ(x)) ≤ 2p̃_ℓ(x)`, so `Π(1+wη) ≤ e^{2Y(x)}`, and
`Φ(x)e^{2Y(x)} ≤ 1`, `Φ(x') ≤ 1`. Lower bound: Jensen,
`Z = Q'(𝒜)E[e^{−2Y}|𝒜] ≥ Q'(𝒜)e^{−2E[Y|𝒜]}` and `E[Y|𝒜] ≤ EY/Q'(𝒜)`. ∎

So in Theorem 4.2 of LS4 one may use `σ_c := σ_tilt` for the fibre law
`Q'_c` (on the event `leak_c ≤ 1/4`, `Q'_c(𝒜_c) ≥ 3/4`), with the
collision bound `log E_T𝓡_2 ≤ 6m_c + 1` in place of `2B_c + log 4`;
the rest of the proof of Thm 4.2 is unchanged, and the open input becomes

> **(A\*_tilt)** for c off an exceptional event of probability ≤ 1/32 and
> every θ ≠ 0 with z-rough denominator, `|σ̂_tilt,c(θ)| ≤ Π_{ℓ∈supp θ}Kℓ^{−γ}`.

(Lemma 5.1 / Thm 5.2 of LS4 also hold for σ_tilt: their proof only uses
that the weight is a function of the activated sets and of
avoider-membership, and that nothing changes when no pinned value meets
`R_ℓ`; `e^{−2Y}` is such a function. So the residue-sparse case is not
lost.)

The advantage: `e^{−2Y} = Π_q e^{−2w_q p̃_q}` is a **product of local
factors**, each moved by an activation at q only by a factor
`e^{−2w_q·O(1/q)}`. A change of activation at a top q is therefore
*paid* by `w_q/q` (or by the coin at q), never by a global threshold.
