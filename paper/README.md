# Paper draft status

`espaper.tex` is the v17 standalone `amsart` consolidation draft (177 pages). Its two record headlines remain:

- `E_all(N) ≪ N exp{-c(log N)^(3/4)}`;
- for every fixed `epsilon > 0`, uniformly for `3 <= m <= (log N)^(3-epsilon)`,
  `E_m(N) ≪_epsilon N exp{-c_epsilon(eta_2(m)(log N)^3/phi(m))^(1/4)}`.

Both remain visibly **CLAIMED/PROVISIONAL**. The general-numerator headline inherits the likewise provisional source Theorem 34.8, paper Theorem `m-pruned`, and every source §39.7 qualification. “Unconditional” means only that no unproved hypothesis is assumed; it does not mean externally validated. The paper does not claim a proof of the Erdős–Straus conjecture.

## v17 changes — 2026-08-30, wave 31

- Absorbed source §70 as Section 32.  For each fixed prime `a = 3 mod 4`, failure splits exactly into quadratic-residue confinement F1 and bounded-budget F3; F2 is empty, F1 has the exact `H/sqrt(log H)` asymptotic, and F3 is lower order with exponent `1/2 + 1/(a-1)`.
- Added the effective shifted-prime upper law and fixed-congruence-wall freeness.  Every compatible fixed progression has density-one success at fixed `a`; all constants and errors may depend on fixed `a`, and no growing-`a`, joint-tail, or pointwise result follows.
- Preserved the composite-modulus correction exactly: maximal avoiding subgroups are kernels of cyclic `2^k` quotients, not merely odd quadratic characters.  The `a=15`, `C_2 x C_4` counterexample is explicit, and table (70.36) remains Computational only.
- Absorbed source §71 as Section 33.  The Shiu, Nair–Tenenbaum, and Henriot theorem statements remain explicit verbatim quotations with their exact page references and dependency sentences.  They prove fixed dimension only; no cited source gives a growth rate for the hidden constant `C(J)`.
- Added the unconditional fixed-`J` shifted-form means, exact discriminant table (71.24), collision-factor table (71.32), and local-correlation formula.  These fixed-`J` bounds are weaker than the standing literature and the campaign’s provisional record shapes.
- Preserved the exact open hypotheses `H_FAIL(theta_0)` and `H_STACK(theta,gamma)`.  Every moving-`J` tail and count-below-one consequence is conditional on both; the favorable branch has exponent `L^theta/(4 theta)`, while prime-only count below one requires `Z > (4+o(1)) log N`.
- Absorbed source §72 as Section 34, wholly Computational/INFO.  The complete `a_1` census covers all 719,781 hard primes below `10^8`, retains maximum 107 uniquely at 8,803,369, and transcribes the per-modulus panel, dependence panel, full tail histogram, strict-record anatomy, F3-share ledger, and omega-conditioned table digit-for-digit.
- Extended the internal pedigree through blocks `(bq)`–`(bs)` and the wave-30 `SOUND-AFTER-REPAIRS`, `SOUND-AFTER-REPAIRS`, and `CONFIRMED-AFTER-REPAIRS` verdicts.  These are internal proof/source reviews and bounded computational replays, not external validation.
- Updated the abstract, introduction roadmap and status register, global pedigree, final status, verifier endpoint, tracked table of contents, and PDF.  The build grows by 26 pages, from 151 to 177.
- Typesetting/reference judgment calls (explicitly recorded by the fidelity review): inserted the missing `\\` before `\hline` in (71.24); used `\resizebox` on wide tables/displays without changing their contents; mapped §70's correlation-warning pointer from source §63.2 to Assessment 63.2 (the actual warning is in source §63.5).  All three are fidelity-preserving.

## Wave-31 v17 fidelity review

- Verdict **FAITHFUL-AFTER-REPAIRS**; restored the abstract's unit hypothesis and escaped 18 percent signs that silently erased census digits, INFO labels, and caveats in Sections 32 and 34.  All 100 tagged displays, the reviewed character-twist and prime-density hypotheses, exact census tables, conditional/provisional statuses, and three judgment calls agree; the two-pass build remains clean at 177 pages.  Review: `reviews/wave31-paper-v17-review.md`.

## v16 changes — 2026-08-30, wave 30

- Absorbed source §69 as Section 31.  Integer-wise polynomial divisibility on a tail collapses to a polynomial identity with an integer-valued cofactor, including all earlier integer arguments; the exact shadow blockage is therefore only failed positivity/range.
- Added the one-step real-sign lemma and Theorem 69.4: no single polynomial witness datum covers a forward tail on any ray anchored at `288`, `336`, or `4545`.  Both pointwise and polynomial divisibility regimes, every degree, every period `K >= 1`, and every tail start are covered.
- Preserved the strict perimeter: this is an obstruction to polynomial witness families only.  Arbitrary non-polynomial functions, finite-piece polynomial choices, and unanchored rays remain untouched; no fourth `W=+infinity` value, classification of `W(2m²)`, or evidence for `C_SQ′` follows.
- Added the complete constant-divisor classification and block `(bp)` ledgers.  The independent bound-5,000 replay has 5,792,112 candidates and zero hits; the 65-class fixed-data projection has 1,709 divisor rows and zero hits.  These bounded zeros are regression checks, not the all-degree proof.
- Retained the wave-29 **SOUND-AFTER-REPAIRS** refutation-class attestation, including the backward-positivity case split, tail induction, integer-valued quotient caveat, and independent finite replays.
- Updated the abstract, introduction, status registers, §66 forward pointer, global pedigree, final status, verifier endpoint, tracked table of contents, and PDF.  The build grows by 6 pages, from 145 to 151.

## v15 changes — 2026-08-30, wave 29

- Absorbed source §66 as the twisted-family escape-cylinder section.  Membership in `{m: W(sm²) <= T}` is class-decidable modulo `L(T)`, with `log L(T)=(2/3+o(1))T`; the three anchored families have unbounded finite depth and density at least `1/L(T)` at each fixed depth, but no new fixed `W=+infinity` member is produced.
- Added the family finite-certificate ceiling and all-degree anchored polynomial-identity obstruction while preserving the repaired forward-ray leak: polynomial equalities extend backward, but positivity and positive-divisor eligibility need not, so the forward-ray gap remains open.
- Added the exact 54,990-candidate identity hunt, 65-class depth-1000 projection modulo 627 with digest, and all three `m <= 2000` censuses.  The sole cap survivors are the proved anchors; finite maxima are `4019/695/479`, and no infinity is inferred from a cap.
- Absorbed source §67 as the finite record-stall anatomy.  The purity depth is an integer supremum allowing `+infinity`, with `tau(193)=+infinity`; all top-ten profiles, depths, four-shift factors, and residue-one rows are retained exactly.
- Preserved the no-evidence register for the fragile spacing model: `P_raw=1.222901698e-9`, `P_0.85=2.656334824e-8`, and formal expectations `0.0169180/0.1497047` are reproducible toy arithmetic, not a tail claim or evidence about the stall.
- Restated the exponent frontier exactly: `A_emp(2031121)=2.923244`, every eventual `A < 1` is refuted, every `A >= 1` remains open, and “1–2” is only the historical finite-normalization panel.
- Absorbed source §68’s full Pomerance–Weingartner arXiv:2511.16817v2 audit: exact Theorems 1.1–1.4, lower-exception regimes, crossover algebra, and the repaired §55 fixed-`B` nuance.  All verdicts are source-bounded, and Theorems 39.7, 43.12, 51.2, and 51.6 remain **CLAIMED/PROVISIONAL** where labelled.
- Registered Gottschlich and Nakayama as adjacent bibliography entries, updated the current PW citation and Vaughan secondary-access record, and retained the no-full-literature-certification caveat.
- Extended the global pedigree through blocks `(bm)`–`(bo)` and the three wave-28 attestations: **SOUND-AFTER-MINOR-REPAIRS**, **SOUND-AFTER-REPAIRS**, and **CONFIRMED AFTER REPAIRS, source-bounded only**.  These remain internal validation or source review, not external refereeing.
- Updated the abstract, introduction, section map, status register, §65 forward pointer, final status, bibliography, verifier endpoint, tracked table of contents, and PDF.  The build grows by 12 pages, from 133 to 145.

## Wave-29 v15 fidelity review

- Verdict **FAITHFUL-AFTER-REPAIRS**; restored the four verbatim PW theorem quotations promised by the source register, made the Layer-1 range explicit in the PW consistency check, and retained every source §66–§68 status, quantifier, digit, caveat, and wave-28 attestation.

## v14 changes — 2026-08-30, wave 28

