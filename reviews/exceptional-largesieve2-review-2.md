# Hostile review R27b — EXCEPTIONAL_LARGESIEVE2.md §§8–9 (checkpoint 3 of O27)

Reviewer: side agent `review-ls2b`. Scope: §§8–9 only (Lemma 8.1, Props 8.2,
8.4, Lemma 8.3, Thm 8.5 + Consequences, Thm 9.1, Prop 9.2, §9 Status).
Reviewed at `side-agent/ls-escapes` @ 519aab5. From-scratch scripts:
`scripts/review_ls2b_*.py`. (Work in progress; verdict table filled in as
checks complete.)

## Verdicts

| claim | verdict |
|---|---|
| Lemma 8.1 | SOUND |
| Prop 8.2(a) | SOUND |
| Prop 8.2(b) | SOUND-AFTER-REPAIRS (m1: needs `\ell'_i \ge 36`) |
| Lemma 8.3 | (pending) |
| Prop 8.4 | (pending) |
| Thm 8.5 | (pending) |
| Thm 8.5 Consequences 1–3 | (pending) |
| Thm 9.1 | (pending) |
| Prop 9.2 | (pending) |
| §9 Status / "Open precisely" | (pending) |

## Line-by-line notes

**Lemma 8.1.** Re-derived. Gale/Hall for a transportation problem with
equal totals (1 = 1): feasible iff `|R|/ℓ ≤ |N(R)|/ℓ'` for all row sets R ✓.
C(R) = columns y with `β(y) ∈ ∩_{α∈α(R)}(B − α)`. Two arcs `B−α₁, B−α₂`
(open, length 2η, centres at circular distance ≥ 2η) are disjoint ✓. If all
pairwise distances are < 2η ≤ 1/4, α(R) lies in an arc of length < 2η (all
points lie within 2η < 1/2 of any one of them, so the configuration is
“linear” and has diameter < 2η) — the doc says “otherwise α(R) lies in an
arc of length < 2η” without this one-line justification (trivial, noted
only). Point counts `≤ 2ηℓ+1`, `≤ 2ηℓ'+1` ✓; `4η + 1/ℓ + 1/ℓ' ≤ 1/2 + 2/5 < 1` ✓.
CRT phase decomposition `na/D ≡ nau/ℓ + nav/ℓ'` with `uℓ'+vℓ = 1` ✓.
*From scratch* (`review_ls2b_gale.py`): direct transportation-LP
feasibility (not via the author's reduction) for all pairs of primes in
[5,47], 6 random a each, both orders, η ∈ {1/8,1/9,1/10,1/20}: 3744 cases,
0 failures. A scan of η upward finds the first infeasible case only at
η ≈ 0.36 (ℓ,ℓ' = 5,7), so the hypothesis η ≤ 1/8 has a large margin.

## Defects

**Prop 8.2(a).** Re-derived. Level is W-rough level over *distinct* primes,
so a modulus of level `≤ λ < L_i` is not divisible by both `ℓ_i, ℓ'_i`
(prime powers do not help it) ✓. μ = ⊗μ_i on the digits mod `D_i`, other
digits (incl. higher powers of `ℓ_i`, W-smooth part, foreign primes)
uniform and independent: the law of `n mod d` is then uniform for every
allowed d ✓, so `E_μ = E_U` on `V_𝒟` and `E_Uν = E_μν ≥ 1` ✓. μ itself is a
comparison measure with S = 0 directly (no LP duality or K2 input needed;
the band family is not a K2 mixture, and the doc rightly does not invoke
K2 Thm 5.1 here) ✓.
*From scratch* (`review_ls2b_lp.py`): K = 2 band families
(`Q = 5005`, three prime pairings × 3 random `(a₁,a₂)`, η = 1/8), exact LP
for the best majorant in the span of class indicators mod
`{ℓ_1ℓ_2, ℓ_1ℓ'_2, ℓ'_1ℓ_2, ℓ'_1ℓ'_2}` (the maximal allowed moduli): value
**1.000000** in all 9 cases, although the density of 𝒜 is ≈ 0.56–0.58.
Control: allowing `D_1` drops the LP value to 0.74–0.77, so the LP is
not trivially stuck at 1.

**Prop 8.2(b).** Re-derived against EK §1–2 (Thm 2.5, Cor 2.6, Lemma 2.1).
Averaging over non-band digits keeps `ν ≥ 0`, `ν ≥ 1` on 𝒜 (𝒜 depends
only on band digits) and the mean ✓; a term of level `≤ λ` contains
`< d` band primes when all exceed `e^{λ/d}` ✓ (so "at most d" holds with
room). Patterns are the binary pairs with top `ℓ'_i`; at `ℓ_i` the
activated set is empty ✓. Light: `p_{ℓ'_i} ≤ (2ηℓ'_i+1)/ℓ'_i = 2η + 1/ℓ'_i`,
and with η = 1/9 this is `≤ 1/4` **only if `ℓ'_i ≥ 36`** — not among the
stated hypotheses (`ℓ > max(W, e^{λ/d})`); it holds if `W ≥ 36`, which is
true for K2's `W₀` but is never said (defect m1). Then all tops light,
σ ⊂ 𝒜 a.s. (EK Lemma 2.1(1)), `M ≤ K/4` pathwise, Cor 2.6 with
`m̄ = K/4`, and Jensen `E e^{−Φ} ≥ e^{−EΦ}` give exactly the stated bound ✓.
Note (b) is not used by Thm 8.5.
