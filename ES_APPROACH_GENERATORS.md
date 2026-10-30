# ES_APPROACH_GENERATORS — wave z52: literature scour, approach generators, ranked first problems (2026-10-30)

**ES is OPEN.** Nothing in this wave proves or disproves it, or any new infinite case of it. Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. All internal results are internally reviewed only, not
refereed.

Inputs. Seven literature lanes, `BRAINSTORM/z52_lit_*.md`, graded in `reviews/z52-lit-grading.md`. Two cross-lab deep
lanes on "how are pointwise theorems in thin regimes proved", `BRAINSTORM/z52_deep_thin_pointwise_{opus,astra}.md`. Two
boards, each with fable, astra and argon over 5 rounds:
- generators: `~/.pi/boards/20261030-es-generators/memo.md`;
- weak points: `~/.pi/boards/20261030-es-weakpoints/memo.md`; argon ran out of credits after round 2.

Proofs and cheap tests of the board items are in `Z52_BANKED.md`. Briefs are in `/home/pasky/projects/math/z52briefs/`.

## 0. Bottom line

1. **No new lead that could move ES itself emerged.** No literature item, generator or weak point both implies
   something about ES(p) at a prescribed prime and comes with a credible way to be proved. All three seats of both
   boards said this in their final positions. The cross-lab deep lanes reached the same verdict independently.
2. **Solved meanwhile, and whether it transfers.**
   - Zaremba is claimed in full: Zhang arXiv:2605.02518v2, with Shkredov 2603.14116v2. Both are unrefereed.
   - Small primes generate (ℤ/q)^× for almost all q: Klurman–Shparlinski–Teräväinen 2609.25393.
   - Two primes plus 6 powers of 2 (5 under GRH): Li–Liu 2610.15784.
   - Erdős #306 was solved by a Fourier count: Li 2609.32140.
   - A flea orbit misses the squares plus five sporadic values: Alkauskas 2508.05347.

   **None transfers** (§1). Each rests on one of four things: a power-size witness reservoir, free choice of
   witnesses, averaging, or a long fixed-target character sum. ES at one prime has none of them.
3. **What the wave did produce** (PROVED / CERTIFIED, `Z52_BANKED.md`):
   - a diagnostic theorem next to ES (the pencil theorem, §2 G2);
   - a structural reason why the obvious Brauer class dies exactly at the ES fibre k = 0;
   - one correction to FRONTIER §5.5;
   - the lemma that the genus layer is pointwise free;
   - a ten-fold extension of the I3_𝒞 census, which bears on an ES-strength reformulation;
   - sibling-failure calibrations.

   These sharpen the map. They are not progress on 4/p.
4. **Meta-finding (Assessment, §2 G1).** Every verified theorem that is pointwise in a thin regime gets existence
   from one of two sources:
   - (T) a thick deterministic object of size ≥ n^c with an exact extraction rule;
   - (R) algebraic rigidity.

   ES has no known instance of either. The generator matrix (thick objects at p × extraction rules) is the wave's
   reusable tool for generating approaches. Its two cells with no construction yet are already-listed loopholes:
   growing-level identities ((J)10) and non-affine windmills.

## 1. Literature dossier (verified 2026-10-30; full entries appended to `LITERATURE_2026.md` "Wave z52 additions")

The grader re-opened 118 arXiv records and 11 PDFs and found no hallucinated items. It did find a fabricated title
for Chen's Annals paper, Shkredov's Thm 8 mis-scoped, and five items wrongly labelled "new"; all three are corrected
in the merged files.

