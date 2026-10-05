# Hostile review of POINTWISE_TRANSFER.md (task R42)

Reviewer branch `side-agent/review-transfer` (merged `side-agent/avoid-transfer` @ 97894d8).
Status: IN PROGRESS. Verdicts and defects are filled in claim by claim.

## Summary verdicts
(to be filled)

## Defects
(to be filled)

## Notes per claim

### Theorem 1.1 (abstract transfer) — step-by-step re-derivation

Checked against [SN] = `paper/es-subexp-note.tex`: `lem:lll`, `cor:lll`, `lem:brw`,
`lem:size`, `lem:l1`, `lem:twist`, `lem:tail`, `cor:el`, `thm:transfer`.

* Step 1 (atoms). The sandwich of `lem:brw` is run over the distinct atoms (cells),
  which *are* single-value events in the sense of [SN] §6 Setting, so `lem:brw`,
  `lem:size`, `lem:tail` apply verbatim to the atom list; nothing about the
  original events is needed except `F` itself. Dropping the single-value hypothesis
  is therefore legitimate; its cost is only `m_a` in place of `m`. Checked
  `m_a ≤ Σ_{j≤k}C(N,j)T^j ≤ Σ_{j≤k}(NT)^j ≤ 2(NT)^k` (NT ≥ 2). OK.
* Codegree: [SN] `lem:tail` uses only support size (remark after its proof);
  [SN] never had a codegree hypothesis in the sandwich. OK.
* Step 3 arithmetic: `2^{k₀} ≥ 400 m_a²(S+1)/δ_L` ⇒
  `m_a²·S·4·2^{−k₀} ≤ Sδ_L/(100(S+1)) ≤ δ_L/100 ≤ δ/100`. The bracketed bound
  `k₀ ≤ 2k log₂(NT)+log₂(1/δ_L)+log₂(S+1)+12` follows from `log₂1600 < 10.7` plus
  the ceiling. OK.
* Step 4: `lem:l1` with η = 1/99 needs `𝔼[F−B] ≤ 𝔼B/99`; `𝔼B ≥ 0.99δ` gives it.
  `A ≤ 1+2/99`. OK. Moduli: product of cells on `I∪J` has modulus `∏_{I∪J}ℓ^{e_ℓ}`,
  so `d ≤ T^{3k+2t}`. OK.
* Step 5 (twist, non-squarefree `f`, 2 ∈ 𝒫 allowed): for `f | ∏ℓ^{e_ℓ}` the
  ℓ-part of `f` divides `ℓ^{e_ℓ}`, so `ψ_ℓ` is a function of `X_ℓ`; for a cell on
  `I`, `f | d ⇔ primes(f) ⊆ I`, else a nontrivial `ψ_ℓ` with ℓ ∉ I averages out.
  So `μ_ψ = 𝔼[Bψ]` holds without squarefreeness / oddness. `0.21δ ≤ 0.2122μ < μ/4`. OK.
* Step 6 (general class `a`, prime `ℓ'`). Re-derived the character expansion of
  `f(n)=B(n)1[n≡a'(Q')]`: `c(χ) = χ̄_{Q'}(a')·𝔼_D[Bχ̄_D]/φ(Q')`. Properties (a),(b)
  of `thm:transfer` use only `|c(χ)|`; (c) gives `|c(χ)| = |μ_ψ|/φ(Q')`. Case A:
  `c = ±μ/φ(Q')`; with sign −1 the main terms give `(1+x^{β₁−1}/β₁)μx/φ(Q') ≥ μx/φ(Q')`
  and every error is then bounded as in Case 0 (`|R₁| ≤ μx/(400φ)`, Gallagher
  error `≤ μx/(200φ)`). OK. Mixed characters (χ₁ with conductor meeting both
  `Q'` and `D`) fall in Case B, where only `|c(χ)| ≤ |μ_ψ|/φ(Q')` with
  `ψ` = primitive character inducing `χ_D` is used; `gcd(f,Q')=1`, `f | d_i`,
  so (Tw) covers it. OK.
  `ℓ' > R ≥ max(T,Q,max d_i)` ⇒ `ℓ' ∤ QD`, `ℓ' ∉ 𝒫`; `p ≡ 1 (ℓ')` ⇒ `p > ℓ' > T`
  ⇒ `p` coprime to all free primes, so `B(p) ≤ F(p)` applies. `log Z ≤ log 2 +
  log R + log Q + (3k+2t)log T ≤ 2log Q + 2(3k+2t)log T + log 2` (as
  `log R ≤ max(log Q,(3k+2t)log T)`). `A ≤ 1.03 ≤ 2^{1/4} ≤ Z^{1/4}`. OK.
  `thm:transfer` needs `Q ≥ 2`: `Q' ≥ ℓ' ≥ 3`. OK.
