# Campaign discoveries (first curated draft)

This ledger records mathematical discoveries formulated by this campaign, rather than census tables, computational replays, or literature re-proofs. Labels are deliberately strict: **Theorem/Lemma/Proposition** means proved and reviewed; **INTERNALLY PROVED** means proved and hostile-reviewed internally, but not externally refereed; **Assessment/Heuristic** means model computation or interpretation; **CLAIMED/PROVISIONAL** and **OPEN/UNPROVED** are retained verbatim; **REFUTED/WITHDRAWN** records a superseded claim. A review path is included where the source states one. No entry is intended as a grade or priority claim.

## (A) Unconditional exceptional-set results

1. `E(N) ≪ N exp{-c(log log N)^2}` for exceptional primes. **Theorem** — notes §12.3, (12.7); review status not stated.
2. `E(N) ≤ N exp{-(log N)^{1/8}}` for all sufficiently large `N`. **Theorem** — notes §13.2, (13.1); review status not stated.
3. A proved k=1-certifying subsystem gives `#{P≤N:P≠4ABC−A−B}≪N exp{-c√log N}` (also for integer targets). **Theorem (proved)** — notes §32.2, §32 theorem; review status not stated.
4. `E(N) ≪ N exp{-(log N)^{2/5-o(1)}}` (indeed with an extra `log log N` in the exponent). **Theorem (proved)** — notes §14.3–14.4, Thm 14.4; review status not stated.
5. `E(N) ≪ N exp{-(log N)^{θ*−o(1)}}`, `θ*=log 3/(1+log 3)=0.523494…`. **Theorem (proved)** — notes §14.6, Thm 14.9; review status not stated.
6. `E(N) ≪ N exp{-c(log N)^{2/3}(log log N)^{1/3}}` for exceptional primes. **Theorem** — notes §16.4, Thm 16.4; paper/vaughan-loglog-note.tex, Theorem 1.1; `reviews/vaughan-loglog-note-review.md` CORRECT-AFTER-REPAIRS.
7. The same `2/3`-with-`loglog` bound holds for all exceptional denominators by the exceptional-prime semigroup transfer. **Theorem (all exceptional denominators)** — notes §16.5, Thm 16.5; paper/vaughan-loglog-note.tex, Theorem 1.2; `reviews/vaughan-loglog-note-review.md` CORRECT-AFTER-REPAIRS.
8. Fixed-polylogarithmic witness tail: `#{p≤N:W(p)>T} ≪ N exp{-c(log T)^2 log(2+log T)}` under `log N ≳ (log T)^3 log log T`. **proved internally with the exact status below** — notes §51.1, Thm 51.2(1); status inherits the §39 moment/Bonferroni qualification.
9. Cubic witness tail: `#{p≤N:W(p)>T} ≪ N exp{-cκ(log T)^3}` when `log N ≳ (log T)^4`. **CLAIMED/PROVISIONAL** — notes §51.1, Thm 51.2(2); inherits Theorem 34.8 and §39.7.

## (B) The three-quarter chain

