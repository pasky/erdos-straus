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
| Comp 4.1 (engine, (4.1) pruning) | SOUND (code audit + independent engine) |
| Cor 4.2 (`L = 7…10`, `v_7(k) ≤ 15`) | SOUND as CERTIFIED (single engine for part of the range; provenance D7) |
| §5 model | SOUND as EVIDENCE/Assessment |

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

### Comp 4.1 / Cor 4.2 — independent re-run
`scripts/review_typei6_vsearch.c` (from scratch; different design from `typei6_vsearch`): (4.1) is checked **exactly**
in GMP for every divisor (no floating point anywhere in the decision path); `M` is factored with a smallest-prime-factor
table / trial division (not an AP sieve); all divisors of `M` are generated and filtered; loop termination uses the
`P_1 = 1` instance of the exact inequality (monotone, see audit); each hit is re-classified (case A / regime) from
scratch. Logs: `reviews/agent-reports/R99_vsearch_log.txt`.
* Positive controls: `typei4_lb` regime-(v) certificates `(13,1)`, `(16,0)×3`, `(18,1)` all found, classified
  regime (v); `(11,0)`, `(14,0)`, `(14,3)` give nothing (not regime (v)), as the author says. Relaxed controls
  `(L,u) = (7,293), (9,1853), (10,293), (12,27), (12,37), (13,29), (13,7)` all found, regime (v).
* **Completeness cross-check against brute force.** R92's independent relaxed brute force (`review_typei5_relax`,
  TYPEI4 Cor 3.2 with arbitrary odd `u`, no size bound) for all odd `u ≤ 20001 / 10001 / 6001 / 4001` at
  `L = 7 / 8 / 9 / 10` gives 12 solutions; my classifier (`scripts/review_typei6_classify.py`) puts 5 in regime (v):
  `(7,293)`, `(8,9883)`, `(9,1853)`, `(9,4003)`, `(10,293)`. My engine run on every odd `u` in the same ranges outputs
  **exactly these 5 and nothing else**. Two of them (`L = 8`, `u = 9883`; `L = 9`, `u = 4003`) are new relative to the
  author's control list, so there is now a regime-(v) positive control at **every** level 7–10.
* **Re-run, `L = 7, 8`, `b = 0…13`: 0 solutions** (well beyond the requested `b ≤ 10`; total < 2 min CPU). The number of
  divisors passing the exact bound equals the author's "candidates" count **for every `(L,b)`, `b ≤ 13`** (e.g. `L = 8`,
  `b = 13`: 64 424 838 both) — an independent check that the long-double pruning loses nothing.
* **Re-run, `L = 9, 10`, `b = 0…13`: 0 solutions** (`L = 10`, `b = 13`: 2.1·10⁹ divisors, 7 min). Candidate counts
  agree with the author's at every `(L,b)` except `L = 9`, `b = 12`: author 44 351 875, R99 44 351 874. The extra one is
  the triple `(a,c',δ) = (1, 40012187, 1)`, `P_1 = 1`, which violates the exact inequality by a relative `< 10⁻⁹` and was
  admitted only by the author's safety slack — i.e. the difference is in the safe direction (author tests a superset).
* **Extension `b = 14, 15`:** `L = 7`, `b = 14, 15`; `L = 8`, `b = 14`; `L = 9`, `b = 14`: 0 solutions, candidate counts
  equal to the author's (`L = 9`, `b = 14`: author 595 004 180, R99 595 004 179 — same slack effect). `L = 8`, `b = 15`:
  see addendum. Not run: `L = 9`, `b = 15` and `L = 10`, `b = 14, 15` (budget).
Cor 4.2 logic: case A (TYPEI5 Lemma 3.6), regimes (i)–(iv) (TYPEI5 Prop 3.3, Comp 3.4) for all `b`; regime (v) via
Lemma 3.1(b) ⇒ (4.1) ⇒ Comp 4.1. Correct. `v_7(k) = b` (`X = k'`, `7 ∤ X`) and all `a = v_7(c)` are enumerated.

### §5
A naive square-density model (`1/(2√Y)` per candidate passing the `16P` test, no local factors). It is labelled
EVIDENCE; the calibration (`4.4` predicted vs `7` found at `L = 11…20`) is consistent with "order of magnitude only".
Not replayed (not load-bearing). No defect beyond keeping the label.

## Defects

