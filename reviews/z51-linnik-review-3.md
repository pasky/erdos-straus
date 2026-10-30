# Hostile referee report, round 3: EXSET_LINNIK

Reviewed 2026-10-30. Final reviewed checkout: `db8dc3a499b93993c59947b70d351f0157b9e612`.
`EXSET_LINNIK.md` SHA-256: `8e047a5ada354d6b6600b1edf9a346afe80f978bed16211bf4a0f5ffcb4d167f`.
`EXCEPTIONAL_LARGESIEVE.md` SHA-256: `e5fc44657b7a4ac636a5aaeea8f5eb0997b417ec461117f0e319f39f8e060ea4`.

Scope: item-by-item verification of the round-2 repairs, especially §§4–6, Theorem 2.10, and §§0/7/8. The final checkout includes the additional bottom-line and Gallagher-constant wording fixes. Unchanged results marked SOUND in round 2 are carried forward, not reopened. The KARY/KARY2/Shiu cap machinery is accepted with its previously stated provisos; this report checks its application, not that machinery anew. ES remains OPEN.

**Overall: MAJOR revision, concentrated in §8 item 5 and summary scope. No remaining FATAL claim identified in the repaired propositions.** Both round-2 FATAL claims are repaired: the general p-dependence blocking lemma is withdrawn, and (WL) now has the correct prime population and scale quantifiers. Proposition 6.1's main assembly/citation repairs work. The fibre-hybrid paragraph is still not a valid sufficient criterion for an exceptional-set estimate as written: its integer domination assertion overlooks zero Jacobi symbols, and its claimed “iff” omits finite-interval counting control.

Grades: **FATAL** = false central theorem/scope or unusable hypothesis; **MAJOR** = substantive missing hypothesis, argument, or scope restriction; **MINOR** = local correction not affecting the principal result; **SOUND** = valid in the stated/inherited scope. An Assessment label does not make an incorrect elementary implication correct.

## 1. Round-2 issues in the earlier core

### 1.1 Lemma 1.2, (1.1), Proposition 2.2, Lemmas 2.3–2.4, Theorem 2.5, Corollary 2.6 — SOUND, carried forward

The round-2 SOUND proofs are unchanged in substance. I do not reopen the coset/Kummer argument, the correct `h+2` inequality, the coprimality selection, the `4^{ω(h)}` per-cell union bound, or the infinite-range Dirichlet conclusion. The “not periodic at all” sentence has been replaced by the intended distinction from ordinary Dirichlet-character tests in the prime variable. Read it in Proposition 2.2's fixed-order, squarefree-support scope, not as denying constant/degenerate tests.

The additional change to (L5) is **SOUND**: with `m=|𝒜|≥3ν` and `H=Σ_{p∈E}log p`, either `H≤ν log N`, or Gallagher gives

`H ≤ ν(m−1)/(m−ν) · log N < (3/2)ν log N`.

Since `H≥#E·log(X/2)`, the new bound with constant 2 is safe.

### 1.2 Remark 2.7 — SOUND repair

The choice `0<ε<min(1/8,1/2−1/A)` restores the inherited domain of `η₀(ε)` while preserving the positive support exponent and power-saving range. No new loss is hidden here.

### 1.3 Proposition 2.8 — SOUND repair

The invocation now explicitly uses `λ=max(λ₀,λ(L))`. The substantive proof remains the round-2 SOUND additive-Haar, whole-period argument. Its open per-summand-only complement is still stated. Nothing here proves the proposed §8 fibre hybrid impossible.

### 1.4 Conjecture 2.9 and numerical descriptions — SOUND repair; MINOR omission retained

The table now says that the 28% avoid the **checked** singleton/pair/triple boxes; it no longer certifies all-modulus sterility from this experiment. Higher boxes and the local-lemma mechanism remain conjectural. The Poisson wording is inside the evidence/heuristic discussion, not a theorem.

The round-2 small-prime bookkeeping request is still absent: “all polylog-smooth squarefree data” includes fixed small primes excluded by `Π≥11`. This is repairable by grouping `n=n₀n₁`, where `n₀` uses the finitely many excluded primes, and applying Cauchy–Schwarz to their coefficients. The cost is a fixed factor `2^{#small primes}`, absorbed by `X^{o(1)}`. Add that sentence; no new conjecture is required.

