# Z60_SUMMARY — wave z60 "attack the cleanest statements + three new idea generators": eight lanes, no lead, one sharper target (U₇), several scoped no-gos

**ES is OPEN; (MS), (MS⁺), (MS⁺₁₀₅), U_II, (MS-U), the new CONJECTURE U₇, CONV-II and (MS-II) are open.** Everything here
is internal and unrefereed. Wave z60 (brief `z52bbriefs/z60_lanes.md`) ran eight lanes: LOPEZ (Opus, structured: López's
single line U_II), LOPEZT (Fable, tryhard, unprimed: "prove López's Conjecture 1"; its kickoff first had the two branch zero
lists swapped — corrected by message; the final memo carries the corrected lists in §0/§4 and the review confirms no claim
was affected), MS105 (Opus, structured: (MS⁺₁₀₅) and the near-square threat), MS105T (Opus, tryhard: "prove the
primality-free statement"), SIGNED (Opus: signed / multi-eigensystem automorphic proxies), RAYCLASS (Opus: norm forms in
ℚ(√(−Cp))), DYNAMICS (Opus: a single long orbit / shrinking targets), TRACE (Opus: Hecke trace formula on Γ(4C)). Memos
`Z60_<LANE>.md`; cross-model reviews `data/z60/xreview/REVIEW_<LANE>.md`. **All eight cross-model verdicts were
ACCEPT-WITH-FIXES; the fixes were applied and not re-reviewed.** Each memo's own statement governs; scopes here are short.

Notation as in `Z59_SUMMARY.md`: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^×;
R₈ = C-even half of (★); U_II = (c = 1) ∪ (a = 1) ⊂ Type II (branch B = (★), branch A = the a = 1 line, = López Type A **at
primes** only); 𝒞₁(2N) = integers that are units and squares at every prime of 2N; 𝔊* = the restricted-family screen
(38 primes, 14 of them the (★)-zero primes, the other 24 have R > 0). New: **U₇(n)**: some f ≡ 7 (mod 8) has
(−n mod f) | f + 1 (⟺ a word with 8 | xy; LOPEZ Lemma 7); **Z₇** = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425};
**S₁(n)** = #{(a, b, c) : 4abc = a + b + nc} (Type II with d = 1, RAYCLASS's single-field family); **g*(p)** = least witness
modulus of the López union (LOPEZT).

## 0. Bottom line

* **No HOT LEAD. No lane found a mechanism proving R(p) ≥ 1, U_II(p) ≥ 1, U₇(p) ≥ 1 or N_II(p) ≥ 1 at every sufficiently
  large hard prime. B2 (the tied-modulus divisor event at one integer) did not move.** Verdicts: LOPEZ "narrowed + sharper
  target; no mechanism"; LOPEZT "NOT PROVED; no HOT LEAD"; MS105 "narrowed (with a certified extension); no HOT LEAD";
  MS105T "NOT PROVED"; SIGNED, RAYCLASS, DYNAMICS, TRACE "narrowed". The two tryhard lanes (LOPEZT, MS105T) mostly
  rederived prior repository results (reviews give the attribution maps). Each of the three new generators (RAYCLASS,
  DYNAMICS, TRACE) produced an exact encoding of (★) and ended at B2 in its own coordinates.
* **Sharper target (CONJECTURE; a statement, not a mechanism).** **CONJECTURE U₇** (LOPEZ §4.2): every odd non-square
  n ∉ Z₇ satisfies U₇. Sign-free (no Jacobi filter, no branch split), T1 automatic; on n ≡ 1 (4), (★) ⊂ U₇ ⊂ U_II and
  U₇ = (★) ∪ (Type A with cd even); U₇ holds on all n ≡ 3 (4); U⁽⁸⁾ ⊂ U₇. CERTIFIED: zeros ≤ 10¹⁰ exactly Z₇ (all composite,
  ≡ 1 (8), each divisible by 5 or 7); no odd prime zero ≤ 10¹⁰; no non-square zero in 𝔐 ≤ 10¹² (one engine + checks).
  (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II) are implications; strictness is not claimed. "Sharper" = fewer conditions, not easier.
* **Scoped no-gos (PROVED in their scopes; none is a necessity theorem for every proof).**
  * SIGNED: in weight 3/2 the *signed* form of T1 (g(m²) ≤ 0) is as strong as the support form, for one or any finite mixture
    of quadratic nebentypus (Thms S1, S2); in weight ≥ 5/2 for one ψ only (Prop S3) — **mixtures in weight ≥ 5/2 escape**
    (explicit rank-5 counterexample, positive at every p ≡ 17 (24), off 𝔐). For multi-eigensystem *support* proxies,
    cancellation is never the obstruction (Prop S5: effective iff S(p) ∉ W, generic real coefficients work); what is missing
    is twisted central-value non-degeneracy plus an independent validity mechanism, neither supplied.
  * LOPEZ Prop D: no p-independent first-witness link law between the two U_II branches (unconditionally in the modulus f;
    under Dickson in the shift and middle-letter coordinates).
  * MS105 Thm 3: along a non-square univariate polynomial the zero set of R has density 0 (no positive-density algebraic
    zero family; not finiteness). MS105T Prop 3.1 / Thm 3.2 / Cor 3.3: bounded congruence covers fail (prior: Z55_HCF).
  * RAYCLASS: per-field ring-class information is at most a "visible layer" GV_C that holds at some level for *every*
    non-square, including all known zeros (Props 3.1–3.2); class-number size is T1-blind (Prop 5.1).
  * DYNAMICS: Fourier-ℓ¹ (Weil-completion) minorant certificates need > 2p^{5/2}/(p − 1 + 2√p) target points vs
    ≤ p(1 + log p)² available (no certificate for p ≥ 10⁴); no modular-surface minorant separates hits (Prop 4′).
  * TRACE: an exact Γ(4C) trace identity whose odd-weight part isolates (★) from the trivial points (general case
    CONDITIONAL on the local Lemma 3); worst-case Deligne certificates need an alignment condition (Cor 4.3) and never fired
    at C = 2, 3 in the screened ranges.