1. `𝓡(M)={−4D (mod M):D|((M+1)/4)^2}` and `(τ(A²)−1)/2 ≤ |𝓡(M)| ≤ τ(A²)`. **Lemma (proved)** — notes §18.1, Lemma 18.1; review status not stated.
2. The full intrinsic forced-class supply has cubic mass: `Σ_{M≤X,M≡3(4)}|𝓡(M)|/M ≍ (log X)^3`. **Theorem (proved)** — notes §18.1, Thm 18.2; review status not stated.
3. The multiplier identity `4/n=1/(suw)+1/(nsvw)+1/(nuvw)` from `kℓ≡3 (mod 4)`, `uvw=(kℓ+1)/4`, and `nv≡−u (mod kℓ)`. **Lemma (proved)** — notes §16.1, Lemma 16.1; paper/vaughan-loglog-note.tex, forced-classes section; review `reviews/vaughan-loglog-note-review.md` CORRECT-AFTER-REPAIRS.
4. Uniform lattice supply: the compatible `(u,v)` box has mass `Σ*1/(uv) ≍ (log z)^2 Σ φ(k)/k²`, with the matching `1/(φ(u)φ(v))` upper bound. **Lemma (proved)** — notes §16.2, Lemma 16.2; review status not stated.
5. The second incidence moment satisfies `Σ r_𝒥(u,v;c)^2/(uv) ≪ (log z)^2(1+log K)^3`. **Lemma (proved)** — notes §34.2, Lemma 34.7; review `reviews/wave32-sec76-review.md` SOUND-AFTER-REPAIRS (component rechecked in §76).
6. Congestion pruning preserves cubic prime-slice mass: `Σ f_c^good(ℓ)/ℓ ≍(log X)^2h(𝒥)`, hence `≍(log X)^3` for the full family. **Theorem (proved; CLAIMED/PROVISIONAL overall chain)** — notes §34.3, Thm 34.8; review lineage in `reviews/es-threequarter-note-review.md` and `reviews/wave31-sec73-review.md`, both SOUND-AFTER-REPAIRS.
7. The c-free factorial-moment/Bonferroni assembly gives `E_all(N)≪N exp{-c(log N)^{3/4}}`. **CLAIMED/PROVISIONAL** — notes §39.1–§39.7, Thms 39.4, 39.6, 39.7; paper/espaper.tex, Theorem 39.7; the original label remains provisional.
8. Weighted second-incidence simplification: `Σ 2^{ω(uv)}r²/φ(4uv) ≪(log z)^4(1+log K)^3`. **Lemma (proved)** — notes §76.1, Lemma 76.1; paper/es-threequarter-note.tex, Lemma 5.1; `reviews/wave32-sec76-review.md` SOUND-AFTER-REPAIRS.
9. Cauchy–Schwarz against Bombieri–Vinogradov gives the unpruned full triple-family supply, with the same cubic mass. **Theorem (proved)** — notes §76.2, Theorem 76.2; paper/es-threequarter-note.tex, Theorem 5.2; `reviews/wave32-sec76-review.md` SOUND-AFTER-REPAIRS.
10. The dependency graph shows the `3/4` exponent, cubic mass, Bonferroni degree, and `e^{O(t⁴)}` ledger survive removal of the pruning machinery. **Corollary (proved)** — notes §76.3, Corollary 76.3; paper/es-threequarter-note.tex, Corollary 5.3; review `reviews/wave32-sec76-review.md` SOUND-AFTER-REPAIRS.
11. The standalone bound `E(N)≪N exp{-c(log N)^{3/4}}` is now labelled **INTERNALLY PROVED; internal checks only, not externally refereed**. **INTERNALLY PROVED** — paper/es-threequarter-note.tex, abstract and Theorem 1.1; `reviews/es-threequarter-note-review.md` SOUND-AFTER-REPAIRS and `reviews/wave32-sec76-review.md` SOUND-AFTER-REPAIRS.

## (C) Structural theorems and reformulations