### 1.5 Theorem 3.1, Corollary 3.2, GRH remark — SOUND, carried forward

These round-2 SOUND proofs and their distinction between cap-exceptional and ES-exceptional primes are unchanged. No numerical re-litigation is needed. Their hypotheses must still be supplied when they are invoked in the new hybrid paragraph; see §6 below.

## 2. Section 4: p-dependent data

### 2.1 Lemma 4.1 — SOUND

For an orthonormal basis `f₁,…,f_d`, each normalized selected vector satisfies

`β_p(a^(p)) ≤ Σ_j β_p(f_j)`.

Summing over `E` gives `T#E≤dΔ`. The change from `K` to `d` removes the clash with a modulus-size exponent. Linear dimension, not injectivity or state count, is the correct loss. Sharpness is appropriately restricted to abstract orthogonal test systems.

### 2.2 Proposition 4.2(i), including overlap — SOUND

The disjoint case remains the previously SOUND argument: the entire plane has residue 1 modulo `L`, so choose `a^(1)` before applying Corollary 2.6.

For the repaired overlap argument, let `H=Π∩supp L`, `|H|=t`, and on a nonempty plane fibre write a squarefree index as `n=uv`, with `u` supported on `H` and `v` on `Π\H`. The signs of `u` are fixed there, while those of `v` remain independent. Thus, for the normalized datum selected by that fibre,

`E_c |Σ_n a_n^(c)(x/n)|² = Σ_v |Σ_u a_uv^(c)(c/u)|² ≤ 2^t Σ_{u,v}|a_uv^(c)|² = 2^t`.

Averaging over the plane preserves this bound despite the datum changing with `c`. The global sterile set has measure at least `1/2`, so it contains a point with its **own selected datum's** bias at most `2^{t+1}`. No sterility of every prescribed residue fibre is asserted or needed.

For any finite `𝔊`, include `L`, its class moduli, 8, and the support primes in the final CRT modulus. The witness is a unit, and Dirichlet supplies infinitely many primes with the same selection and bias. The strict threshold `T>2^{t+1}` is correct. This is still an infinite-range obstruction, not a guarantee of witnesses in the current dyadic interval.

### 2.3 Proposition 4.2(ii), twists — SOUND

The fundamental theorem of calculus gives the displayed supremum bound. On the sparse plane, with Corollary 2.6's squarefree support hypotheses,

`E|F(t)|²=‖a‖²`, and `E|F′(t)|²=Σ|a_n|²(log n)²≤(log N)²‖a‖²`.

Cauchy–Schwarz and integration over an interval of length `2T₀` give exactly

`E sup_{|t|≤T₀}|F(t)|² ≤ (1+4T₀ log N)‖a‖²`.

The sterile-set factor is 2, hence `T>2(1+4T₀ log N)`. The endpoint `T₀=0` is now correct. The supremum controls every possible selected `t_p`; no unjustified integrated-hybrid-sieve estimate is invoked. The erroneous assertion that the selected-t large-sieve constant simply costs `T₀` is gone.

For clarity, repeat “under Corollary 2.6's support and sparsity hypotheses” in (ii); its reference to that corollary currently supplies them.

### 2.4 Proposition 4.2(iii) and scope note — SOUND

Linear independence is now an actual hypothesis. For divisor-indicator vectors in an ambient space containing all their coordinates, ordering the primes increasingly makes the coordinates `p+1` triangular with nonzero diagonal. This proves the example's full rank, rather than inferring independence from injectivity.

For a nonempty full-rank family the dimension bound becomes `#E≤#E·Δ/T`; a valid `Δ` bounds every individual bias, so this use of Lemma 4.1 is indeed void. It does not prove that every possible analysis of that family is void.

The rank-2 counterexample and the warning that few states need not mean congruence dependence are explicitly retained. The universal blocking lemma is genuinely withdrawn. Read “excludes” in the scope note as the particular bounds and thresholds just proved, not an exclusion of arbitrary twists or arbitrary fibre-dependent data at every threshold.

## 3. Section 5: orientation, windows, and the conditional theorem

### 3.1 Lemma 5.1's corrected list — SOUND

The implication and failure-set orientation are correct. The surviving relaxation examples really admit integer ES triples: EXPONENT_CAP Definition 1.1 permits denominator 1 at every cap; UNIT_ORBIT_ES §1 and SYNTHESIS_SPARKS2 §2 explicitly include ES; POWER_LADDER_ES Definition 1.1 permits `Q=1` for every rung. The deleted restricted-window and mixed-sign `V_φ` examples are correctly identified as not tautological relaxations.

