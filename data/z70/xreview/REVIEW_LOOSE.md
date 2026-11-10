# z70 LOOSE — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES. ES remains OPEN.** Reviewed `side-agent/z70-loose` at `e6fc78c8a89b92c8977b0f88dfed372cd30e8cb5`.
The decisive mathematics survives independent re-derivation. The empirical negatives do not close the underlying ideas.
No provider/auth/quota error occurred. All computations used `ulimit -v 6000000`, timeouts ≤1800 seconds, and ≤2 compute processes.

## Per-claim audit
| Claim | Classification | Independent finding |
|---|---|---|
| Theorem F on ℍ and slit-plane continuation | CORRECT | Mellin residues, Hurwitz phases, kernel signs and lower indentation agree; independent 35-digit checks below pass for both fibres. |
| K6a was met by the lane | CORRECT-WITH-FIX | Five d=3 points at **20**, not 30, digits did not meet the registered arithmetic requirement. This review supplies five at 35 digits; do not retroactively describe the lane run as compliant. |
| S₁,S₂ ∉ M₁ for d=1; fibre mock status | CORRECT, scoped | Odd coefficients of S₁ are ±2τ(n), and S₂ has the opposite odd coefficients. Filtering n≡3 (4) produces a y⁻¹log(1/y) singularity, incompatible with a holomorphic weight-1 modular form's O(y⁻¹) cusp bound. This does NOT identify every possible shadow. |
| Lemma K | CORRECT | Class counts, perturbation squeeze and sectorial Abelian step work. Exact cyclotomic reduction verifies the local character sum for every c≤121 and all coprime numerators, independently of lane code. |
| Single-fibre κ_d contrast | CORRECT | Summing the β residue class leaves 4dα≡1 (c), hence κ_d=c⁻¹e(−a₀·inverse(4d)/c) when gcd(c,4d)=1, and zero otherwise. This is compatibility with a fibre law, not positivity. |
| Theorem LS | CORRECT | A finite-index subgroup contains Uʲ; choose positive r with jr+1 divisible by ℓ². κ(r)=1, κ(Uʲr)=0, contradicting the stated small-cocycle condition for every real weight. |
| Corollary LS-M, cuspidal shadow | CORRECT | The uniform O(y⁻ᵏᐟ²+log(1/y)+1) nonholomorphic-part bound for k<2 is o(y⁻¹); for k≥2 the cuspidal shadow vanishes. Principal parts in the holomorphic part do not invalidate this argument. |
| LS-M, noncuspidal extension | CORRECT-WITH-FIX | Holomorphic **at every cusp** shadows give O(y⁻¹+abs(Yₖ(y))) for k≤2, hence the required little-o bound. Replace the memory citation with the checked source and zero-mode derivation below; refine the “not covered” wording. |
| I5: seven maps + 400 expressions | CORRECT, bounded | Independent word enumeration and finite-orbit matrix matching reproduce 23/39 words, 8/8 certificates, all seven failures, and the grammar split 246 involutions /154 non-involutions; no survivor. |
| I5 registration substitutions | CORRECT-WITH-FIX | Precise replacement list is committed before results (`fc375a95e`); grammar before results (`b1e8463e4`). This is disclosed prospective amendment, NOT execution or refutation of the original coset/continuant proposals. |
| Lemma P5 | CORRECT | Three divisor families have only one overlap; swap is free off them for prime p≡1 (4). The certificate condition is exactly existence of a prime divisor 3 mod 4 in p+1. Independently: 383 primes <6000, 54 without a trivial certificate. |
| Lemma S and Lemma T10 use | CORRECT | e divides 4a²d+1 because e divides a+b; f=4acd−p and a≤b imply f≤p+2 and a≤(p+1)/(2d). T10 follows from (−d/f)=1, f≡3 (4), and reciprocity; the Jacobi version really does exclude squares. |
| #10 coverage and forcing-rule kill | CORRECT; stronger than stated | Full 10⁸ rerun reproduces all four coverage numerators. All four rules also have exact untruncated counterexamples, not only NP: see below. No conclusion about other rules or all finite menus. |
| Pell 2-adic lemma/recalibration | CORRECT | U odd, T divisible by 4; Sᵥ is the liftable projection with size 2ᵛ⁻¹. Independently checked 160 local probabilities, 36 lifted sets through v=6, four review fixtures and 594 observed D events at 30 primes. |
| Pell non-rejection | CORRECT-WITH-FIX | Aggregates reproduce, but 60.3%/59.6%/64.8% of train/test/control decoys equal the real letter. Disclose this loss of contrast and remove the unsupported assertion that odd-prime null bias leaves the contrast “unaffected.” |
| I9 under-filled design/results | CORRECT, bounded | Independent aggregation reproduces retained strata, disjoint controls, all intervals and registered McNemar counts. Noprime CI is (−0.101226,+0.058102): equivalence fails. Plug-in variance assigns zero uncertainty to singleton strata; these are model-based intervals, not certified effect bounds. |