1. Complete criterion: `4/p` is solvable iff a Case-B divisor `d|((p+q)/4)^2` satisfies `q|d+(p+q)/4`, or the Case-A mirror does. **Theorem** — notes §3, Thm 3.1; review status not stated.
2. No guaranteed divisor-forced family, with any padding, covers even one prime class `p≡1 (mod N)` when `N` contains its modulus. **Theorem** — notes §5, Thm 5.1; review status not stated.
3. The reciprocity collapse identifies the Case-B character: `(d|q)=−(x|q)` for `x=(p+q)/4`. **Proposition (proved + verified)** — notes §8.2, Prop. 8.1; verify.py block `(h)`/section §8; review status not stated.
4. The Case-A mirror has the same p-intrinsic character landscape: `(r|m)=(r|p)` for prime `r|(pm+1)/4`. **Proposition (proved + verified)** — notes §9.1, Prop. 9.1; verify.py block `(h)`; review status not stated.
5. The complete Type-I/Type-II four-parameter parametrization is equivalent to the two criterion halves. **Theorem** — notes §17.1, Thm 17.1; review status not stated.
6. The two criterion halves share one quadratic bit: `(d_odd|p)=−(x_odd|p)` in Case B, so the apparent two-barrel independence is not character-level independence. **Proposition (proved)** — notes §9.2 and §10.2, Prop. 9.2; review status not stated.
7. Every forced class of the displayed identity shapes is escaped by a residue-one prime class; finite congruence-identity coverings therefore cannot settle ES. **Theorem** — notes §17.3, Thm 17.3; review status not stated.
8. The complete-system avoider density is bounded below at the cubic scale, so the original `H_PF` cubic partition-free target is false. **Theorem (proved)** — notes §31.1–§31.4, Thm 31.4; review status not stated.
9. Every fixed slice has a genus obstruction, but no further identically zero slice occurs in the small-box classification; fixed-divisor slices have residue-one escapes. **Theorem (proved)** — notes §48, Thms 48.1, 48.4, 48.5; review status: FAITHFUL-AFTER-REPAIRS (paper v4).
10. The exact atom implication criterion is a divisor-poset relation, and a complete bipartite semiprime grid refutes the reduced hierarchy and reduced factorial-moment target. **Theorems (proved)** — notes §49, Thms 49.1, 49.5; review status not stated.
11. A one-prime-factor slice criterion gives a conditional Type-I route, while prime norms have the wrong quadratic grade. **Theorem/Lemma (proved); bespoke hypothesis unproved** — notes §50, Thms 50.1–50.3; review status not stated.
12. Every square escapes the complete harvested witness system: `W(m²)=+∞`; the moving integer inverse obeys `T<L_int(T)≤T+2√T+1`. **Theorem (proved)** — notes §58.1, Thm 58.1; review SOUND-AFTER-REPAIRS.
13. Polynomial uniform escapes face a root-field/cyclotomic obstruction in every degree, with qualitative Chebotarev input. **Theorem (proved using qualitative Chebotarev; INEFFECTIVE)** — notes §59.1, Thm 59.2; review status not stated.
14. Uniform polynomial escapes of degree at most two are exactly polynomial squares; in particular there is no linear uniform escape. **Theorem (proved)** — notes §59.1, Thm 59.3; review status not stated.
15. Every witness datum has the dual form `aM=4D+n`, and the canonical normal form gives `a,u≤2⌊(n+1)/3⌋`, `M≤8B²−1`. **Theorem (proved)** — notes §60.1, Thm 60.1; review status: SOUND-AFTER-REPAIRS (PROJECT.md Outcome 28).
16. For hard primes, `W(p)<∞` iff some `a≡3 (mod 4)`, `a≤2⌊(p+1)/3⌋`, has `D|((p+a)/4)^2` and `D≡−(p+a)/4 (mod a)`. **Theorem (proved)** — notes §61.2, Thm 61.4; review status not stated.
17. The exact divisor-ratio spectrum is `Rat_a(h)={∏_{q|h}q^{f_q}:|f_q|≤v_q(h)}`; witness existence is `−1∈Rat_a(h)`. **Theorem (proved)** — notes §62.1, Thm 62.1; review status not stated.
18. Fixed-`D` laws and the universal `a`-law reduce success to one bounded-exponent divisor condition, with one shared CRT exponent across components. **Theorems (proved)** — notes §63.2, Thms 63.4–63.5; review status: SOUND-AFTER-REPAIRS (wave 27).
19. Quotient-row failure is exactly cancellation of eligibility at primes dividing the candidate; this is the gcd-supported cancellation-cover theorem. **Theorem (proved)** — notes §64.1, Thm 64.1; review status: SOUND-AFTER-REPAIRS (wave 27).
20. Integer-wise polynomial divisibility forces an integer-valued polynomial quotient, and positivity propagates backward; no polynomial witness family exists on the three anchored sporadic rays. **Lemmas/Theorem (proved)** — notes §69.1–§69.2, Lemmas 69.1, 69.3 and Thm 69.4; review status: SOUND-AFTER-REPAIRS (wave 29).
21. For prime `a≡3 (mod 4)`, failure splits exactly into quadratic confinement F1 and bounded-budget F3; F2 is empty. **Lemma/Corollaries (proved)** — notes §70.1, Lemma 70.1 and Corollaries 70.2–70.4; review status: SOUND-AFTER-REPAIRS (wave 30).
22. Fixed-`a` failure has integer scale `C_aH/√log H`, while F3 is lower order with exponent `1/2+1/(a−1)`. **Theorems (proved)** — notes §70.2–§70.3, Thms 70.5, 70.7, 70.8; review status: SOUND-AFTER-REPAIRS (wave 30).
23. Fixed-`a` failure among shifted primes is `≪_a N/(log N)^{3/2}`, and every compatible fixed progression has density-one success. **Theorems (proved, effective)** — notes §70.4 and §70.6, Thms 70.9, 70.11; review status: SOUND-AFTER-REPAIRS (wave 30).
24. Composite-modulus maximal avoiding subgroups are exactly kernels with cyclic `2^k` quotient; odd quadratic kernels alone are insufficient. **Theorem (proved)** — notes §70.5, Thm 70.10; review status: SOUND-AFTER-REPAIRS (wave 30).
25. The exact mechanism trichotomy is F1 / proper-even-subgroup CF3 / full-generation block BLK. **Lemma (proved)** — notes §73.1, Lemma 73.1; review `reviews/wave31-sec73-review.md` SOUND-AFTER-REPAIRS.
26. A target-pair exclusion bounds the F3 event by excluding a second residue class after one nonresidue class is present. **Lemma (proved)** — notes §74.2, Lemma 74.5; review `reviews/wave31-sec74-review.md` SOUND-AFTER-REPAIRS.
27. For `m` independent uniform classes mod `a`, `P(−1∈signed products)≤(3^m−1)/(a−1)`. **Lemma (proved)** — notes §75.1, Lemma 75.1; review status not stated.
28. The single-modulus tilted moments give failure `O((log N)^{-ε/2})` uniformly for `w≤(log N)^{1/2−ε}`. **Theorem (proved)** — notes §13.4, Thm 13.11; verify.py block `(k)`; review status not stated.
29. For every fixed slice, residual vanishing is `≪X(log X)^{-1−2/φ(4ck)}`; no unforced slice class is identically vanishing. **Theorem/Corollary (proved)** — notes §52.1, Thm 52.1 and Cor. 52.2; review status not stated.
30. After quotienting duplicate radicands, the stacked slice sieve proves almost-all `H_SPF(A)` for every `A<1`, with saving `exp{-c_A(log log X)^{3/2}/√log log log X}`. **Theorem (proved, effective)** — notes §53.1, Thm 53.3; review status: SOUND-AFTER-REPAIRS (wave 20).
31. The fixed-`(c,k)` composition law is `u∘_L v=u+v+Luv`, with `N(u∘_L v)=N(u)N(v)` and witness absorption. **Lemma (proved)** — notes §20.1, Lemma 20.1; review status not stated.

