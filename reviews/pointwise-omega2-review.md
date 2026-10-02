# Hostile review of POINTWISE_OMEGA2.md (branch `side-agent/omega-hub` @ 3f43543)

Reviewer: side agent (review-omega2). Scope: POINTWISE_OMEGA2.md,
reviews/agent-reports/AGENT_REPORT_O2.md, scripts/omega2_*.py as of 3f43543.
Context used: POINTWISE_OMEGA.md (PO) §1, Thm 4.1, §6.2 (H_MIN, Thm 6.2),
§9 (Lemma 9.1/9.2 setting); paper/es-omega-note.tex (definition of W, 𝓡).

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects are numbered
D1, D2, … with severity FATAL / MAJOR / MINOR / COSMETIC.

## Per-item verdicts

(filled in item by item below)

### Item 1 — Lemma 1.1 (closed form of support-truncated B_L): **SOUND**

Re-derived. `Σ_{F⊆A, supp F⊆U}(−1)^{|F|} = I(U)` (alternating sum over the
subsets of `{E∈A: supp E⊆U}`, empty F included); Möbius on the Boolean
lattice; every `supp F⊆V`; swapping sums gives
`Σ_{W⊆V, I(W)=1, |W|≤L} Σ_{j=0}^{L−|W|}(−1)^j binom(N−|W|,j)`, and the
partial alternating row sum is `(−1)^k binom(n−1,k)` for `n≥1`. `I(V)=1` iff
`A=∅`, so for `A≠∅` only `W⊊V` occur, `N−|W|−1≥0`, and for `N≤L` every
binomial vanishes. No gap.

Independent brute force (reviewer code, written without reading the
author's script): `reviews/omega2-review-scripts/bf_lemma12.py`. Events are
arbitrary subsets of `∏_{supp}Ω_ℓ` (supports 1–3, `|Ω_ℓ|≤3`, up to 5
primes, up to 9 events), all outcomes, all `0≤L≤|𝒫|+1`; `B_L` computed by
enumerating `F⊆A(x)`. Closed form = definition in 102 277 cases (seeds
11, 12, 13), 0 failures. Mutation check (sign `(−1)^w` instead of
`(−1)^{L−w}`): 213 failures in 4 412 cases, so the test has teeth.

### Item 2 — Lemma 1.2 (pointwise minorant): **SOUND**

Re-derived: `|R_L| ≤ Σ_w binom(N,w)binom(N,L−w)=binom(2N,L)` (Vandermonde);
`f(N+1)/f(N)=2(2N+1)(N−L)/((2N+2−L)(2N+1−L))`, and with `N=L+t` the
difference denominator − numerator is `L²+3L+4t+2` (checked by hand);
`f(L+1)=binom(2L+2,L)≤4^{L+1}`; `binom(N,L+1)=e_{L+1}(1_V)≤e_{L+1}(a)` by
monotonicity. Both inequalities hold in all 102 277 brute-force cases
(same script). Observed `max |B_L|/(4^{L+1}e_{L+1}(a)) = 1/4` over cases with
`A≠∅, N≥L+1`: the constant is lossy by a factor ≥4 in practice, which is
harmless.

### Item 3 — Lemma 1.3 (mean, mass, twist reduce to `E∏(1+za)`): **SOUND**

(1) termwise `e_{L+1}(a)≤z^{−(L+1)}∏(1+za_ℓ)`; with `z=16`,
`2·4^{L+1}·16^{−(L+1)} = 2·4^{−(L+1)}`. Correct.
(2) Grouping by `U=supp F`: on a cell c of the U-coordinates the
coefficient is `κ(U,c)=Σ_{F⊆A_U(c), supp F=U}(−1)^{|F|}`; Möbius gives
`|κ|≤2^{|U|}`; κ vanishes unless every `ℓ∈U` is covered by an occurring
event (trivially, since `supp F=U` forces this). Hence
`M_1(B_L)≤Σ_U 2^{|U|}E∏_{ℓ∈U}a_ℓ=E∏(1+2a_ℓ)`. Non-unit cells get κ=0
(no event occurs at a non-unit coordinate), so the expansion is into unit
classes as PO Thm 4.1 requires (`gcd(b_i,d_i)=1`). The `G_{L+1}` expansion
has nonnegative coefficients (products of event indicators are indicators
of intersections of unit classes), so mass = mean. The brute force also
computes the exact merged cell expansion of `B_L` and checks
`M_1(B_L) ≤ E∏(1+2a_ℓ)` for every L: 0 failures.

PO Thm 4.1's `M_1=Σ|c_i|/φ(d_i)` is representation-dependent; using the
merged-cell representations of `B_L` and `G_{L+1}` separately and the
triangle inequality is legitimate. No defect.