- Absorbed source §63 as the new algebraic-witness-taxonomy section.  The proved DIV/D1, fixed-`D`, universal CRT-coupled `a`, square-root, congruence-coverage, and effective half-dimensional-sieve laws retain all hypotheses and range checks.
- Preserved the honest comparison: the square-root regime is weaker than §51 on both the modulus and exceptional-set axes, is not directly threshold-comparable to that window, and gives no pointwise progress or new supply family.
- Added the exact `a_1` first-witness-index censuses through `10^6` and gated `10^7`, separating `a_1` from `a_W` and retaining every histogram, maximum, correlation, late row, and no-growth-law warning.
- Absorbed source §64 as the gcd-mechanism section.  The cancellation-cover theorem keeps the exact eligibility-failure valuation window and empty-row possibility; the `D=1,2`, dyadic, twisted-square, and composite-unit-branch laws remain necessary/sufficient only at their stated scopes.
- Added all three complete sporadic cancellation ledgers and the enlarged hunt: 146016 old plus 242837 new pairs, 388853 total distinct points, no survivor, and exact maximum `W(3201660)=5303` at `15*462^2`.  The `10^9` result remains a thin coordinate slice, not an interval scan.
- Kept the classification walls explicit: nonsquare finiteness is open, `C_SQ'` remains open with only its right-to-left inclusion proved, and finite hunts concern the harvested `W` mechanism rather than all Egyptian-fraction representations.
- Absorbed source §65 as the Computational/INFO two-decade census of all 719781 hard primes below `10^8`.  All 15 strict records, the empty post-`10^7` record list, parity split, histogram, and 21 dyadic block rows are retained without a growth-law or `H_MOD` claim.
- Recorded the source-audit distinction exactly: block `(bl)` is a bounded record replay even under `ES_FULL_SCAN=1`; committed `scripts/review65_independent.py`, not `(bl)`, independently reruns the full census.
- Extended the internal pedigree through blocks `(bj)`–`(bl)` and all three wave-27 **SOUND-AFTER-REPAIRS** reviews.  These remain internal verification only.
- Updated the abstract, introduction, section map, status register, §62 forward pointer, final status, verifier endpoint, tracked table of contents, and PDF.  The build grows by 15 pages, from 118 to 133.

## Wave-28 v14 fidelity review

- Verdict **FAITHFUL-AFTER-REPAIRS**; restored the omitted sporadic ledger triples `(48,43,0)/(56,65,0)/(757,188,0)` and made the enlarged hunt's coordinate-box-only scope explicit; all other source §63–§65 statements, digits, statuses, and caveats agree.

## v13 changes — 2026-08-30, wave 27

- Absorbed source §62 as the new section immediately after the decidable-census section.  The proved ratio-spectrum law retains the exact bounded-exponent spectrum, divisor pairing, witness reconstruction, and `W(p)` minimization.
- Added the six exact small-`a` laws for `a=3,7,11,15,19,23`, including every inverse-paired residue row, the ten minimal mod-11 budgets, the `C4 x C2` law at 15, and the full multiplicity counterexample `Rat_7(17)={5,1,3}`.
- Preserved Assessment 62.1 and the exact six-column failure census through unit `h <= 10^5`; the Landau–Selberg–Delange asymptotic is context only and is not used in a proof.
- Added the finite-conspiracy equivalence, the exhibited-mechanisms-only register, and the explicitly Heuristic independence model with its shared-shift, shared-factor, no-tail, and no-pointwise caveats.
- Transcribed all four late-resolution rows, all fixed-`a` outcomes and failure-budget vectors, and the exact composite degradation ledger.  Small-`a` success may still have huge `M`, while the sporadic quotient rows remain confined to nonunit gcd/eligibility branches.
- Added the staged fourth-sporadic hunt over exactly the stated `(s,m)`-box subset: 146016 distinct integers, no stage-1 survivor, and exact maximum `W(9028800)=3359` at `(M,D,a)=(3359,48,2688)`.  This is bounded stress only: `C_SQ'` remains open, only its right-to-left inclusion is proved, and no `C_SQ''` is introduced.
- Transcribed the wave-26 **SOUND-AFTER-REPAIRS** pedigree and block `(bi)` scope accurately: ratio/pairing checks, every unit `h <= 10^5`, 1181 hard primes through `10^5`, record and sporadic ledgers, bounded Python-integer state, and the gated full hunt.  These remain internal validation only.
- Updated the abstract, introduction, section map, status register, internal and local pedigrees, final status, verifier endpoint, tracked table of contents, and PDF.  Block `(bi)` is the v13 verifier endpoint.

## Wave-27 v13 fidelity review

- Verdict **FAITHFUL**; no source-§62 transcription defects were found, all requested table digits and scope/status caveats agree, and the two-pass build is clean.

## v12 changes — 2026-08-30, wave 26

- Absorbed source §61 as the new section immediately after the witness-duality section.  The proved forward normal-form sieve retains the exact simultaneous bounds, positivity argument, divisor-table bound, and finite-decision equivalence.
- Added the complete Computational census: through `200000` by default and `10^6` under `ES_FULL_SCAN=1`, the `W=+infinity` set is exactly the squares plus `288,336,4545`; the optional row is `1003 = 1000 + 3`.  The forward canonical sieve, original-coordinate overlap, and all-3202-hard-prime comparison are kept methodologically distinct.
- Preserved the exact register for open `C_SQ'`: only the right-to-left inclusion is proved.  The bounded census is finite stress evidence, not an unbounded classification, and no `C_SQ''` is introduced.
- Added the finite twisted-square criterion with every gcd, uncancelled-eligibility, character, and even-`D` caveat.  The complete box has 3630 entries for squarefree `2 <= s <= 200`, `1 <= m <= 30`, with only `(2,12)` and `(21,4)` vanishing; `(505,3)` is explicitly a control outside the box.
- Proved the exact first-layer laws for `2m^2`: `W=3` iff `3` does not divide `m`; the `W=11` roots are `±2,±3,±4 (mod 11)` after the `M=3,7` exclusions; and, when those fail, roots `±3,±6,±8 (mod 19)` give `W=19` after the `M=15` exclusion.  The full root arithmetic and minimality proof are included without promoting this to a complete family classification.
- Added the standalone hard-prime criterion: for prime `p = 1 (mod 24)`, `W(p) < infinity` iff some `a = 3 (mod 4)`, `a <= 2 floor((p+1)/3)`, has a divisor `D | h^2` in the class `-h (mod a)`, `h=(p+a)/4`.  The proof makes `gcd(a,D)=1` automatic and explicitly retains all even `D`; it is a terminating equivalence, not a nonemptiness theorem.
- Retained the no-claim mechanism register, the `H_EQ` localization link, Heuristic-only divisor masses, the three later exact prime rows, and the §54 residue-one instance.  The all-hard-prime replay through `3*10^5` agrees in all 3202 cases; 1941 selected minimum rows have even `D`.
- Transcribed the wave-25 **SOUND-AFTER-REPAIRS** pedigree accurately: fresh original-coordinate classification for every `n <= 5000`, seeded samples `2000@[5000,200000]` and `500@[200000,10^6]`, optional complete million replay, independent twisted-square box replay, exact-ceiling scans, and memory bounds.  These remain internal validation only.
- Updated the abstract, introduction, section map, status register, internal pedigree, final status, verifier register, tracked table of contents, and PDF.  Block `(bh)` is the v12 verifier endpoint.

## v11 changes — 2026-08-30, wave 25

- Absorbed source §60 as the new section immediately after the polynomial-escape section.  The proved witness duality retains the full `aM=4D+n` correspondence, exact cancellation ledger, `gcd(a,D) | n`, the nonredundant eligibility recheck when the gcd is nontrivial, and the 2-adic caveat.
- Added the canonical `A=gu`, `h=gv`, `D=gd` normal form with `(u,v)=1`, `d | g`, `a=4gv-n`, and `au=d+v`.  Its unconditional bounds `a,u <= 2B` and `M <= 8B^2-1`, `B=floor((n+1)/3)`, use no `a <-> M` assumption and make `W(n)=+infinity` decidable by finite computation.
- Added computer-assisted Theorem 60.3: `W(288)=W(336)=W(4545)=+infinity`.  The paper records both exact normal-form exhaustions and the maximum-severity review's independent original-coordinate scans through `73,727`, `100,351`, and `18,361,799`, including the `409,000,770`-incidence largest replay.
- Reconciled every v10 frontier passage without deleting the still-valid §59 quadratic classification, twisted-square reductions, census, historical deep scan, or family controls.  Former `C_SQ` is now explicitly refuted; open `C_SQ'` adds exactly the three composite sporadics to the squares.  Only its right-to-left inclusion is proved, and the three displayed Egyptian-fraction representations make clear that these are statistic-escapes, not Erdős–Straus counterexamples.
- Added the exact near-miss ledger: all rows surviving the §59 filters fail uncancelled prime-power eligibility, and the four rows for `288` all have `gcd(a,D)=9` and fail at 3.  Added the exact terminating algorithm, its average divisor-work order, the odd-prime gcd simplification, and the warning that no pointwise prime or Erdős–Straus theorem follows.
- Added the conditional `a <-> M` involution, including bi-eligibility on both sides and the forced class `n = 1 mod 4`, plus the exact two-front coverage identity and the historical-scan supersession.
- Updated the abstract, introduction, section map, status register, internal pedigree, final status, verifier register, and tracked table of contents.  Block `(bg)` and the wave-24 **SOUND-AFTER-REPAIRS** attestation remain internal validation only.