The wording now says that the character property does not transfer **by this inclusion**, not that no independent proof could establish it. The `p=5,q=7` warning is correct.

### 3.2 Lemma 5.2's failure set — SOUND

The failure set is now the prime part of `Ω(𝔊)`, not the redundant intersection `E_X∩Ω(𝔊)`. With the stated threshold qualification it contains the relevant exceptional primes. The finite-menu, sparse-support and whole-period restrictions are explicitly preserved. No claim about every infinite menu or every finite-range implementation has been smuggled in.

### 3.3 Window criterion and “forced” terminology — SOUND

The inserted necessity proof is correct: coprimality of `u,v` gives `uv|B`, and `gcd(q,B)=1` removes the factor `h` from `q|h(u+v)`. Conversely the two displayed denominators are positive integers and their reciprocal sum is `q/B`. Their ordering is irrelevant.

The CAP_DOWN “some capped certificate” assertion is now restricted to `p≡1 mod 8`, avoiding the round-2 even-window objection. It is not being identified with a cap-0 firing. The existing independent checker again passes all 273 direct-search comparisons; see §8 of this report.

### 3.4 Relabelled finite window evidence — SOUND; MINOR wording

The table correctly measures **forced-only** failures, a superset of actual window failures, and reports the correlation range reaching 0.11. Stored JSON agrees with the displayed rounded entries. The changing forced rate and the need for an asymptotic rate hypothesis are acknowledged.

Replace “within ≈25% in the populated bins” by “within ≈25% in the displayed bins.” The stored `y=200,k=9` bin has 878 primes but observed/predicted failure rates `0.0011/0.0021`, about a 48% discrepancy. Its expected failure count is tiny; that is a sound reason not to use it for a relative-error claim, but “populated” alone does not express that reason. This does not undermine the qualitative evidence.

### 3.5 The repaired lottery model — MINOR mathematical overstatement

A lower bound `(log X)^{−o(1)}` on rates is now supplied, which repairs the missing assumption behind the model's exponentially small failure estimate. But it does **not** supply a tilt factor bounded away from 1.

Even in the intended independent model with initially fair signs, if the forced and unforced rates are `f,u`, the failure-conditioned nonresidue probability is

`θ_fail=(1−f)/(2−f−u)`, so `1/2−θ_fail=(f−u)/(2(2−f−u))`.

Taking `u=exp(−√log log X)` and `f=2u` satisfies the new rate hypotheses, but the tilt factor `(1−f)/(1−u)` tends to 1 and the bias tends to zero. It is still `(log X)^{−o(1)}`, sufficient to exceed a fixed `(log X)^{−κ}` threshold when `κ>0`; it is not a fixed positive bias and does not justify that reading at `κ=0`.

**Repair:** state the displayed bias formula and its rate-dependent consequence, or assume the firing-rate gap is bounded below by a positive constant. This affects the Assessment, not Corollary 5.3.

### 3.6 (WL_{A,κ}) and Corollary 5.3 — SOUND

All the substantive round-2 repairs are present:

* only Mordell-hard primes are quantified, so the windows have integral `x`;
* `A>1` and `0≤κ<(A−1)/2` are fixed;
* the hypothesis holds at **every sufficiently large scale**;
* the block has `s∼y/(4 log y)`, enough for Theorem 3.1;
* non-Mordell-hard primes are handled by the classical ES solutions;
* the conclusion is the every-δ form, not an uncontrolled variation of the large-sieve epsilon.

For completeness, put `α=(1+2κ)/A>0` and `X_j=X/2^j`. In each sufficiently large dyadic interval, failure of ES and (WL) imply `|σ_{S_j}(p)|≥(log X_j)^{−κ}s_j`. Theorem 3.1 gives `O_{A,κ,δ}(X_j^{α+δ})`. The sum is bounded by

`X^{α+δ} Σ_{j≥0}2^{−j(α+δ)}=O_{A,κ,δ}(X^{α+δ})`.

The finitely many remaining primes are absorbed in the constant. A fixed starting scale for (WL) is understood. The strict inequality in the antecedent puts equality into the biased set, as needed.

