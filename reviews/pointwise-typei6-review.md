# Hostile review R99 of POINTWISE_TYPEI6.md (task O99, branch `side-agent/regime-v-units`)

Reviewer: side agent R99 (branch `side-agent/review-typei6`). From-scratch scripts: `scripts/review_typei6_*`.
Status: in progress.

## Verdicts (summary)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (a)–(d), regime (v) ⟺ `j² > mP_1` | SOUND |
| Lemma 1.3 | SOUND |
| Remark 1.2 (`L=13`, `b=1` in regime (v)) | SOUND |
| Prop 2.1 (a), (b) | SOUND |
| Prop 2.1 (c) (Schinzel, cited) | SOUND (citation matches the statement as reproduced by van der Poorten 1999; original not accessed) |
| Lemma 3.1 (identity, (a), (b), (c)) | SOUND ((c) is only asymptotic; see D3) |
| Interpretation after Lemma 3.1 | SOUND-AFTER-REPAIRS (D2) |
| Thm 3.2 (abc ⇒ finiteness per level) | SOUND-AFTER-REPAIRS (D1: case-A citation) |
| Remarks after Thm 3.2 | SOUND-AFTER-REPAIRS (D4: wording) |

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

### Prop 2.1
(a) Re-derived. `√d ∈ ℚ((1/δ))` since `d = c_o²δ²(1 + T/(c_oδ²))`; the two embeddings give `deg_±` with
`deg_+ + deg_− = deg N`; on `R^×` the norm is a nonzero constant, so `deg_+` is a homomorphism; kernel `ℚ^×` by the
`y√d` degree argument; `deg_+(η) = 1`, so `R^× = ℚ^×η^ℤ`; norm 1 forces even exponent (odd gives `−r²c_oT^k < 0`).
`ε_* = η²/(c_oT) = (2c_oδ² + T + 2δ√d)/T` verified symbolically (and `N(ε_*) = 1`). The `c_o`-variable variant:
`N(ξ) = T²/(4δ²) > 0`, so here odd exponents are allowed and the norm-1 group is `±(2δξ/T)^ℤ`; `2δξ/T = ε_*`
verified. Correct as stated. Two-variable polynomial units specialise to one-variable ones, so they are excluded too.
(b) `d ≡ 1 (8)` for `L ≥ 7`; `x_+ + x_− = 2c_oδ`, `x_+x_− = −c_oT` force valuations `{1, L−5}`, so
`v_2(ε_*^n) ∈ {n(6−L), n(L−6)}`: one embedding is negative for every `n ≠ 0`. Correct. (The parenthetical
valuations for `L = 5, 6` are loose — for `L = 5` the prime 2 ramifies — but the stated conclusion, `ε_*` integral,
is right: `ε_* = c_oδ² + 1 + δ√d` resp. `(c_oδ² + 2 + δ√d)/2` with `d ≡ 5 (8)`.)
(c) Citation check. Schinzel (Acta Arith. 6 (1961) 393–413; 7 (1962) 287–298) — originals not accessed. The statement
as reproduced by van der Poorten (Acta Arith. 89 (1999), §1, fetched from matwbn.icm.edu.pl): for integer-valued
quadratic `F(X) = A²X² + BX + C`, `A > 0`, `Δ = B² − 4A²C ≠ 0`, `lp(√F(X))` is bounded iff `Δ | 4(2A², B)²`
(other degrees / non-square leading coefficient: `lp → ∞`). This is exactly the author's form (equivalent to the
`A²X² + 2BX + C`, `B² − A²C | 4(A², B)²` form since `B` is even here). The coefficients along `δ = δ_0 + Nt`
(`A = c_oN`, `B = 2c_o²δ_0N`, `Δ = −4c_o³TN²`) are verified symbolically, and the criterion reduces to
`T | 4c_o gcd(N,δ_0)²` ⟺ `T ≤ 4` (`c_o`, `δ_0` odd). Correct. Independent evidence
(`scripts/review_typei6_period.py`, `c_o = 7`): max period over odd `δ` in growing windows is `2,2,2` (`L = 5`),
`10,10,10` (`L = 6`), `246, 1778, 6222` (`L = 7`), `982, 5514, 14402` (`L = 8`). Note (c) is not used for the
"no polynomial unit" conclusion, which follows from (a)+(b) alone.