## Mathematical checks behind the verdict
1. **F:** shifting Γ(s)(2πM²y)⁻ˢζ(s,a)ζ(s,b) crosses only the double pole at 1 and the pole at 0; their residues give E exactly.
   With s=1−u, the Hurwitz factors give πcot(πu)∓πi and π/sin(πu). Their inverse kernels are `1/Y−exp(−Y)Ei(Y)` and `exp(Y)E₁(Y)−1/Y`.
   The lower contour has integral PV+πi·Res; substituting PV=integral−πi·Res combines the two exponential terms into L*ₐ,ᵦ/(M²z), with the stated sign.
   Nonintegral a,b make the twisted Dirichlet series entire, so L* is bounded in sectors at zero; decay at infinity and contour rotation give the stated continuation. No boundary jump theorem follows automatically.
2. **K:** a fixed triple class has xlog²x/(8c³)+O(xlog x) points for 4abd≤x. Bounded coordinates contribute only O_K(xlog x); the remaining perturbation is multiplicatively 1+O(1/K).
   Sectorial partial summation preserves the leading coefficient. Summing d first imposes c∣4αβ. Ramanujan sums give −1 at odd primes, 0 at their higher powers, and 0 at every positive power of 2.
   The numerator-independence substitution scales **both** α and β by a₀⁻¹; the constraint is unchanged. This proves κ=1[c odd]μ(c)/c², not merely a numerical fit.
3. **LS scope:** γz−γr=(z−r)/((cz+d)(cr+d)) stays in a fixed upper sector at a non-pole rational; therefore Lemma K applies to the transformed approach, not just a vertical one.
   A finite-image vector representation reduces to the scalar case on its finite-index kernel, provided the same cocycle bound holds. Infinite-image systems and growing/infinite-level constructions are not ruled out.
4. **Shadow source:** checked Bruinier–Funke, *On two geometric theta lifts*, §3, (3.2), Lemma 3.1 and Proposition 3.2: https://arxiv.org/pdf/math/0212286 .
   The source explicitly assumes half-integral k≠1; do not cite it alone for arbitrary real k or k=1. The Fourier-mode ODE works for real k; directly ξₖ(y¹⁻ᵏ)=1−k and ξ₁(log y)=1, supplying the missing zero mode.
   Subtract the shadow's constant term in the Eichler integral. For k<2, ∫ᵧ¹tᵏ⁻²(t+y)⁻ᵏdt=O(y⁻¹); k=2 has only a constant shadow; k>2 has none. Thus the holomorphic-at-cusps extension is valid with this explanation.
   “Exponential-growth harmonic forms/principal parts” is too broad an escape hatch: holomorphic principal parts with cuspidal or holomorphic-at-cusps shadow are already excluded. Shadows with actual cusp poles remain outside this proof.

## Independent numerical record
`z70_xrev_loose_mp.py` uses 35-digit mpmath, a different contour angle, and a two-strip Lambert summation with an explicit <10⁻⁴² omitted-tail bound; a 64-term small-τ asymptotic handles the endpoint (numerical, not interval certification).
Here z=z₀·1.6/(M−1)². Each entry is relative error versus the directly summed original fibre.
| z₀ | d=1, M=4 | d=3, M=12 |
|---|---:|---:|
| 0.5i | 9.12·10⁻³⁶ | 2.98·10⁻³⁶ |
| 0.3+0.4i | 5.10·10⁻³⁴ | 1.20·10⁻³⁵ |
| −0.2+0.5i | 1.16·10⁻²⁷ | 4.83·10⁻³⁵ |
| 1+0.3i | 2.85·10⁻³⁶ | 4.81·10⁻³⁷ |
| 0.13+0.08i | 3.80·10⁻³⁵ | 3.16·10⁻³⁶ |
Halving the endpoint switch (0.00025→0.000125) leaves the worst d=1 point and smallest-height d=3 point unchanged at the reported errors. K6a now passes independently for both fibres.
Full #10 rerun: NP 700996/719781=0.97390; Q3 653511/719781=0.90793; CF 559272/719781=0.77700 (846 undefined); GA 146/23993=0.00609 (subsample).
The one-pass random decoys differ from the lane's two restarted runs; coverage agrees exactly. All three screen-list reruns (14,38,12) are byte-identical to stored output.
The six reported NP-empty slices and six second-NP recoveries reproduce. Independent exact enumeration additionally establishes:
- At p=102001, NP=Q3=CF=23 and the full slice is empty (amax=2217). Thus these **three** selection rules fail untruncated.
- At p=409=3²+20², Gaussian candidates 3,5,23,17 are residues; the rule selects d=43. Its full slice is empty (amax=4). Thus GA fails untruncated too.
- Fixture (p,a,d)=(1033,1,132): f=e=23, b=45, c=2; 4abd=pe+1 and ce=a+b exactly.
Pell cluster z (real-null / decoy-null / adjusted contrast): train −0.365/+0.015/−0.828; test −0.281/+0.277/−1.277; controls −2.247/−3.019/+1.641. Raw contrast z is −1.24/−1.81/+0.85: still no registered signal.
I9 registered noprime controls: 889 pairs, discordances 23/20. Same-subset rerun: 1233 pairs, nearest/two-sided z=+0.09/+0.84; excluded 428 have Y(q)=0.4159 vs 0.1706. Confounding diagnosis reproduces, not a proof of zero effect.
Secondary NP-menu census to 10⁷ and odd-q χ² diagnostics were inspected, not fully regenerated; neither is needed for this verdict. The singular-fit illustration is not used as proof of K.

