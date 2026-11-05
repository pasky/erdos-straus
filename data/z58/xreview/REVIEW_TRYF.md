# Z58 TRYF — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** Bank the prime-modulus Theorem 2.1 and the exact weighted identity, not the claimed reciprocity frontier or method-exclusion conclusions. NO PROOF / NOT A HOT LEAD is justified; ES remains OPEN.
Reviewed `side-agent/z58-tryf` at `239c29db21b39d94c6a895385deedd70a639e48a` (`Z58_TRYF.md`). No target files changed.

## Per-claim audit

| Claim | Classification | Independent finding / required qualification |
|---|---|---|
| Lemma 1.1, including automatic bound | CORRECT | The bijection is exact for every integer n ≥ 1; positive divisors are understood. All four formulations and the C-factorisation work. Entirely prior, below. |
| Lemma 1.2, including non-unit squares | CORRECT | The 2-part and odd-part reciprocity signs both give (k/d)=1. A non-unit square cannot hit because every k is a unit. Entirely prior. |
| Theorem 2.1, prime p ≡ 1 (4) | CORRECT | Conductor p, all shifted intervals, the four-region split, coefficient 1/64 and Q lower bound survive; details below. This bounds only the singled-out Jacobi layer, not L_r or actual hits. |
| §2 “conditioned expectation” | CORRECT-WITH-FIX | Interpret M−S as a **weighted** unit-residue expectation for R̃. The unweighted hit probability conditional on Jacobi −1 is 2τ/φ(d), not 2τ/d at composite d. |
| §2 GRH remark | GAP | The argument needs cancellation in **arbitrarily shifted** intervals of length p^ε′, not just initial sums. No such GRH consequence is supplied. Replace GRH by an explicit uniform-short-interval hypothesis or remove the remark. |
| Lemma 3.1 and four-layer decomposition | CORRECT | Orthogonality yields exactly φ(d)/d times the hit indicator. For p ≡ 1 (4), d ≤ X_p, all d are prime to p, including composite d; principal and Jacobi characters are distinct. |
| All-real-character description / flip | CORRECT-WITH-FIX | χ_e on units, e squarefree dividing d, flips algebraically to (−1/e)(e/p); τ_χ_i is nonnegative by its Euler factors. For nonsquarefree d retain e ≠ 1, core(d), not merely e,i>1: d=27 has no “other real” character. No analytic bound for the resulting weights is proved. |
| §0 prime-d overview | GAP | This is not §2: Burgess on free C does not preserve “4kC−1 prime”, and the prime-d principal sum is not the all-d log² main term. Replace the overview with §3's weighted all-d formulation. |
| §3 “at most six flippable characters / all others have no reciprocity law” | WRONG | p=241 ≡1 (24), d=11 ≡3 (4) have gcd(p−1,d−1)=10: orders 5 and 10 are not excluded by p ≡1 (24). Higher power reciprocity exists; no simple rational conductor-p flip has been established here. The proposed classification does not follow. |
| HCE and Theorem 3.2 | CORRECT conditional implication | Algebraically HCE is R̃ ≥ δ(M−S), hence a uniform weighted Ω(log²p) lower bound. This is stronger than mere eventual positivity, not an equivalent weaker reduction. The memo's “plus a quantitative margin” caveat is essential. |
| §4 census and layer numbers | CORRECT as finite evidence | Reproduced below. L_n in the production program is a residual, not an independent verification; an independent small-modulus character check also passes. |
| “Any proof must use u,B,C all unbounded”; “nothing short of controlling the full spectrum”; local-factor attribution of empirical mean | GAP / Assessment only | Finite threshold counterexamples do not refute every fixed bound eventually. The identity forces an inequality, not a particular proof technique. A mean of −3.18 does not identify which characters caused it. |

## Proof re-derivation and external input