## (D) Walls and ceilings

1. In the independent signed-witness/finite-rounding architecture, the entropy threshold is `θ*=log 3/(1+log 3)=0.523494…`; every `θ<θ*` is attained, and the endpoint is not claimed. **Assessment (proved within the named model)** — notes §14.4, Assessment and Thm 14.9; label is not a universal impossibility theorem.
2. The class-mass optimization is `θ=B/(B+1)`: prime-modulus mass `B=2` gives `2/3`, while cubic total intrinsic supply `B=3` gives the `3/4` architecture scale. **Assessment (proved arithmetic under the stated assembly model)** — notes §18.3–§18.4, Assessments 18.3–18.4; not a universal method theorem.
3. The product-over-smooth-parts a-frame model has maximum exponent `0.58230…` at `θ=0.63481…`, below `2/3`; `θ*` is not its peak. **Assessment (restricted model)** — notes §75.4, Assessment 75.5, (75.10)–(75.11); no universal ceiling is claimed.
4. Complete avoider cylinders require `∏_{ℓ≤X,ℓ≡3(4)}ℓ | Q`; hence `log Q` is at least linear in `X` for this polylog-representation route. **Theorem (proved)** — notes §33.1, Thm 33.1; review status not stated.
5. Any Type-II congruence certificate for `W>T` contains `P_3(T)`, so `log Q≥(1/2+o(1))T`. **Theorem (proved, effective)** — notes §56.1, Thm 56.1; review status not stated.
6. Any Type-I certificate through depth `T` must carry every prime `5≤ℓ≤T`, giving `log Q≥T+o(T)`. **Theorem (proved, effective)** — notes §56.1, Thm 56.2; review status not stated.
7. Proposition 75.5P leaves a `(J−1)`-dimensional shifted sieve after one level-of-distribution expansion; the sufficient error is `N exp{-L^{θ-o(1)}}`, not a fixed-power saving. **Proposition (proved)** — notes §75.5, Prop. 75.5P; review status not stated.
8. The square family is an all-integer ceiling: a cubic supercritical tail cannot hold beyond `θ=1/3` because `W(m²)=+∞` for about `√N` integers. **Theorem/Assessment (proved obstruction)** — notes §58.1 and §59.1; review SOUND-AFTER-REPAIRS.