* **New certified data:** U₇ census (above); MS105 kernel census of 67 872 056 404 inputs s·m² < 2⁶⁴ (no new zero; plus
  windows to n ≈ 10³⁷, near squares, pseudosquares, locally-square inputs); MS105T cover at modulus 1 441 440 (6275 of
  164 736 admissible classes uncovered); López joint run on 6 354 932 primes p ≡ 1 (24) ≤ 10⁹; least López witness g* ≤ 10487
  for p ≡ 1 (24) ≤ 10⁸; S₁ prime-zero census ≤ 10⁷ (160 zeros); mixed-ψ validity certificates at L = 168, 240, 280 (§3).

## 1. Per-lane table

Labels after review fixes. All verdicts ACCEPT-WITH-FIXES, fixes applied, not re-reviewed.

| Lane | Tried | Proved / certified (labelled, scoped) | Killed (scoped) | Survives | Review (all ACCEPT-WITH-FIXES): main fixes |
|---|---|---|---|---|---|
| LOPEZ | Pointwise link between U_II's two branches; joint first-witness structure at hard primes; sign-free sub-target | PROVED: Lemma L (U_II ⟺ ∃ f ≡ 3 (4), (n/f) = −1, (−n mod f) \| f + 1 ⟺ word with 4 \| x, y or z; forms mostly prior: DK Thm 4.5, HJ_DEEP, CONV2 Lemma 1); Prop E (inversion swaps branches at fixed f; branch vectors exchangeable in law for each fixed X — not same-prime rescue, not independence); coupling lemma (every witness f of either branch at p ≡ 1 (4) has a prime factor ℓ with χ_p(ℓ) = −1, so both least f ≥ n′_p); Prop D; Lemma 7 (U₇ forms; U₇(m²) = 0; moduli 7, 15 complete). EVIDENCE (CERTIFIED counts): 6 354 932 primes p ≡ 1 (24) ≤ 10⁹ — deep-tail (99–99.9 %) co-failure *positively* dependent, 1.2–5.9× conditional independence after stratification (up to 16× raw; 59–107 joint events); bulk (≈ 94 %) weakly negative, 0.81–0.95. CERTIFIED: U₇ census (§3) | p-independent "A fails up to X ⟹ B fires by g(X)" laws (or reverse): for every X infinitely many p ≡ 1 (840) fail both branches at all f ≤ X (PROVED, Dirichlet); shift / middle-letter versions CONDITIONAL on Dickson; one-sided laws refuted by 5569 (F4) | CONJECTURE U₇, U_II, (MS-U); adaptive / p-dependent links, counting arguments. Causal readings of the dependence (small-prime χ_p, sieve repulsion) are hypotheses / Assessment | A-line ≠ López Type A on composites; "no complementarity" limited to tested deep tails; R₈ F2 control added |
| LOPEZT | Unprimed: López Conj 1 via Type I/II parametrisations, unified forms U1–U7, coverings, counting | PROVED (largely prior: Z59_CONV2 Lemma 1(vi), B1_LINE, Z58_CONVF, CLASS_FORCING): Lemmas 0.1–0.5, 1.1 (U5: S iff p or p⁻¹ mod g ∈ −Div((g+1)/4)), 1.2 (fixed M: infinitely many p ≡ 1 (24) with no witness g ≤ M), 2.1–2.2 (prime-p Type II / Type I forms; S = the two Type II axes m = 1, a = 1); Prop 3.1 (g*(p) ≥ (1/5 − o(1)) log p i.o.). HEURISTIC: witness count ≪ (log X)² (no constants; probability bound with φ(g), corrected from g). CERTIFIED: g* census (§3) | fixed bounded witness moduli (Lemma 1.2) — growing moduli and analytic methods not excluded; C2–C5 (explicit / prime / composite witnesses, counting) are Assessments | P* (equivalent to U1/U3–U6); for P* to avoid the S₈ failures it must use g ≡ 3 (8) or a non-liftable U5 divisor (on B4: a odd; example p = 83449). Off-axis Type II rescues 105 ((a, m, g) = (3, 2, 71)), not 4545 | φ(g) for g, constants withdrawn; U5 vs shift 2-adic slack (p = 83449); F2–F4 rows; prior-art map; C2–C5 as Assessments |
| MS105 | Near-square / square-mimicking threat to (MS⁺₁₀₅) far beyond 10¹⁰; composite-only routes; polynomial families | PROVED: Claim 0; Lemma 1 (twisted T1: n = s·m² ⟹ s ∤ uC, s ∤ BC; ((s/g)/d) = −1 for g = gcd(s, uC)); Lemma 2 (kernel decomposition R(n) = Σ_{g\|n} R*_g(n/g); prior Z59_MSPLUS Lemma 5.1); **Thm 3** (rel. Serre / Cohen HIT + Chebotarev: f ∈ ℤ[t] non-constant, positive leading coefficient — (a) f = g², g ∈ ℚ[t] ⟹ R(f(t)) = 0 whenever g(t) is an odd integer; (b) otherwise {t : R(f(t)) = 0} has natural density 0); Prop 4 (d-form hits a, b coprime ⟹ ab a hit only if (a/d)(b/d) = −1; necessary, not sufficient). CERTIFIED: threat censuses (§3). EVIDENCE: maximal square-mimicry lowers group-mean hit counts by ≈ 30 % (pseudosquares) / ≈ 11–17 % (locally square) | positive-density zero families along non-square univariate polynomials (not finiteness, not sporadic zeros, no multivariate theorem — compositions can produce squares); unconditional scaling ascent (12 538 801 = 517·24 253; 4545); common-modulus gluing of two factor hits | **(MS⁺₁₀₅) survives every test (not refuted)**; no data-driven strengthening of non-squareness recommended; R₈ control materially later (281 UNK above 10¹⁰, not certified zeros) | both prime screens reported, 38-zero reference list kept separate; runners hardened (shell status not a certificate) |
| MS105T | Unprimed: prove eventual (MS⁺₁₀₅) ("MS105") | PROVED: Lemmas 1.1–1.3 (equivalent forms; n ≡ 5 (8) good via d = n + 2), 2.1–2.4, Cor 2.3 (odd squares never good; (s/a) = −1 constraint satisfiable), Prop 3.1 (every fixed M leaves infinitely many primes outside all good classes mod divisors of M), Thm 3.2 (profinite x with x_q = r, q > 3r + 1, x_ℓ = 1 else, lies in no good class) and Cor 3.3 (∀ M ∃^∞ p — not one prime avoiding every M; q = 5, 7 only at M = 1 441 440) — D-part prior: **Z55_HCF Thm 3.1 / Cor 3.2–3.3**; Cor 3.4 (∀ B infinitely many such primes have every solution with uk, kC, uC > B; not existence). CERTIFIED: Thm 4.1 cover; zero census ≤ 3·10⁷ (§3) | bounded congruence covers; one prescribed non-residue prime; unconditional good × good closure (2929 = 29·101 is a zero) | growing / size-controlled searches, conditional descent / gluing. Missing input (Assessment): a pointwise lower bound for divisors of 4Cn + 1 or n + k in progressions whose modulus grows with the shift | 38 / 14 / 24 distinction; ∀ M ∃^∞ p quantifier; Z55_HCF credit; `%ld` fix, reverified |
| SIGNED | Signed minorants, mixed quadratic ψ, multi-eigensystem sums, cosets, higher weight, mock / Rademacher, FJ / indefinite theta | PROVED rel. cited inputs: Thm S1 (one ψ, weight 3/2, g(ℓ²) ≤ 0 at large primes ⟹ E(1) ≤ 0; E(1) < 0 ⟹ g(p) < 0 at every large p ∈ 𝒞₁ (ineffective); E(1) = 0 ⟹ only components with L(½, φ ⊗ ψχ₋₄) = 0 survive on squarefree t ∈ 𝒞₁, t > 1); Lemma 3.1 (no division by E_ψ(1)); Thm S2 (any finite mixture of quadratic ψ, weight 3/2; support and signed forms, using good squarefree-index squares incl. composite m); Prop S3 (weight ≥ 5/2, one ψ; mixed-ψ *support* extension PROVED); rank-5 mixed signed counterexample (PROVED: g(m²) < 0 every odd m, g(p) > 0 every p ≡ 17 (24); negative at all 53 𝔐-primes ≤ 20 000); Lemma S4 (elementary); Prop S5 (support criterion, elementary). CONDITIONAL: cosets on (SWc) (class by class); S4′ on (Dom); S5 L-value reading on the W1′ dictionary. CERTIFIED: §3. Assessment: non-quadratic nebentypus (S2 Remark 2); FJ / indefinite (reductions only) | signed proxies in weight 3/2 (one or mixed quadratic ψ) and weight ≥ 5/2 (one ψ) on squarefree 𝒞₁: only Gauss-exceptional components survive; termwise coset recipes (CONDITIONAL on SWc); exponential objects with a dominant periodic term (CONDITIONAL on Dom) | integral-weight signed proxies (AUTOMORPH B1); mixed-ψ signed in weight ≥ 5/2; off-𝒞₁; varying level (needs q ≥ n_p, B2); non-quadratic characters; coset cusp parts; general mock objects; level sums; signed multi-eigensystem (common-K joint sign feasibility); an independent validity mechanism (none known) | rank-5 proof for all odd m; signed cone vs span; Lemma 3.1 without division; n = 193 PY note; S2 Remark 2 → Assessment |
| RAYCLASS | (★), a = 1 line, full Type II as ideal divisors of β_r = 1 + r√(−t₀n) in K = ℚ(√(−t₀n)); ray / ring class, class number, splitting, cross-field data | PROVED: Lemma 1 (dictionary for orders containing β; moduli t₀r², 4t₀r², 2t₀r; even-r a = 1 events ⊂ (★), only odd r adds); Lemma 2 / Cor 2.1 (T1 via the square-class field: for n = s·m², (★) has no hit at C with s \| C; for primes this kills only C ≥ n, outside the (MS) range); Prop 3.1 (standard CFT: event class-determined in some order only if C ∈ {1, 2, 3, 6}, even then not necessarily); Prop 3.2 (every odd non-square has a level with GV_C); Prop 4.1 (cross-field fibre products carry quartic information; group theory PROVED, ℚ(√−17), ℤ[17i] instance CERTIFIED on a sample); Prop 4.2 (CFT relations on β's factors are total-product relations); Prop 5.1; Prop 5.2 (box-count identity, Re σ > 1). EVIDENCE: S₁/L(1, χ₋₄ₚ) Spearman 0.875 on 7 254 primes p ≡ 1 (4) ∈ [10⁶, 1.2·10⁶]; the part of R at non-square levels C (t₀ > 1) correlates only 0.053 (all of R: 0.426; small but nonzero, p ≈ 5.9·10⁻⁶ — "uncorrelated" is descriptive only) | proofs using only the visible ring-class layer GV_C; class-number size; small-prime splitting alone (Legendre data); all-n class-number criteria h ≥ g(n) with g ≤ c√n / log log n at fixed C (false on squares; prime-restricted versions not refuted). Not a blanket no-go for class-group or single-field methods | (E1) non-CFT relations linking individual factors across levels C (shared primes q \| C − C′); (E2) twist-averaged bounds via Prop 5.2; (E3) cross-field characters as sieve input (still B1/B2). Single-field S₁ has its own prime zeros (160 ≤ 10⁷) | F4 / S₁ scope; dictionary only for orders containing β; Siegel ineffective, Paulin attribution; T1 exactly at s \| C |
| DYNAMICS | (★) as hits of one p-dependent Kloosterman / Hecke-point orbit in a target; rates vs target mass; thickening, alternate orbits | PROVED: Lemma 1 (R(n) = R°(n) + #{u = 1 or B = 1}, R° = orbit-target hits, odd n ≥ 5); Lemma 1′ (shell c = tied modulus); Lemma 1″ (R° = coprime A with minus continued fraction of n/A of length 3, [[c, m, s]], 4 \| m); Lemma 2 (hits in the χ_n = −1 coset; index 2 only for non-squares; empty iff square); Lemma 3a (\|T_n\| ≤ n(1 + log n)²); Lemma 3 (ℓ¹ exponent ½ optimal for that norm); Prop 3 / Cor 3; Prop 4′; Prop 4 (abstract); Prop 6 (Σ χ_n(x)1_T = −R°(n)). CONDITIONAL (Γ\G rate p^{−1/2+θ}, θ = 7/64, Sobolev norm, compact support): Prop 4 application — margin / rate ≤ p^{−1/6−θ+o(1)} (exponent −53/192); a big orbit hole is necessary. EVIDENCE: \|T_n\| ~ n(log n)²/8 heuristic (ratios 0.64–0.80); discrepancy samples | Weil-completion certificates for T_p, p ≥ 10⁴ (missing exponent ½ up to logs, in that norm only); modular-surface minorants (any rate); rate-based margin route highly constrained | target-specific cancellation, other norms, actual orbit holes, Γ\G certificates with tiny margin, QNR half-orbit analysis (E3), spectral cancellation (→ TRACE), alternate encodings. "Hole-finding is B2" is an Assessment | 𝔊* F4 screen (1621); no-go wording narrowed, Prop 4 hypotheses kept; Lemma 2 index-2 fix; literature scopes |
| TRACE | Exact elliptic + hyperbolic + scalar trace identity on Γ(4C) via Γ = Qγ − I, Q = 4C; positivity from spectral bounds | PROVED: Lemma 1 (dictionary; ES_k(C, m²) = 0 for odd m); Lemma 2 (class counting, factor 2μ_C·H(4s − w²)). **Thm 2 (trace identity): CERTIFIED by exact spectral computation on a sparse finite list; for general (C, k, n) CONDITIONAL on Lemma 3** (local f-sum / embedding identity; CERTIFIED on 21 044 cases, not proved), relative to Cohen–Strömberg Thm 12.4.11 (checked via secondary quotation). Cor 2.1 (C = 1; CONDITIONAL; CERTIFIED to n ≤ 50 000). Props 4.1, 4.2, Cor 4.3, Prop 4.4: PROVED from Thm 2 (so CONDITIONAL where Thm 2 is). Remarks 4.5, 4.6: Assessments | worst-case Deligne certificate (B = D) needs average normalised eigenvalue > 1 − 6/((k − 1)Q − 6) (only (k, Q) = (3, 4) lacks a ρ-free constraint); never fired at C = 2 (n ≤ 3000) or C = 3 (n ≤ 600) — finite evidence, not universal non-firing; a level-uniform absolute square-root bound (all Γ(4C), all n; family at n ≡ 5 (8), outside the Mordell-hard domain; CONDITIONAL on Thm 2) | single-N bounds sharper than Deligne with slack ≪ (ε∞/2)·ES (none known); one-sided estimates restricted to Mordell-hard primes; other C-ranges; an identity whose spectral side carries independent positivity. Encoding success, not positivity | Deligne claim → necessary condition + finite evidence; F4 38 / 24; gcd(Q − 1, 2Q − 1) = 1, ρ-free qualifier; LIT_CHECK conventions |

## 2. Falsifier lessons across lanes

| Lane / idea | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros |
|---|---|---|---|---|
| LOPEZ, link laws / U₇ | both branches fail at every f at m²; U₇(m²) = 0 (Lemma 7(ii)); Prop D's primes are squares at every modulus ≤ X | U⁽⁸⁾ (547 zeros n ≡ 1 (4) ≤ 10⁸, 45 primes, last 3 869 153) ⊂ U₇: a U₇ proof must use the extra targets; all 12 R₈-zero primes in [10¹⁰, 1.1·10¹⁰] rescued (R ≥ 12); U₇'s two branch halves fail at 14 resp. 12 primes ≤ 10⁸ | U₇-zeros = Z₇ (8 composites); 105, 4545 fail both U_II branches; review: of the 285 (★)-composites, 8 U₇ failures, 277 rescued | U₇ rescues all 14 (★)-zero primes, 193, 2521, 66529, the 24 𝔊*-zeros with R ≥ 1; B never fires at 5569 while A fires at a = 2 (kills one-sided laws) |
| LOPEZT, union S | Jacobi obstruction (Lemma 0.5), no primality needed | S₈ has 45 prime zeros ≡ 1 (4) ≤ 10⁸ (last 3 869 153; 61 over all odd primes — keep apart); the 12 R₈-zero primes all have B4 and BN witnesses | of the 285 (★)-composites, 283 have B4 witnesses; S fails exactly at 105, 4545 | B4 fails at 193, 2521, 66529; BN at the 14 (★)-primes (all have B4 witnesses, least g 7 … 1735); all 38 𝔊*-zeros have B4 witnesses |
| MS105, threat search / Thm 3 | s = 1 excluded; Lemma 1 at s = 1 is T1; Thm 3(a) is the square case | R₈ control: 281 UNK above 10¹⁰ (to 1.84·10¹⁹) where R has none above 10⁶; 40 certified R₈ zeros ≤ 2.93·10⁷; Thm 3 also holds for R₈ unless f or 2f is a square | census reproduces the known composite zeros (incl. 752 257 = 11²·6217); 12 538 801 kills unconditional ascent; inheritance = 1.7 % of R on composites ≤ 2·10⁷ | 14 (★)-primes have R = 0; of the 38 𝔊*, the other 24 have R > 0; 38 coprime-to-105 R-zeros ≤ 10¹⁰ (14 primes + 24 composites) |
| MS105T, covers | Cor 2.3: squares never good; (s/a) = −1 satisfiable for s·m² | warning only: no claimed positive result restricts C; review re-enumerated the 12 R₈ zeros (all full-family witnesses have odd C) | 361 non-square zeros ≤ 3·10⁷ (38 coprime to 105: 14 primes, 24 composites); 285-list matches z58 | 14 full-family prime zeros (all ≡ 1 (8)); all 2280 zeros in [1 441 440, 3·10⁷] lie in uncovered classes |
| SIGNED, automorphic proxies | S1–S3 upgrade the sign inequality to support conclusions (scoped); integral weight / mixed ψ in weight ≥ 5/2 do not | line-blind: negative results apply to R₈-minorants; an R₈ version of S5 must start above 10 868 474 401 (largest in-𝔐 R₈ zero) | squarefree composite zeros enter S5's zero space like primes; used in mixed certificates | 9 of the 14 (★)-primes in 𝔐; L = 420 lines vanishing at 5569, 9601 are non-zero at other zeros (102001, 712321, 1724209, 5212561, 8813281; numerical / BSD-dependent) ⟹ not prime-valid |
| RAYCLASS, ideal divisors | Lemma 2(c) at every level; GV = 0 for 99 odd squares (C ≤ 100) | GV holds at 16–38 even levels C ≤ 200 at each R₈-zero prime, hits none | GV at 9–38 levels C ≤ 100 at the 285 composites; nothing uses primality | GV at 64–90 levels C ≤ 300 at each (★)-zero prime, hits none; S₁ ≥ 1 at all 14 and 36/38 𝔊* (S₁ = 0 at 37, 1621) |
| DYNAMICS, orbit hitting | hits in the QNR half-orbit, empty iff square; Nμ = 7.95 at 101² vs 7.95 at 10007 (target mass square-blind) | T⁽⁸⁾ = {8 \| c}: same orbit, ≈ half mass, same rates — parity-blind certificates fail | Kloosterman bound carries τ(n)gcd(h, k, n)^{1/2}; 285 composite zeros, 105, 4545 | Nμ ≈ 2.9–27.2 at the R-zero primes; 𝔊*: only 17/38 recomputed (37, 157, 184837 boundary-only; 1621 has R° = 2) |
| TRACE, spectral certificate | ES_k(C, m²) = 0 PROVED; no certificate fires on the screened squares (max Tr/D 0.66 at 81², C = 2) | identity is per C; an argument transporting verbatim to even C is false at the 12 + 2 R₈-zero primes in [10¹⁰, 2.33·10¹⁰] | identity uniform in n; 285 composite zeros have ES = 0 at every C | 14 global zeros: ES = 0 at every C (any spectral lower bound must fail there or start above 8 813 281); at 9601, C = 2: Tr/D = 0.068 |

**Lessons** (Assessment unless labelled).
1. **Every new encoding reaches B2 at the same place.** RAYCLASS (an ideal divisor of β with norm ≡ −1 mod the level),
   DYNAMICS (shell index = tied modulus; hole-finding), TRACE (positive split points; spectral side does not see the tie
   without new positivity input) and MS105T (divisors of 4Cn + 1 / n + k in progressions growing with the shift) each restate
   the tied-divisor event exactly; none supplies the pointwise input.
2. **T1 is a sign (kernel) statement in every coordinate system and is now known to be *stronger* than "no genus term" also
   in signed form** (SIGNED S1–S3; DYNAMICS Lemma 2 / Prop 6; RAYCLASS Lemma 2; MS105 twisted T1; LOPEZ coupling lemma).
   Its exact limits: integral weight and mixed-ψ higher weight (SIGNED counterexample) do not inherit it.
3. **Square-mimicking composites are not the threat to (MS⁺₁₀₅) at the tested scales** (MS105: ≈ 8.3·10¹⁰ structured
   inputs, no zero above 29 210 401; Thm 3 kills positive-density polynomial zero families). The R₈ control behaves very
   differently (281 UNK above 10¹⁰): C-parity matters, square-mimicry only lowers hit counts.
4. **Numerator 8 / C-even again bites every line-level statement** (U⁽⁸⁾ ⊂ U₇; S₈ 45 prime zeros; R₈ UNK set; parity-blind
   dynamics / trace certificates). A U₇ proof must use the targets U₇ adds to U⁽⁸⁾.
5. **Keep 𝔊* and R apart** (DYNAMICS, TRACE, MS105T, LOPEZT fixes): the 24 non-(★) 𝔊*-zeros have R > 0.
6. **Fixed finite menus / bounded covers fail again** (LOPEZT Lemma 1.2, MS105T Prop 3.1–Cor 3.3, LOPEZ Prop D); all prior in
   substance (Z55_HCF, Z58_LADDER, Z58_CONVF, Z59_CONV2). Unprimed lanes cost rediscovery, not novelty.

## 3. New certified data

"One engine" = one production engine; independent coverage listed. No large interval census was fully rerun by a second engine.

* **U₇ census (LOPEZ §4.2; CERTIFIED, `scripts/z60_lopez_u7.c`).** All odd n ≤ 10⁸: zeros exactly Z₇ (4999 odd squares
  skipped, T1; 4976 LATE certificates). n ≡ 1 (4) in (10⁸, 10¹⁰]: no zero (2.475·10⁹ inputs; n ≡ 3 (4) by Lemma 7(iii)).
  𝔐 ∩ (10¹⁰, 10¹²]: 7 071 428 573 inputs, 205 714 odd squares skipped, **no zero among the 7 071 222 859 non-squares**.
  Checks: independent word enumeration ≤ 10⁶ (cross-review to 2·10⁵: Z₇ exactly, no square hit); all 342 375 LATE certificates;
  3000 random n ≡ 1 (4) and 2000 random 𝔐 inputs by a plain f-loop. **Above 10⁶ one full engine + checks, not a second census.**
  U_II on 𝔐 ≤ 10¹² is inherited ((★) ⊂ U_II; TRYO / LADDER / MSPLUS), not recomputed.
* **López joint run (LOPEZ §3.2; counts CERTIFIED, reading EVIDENCE; `scripts/z60_lopez_joint.c`, one engine).** All
  6 354 932 primes p ≡ 1 (24) ≤ 10⁹ (bounds a ≤ 3000, f ≤ 20 000, T ≤ 3000); 45 hardest primes recomputed, all in 𝔐; a fresh
  run ≤ 2·10⁷ reproduced the qualitative pattern; raw data not independently regenerated.
* **Least López witness g* (LOPEZT §3.1; CERTIFIED, `scripts/z60_lopezt_leastg.c`).** 719 781 primes p ≡ 1 (24) < 10⁸:
  g* ≤ 10487 (at p = 9 658 489; no new record in [10⁷, 10⁸]); g* = 7 for 50.06 %, ≤ 23 for 90.1 %, > 1000 for 172, > 3000
  for 12 (review audit agrees). S₈ prime zeros ≤ 4·10⁶: 45, last 3 869 153 (review reproduced to 10⁸).
* **MS105 threat censuses (MS105 §2; CERTIFIED first-hit searches, LIM = 10⁸ unless stated, one engine per run).**
  Kernel census: squarefree s ≡ 1 (4), 13 ≤ s ≤ 10⁵, gcd(s, 105) = 1; odd m, gcd(m, 105) = 1, s·m² < 2⁶⁴:
  6 086 436 506 + 61 785 619 898 = **67 872 056 404 inputs**, UNK exactly the 16 known zeros (15 with m = 1, 409 … 90 889; and
  752 257, s = 6217, m = 11). Windows (106 kernels s ≤ 1000, m ∈ [10ᵏ, 10ᵏ + 2·10⁷], k = 10…17): 3 876 571 898 inputs, no UNK.
  Near squares m² + c (c ∈ ±{8, …, 200}, odd m ≤ 10⁹): 11 361 904 661 inputs, UNK only at 15 known zeros ≤ 1.26·10⁷.
  All 52 Lehmer pseudosquares ≤ 4.24·10²⁴ (+ 20 controls each): zeros exactly 2641 = L₄, 18 001 = L₆. Locally square
  x² + kP_y (y ∈ {47, 59, 71, 79, 83}, to ≈ 4·10³⁵): no UNK. R₈ control (106 kernels, 6 086 436 506 inputs): 321 UNK = 40
  certified R₈ zeros (≤ 2.93·10⁷) + 281 above 10¹⁰ (to 1.84·10¹⁹; spot checks find late witnesses, not zeros). Cross-review:
  coverage reconciled, bounded slices and extremal hits replayed; pseudosquare / locally-square replays used the same decider
  (not an independent large-number oracle); no full replay.
* **MS105T (CERTIFIED; `scripts/z60_ms105t_zeros.c`, `z60_ms105t_cover.py`; independently reproduced by the cross-review).**
  Zero census ≤ 3·10⁷: 361 non-square zeros (plus 2739 odd squares), 38 coprime to 105 (14 primes, 24 composites; only 752 257
  non-squarefree). Cover (Thm 4.1): every admissible n (≡ 1 (4), coprime to 105) ≥ 1 441 440 outside 6275 of the 164 736
  admissible classes mod 1 441 440 is good (3024 of the 6275 square classes); at M = 840: 11 of 96 uncovered (5 non-square).
* **SIGNED mixed-ψ certificates (§6.1; CERTIFIED exact rational linear algebra, PARI spaces, `scripts/z60_signed_mixed.py`;
  reproduced by the cross-review).** Full spaces over all quadratic ψ, with R-zero rows: L = 168, B = 40 000 (dim 176);
  L = 240, B = 30 000 (dim 272); L = 280, B = 30 000 (dim 240): mixed-kernel rank on 𝒞₁ ∩ [1, B] = 0 — every valid mixed-ψ
  *support* proxy vanishes there (not signed-cone certificates). Rank-5 example: all 289 primes ≡ 17 (24) ≤ 20 000 positive,
  0/53 𝔐-primes. `ellrank` bounds for 18 twists (§6.3): rank ≥ 2 ⟹ central vanishing (GZK); rank upper bound 0 does **not**
  certify non-vanishing; line ↔ eigensystem identification EVIDENCE.
* **RAYCLASS (CERTIFIED, `scripts/z60_rayclass_fam.c`, one engine; brute check on 100 small n).** S₁: 160 prime zeros
  p ≡ 1 (4) ≤ 10⁷ (25 in 𝔐, largest in 𝔐 6 193 441; largest 8 841 673; 105 with p ≡ 1 (24)); count per decade still rising
  in range — a counterexample to all-prime positivity of S₁ only. GV screens: F1–F4 rows above.
* **TRACE (CERTIFIED finite).** Thm 2 on (C, k, n ≤ n_max) = (1, 2, 150), (1, 3, 60), (1, 4, 150), (1, 5, 150), (2, 2, 80),
  (2, 3, 1500), (2, 4, 60), (3, 3, 600), (4, 3, 40), (5, 3, 30), screens (2, 3, 3000), (1, 3, 20 000): 0 mismatches; Lemma 3 on
  21 044 cases (Q ∈ {4, 8, 12, 16, 20}, n ≤ 60); Cor 2.1 to n ≤ 50 000 (pari class numbers). Deligne screens: C = 1, k = 3,
  n ≤ 20 000: fires at 137 of 12 229; C = 2, n ≤ 3000 and C = 3, n ≤ 600: 0 fires (min slack ratio 3.82, 6.76). Cross-review:
  2320 stored + 202 fresh spectral rows, 23 600 TSV rows, 998 explicit-family cases; shared PARI for factorisation.
* **DYNAMICS (CERTIFIED small checks).** Encodings checked on 19 / 11 n-values; cross-review reran F1 for every odd
  n ∈ [5, 1001] and F2/F3/F4 screens (14 R-zero primes reproduced, not completeness to 10¹⁰).

## 4. Prior-art attribution (short)

LOPEZ Lemma L / Prop E: DK Thm 4.5, HJ_DEEP Prop 2.1–2.2, Z59_CONV2 Lemma 1(vi), López's remark, Z58_LIT Prop I; López
Conjecture 1 = arXiv:2404.01508v3. LOPEZT: Z59_CONV2, B1_LINE, Z58_CONVF, CLASS_FORCING (structural results not new).
MS105: Z59_MSPLUS Lemmas 4.1, 5.1; Z59_MSPF; Serre / Cohen HIT. MS105T: Z55_HCF (Thm 3.2 / Cor 3.3), Z59_MSPLUS, Z58_LOGIC,
Z58_LADDER, Z57_SYNTH. SIGNED: Z58_TERNARY, Z59_WALDS, Z58_AUTOMORPH (Q2′, B1, B2). RAYCLASS: WINDMILL_REDUCTION Prop 10.3,
CLASS_FORCING Thm 2.1, B2_ACROSS_FIELDS, Z53_WILDCARD row 6 (addressed: joint data real as information, no forcing found).
DYNAMICS: Burrin–Shapira–Yu (Math. Ann. 2022), Strömbergsson (Duke 2004), Sarnak, COU (not re-read); LENGTH_THREE,
Z52D_HYPERBOLA. TRACE: GROWING_IDENTITIES (O170) Prop 2.1–2.2 (±1 term, parity, Deligne scale), y1_gamma8_trace (O209),
Mertens 2016, Kane–Pujahari(–Yang); new: the Γ(4C) principal-level Hecke set and the Deligne firing condition.

## 5. Open problems supported by the memos (none is a lead)

1. **CONJECTURE U₇ / (MS-U₇)** (LOPEZ): a fixed-p argument for "some f ≡ 7 (8) has (−p mod f) | f + 1" suffices for (MS-U).
   It must fail at the eight composites of Z₇ and use the targets beyond U⁽⁸⁾ (v₂((f+1)/8) < v₂(r) < 3). Adaptive /
   p-dependent branch links and counting arguments are not excluded by Prop D.
2. **(MS⁺₁₀₅)** (MS105, MS105T): survives all threat tests; open are finiteness along any family, density-zero
   non-algebraic families and sporadic zeros. Missing input (Assessment): pointwise lower bounds for divisors of n + k /
   4Cn + 1 in progressions whose modulus grows with the shift; a proof must use C odd somewhere.
3. **Automorphic (SIGNED):** an independent validity mechanism for exceptional Shimura sums; pointwise non-degeneracy
   S(p) ∉ W (for the full line span: some exceptional G_φ with L(½, G_φ ⊗ χ_p) ≠ 0 at every large p ∈ 𝒞₁ — (𝒟_N)); whether a
   mixed higher-weight signed proxy can be positive at all large 𝔐-primes; cosets beyond (SWc); objects where (Dom) fails.
4. **RAYCLASS (E1)–(E3):** a non-CFT relation linking individual prime factors of β across levels; twist-averaged
   bounds; whether a (★)-internal Prop 4.1 configuration exists; eventual S₁ positivity.
5. **DYNAMICS / TRACE:** target-specific cancellation on the QNR half-orbit; orbit holes; single-N trace bounds sharper
   than Deligne with slack ≪ (ε∞/2)·ES at Mordell-hard primes; **prove TRACE Lemma 3** (turns Thm 2 into a theorem).
6. **LOPEZT P***: witnesses with g ≡ 3 (8) or non-liftable U5 divisors (forced by S₈); g* growth (≥ (1/5 − o(1)) log p i.o.,
   PROVED; ≤ 10487 to 10⁸).

## 6. Caveats / do-not-export

* **ES, (MS), (MS⁺), (MS⁺₁₀₅), U_II, (MS-U), U₇, (MS-U₇), CONV-II, (MS-II) are open.** No HOT LEAD. Do not call U₇ easier than
  U_II; it has more zeros (8 vs 2) and fewer conditions.
* **Finite data stay finite.** U₇ above 10⁶, the López joint run, the MS105 threat censuses and the S₁ census are
  one-engine; UNK ≠ zero unless LIM covers the bound; the MS105 "≈ 4·10⁻³ expected zeros beyond 10¹⁰" is a model estimate.
* **LOPEZ:** A-line ≠ López Type A on composites (4/25 example). Dependence findings are EVIDENCE; fixed-X exchangeability is
  not independence or same-prime rescue; causal accounts are hypotheses. Prop D's shift / T versions are CONDITIONAL (Dickson).
* **LOPEZT:** only fixed bounded witness moduli are ruled out; the log² count is heuristic (φ(g), no constants, no
  almost-all claim); 45 S₈ zeros (p ≡ 1 (4)) vs 61 (all odd primes); the 12 R₈-zero screen ≠ the S₈ list; Graham–Ringrose
  improvement not source-certified.
* **MS105:** Thm 3 is density 0, not finiteness; univariate only; the R₈ control was completed after internal review (not
  reviewed); its proposed FRONTIER text was marked "do not apply without review" (applied here only in the scoped form above).
* **MS105T:** Cor 3.3 is ∀ M ∃^∞ p, not one prime avoiding every M, not a zero; Cor 3.4 is not existence (can be vacuous);
  the barrier is Z55_HCF's, not new.
* **SIGNED:** the mixed higher-weight signed theorem is **false** (counterexample; positive only at p ≡ 17 (24), off 𝔐, not
  valid); cosets CONDITIONAL on (SWc), class by class; S4′ only under (Dom); S5's generic-real-coefficient statement does not
  transfer to rational coefficients or the signed cone; L = 420 non-vanishings are numerical / BSD-dependent; §6.2
  correlations finite EVIDENCE; non-quadratic nebentypus extension is an Assessment.
* **RAYCLASS:** scoped to the visible layer, class-number size and Legendre data — not all class-group or single-field
  methods; Siegel is ineffective (no explicit 10¹⁷ cutoff); L-weighted expectations are heuristic; Cox / Burde via
  secondary sources.
* **DYNAMICS:** not "dynamics impossible", not a shrinking-target theorem; Prop 4 application CONDITIONAL on the Γ\G rate
  and normalisations; 𝔊* screen incomplete (21 of 38 not recomputed); "𝔊*-zero ⟹ orbit misses target" is false (1621).
* **TRACE:** do not export Thm 2 as unconditional (Lemma 3 unproved); do not export "Deligne cannot work beyond Γ(4)" or
  "no positivity possible" — only the necessary alignment condition and finite non-firing evidence; Cohen–Strömberg,
  Eichler–Zagier, Serre primary sources not obtained.
* **Nothing has been posted.**