1. A hit has u=(−p mod d), C=(d+1)/(4u), B=(p+u)/d; conversely 4uBC−u−B=p gives d=4uC−1 and the same u<d. Then d≤p+u≤p+(d+1)/4, hence 3d≤4p+1. The divisor condition on p+u is immediate; (4uC−1)(4BC−1)=4Cp+1 proves the other equivalence.
2. Write k=2^a k′. If a>0 then d≡−1 (8), so (2/d)=1. For odd k′, d≡−1 (k′) and d≡3 (4) give (k′/d)=(−1/k′)²=1. Multiplication by (−1/d)=−1 proves the hit obstruction, including the separate non-unit case.
3. Burgess source checked directly: D. R. Heath-Brown, *Burgess's Bounds for Character Sums*, introduction, equation (1), https://arxiv.org/html/1203.5219v2. It states H^(1−1/r)q^((r+1)/(4r²)+η), uniformly in the interval start, for cube-free q and arbitrary integer r≥2. Here q=p is prime and χ_p primitive/nonprincipal; the selected r>9 is allowed. No averaging over p or moduli is being smuggled in.
4. Put a=1/4+ε, K=⌈p^a⌉. The small-small rectangle contributes at most (1/4)H_K²+O(1)=(1+4ε)²log²p/64+O_ε(log p), even after truncation by 4kC≤X+1.
5. Outside it, fix the shorter/specified coordinate k. In regions II and IV, k<p for large p uniformly for X≤2p, so χ_p(4kC−1)=χ_p(4k)χ_p(C−(4k)^−1). Partial summation on dyadic C-blocks above K gives ≪_ε k^−1 p^(1/(4r²)−ε/r+η). Truncated blocks use the same supremum bound; shifts may be reduced modulo p.
6. With r=⌈1/ε⌉+1, η=ε/(4r), this exponent is ≤−ε/(4r). The geometric-block factor depends on r only. Summing 1/k in II/IV, and swapping coordinates for III, costs O(log p); all three contributions are O_ε(p^−δ log p), uniformly in X. The constants are ε-dependent and effective, **not numerically evaluated**; no specific “astronomical” threshold is certified.
7. M(X_p)=(1/8)log²p+O(log p). No d≡3 (4), d≤2p is divisible by p≡1 (4), so Q=(M−S)/2 exactly, without zero-symbol corrections. Its coefficient is (7−8ε−16ε²)/128, strictly larger than 7/128−ε. Fixing arbitrarily small ε gives limsup |S|/M≤1/8 and M−S≥(7/8−o(1))M. For C even set C=2j: the leading small-box and M coefficients halve; the affine slope is 8k. This is a valid adaptation, not exact halving at finite X.
8. Orthogonality: Σ_χ χ(−p)χ̄(k)=φ(d)1[p≡−k (d)]. Divisor residues are distinct and units. The Jacobi coefficient equals τ by step 2. Splitting the remaining characters into real/non-real proves the identity with no omitted term. For a real character, τ_χ(m)=∏_{q^b∥m}(1+χ(q)+⋯+χ(q)^b)≥0; reciprocity supplies its sign but no cancellation estimate. HCE then gives R̃≥δ(M−S)>0 directly.

## Mandatory falsifiers

| Screen | Correct behaviour; audit of memo's entry |
|---|---|
| F1: odd squares | PASS. For gcd(d,m)=1 the principal/Jacobi layers cancel termwise; non-units cannot hit. Nonprincipal χ_p is the prime theorem's identifiable square-sensitive input. No positivity theorem for squares is claimed. |
| F2: 12 R₈-zeros near 10¹⁰ | Counts verified, but **fix the quantifier**: the pointwise HCE inequality fails at these zeros whenever its base mass is positive; finitely many zeros do not refute an “all sufficiently large primes” hypothesis. Only **6/12** listed p are 1 mod 24, the HCE domain. C-even M has half the leading coefficient, not exactly half its value. Positivity of M₈−S₈ at these heights is not supplied by the asymptotic theorem. Zeros force the total remainder L_r,8+L_n,8 to cancel that base, not necessarily L_n,8 alone. |
| F3: 285 nonsquare composite zeros | Counts verified. The memo's composite “verbatim” extension is unproved: the Jacobi character modulo n is imprimitive when n has square factors; removing extra zero factors and handling noninvertible slopes requires work. More immediately, restrict every layer sum to gcd(d,n)=1: for the screen zero n=57,d=3, every character value at n is zero, whereas the displayed unrestricted M incorrectly contributes 1/3. HCE is stated only for primes, so these n do not falsify it. |
| F4: 14 (★)-zeros **and 38 𝔊*-zeros** | The 14 counts/layer cancellations agree. The memo **omits the 38 𝔊*-zeros entirely**. These are not all full-family zeros: at 564661441, R=2 but R_𝔊*=0. Add this distinction; full-family Theorem 2.1 makes no restricted-𝔊* remainder claim. An eventual restricted-family hypothesis is again not disproved by finitely many zeros. |

The empirical “2.6 standard deviations” is a reading of a 329-prime sample near 10⁶, not a validated description of all composite zeros, all 14 prime zeros, or different subfamilies/heights.

## Recomputations and reproducibility