## (E) Precisely stated open hypotheses and conditional theorems

1. `H_kBV(κ)`: a weighted, residue-varying `k`-aspect BV estimate for the full `(u,v,k)` incidence family at `K=X^κ`. **Hypothesis (restated, not assumed here)** — notes §34.1 and §18.2; open, with Theorem 34.8 showing the pruned substitute.
2. `H_FAIL(θ₀)`: uniform per-modulus first-witness failure control with literal constant normalization. **Hypothesis (open)** — notes §71.3, (71.37); review status not stated.
3. `H_STACK(θ,γ)`: a moving-`J` Nair–Tenenbaum/shifted-form mean-value bound with controlled `C(J)` growth. **Hypothesis (open)** — notes §71.3, (71.38); no cited theorem supplies the required growth rate.
4. `H_BLK(θ)`: the joint partition bound for no-block components and full-generation blocks in (73.43). **Hypothesis (open, joint and falsifiable)** — notes §73.5, (73.43); its literal calibration is separately challenged in §75.2.
5. `H'_BLK(θ,δ_B)`: corrected block hypothesis with arbitrary fixed positive per-block saving `L^{-δ_B}`. **Definition (corrected hypothesis; open)** — notes §75.2, (75.7); not a proved input.
6. `H^+_LT(θ,λ,c₀)`: the joint lower-tail bound over confinement, low-`ω` blocks, and structured blocks, with loss `e^{CJ log log L}`. **Hypothesis (open)** — notes §75.3, (75.9); this is the sharp sufficient a-frame input.
7. `H_PF' (kℓ;good)`: restricted partition-free critical-window assembly for the pruned multiplier family. **OPEN** — notes §34.4; it is not needed by the internally proved unpruned note.
8. Under `H_BLK(θ)`, `#{p:a₁(p)>L^θ}≤N exp{-(1−θ)L^θ/(4θ)+o(L^θ)}`. **Corollary (proved implication)** — notes §73.5, Corollary 73.C(ii); conditional only.
9. Under `H'_BLK(θ,δ_B)`, `E(N)≪N exp{-cL^θ}` with exponent constant `min((1−θ)/2,δ_B)/(2θ)`. **Corollary (proved implication)** — notes §75.2, Corollary 75.3; conditional only.
10. Under `H^+_LT(θ,λ,c₀)`, `H'_BLK(θ,c₀)` and hence `E(N)≪N exp{-cL^θ}`. **Theorem (conditional exceptional-set bound; proved implication)** — notes §75.3, Theorem 75.4; conditional only.