The corrected window-count factor and the withdrawal of “not a CRT consequence” are also SOUND. CONDITIONAL is now an honest label for a viable but unproved hypothesis.

## 4. Section 6: ratio classes and reverse-role sieves

### 4.1 Section 6.1's evidence bullet — SOUND

“Labels” now means accepted `(M,D)` occurrences, not distinct residues or independent coupon draws. The cubic expression is explicitly a finite fit and its extrapolation a model. The one-coordinate result is not being promoted to multi-coordinate ratio-family sterility. These are the repairs round 2 requested; the unchanged generic forcing runs need not be repeated.

### 4.2 Plane ℛ(M) finiteness argument — SOUND

The new finite-enumeration argument is valid. With `k≤k′`,

`km−1≤qm+1`, hence `k≤q+2`.

Expanding the product identity gives `m(kk′−q²)=k+k′+2q`. For `k≥2`, `m≥1` implies `(k−1)(k′−1)≤(q+1)²`, giving a finite range for `k′`. For `k=1`, the positive factors in

`(m−1)(k′−q²)=(q+1)²`

give a finite divisor enumeration. This is not merely an empirical cutoff in `m`.

The existing checker retains the necessary original congruence, positivity, divisibility-by-4 and `q∤m` filters. Its rerun confirms the exact mean `39.83018867924528`, largest pivot `5,706,695`, zero residue hits, and all five rounded coverage values. The saturation assertion is explicitly confined to the finite tested q-range. PROVED for finiteness and CERTIFIED for the finite table are appropriate labels.

### 4.3 Proposition 6.1(a): citation audit — SOUND, with an interval clarification

The relevant source is EXCEPTIONAL_LARGESIEVE Theorem 3.1, lines 242–277, not a native-family cap. Its hypotheses match as follows:

| Cited hypothesis | Present application |
|---|---|
| finite mixture of ℛ(M), `(a,D)`, Case-A and selector classes | exactly the family in (a) |
| an interval of `N` integers | take `I=[1,X]`, `N=X` (integer endpoint convention) |
| `Q₀≤N/2` | `Q₀=L≤X/2` |
| every fibre handled, by a CRT-admissible sieve or the trivial bound | all residues, including nonunits, are now included |
| lower bound valid for every probability law on the **whole** fibre avoider | missed residue classes of that avoider; Montgomery's residue-only inequality has this property |
| rational frequencies of charged level `λ_Θ` | Farey denominators `d≤Q`, so `λ_Θ≤log Q` |

For `(d,L)=1`, reparametrizing `n=c+Lk` permutes residue classes modulo `d`; it does not change the certified number of missing classes. The use of squarefree composite denominators in the Montgomery product is consistent with the citation. The source also permits more general denominators, so squarefreeness is not essential to the level argument.

Thus the cited theorem gives the asserted lower bound with `λ=max(λ₀,λ(L)+2log Q)` (enlarging the actual charged level only weakens the floor). It remains relative to the source's internal KARY2 dependencies.

**Clarification:** say explicitly that the sieve is run on `[1,X]`, thereby bounding the dyadic exceptional subset as well. If instead it is run directly on `(X/2,X]`, its interval length is `N≈X/2`, not `X`: the cited hypothesis would be `L≤N/2≈X/4`, and the stated prefactor changes. The current proof's `⌊X/L⌋` makes the full-interval reading clear, but this should not be left implicit.

### 4.4 Proposition 6.1(b): native version and assembly — SOUND

EXCEPTIONAL_LARGESIEVE Corollary 2.2 is pure duality; it does not require the avoider itself to be a ratio-family avoider. In each fibre it gives a globally nonnegative majorant with mean cost at most the sieve bound divided by the fibre length. Reassembling gives

`ν(n)=ν_c((n−c)/L)`, `Eν=L^{−1}Σ_c Eν_c`.

Every fibre is now represented. “Empty ones” must mean the **periodic fibre avoider is empty**, as in the cited proof, not merely that no exceptional prime has been observed there. The new length restriction also prevents geometrically empty full-interval fibres.

A local summand modulus dividing `lcm(d₁,d₂)` becomes `L·lcm(d₁,d₂)`, with level at most `λ(L)+2log Q`. This is correctly per-summand, not the total frequency period. Thus

`total bound ≥ ⌊X/L⌋Σ_c Eν_c = ⌊X/L⌋L Eν ≥ (X/2)Eν`.