## Decisive versus bounded / false-negative register
| Item | Decisively closed | Still live; concrete next test |
|---|---|---|
| I6 | Fixed finite-index small-cocycle laws for this G; cuspidal/holomorphic-at-cusps shadows | Fibre mock completion is **not killed**. Specify its completion and shadow, derive the period including the crossed residue, then test that law; infinite-level and infinite-image constructions need separate hypotheses. |
| I5 | These 407 expressions fail on complete T₇₃/T₄₀₉ | **One grammar only.** Implement a precise continuant expansion/recontraction transport, or the original norm-minimised coset proposal, with deterministic domain/ties; retest both complete word sets. |
| #10 | All four named selection rules, now with exact counterexamples | Other p-dependent rules and larger menus remain live. Test first-four-NP menus with the exact decider on prior NP₃ failures, not A=2000; no general covering theorem is disproved. |
| Pell | No registered D-union signal in these samples/relations | **One statistic/null implementation.** Rerun on distinct decoys with small-prime/unit-residue conditioning; report effective paired sample and cluster uncertainty. A shared p does not make different letter moduli exchangeable. |
| I9 | This q·m, m≤64 builder is not universal; no detected eligible-sample excess | **One builder/design.** Enumerate scarce control windows, use interval/randomisation inference valid for singleton strata, and preregister a q,Y-dependent builder plus explicit small-q controls. |

## Falsifier audit
| Screen | Finding |
|---|---|
| F1 odd squares | Fibre zero coefficients and T10's Jacobi obstruction are genuine; square T₉ has 11 words and no certificates. Pell uses witness-conditioned samples, not a square positivity test. I9's primitive square representation forces the relevant symbols +1. |
| F2 C-even / 12 R₈ zeros | Even-d fibres obey F; there is no positivity consequence. Reproduced Type-I counts NP/Q3/CF/GA=12/12/9/0; Type I is not R₈ positivity. I9 uses only four Mordell-class members. |
| F3 285 non-square composite zeros | No full screen was run and none may be claimed. 105 belongs to this screen: independently 11 words, no certificates. Final table's “105 control as F1” is a category error; move it explicitly to F3. |
| F4 14 (★)- /38 𝔊*-zero primes | Coverage reruns agree; 102001 is an exact three-rule obstruction. 409 is a (★)-zero; 73 is a parity fixture, not a (★)-zero. Witness-set statistics do not imply positivity on these screens. |
No “survives all four” or HOT LEAD claim is justified; the memo correctly makes neither.

## Required fixes (priority order)
1. Record K6a's original d=3 precision deviation as a failed procedural requirement, now repaired by this independent 35-digit grid; delete “criterion met” for the 20-digit run.
2. Disclose Pell self-decoy counts 17043/28272, 15896/26664, 65877/101620; remove “contrast … unaffected,” and retain non-rejection rather than equivalence or a general Pell kill.
3. Replace the LS-M memory citation with the checked source plus real-weight/weight-1 zero-mode argument; distinguish cusp-polar shadows from merely exponential holomorphic principal parts.
4. Replace “seven registered maps” with “seven amended/pre-run-specified expressions”; preserve the original coset/continuant proposals as untested. Correct 105's F3 classification.
5. Tighten #10 using the exact counterexamples above; retain I9's under-filled-stratum/model qualification and explicit failure of the two-sided equivalence criterion in any exported summary.
Reproduction scripts committed with this review: `scripts/z70_xrev_loose_{mp,audit,pell}.py`; pass the extracted lane tree to audit/pell, and M, Re(z₀), Im(z₀) to mp. Use uv with mpmath/sympy/numpy respectively. No lane files were modified.