## (F) Refutations, withdrawals, and corrections

1. The full-system cubic `H_PF` is refuted by the positive natural-density lower bound for its avoiders; the critical-window variant remains open. **REFUTED** — notes §31.1–§31.4, Thm 31.4 and §21 status correction; review status not stated.
2. The subset-witness claim that mass `(1+ε)log h` always gives polynomially small miss probability is false for `0<ε<1/log 2−1`; only signed witnesses pass the entropy threshold. **REFUTED** — notes §14.6, Lemma 14.6(1) and surrounding ledger; review status not stated.
3. The earlier “`1/2` ceiling” for the stacking architecture was false; signed entropy gives `θ*=log3/(1+log3)`, not `1/2`. **REFUTED/WITHDRAWN (label unclear — check §14.4)** — notes §14.4; no separate review status stated.
4. The claim that `STR` is negligible under `(EQ)` is false: the index-six structured-block family has mass `H(log H)^{-5/6+o(1)}` and can dominate the low-`ω` family. **REFUTED/WITHDRAWN (label unclear — check §75.1–§75.2)** — notes §75.1–§75.2; review status not separately stated.
5. The literal `H_BLK` saving `L^{-(1−θ)/2}` is miscalibrated against the block-rate model on `(θ₁,θ_hi)=(0.3357…,0.9899…)`; it is replaced by `H'_BLK`. **Assessment 75.2 (heuristic tension; label unclear — check §75.2)** — notes §75.2, (75.5)–(75.7); this is not a logical refutation of every possible block model.
6. The proposed universal “sieve ceiling” from the a-frame model was withdrawn: the `0.5823` ceiling is only for the restricted smooth-part product-majorant architecture. **WITHDRAWN/RESTRICTED-MODEL ONLY (label unclear — check §75.4)** — notes §75.4, Assessment 75.5.
7. The claimed k-wise “free deficit” was withdrawn: the free profile has a square-root error, `e^{w/2}/√J`, with total `O(1)` rather than a growing saving. **REFUTED/WITHDRAWN (label unclear — check §75 status and Outcome 36)** — notes §75.5–§75.6 / PROJECT.md Outcome 36; review `reviews/wave32-sec75-review-round2.md` and `-round3.md` SOUND-AFTER-REPAIRS.
8. The claim that one-prime witness supply is concentrated in polylogarithmically many moduli was withdrawn: the all-modulus proxy gives `(log p)^2` per polynomial scale and `(log p)^3` total, not the claimed concentration. **REFUTED/WITHDRAWN (label unclear — check §75 status and Outcome 36)** — notes §75.5–§75.7 / PROJECT.md Outcome 36; review `reviews/wave32-sec75-review-round3.md` SOUND-AFTER-REPAIRS.
9. The old conjecture `C_SQ` (“`W=+∞` iff square”) is refuted by `W(288)=W(336)=W(4545)=+∞`; the replacement `C'_SQ` adds these three sporadics and remains open. **REFUTED; OPEN replacement** — notes §60.2, Thm 60.3 and §61 status; review status recorded as SOUND-AFTER-REPAIRS in PROJECT.md Outcome 28.
10. The pointwise hypotheses `H_MOD(A)` and `H_SPF(A)` are refuted for every `A<1`; the exact remaining frontier is `A≥1`. **REFUTED** — notes §54.1, Thms 54.1 and 54.3; review CONFIRMED with no mathematical repairs (PROJECT.md Outcome 24).