EXSET_SIEVE_MASS Theorem 3.2, lines 292–299, permits arbitrary native class moduli and precisely the globally nonnegative majorant of the whole integer avoider just constructed. It supplies the `2/3` floor. There is no remaining omitted-nonunit-fibre gap, and no need for the alternative unit-selector repair proposed in round 2.

### 4.5 “Why the cubic reach does not enter” — SOUND as a model

The `1/m` weight is now explicitly an average over `c`, not a literal count or a uniform bound in every fibre. No theorem is inferred about unusually dense fibres. The suggested `(log log X)^3` scale remains a heuristic, not a consequence of Proposition 6.1.

### 4.6 Section 6.3 decision — SOUND family repair; MINOR scope qualifications

The ratio/native distinction is now correct: ratio mixtures use `3/4`, native U/ES₅ uses `2/3`. The false assertion that native sterile points have zero ratio-family reach is gone. Approximate input is explicitly allowed, rather than pointwise input being declared necessary.

However, “Every fibred, CRT-admissible implementation” must inherit the interval/fibring hypotheses of Proposition 6.1. A no-fixed-power-saving conclusion also needs `λ(L)+2log Q=O(log X)`, for example `Q≤X^K` with fixed K; the quantitative proposition itself allows larger Q but then does not give a `(log X)^{3/4}` cap. Add those qualifiers. Likewise “outside these CRT mechanisms” must not mean outside *all* CRT mechanisms: the per-summand hybrid of §8 remains open.

## 5. Theorem 2.10, summaries, and the repair ledger

### 5.1 Theorem 2.10(A)–(D) — SOUND as a scoped conjunction

* **(A): SOUND.** The missing `T>φ(k)` is explicit. The compatible unit-class hypotheses of Proposition 2.2 are inherited.
* **(B): SOUND.** Sparse Π, native family, finite class menu and all-large-primes scope remain present. “Such data would give a power saving” refers to the useful choices in Remark 2.7, not every sparse datum.
* **(C): SOUND.** Whole-period control is explicit; this is not a per-summand-only theorem.
* **(D): SOUND with Proposition 6.1's hypotheses.** The two family exponents now have the correct sources. State “under Proposition 6.1's fibre and level hypotheses” to prevent an unqualified reading.

### 5.2 The not-covered list — SOUND

The list retains dense/multiscale supports, the genuinely open p-dependent families, variable-order/full-character systems, per-summand-only hybrids, ratio-family multi-coordinate planes, and finite-range arguments. In particular, it does not confuse the reverse-role ratio-family cap with a sterile-plane theorem for that family. The finite-range caveat is substantive and must stay.

### 5.3 Section 0 table and bottom line — MINOR table qualifications; MAJOR exhaustive conclusion

Most table repairs are faithful: dimension replaces state count; the universal lemma is withdrawn; window failures are forced-only; checked boxes are named; the two family caps are distinguished. The 4.2 and 6.2 rows should inherit their actual thresholds, sparse-support and fibre/level restrictions rather than suggest unrestricted exclusions. The fixed-order mean statement should say “compatible unit class,” as in Proposition 2.2.

The bottom line now correctly says **bounded whole-period level**, but still ends with “what is missing is a non-CRT input.” That is not what the body proves: §8 item 5 explicitly leaves a CRT-majorant hybrid open, and dense/structured mechanisms also lie outside the proved exclusions. Theorem 2.10's Reading has the same overly exhaustive pointwise-or-non-CRT formulation. This was a round-2 scope concern and is not fully repaired.

**Repair:** say “additional input outside the proved certification mechanisms, possibly through the still-open CRT hybrids, dense-support or structured-data routes, or through pointwise/approximate non-CRT input.” Also retain `T>φ(k)` and squarefree support in the bottom-line higher-order shorthand. These are scope corrections, not withdrawals of the proved barriers.

### 5.4 Section 7's repair ledger — MINOR overstatement

The ledger accurately records the main §§4–6 repairs, including all fibres and `L≤X/2`. “All repaired” is too categorical for the small-prime bookkeeping and the remaining summary qualifications. More importantly, “§8 item 5 … Repaired” describes only part of the repair: the correct denominator and average have been supplied, but the domination and counting issues below remain. Update the ledger after fixing those rather than certifying them by assertion.

## 6. Section 8: remaining gap and fibre-cap hybrid