All shell calls used `ulimit -v 4000000` and timeout ≤1800 seconds; working inputs/binaries/output are under `/tmp/xrev_TRYF/`, not committed.
- Archived the pinned branch's scripts/data. Compiled `z58_tryf_stats.c`; reran N=200000000: output byte-for-byte equal to `stats_2e8.txt` (350410 data rows). All §4.2 decade entries agree; no Mordell R counter reaches the saturation value 255. The 84 nonsquare composite zeros n≡1 (24), last 162267625, and all 14 prime zeros agree.
- Compiled `z58_tryf_layers.c`; reran all 14 exceptional + 9 sample + 329 distribution inputs: all three files byte-for-byte equal. Distribution: L₀=24.4419; L₂=−1.0955 (sd .4680), L_r=−1.5499 (.5238), L_n=−3.1831 (7.2564), range [−19.7841,21.9251]; R mean 22.5289, minimum 2.
- Reran `z58_screens_rstar.c 9000000`: exactly the 14 supplied prime zeros and, after the ≤8e6 cutoff, exactly the 285 supplied nonsquare composites. Reran `z57_synth_dec8.c` at each of the 12 listed inputs: every R and R₈ count agrees (not a new exhaustive interval search).
- Reran `z56_famdesign_decide.c` at the 34 listed 𝔊*-zeros ≥1000; directly enumerated the four smaller ones. All 38 restricted counts are zero; its largest input has one unordered hit, hence R=2.
- New `scripts/z58_xrev_tryf_audit.py` streams/reconciles these outputs and independently enumerates **all** characters modulo d≤255 via cyclic prime-power unit groups for p∈{5,13,73,241,409,5569}, excluding non-units: 365 checks pass. L_n is summed directly, not obtained by subtraction. The all-real sum independently matches the local-square projector. Odd-square direct checks through 101² also pass.
- Audit command: `ulimit -v 4000000; timeout 300 uv run scripts/z58_xrev_tryf_audit.py /tmp/xrev_TRYF`. `layers_*_rerun.txt`, `stats_rerun.txt`, `screens_rerun.txt`, `r8_rerun.txt`, and `gstar_rerun.txt` are the named reruns; legacy deciders' archived copies are `dec8.c` and `decide.c`.

## Novelty against the repo

`git grep` and direct comparison establish the following prior work; “unprimed” does not confer novelty.
- **Z56_FAMTRY §1, Lemmas 1.1–1.4:** all hit/divisor/C-factorisations, the automatic d bound, the identical Jacobi argument and square obstruction. Its §1 already gives τ((d+1)/4)/d and the (1/8)log² heuristic. TRYF Lemmas 1.1–1.2 are rediscoveries.
- **Z57_SYNTH Lemma A.1:** exactly H_d, the bijection, the bound and unit/Jacobi statement, already credited there to FAMTRY. Its §2.1 supplies the C-even counterexamples; TRYF does not discover those screens.
- **Z53_GENUSX §1, Lemmas 1–2 and H⁻_𝔉:** exact real/non-real splitting, the reciprocity-flipped quadratic component and square cancellation, and a remainder ≥−(1−ε)main hypothesis already occur on a different subfamily. Its Theorem X uses prime-conductor Burgess and shifted-interval factorisation for density layers. TRYF's decomposition is a useful full-d weighted presentation, not a new genus/remainder strategy; HCE adds no weaker target.
- **Potential incremental contribution:** the particularly simple full-d estimate |S_p(X)|≤(1/64+o(1))log²p uniformly for X≤2p, its 7/8 weighted-base consequence, and this full-d census/layer dataset. I found no exact prior duplicate of that bound in the requested memos/repo grep; this is not a literature-novelty certification.

## Required fixes, in priority order

1. Remove the false ≤6/no-reciprocity classification; replace the prime-d overview with the actual all-d weighted identity. Separate algebraic flips from analytic control; only L₂ is controlled here.
2. Repair F2/F3 quantifiers and domain/coprimality issues; add the missing 38-zero 𝔊* entry. Do not assert finite zeros disprove eventual HCE, or that the prime Burgess proof transfers unchanged to composites.
3. State HCE explicitly as the stronger weighted Ω(log²p) target, not a reduction. Remove the unsupported GRH shifted-interval upgrade and numerical threshold assertion; clarify the weighted expectation and nonsquarefree real-character exclusions.
4. Credit the exact prior lemmas/decomposition strategy. Downgrade the bounded-parameter/full-spectrum no-gos and local-factor attribution to scoped observations. Correct §4.1's “none in [8813281,2e8]” to **(8813281,2e8]**.

After these fixes: a valid incremental quadratic-layer lemma plus reproducible diagnostics, not an advance on the missing pointwise remainder estimate or a proof of (★)/ES.