## (G) Pointwise signed refactor graph (SIGNED_REFACTOR.md, POINTWISE.md §1; attributions per LITERATURE_2026.md)

1. Signed character dichotomy (2a): a signed vertex is all-positive iff its same-valuation pair has opposite Legendre characters mod `p`. **KNOWN** — Bright–Loughran 2020 (arXiv:1908.02526) Thm 1.2 + Thm 1.5 at `n=p`, combined with the signed valuation lemma; the positive direction is Yamamoto 1965. The campaign's elementary proof re-derives it. It is not a campaign discovery.
2. Finiteness of the signed solution set. **KNOWN** — Bright–Loughran Lemma 3.10.
3. Labels `(4m-1)(4n-1)≡1 (mod p)` and the symmetric Type I chart `e|x²⇔e|m²`. **KNOWN in disguise** — Elsholtz–Tao coordinates, (2.1), (2.6), (2.7), (2.21). Type I/II p-divisible rigidity in the positive case: Jiang arXiv:2609.09204v1 Thm 3.2 (v2 withdrawn).
4. The refactor graph and seed `(t,-2pt,-2pt)`; the three-edge dual-hub bridge; hub fibre sizes `3τ(t²)`, `τ(t²)`; Type II fibres have at most 2 vertices; p-free buckets outside `[1,2t]` are singletons (SR §5 + WINDMILL Thm 7); singleton bounds for p-free anchors outside `[1,2t]`. **PROVED (elementary; no prior source found)** — SIGNED_REFACTOR §§1, 5.
5. Seed-component conjecture (the seed component contains a positive vertex); it implies ES for `p≡1 (4)`. **OPEN unconditionally; FALSE under H** (item 12). EVIDENCE: seed distance ≤3 for all `p≡1 (4)` below `3·10⁵` and all `p≡1 (24)` up to `5·10⁶` (SIGNED_REFACTOR §7).

6. Exact classification of seed escapes of length ≤3. Such an escape exists iff (9), (A) a negative-fibre transfer `c|t²`, `d|(pc+t)²`, `d≡-c (mod 4c+1)` with a productive anchor `t+(d+c)/(4c+1)` or `w`, or (B) a Type II swap holds. **PROVED** — DEPTH3.md Theorem 1. Validated against brute-force BFS layers.
7. Under Schinzel's Hypothesis H, the seed distance is unbounded. For every k, infinitely many `p=24q+1` have every vertex within distance k of the seed nonpositive. Under Bateman–Horn there are `≫_k N/(log N)^{C_k}` such `p≤N`. This is a graph version of Schinzel's polynomial-identity obstruction, via a profinite generic base point and the character dichotomy (2a). **CONDITIONAL on H (proved implication); novelty unchecked**. Informal antecedent: Elsholtz–Tao arXiv:1107.1010v6 p. 6, remark after Prop 1.6 ("methods must fail for odd squares"; PAPER_B_ISSUES 1); see also Schinzel, Bright–Loughran Cor 1.4, and Dahan Prop 3.8 / Thm 4.14. It is best read as the H-conditional form of that principle — DEPTH3.md Theorem 2, §3.
8. Forced exits and exceptional-set bounds.
   * Every prime outside Mordell's six classes mod 840 has seed distance exactly 2.
   * `#{p≤N: dist>2} ≪ N/(log N)^{11/2}`.
   * `#{p≤N: dist>5} ≪ N/(log N)^{10}`.
   * Both use Dahan's half-dimension (Lemma 4.2 / Thm 4.3). The first version's
     crude exponents were `1+κ₂≈2.02` and `1+2κ₂`.
   * Every exit needs a prime factor of a new shift that is a non-residue mod p (DEPTH3 Lemma 5).

   * Note: after the wave34 review repair, DEPTH3 Theorem 3 states the half-dimension exponents. The data suggest a local exponent ≈6.2, so these are still not sharp.

   **PROVED modulo a standard sieve theorem (Corollary PROVED outright)** — DEPTH3.md Lemma 4, Corollary, Theorem 3, Lemma 5.