### Comp 4.1 engine (`typei6_vsearch.c`) — code audit
(4.1) is Lemma 3.1(b) weakened by `√d ≥ c_oδ` and rearranged with `Q = d/P`: correct (weaker = safe). Audit of the
pruning: with `x := c_oδ²`, `p1max = u²T⁴·x(x+T)/(δ²c'(64x⁴ − T⁴))` and `d/dx[x(x+T)/(64x⁴−T⁴)]` has numerator
`−128x⁵ − 192Tx⁴ − 2T⁴x − T⁵ < 0`; so where `64x⁴ > T⁴` the bound is strictly decreasing in each of `a`, `δ`, `c'`, and
the three `break`s (`c' = 1, δ = 1` for `a`; `c' = 1` for `δ`; doubling search for `cmax`, forced past the vacuous zone)
and the sieve/small split at `p1max < 64` are valid. Long-double evaluation with relative slack `10⁻⁹` only enlarges the
search. Sieve along `M = Ac' + T`: primes `p | A` are correctly skipped (`p ∤ M`), cofactor after primes `≤ √M_hi` is
prime, overflow guards exit loudly (`M > 2^50`, divisor count, `MAXF`, `7^a`). Final test exact (GMP), checks `X` odd,
`7 ∤ X`. No soundness defect found in the engine.
No FATAL, no MAJOR defects. All MINOR defects below are applied to POINTWISE_TYPEI6.md, marked
"(R99 repair, applied by reviewer)".

**D1 (MINOR; Thm 3.2 proof, last sentence).** "Case A … finite at each `L` unconditionally (TYPEI5 Lemma 3.6 …)":
Lemma 3.6 is proved only for `L ∈ {7,…,10}`; TYPEI5 §4 merely asserts the general case. The claim is true at every `L`:
in case A, `P_1 = c'g² + 2·7^auJ ≤ ρP_1 = Tu/2 − J` gives `J < T/(4·7^a)` and `ρ < T/(4·7^aJ)`; with `G := c'g`,
`G | y = Tu/2 + J` and `4G | 1 + 7^auρ` give `G | 7^aρJ − T/2 ≠ 0` (7 divides the first term only), so `G < T`;
then `c'g² = u(T/(2ρ) − 2·7^aJ) − J/ρ ≤ G²` with the bracket `≥ 1/(2ρ)` (it must be `> 0`), so `u ≤ 2ρ(G² + J) < T³`.
*Repair:* insert this argument (applied).

**D2 (MINOR; Interpretation after Lemma 3.1).** "`ν_0 = 2c − 1 > 128d²δ⁶/T⁴`-ish": `2c − 1 = A` is the rational part of
`ν_0 = A + 8Xu√d ≈ 2A`, and Lemma 3.1(b) gives `A > 128c_o⁴δ⁸/T⁴ − 1 = 128d²δ⁴/(τ²T⁴) − 1` (`δ⁴`, not `δ⁶`).
*Repair:* "`ν_0 > A = 2c − 1 > 128c_o⁴δ⁸/T⁴ − 1 ≈ 128d²δ⁴/T⁴`" (applied).

**D3 (MINOR; Lemma 3.1(c) and its use after Cor 4.2).** The exact consequence of (b) is
`u² > 64c_o³δ⁷P/(T⁴√d) − 1/Q`, i.e. `u ≳ 8c_oδ³√P/(T²τ^{1/4})`; the stated `8c_oδ³√P/T²` drops `τ^{−1/4}` (harmless
for large `c_oδ²/T`, but `≳` should say so). *Repair:* add the exact form (applied).

**D4 (MINOR; Remark (ii) after Thm 3.2).** (a) The "idealised limit `ε → 0`, `K = 1`" is not a form of abc at all
(`1 + 8 = 9` violates `c < rad`); it is a heuristic idealisation, and the "levels 7–10 would be empty" sentence must not
be read as conditional on any abc statement. (b) Baker's explicit form and `c < N^{7/4}` are *conjectures* ("published
explicit abc conjectures"), not results. The negative Assessment itself is right: `ω ≥ 3` and `log N ≳ (1/2)log c`
make Baker's factor `(log N)^ω/ω! ≫ 10³`, whereas emptiness at `L = 10` would need it `≲ 1.2`; `7/4 > 8/7`.
*Repair:* wording (applied).

**D5 (MINOR; Lemma 1.1 header).** "any odd `u` with `7 ∤ u`-free hypotheses as in (1.1)" is garbled. The identities
(a)–(d) hold for any positive integer `u` and any solution of `16PX² − Qu² = 1` in the notation (1.1) (verified with `u`
a free symbol). *Repair:* reword (applied).

**D6 (MINOR, cosmetic; Prop 2.1(b) closing parenthesis).** "For `L = 5, 6` the valuations are `n, 0` resp. `0, 0`": for
`L = 5`, `d ≡ 3 (4)` and 2 ramifies, so the two-embedding valuation bookkeeping of the proof does not apply as written.
The conclusion (integrality) is right: `ε_* = c_oδ² + 1 + δ√d` (`L = 5`), `(c_oδ² + 2 + δ√d)/2` with `d ≡ 5 (8)`
(`L = 6`). *Repair:* state integrality directly (applied).

**D7 (MINOR; provenance of Comp 4.1 / Cor 4.2).** "single engine" should be updated: R99's independent engine
confirms regime (v) empty for `b ≤ 13` at all of `L = 7, 8, 9, 10`, with identical candidate counts (up to the one
slack-admitted extra), and the brute-force completeness cross-check gives regime-(v) controls at every level 7–10.
Only `b = 14, 15` remain single-engine (see addendum below for any further R99 runs). *Repair:* add a
provenance note (applied).