## v10 changes — 2026-08-30, wave 24

- Absorbed source §59 as the new section immediately after the inverse census. The proved exact local criterion retains the eventual-tail convention, every harvested divisor class, the distinct arithmetic-progression compatibility condition, and the warning that finite-depth residue-one escape is not uniform polynomial escape.
- Added the all-degree root-field/cyclotomic obstruction with every shift `D`, the root-field rather than splitting-field conclusion, and the `X^4-3` counterexample to using only `D=1`. Its Chebotarev input is qualitative and **INEFFECTIVE**; no least-prime bound is claimed.
- Proved the complete degree-at-most-two classification: uniform linear/quadratic escapes are exactly the polynomial squares, hence no linear escapes exist. The proof retains the leading-coefficient, eventual-sign, reducible/zero-discriminant, real/imaginary discriminant, coefficient-dependent new-prime, conductor, and divisibility cases, plus all three explicit later-shift replays.
- Added open conjectures `C_POLY` and `C_SQ` without promotion. `C_SQ` says that the positive integers with `W=+infinity` are exactly the squares; it implies Erdős–Straus for all primes and is strictly stronger, while no reverse implication is claimed. The proved prime-value corollary closes only the polynomial-family route through degree two, conditionally all degrees under `C_POLY`; progressions, higher degrees, recurrence orbits, and arbitrary thin families remain outside the unconditional scope.
- Added the proved all-integer tail obstruction. Squares force failure of the cubic supercritical hypothesis in every power window beyond `theta=1/3`; at the endpoint the displayed square comparison contradicts it for `cb^3>1/2`, while equality retains the prefactor/floor caveat. This retroactively makes the prime restriction in paper Theorem `witness-tail` logically necessary for the §57 count-below-one route.
- Added the exact twisted-square reductions and survivor census. The three live nonsquare candidates are `288=2*12^2`, `336=21*4^2`, and `4545=505*3^2`, each unresolved past `M=1.5*10^8`. The paper explicitly quarantines and rejects the former fixed-width-overflow pseudo-witnesses, records the streamed Python-integer run and its memory bound, and reports that 177 of 180 family controls are ordinary finite hits. These candidates are stress tests for `C_SQ`, **not positive evidence**.
- Updated the abstract, introduction, section map, status register, internal pedigree, final status, verifier register, and tracked table of contents. Block `(bf)` and the wave-23 **SOUND-AFTER-REPAIRS** attestation are represented as internal review only.

## v9 changes — 2026-08-30, wave 23

- Absorbed source §57 as Section 19, immediately after the congruence-certificate ceiling. The proved-conditional count-below-one reduction retains the exact thresholds: cubic `H_WIN(theta)` needs `theta > 1/3` without a favorable endpoint constant, while square-log `H'_WIN(theta)` includes `theta = 1/2`. Both window hypotheses are **UNPROVED**; the currently realized common power window remains only `theta = 1/4`, with the cubic row inheriting **CLAIMED/PROVISIONAL** Theorem 34.8 and the fixed-polylog row retaining the §39 review qualification.
- Added the exact cubic endpoint cases, including `cb^3 = 1` forcing zero only for `C < 1`, and the full counterexample-prime → `W=+infinity` → zero-count quantifier chain. No unconditional pointwise Erdős–Straus conclusion is claimed.
- Preserved Proposition 57.2 as proved arithmetic only inside the formal `AR(mu,t)` absolute-remainder architecture. Its source §18.2/(18.15)/Assessment 18.4, Lemma 33.3, and (51.11) antecedents remain explicit; the broader no-assembly statement is an **Assessment**, not the Proposition.
- Added the open `H_XW` supercritical-remainder and `H_EQ` fair-share hypotheses with fixed-family quantifiers, Proposition 57.4's proved-conditional crossing implication, §54's subcritical consistency, and exact verifier block `(bd)` calibration. None of the crossing hypotheses is asserted.
- Absorbed source §58 as Section 20, before the general-numerator truncation. The headline Theorem 58.1 is transcribed with its full repaired Jacobi proof: common-factor, nonunit, 2-adic, prime-power, global/local obstruction, and `(M,D)=(15,2)` cases are all explicit. It proves `W(m^2)=+infinity` for every positive integer and `T < L_int(T) <= T+2 sqrt(T)+1` under the moving inverse convention.
- Separated `L_int`, all-prime `L_p`, and hard-prime `L_h` throughout, including the warning `L_p(335)=22621` versus `L_h(335)=1853329`. The integer/prime dichotomy makes count below one prime-essential and retroactively explains Theorem 51.2's prime restriction. The only proved prime upper end remains `L_p(T) <= exp{(5.2+o(1))T}`.
- Added the exact inverse censuses, shifted-sieve lemma, the secondary-source-verified Iwaniec Jacobsthal bound and its strict scope, the prime-survivor technology audit, and Lemma 58.5's corrected `liminf` and `A`-window dualities. The primary 1978 Iwaniec PDF remains inaccessible; provenance is limited to the archived Costello–Watts and Ford–Green–Konyagin–Maynard–Tao full texts under `sources/jacobsthal-literature/`.
- Updated the abstract, introduction, section map, status register, internal pedigree, final status, bibliography, and verifier register. Blocks `(bd)`–`(be)` and both wave-22 **SOUND-AFTER-REPAIRS** attestations are represented without promoting internal review to external validation.

## v8 changes — 2026-08-30, wave 22

- Absorbed source §56's proved, effective congruence-certificate ceilings with both proofs complete. Every prime or all-integer Type-II certificate for `W > T` carries `P_3(T)`, so `log Q >= (1/2+o(1))T`; the paper expressly withholds the full-lcm constant `1`. Every hard Type-I certificate through `T` carries every prime `5 <= ell <= T`, so `log Q >= T+o(T)`.
- Added the scoped congruence/Linnik corollary, including the wave-21 repair that a least-prime bound must actually select a prime beyond an eventual certificate's finite exceptional prefix. The GRH consequence is visibly conditional. The congruence wall remains an architecture assessment, not a theorem that every superlogarithmic extremal argument must be noncongruential.
- Added the exact informational census: `W` through `10^6` and the memory-bounded full scan through `10^7`, including `(2031121,2495)`; `ck_pr` through `3*10^5` and the full scan through `10^6`; and the corresponding unrestricted `D(p)` records. The normalized panels are INFO-only and retain the warning against mixing finite census maxima with §54's asymptotic construction.
- Repaired the v7 two-sided-frontier wording to match §56: `[1, ~2]` is only a finite-search normalization panel, not a proved bound, conjectured limiting exponent, or monotonic trend. The pointwise frontier remains exactly `A < 1` impossible and `A >= 1` open; the new theorems constrain only complete-class certificates.
- Updated the abstract, introduction, section map, internal pedigree, and verifier register. Block `(bc)` now covers the certificate data and all extended finite scans; the source §56 hostile review's finite-prefix, resident-memory, and architecture-pointer repairs are preserved.
- Cleared the v8 queue: source §56 is absorbed. Source §§57–58 are queued for v9 only; no claims from those sections are imported.

## v7 changes — 2026-08-30, wave 21

- Absorbed source §54's proved, effective logarithmic lower tails. Theorem 54.1 gives infinitely many primes with `W(p) >= c log p`; its Type-I mirror forces every slice through `ck <= c log p` to vanish infinitely often. Consequently `H_MOD(A)` and `H_SPF(A)` are false for every `0 < A < 1`, and exactly `A >= 1` remains open in both defined pointwise frames.
- Added the two-sided frontier capstone: census-small and almost-all polylog-to-epsilon typical scale, an effective logarithmic extremal lower scale, and a clearly conjectural logarithm-squared-like ceiling suggested by distinct measured statistics. The data-guided window `[1, ~2]` is separated from the proved necessity `A >= 1`.
- Absorbed source §55's general-`m` truncated tails and exact status-preserving effectivity perimeter. The fixed-polylogarithmic Layer-1 row retains the §39 review qualification; the cubic row and Theorem 43.12 recovery remain **CLAIMED/PROVISIONAL**.
- Preserved the review-tightened Page-conductor quantifiers: when the exceptional conductor divides `m`, favorable-sign selection is proved only for the full Layer-1 multiplier family and the structured `c`-free fibres, never for arbitrary sparse subfamilies. The worst-case fibre subtraction and unfavorable formal `k=1` bookkeeping are explicit.
- Added the general-`m` Pomerance–Weingartner truncation comparison and finite block `(bb)` companion without claiming a finite crossover, range extension, or pointwise theorem.
- Added the related-work register for Dyachenko arXiv:2511.07465 and the auro-zera Lean formalization: the identity layer is sound, one axiom isolates the open core, compilation remains unverified, and Dyachenko's own Conclusion characterizes the needed infinite case as conditional. Sections 51–54 quantify what that axiom assumes; no paper theorem relies on it.
- Updated the abstract, introduction, earlier `H_MOD`/`H_SPF` discussions, internal pedigree, and bibliography. Wave-20 hostile reviews are registered; verifier coverage now runs through `(bb)`.
- Cleared the v7 queue: source §§54–55 are absorbed.