### Lemma 3.1
Identity verified exactly (above). (a): `θ = T²c_o/(2(√d + c_oδ)²) < T²/(8c_oδ²)`, `ζ < 8X√P`, `μ > 8c_oδ²`, so
`σ > 0 ⇒ uX·T⁴/(2c_o²δ⁴) > 8c_oδ³`, i.e. `uX > 16c_o³δ⁷/T⁴`. (b): `u√Q < 4X√P` gives `X² > 4c_o³δ⁷Q/(T⁴√d)`, times
`16P`. Both correct. (b) uses only `σ > 0`, so it holds throughout regime (v); this is what Comp 4.1 needs.
(c) exact form: `Qu² > 64c_o³δ⁷√d/T⁴ − 1`, i.e. `u² > 64c_o³δ⁷P/(T⁴√d) − 1/Q`, so
`u ≳ 8c_oδ³√P/(T²τ^{1/4})` (`τ = 1 + T/(c_oδ²)`) — the stated `u ≳ 8c_oδ³√P/T²` drops `τ^{−1/4} ∈ [(1+T)^{−1/4}, 1]`.

### Theorem 3.2
abc form used: `c < K_ε rad(abc)^{1+ε}` for coprime `a + b = c`, applied to `1 + Qu² = 16PX²` (coprime trivially).
`rad(16PX²·Qu²) = rad(2·7·Q_1·P·X) ≤ 14PXQ_1` — the 7-power `u` contributes nothing new because `7 | Q` already;
this is exactly where `u = 7^b` enters (for general `u`, `rad` would contain `rad(u)`). With `X = √(c/16P)`:
`rad ≤ 3.5(d/7^a)√(c/P)`, hence `c^{(1−ε)/2} < K(3.5d/7^a)^{1+ε}P^{−(1+ε)/2}`. Inserting Lemma 3.1(b)
(`c > 64c_o⁴δ⁸/T⁴`, regime (v)) and `d = c_o²δ²τ`, then `c_o^{4ε} ≤ 7^{4aε}P^{4ε}`, I re-derive exactly
`δ^{2−6ε}7^{a(1−3ε)}P^{(1−7ε)/2} < K(3.5τ)^{1+ε}(T²/8)^{1−ε}`. `ε < 1/7` is needed precisely for the `P` exponent;
`τ ≤ 1 + T`. So `δ`, `a`, `P ≥ c'` are bounded ⇒ finitely many `d`, splittings, and (TYPEI5 Lemma 1.1) at most one
`b` each. Correct. For "all regimes" the proof cites TYPEI5 Lemma 3.6 for case A, which is proved only for
`L ∈ {7,…,10}` — see D1 (true at every `L`, short proof supplied).
Remark (ii): idealised `K = 1`, `ε → 0`: `49^aδ⁴P < 49T⁴τ²/256`; at `L = 10`, `7T⁴/256 = 458752`; the case split
`τ ≤ 1.2` / `c_oδ² < 5T` gives `c_oδ < 6.7·10⁵`. Arithmetic correct. The "idealised" inequality is not an abc
statement at all (`1 + 8 = 9` violates `c < rad`), see D4. Baker's explicit form: with `N = rad ≥ 14PX` one has
`ω ≥ 3` and `log N ≳ (1/2)log c` large, so the factor `(log N)^ω/ω!` is `≫ 10³` while emptiness at `L = 10` would need
it `≲ 1`; and `c < N^{7/4}` has exponent `7/4 > 8/7`. So the author's negative Assessment is right.

## Defects
(numbered below as found)