| Result (status) | What made it solvable | Does ES share it? | Transfer |
|---|---|---|---|
| Zaremba, all q (Zhang 2605.02518v2 Thm 1.2; Shkredov Thm 8 on class 𝒵 + Rem 9; CLAIMED, unrefereed) | expansion in SL₂(ℤ/q) on Cantor digit sets; count tunable to ≈ q^{2δ−1} by enlarging the alphabet | No: ES₅ word length is fixed at 3, so the count is ≍ log²n and cannot be tuned (B3). Matrices are self-levelled (B2). Expansion also holds at squares, so it is blind to T1 | none; Question R/TG untouched |
| "squares + finitely many sporadic": Rickards–Stange Thm 2.8 (PROVED, fat Ψ, 15 sporadic); HKRS (OPEN); Alkauskas fleas (5 sporadic ≤ 10¹², completeness open); U(n) (6 sporadic ≤ 10⁹) | the only *proved* case uses a long character sum over one target's fibre (an AP of length ≍ n) | No: U(n)'s fibre has expected size log²n. ES₅/U(n) is not known to be an RS orbit or HKRS instance, and the certificate set contains no multiplication-closed subset | a *model of the statement*, not a method. Flea multiplicity ≈ X^{0.31} (EVIDENCE; power regime) |
| Linnik–Goldbach, 2 primes + 6 powers of 2 (Li–Liu 2610.15784) | Goldbach pair reservoir N/log²N | No. The one-prime rungs fail: p + 2^k on an AP (Erdős), p + 2^a + 2^b i.o. (Crocker 1971, Pan 2011). ES failures cannot fill an AP (PROVED: scale ES(q), q ≡ 3 (4), by CRT) | none |
| Subset-product generation of (ℤ/q)^× by (log Q)^{1+ε} small primes, almost all q (KST 2609.25393) | free shared primes, averaging over q; beating it would need Vinogradov's least-QNR conjecture | No: gate G4 needs the prime factors of *one* p-tied integer to hit −1 (B2, §4.9) | none; the "class, not parity" gap is untouched by all literature |
| Erdős #306 (Li 2609.32140; Lean except one inequality) and the 2025–26 AI/Lean crop (#283, #728, #729, #401, #38, #90) | abundance: Fourier counts over exponentially many configurations, or a good m in an interval | No: none has ES's "every n, polylog witnesses" shape | none (calibration: AI+Lean pipelines solve exactly the shapes the barriers allow) |
| Markoff (Chen, Ann. Math. 2024, "Nonabelian level structures, Nielsen equivalence, and Markoff triples"; Kingsbury-Neuschotz 2603.04096 density one, general parameters) | every orbit size ≡ 0 mod p (a divisibility invariant) + giant component | No group acts on U_n(ℤ); no orbit-size invariant | none |
| Direct ES: Cao–Xu 2610.32302 (56 families, tested to 10¹¹, unproved by the authors' own statement) | — | — | unproved cover; B1 not shown to apply (unbounded parameters) |
| Covering systems: Filaseta–Kalogirou–Klein 2610.34541, Hashimoto 2603.26043 | finite-system structure theory | No (B1) | none |

Deep-lane catalogue (40 + 23 entries): Zagier, Thue, Pell, Chevalley–Warning, Alon CN, Huang, Ramaré–Walker, LLS, CLB
palindromes, Bang–Zsigmondy, … Every thin-count pointwise theorem falls under (T) or (R). The thin-count statements
with neither are false or open: p + 2^k, p + 2^a + 2^b, p + 2k² (5777, 5993), Markoff k (Ghosh–Sarnak), three cubes,
and ES.

## 2. Generators (each: what · non-obvious input · why not already dead · first lemma · how it fails · z52 status)

**G1. Thick object × extraction rule (the generator matrix).**
`BRAINSTORM/z52_deep_thin_pointwise_opus.md` §2.0.
- *What.* The rows are the thick objects available at p:
  - trial pairs;
  - divisor sets of 4Cp + 1;
  - the modular hyperbola;
  - HJ/CF data;
  - class groups;
  - the lattices L_ρ;
  - Zagier-type sets X(p);
  - SL₂ words.

  The columns are the extraction rules: collision, parity or count congruence, descent, interlacing, exact charge
  identity, inhomogeneous covering, orbit, size squeeze.
- *Non-obvious input.* Precedents (Zagier, Huang, Dirichlet) never estimate the witness count. They need a thick
  object, an exact rule, and one step that is false at squares.
- *Why not dead.* B1–B9 are scoped to constructions, not cells.
- *First lemma.* Any new row or column must be run against the whole matrix first.
- *Tested this wave (PROVED, scoped negatives):*
  - complement pairing makes every level count even, and R(p)/2 mod 2 behaves like a coin (49.9 % / 51.0 %);
  - the Dedekind–HJ discharging charge is χ-blind;
  - multiplicative χ-cliques are cosets, so Hoffman/Huang bounds that depend only on |A| do not apply;
  - homogenised Chevalley–Warning counts are numerator-blind.
- *Open cells.* Growing-level exact identities ((J)10) and non-affine or infinite windmill menus (INVOLUTION_ES2).
  Neither has a concrete construction. Digit-carry algorithms with unbounded loops (the B1 E2 hatch) are unscreened.

**G2. Constant-term deformation: the pencil S_{n,k} : 4xyz − n(xy+yz+zx) = k** (fable-7 → `Z52_BANKED.md` §1(a)).
- **Theorem (PROVED).** Let k = m². Suppose n ≡ 1 (8) if m is even and n ≡ 5 (8) if m is odd, and (n/ℓ) = 1 for
  every odd prime ℓ | m.
  - Then S_{n,k}(ℕ) = ∅.
  - The class 𝒜 = (−q, −d) ∈ Br S_{n,k}, with q = 4y − n and d = qz − ny, is a Brauer–Manin obstruction to
    *positive integral* points.
  - The surface is locally soluble at every place.
  - Each square k gives a positive-density set of such n.
  - The repo had not recorded this regime before. The literature search found no prior treatment of k ≠ 0
    fibres; this is a search result, not a proof of novelty, and the method is standard.
- **Why it dies at k = 0 (PROVED).** The step "ℓ | d ⇒ −q is a square mod ℓ" uses the term kq of dd′ = n²y² + kq.
  At k = 0 the fibre is singular. On blowing up the origin, 𝒜 has residue (the class of n) along the exceptional
  conic, so for non-square n it does not extend to Br U_n. For square n the residue vanishes.
- *Reading (Assessment).* The hypotheses "(n/ℓ) = 1 for all ℓ | m" read at m = 0 give "n is a QR at every prime",
  i.e. n is a square. This is the T1 pattern seen as a degenerate limit. It explains structurally why primes escape
  this BM mechanism. It supplies no transport to k = 0: scaling preserves k/n³, and the fibres are coprime at fixed y.
- *Data (CERTIFIED).* Unexplained zeros remain: S_{3861,4}(ℕ) = ∅ (n ≡ 5 (8)). The zeros of S_{n,1} at n ≡ 1 (8)
  up to 10⁵ number twenty, all divisible by 3.
- *How it fails as a generator.* There is no k → 0 transport (conceded by fable). It is a disproof-shape
  calibration for FRONTIER §7.15, not a proof route.

**G3. Conservative ring extensions and the conjugate-pair shadow** (fable-2/3, argon-4).
- *What.* ES_Q1 over ℤ[i] is ES with denominators in the closed first quadrant. It is conservative: real n have only
  ℕ³ solutions. It has genuine prime failures at 2+5i, 4+5i, 5+6i, 10+13i, 2+17i and 8+73i (N ≤ 10⁴, three code
  paths).
- *z52 test (CERTIFIED).* There are no failures for 10⁴ < N ≤ 10⁶ (38 566 primes). The count grows like log³N, not
  the board's log²N (EVIDENCE, finite range). All six failures have Im n ≡ 1 (4), a low-count cell; no invariant
  was found.
- *Fable-3 (PROVED, sufficient direction).* A ring extension in which ES becomes easy does so through a Galois-stable
  pair 1/β + 1/β̄. "Necessary" is false: ℤ[1/3] needs no pair.
- *How it fails.* Conservative on ℝ means every real statement is ES verbatim (sustained objection). The non-real
  failures are a sibling lottery. ℤ[√2] alternating pair-unit moves (astra-2) are the one open existence question:
  multi-step paths are unanalysed, and every seat rates it low probability.

**G4. Failure-calibrated siblings** (fable-6; `Z52_BANKED.md` T2–T4).
- *What.* ES-shaped lotteries with known failures: S_{n,−4}, ES_Q1, 8/n, TES. They are used to fit the zero law
  behind "P(ES false)".
- *Status after z52 (CERTIFIED).* S_{n,−4} fails for 2 ≤ n ≤ 10⁵ only at {2, 9, 21, 165, 945, 1197}, all odd ones
  ≡ 0 (3), in a low-count local cell; it has a log² count scale.
- *Finding (Assessment).* Both siblings fail *less* often than the (J)97 zero law predicts: 6 Gaussian failures
  observed against ≈ 20 predicted (N ≤ 10⁶), and 5 S_{n,−4} failures at n ≡ 1 (4) against ≈ 37 (n ≤ 10⁵). No "prime T1 in a sibling" appeared. The
  law was fitted on a different normalisation, so this is a calibration mismatch, not a rejection.

**G5. Barrier-artefact audit (presentation vs genuine).**
- *(a) Category artefact (CERTIFIED).* Under the *coprime* Type I/II definition that FRONTIER §1 uses, "Type I ∪
  Type II empty ⟺ n square" is false at 105, 345, 561 and 5985. The repo's SQ (O146, (J)1) was stated for ET
  N-points with no coprimality and is **not refuted**: FRONTIER §5.5 mis-transcribed it, and that line is fixed this
  wave. Coprime ES ⇒ coprime ES₅ fails at 3985; all its five-slot words have gcd(uv, n) = 5 (re-checked by the
  parent). At primes nothing changes.
- *(b) Genus layer (GT1 lemma, PROVED rel. Dirichlet).* Every non-square n ≡ 1 (4) has a genus-free level t = 4r, so
  T1's genus form bites only at squares. Only the *class* of the divisor remains: FRONTIER §4 line 9, now with the
  genus layer proved free pointwise as well as the BM layer ((J)103).
- *(c) Kneser at a failing forced window (PROVED).* 1 ≤ Ω_out ≤ d − 2 for both stabilisers, and at q = 7 a failing
  window forces p ≡ 5 (mod 7). The fable within-class test shows the failure profile carries nothing beyond p mod M,
  so there is no escape.
- *(d) Fixed-q forcing line.* F_q, "(q/p) = −1 ⟹ ES(p)", is open from q = **11**, not 17: the sterile point x** has
  (2/11) = −1, so x** lies in the non-residue cell for q = 11. Scope correction to the wave brief: "ES(p) when
  n₂(p) ≤ 13" is a statement about the *generic point* of the least-QNR line. For all primes with n₂(p) ∈ {11, 13}
  no covering theorem is claimed; classically n₂(p) ∈ {3, 5, 7} is covered (`EXSET_CHAR_FORCING.md` §7.1).

**Killed this wave (one line each; details in the memos):**
- support-disjoint norm descent (a sub-event of (★); 0 survivors at the hard primes);
- carry-aware base-q function-field lift (reduces to an interval search);
- remainder rays and parabola completion (coordinate changes of known slices);
- the odd-prime δ-fold (one certificate written twice);
- the Δ-harmonic ℤ[i] bridge (counterexample π = 3+2i);
- Angular-Pinching (counterexample 4/(3+8i) = 1/(1+3i) + 1/(17+21i) + 1/(3+8i));
- the global Alternation Trap;
- the I3 sign-ladder thin tail (a counting artefact);
- the GRH-forcing "equivalence" as a lead (one line, no information);
- "prime T1 closed" (a cap-∞ restatement);
- the Lenstra/Bernstein dichotomy as new (prior art, `s3_lll_lenstra.md`).

## 3. Ranked slate: first problems and weak points (Assessment)

Ranking is by (information about ES itself) × (tractability). **None is expected to prove ES.** Items 1–3 are
ES-strength; items 4–8 are calibration or loophole probes.

1. **Question R / Hypothesis TG** (FRONTIER §7.11).
   - *Why it moves ES.* It is the exact Rickards–Stange form of T1 on the self-levelled words that are ES₅
     certificates. z52 confirms it as the hinge: the full-Zaremba claims, KST, Alkauskas and HKRS follow-ups leave it
     untouched.
   - *Tractability.* Low. No thin-orbit local–global theorem exists anywhere in the literature surveyed.
   - *Cheap test.* Use the flea orbit (decidable, obstructed, power-count) as a control set for the reciprocity
     singular series of QUESTION_R §3. The z52 by-product was inconclusive.
2. **I3_𝒞 conjecture.** Every prime p ≡ 1 (4), p > 2521, has a word tuv − u − v = p with t, u, v ≥ 3 and a
   coordinate in 4ℤ ∪ (8ℤ − p).
   - *Why it moves ES.* It implies ES₅(p) and hence ES(p) (PROVED, five slot identities).
   - *Status.* CERTIFIED to 10⁹: the zeros are exactly {5, 13, 17, 2521}, and the least certifying interior endpoint
     is u ≤ 39 throughout.
   - *Tractability.* Low; it is B2 again. A fixed u-menu fails i.o. under Dickson. Prop 3.2(b) (PROVED): for a
     Mordell-hard p, a u = 3 interior word exists ⟺ (p+3)/4 is composite.
   - *Cheap next test.* The growth of the least u over primes to 10¹⁰. Does max u grow like log p, or stay bounded
     in range?
3. **Growing-level exact identities** ((J)10; open cell of G1).
   - *Why.* It is the only (T)/(R)-type cell where positivity at one p could come from an exact formula. The
     T1-respecting W(n) identity exists; its positivity is the spin event.
   - *Tractability.* Unknown; no construction exists.
   - *Cheap test.* Search for an identity at level growing with p whose terms are individually signed by (·/p), on
     p < 10⁴.
4. **Non-affine thick windmills** (open cell of G1; INVOLUTION_ES2 bars finite affine menus only).
   - *What it needs.* An involution on a set of size ≍ p whose fixed points are certificates and whose parity is
     computable.
   - *Status.* The simplest mod-2 laws fail (z52 §2.1); weighted and odd-modulus counts remain.
   - *Cheap test.* Enumerate the involutions generated by the slice symmetries on X(p) for p < 10⁴, and test the
     fixed-point parity against R(p).
5. **Br S_{n,k}/Br ℚ in full, and its degeneration at k = 0** (G2).
   - *Why.* It identifies exactly which reciprocity mechanism ES escapes, and turns "no prime T1" into a statement
     about one degenerating class.
   - *Tractability.* High (algebraic geometry).
   - *Cheap tests.* Explain S_{3861,4}(ℕ) = ∅, and the divisibility by 3 of every S_{n,1} zero at n ≡ 1 (8).
6. **Sibling zero-law recalibration** (G4).
   - *Why.* Fitting one law on the ES cells and on S_{n,−4}, ES_Q1 and 8/n would turn the model risk "P(ES false)"
     into a falsifiable statement. Both siblings currently fail less often than predicted.
   - *Tractability.* High; it is computational.
   - *Cheap test.* Refit (J)97's P(0) on the per-cell means of all four siblings with the same normalisation.
7. **F₁₁: "(11/p) = −1 ⟹ ES(p)"** (G5(d)).
   - *Why.* It is the first open fixed-q forcing statement, and it is a pointwise implication at prescribed p.
   - *Tractability.* Very low by B1: the sterile point x** blocks every finite covering. It needs non-congruence
     input.
   - *Cheap test.* None beyond the existing sterile-point certification.
8. **Watch item, external.** The first proof of the HKRS *revised* local–global conjecture (or the Alkauskas flea
   completeness) for any thin orbit would be the first literature input that could transfer to U(n) or Question R.
   Track arXiv citers of 2307.02749 and 2401.01860.

**Recommended next wave (Assessment).** Do not launch another attack lane on ES or on densities from this slate. The
evidence of z50–z52 says the missing ingredient is a new extraction rule (G1). If the user wants a wave, the cheapest
informative one is a two-lane probe:
- Lane 1: item 5 (Br S_{n,k} and the k → 0 degeneration; one lane, algebraic, likely to finish).
- Lane 2: item 3 or item 4 (one serious attempt at a growing-level identity or a non-affine windmill, with a hard
  drop-condition on p < 10⁴).

Otherwise bank z52 and pause.