## v6 changes — 2026-08-29, wave 20

- Absorbed source §51's minimal witness-modulus statistic `W(p)`, parameterized truncation, both exact tail windows, polylogarithmic corollaries, `H_MOD(A)`, and the exact nonimplication relation with `H_SPF(A)`. The cubic variant remains **CLAIMED/PROVISIONAL**; the fixed-polylog variant retains the §39 review qualification.
- Added the effectivity headline: checked Lenstra–Pomerance JEMS 2019 Lemma 11.2, one-exceptional-conductor Bombieri–Vinogradov, uniform deletion tolerance, and effective class-supply/downstream constants. Theorem 51.6 is record-adjacent **CLAIMED/PROVISIONAL** and expressly does not effectivize Theorem 34.8's ancillary all-low-congestion-triples `o(1)`.
- Added §51's PW truncation credit and priority register. Dahan arXiv:2608.24035 Theorem 4.17 is prominently credited as the independent cubic exponent-shape antecedent for a different, ineffective two-parameter statistic; Vaughan remains inaccessible and no phrase-level search result is promoted to a literature guarantee.
- Recorded the §51 attested-blind protocol and **CONVERGED-WITH-DIVERGENCES** adjudication. The blind-side all-of-Theorem-34.8 effectivity overclaim was rejected, and all prior labels remain unchanged.
- Absorbed source §52's proved fixed-slice sieve with exact exponent `1+2/phi(4ck)`, elementary remainder, effective fixed-slice scope, empty congruence-level third layer, and proved but ineffective Siegel–Walfisz-uniform proposition. The finite composite-witness shapes and correlation caveats remain informational only.
- Absorbed source §53's duplicate-radicand quotient, fixed-box exponent `1+m_#(C)`, exact independent genus bits, permission-pair mass, and growing stack. Theorem 53.3 and the almost-all `H_SPF` corollary are **proved and effective**, with the uniform-in-dimension Friedlander–Iwaniec beta sieve and Landau–Page-deleted Siegel–Walfisz ledger explicit.
- Updated the abstract, introduction, §50 frontier, internal pedigree, and bibliography. Verifier blocks `(ax)`–`(az)`, all three hostile reviews, and the §51 adjudication are registered without promoting internal review to external validation.
- Cleared the v6 queue: source §§51–53 are now absorbed.

## v5 changes — 2026-08-29, wave 18

- Absorbed source §49's exact implication criterion, pointwise antichain void identity, failure of a uniform residue profile, and complete-bipartite semiprime grid. The grid refutes both repaired hierarchy (47.16) and the ordinary factorial-moment target for the reduced count, with the full every-even-`m`, pairwise-coprime squarefree, extension-ratio-one, and conditional CRT-cost quantifiers retained.
- Reclassified the complete-system hierarchy/moment axis as **DORMANT**. The nested cube remains the refutation of the raw formulations; the grid is the separate collective refutation of their antichain replacements. Proposition 47.3's prime-only rung survives, while `H_PF'`, (33.16), (37.27), and (40.19) remain open.
- Added source §50 as a new conditional pointwise section: the proved one-prime-factor slice criterion and explicit Type-I reconstruction, bespoke unproved `H_SPF(A)`, its conditional consequence, prime-norm and bounded-core walls, the GRH active-slice-only theorem, the GRH/Chebotarev mass audit, exact genus pairing, Duke assessment, frontier table, and exact finite census.
- Preserved the section's scope: §50 is a conditional reduction and map of missing input, not an unconditional theorem. The provisional record labels, source §39.7 qualifications, Vaughan-access warning, Pomerance–Weingartner comparison limits, and internal-only verification register are unchanged.
- Extended the internal pedigree with the hostile §49 and §50 reviews, updated the abstract/introduction/status register, and regenerated the tracked table of contents.

## v4 changes

- Promoted source Theorem 43.12 to the abstract, introduction, and general-`m` headline. Its proof includes the finite relative-mass inequality (43.36), thinned quarantine and Bonferroni degree, `O(Mt)` ledger, full `m <= (log N)^(3-epsilon)` audit, and uniform semigroup transfer. Source Theorem 43.8 remains as the one-sentence conservative linear-thinning variant.
- Replaced the old Pomerance–Weingartner comparison by the adjudicated scales `R=(eta_2/phi)^(1/4)L^(3/4)` and `P=L^(2/3)/phi^(1/3)`, exact ratio/crossover (43.33)–(43.34), common-domain comparison, and separate `L^(3-epsilon)` range discussion. Layer 1 now has its repaired all-denominator range `m <= L^(2-epsilon)`.
- Extended the verification pedigree with the source §43.11 attested-blind protocol, freeze commit, convergence/divergence scope, and hostile strengthening adjudication. It remains explicitly internal.
- Added the §47 nested squarefree divisor cube. It refutes literal raw targets (40.28) and (37.19), not `H_PF'`, pair target (40.19), or the conjecture. The implication antichain preserves the void, and (47.16) is the exact replacement **OPEN** wall.
- Extended the endpoint frontier from Theorem 45.9’s injective `W_0` prefix to `W_1 ~ L^5 loglog L/(log L)^2` and the wedge `c >= z, m <= zW_1`. The distinct-cell collision sum (46.13) is the exact current **OPEN** pair remainder.
- Added source Theorem 48.1 in full, the fixed-divisor law (48.16)–(48.17), residue-one escape (48.20), and the finite depth census. Pointwise Type-I existence remains the conjectural target; no progress claim is made.
- Updated the abstract/frontier/status register, compacted already-resolved bibliography entries without adding citation keys, and regenerated the tracked table of contents.

## Wave-17 v4 fidelity review

- Review: `reviews/wave17-paper-v4-review.md`; verdict **FAITHFUL-AFTER-REPAIRS** after minimal source-§49 status corrections; two-pass build clean.
- wave-17: the antichain hierarchy is also refuted (notes §49); the pending paper absorption is resolved in v5.

## Resolved v3 errata

The pending v4 structural erratum in the wave-16 fidelity review was resolved in v4: raw (37.19) and literal (40.28) were no longer called open, and implication-antichain (47.16) was identified as the then-current repair. V5 now absorbs source §49's later refutation of that repair and of the reduced-count moment itself. The review’s “do not insert an unadjudicated strengthening” guard remains resolved correctly: only the hostile-adjudicated Theorem 43.12 is promoted, with every provisional label retained. The post-freeze Layer-1 all-denominator range correction and the §46 endpoint refinement remain incorporated.

## Statement fidelity

Every new or changed theorem statement was diffed against the post-review `notes.md` text symbol by symbol:

