# TWISTED_T1 — "T1 of order k": twisted Erdős–Straus targets, anchors, and cubic obstructions (task O182, spark relay I)

Status: in progress (O182). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on DRINFELD_ES.md (O181, CLAIMED, under review R181), KUDLA_ES.md §1, FUNCTIONFIELD_ES.md. Scripts
`scripts/tw_*`, memos `BRAINSTORM/bsI_*.md`.

Notation. For a field K ⊇ μ_m and ζ ∈ μ_m primitive, (a, b)_ζ ∈ Br K[m] is the cyclic algebra; for a place v,
⟨a, b⟩_v := inv_v (a, b)_ζ ∈ (1/m)ℤ/ℤ (identified with ℤ/m). For a twisted target λ = Σ c_i/X_i we put
u_i := X_i/c_i, so λ = Σ 1/u_i is the Bright–Loughran surface, and α(u) := (−u₁/u₃, −u₂/u₃)_ζ (DRINFELD_ES §2).

## 0. Iteration log
(I1) Brief's candidate: over F_q[T] with c₁ + c₂ + c₃ = 1 "all three denominators of minimal degree" might pin the
∞-invariant. **Killed (Lemma 1.1): that configuration never occurs when deg A ≥ 1** — the prime power P must divide
a denominator. Hypothesis violated by the idea: "the degree coordinate is free". Modification: isolate the exact
algebraic condition under which a normalisation pins an invariant (§2, Anchor Lemma) and look for places where it
can hold with order m ≥ 3.

## 1. Function fields: the c₁ + c₂ + c₃ = 1 case is vacuous; the ∞-invariant is a determinant

Setting (DRINFELD_ES §3): ES_q^c(A, P): A/P = c₁/X₁ + c₂/X₂ + c₃/X₃, X_i ∈ F_q[T] monic, deg X_i ≥ n − k
(n = deg P, k = deg A ≥ 1, P monic, P = Q^e with Q irreducible, Q ∤ A), c ∈ (F_q^*)³, m | q − 1 odd.

**Lemma 1.1 (all-minimal configuration is impossible; PROVED).** Under the setting, at least one X_i has degree
≥ n > n − k. In particular no solution has all three denominators of the minimal degree n − k, whatever c is.
*Proof.* v_Q(A/P) = −e. If v_Q(c_i/X_i) ≥ −e + 1 for all i then v_Q(Σ) ≥ −e + 1, contradiction. So some X_i has
v_Q(X_i) ≥ e, deg X_i ≥ e·deg Q = n. ∎
(For k = 0, A = 1, the all-minimal configuration exists — e.g. X₁ = X₂ = X₃ = P when c₁ + c₂ + c₃ = 1 — but this
is the degenerate "1/n" problem.) So the hoped-for degeneration of the degree character does not exist: Lemma 3.2
of DRINFELD_ES always applies. Its formula has a symmetric form:

**Proposition 1.2 (∞-invariant = a determinant; PROVED).** Write d_i = deg X_i and fix a generator of
F_q^*/F_q^{*m} ≅ ℤ/m, w_i := class of c_i. For every solution u of ES_q^c, the odd-order (order m) part of
inv_∞ α(u) equals, up to a global sign convention,
`χ_∞(u) = det [[1, 1, 1], [w₁, w₂, w₃], [d₁, d₂, d₃]] = w₁(d₂ − d₃) + w₂(d₃ − d₁) + w₃(d₁ − d₂)  (mod m).`
*Proof.* At ∞ (uniformiser 1/T), a = −u₁/u₃ has sign −c₃/c₁ and valuation d₃ − d₁; b = −u₂/u₃ has sign −c₃/c₂ and
valuation d₃ − d₂. Tame symbol {a, b}_∞ = (−1)^{v(a)v(b)} sgn(a)^{v(b)} sgn(b)^{−v(a)}; discarding ±1 (order 2,
m odd): (c₃/c₁)^{d₃−d₂}(c₃/c₂)^{d₁−d₃}; taking logs gives (w₃ − w₁)(d₃ − d₂) + (w₃ − w₂)(d₁ − d₃), which expands
to the determinant. ∎
(It agrees with DRINFELD_ES Lemma 3.2 whenever the minimal-degree c's sum to 1, which Lemma 1.1 and the leading-term
identity guarantee; the determinant form is manifestly antisymmetric under relabelling, as α is.)

