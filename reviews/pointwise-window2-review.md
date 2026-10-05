# Hostile review R29 of O29 / POINTWISE_WINDOW2.md

Reviewer branch `side-agent/review-window2`; author branch `side-agent/window-parity` @1c7763c.
All numerical checks are from-scratch (`scripts/review_w2_*.py`); no author code reused.

Status: round 1 complete.

## Summary

| claim | verdict |
|---|---|
| Lemma 1.1/1.2 (norm forms, FI09 shape) | SOUND |
| Thm P1, one window | SOUND (minor m5) |
| Thm P1, joint four-class sentence | GAP (M1) — joint data differ at d₂=3 |
| Lemma 3.2, 3.6 | SOUND (m2 wording) |
| §3.3–3.4 block/tree MC | SOUND as EVIDENCE (m3) |
| §3.5 LP values | SOUND; several now CERTIFIED by reviewer duals (m6) |
| Prop 3.7 (discrete fake, ε=0.1, K=8) | SOUND — re-verified from scratch at 60 digits |
| Relevance of model to real sieves (§4, §5) | GAP (M2 scope, M4 fidelity) |
| §5 item 2 "parity sufficient for one window (W1)" | GAP (M3: W1 uses switching) |
| §6.1–6.2 caps | numbers SOUND (EVIDENCE); interpretation m4 |
| §6.3 slice reduction | SOUND after m1 |
| Routes (ii), (iv), (v) Assessments | honest as Assessments; (ii) supported by reviewer mixed-level test (m7) |

Labels: nothing about actual primes is claimed beyond Lemma 1.2 and P1, except the §4/§5 wording
flagged in M2/M3. The "true law" is called heuristic in §3.3 and §6.1, but Prop 3.7 and §4/§5 omit
that the model data are those of a coarse heuristic law (M4).

## Verdicts per claim

### Prop 3.7 (certified fake at θ=1/2, discrete model ε=0.1, K=8) — SOUND (as a discrete-model statement)
`scripts/review_w2_certify.py data/window2/fake_eps0.1_K8_theta0.5.json.gz` (mpmath, 60 digits):
* independently enumerated window configurations: 113 (even count, Σg<1), 12769 joint — identical
  to the dump's set; μ agrees to 5e-14 relative.
* 89 visible correlations (all pairs of multiplicity vectors with total ≤ θ, any parity).
* dumped ν: ν≥0, ν(∅,∅)=0, max relative residual 9.0e-15; support = 89 configs, ν/μ∈[0.1542, 92506].
* 60-digit LU solve of the 89×89 square system restricted to the support: solution agrees with the
  dump to 7e-13, min ν/μ = 0.15423 > 0, cond₁ = 3.0e5. Hence the exact (real-arithmetic) system
  has a strictly positive solution with ν(∅,∅)=0: the certificate is genuine, not a float artefact.
* Fragility note: the closest visible/invisible boundary is a 4-point S (3×0.1155+0.1540 = 0.50043)
  at distance 4.3e-4 above θ. The statement is for the discrete model only (see defects).