- notes §70 status, Lemma 70.1, Corollaries 70.2–70.4, and (70.1)–(70.5) ↔ `a-frame-failure`, `a-frame-involution`, `quadratic-confinement`, `prime-F2-empty`, and `F1-F3`: exact fixed-prime/unit hypotheses, unique-involution equivalence, quadratic confinement, F2 emptiness, F1/F3 disjoint decomposition, and the `a=7,h=17` budget warning agree.
- notes Standard Fact 70.1, Theorem 70.5, and (70.6)–(70.14) ↔ `integer-confinement`: the progression-compatibility caveat, fixed-mark bound, exact constants, all five hard-class ratios, tied-twist warning, and strictly positive fixed-`a` asymptotics agree.
- notes Lemma 70.6, Theorem 70.7, Corollary 70.8, and (70.15)–(70.23) ↔ `budget-rigidity`, `fixed-modulus-budget`, and `integer-failure-law`: inversion-orbit budget, forbidden correction class, exact `K_a` and `beta_a`, lower-order F3 ratio, hard progression, and nonuniformity in `a` agree.
- notes Standard Fact 70.2, Theorem 70.9, and (70.24)–(70.28) ↔ `prime-frame-upper`: primitive two-form hypotheses, fixed-`K` sieve, effective `N/(log N)^(3/2)` law, sharper F3 exponent, fixed-progression extension, and no prime-frame lower bound agree.
- notes Theorems 70.10–70.11 and (70.29)–(70.35) ↔ `composite-confinement` and `congruence-wall-free`: cyclic `2^k` quotient classification, exact kernel count, `2^(omega(a)-1)` quadratic term, `a=15` counterexample, unit compatibility, density-one success, and fixed-only perimeter agree.
- notes Computational/Heuristic 70.1 and (70.36)–(70.39) ↔ the finite replay and outlook: every count, finite gate, `ES_FULL_SCAN` scope, composite extrapolation warning, distinct all-coefficient/prime-only models, and complete no-joint-tail register agree.
- notes §71 status, Lemmas 71.1–71.2, and (71.1)–(71.7) ↔ `fixed-J-stacking`, `prime-a-separation`, and `a1-count-below-one`: prime-only selection, exact F1/F3 separation, one-excluded-class majorant, admissibility cutoff, integer-frame enlargement, endpoint covering sequence, and no congruence-wall transfer agree.
- notes Facts 71.1–71.3 and (71.8)–(71.15a) ↔ the quotation subsection: Shiu pp. 162–163, Nair–Tenenbaum pp. 123–126, and Henriot pp. 4–8 are retained as explicit verbatim quotations; every fixed-dimension, range, discriminant, prime-density, and dependency sentence agrees, with no claimed growth rate for `C(J)`.
- notes Theorem 71.3, Corollary 71.4, and (71.16)–(71.28) ↔ `fixed-J-means` and `fixed-J-tail`: both indicator means, prime-input factor, exact Euler deficits, discriminant table (71.24), all six exponent fractions, F1-only warning, and weaker-than-standing-literature assessment agree.
- notes Lemma 71.5, Heuristic 71.1, and (71.29)–(71.36) ↔ `local-confinement-factor` and the local model: exact collision set, coprimality deletion, boxed local factor, table (71.32), all three heuristic scales, and no-tensorization caveat agree.
- notes `H_FAIL`, `H_STACK`, Theorem 71.6, Fact 71.4, Assessment 71.2, and (71.37)–(71.47) ↔ `H-FAIL`, `H-STACK`, and `moving-J-tail`: both hypotheses’ exact displayed forms, effective constants, gamma branches, conditional comparison thresholds, Pomerance–Weingartner statement, `Z>(4+o(1))L` correction, finite crossover, falsification register, and no-unconditional-record conclusion agree.
- notes §72 status and (72.1)–(72.6) ↔ `a-frame-census` method, four-window panel, and dependence panel: exact half-open ranges, populations, every F1/F3/INFO cell, all 15 joint rows, and no scale or independence claim agree.
- notes (72.7)–(72.12) ↔ the third-decade census and anatomy: all 20 histogram counts, total 719781, unique maximum and deep values, complete upper tail, eight strict-record rows, every sigma count, digest, F3 shares, all omega-conditioned cells, timings, memory, gates, and no-asymptotic/no-pointwise wall agree.
- notes §69 status, definition, Lemma 69.1, and (69.1)–(69.4) ↔ `forward-ray` and `integerwise-collapse`: maximal rational integer-valued scope, sufficiently-large tail, nonzero divisor values, integer-valued quotient on every integer, resultant bound, and no coefficient-wise `Z[t]` claim agree.
- notes Lemma 69.2 and (69.5)–(69.7) ↔ `shadow-blockage`: both polynomial identities and integer-valued cofactors, exact `M(0) <= -1` or `D(0) < 0` alternatives, zero-divisor edge, and no standalone eligibility failure agree.
- notes Lemma 69.3, Theorem 69.4, and (69.8)–(69.10a) ↔ `positivity-propagation` and `forward-ray-obstruction`: both forced-sign arguments, nonzero premise, original-anchor induction, all three Theorem-60.3 anchors, every degree, every `K >= 1`, every tail start, and constant-`M` edge agree.
- notes (69.11)–(69.15) and Computational 69.1 ↔ the constant-divisor classification and block `(bp)` register: exact three finite differences, 19-period panel, 57 rows, all syntactic totals, bound-500 and bound-5,000 ledgers, 5,792,112 zero-hit candidates, 65-class `445/1,709/0` projection, collapse examples, shadow check, runtimes, and bounded-regression-only caveat agree.
- notes §69.4 ↔ the consequence and honest walls: polynomial witness families only; pointwise and polynomial divisibility both covered; no degree, period, or tail-start restriction; arbitrary non-polynomial, piecewise-polynomial, and unanchored rays untouched; no new infinite value, `W(2m²)` classification, quantifier exchange, or evidence for `C_SQ′` agree.
- notes §69.5 ↔ the local and global `(bp)` pedigrees: every critical/high repair, independent bound-500 and bound-5,000 replay, 50,000 seeded rows, 65-class projection, full-suite time/memory, **SOUND-AFTER-REPAIRS** verdict, and internal-only status agree.
- notes §66 status, Theorem 66.1, Lemma 66.2, and (66.1)–(66.6) ↔ `escape-cylinders`, `twisted-class-decidability`, and `class-period`: exact squarefree/real-depth quantifiers, empty-lcm convention, finite union, prime-power iff, theta decomposition, effective `2/3` scale, and no-new-infinite-member boundary agree.
- notes Theorem 66.3, Corollary 66.4, and (66.7)–(66.9) ↔ `twisted-family-unbounded` and `family-certificate-ceiling`: all three anchors and classes, every-`X` density count, limsup quantifiers, finite-fixed-harvested-law scope, and distinction from the §56 certificate architecture agree.
- notes Proposition 66.5 and (66.10)–(66.14) ↔ `anchored-identity-wall` and Computational 66.1: exact integer-valued/positivity eligibility, all-degree anchor specialization, forward-ray positivity leak, all twelve `(K,e)` families, three shapes, 54,990/6,810 totals, and no hidden coefficient cutoff agree.
- notes Computational 66.2–66.3 and (66.15)–(66.20) ↔ the projection, censuses, and honest walls: 287 digits, exact logarithm, 65/562 classes, lift maximum and digest, all survivor/maximum/where rows, depth-1000 exceptions, cap caveat, changing-class quantifier, and open `C_SQ'` status agree.
- notes §66.6 ↔ local and global `(bm)` pedigrees: `2/3` recomputation, all finite independent replays, exact forward-ray repair, deterministic Python-integer scope, and **SOUND-AFTER-MINOR-REPAIRS** internal-only verdict agree.
- notes §67 status, (67.1)–(67.4), and Computational 67.1 ↔ `record-stall`: exact 50-law profile, integer-supremum/infinity convention for `tau`, `M>4D` diagnostic scope, `D<p/8` exhaustion, `tau(193)=infinity`, every top-ten row/depth/profile, four-shift factor, and nonmonotonicity statement agree.
- notes Computational 67.2 and (67.5)–(67.6) ↔ the residue-one subsection: full lcm rather than eligible-only modulus, all four `(T,M,k,p,W,W-T,a_1)` rows, strict guarantee, logarithmic-column scope, and no improved Linnik estimate agree.
- notes Heuristic 67.1 and (67.7)–(67.11) ↔ the fragile-spacing subsection: every class input and calibration row, deliberately false independence, exact raw/calibrated probabilities and expectations, proxy population, formal Poisson mass, and explicit no-evidence/no-tail/no-next-record register agree.
- notes Computational/Assessment 67.3 and (67.12)–(67.13) ↔ the empirical-exponent subsection: all 15 rows, natural logarithms, exact `2.923244`, sufficiently-large quantifier, every `A >= 1` open, “1–2” finite-normalization-only gloss, and no eventual-limsup inference agree.
- notes §§67.5–67.6 ↔ local and global `(bn)` pedigrees: default/gated ranking scope, bounded-memory method, all-record `a_1/tau` vectors, exact toy recomputation, **SOUND-AFTER-REPAIRS** verdict, and no-growth/no-pointwise perimeter agree.
- notes §68.1 and (68.1)–(68.3) ↔ `PW-v2-audit`: exact Theorems 1.1–1.4 quantifiers, exponents, thresholds, all-denominator/prime distinctions, Type-I/Type-II admitting classes, finite-versus-theorem scope, and no-effectivity-claim wording agree.
- notes §68.2 and (68.4)–(68.6) ↔ range consistency and crossover: fixed-gap algebra, both exception regimes, repaired §55 fixed-`B > 3` entry with vanishing masses, exact `eta_2/phi/L` powers, unknown-constant caveat, and inherited **CLAIMED/PROVISIONAL** status agree.
- notes §§68.3–68.4 ↔ the priority, Vaughan, bibliography, version, and `(bo)` registers: all four source-bounded no-threat verdicts, five secondary Vaughan descriptions, complete 13-item sweep, Gottschlich/Nakayama registration, v1 content-not-binary identity, access-log limits, **CONFIRMED AFTER REPAIRS** verdict, and no full-literature-certification caveat agree.
- notes §63 status, Lemmas 63.1–63.2, Corollary 63.3, and (63.1)–(63.7) ↔ `witness-taxonomy`, `DIV-family`, `D1-family`, and `square-root-law`: exact hard-prime context, all range endpoints, paired `D=1,h^2` witnesses, complementary-factor choice, and square-root bound agree.
- notes Theorems 63.4–63.5 and (63.8)–(63.16) ↔ `fixed-D-laws` and `universal-a-law`: if-and-only-if divisor conditions, squarefree and `D=4` branches, all four fixed-`D` rows, primitive-root vectors, bounded valuations, and one shared exponent across every CRT component agree.
- notes Corollary 63.6, Theorem 63.7, Corollary 63.8, and (63.17)–(63.24) ↔ the coverage subsection: empty `a=3` branch, exact two-class sieve, `O(rho(d))` remainder, effective dimension `3/2`, explicit exceptional set, four late factorizations, and weaker-on-both-axes comparison agree.
- notes Computational 63.1–63.3 and (63.25)–(63.33) ↔ the first-index and pedigree subsections: `a_1`/`a_W` definitions, both exact populations and histograms, all maxima/correlations/ratios/differences, four late rows, no-asymptotic and no-hidden-positivity walls, gated scope, and block `(bj)` review pedigree agree.
- notes §64 status, Theorem 64.1, and (64.1)–(64.3) ↔ `gcd-mechanism` and `cancellation-cover`: exact quotient-row box, empty-set convention, eligibility-failure valuation window, gcd support inside `n`, unit-row consequence, and necessary-versus-sufficient boundary agree.
- notes Theorem 64.2, Corollaries 64.3–64.4, Theorem 64.5, and (64.4)–(64.10) ↔ the shifted-law and unit-branch subsections: all-`n` quantifiers, exact support alternatives, six dyadic exclusions, two Legendre-symbol roots, `q=3` specialization, odd composite unit hypothesis, and no nonunit claim agree.
- notes Computational 64.1 and (64.11)–(64.12) ↔ the complete ledgers: every gcd and failed-prime multiplicity, totals 43/65/188, exact support unions, 400 unit branches and zero unit rows for 4545, and input-specific rather than family-wide diagnosis agree.
- notes Assessment/Heuristic 64.1 and Computational 64.2–64.3 ↔ the finiteness and hunt subsections: all open walls, heuristic-only assumptions, 64978-class product, exact 146016/242837/388853 box counts, prefilters, `W(3201660)=5303` datum, default box, thin `10^9` slice, right-to-left-only `C_SQ'`, and no-`C_SQ''` clause agree.
- notes §64.6–§64.7 ↔ the local and global `(bk)` pedigrees: Python-integer and streaming scope, every review count, independent full hunt, **SOUND-AFTER-REPAIRS** verdict, and no-growth/no-classification perimeter agree.
- notes Computational 65.1 and (65.1)–(65.2) ↔ `two-decade-census` and the strict-record ledger: exclusive `p<10^8` scope, 719781 primes, 7500 rows, 244216 classes, all 15 records, selected-least-`D` convention, empty post-`10^7` record list, and zero square-root-prediction violations agree.
- notes Computational 65.2 and (65.3) ↔ the parity/histogram subsection: exact 49975/32912 split and percentages, intrinsic 49975/32454/458 split, every interval count and percentile, 67 occupied moduli, and no-distribution-law clause agree.
- notes INFO 65.1 and (65.4) ↔ the blockwise table: all 21 populations and both six-decimal normalized columns, clipped endpoint, local-versus-strict-record distinction, and global suprema 171.783468/64.198698 agree.
- notes Computational 65.3 and §65.5 ↔ the replay and review pedigree: block `(bl)` default/full distinction, historical transient-runner limitation, committed independent full replay script, explicit leftover assertion, memory scope, **SOUND-AFTER-REPAIRS** verdict, INFO-only status, no growth law, and `H_MOD` untouched agree.
- notes §62 status, Theorem 62.1, and (62.1)–(62.8) ↔ `ratio-spectrum` and `thm:ratio-spectrum`: exact coprimality hypothesis, bounded exponent spectrum, hard-prime and `a` quantifiers, divisor pairing, reconstruction, automatic eligibility, and `W(p)` minimization agree.
- notes Theorem 62.2 and (62.9)–(62.16) ↔ `small-a-laws`: all inverse-paired class rows, exact laws at `3,7,11,15,19,23`, ten mod-11 minimal budgets, four mod-15 rows, finite-log proof, repeated-prime budgets, and the full `a=7,h=17` multiplicity failure agree.
- notes Assessment 62.1 and (62.17)–(62.18) ↔ the first-layer density paragraph: contextual-only Landau–Selberg–Delange status, all six checked counts, all six exact failure counts, and Computational-only finite scope agree.
- notes (62.19)–(62.21), Assessment 62.2, and Heuristic 62.1 ↔ the finite-conspiracy subsection: exact all-`a` equivalence, exhibited-mechanisms-only honesty clause, model-only independence product, shared-shift/shared-factor caveats, and no-tail/no-pointwise perimeter agree.
- notes Computational 62.1 and (62.22)–(62.24) ↔ the late-resolution and composite ledgers: every table digit, all fixed-`a` outcomes, every displayed budget vector, small-`a`/large-`M` distinction, and exact nonunit/gcd/eligibility diagnosis agree.
- notes Computational 62.2 and (62.25)–(62.26) ↔ the staged hunt: exact coordinate-box rather than full-interval scope, 607/146016 counts, empty deeper stages, exact maximum and witness tuple, default slice, optional gate, right-to-left-only `C_SQ'` status, and no-`C_SQ''` clause agree.
- notes Computational 62.3 and §62.7 ↔ the local and global pedigrees: 500 seeded unit pairs, every unit `h <= 10^5`, all 1181 hard primes, 27107184 tested rows, exact maximum/sum, bounded Python-integer state, independent hunt replay, **SOUND-AFTER-REPAIRS** verdict, and internal-only status agree.
- notes §61 status, Lemma 61.1, and (61.1)–(61.3) ↔ `decidable-census` and `forward-normal-form`: proved/Computational separation, exact simultaneous bounds, positivity and divisor-table arguments, both census endpoints, tuple counts, memory gate, two-method overlap, and all-hard-prime cross-check agree.
- notes Theorem 61.2 and (61.4)–(61.6) ↔ `twisted-square-criterion`: finite if-and-only-if, all four automatic conditions, gcd cancellation warning, even-`D` coverage, exact near-miss supports, and no-family diagnosis agree.
- notes Theorem 61.3 and (61.7)–(61.8) ↔ `two-square-layers`: exact `W=3` and `W=11` equivalences, root sets `±2,±3,±4 (mod 11)`, conditional `W=19` classes `±3,±6,±8 (mod 19)`, and every smaller-modulus exclusion agree.
- notes Computational 61.2 and (61.9)–(61.11) ↔ the complete twisted-square box: 3630/3628 counts, two vanishing pairs, exact histogram, digest scope, explicit `s=505` outside-box control, and no unbounded-classification claim agree.
- notes Theorem 61.4, Corollary 61.5, and (61.12)–(61.15) ↔ `hard-prime-criterion` and `prime-third-mechanism`: exact hard-prime quantifiers, automatic coprimality, all formulas, even-`D` sufficiency, minimum convention, the two unavailable mechanisms, and exact no-claim assessment agree.
- notes Heuristic 61.1, Computational 61.3, and (61.16)–(61.17) ↔ the prime diagnostics: Heuristic label, nonindependence warning, all composite mass/row counts, all-3202-prime replay, 1941 even-`D` minima, later prime table, §54 instance, and no asymptotic-law claim agree.
- notes §61.4–§61.5 ↔ the scope and `pedigree`: every default/optional gate, all-`n <= 5000` independent original replay, both exact seeded samples, optional million replication, twisted-box replay, exact-ceiling incidence and memory bounds, **SOUND-AFTER-REPAIRS** verdict, and internal-only status agree.
- notes §60 status and (60.1)–(60.4) ↔ `witness-duality`: complete harvested-datum scope, inverse maps, positivity, and the distinction from a new identity family agree.
- notes Theorem 60.1, (60.5)–(60.12) ↔ `witness-duality`: exact cancellation, `gcd(a,D) | n`, prime-adic and 2-adic caveats, canonical normal form, all four finite bounds, and the no-swap derivation agree.
- notes (60.13)–(60.13a) ↔ the three specialized reductions: oddness, quotient and uncancelled checks, all §59 necessary filters, precise cancellation primes, and exact `a` bounds agree.
- notes Lemma 60.2, (60.14)–(60.15) ↔ `witness-involution`: bi-eligibility if and only if, genuine involution scope, examples and counterexample, and forced `n = 1 mod 4` agree.
- notes (60.16)–(60.19) and Theorem 60.3 ↔ the survivor-frontier subsection: exact two-front union, finite ceilings, no hidden middle regime, two exhaustive normal-form certificates, and computer-assisted status agree.
- notes (60.20a)–(60.22) ↔ the scope, near-miss ledger, and repaired conjecture: explicit Egyptian fractions, gcd-structural failures, four `288` gcds equal to 9, failed character route, heuristic-only comparison, refutation of `C_SQ`, and only right-to-left proof for open `C_SQ'` agree.
- notes (60.23)–(60.25) ↔ the statistic/prime subsection: terminating algorithm, exact divisor-work sum and average order, odd-prime gcd redundancy, separate `p=2` datum, and every no-tail/no-Erdős–Straus caveat agree.
- notes §60.5–§60.6 ↔ the verification ledger and `pedigree`: bounded replay, two-front double count, swap counts, exact independent ceilings and incidence counts, memory bound, optional historical scan, and **SOUND-AFTER-REPAIRS** internal-only status agree.
- notes §59 status and Definition 59.1 ↔ `polynomial-escape` preface and `uniform-polynomial-escape`: proved versus Computational versus Conjectural labels, eventual positivity and threshold, positive-degree exclusion, square examples, and independence from Theorem 34.8/§39 agree.
- notes Lemma 59.1, (59.1)–(59.4) ↔ `polynomial-local`: exact rounded radical, complete harvested-congruence equivalence, both tail directions, progression compatibility modulo `(M,q)`, finite-depth separation, and fixed-progression `D=1` hit agree.
- notes Theorem 59.2, (59.5)–(59.9) ↔ `cyclotomic-obstruction`: every fixed shift, prime eligibility, root-field intersections, both Chebotarev directions, all-but-finitely-many perimeter, `Q(i)` specialization, root-field-not-splitting-field warning, `X^4-3` replay, and qualitative **ineffectivity** agree.
- notes Theorem 59.3, (59.10)–(59.15) ↔ `quadratic-escape`: no linear escapes, leading-coefficient choice, `a>0`, reducible/zero and all discriminant-sign cases, coefficient-dependent `q`, exact conductor exclusion, integral square-root divisibilities, converse, and all three finite replays agree.
- notes `C_POLY` and Corollary 59.4 ↔ `C_POLY` and `polynomial-primes`: higher-degree classification remains open; every classified positive value is `1` or composite; the unconditional conclusion is polynomial-family-only through degree two, with every named outside family retained.
- notes Proposition 59.5, (59.16)–(59.19) ↔ `integer-tail-obstruction`: moving square count, exact interior crossing, every `theta>1/3`, endpoint `cb^3>1/2`, equality caveat, and no-earlier-obstruction disclaimer agree.
- notes `C_SQ` and Lemmas 59.6–59.7, (59.20)–(59.22) ↔ the complete-square and twisted-square subsections: exact set equality, `C_SQ =>` Erdős–Straus direction only, strict-strength explanation, `C_SQ => C_POLY`, Schur/Gauss proof, Jacobi sign, `s` not dividing `D`, scaling/lift conditions, and all three candidate-specific classes agree.
- notes Computational 59.8, (59.23)–(59.27) ↔ the survivor census: all nonsquare counts, the three factorizations, default and deep frontiers, 2,878,826,874 streamed values, Python-integer/<170 MB ledger, explicit overflow-artifact rejection, optional million endpoint, 643245 witness, all family histograms, 177/180 control result, and no-infinite-escape/no-positive-evidence warning agree.
- notes §59.6 review attestation ↔ `pedigree`: every high/medium/low repair, block `(bf)` scope, and **SOUND-AFTER-REPAIRS** verdict are retained as internal review only.
- notes §57 status and (57.1) ↔ Section 19 preface: `H_WIN`/`H'_WIN` are unproved, fixed-polylog use retains the §39 qualification, cubic use inherits **CLAIMED/PROVISIONAL** Theorem 34.8, the realized common exponent is only `1/4`, and the full counterexample-prime containment through `W=+infinity` agrees.
- notes Theorem 57.1, (57.2)–(57.7) ↔ `count-below-one`: fixed constants and moving-window uniformity, cubic `theta > 1/3`, square-log `theta >= 1/2`, all three cubic endpoint-constant cases, effective thresholds, dyadic coverage, and present-window calibration agree.
- notes Proposition 57.2, (57.8)–(57.15) ↔ `mass-gap`: source §18.2/(18.15)/Assessment 18.4, Lemma 33.3, and (51.11) antecedents; formal `AR(mu,t)` scope; exact versus sufficient fixed-margin inequalities; `a/(a+1)` ceiling; and Assessment-only general no-go language agree.
- notes `H_XW`, Proposition 57.4, `H_EQ`, (57.16)–(57.21) ↔ the crossing subsection: fixed-family/error-function quantifiers, one-sided remainder, factor-two proof, dyadic coverage, pair-endpoint localization limits, cylinder scope, and §54 subcritical consistency agree.
- notes Computational 57.6–57.7, (57.22)–(57.24) ↔ block `(bd)` register: exact mass/tail table, square explanation, endpoint replays and surrogate-only warnings, toy lcm table, and informational scope agree.
- notes moving convention (58.1)–(58.3) ↔ Section 20.1: raw inverse corruption, distinct `L_int`/`L_p`/`L_h`, exact `22621` versus `1853329` warning, and both directions of the complete divisor harvest agree.
- notes Theorem 58.1, (58.8)–(58.10) ↔ `square-escape`: `W(m^2)=+infinity` for every positive integer, the full common-factor/nonunit/2-adic/prime-power proof, the global Jacobi sign and `(15,2)` local warning, strict definitional lower bound, square upper bound, residue-one integer bound, and effective all-prime/hard-prime Linnik bounds agree.
- notes Computational 58.1, (58.4)–(58.7) ↔ the inverse census: every default and optional row, witness brackets, hard-prime plateau, natural-log normalization, step-function warning, and no-growth-law scope agree.
- notes Lemma 58.2 and Corollary 58.4, (58.11)–(58.12), (58.16)–(58.17) ↔ `shifted-sieve` and `integer-prime-dichotomy`: both shifts, contextual-only Selberg–Delange calculation, exact moving square count, near-linear interpretation, and prime-essential conclusion agree.
- notes Theorem 58.3, (58.13)–(58.15) ↔ `jacobsthal`: literal `k >= 2`, all-`k` `log(2k)` form, absolute nonexplicit constant, archived secondary-source provenance, inaccessible primary disclaimer, one-way subsystem inclusion, composite-class obstruction, and maximal-gap/first-survivor distinction agree.
- notes Assessment 58.1, (58.18), and Lemma 58.5, (58.19)–(58.20) ↔ the prime-survivor and inverse-duality subsections: parity/distribution audit, proved exponential prime upper end only, liminf rather than naive global `o(T)`, both inverse substitutions, and exact `A`-window restatement agree.
- notes §57.5/§58.6 review attestations ↔ `pedigree`: every high/medium repair, `(bd)`/`(be)` scope, memory-bounded/chunked verification, exact finite replay counts, and secondary-source attestation are retained as internal review only.
- notes Theorem 56.1, (56.1)–(56.3) ↔ `typeII-certificate`: prime and nonreduced all-integer certificate scopes, eventual quantifier, exact `P_3(T)` divisibility, effective `(1/2+o(1))T` constant, literal `D=1` multiplier datum, CRT/Dirichlet proof, and the explicit no-full-lcm/no-constant-`1` limitation agree.
- notes Theorem 56.2, (56.4)–(56.7) ↔ `typeI-certificate`: reduced hard-class definition, every prime core `5 <= ell <= T`, `theta(T)-log 6`, nonresidue refinement, reciprocity computation, admissibility, Corollary 52.2 application, and additive-not-multiplicative primitivity warning agree.
- notes (56.8)–(56.9) and Assessment 56.2a ↔ `certificate-Linnik`, `GRH-certificate`, and the congruence-wall paragraph: certified-prime finite-prefix repair, exact `1/(alpha L)` algebra, Type-II/Type-I coefficient ceilings, §54 saturation claims, conditional GRH label, and architecture-only perimeter all agree.
- notes Computational 56.3–56.4, (56.10)–(56.15) ↔ the two census subsections: all endpoint counts, strict records, full-scan extensions, natural-log maxima, exact-minimum scope, INFO-only register, no-growth-law warning, and the repaired linear resident-memory description agree.
- notes §56.5, (56.16) ↔ `remaining-window` and revised (54.12): the pointwise lower wall and open range are separated from the overlapping finite-search panel; `lesssim 2` is neither a bound nor a conjectured exponent, and the certificate ceilings do not alter the pointwise frontiers.
- notes Theorem 54.1, (54.1)–(54.5) ↔ `W-lower` and `MOD-frontier`: full-lcm scope over every `k*ell`, effective Xylouris exponent `5.2`, unbounded selected primes, limsup constant `1/5.2`, every `0<A<1` refutation, and the provisional upper-tail label all agree.
- notes Theorem 54.3, (54.6)–(54.10) ↔ `slice-lower` and `SPF-frontier`: squarefree-core genus forcing, every-slice vanishing, admissibility through `R(T)>4T`, effective Linnik quantification, `ck_pr`/`ck_min` scope, and every `0<A<1` refutation agree.
- notes §54 sandwich as refined by §56 ↔ the two-sided frontier: almost-all polylog-to-epsilon upper scale and effective logarithmic infinite lower scale are proved; the former logarithm-squared motivation is now retained only in §56's finite-search normalization panel, not promoted to a bound or limiting-exponent conjecture.
- notes Lemma 55.1 and Theorem 55.2, (55.1)–(55.13) ↔ `m-truncated` and `general-m-tails`: prime scope, `lambda_m`/`theta_m` masses, `t(1+M_i)` ledger, exact `(m,T,N)` windows, fixed-gap recoveries, and cubic **CLAIMED/PROVISIONAL** status agree.
- notes Lemma 55.4 and Theorem 55.5, (55.14)–(55.18) ↔ `m-Page` and `m-effectivity`: literal modulus `muv`, all three conductor cases, favorable sign, full-family/structured-fibre-only quantifiers, inequalities (55.17a)–(55.17b), unfavorable `k=1` handling, and ancillary-all-triples exclusion agree.
- notes (55.19)–(55.21) ↔ the PW and finite registers: formal crossovers are separated from the actual uniform window; proved/provisional status and unknown-constant caveats remain; block `(bb)` numbers and informational scope agree.
- notes Theorem 43.4, (43.13)–(43.15) ↔ `general-two-third`: unchanged exponent and local factor; both prime and all-denominator ranges are now exactly `m <= L^(2-epsilon)`.
- notes Theorem 43.8, (43.28) ↔ `general-three-quarter-conservative`: `eta_1(m)/phi(m)`, `L^(3/4)`, range `m <= L^(3/4-epsilon)`, primes and all denominators, and inherited status all agree.
- notes PW (43.32)–(43.34) ↔ paper (43.32)–(43.34): `R/P={eta_2(m)^3 phi(m)L}^(1/12)` and crossover `L >= 1/(eta_2(m)^3 phi(m))` agree; no old `eta_1` crossover or uniform-beating claim remains.
- notes Theorem 43.12, (43.35) ↔ `general-three-quarter`: `≪_epsilon`, `c_epsilon`, fourth root, `eta_2(m)L^3/phi(m)`, exact `3 <= m <= L^(3-epsilon)` range, prime/all-denominator scope, and all inheritance caveats agree.
- notes (43.36)–(43.42) ↔ the new proof: finite cutoff `K`, coefficient `(1-1/p)/p^e`, bound `H_m(K)/p`, fixed relative threshold, `M=eta_2(m)t^3/phi(m)`, `y,r=O(M)`, `O(Mt)` ledger, `t=alpha(L/theta_m)^(1/4)`, fixed-gap constraints, and semigroup `gamma` agree.
- notes §43.11 and Assessment 43.13 ↔ `pedigree` and the thinned-window preface: allowed reads, freeze hash, self-attestation limitation, S3/S6/S7 qualifications, adjudicated checks, verdict, and unchanged provisional status agree.
- notes Theorem 47.2, (47.10)–(47.14) ↔ `nested-cube`: squarefree top atom, `exp(cL/log L)` extension mass, conditioned raw-`H` moment failure for every fixed `C`, and the `Y`-to-`2Y` odd-subset mechanism agree.
- notes (47.16) ↔ `antichain-wall`: deletion direction, unchanged union/void, `Q_S`, `w_B`, every shared prime-power factor in `Gamma_S`, compatible-set quantifiers, even `m in [D Lambda,D Lambda+2]`, and `C Lambda` right side agree; it is retained historically and immediately refuted by the §49 grid.
- notes Theorem 49.1, (49.1)–(49.5) ↔ `implication-criterion` and `antichain-void`: distinct retained-atom scope, both implication equivalences, `M=tm` unpacking, survival hypotheses, inclusion-largest orientation, and pointwise conditioned void identity agree.
- notes Theorem 49.4, (49.8)–(49.11) ↔ `antichain-profile`: reduced-class scope, uniform-`C` negation, `g asymp X` strength, exact semiprime intervals and `D=2` retention, and `g^(1-o(1))` ratio agree.
- notes Theorem 49.5, (49.12)–(49.21) ↔ `grid-obstruction`: every fixed `C,D`, every sufficiently large `X`, every admissible even `m`, compatible pairwise-coprime squarefree `S`, exact extension ratio one, prime-supply ranges, `(2z)^(-2t)` CRT cost, and direct reduced factorial-moment failure agree.
- notes Computational 49.7 and Assessment 49.8 ↔ the distinct paper registers: finite fractions remain diagnostics, the two formulations alone are refuted, narrower open routes survive, and the complete-system moment axis alone is dormant.
- notes Theorems 50.1–50.2, (50.1)–(50.8) ↔ `one-prime-slice`, `SPF`, and `hyp:SPF`: exact good class, raw/nonprimitive boundary, explicit `e,a,b`, Type-I identity, fixed-`A` hypothesis quantifier, no bound on `q`, and all-large-hard-prime conclusion agree.
- notes Lemma 50.3 and Theorems 50.5–50.6, (50.9) ↔ `prime-norm`, `bounded-core`, and `GRH-active`: wrong-grade prime norm, every-fixed-`B` genus escape for all `k`, and GRH's unforced-slice-only conclusion agree.
- notes (50.10)–(50.17) ↔ the Chebotarev and genus-pairing audits: principal-ideal divisor condition, prime-qualified `1/8` mass envelope, heuristic-only (50.13), exact pairing, residual projector, and assessment—not independence-theorem—register agree.
- notes Computational 50.9, (50.18)–(50.20) ↔ the census: all 385 counts, eight records, `311/74` split, gap 55 witness, and informational-only optional maximum agree.
- notes Theorem 46.2, (46.8)–(46.10) ↔ `endpoint-wedge`: `W_1=floor(zL^2/log L)`, `W_2=floor(zW_1)`, full prefix, large-`c` wedge, and `O(Lambda^2)` conclusions agree. The preceding displayed diagonal/occupancy inequalities reproduce (46.3) and (46.9).
- notes Corollary 46.3, (46.11)–(46.13) ↔ `endpoint-core`: the sets `A,B`, ordered distinct-cell condition `m != m'`, congruence modulo `p`, weight `G_{m,p}G_{m',p}/p`, prime range, and equivalence to (40.19) agree.
- notes Theorem 48.1, (48.1)–(48.3) ↔ `moving-genus`: fundamental discriminant character, admissible hard-prime scope, implication `chi_s(p)=1 => M_{c,k}(p)=0`, exact set `{1,2,3,6}`, relative density `1/2`, and finite exclusions agree.
- notes Theorem 48.4, (48.15)–(48.17) ↔ `fixed-divisor-slice`: paper `L_d` is the notes’ local `L`; all three congruences, reduced-class and admissibility scope, explicit `e,a,b`, necessity within the fixed-`d` shape, and refinement clause agree.
- notes Theorem 48.5, (48.20)–(48.21) ↔ `slice-residue-one`: no residue one, bounded full-modulus union, `Lambda_Q`, infinite prime class, and factor-size contradiction agree.
- notes (48.8)–(48.14) ↔ the depth paragraph: `D=ck_min-1`, `385`, `77`, `(12289,76)`, `1181`, `103`, and `(92401,102)` agree and remain computational only.

