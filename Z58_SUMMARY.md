# Z58_SUMMARY — wave z58 "radical, many-angled probe of (MS)": sixteen lanes, no lead, a sharper map

**ES is OPEN.** Every result here is internal and unrefereed. Wave z58 (brief `z52bbriefs/z58_lanes.md`) attacked the
minimal missing statement (MS) of `Z57_SYNTH.md` from 13 first-round angles — WITNESS, FFIELD, AUTOMORPH, MORDELL, LADDER,
WILDCARD, STRUCT, LOGIC, DISPROOF, LIT (Opus, structured), TRYO (Opus, tryhard), TRYF, TRYF2 (Fable, tryhard) — plus three
follow-ups: STRUCT2, TERNARY (Opus) and CONVF (Fable, tryhard). Each lane wrote `Z58_<LANE>.md` and had internal hostile
review(s) and a cross-model review (`data/z58/xreview/REVIEW_<LANE>.md`). **All 16 cross-model verdicts were
ACCEPT-WITH-FIXES.** The lanes applied the fixes; the fixed memos were *not* re-reviewed. Every lane ran the mandatory
falsifier screens (`data/z58/screens/`). This summary carries scopes only in short form; **each memo's own statement
governs.**

Notation (as in `Z57_SUMMARY.md`): R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (the (★) count, c = 1 line of Type II);
𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^× (Mordell's classes); R₈ = the C-even half of (★) (= the c = 1 line of 8/p);
R_𝔊* = the Theorem V subfamily; N_II(n) = #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} (full Type II family);
**(MS)**: every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1.

## 0. Bottom line

* **No HOT LEAD.** No lane found a mechanism that forces R(p) ≥ 1 (or N_II(p) ≥ 1) at a single large prime. **(MS) is open,
  and ES is open.** The B2 wall (the tied-modulus divisor event at one integer) did not move. No lane supplies a HOT LEAD. The
  structured probes report "narrowed". TRYO, TRYF, TRYF2 and CONVF report no proof and no pointwise mechanism, not an
  exhausted target. WILDCARD reports "strengthened (choice of target) / inconclusive (mechanism)". No lane claims a route
  is exhausted.
* **The one statement-level survivor is the full Type II family.** WILDCARD's CONJECTURE **CONV-II**: every odd non-square
  n ≥ 3 except n = 4545 has N_II(n) ≥ 1. It is CERTIFIED for n ≤ 10¹⁰ and PROVED for n ≡ 3 (mod 4). It passes F1–F4 *as a
  statement* in the tested ranges. This is a "HOT TARGET" (Assessment about the statement), **not** a mechanism. STRUCT2
  shows that 4545 is a genuine non-BM, non-local positive-integral Hasse failure (PROVED + CERTIFIED). CONVF finds no
  pointwise construction for it.
* **Scoped no-gos, many angles (PROVED, each in its stated scope).**
  * Fixed-level holomorphic Hecke-finite proxies ℋ_M, valid on all n ≡ 1 (4) coprime to M: AUTOMORPH Thm A / Cor A1.
    Prime-only support is not covered.
  * Ternary-theta genus main terms: TERNARY Thm F / Cor F1. The genus term vanishes on 𝒞₁(2N). This contains every
    𝔐-input (𝔐 = the squares of (ℤ/840)^×) when every odd prime divisor of the level N lies in {3, 5, 7}; for
    general N, extra quadratic-residue conditions are required.
  * Positive-integral Brauer–Manin: STRUCT Thm A, STRUCT2 Thm B. For n ≥ 1, on the displayed (★) surface and Type II
    threefold (positive real region), BM detects *exactly* non-squareness (numerator 8: □ ∪ 2□). Nonemptiness is not
    sufficient for a positive integral point.
  * Fixed finite (★) menus on sterile class-1 fibres, and global polynomial certificates in x² + 840y²: MORDELL S2, C1.
  * Fixed-degree, large-q function-field positivity: FFIELD Cor 3.2.
  * Bounded-coordinate hit constructions: TRYF2 Prop 2.1; WITNESS Prop 3.1 (CONDITIONAL on Dickson).
  * Weak arithmetic: LOGIC Thm 6.2 (IOpen ⊬ MS⁺★(P)) and Thm 3.1 (rel. Buss: an S¹₂ proof of (MS) would yield a polynomial-time
    hit-or-nontrivial-factor-pair algorithm on n > 10¹⁷ with n mod 840 ∈ 𝔐; not a general factoring algorithm).
* **New certified data.**
  * TRYO: (★) holds at all 355 096 166 primes in 𝔐 ∩ (10¹⁰, 3·10¹¹] (one engine plus independent slices).
  * LADDER/LOGIC: Mordell-class censuses including composites. LADDER finds no non-square zero in 𝔐 ∩ (17 401 609, 10¹¹]
    (one engine). From this, the new **CONJECTURE (MS⁺)**: R(n) ≥ 1 for every non-square n > 17 401 609 in 𝔐.
  * DISPROOF: 868 562 designed and control primes up to ≈ 7.31·10¹⁵ (sampled, not an interval census), with no R- or
    𝔊*-zero, and two new R₈-zeros.
  * WILDCARD: N_II census to 10¹⁰.
  * WITNESS: least-witness census to 10¹⁰.
  * FFIELD: q = 3 census through degree 18.
* **Two new analytic lower bounds, for surrogates, not for R.**
  * TRYF Theorem 2.1 (Burgess; asymptotic, primes p ≡ 1 (4), no numerical onset evaluated): the Jacobi layer satisfies
    |L₂| ≤ (1/64 + o(1))log²p against the principal layer L₀ = (1/8)log²p + O(log p). So the quadratic constraint removes at most a fraction 1/8 + o(1) of the expected hits.
  * TRYF2 Theorem A: M₂(p) ≥ c₀ log²p for every sufficiently large prime p ≡ 1 (4).
  * In both cases the gap to (★) is an unproved remainder bound: HCE for TRYF, E₂ > −M₂ for TRYF2.
* **Literature: a priority correction is needed** (LIT §2.1). Kandukoori–Ramesh–Kumar (PDF dated 2026-07-29; unrefereed)
  claim E(N) ≪ N exp(−c(log N)^{3/4}). Their Lean repository has a root commit dated 2026-07-30 with the 3/4 saving. The
  campaign's internal 3/4 note was first committed 2026-09-06. FRONTIER §1 and the note's abstract must cite K-R-K (§4
  below). (MS) relevance: none.
* **Nothing has been posted.** Paper-side changes (count note citation, 3/4-note abstract) are proposals for the paper
  owner, **need the user**.

## 1. Per-angle table

Labels as in the memos *after* review fixes. "Survives" lists what the memo itself leaves open. All verdicts were
ACCEPT-WITH-FIXES with fixes applied; none were re-reviewed.

| Lane | Angle | What was tried | Proved / certified (labelled, scoped) | Killed (scoped no-go) | Survives / escape hatch |
|---|---|---|---|---|---|
| WITNESS | (MS) as a witness selector | least d, q, m3, u, C, s orderings; congruence, n_p, CF, two-square, location predictors | PROVED: orderings all "none" iff R = 0. Lemma 1.1: d_min ≥ n_p for p ≡ 1 (8). CONDITIONAL (Dickson) Prop 3.1: for every S, infinitely many p ≡ 1 (840) have s(p) > S. CERTIFIED: four-ordering census p ≤ 10⁹ (25 423 491 primes); extension to 10¹⁰; s ≤ 201 for every p ≤ 10¹⁰ with R ≥ 1 | fixed-congruence selectors on 𝔐 (PROVED); fixed bounded-coordinate menus (CONDITIONAL, Dickson); CF, two-square and n_p-rooting as predictors (EVIDENCE, null) | CONJECTURE W: every prime p > 8 813 281, p ≡ 1 (4), has a (★) solution with min(u, B, C) ≤ (log p)² (W ⟹ (MS)); growing-coordinate menus |
| FFIELD | 𝔽_q[T] analogue (★)_q, deg t odd (an analogy, not a reduction) | Weil/RH, Lang–Weil, Chebotarev; q = 3, 7, 11 censuses | PROVED: Lemma 1.2 (R_q(g²) = 0); Prop 3.1 (local word counts residue-blind at ℓ ∤ f); Prop 3.3 (rel. function-field RH: menus of degree ≤ (1/2 − δ)n leave avoiders); Lemma 4.1. CERTIFIED: q = 3 irreducible zeros only at degrees 6–12 among even degrees ≤ 18 | Cor 3.2 (rel. Chebotarev): no fixed N₀ works for all q ≡ 3 (4), so fixed-degree large-q positivity is dead; residue-blind local route | CONJECTURE: for each fixed q, eventual MS_q holds (with N₀(q) → ∞); faithful C-parity / 𝔊* analogue; transfer to the integers |
| AUTOMORPH | Extend T1 to fixed-level classes ℋ_M (fixed finite combinations of holomorphic newform/Eisenstein eigenvalue systems of integral weight k ≥ 1 and level dividing M, their n^j-twists, and the specified character-weighted real-parameter divisor sums with finitely many derivatives) | support proxies, signed minorants, half-integral weight, outside-ℋ, higher depth | PROVED: Lemma S. Thm A (rel. Deligne/Deligne–Serre, purity, Chebotarev): vanishing at 1, p², p⁴, … plus no ±-collision forces a(p) = 0. The collision-free positive-density prime set depends on the chosen combination; no common set for all ℋ is asserted. Cor A1: no a ∈ ℋ_M is both valid (a(n) ≠ 0 ⟹ R(n) ≥ 1 for every n ≡ 1 (4) coprime to M) and effective (a(p) ≠ 0 at every sufficiently large 𝔐-prime in the domain); no a ∈ ℋ_M equals R on all n ≡ 1 (4) coprime to M. Props B1, B2. CONDITIONAL Prop C (on (I) and the unproved (H_E)) | valid-and-effective support proxies in fixed ℋ_M; exact R-identity in ℋ_M; T1-compatible Eisenstein + cusp proxies (A1c). Not killed: prime-only support/equality (it does not provide square vanishing), and prime-only arguments with error outside ℋ | E1 half-integral weight; E2 coefficients outside ℋ (variable level); E3 higher depth / non-GL₂; effective signed minorants (open) |
| MORDELL | Profinite 1-points of Mordell case splits; x² + 840y² | sterility of residue points for H_d and K_{u,B} menus; class statistics; polynomial certificates | PROVED: Lemma P (polynomial identity 4UBC − U − B = a + Mt in ℚ[t] forces two constant coordinates; with positive-integral certificates the family lies in one H_d or K_{u,B} class), Thm S1, Thm S3, exact B criterion, Lemmas G0/G/O, Prop C1 (algebraic rigidity; congruence reading assumes positive-integer constants and a positive-integral solution at some point with f > 0). Cor S2 (with Dirichlet): for an odd prime ℓ and M ≥ 1 with ℓ ∤ M, every finite H ∪ K menu misses infinitely many primes p ≡ 1 (M), p ≡ R (ℓ), at non-residues R with x_{ℓ,R} sterile. CERTIFIED: bounded coverings (11 full-menu survivors mod 840) | finite (★) case splits on class-1 sterile fibres (S2); global polynomial certificates in (x, y) with positive-integral constants reduce to congruences (C1); arbitrary one-parameter algorithms, rational or piecewise families not covered | the other five Mordell classes; non-polynomial or divisor uses of (x, y); B2 large-factor route |
| LADDER | Mechanism III: size-controlled symmetric covering; primality-blind rung; exponent-cap ladder | μ(p) tails, L2^𝔐 census, cap-k counts | PROVED: Lemma 1.1; Prop 1.2 (SC(D) ⟹ n_p ≤ D(p) on 𝔐, beyond Burgess if D ≤ p^θ, θ < 1/(4√e)); Cor 1.3 (bounded D fails); Lemma 3.1 (R^{(k)}(m₀²) = 0 for every odd m₀ and every k ≤ ∞). CERTIFIED: μ tails and the L2^𝔐 zero set to 10¹¹ (one engine); cap-k data | bounded D; threshold-free exact mechanisms on 𝔐 (refuted by 9 prime + 18 composite zeros); no L6 ⟹ L5 or L5 ⟹ L4 arrow | explicit-threshold counting; coverings at scales p^{0.15}–p^{2/3}; primality-blind eventual proof on 𝔐; cap rung k ≥ 2 (unproved) |
| WILDCARD | Full Type II family N_II | four screens; numerator ladder K = 4, 8, 12, …; inheritance; rigid slices | PROVED: Lemmas 4.1 (numerator nesting), 4.2 (scaling bijection), 4.3 (twisted T1: for K ≡ 0 (4), N^{(K)}(s m²) = 0 for odd s ∣ K/4 and odd m), 4.4 (n ≡ 3 (4) solved; zeros in S₃). CERTIFIED: no odd prime N_II-zero ≤ 10¹⁰; the only odd non-square zero ≤ 10¹⁰ is 4545 | r-spectrum multiplicativity (false: 4 ∉ ℛ(409)); unconditional inheritance (false: N_II(5) > 0, N_II(4545) = 0) | CONJECTURES CONV-II, CONV-II-15, (MS-II), CONV-II(K); a fixed-p argument using c ≥ 2 and non-squareness (strategy, not forced) |
| STRUCT | Integral BM / descent / fibrations on S_n : 4uBC − u − B = n | Brauer group; local invariants; fibrations; scaling | PROVED Thm A: Br(S)/Br(ℚ) ≅ ℤ/2 (transcendental β_n); étale-BM = BM; **the positive-integral BM set is empty iff n is a square** (k = 4), iff n ∈ □ ∪ 2□ (k = 8). Props B, C | Cor A′: BM (even étale-BM) nonemptiness does not imply a positive integral point (fails at 285 composites and 14 primes; on the C-even model at 1 270 + 12 R₈-zero primes); primality alone does not rescue it | extra fibre/divisor arithmetic; Brauer set of the open S° (unresolved); further hypotheses |
| STRUCT2 | Same on the Type II threefold X_n : 4abcd = a + b + nc | Br, fibrewise BM, 4545 | PROVED Thm B: Br(X)/Br(ℚ) ≅ ℤ/2; **positive-integral BM set empty iff n is a square** (K = 4), iff n ∈ □ ∪ 2□ (K = 8). Lemma C; Prop F (odd n ≥ 1, K = 4, c₀ ≥ 1: fibre c = c₀ obstructed iff s(n) ∣ c₀); Prop T (tautological). Thm 4.1: N_II(4545) = 0 (CERTIFIED), with a nonempty BM set and local points even under ET coprimality (PROVED) | an argument using only BM-nonemptiness plus primality, π₁, Br, local solvability and smoothness, applied verbatim to fixed open-closed local classes, proves false statements (class table, CERTIFIED). Further hypotheses and eventual theorems are not excluded | CONV-II ⟺ IHP_BM for (𝒳_n, Ω) at odd n ≠ 4545; equidistribution / extra arithmetic (possible, not necessary) |
| LOGIC | Arithmetic hierarchy and complexity of (MS) | Π⁰₁ form, Buss witnessing, Shepherdson model, witness extrema | PROVED: Prop 2.1 ((MS) is Π⁰₁; independence ⟹ truth), Prop 2.2; Thm 3.1 / Cor 3.2 (rel. Buss); Lemmas 5.1–5.3; Prop 5.4; Prop 5.5; Thm 6.2 (IOpen ⊬ MS⁺★(P) for every numeral P). CERTIFIED: Mordell-class census to 10¹⁰ incl. composites | polylog (u, C)/(B, C) menus i.o. (modulo the OMEGA13 cited inputs); IOpen + residues (pseudo-squares) | **CONJECTURE (MS⁺)**; CONJECTURE FQ_u(A); growing polylog (u, B) menus (open) |
| DISPROOF | Counterexample search for (MS) | designed progressions (square-class, near-square, avoidance, CRT); zero-law model | PROVED: Lemma 2.1; Lemma 2.2 (square-class shadow, one-way); Lemma 2.3 (line sterility, needs gcd(m, t) = 1); Prop 2.4(i). CERTIFIED: 868 562 sampled primes, no R/𝔊*-zero; new R₈-zeros 20 840 951 041 and 23 296 553 281 | fixed-y square-class designs fade with p (model, Assessment); fixed-offset kills remove O_k(L) mass (conditional) | slowly decaying mixtures, growing offsets, other polynomial families, a non-local "prime T1" |
| LIT | 2024–26 literature audit | ES literature; pointwise divisor-in-class results; square-obstructed structures | Prop I (PROVED): H_d is invariant under x ↦ (4x)⁻¹; fixed-cutoff hit-pattern symmetry (no existence content). CERTIFIED metadata: K-R-K, Akaka v0.8, Ventas, Pomerance–Weingartner (§4) | no direct transfer to (MS) found (Assessment); no pointwise lower bound for divisors of one integer in a growing-modulus class was located | an eventual all-non-square theorem, or one with a finite sporadic exception set, is not excluded by F3 |
| TRYO | Tryhard on (★): fixed characters, least non-residue, sieve | covering of 𝔐 by fixed q; quadratic forms; symbol laws | PROVED: Lemmas 1.1–1.4; Thm 2 (avoiders ≪_A X(log X)^{−A}; already covered in substance by the earlier, stronger Z56_FAMTRY Thm A); Cor 2.1 (short intervals, Huxley); Props 3.1 (prior), 3.2; Lemmas 8.1–8.2; Prop 8.7. **CERTIFIED: (★) at all 355 096 166 primes in 𝔐 ∩ (10¹⁰, 3·10¹¹]** | no-threshold fixed-q covering for each q ∈ [11, 47] (CERTIFIED by the screen zeros); finite (u, B) identities | pointwise forcing for p + u factors; thresholded/eventual variants |
| TRYF | Character-layer decomposition of the hit indicator | L₀ + L₂ + L_r + L_n; Burgess on L₂ | PROVED: Lemmas 1.1, 1.2, 3.1; Thm 2.1 (for every ε ∈ (0, 1/8), primes p ≥ p₀(ε) (applied to p ≡ 1 (4)) and 3 ≤ X ≤ 2p: |S_p(X)| ≤ (1 + 4ε)²(log p)²/64 + O_ε(log p); no numerical onset evaluated). CONDITIONAL Thm 3.2: (★) for all sufficiently large primes p ≡ 1 (24), assuming HCE(δ) for a fixed δ > 0 at all sufficiently large such primes; HCE is a non-standard hypothesis stronger than the target. EVIDENCE: layer tables | no bound for L_r or L_n | a rigorous L_r bound (Shiu + Pólya–Vinogradov looks feasible); L_n open |
| TRYF2 | Hits as divisors of 4pC + 1; surrogate main term | bounded-coordinate constructions; M₂ + E₂ split; vdC/Weil/Erdős–Turán | PROVED: Lemma 1.1, Remark 1.2, Lemma 1.3; Prop 2.1 (for every U, every p ≡ 1 (mod 840·L_U) has no U-local hit); **Thm A: M₂(p) ≥ c₀ log²p for every sufficiently large prime p ≡ 1 (4)** (a surrogate, not R) | constructions whose hits have two uniformly bounded coordinates; the tried exponential-sum methods (Assessment) | pointwise E₂ > −M₂; coupling of hits across C or u |
| TERNARY | Ternary theta / class numbers / Heegner, half-integral weight | genus vs cusp on local square classes; Waldspurger screen | PROVED: Lemma D (Type II ↔ hypercycle incidences). **Thm F** (rel. (S1)–(S5)): a valid ternary-theta proxy with g(ℓ²) = 0 has E = 0 on 𝒞₁(2N), so g(p) = h⊥(p). **Cor F1**: the squares of (ℤ/840)^× are exactly 𝔐, so no genus main term remains at 𝔐-primes p ∤ N when every odd prime divisor of N lies in {3, 5, 7} (general N: extra quadratic-residue conditions). EVIDENCE: Waldspurger screen (15 L-functions) | genus main term on 𝒞₁ for one-nebentypus genus-theta combinations; fixed-embedding bounded recipes outside Mordell-type classes (via POINTWISE_TERNARY Thm 4.1) | cusp-coefficient route with nonvanishing; E1′ thin-set Heegner incidence; off-𝒞₁ classes; prime-only support (no square vanishing); other encodings |
| CONVF | Tryhard on CONV-II / Type II at primes | six divisor faces; a = 1 / c = 1 lines; non-residue, Pell, CRT, norm, character, descent | PROVED: Lemmas 1.1–1.5; Thm 3.1 (sieve; already covered in substance by the stronger Z56_FAMTRY Thm A). CERTIFIED (to 10⁸): no prime zero of full Type II; of the union a = 1 ∪ c = 1; or of c ≤ 3. c ≤ 2 has zeros 102001 and 8 813 281; a = 1 has zeros 193, 2521, 66529. The only odd non-square composite full-family zero ≤ 10⁸ is 4545 | finite fixed triples (Lemma 1.4); §4(A–H) are failed attempts, not barriers | a = 1 line (López) and its union with c = 1; pointwise divisor-in-class |

## 2. The falsifier table across lanes

Screens (`data/z58/screens/README.md`, all CERTIFIED there):
* F1: odd squares, R(m²) = 0.
* F2: C-even / numerator 8, i.e. R₈. There are 12 R₈-zero primes in [10¹⁰, 1.1·10¹⁰], 4 of them in 𝔐; DISPROOF adds two more (§3).
* F3: the 285 non-square composites n ≡ 1 (4), n ≤ 7 999 801, with R(n) = 0.
* F4: known zeros. 14 (★)-zero primes ≤ 10¹⁰ (9 in 𝔐); 38 𝔊*-zero primes (20 in 𝔐); the R₈ zeros.

| Idea family (lane) | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros |
|---|---|---|---|---|
| Fixed-level Hecke proxies ℋ_M (AUTOMORPH) | binds: T1 forces vanishing at p^{2j}, and Thm A then kills a(p) at collision-free primes | line-blind; Thm A also applies to R₈ ≤ R | not used by Thm A; Prop C uses composites only conditionally | any R-proxy must vanish at the 14; B1 is invalid there |
| Ternary theta (TERNARY) | binds via genus densities; Thm F kills the genus term on 𝒞₁(2N), which contains 𝔐 when the odd primes of N lie in {3, 5, 7} | line-blind | not needed for Thm F | the Waldspurger screen constrains R-support only; Type II has witnesses at the 4 𝔐-zeros |
| Integral BM, surface S_n (STRUCT) | **BM detects exactly T1** (n ≥ 1: positive-integral BM set empty iff n = □) | BM does not see C parity; "BM ≠ ∅ ⟹ point" fails at 12 R₈ primes | all 285 have nonempty BM sets: **not BM** | 14 S_n failures; 24 of the 38 𝔊*-zeros are not (★)-zeros |
| Integral BM, threefold X_n (STRUCT2) | BM detects exactly T1 | X_n^{(8)}: same criterion (□ ∪ 2□); all 12 R₈ primes have N^{(8)} points with c > 1 | 284/285 have X_n points; **4545 is the one failure, non-BM** | all 14 and all 38 have N_II ≥ 1 |
| Full Type II statement CONV-II (WILDCARD, CONVF) | N_II(m²) = 0; non-squareness is the hypothesis | full N^{(8)} has 22 prime zeros ≤ 10⁹ (last 35 569); no trap in range | **only 4545** among odd non-squares ≤ 10¹⁰ | witnesses at all 14, 38 and 12 |
| Witness selectors (WITNESS) | the Jacobi obstruction kills fixed-congruence selectors | the rules range over both parities; W must allow odd C | every rule returns "none" at all 285 | no witness at the 14; W needs cutoff ≥ 8 813 281 |
| Function-field model (FFIELD) | passes: R_q(g²) = 0 | no faithful C-parity image; proxy sub-lines have zeros where the full family has none | small-factor enrichment qualitatively matches the integers | fixed n with large q has positive-proportion zeros, so N₀(q) → ∞ |
| Covering / size rungs (LADDER) | the exponent-cap ladder keeps T1 at every k | SC(D) and L2^𝔐 become false R₈ statements above 10¹⁰; the k = 2 cap is not screened out | 18 composite zeros in 𝔐, last 17 401 609 | thresholds P ≥ 8 813 281 for MS(P), P ≥ 17 401 609 for L2^𝔐(P) |
| Mordell sterile points (MORDELL) | no square in H_d or K_{u,B} | sterility passes to the C-even submenu | residue cylinders cannot tell primes from composites | all 14 lie in the 11 survivors mod 840; all 9 in-𝔐 zeros have sterile 1-points |
| Character layers / surrogates (TRYF, TRYF2) | for n = m², on the unit-restricted sum gcd(d, m) = 1, the Jacobi layer cancels the principal layer termwise (non-unit d cannot be hits and are excluded); Pólya–Vinogradov / Burgess non-principality is the square-sensitive step | at R₈ zeros E₂^{even} = −M₂^{even}; only even-C positivity claims whose asserted range includes the zeros are ruled out (HCE's domain p ≡ 1 (24) contains 6 of the 12 original R₈ zeros) | the composite transfer is NOT PROVED (M₂(57) = M₂(105) = 0) | M₂ > 0 at all 14 zeros, so E₂ = −M₂ there; no positivity claimed |
| Logic (LOGIC) | squares are decidable and factorable in P | applies verbatim to R₈; the 𝔐-restricted R₈ rung is false at 10¹⁰ | an S¹₂ proof of (MS) must split (nontrivial factor pair) any composite R-zeros n > 10¹⁷ in 𝔐; not general factoring | each in-domain zero p gives a brute-force Q-refutation (length p^{O(1)}, not poly(log p)) of the rung below it |
| Designed disproof (DISPROOF) | square-class shadow kills only moduli dividing M | found 2 new R₈ zeros; no structural parity conclusion | not in the search domain | engine reproduces the 14; no new R/𝔊* zero |

**Cross-lane lessons** (Assessment unless labelled).
1. **Brauer–Manin sees exactly T1, and nothing else** (PROVED, STRUCT Thm A, STRUCT2 Thm B). For n ≥ 1, on the displayed
   (★) surface and full Type II threefold with the positive real region, the positive-integral BM set is empty iff n is
   a square (numerator 8: n ∈ □ ∪ 2□); without positivity these models have integral points at every n. The listed
   known non-square zeros, on their respective models, are non-BM failures: the 14 prime and 285 composite (★)-zeros,
   the R₈ primes, and 4545 for Type II. Contrast FRONTIER §1 (BL: no BM obstruction on the all-solution surface U_n at
   n ≥ 2): on these models BM does fail at squares, but nonemptiness is not sufficient for a positive integral point.
2. **The composite screen is overwhelmingly a small-prime-factor phenomenon** (CERTIFIED counts, EVIDENCE reading).
   * Of the 285, 265 have a factor 3, 5 or 7 (LADDER, WITNESS), and 270 lie outside 𝔐.
   * Above 10⁸, every composite zero ≤ 10¹⁰ is divisible by 3, 5 or 7 (LOGIC). The non-square composite zeros ≤ 10¹⁰
     coprime to 1155 number 16, the last 17 401 609 (TERNARY).
   * Within 𝔐 there is no non-square zero in (17 401 609, 10¹¹] (LADDER; one engine).
   * Caveat: "all moduli alive" is weak; 897 961 = 443·2027 is a zero.
   * Composite μ-tails in 𝔐 exceed prime ones (≈ 10 %, 22 %, 40 % at D = 10², 10³, 10⁴), while 100-rough composites match
     primes. The small-factor cause is hypothesised, not measured.
   * So the data permit a primality-blind eventual statement on 𝔐: (MS⁺), CONJECTURE. They neither establish it nor show
     that 𝔐 is necessary.
3. **Ternary and automorphic proxies lose their main term on 𝔐.**
   * TERNARY Cor F1 (PROVED): 𝔐 is exactly the square class of (ℤ/840)^×. A valid ternary-theta proxy (one
     nebentypus, genus-theta combination) whose level N has all odd prime divisors in {3, 5, 7} has g(p) = h⊥(p) at every
     𝔐-prime p ∤ N (cusp only). For general N, extra quadratic-residue conditions are required.
   * AUTOMORPH Thm A (PROVED rel. Deligne et al.): each fixed valid (on all n ≡ 1 (4) coprime to M) ℋ_M proxy vanishes
     at a positive-density prime set inside 1 mod 840 that depends on the proxy; no common set is asserted. For
     all-Eisenstein proxies, at every p ≡ 1 (mod lcm(L, 840)). Prime-only support does not give square vanishing and
     is not covered.
   * The surviving routes are cusp/nonvanishing, half-integral weight with distinct Shimura orbits, coefficients outside
     ℋ, and higher depth. These are escape hatches, not leads.
4. **The full Type II target passes all four screens at statement level**, with the single composite exception 4545
   (CERTIFIED ≤ 10¹⁰; WILDCARD, CONVF, STRUCT2).
   * 4545 = 3²·5·101 has local points everywhere, also under ET coprimality, and a nonempty BM set. It is a genuine
     non-BM positive-integral Hasse failure (PROVED + CERTIFIED, STRUCT2 Thm 4.1).
   * PROVED witness constraint: for odd positive n, every positive Type II witness supplies f = 4acd − 1 with
     (n/f) = −1. Assessment / proposed strategy: seek a pointwise Type II construction that uses non-squareness and
     resolves the tied divisor-class event (B2). This is not a necessity theorem about how every proof of CONV-II,
     (MS-II) or ES must be organised; no such mechanism was found.
5. **Every pointwise attempt stops at the same place.** The open steps are: the remainder E₂ > −M₂ (TRYF2); the non-real
   layer L_n and the real layer L_r (TRYF); the residue of the prime factors of p + u (TRYO); the Waldspurger/cusp
   nonvanishing (TERNARY); and the divisor-in-class problem on the a = 1 line (CONVF). Each is B2.

## 3. New certified data

"One engine" means a single production engine. Cross-checks are listed where they exist. None of the large interval
censuses was fully rerun by a second engine. CERTIFIED here denotes the exact finite computation in the cited memo, with
its stated engine and independent-check coverage, not a second full-range census. The DISPROOF sample is fully
independently checked input by input (below), but it is not an interval census.

* **(★) on 𝔐 to 3·10¹¹ (TRYO §8.6; CERTIFIED).**
  * (★) holds at every prime p ∈ 𝔐 with 10¹⁰ < p ≤ 3·10¹¹: 355 096 166 primes in four contiguous runs (58 344 306;
    56 111 206; 121 533 478; 119 107 176), hard = 0, VERIFYFAIL = 0.
  * Engine: trial division, Pollard rho, 12-base Miller–Rabin, 128-bit witness verification.
  * The cross-review checked 8 732 primes in independent slices; the full run was not repeated.
  * This certifies full (★) only, not R₈ and not R_𝔊*.
* **(★) and composites on 𝔐 to 10¹¹ (LADDER §3; CERTIFIED, one engine).**
  * Exact decider on (10⁸, 10¹¹], sieve below; the two engines agree on [10³, 2·10⁷].
  * The non-square zero set of R on 𝔐 up to 10¹¹ is exactly 9 primes (5569, 9601, 83449, 102001, 712321, 1 724 209,
    1 726 201, 5 212 561, 8 813 281) and 18 composites, the last 17 401 609 = 47·370 247.
  * No zero among the 128 491 751 primes and 585 009 682 non-square composites in 𝔐 ∩ (10⁸, 10¹¹].
  * The cross-review decided 42 832 high-range inputs pointwise; it did not run a second full census.
  * μ-tails for primes in 𝔐 (pooled over (10⁸, 10¹¹]): P(μ > 10², 10³, 10⁴) = 0.2103, 0.01292, 1.77·10⁻⁴. These are CERTIFIED counts with
    an EVIDENCE reading; the fitted D* ≈ x^{0.42} is an extrapolation, not a bound.
  * Cap-k data (exhaustive): R^{(2)} ≥ 3 at the 14 prime zeros and at the three largest 𝔐-composite zeros; no rung
    k ≥ 2 is proved.
* **Mordell-class census incl. composites to 10¹⁰ (LOGIC §4; CERTIFIED).**
  * Exhaustive triple sieve. Two implementations agree to 4·10⁹; a single engine beyond, with an independent decider on
    selected inputs. The cross-review resieved to 10⁹.
  * Exactly 18 composite zeros in 𝔐; none in (1.75·10⁷, 10¹⁰]. The non-square composite zeros n ≡ 1 (4) ≤ 10¹⁰ number
    486 in total (TERNARY, same data).
  * Means of R/L² on [10⁷, 10⁸]: primes in 𝔐 0.1246; non-square composites in 𝔐 0.1189.
  * From this: **CONJECTURE (MS⁺)**, R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐. It is consistent
    with LADDER's census to 10¹¹. MS⁺(P) ⟹ (MS) for P ≤ 10¹⁷.
* **Designed disproof search (DISPROOF; CERTIFIED decisions).**
  * 868 562 distinct design and control primes (777 973 in 𝔐), range [10 000 000 033, 7 307 828 669 535 601]. Exact
    enumeration or decision mode; **sampled, not an interval census.** No R- or 𝔊*-zero.
  * Two new R₈-zeros, both ≡ 1 (mod 840): **20 840 951 041** (R = 24) and **23 296 553 281** (R = 36).
  * The cross-review re-certified every prime with an explicit witness.
  * The fitted zero law and the [10¹⁷, 10³¹] tail (120 non-residue slices, truncated) are a scenario estimate
    (EVIDENCE/Assessment), not an upper bound.
* **N_II census (WILDCARD; CERTIFIED).**
  * No odd prime N_II-zero ≤ 10¹⁰. The only odd non-square zero ≤ 10¹⁰ is 4545.
  * Coprime (ET) form: 142 zeros ≤ 10⁸, all divisible by 3 or 5 (137 by 3), the last 21 754 425.
  * Numerator 8: 129 odd non-square zeros ≤ 10⁹ (22 primes, last 35 569; 107 composites, last 1 239 315).
  * The d-odd half has exactly 8 odd non-square zeros ≤ 10⁹ (13, 301, 445, 685, 1981, 3105, 4545, 9121).
  * Cross-review: independent progression sieve through 10⁸. 4545 was confirmed by two independent exhaustive
    enumerations (STRUCT2).
* **Least-witness census (WITNESS; CERTIFIED).**
  * All four orderings for the 25 423 491 primes p ≡ 1 (4) ≤ 10⁹. Records: d 2 953 943 at 85 664 329; q 37 223 480 at
    743 804 881; m3 193 763 at 413 490 001; u 469 at 53 325 721; C 76 141 at 564 661 441; s = 201 at 413 490 001.
  * Extension: all 202 099 784 primes in (10⁹, 10¹⁰], max s = 97.
  * So every prime p ≡ 1 (4) ≤ 10¹⁰ with R ≥ 1 has s ≤ 201 and s ≤ 0.52 log²p.
  * The cross-review reran the 10⁹ census; it did not repeat the full extension witness scan.
  * Dickson instances (CERTIFIED): S = 3 at 94 807 441, 2 682 912 961, 26 678 957 761; none for S = 4 with k ≤ 3·10⁶.
* **Function-field census (FFIELD; CERTIFIED).**
  * q = 3, full family, irreducible/composite/square zeros at n = 4, …, 16: 0/6/9, 3/27/27, 3/48/81, 6/87/243,
    3/67/729, 0/51/2 187, 0/15/6 561.
  * Complete q = 3 irreducible census through degree 18: zeros only at degrees 6–12. The cross-review checked a
    degree-18 slice, not the full degree-18 certification.
  * q = 7 irreducible zeros at n = 4, 6, 8, 10: 49, 280, 707, 938. q = 11 at n = 4, 6: 363, 3 674.
* **Other (CERTIFIED, smaller).**
  * MORDELL: bounded coverings mod 9240 … 19320; S1/S3 brute force for ℓ < 60.
  * CONVF: zero lists of sub-lines to 10⁸ (§1 row).
  * STRUCT2: class table (n < 120 001; primes in [120 001, 400 001)).
  * AUTOMORPH: Prop B1 checked for odd squares m ≤ 20 001.
  * TRYF: stats sieve to 2·10⁸ (84 non-square composite zeros n ≡ 1 (mod 24) up to 2·10⁸, last 162 267 625).

## 4. Literature (LIT; cross-review ACCEPT-WITH-FIXES)

* **Priority item: Kandukoori–Ramesh–Kumar (K-R-K)**, *An improved bound for the exceptional set of the Erdős–Straus
  equation*.
  * **What is verified.**
    * The PDF is dated 2026-07-29 and archived as `data/z58/lit/sources/kandukoori-ramesh-kumar-2026-07-29.pdf`.
    * Its Theorem 1 reads "E(N) ≪ N exp{−c(log N)^{3/4}}" for all N ≥ 3. The same saving holds for exceptional primes.
      Theorem 2 gives E_m(N) for each fixed m ≥ 4, with constants depending on m.
    * No arXiv record was found. It is unrefereed as far as known.
    * The Lean repository's root commit `268ebdbf` is dated 2026-07-30 and already defines the 3/4 saving. At that time
      it was conditional on **nine named analytic axioms**.
    * At HEAD `f6c99eaa` (2026-10-30), CI passes, and five `#print axioms` checks give only Lean's three standard axioms.
      This was verified via the GitHub API. The definitions were read and are faithful.
  * **What is not verified.**
    * The analytic proof was not re-audited.
    * The project was not rebuilt locally (memory budget).
    * Whether the repository was public on 2026-07-30 is unknown, so exact *public* priority is not established.
    * The standard-axioms closure must not be backdated before October.
  * **Consequences** (Assessment).
    * The campaign's `paper/es-threequarter-note.tex` was first committed 2026-09-06. That date dates the file, not the
      discovery. Its abstract ("not aware of an earlier improvement of the exponent 2/3") must be corrected.
    * FRONTIER §1 ("INTERNALLY PROVED") and STATUS must cite K-R-K.
    * `LITERATURE_2026_UPDATE.md` §1 is outdated.
    * The two proofs share an architecture (Type II classes, cubic mass, conditioning). K-R-K corroborates the internal
      result; independence of development is not documented. K-R-K Remark 1.2 is an achievability calculation, not a
      sharpness theorem.
    * Count-note Theorems A–D are **not superseded**. A qualified citation is proposed; it is not applied.
    * Possibly still campaign-new: the interval/progression versions ((D)30) and uniformity in m ((D)31). This needs a
      careful comparison by the paper owner.
    * (MS) relevance: none (a density statement, B6).
* **Akaka v0.8** (Zenodo 22905042, 2026-09-22; CERTIFIED metadata; the theorem is an author claim).
  * The claim: there are absolute constants c, C, X₀ > 0 such that for every real X ≥ X₀ and each integer
    4 ≤ m ≤ (log X)³, at most CmX/(log X)⁴ primes in (X, 2X] have R_II,m(p) < c(log X)³/m.
  * A Lean certificate is claimed; specialist review is outstanding.
  * It counts the full strict Type II family, not the R₈ line. It gives no numerical allowance.
  * The count note's v0.7 auxiliary-family disjointness still holds; the full Type II families are not disjoint.
* **Ventas, arXiv:2610.41027v1 (2026-10-29)**, "Modular Inversion in Mordell Classes".
  * It proves finite hit-pattern invariance under modular inversion: Type I for prime inputs, and coprimality can fail
    for composites.
  * It gives no universal coverage. LIT's Prop I (PROVED) is the (★) analogue, with no existence content.
* **Pomerance–Weingartner** is now *Ramanujan J.* 69 (2026), no. 2, art. 31, DOI 10.1007/s11139-025-01312-2
  (CERTIFIED via Crossref).
* **Searches that came up empty** (Assessment): no pointwise lower bound for divisors of one integer in a class modulo a
  growing modulus (Lenstra and CHN give upper bounds), and no result of the target shape. Dao arXiv:2504.10992 is a
  Markoff-type BM analogue; negative Pell is classical descent.

## 5. Open problems / next steps supported by the memos

None of these is a lead. Each is stated in its memo with its scope.

1. **CONV-II / (MS-II)** (WILDCARD, STRUCT2, CONVF; CONJECTURE).
   * CONV-II: N_II(n) ≥ 1 for every odd non-square n ≠ 4545.
   * (MS-II): N_II(p) ≥ 1 for primes p > 10¹⁷ in 𝔐. (MS) ⟹ (MS-II), and (MS-II) ⟹ ES relative to Mordell + Salez.
   * The statement-level hot target. PROVED witness constraint: every positive Type II witness at odd n has
     f = 4acd − 1 with (n/f) = −1. Proposed strategy (Assessment, not a necessity theorem about proofs): a pointwise
     construction using non-squareness that resolves B2. Using c ≥ 2 is a strategy, not forced at 10¹⁷.
   * Sub-targets: the a = 1 line (López; prime zeros 193, 2521, 66529) and its union with c = 1 (no prime
     zero to 10⁸); CONV-II-15; eventual positivity
     of N^{(K)}; a composite genus analysis without conductor cancellation.
2. **(MS⁺)** (LOGIC, LADDER; CONJECTURE): the primality-blind form on 𝔐 with threshold 17 401 609.
   * A feasible (S¹₂) proof of (MS) yields a polynomial-time hit-or-nontrivial-factor-pair algorithm on n > 10¹⁷ with
     n mod 840 ∈ 𝔐: it must find hits at those primes and split any composite R-zeros there (not general factoring).
   * IOpen plus residues cannot prove MS⁺★(P) (pseudo-squares).
3. **Remainder bounds behind proved surrogates.**
   * TRYF2: E₂(p) > −M₂(p) pointwise.
   * TRYF: a rigorous L_r bound (Shiu + Pólya–Vinogradov suggested); L_n open; HCE is stronger than the target.
   * A mechanism coupling hits across C or u (TRYF2 §5).
4. **Named escape hatches from the scoped no-gos.**
   * AUTOMORPH E1 (half-integral weight, under the conditional class-zero hypothesis), E2 (coefficients outside ℋ), E3
     (higher depth).
   * TERNARY: cusp-coefficient nonvanishing on 𝔐 (Goldfeld-type when the root number is +1), E1′ (a thin-set Heegner
     incidence theorem), off-𝒞₁ classes.
   * STRUCT: the Brauer set of the open S°; fibre arithmetic beyond BM.
   * STRUCT2: an eventual IHP_BM for (𝒳_n, Ω) under further hypotheses; equidistribution as a possible input.
   * MORDELL: the other five Mordell classes; non-polynomial uses of x² + 840y².
5. **Witness size** (WITNESS CONJECTURE W, LOGIC CONJECTURE FQ_u(A)).
   * W: min(u, B, C) ≤ (log p)² for p > 8 813 281.
   * FQ_u(A): u_min ≤ (log p)^A on 𝔐 when R ≥ 1.
   * Growing polylog (u, B) menus are open (LOGIC Prop 5.4).
6. **Function field** (FFIELD): fixed-q eventual MS_q (CONJECTURE); a faithful C-parity / 𝔊* model; any transfer back
   to the integers.
7. **Disproof side** (DISPROOF): slowly decaying mixtures, growing offsets or other polynomial families, and a non-local
   "prime T1" remain unexcluded. The model is not an upper bound.
8. **Literature / papers** (LIT): the K-R-K citation and the 3/4-note abstract; a comparison of (D)30/(D)31 with K-R-K.
   **Needs the user / paper owner.**

## 6. Do-not-export list / caveats

* **ES and (MS) are open.** "HOT TARGET" (WILDCARD) is an Assessment about a statement, not a lead. No lane supplies a
  HOT LEAD. The structured probes report "narrowed"; TRYO, TRYF, TRYF2 and CONVF report no proof / no pointwise
  mechanism, not an exhausted target; WILDCARD reports "strengthened (choice of target) / inconclusive (mechanism)".
  None says "exhausted" or "impossible" beyond its stated scope.
* **Finite data stay finite.** The large interval censuses (TRYO 3·10¹¹, LADDER 10¹¹, LOGIC/WILDCARD/WITNESS 10¹⁰) have
  the engine/cross-check coverage listed in §3. DISPROOF is a sampled search, not a census, and not all 868 562 primes
  are in 𝔐. Every one of its 868 562 inputs was independently checked for primality and for an explicit R/𝔊* witness,
  and both new R₈ zeros were independently exhaustively enumerated. This still gives no interval-wide completeness
  claim. Fitted laws are EVIDENCE: DISPROOF zero law and tail scenario, LADDER D*, WITNESS
  survival fits, WILDCARD Poisson fit. Extrapolations are Assessment and never bounds.
* **Surrogates are not R.**
  * TRYF Thm 2.1 bounds the Jacobi layer and a weighted conditioned expectation.
  * TRYF2 Thm A bounds M₂, whose "expected count" reading assumes unproved coset uniformity.
  * TRYO Thm 2 and CONVF Thm 3.1 are density statements, already covered in substance by the earlier, stronger
    Z56_FAMTRY Thm A.
  * None certifies any individual integer.
* **Scope of each no-go.**
  * AUTOMORPH: fixed ℋ_M only (holomorphic integral weight, twists, specified divisor sums), with validity on all
    n ≡ 1 (4) coprime to M; not prime-only support/equality, prime-only arguments with error outside ℋ, mock forms, or
    signed minorants. The collision-free prime set is per proxy.
  * TERNARY: the unit class 𝒞₁, one nebentypus, genus-theta combinations; prime-only support is not covered. The square obstruction applies at the
    identity's own modulus; finer moduli are not excluded.
  * STRUCT/STRUCT2: *positive-integral* BM on the displayed models. Without positivity there are integral points for
    every n.
  * MORDELL: class 1, sterile fibres, finite menus, global polynomials.
  * FFIELD: fixed degree, large q; the model is an analogy, not a reduction.
  * WITNESS: structural selectors, not arbitrary algorithms.
  * LOGIC: IOpen only, not a general proof barrier.
* **Labels and dependencies.**
  * The memos' failed-attempt sections (CONVF §4, TRYF2 §4–5, TRYO §8.5) record failures, not barriers.
  * MORDELL's genus "blind spot" and L6 readings are EVIDENCE-grade (long double, no enclosures).
  * WILDCARD's composite genus step is heuristic.
  * LOGIC's Ω lower bounds hold modulo the OMEGA13 cited inputs.
  * CONVF's quoted "22 zeros ≤ 10⁹" needs WILDCARD's source and domain (full N^{(8)}, odd non-squares, primes).
* **Literature.** K-R-K is unrefereed. Its Lean closure was CI-verified, not rebuilt, and dates from October, not July.
  Public priority is unverified. Akaka is an author claim. Do not claim the campaign's 3/4 bound as first.
* **Nothing has been posted.** Paper changes are proposals; the user decides.