**Corollary 1.3 (exact scope of the function-field order-m T1; PROVED from DRINFELD_ES Thm 3.3).** At P = Q^m, every
Type I/II-shaped solution satisfies det(1, w, d) ≡ 0 (mod m). This is a condition on the vector of degrees only;
it is empty iff all w_i are equal (c_i/c_j ∈ F_q^{*m}), i.e. iff the twist is trivial mod m-th powers.
*Proof.* Thm 3.3 + Lemma 3.1 + reciprocity give χ_∞(u) = 0; if the w_i are not all equal, the linear form
d ↦ det(1, w, d) is non-zero on ℤ³ (e.g. d = (1,0,0) gives w₂ − w₃ or a permutation is ≠ 0). ∎

## 2. The anchor calculus: which normalisations can pin an order-m invariant

(I2) Abstracting what T1 uses: a place where a *normalisation* of the denominators (positivity, monic, primary,
congruence) pins inv_v α to a constant, and a reciprocity argument. Below: exact conditions.

Fix a place v of K ⊇ μ_m, V_v := K_v^*/K_v^{*m}, and the Hilbert pairing ⟨·,·⟩_v : V_v × V_v → ℤ/m.
It satisfies ⟨a, a⟩ = ⟨a, −1⟩; **for odd m it is alternating** (−1 = (−1)^m), for m = 2 it is symmetric
but not alternating at v where ⟨−1, −1⟩_v ≠ 0 (v real, v = 2 over ℚ). A *normalisation* at v is a subgroup
N_v ⊂ K_v^* in which the denominators X_i are required to lie; N̄_v is its image in V_v. Put
`τ₁ := −c₃/c₁, τ₂ := −c₃/c₂` (the *twisted targets*; for ES, c = (1,1,1), τ₁ = τ₂ = −1).

**Lemma 2.1 (anchor lemma; PROVED, linear algebra).** As X ranges over N_v³, the value inv_v α(X/c) is constant
iff N̄_v is isotropic (⟨N̄_v, N̄_v⟩ = 0) and τ₁, τ₂ ∈ N̄_v^⊥. The constant is then ⟨τ₁, τ₂⟩_v, which for odd m equals
`⟨c₁, c₂⟩_v + ⟨c₂, c₃⟩_v + ⟨c₃, c₁⟩_v.`
*Proof.* α(X/c) = (τ₁r, τ₂s) with r = X₁/X₃, s = X₂/X₃; as X ranges over N_v³, (r, s) ranges over all of N_v²
(take X₃ = 1). By bilinearity inv_v = ⟨τ₁, τ₂⟩ + ⟨τ₁, s⟩ + ⟨r, τ₂⟩ + ⟨r, s⟩. Constancy with r = 1 (resp. s = 1)
forces τ₁ ⊥ N̄ (resp. τ₂ ⊥ N̄), and then ⟨r, s⟩ = 0. Converse clear. For odd m, ⟨−x, y⟩ = ⟨x, y⟩ and
⟨c₃/c₁, c₃/c₂⟩ expands, by antisymmetry and ⟨c₃, c₃⟩ = 0, to the cyclic sum. ∎
(This is the *normalisation-only* anchor; the equation itself may pin further invariants, see Lemma 2.4.)