The retained v3 correspondences were also rechecked after the edits:

- notes (43.2)–(43.3) ↔ `m-identity`, including positivity;
- notes (43.4), (43.6)–(43.9) ↔ `m-thinning`, including `eta_1`, `eta_2`, `C_2`, aggregate scope, and no `(uv,m)=1` assumption;
- notes (43.10)–(43.23) ↔ `m-class-mass`, `m-profiles`, and `m-pruned`, including the prime domain, product modulus `muv`, reduced-fibre quantifier, and `1/phi(m)`;
- notes (43.24)–(43.27) ↔ the unequal-prime-power moment replay and mixed local-factor correction;
- notes (44.3)–(44.16) ↔ raw slice vanishing, primitive caveat, `80/111`, `15/385`, and the retained `p=2521` datum;
- notes (42.1)–(42.17) and Theorem 45.9 ↔ endpoint uniqueness, collision law, fixed fibres, Kloosterman matrix, DFI/BC quantifiers, and `W_0` injectivity;
- notes §41.1–§41.5 and §34.5 ↔ all verification counts and internal-only caveats.

No statement discrepancy remains from this pass.

## Build and hygiene

Run from `paper/`:

```sh
pdflatex -interaction=nonstopmode espaper.tex
pdflatex -interaction=nonstopmode espaper.tex
```

The v17 build completes in 177 pages with zero TeX errors and no undefined references or citations. Generated PDF and auxiliary files are updated by the final validation passes. Manual source-style equation tags retain the pre-existing duplicate-destination `hyperref` warnings, which are not unresolved references. The control-byte scan of `espaper.tex` is zero; the v17-relevant verifier coverage passes through block `(bs)`.

## Submission TODO

- Obtain external expert review of Theorem 34.8, the §39 chain, and the full thinned-window §43 transfer.
- Obtain/read Vaughan 1970 and complete the priority search.
- Prove or disprove endpoint remainder (46.13); any revival of the dormant complete-system moment axis needs a genuinely new pointwise formulation.
- Obtain external expert review of the proved §49 and §50 theorem transcriptions and the §50 standard-hypothesis assessments.
- Settle author metadata and perform a final line-by-line referee audit.

## v18 queue

- v18 queue: source §§73–§74, being written in parallel; no claims from those sections are imported into v17.
