# Review R82 of POINTWISE_MN3.md (task O82, branch side-agent/sierpinski-si)

Reviewer: hostile side agent `side-agent/review-mn3`. Read: POINTWISE_MN3.md, POINTWISE_MN2.md (§§1–3, 5),
POINTWISE_MN.md Cor 6.1(0), POINTWISE_OMEGA12.md Lemma 2.1, AGENT_REPORT_O82.md.
From-scratch scripts: `scripts/review_mn3_*.py`.


**Summary.** The PROVED lemmas (1.1, 2.1, 3.1, 4.1, 5.1, 5.2) are correct after minor repairs; all were
re-derived and brute-forced, and every EVIDENCE number was reproduced by independent code. Two MAJOR defects,
both in the negative/localisation part: (D1) ET's 3/5 device applies verbatim — R(N) is an m-analogue of ET's
Type I count, so `R(N) ≪ N^{3/5+o(1)}`, contradicting "the same device gives only 2/3 here"; (D2) the
"exact missing input" (P)/(M2) with `K_0 ≈ 10` ignores the range `q_0 < q < Q_0`, where scales are `e^{O(q)}`
and which dominates SI's tail. SI remains OPEN; labels of (M2), SI, W_5 are correct.

## Verdicts per claim

| claim | verdict |
|---|---|
| Lemma 1.1 (`E_ν[p_0(E^-)] = 1[s|P]φ(s)/φ(M^-) ≤ ℓ/φ(N)`, `E^ν_1 ≤ 2ℓU_1`) | SOUND (re-derived; brute force exact, 0 defects) |
| Lemma 2.1 (N-parametrisation, `R(N) < ∞`) | SOUND (re-derived; brute force on 1.5·10⁶ atoms) |
| Lemma 3.1 (three levels; SI ⟸ (R_a)+(R_b)) | SOUND-AFTER-REPAIRS (proves the 3-level variant SI_3, not MN2's SI; D4) |
| Lemma 4.1 (prefix part) | SOUND-AFTER-REPAIRS (two false side statements; D5, D6) |
| Lemma 5.1 | SOUND (re-derived, reproduced Y(ℓ) and forbidden fractions) |
| Lemma 5.2 (`R(N) ≪ N^{2/3+ε}`) | SOUND, but sub-optimal: ET's device gives `N^{3/5+o(1)}` here, contrary to §5 (D1) |
| §2/§4/§5 EVIDENCE (U_1, R(N), residual shares, (M2) moments, Y(ℓ)) | all reproduced from scratch; truncation caveats (D8, D9) |
| §4 route table / residual | Assessment, not checked line by line (light review); residual shares reproduced |
| §5 "exact missing input" (P)/(AP)/(M2) with `K_0 ≈ 10` | GAP (D2: ignores the range `q_0 < q < Q_0`, which dominates SI's tail; D3: "reduces" overclaimed) |
| (M2) CONJECTURE; SI OPEN; W_5 exponent 1/4 CONDITIONAL | labels correct |

No PROVED label is FATALLY wrong. SI is correctly reported as not proved.

## Re-derivations and from-scratch checks

**Lemma 1.1.** Re-derived: `v_ℓ(Q_0) = a_ℓ ≤ a` (stage-A steps have `ℓ^{a+1} > q_0`) gives `s = gcd(M,Q_0)`;
CRT on units mod `lcm(M^-,Q_0)` with `r ≡ 1 (Q_0)` gives `1[−mD ≡ 1 (s)]φ(s)/φ(M^-)` (this needs `−mD` a unit
mod `M^-`: true since `gcd(D,M) | gcd(A²,mA−1) = 1`, `gcd(m,M) = 1`); `φ(M) = φ(M^-)·(ℓ or ℓ−1)`,
super-multiplicativity of φ. Factor 2 via `mD(mA²/D+1) ≡ mD+1 (mod M)`. Weight `K^{ω(M^-)} ≤ K^{ω(M)}` (K ≥ 1).
`scripts/review_mn3_lemma11.py` enumerates `r mod lcm(Q_0,M^-)` exactly: m = 5, q_0 = 8 (`Q_0 = 168`),
`q ≤ 32`, `M ≤ 2·10⁵`: 4125 atoms, exact probability = formula and ≤ `ℓ/φ(N)` and ≤ `ℓ/(φ(N)φ(g/s))` in every
case; same for m = 7, q_0 = 12 (6566 atoms) and m = 6, q_0 = 9 (2682 atoms).

**Lemma 2.1.** Re-derived all four identities (`fb = cP − af = aN + c`; `cM = ceN = (a+b)N`;
`u(aN+c) ≡ N² + mc²d (mod f)` with `ua = f+N`); `N ≥ (m/2)acd − 1 ≥ acd` from `eN ≥ ef − 2`.
`scripts/review_mn3_atoms.py 5 300000 15`: all 1 513 036 atoms with `D ≤ A`, `M ≤ 3·10⁵` satisfy every
identity, `N ≥ acd`, `f ≤ (m−1)N`, involution invariance of g, and `N ≠ 1`. `R(N)` for `N ≤ 15` from the raw
atom list (complete, since `M = eN ≤ N(mN³+1)`) equals the validated (a,c,d)-count. Note the unvalidated
(a,c,d)-count of the Lemma's displayed bound is ≈ 1.8× R(N) (e.g. Σ_{N≤10³}: 19674 vs 11158) — fine, it is
stated as an upper bound.

**Lemma 3.1.** Re-derived. With L levels, "no bad step ⇒ Λ(ℓ) ≤ (1−θ)^{−L}" is immediate (Lemma 1.3).
(b): a ≥ 1, ℓ (or 2) fibre lifts, Markov + MN2's supermartingale first moment (Ψ_0 = 1 for δ_1, Ψ ≤ K^{ω(M^-)}
while alive) + Lemma 1.1 give `P(bad) ≤ E^ν_1(q)/(θℓ) ≤ 2U_1(q)/θ` (the stated `4U_1/θ` is a safe overestimate);
all (b) q are distinct proper prime powers `> q_0`, and `#{proper pp ∈ (x,2x]} ≪ x^{1/2}/log x` gives
`Σ ≪ q_0^{−δ}`. (c), ℓ > q_0: `k ≥ 4`, `Σ_ℓ ℓ·ℓ^{−k(1/2+δ)}` summable. (c), ℓ ≤ q_0: `q ≥ ℓ^{a_ℓ+4} > q_0ℓ³`
(as `ℓ^{a_ℓ} > q_0/ℓ`), so the term is `≤ q_0^{−1/2}ℓ^{−1/2}` up to a geometric factor, total `≪ 1/log q_0`.
I checked that L = 3 is really needed: with L = 2, (c) at `q = ℓ³`, ℓ > q_0, would need `Σ_ℓ ℓ^{−1/2−3δ}` — divergent.
So the lemma is correct, but it proves the **three-level analogue** of SI (call it SI_3), not MN2's SI
(two levels, K = (1−θ)^{−2}) — see defect 4.

**Lemma 4.1.** The inequality is right (`M/s = N·(g/s)`, super-multiplicativity). Two statements are not:
see defects 5, 6. Brute force (`review_mn3_lemma11.py`): on every positive-weight atom `s = gcd(g,Q_0)` and
weight `≤ ℓ/(φ(N)φ(g/s))`; but on 2568 of 4125 atoms (m = 5, q_0 = 8) the weight is 0 and `s ≠ gcd(g,Q_0)`.

**Lemma 5.1.** Re-derived; trivial first clause, second clause correct (M_1 | L(ℓ) fully revealed and ℓ ∤ M_1,
so `M_1 | g`, `N ∈ {1, ℓ}`; `N = 1` never occurs — also confirmed on 1.5·10⁶ atoms). From-scratch
`review_mn3_first.py 5 11 … 31`: `Y(ℓ) = 4, 6, 7, 13, 12, 25, 6`, all with `N = ℓ`, `Y ≤ 2R_ℓ(ℓ)`
(strict only when the fixed point D = A occurs), forbidden fractions 0.200–0.455 — matches the author's 0.20–0.46.

**Lemma 5.2.** Re-derived; correct (pairwise products of a, c, d multiply to `(acd)² ≤ N²`; each case a divisor
count of a quantity `≤ N^{O(1)}`). But it is not the best this device gives — see defect 1 (MAJOR): the
author's coordinates are *exactly* Elsholtz–Tao's Type I sextuples and ET's 3/5 argument goes through verbatim.

## Defects

**D1 (MAJOR) — §5 bullet (P), §5 "Type II" remark, AGENT_REPORT ("here 2/3"): ET's 3/5 device *does* apply.**
The O12 sextuple of an atom with cofactor N satisfies `mabd = eN+1`, `ce = a+b`, `macd = N+f`,
`ef = ma²d+1`, `bf = aN+c`, `N²+mc²d = f(mbcd−N)` — exactly ET's (2.1),(2.2),(2.6),(2.7),(2.8),(2.9) with
`(4,n) ↦ (m,N)` — and `m/N = 1/(abdN) + 1/(acd) + 1/(bcd)` (checked exactly, `review_mn3_et35.py`).
So `R(N)` counts N-points of ET's Type I variety Σ_I^N (m-version) with `a ≤ b` (the *Type I* shape, `N | x`;
§5's "Type II solution count" is a mislabel). ET Lemma 2.8's bounds hold here with the same proof:
`ef ≡ 1 (m)`, `ef ≥ m+1 ≥ 5` ⇒ `bf ≤ aN/(1−2/(ef)) ≤ 5aN/3`, `c ≤ 2aN/3`; `ce ≤ 2b`; `acd ≤ N`. Hence
`e·f·(cd)²·ac = (acd)²(ce/b)(bf/a) ≤ (10/3)N³`, one of `e, f, cd, ac` is `≤ (10/3)^{1/5}N^{3/5}`, and each
case is finished by a divisor bound on `eN+1`, `(N+f)/m`, `N²+mc²d`, `aN+c` respectively (ET p. 18,
proof of Prop 1.7). Thus **`R(N) ≪ N^{3/5+O(1/log log N)}`**. Numerically (m = 5, N ≤ 3000, 48 934 atoms;
m = 7, N ≤ 2000): max of the product`/N³` is 0.75 resp. 0.30, `max min(e,f,cd,ac)/N^{0.6}` = 0.66 resp. 0.52.
*Repair:* upgrade Lemma 5.2 to 3/5 (cite ET Prop 1.7's proof with `4 ↦ m`), delete "the same device gives only
2/3 here", call R(N) a Type-I-shape count for `m/N`. (Conclusions unchanged: 3/5 is still ≫ 1/K_0.) A bonus
of the identification: first moments `Σ_{N≤X} R(N)` are ET-type averages of `f_I`, which may help (AP)/(M2).

**D2 (MAJOR) — §5 (P)/(M2) thresholds `θ, η < 1/K_0`, `K_0 ≈ 10`; §4 "Consequence"; AGENT_REPORT.**
The scale cutoff `N ≤ ℓ^{K_0}` comes from Lemma 4.1's saving, which needs `g ≥ Q_0²q^{1+3δ}`. It is polynomial
in q only for `q ≥ Q_0 = e^{(1+o(1))q_0}`. For `q_0 < q < Q_0` — which contains every term that matters for
SI's tail sums as `q_0 → ∞` — the cutoff is `(Q_0q)^{O(1)} = e^{O(q_0)}`; for `q ≲ 2q_0` even
`g ≤ M ≤ qL(q) = qQ_0e^{(1+o(1))(q−q_0)} < Q_0²q` (up to the ℓ-part), so Lemma 4.1 never fires and atoms live at all scales up to `e^{O(q)}`.
There a pointwise bound `R ≪ N^θ` with any fixed θ > 0 gives nothing (`Σ_{N''|L(q)} N''^{θ−1}` is
`exp(q^{θ+o(1)})`), and `(M2)` with `X^{1+o(1)}` does not suffice either. The data show the large scales are
real: `q·U_1(97)` = 85.4, 106.2, 118.6, 125.1 for `M ≤ 10⁶, 10⁷, 10⁸, 10⁹` (`review_mn3_u1.py`), and the
"N < q²" share falls 0.81 → 0.63. The author mentions this range once in §4 but §5, the status table and the
report present (P)/(M2) with `K_0 ≈ 10` as "the exact missing input".
*Repair:* restrict the (P)/(AP)/(M2) localisation to `q ≥ Q_0` (or `q ≥ Q_0^c`) and list the range
`q_0 < q < Q_0` as a separate open component; state (M2) in polylog form `Σ_{N≤X} R(N)² ≪ X(log X)^C`, which
(reviewer sketch, unverified) combined with Rankin (`σ ≍ 1/log q`, Cauchy–Schwarz against
`Σ_N v_q(N)N^{4σ−1} ≪ (log q)^{O(1)}`) is the form a large-scale argument would plausibly need.

**D3 (MINOR) — §5 Assessment "The (M2) route reduces SI(δ_1) at level 0 to a congruence-free second-moment
statement".** Stated as fact, but nothing is proved (the report correctly says "sketched"). Also, at level 0
SI's quantity is the pair sum `Σ_ℓ E^ν_2(ℓ)/ℓ²` ((R_a)), not the first moment `U_1(ℓ)` that §5 discusses;
heuristically it is `≈ Σ_ℓ U_1(ℓ)² +` diagonal `Σ_ℓ U_1(ℓ)/ℓ` (harmless) `+` correlations. Reviewer check of the
shape: CS gives `Σ_{ℓ~L} U_1^{(q|N)}(ℓ)² ≲ (log X)² L^{−1}Σ_{N≤X}R(N)²/N`, so with `X = L^{K_0}` (only
legitimate for `q ≥ Q_0`, D2) `η < 1/K_0` suffices for the `q | N` part — plausible, but the `q | P` part, the
correlations and the scales are missing. *Repair:* "reduces" → "would reduce (sketch), modulo …"; write the
level-0 target as (R_a) explicitly.

**D4 (MINOR) — Lemma 3.1 statement / status table "SI(δ_1) ⟸ (R_a) + (R_b)".** What is proved is SI_3:
three levels `a ∈ [a_ℓ, a_ℓ+2]` with `Y ≤ θN`, `Y = 0` above, `K = (1−θ)^{−3}` (also in the K-weights of
`U_1`, `E^ν_2`). MN2's SI (two levels) does **not** follow from (R_b): its (c) terms at `q = ℓ³`, `ℓ > q_0`,
give `Σ_ℓ ℓ^{−1/2−3δ} = ∞`. *Repair:* name it SI_3 and add one line "SI_3 ⇒ ADM_m((1−θ)^{−3}, Q(q_0)) by the
proof of MN2 Prop 5.1 / Thm 3.1 with L = 3". Cosmetic in the same proof: "N ∈ {2, ℓ}" and the bound
`4U_1/θ` (it is `2U_1/θ`); the display `Σ_ℓ min(ℓ^{−1−2δ},·)` is garbled (the clean bound is
`Σ_{dyadic x>q_0} x^{1/2}·x^{−1/2−δ} ≪ q_0^{−δ}`).

**D5 (MINOR) — Lemma 4.1, first sentence "s = gcd(g, Q_0)".** True only when `s | P` (positive weight).
Brute force (m = 5, q_0 = 8): 2568 of 4125 atoms have weight 0 and `s ≠ gcd(g,Q_0)`. *Repair:* "on atoms of
positive ν-weight".

**D6 (MINOR) — Lemma 4.1 "on atoms with `g ≥ Q_0G` … extra factor `≤ 1/φ(G)`".** φ is not monotone
(`g/s = 8 ≥ G = 7` but `1/φ(8) = 1/4 > 1/6`). *Repair:* `≤ 1/φ(g/s) ≪ (log log G)/G`.

**D7 (MINOR) — §5 "`R(N) ≤ #{(f,δ): f ≤ N+1, …}`".** `f ≤ N+1` is false: `(M,D) = (9,2)` (m = 5) has
`g = 1`, `N = 9`, `f = 11`; every `D = A` with M odd gives `f = N+2` (30 000 atoms with `M ≤ 3·10⁵`).
From `eN ≥ ef−2`: `f ≤ N + 2/e`. *Repair:* `f ≤ N+2`.

**D8 (MINOR) — §2/§4 EVIDENCE: truncation and small numeric slips.** All headline numbers reproduced from
scratch (`q·U_1 = 11.34, 35.30, 61.01, 85.37`; residual shares 0.906, 0.822, 0.810, 0.738, 0.716, 0.743 for
q = 11, 13, 23, 47, 97, 199; `Σ_{N≤10³}R = 11158`, `Σ R/N = 34.15`, maxima 127, 406, 663 (at 899, 8399,
27299), `R(9973) = 154`). But at `M ≤ 10⁶` the sums are not converged for q ≥ 47 (D2 numbers; residual share
for q = 97 is 0.678 at `M ≤ 10⁸`). Slips: the "q | N" share is 0.670–0.943 (not "70–95%"), the "N < q²" share
0.772–0.922 (not "75–90%"), `(log 23)³ = 30.8` (not 30.1). §2 "f = 2 gives every factorisation … a, d odd"
also needs d squarefree. *Repair:* state the truncation dependence; fix numbers.

**D9 (MINOR) — §5 (M2) EVIDENCE "(M2) looks true with η = o(1)".** Reproduced
`Σ_{N≤Y}R(N)²/Y = 367.2, 803.1, 1679.1, 3081.7`, but the local power exponents are 0.71, 0.61, 0.55: the range
cannot distinguish `(log Y)⁶` from `Y^{0.55}`, and `max R` grows like `N^{0.48}` on it. CONJECTURE label is
right; the sentence should read "is consistent with η = o(1); not discriminating". (Heuristic support that
does exist: R(N) ≈ Σ_f τ_3((N+f)/m)-type sums, D1's Type I identification.)

## Replay (reviewer scripts, all < 10 s each)

```
cd scripts
(ulimit -v 8000000; timeout 900 uv run python review_mn3_atoms.py 5 300000 15)                    # Lemma 2.1, D7
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_rn.py 5 30000)              # R(N), (M2) data
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_u1.py 5 1000000000 97)      # U_1, D2/D8
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_lemma11.py 5 8 32 200000)   # Lemma 1.1/4.1
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_first.py 5 11 13 17 19 23 29 31)  # Lemma 5.1
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_et35.py 5 3000)             # D1
(ulimit -v 8000000; timeout 900 uv run --with sympy python review_mn3_resid.py 5 3000000 11 97)   # residual shares
```
Sources: ET (`sources/elsholtz-tao-1107.1010.pdf`) Lemma 2.8, Prop 1.7 and its proof (p. 18) read directly.

## Round 2 / repairs applied (by the reviewer, author's context exhausted)

Merged the author's latest polish (`side-agent/sierpinski-si`; it had already relabelled (M2) ⇒ SI as a
SKETCH with five missing pieces, which covers most of D3). Then applied, one commit each, all marked
"(R82 repair, applied by reviewer)" in POINTWISE_MN3.md and AGENT_REPORT_O82.md:
* D1: Lemma 5.2 upgraded to `R(N) ≪ N^{3/5+O(1/log log N)}` with full proof (ET Type I identities with `4 ↦ m`,
  ET Lemma 2.8 bounds re-proved, four divisor cases); the old 2/3 proof is kept as superseded; the
  "Type II" label and the claim "only 2/3 here" are corrected (§0 table, §5 (P), Assessment, report).
* D2: §5 scope note — the (P)/(AP)/(M2) localisation with fixed `K_0` is restricted to `q ≥ Q_0`;
  `q_0 < q < Q_0` is listed as a separate OPEN component (new §0 table row, §4 consequence, Conj. 5.3, report).
* D3: level-0 target stated as the pair sum (R_a).
* D4: Lemma 3.1 now proves SI_3 (defined), with "SI_3 ⇒ ADM_m((1−θ)^{−3})" and the remark that MN2's two-level
  SI does not follow; `2U_1/θ` and the dyadic display fixed.
* D5, D6: Lemma 4.1 restricted to positive-weight atoms; `1/φ(G)` → `≪ log log G/G`.
* D7: `f ≤ N+2`.  D8: numbers and truncation data.  D9: (M2) data caveat.
Status after repairs: all PROVED lemmas SOUND; §5 localisation SOUND as an Assessment for `q ≥ Q_0`, with the
range `q_0 < q < Q_0` honestly OPEN. SI, ADM_m remain OPEN; W_5 exponent 1/4 CONDITIONAL.