* Verdict: **SOUND** (modulo G+H, as labelled). Minor presentation points below.

### Lemma 1.2, Lemma 3.2 (twist criteria)

Re-derived: `|𝔼_{X_{ℓ₀}}[ψ₀1_{Forb}]| ≤ ℙ_{X_{ℓ₀}}(Forb) ≤ Σ_{i∋ℓ₀}ℙ_{X_{ℓ₀}}(E_i | X_{−ℓ₀})`,
and `F'` does not depend on `X_{ℓ₀}`, so `𝔼[F'ℙ_{X_{ℓ₀}}(Forb)] ≤ Σ_{i∋ℓ₀}ℙ(F'=1,E_i)`.
`lem:lll` (second part) is valid for arbitrary (non-cell) events `B=E_i` on a
coordinate set; the LLL inequality restricted to a subfamily is weaker, so it
passes. Including `j=i` in `∏_{j∼i}` only enlarges `η`. Then
`𝔼F' ≤ δ/(1−η)` and `|𝔼Fψ| ≤ ηδ/(1−η) ≤ δ/5` for `η ≤ 1/6`. Lemma 3.2:
`𝔼[F'ℙ(Forb)] = 𝔼F' − 𝔼F` exactly since `F = F'(1−1_{Forb})`. Both **SOUND**.

### Corollary 1.3
`x_i = 2ℙ(E_i) ≤ 2w_ℓ ≤ 1/(32k)`; `Σ_{j∼i}x_j ≤ 2Σ_{ℓ∈supp E_i}w_ℓ ≤ 1/32`;
`1−x ≥ e^{−1.1x}` on `[0,1/32]` (0.96875 ≥ 0.96621); `log₂e^{2.2S} = 3.17S`;
`η_ℓ ≤ e^{1.1/32}/(64k) < 1/6`. The final simplification uses `log₂(S+1) ≪ S+1`
and `12 ≪ k log(4NT)`. **SOUND.**

**From-scratch toy check** `scripts/review_tr_sandwich.py` (numpy, <1 min):
Haar space `(ℤ/8)^××(ℤ/3)^××(ℤ/5)^××(ℤ/7)^××(ℤ/11)^×` (1920 points; 2 is a free
prime with `e_2 = 3`, so conductors 4, 8 and composite `f` such as `8·5·11` occur),
random *general* events (≤ 4 classes, width ≤ 2), own Efron–Stein truncation.
Passing: `B ≤ F`; BRW identity; `𝔼[F−B] ≤ m_a²Σℙ(C_j)En(F^{(j)};t)`; Lemma 3.2 chain
`|𝔼Fψ| ≤ δ^{(ℓ₀)}−δ` for all 63 real primitive `ψ` and all `ℓ₀ | f`; Lemma 1.2
(`η ≤ 1/6` ⇒ `|𝔼Fψ| ≤ δ/5`) in the 11/30 sparse systems where it applies.
Consistent with the author's toy (seed with `max|𝔼Fψ|/δ = 1` reproduced: (Tw) can fail).