### 6.1 Items 1–4 — SOUND, with the inherited qualifications

They correctly distinguish T2-lite from T2-full, keep per-summand hybrids and structured low-rank families open, call the cubic reach a model, identify forced-only window failures, and restrict proved multi-coordinate sterility to the native sparse setting. The GRH obstruction is specifically to the confinement route below the cap threshold. Add the fibre/polynomial-level qualifiers to item 1(D), as above.

### 6.2 Item 5: what is repaired — SOUND

The new denominator is `(1/2−η/2)s`. Consequently `0<η<1` is the correct positivity restriction; the earlier recommendation `η<1/2` concerned the *old* denominator `(1/2−η)s` and should not be repeated mechanically. Replacing “most q” by an average is also correct. The text now distinguishes conditional probability from joint density and from an attainable low-level majorant. It no longer claims that Linnik removes “exactly” the square-like points or that an old cap has been proved inapplicable in every possible form.

### 6.3 Item 5: domination on the integer avoider — MAJOR, not repaired

The assertion that **every avoider point outside `B_J`** has at least `(1−η)s/2` negative coordinates uses the identity

`#negative=(s−σ_S)/2`,

which requires every symbol to be ±1. On the integer/profinite domain being majorized, symbols may be zero. Neither global nonnegativity of `ν_q` nor the new parameter range repairs this.

There is an explicit native-family obstruction to the printed argument. Every native class is restricted to `n≡1 mod 4` (the U classes further to `1 mod 8`). Take `x=4∏_{q∈S}q`. It avoids every such native class, but all `(x/q)=0` and it has **no** negative coordinates. The individually legitimate choices

`ν_q(x)=1[(x/q)=−1]`

are globally nonnegative congruence combinations of level at most `log q` and dominate their required fibre avoiders. Their normalized sum is zero at this x.

This also defeats the natural moment-datum interpretation of `B_J`: for the parity-kernel vector b of Theorem 3.1, at this x only the coordinate `n₀=1` can contribute. Hence `β_x(b)=|b₁|²/‖b‖²≤1`, whereas the useful Linnik threshold grows as a positive power of X. Thus x is outside that `B_J`, too. One cannot silently replace a claim about the whole integer avoider by a claim only about primes.

**Repair:** explicitly restrict domination to an avoider with selectors `0 mod q`, `q∈S`, removed (and the desired hard-prime congruence restrictions), or add a separate majorant for the zero-coordinate locus. Exceptional primes dividing `∏S` can be discarded separately; in the dyadic large-X regime they are absent. Then define the bias set consistently:

`B_sign={x:(x,∏S)=1, |Σ_q(x/q)|≥ηs}`.

On that unit domain the moment identity identifies it with `B_J` for b at threshold `T=(ηs)^{2r}/‖b‖²`. Fix `A>1` and **`0<κ<(A−1)/2`**, `η=(log X)^{−κ}`; this both makes the normalization bounded and lets Theorem 3.1 count the biased primes with a power saving. The κ=0 endpoint has η=1 and is not available for this particular averaging construction.

Also specify a finite, threshold-handled class family defining `Ω_λ`, or justify an infinite-family substitute. A bound on radical level alone does not bound prime-power exponents and therefore does not automatically define a finite periodic class menu. The primes to be bounded must actually lie in this avoider.

### 6.4 Item 5: power-small average versus an actual prime estimate — MAJOR missing qualification

For the repaired unit-domain construction,

`Eν = 2/(1−η) · (s^{-1}Σ_q Eν_q)`.

Thus a power-small average is exactly the relevant **Haar-mean target**, provided `(1−η)^{-1}=X^{o(1)}`. It is not, by itself, an “iff” criterion for this sieve to give a power-saving finite-interval exceptional-set bound.

Writing `ν=Σ_i c_i1[n≡b_i mod d_i]` gives only

`Σ_{n≤X}ν(n) ≤ X Eν + Σ_i |c_i|`.

Level alone controls neither that coefficient sum nor a substitute discrepancy bound. In this paper it is radical level: high powers of 2 already permit arbitrarily long periods at zero charged level. For example, with `2^h>X`, the indicator of the residues `1,…,⌊X⌋ mod 2^h` has mean `⌊X⌋/2^h` but is 1 throughout the target interval. Taking h large makes the mean arbitrarily small without changing that fact or its charged level. Such a spike can also be added to any nonnegative candidate without spoiling domination. Thus low level plus low Haar mean is not a counting theorem.