**Corollary 2.2 (catalogue of natural normalisations; PROVED).**
(a) v real, m = 2, N_v = ℝ_{>0} (positivity): N̄ = 0, anchor ⟨τ₁, τ₂⟩_∞ = ½ iff τ₁, τ₂ < 0 (e.g. all c_i > 0).
This is the ES anchor: ⟨−1, −1⟩_∞ = ½ (Hamilton quaternions).
(b) v complex: V_v = 0, no anchor of any order.
(c) v = ∞ of F_q(T), N_v = monic (Hayes sign): V_v ≅ F_q^*/F_q^{*m} × ℤ/m (sign × degree), N̄ = ⟨T⟩ is
**Lagrangian** (order m in a non-degenerate alternating space of order m², isotropic as ⟨T, T⟩ = ⟨T, −1⟩ = 0).
So τ_i ⊥ N̄ forces τ_i ∈ N̄ and the anchor is ⟨N̄, N̄⟩ = 0; otherwise the invariant is the degree character of
Prop 1.2. **No twist by constants anchors anything at ∞ over F_q(T).** (DRINFELD_ES §3 "degree unpinnable", now as
a one-line structural fact.)
(d) v tame finite, N_v = O_v^* ("v-unit"): N̄ = units, again Lagrangian ⇒ anchor 0 or non-constant.
(e) v tame finite, N_v = 1 + 𝔪_v ("≡ 1 mod v"): a pro-ℓ group with ℓ ∤ m, hence m-divisible: N̄ = 0, and every
τ gives a pinned anchor ⟨τ₁, τ₂⟩_v (non-zero only if some τ_i has v(τ_i) ≢ 0 mod m).
(f) v = λ = (1 − ζ₃) over ℚ(ζ₃), m = 3, N_v = ±(1 + 3O_λ) ("x ≡ ±1 mod 3", the cubic-reciprocity *primary*
normalisation up to the cube −1): N̄ = U^{(2)}K^{*3}/K^{*3} has order 9 in V_λ (order 3^{2+2} = 81) and is isotropic
because ⟨U^{(i)}, U^{(j)}⟩ = 0 for i + j > pe/(p − 1) = 3; hence Lagrangian, anchor 0 or non-constant.
*Proof.* (a), (b) standard. (c) tame symbol: ⟨T, c⟩ = c^{±1}, ⟨c, c'⟩ = 0 for constants. (d) tame symbol of two
units is 1; ⟨π, u⟩ = ū^{±1}, so units = units^⊥. (e) clear. (f) the bound on ⟨U^{(i)}, U^{(j)}⟩ is the standard
conductor estimate for the p-th Hilbert symbol (Fesenko–Vostokov Ch. IV; Serre, *Local Fields*, XIV); orders from
|K^*/K^{*p}| = p^{2+[K:ℚ_p]} and U^{(4)} ⊂ K^{*3} (U^{(i)} ⊂ K^{*p} for i > pe/(p − 1)). Isotropic of order
√|V| in a non-degenerate alternating space ⇒ Lagrangian. ∎

**Proposition 2.3 (an anchor needs a ramified constant algebra; PROVED).** Suppose the anchors at the normalised
places S are pinned (Lemma 2.1) and the total anchor A_S := Σ_{v∈S} ⟨τ₁, τ₂⟩_v is non-zero. Then the constant
cyclic algebra (τ₁, τ₂)_ζ ∈ Br K is ramified at some w ∉ S (reciprocity: Σ_all v ⟨τ₁, τ₂⟩_v = 0).
Consequences: (i) **F_q(T), constant twists: never** — (τ₁, τ₂) is a symbol of two constants, unramified
everywhere (tame symbols of units; also at ∞), so it is 0 in Br F_q(T). (ii) **ℚ(ζ₃), unit twists c_i ∈ μ₆: never**
— units are tame-trivial at all v ∤ 3, and at λ ⟨ζ^a, ζ^b⟩ = ab⟨ζ, ζ⟩ = ab⟨ζ, −1⟩ = 0. So the brief's
"ζ₃ as an order-3 target" does not anchor: for odd m a single target t never anchors (⟨t, t⟩ = 0); two
independent constants with ⟨τ₁, τ₂⟩ ≠ 0 are needed. (iii) ES over ℚ: (−1, −1) = Hamilton quaternions, ramified at
{∞, 2}: anchor ∞, *partner* 2.
**Principle (Assessment, made precise by 2.1–2.3).** "The T1 obstruction for target −1 has order 2" is literally:
the anchor is ⟨−1, −1⟩, which is non-zero only because the m = 2 Hilbert symbol is not alternating. For odd m an
order-m T1 needs (α) a pinned normalised place v₀ (Lagrangian normalisations — monic, unit, primary — never pin a
non-zero value), and (β) a partner place w where the constant algebra (τ₁, τ₂) ramifies but the *equation*
forces inv_w α(u) = 0 on all integral points (for ES: w = 2, forced by the numerator 4 — BL).
