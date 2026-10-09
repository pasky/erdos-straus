# Hostile review R99 of POINTWISE_TYPEI6.md (task O99, branch `side-agent/regime-v-units`)

Reviewer: side agent R99 (branch `side-agent/review-typei6`). From-scratch scripts: `scripts/review_typei6_*`.
Status: in progress.

## Verdicts (summary)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (a)–(d), regime (v) ⟺ `j² > mP_1` | SOUND |
| Lemma 1.3 | SOUND |
| Remark 1.2 (`L=13`, `b=1` in regime (v)) | SOUND |

## Checks

### Lemma 1.1, Lemma 1.3, Remark 1.2
`scripts/review_typei6_identities.py` (sympy, from scratch): `T` is eliminated through the Pell relation
`16PX² − Qu² = 1`, so each claimed identity "on solutions" must be a rational identity in the free variables
`(c', 7^a, δ, P_1, X, u)`. Verified exactly: (a), (b) (and that `4J² − μJu + T²u²` has discriminant `64δ²d`), (c), the
relation `σ = Δ − 2Tj`, Lemma 1.3; (d) and the Lemma 3.1 identity `σ = 4uθ² − μδ√P/ζ` exactly in `ℚ(√P, √Q)` (with
`1/ζ = 4X√P − u√Q`, `θ` rationalised as `(T/2)(√d − c_oδ)²/(c_oT)`). Proofs re-derived by hand; they are correct.
Regime equivalence: by (c), `σ > 0` already forces `λ > 0` (as `j > 0`), so regime (v) ⟺ `σ ≥ 1` ⟺ (by (b), `u > 0`)
`j² > mP_1`. Correct.
Remark 1.2: from the data `(c',g,δ,P_1,X) = (79,19,1,1,17)`, `a = b = 1`, `L = 13`: Pell holds, `j = 291`, `λ = 86582`,
`σ = 48344`, `j² > mP_1`. The certificate `F = 204135`, `e = 1257047` satisfies `Fe = 1 + 2^{15}·79·7³·17²`,
`F ≡ 7 (16)`, `F ≡ −1 (mod c'k')`, `F ≡ 1 (mod 7^{a+b})`; for every split `α + 2γ = 13` it is a certificate at
`w ≡ −F (mod 2^t)` (`w ≡ 9 (16)`; e.g. `w = 665` for `γ = 2…5`), and **not** at `w = 9` (`v_2(F+9) = 4`,
`v_2(e+9) = 5 < 9 ≤ t`). So it is a genuine fibre certificate in regime (v) but irrelevant to `x̂_9`, as the remark says.

## Defects
(numbered below as found)