9. Survey results.
   * Every prime `p≡1 (4)` below `10^12` has seed distance ≤3; exactly 44197 have distance 3.
   * All 1113907 primes `p=24q+1` (q prime, `q≤10^13`) that fail (9) escape at depth 3.
   * No prime of distance ≥4 is known.

   **EVIDENCE** — DEPTH3.md §5.

10. Windmill/parity search. Any two-involution parity argument yields an explicit weight on positive solutions with odd total (Lemma 1). Only the swap and the sign change are integral affine symmetries of the four-parameter model (Prop 2). Fibre parity certifies only mixed-sign vertices (Lemma 3). The natural odd set `S_112` sees ES with weight 6 (Prop 5). No generalising parity law among the tested features. **PROVED (lemmas) / EVIDENCE (negative scans)** — WINDMILL.md.
11. Size conjecture refuted in practice: certified "dead-hub" sterile components of up to 30035 vertices, larger than the seed component (10155) at `p=274159709010072908384347957`. Lemmas A (negative quadrant), B (dead-hub fibre), C (descent), E (sign flip via a prime `≡-1` mod the anchor/bucket modulus). **CERTIFIED / PROVED** — SIZE_CONJECTURE.md; certificates re-checked in reviews/wave34-hostile-review.md.

12. **Theorem F: the seed-component conjecture is conditionally false.** Assume Schinzel's Hypothesis H for an explicit family of 6402 polynomials (13521 in the literal Lemma-3 form). Then infinitely many primes `p=24q+1` (q prime) have a seed component with **no** all-positive vertex. That component is exactly the set of values of 7883 explicit formal vertices, all nonpositive. Under Bateman–Horn there are `≫N/(log N)^{6402}` such `p≤N`.
   * The proof is a finite certificate: S, Λ (2036 primes), `q0 mod M≈10^{12088}`, and the 7883 formal vertices, closed under all formal fibres. Dead denominators are handled by WINDMILL Thm 7.
   * The "accidental-prime" gap is closed by putting every prime of every constant `c_r` into Λ, via a fixed-point choice of `q0`.
   * ES itself is untouched. No example is within computational reach.
   * The class q0 is not a square class (`24q0+1` is a non-residue mod 870 of the 2036 primes of Λ); (C4) is checked directly, not explained by "every prime met is a residue" (PAPER_B_ISSUES 4).
   * Stronger companion version: `../erdos-straus-astra` (Dickson for 159 linear forms). Its positive solution outside the sterile component needs Dickson for the forms restricted to the subprogression `n≡507 (857)` (admissibility checked there; PAPER_B_ISSUES 11).

   **CONDITIONAL on H (proved implication) + CERTIFIED; independently reviewed.** The review (reviews/formal-closure-review.md) used a from-scratch engine: all 9961 fibres equal, logic CORRECT. The parent re-ran `formal2_verify.py` and `formal2_verify_extra.py`: OK — FORMAL_CLOSURE.md, data/formal_closure/.

## Items to verify by the maintainer

- Confirm whether the exact preferred label for the §14.4 correction is `REFUTED`, `WITHDRAWN`, or only the source’s prose “false”; the ledger intentionally marks it unclear.
- Confirm labels for the withdrawn §75 claims (STR negligibility, universal ceiling, free deficit, and polylogarithmic concentration) against the precise review blocks; the source records the decisions in PROJECT.md Outcome 36 but not all as bold theorem labels.
- Confirm whether §31.4 should be listed as a campaign original theorem or as a refutation of the earlier `H_PF` formulation only; the mathematical statement itself is source-labelled proved.
- Confirm whether the `2/3` loglog result should be called a new campaign discovery after the external priority audit; the source reports no prior improvement but retains the priority caveat.