This distinction is exactly why Proposition 6.1 uses the large-sieve dual objective to bound the *numerical sieve bound*, whereas the proposed hybrid uses actual CRT majorants on a finite interval.

**Repair:** call the average condition the mean-saving target, and add a quantitative finite-interval evaluation hypothesis, such as `Σ_i|c_i|≤X^{1−c}` together with `Eν≤X^{−c}`, or another justified discrepancy estimate. Then

`#E_X ≤ #B_J + Σ_{n≤X}ν(n)`

gives a power saving. A fibre-cap hypothesis about least **mean** alone is not yet a sufficient implementation theorem. The “if it is ≈ μ(Ω_λ)ρ_q(λ)e^{O(λ^{3/4})}, the hybrid gives a power saving” sentence needs the same qualification, as well as an average/uniform bound over the chosen q-block.

### 6.5 Item 5: model bullets and tilt experiment — SOUND as open modelling, not as exclusion

The quadratic-versus-cubic label comparison remains explicitly heuristic. The claim that there are only `X^{o(1)}` squarefree products of primes at most `C log X` follows already from `2^{π(C log X)}=X^{o(1)}`; it supports the support-count warning, not an exclusion of all p-dependent or multi-coordinate mechanisms. The ratio-family window of possible overlap is a model opportunity, not a theorem.

A merely “positive-measure” twisted base would also need a quantitative `X^{-o(1)}`-type mass lower bound and the appropriate level/projection argument to cap a power saving; arbitrary positive mass could itself be power-small. The text should say so.

The finite tilt experiment is clearly described as such, with its diminishing survivor population and irrelevant small-q regime. I did not rerun it. It does not supply either missing hybrid hypothesis. The statement that measure-zero sterile planes do not settle this door is correct.

## 7. Label honesty

**SOUND:** PROVED for the dimension inequality, repaired overlap/twist bounds, orientation and window algebra; CONDITIONAL for Corollary 5.3; PROVED relative to the cited cap machinery for Proposition 6.1; EVIDENCE for the finite window and generic forcing data; PROVED/CERTIFIED for the correctly scoped plane finiteness/table; CONJECTURE for dense sterility.

**Needs correction:** Assessment does not justify the fixed-factor lottery claim, the exhaustive “non-CRT input is missing” conclusion, or §8's unconditional elementary domination and “iff” statements. These are the residual issues, not failures of the principal repaired propositions. The repair ledger should not mark them completed until the stated qualifications are added.

## 8. Bounded verification

No new test was added: the existing round-2 independent checker already covers the inserted window proof and the plane enumeration. I inspected its allocation/loops first: trial division, small divisor lists, and streamed ranges up to q=300, not dense product arrays. It was run with both requested limits:

```sh
ulimit -v 8000000
timeout 180 uv run --no-project python3 reviews/z51-linnik-review-2-check.py
```

It exited 0. Results: 273 window cases, 86 live, zero disagreements; 61 plane primes through 300; mean labels `39.83018867924528`; maximum pivot `5706695`; zero residue hits; coverage `0.567567568 / 0.401662050 / 0.320066335 / 0.313402062 / 0.258928571`. The two small window JSON files were read directly for evidence wording. No full expensive experiment was rerun, and no empirical computation is being used to validate an asymptotic claim.

## Final list

1. **SOUND:** both round-2 FATAL claims are repaired; §§4's main bounds and (WL)/Corollary 5.3 survive.
2. **SOUND:** Proposition 6.1's all-fibre assembly and ratio/native citations match, on a full interval of length X with `L≤X/2`; retain polynomial-level qualifiers for the no-power-saving reading.
3. **MAJOR:** §8 item 5 needs unit selectors or zero-symbol control, an explicit matched bias datum, and admissible parameters/class menu.
4. **MAJOR:** power-small average Haar means need a finite-interval counting/discrepancy hypothesis before they yield the claimed hybrid saving.
5. **MAJOR scope / MINOR wording:** summaries must leave open CRT hybrids; correct the rate-dependent lottery tilt, the displayed-bin wording, and the remaining small-prime bookkeeping.

The repaired core does not prove a power-saving ES exceptional-set estimate. The remaining fibre-cap route is genuinely open, but its sufficient conditions are not yet stated correctly.