### Thm P1 (§2) — one window: SOUND-AFTER-REPAIRS (minor); joint "four sign classes" sentence: GAP
`scripts/review_w2_p1.py 3e6` (sympy factorisation, all primes ≤3·10⁶):
* `A^+ = {p≡1 (840)}` exactly (W1's set), `A^- = {p≡281 (840)}`. |A⁺|=1115, |A⁻|=1138.
* `A^-`: n₃ clean for **0** primes (as claimed; trivially, `n₃≡p≡2 (3)`). `A^+`: 640 clean.
* `(−1)^{Ω₃⁻(n₃)}=(p/3)` (with multiplicity) for every p≡1 (8) ≤3·10⁶: 0 violations.
* `|A^±_d|` for d∈{11,17,23,29,41,47,53,187,253,391} agree to sampling noise; for 5|d both are 0.
* The proof is correct: the conditions are one residue class mod 840d, BV with modulus ≤840·x^{1/2}(log x)^{−B}.
  The A⁻ half (S=0, identical data) is all that "parity is necessary" needs, and it is unconditional
  (BV is a theorem); only the A⁺ lower bound inherits W1's dependence on S1–S3.
* Joint version (last sentence of the theorem): the three "wrong" classes indeed have 0 both-clean
  elements (brute force: (−,−) 0/3390, (−,+) 0/3374, (+,−) 0/3417; (+,+) 1262/3309), and
  `(−1)^{Ω₇⁻(n₇)}=(p/7)` holds without exception. **But the joint sieve data are not identical across
  all four classes:** 3 is a window-7 bad prime ((3/7)=−1) and `3 | n₇=(p+7)/4` for *every* p with
  (p/3)=−1 and for *no* p with (p/3)=+1 (brute force: 3390/3390, 3374/3374 vs 0, 0). So
  `|A_{d₁·3}|` distinguishes (p/3)=−1 from +1. See defect M1.

### Lemma 1.1/1.2 (norm-form reformulation) — SOUND
* `scripts/review_w2_norms.py 2e5`: for all n≤2·10⁵ with 3∤n (resp. 7∤n), "no prime factor ≡2 (3)"
  ⟺ primitive representation by a²+ab+b² (resp. "no r with (r/7)=−1" ⟺ primitive rep. by c²+cd+2d²):
  0 mismatches. `n₇=n₃+1`, 3∤n₃, 7∤n₇ for p≡1 (21): correct.
* Note: Lemma 1.2 is about "both F1-clean", which by POINTWISE_WINDOW Lemma 1.1 is *sufficient* for
  a_min≥11 (the converse is only asserted at q=3). The doc only uses sufficiency; fine.

### External citations (§1) — SOUND
* FI09 (archived txt): Thm 2 is conditional on A(θ) for some θ<1 "sufficiently close to 1"; upper
  bound unconditional; semi-linear sieve with level D<√x (their §6–7). Matches the doc.
* Sedunova (arXiv 2609.28200, archived): abstract — FI09 lower bound conditional; unconditional
  asymptotic for square-free distances; ≤7 prime factors via level x^{1/6} of r(n−2)r(n+2). Matches.
* Nath–Xie (arXiv 2501.16723, archived): Thm 1.1 `#{p=m²+n²+1, Ω(p+2)≤9} ≫ x/(log x)^{3/2}`. Matches.

### Model scope (§3.1, §4 route "Pure Type-I", §5 last paragraph) — GAP (overclaimed scope; see M2)
The model's data are the correlations of the *bad* prime factors only; good primes and primes
< x^ε are lumped into the clean weight `(1−Σt)^{−1/2}`. Real Type-I data at BV level include
`|A_d|` for all d≤x^{1/2} (good and mixed d). A reweighting ν(C)/μ(C) that moves mass between
configurations with different cofactor sizes 1−Σt changes the good-divisor correlations, so the
model fake is **not** shown to be a fake for "all Type-I data". The §2 axioms (d | P₃(z)) are
consistent with the model; the wording in §4 ("any weights, any combinatorics") and §5
("Methods that provably cannot give a_min≥11 …") is not.

### §3.5 LP values (discrete model ε=0.1, K=8) — SOUND; several upgradable to CERTIFIED
`scripts/review_w2_lp.py` (own model build + HiGHS + **exact rational dual-feasibility check**, ρ in
40 digits; a dual y with `Σ_S y_S emb(S,C) ≤ [C=∅]` ∀C proves ν(∅) ≥ y·ρ for every fake):

| case | author (LP) | reviewer primal | reviewer certified lower bound |
|---|---|---|---|
| one window θ=0.5 | 0.744 | 0.74412 | **≥ 0.744128** |
| one window θ=0.6 | 0.828 | — | **≥ 0.827541** |
| two windows θ=0.5 | 0 | 0 | (fake certified, Prop 3.7) |
| two windows θ=0.6 | 0 | 0 | — (primal not certified: the 203-column HiGHS support re-solved at 40 digits has negative entries) |
| two windows θ=0.7 | 0.497 | 0.49695 | **≥ 0.497087** |
| two windows θ=0.8 | 0.728 | 0.72833 | **≥ 0.728369** |

Since visible sets grow with θ, min ν(∅)/τ is nondecreasing in θ. So in this grid the
two-window threshold θ₂ ∈ (0.5, 0.7] is *certified*; (0.6, 0.7] remains EVIDENCE (0.6 fake uncertified).

### §6.3 slice reduction — SOUND (algebra); quantitative step: SOUND-AFTER-REPAIRS (m1)
* Sufficiency algebra checked: for visible S with S₃≠∅, ρ_δ(S)=Σ_Q emb(S₇,Q)·[slice-Q correlation of S₃],
  s₃≤1/2−s₇≤1/2, so (1) kills it; S₃=∅ is (2). Correct.
* `scripts/review_w2_slice.py 0.1 8 0.5` solves the *full* slice-separable LP (conditions (1)+(2), ν≥0):
  **min ν(∅,∅)/τ = 0.430 > 0**, confirming "slice-separable fakes cannot work" on this grid.
  Also confirmed: max one-window total with ν'(∅)=0 is μ_tot−0.74413 (the "m(∅)≤−0.744" step).
* The prose chain "homogeneity … caps Σm(Q) at 0.256·1.256≈0.32" is not derived in the text (the
  1.256 cost bound is unexplained; with ν'(∅)=0 forced I get a minimal slice-total change −1.226).
  Replace it by the direct separable-LP value (0.430), labelled EVIDENCE (or certify its dual).

### Lemma 3.2 (two-block fakes) — SOUND; trivial-range sentence — MINOR (m2)
* Re-derived: for multisets, emb(S,U⊔V)=Σ_{S=S_U⊔S_V} emb(S_U,U)emb(S_V,V) (Vandermonde); mixed
  splits have ΣS ≥ minU+minV > θ; the remaining terms cancel. Parity preserved. Correct.
* The R(θ)≥τ ⇒ fake step is correct (remove c_C≤μ(C), add U,V freely).
* "θ<1/2: U={a,b} with a,b∈(θ,1−θ)": the fake meant is δ=−[∅]+[{a,b}] (not Lemma 3.2, which needs
  V≠∅), and the condition is a,b>θ with **a+b<1**; a,b∈(θ,1−θ) does not imply a+b<1 (θ=0.1,a=b=0.8).

### Lemma 3.6 (product fakes) — SOUND
ρ_{γ₃⊗γ₇}(S)=ρ_{γ₃}(S₃)ρ_{γ₇}(S₇); s₃+s₇≤a+b ⇒ s₃≤a or s₇≤b (S_q=∅ is included in "zero correlations",
so total masses vanish); ν(∅,∅)=0; positivity termwise. Correct.

### §3.3–3.4 block-fake MC — SOUND as EVIDENCE; error bars not valid (m3)
`scripts/review_w2_blockmc.py 1e6 0.02 SEED θ…` (own Poisson-process sampler, brute-force optimal
split over all V, no author rule): R/τ at θ=0.5 = 0.448, 0.449, 0.413 (seeds 7,8,9); θ=0.6: 0.139,
0.145, 0.121; θ=0.55: 0.242; θ=0.7: 0.047. Agrees with the author's ≈0.42–0.45.
But θ=0.4 gives 3.48 / 1.53 / 1.46 across seeds: the weight (1−Σt)^{−1/2} has **infinite second
moment** (∫(1−s)^{−1}ds diverges), so the MC estimator has infinite variance and "R/τ≈0.43±0.05"
is not a statistically valid error bar. Repair: compute R(θ) by quadrature / in the discrete model
(exact), or importance-sample Σt near 1; drop the ±. (Conclusion unaffected: superseded by the LP.)

### §6.1–6.2 caps — numbers SOUND (EVIDENCE); modelling of "switching" — Assessment, see m4
`scripts/review_w2_lp.py 0.1 8 0.5 --cap=C | --swcap=K:α` (own LP, primal only, exact-equality rows):
cap 2 → 0.3735, cap 3 → 0.0779, cap 3.5 → 0 (author 0.373, 0.078, 0). swcap K:α (cap on configs with a
bin value ≥α): 1.001:0.45 → 0.793, 2:0.45 → 0.168, 3:0.45 → 0, 1.001:0.6 → 0.453, 2:0.6 → 0.106,
3:0.6 → 0, 3:0.3 → 0 (author 0.801, 0.173, 0, 0.459, 0.111, 0, 0; the small offsets are the author's
residual-1e-9 bisection vs my exact rows; with K=1 exactly HiGHS falsely reports infeasibility,
although ν=μ is feasible — a numerical artefact on the boundary, not a model issue).

### §4 route (ii) — Assessment SOUND (in the model), and strengthened
The two-window class `CRT(−3,−7) mod d₁d₂` indeed varies with the modulus (BFI/Maynard need fixed a).
But window 3 *alone* has fixed a=−3, so one-window data beyond 1/2 are a priori available. The doc
does not test this mixed-level model. Reviewer test (`--onewin=T₁`: joint level 1/2 plus pure
one-window data (S₃,∅),(∅,S₇) up to T₁): T₁=0.55 → 0, T₁=0.6 → 0 (fake persists; primal uncertified),
T₁=0.7 → **certified ≥0.16298**. So at BFI/Maynard-type levels (≤3/5) the obstruction persists in the
grid — supports "closed" for (ii). Suggest adding this test to §4 (EVIDENCE).

### §5 item 2 / Prop 3.7 last sentence / §0 — MAJOR presentation defect (M3)
W1 (POINTWISE_WINDOW §2.2 Step 4) bounds T₂ by the prime-pair upper sieve S2 applied to
`p=4mr₁r₂−3`, i.e. it **uses primality in a switched variable** — outside 𝒯𝒫(θ) (the doc itself says
so in §4 route (i) and §6.2). So "Parity is sufficient for one window at level 1/2 (Thm W1)" is not a
statement about Type-I+parity. The one-window model positivity is a *separate* fact: grid LP 0.744,
now certified by the reviewer's exact dual (≥0.744128). "In 𝒯𝒫(θ) the one-window threshold is
exactly 1/2" is proved only below 1/2 (fakes) and on one grid at 1/2; the continuum statement at
θ=1/2 is unproved. Repair: separate (a) actual primes: W1 = Type-I + parity + switching;
(b) model: one window positive at θ=1/2 on the grid (CERTIFIED with dual), continuum open.

### Model fidelity: the discrete "true law" has parity-sensitive Type-I data — MAJOR (M4)
`scripts/review_w2_rhocheck.py 0.1 8 0.5`: normalised one-window correlations
`r(S)=ρ_μ(S)/(∏_k w_k^{S_k}/S_k!)/ρ_μ(∅)` of the model's μ (θ=1/2 visible S) range over
[0.82, 1.87]; and the *odd* law (the (p/3)=−1 analogue) has different data (e.g. single point at
bin 0.115: 1.349 even vs 1.081 odd). For actual primes, BV + fundamental lemma give
`r(S)≈1` independent of |S| parity — that is exactly Thm P1. So at ε=0.1 the model's Type-I data
partly *encode* parity, i.e. the model is far from the asymptotic regime it is meant to represent
(Λ=½ln10≈1.15 expected bad points). In the continuum ε→0 the heuristic gives r(S)→1, so this is a
coarse-grid artefact, but it means Prop 3.7 is a statement about a law whose sieve data differ from
real sieve data by up to ~90%. Moreover **every θ=1/2 LP in the doc uses ε=0.1** (K=8, 12); the
(ε,K) grid study was done only at θ≥0.7. Repair: re-run the θ=1/2 two-window LP for smaller ε
(e.g. 0.05, 0.03) and report r(S) spreads; until then Prop 3.7's relevance to sieve methods is
EVIDENCE of the weakest kind, and §4/§5 "blocked" statements must say "at ε=0.1".
*Reviewer attempt at a finer grid* (`scripts/review_w2_lpfast.py`, own lean float LP): ε=0.07, K=9
(439 window configs, 192721 joint, 408 visible): HiGHS returns min 0, but unconstrained with residual
0.34 (support re-solve not positive, cond 3e10) — unusable; with ν/μ≤10³: min 0 at relative residual
3.4e-4 (EVIDENCE that the fake persists at ε=0.07, not certified). r(S) spreads at ε=0.07/K=9:
[0.71,1.76]; at ε=0.05/K=10: [0.82,1.64] — fidelity improves only slowly (bin discretisation
contributes too). So M4 is not resolved by refinement within reach; it must be stated as a caveat.

## Numbered defects

**FATAL:** none.

**M1 (MAJOR, §2 Thm P1, last two sentences "The same holds jointly … three of them have no
both-clean element").** The four classes ((p/3),(p/7)) do *not* have identical joint sieve data:
3 is a window-7 bad prime and `3|n₇` iff (p/3)=−1 (brute force 100% / 0%). So the joint statement as
written is false (the sieve sees `|A_{d₁·3}|`). Repair: state the joint barrier only for the pair
(+,+) vs (+,−) (identical joint data: 3∤n₇ and 5∤n₃n₇ in both; brute force confirms 0 both-clean in
(+,−)), or exclude 3 from the window-7 sifting set and say so. (The one-window P1 is unaffected.)

**M2 (MAJOR, §4 bullet "Pure Type-I sieves … (any weights, any combinatorics)" and §5 last
paragraph "Methods that provably cannot give a_min≥11").** The model only contains bad-prime
divisibility data; real BV-level Type-I data include good and mixed d, which the model fake is not
shown to match (it reweights configurations with different cofactor sizes). Also "provably" refers to
one discrete grid. Repair: say "sieves whose only inputs are |A_{d₁d₂}| for bad squarefree d₁d₂ ≤ x^{1/2},
parity and total mass — in the discrete model ε=0.1, K=8"; drop "any weights"/"provably" or qualify.

**M3 (MAJOR, §5 item 2, §0, Prop 3.7 last sentence).** W1 uses switching (S2 prime-pair sieve in
Step 4), so it is not evidence that Type-I+parity suffices for one window. See verdict above;
repair by separating actual-prime and model statements, and cite the (now certified) one-window dual.

**M4 (MAJOR, model fidelity; §3.5, §3.7, §4, §5).** At ε=0.1 the model's own Type-I data deviate from
product form by up to 87% and depend on |S| parity (so are not parity-blind like the real data of
Thm P1); every θ=1/2 computation uses ε=0.1. Repair: add r(S)-spread diagnostics, run θ=1/2 at
smaller ε (reviewer: ε=0.07 fake persists to residual 3.4e-4, uncertified), and qualify all
"blocked" statements by the grid.

**m1 (MINOR, §6.3).** The "0.256·1.256≈0.32" homogeneity chain is not derived; replace by the
direct separable LP (reviewer: min 0.430 > 0).

**m2 (MINOR, §3.2 trivial range).** Use δ=−[∅]+[{a,b}] with a,b>θ, a+b<1 (not "a,b∈(θ,1−θ)"; not
an instance of Lemma 3.2 since V=∅).

**m3 (MINOR, §3.3).** MC weight has infinite variance; "±0.05" not valid (θ=0.4 swings 1.46–3.48
across seeds). Use quadrature/discrete exact values.

**m4 (MINOR/Assessment, §6.2).** Per-configuration caps ν(C)≤Kμ(C) are *stronger* information than a
switched upper-bound sieve provides (which bounds aggregates over configuration families). So the
needed K for realistic (aggregate) caps is at most as large as 2–3, possibly no K works; the
comparison with the 3.4·HL twin-prime constant is heuristic. State this direction explicitly. Also
the twin-prime constant (Wu 2004: ≈3.3996) was "recalled, not re-checked" — fine as stated.

**m5 (MINOR, §2 P1).** Main term `li(x)/(2φ(280)φ(d))` is wrong for 5|d (then |A^±_d|=0 since
p≡1 (5) ⇒ 5∤n₃); harmless (same for both classes) but say g(5)=0 as in W1. P1's label: the
"parity necessary" half is unconditional (BV); only the A⁺ lower bound inherits W1's "modulo S1–S3".

**m6 (MINOR, §0/§3.5).** Several EVIDENCE numbers can be upgraded: one-window θ=0.5 (≥0.744128) and
θ=0.6 (≥0.827541), two-window θ=0.7 (≥0.497087), 0.8 (≥0.728369) are certified lower bounds by exact
rational dual feasibility (`scripts/review_w2_lp.py`); hence θ₂∈(0.5,0.7] is CERTIFIED on the grid.

**m7 (MINOR, §4 route (ii)).** Add the mixed-level test (one-window data to T₁ with joint data at
1/2): fake persists for T₁≤0.6, positivity at T₁=0.7 (certified ≥0.163). Supports "closed".

*M1 repair check* (`scripts/review_w2_p1joint.py 3e6`): joint counts |A_{d₁,d₂}| for
d₁|d₂ ∈ {1|1, 1|3, 11|1, 1|5, 1|13, 11|13, 17|3, 23|17, 1|19, 29|31}: (+,+) 3309, 0, 331, 0, 268, 22, 0, 8,
185, 7 vs (+,−) 3417, 0, 348, 0, 275, 37, 0, 11, 179, 2 — same pattern (zeros at 3|d₂, 5|d₂), noise-level
differences; (−,±) have |A_{1,3}|=N. So the repaired joint statement ((+,+) vs (+,−)) holds.
