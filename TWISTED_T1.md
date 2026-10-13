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
