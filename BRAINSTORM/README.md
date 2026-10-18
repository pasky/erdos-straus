# BRAINSTORM/ — index of the brainstorm phase (O140–O155), with triage calibration (O156/O157)

Index compiled by O160 from the memos, `reviews/triage-brainstorm-A.md` (O156, memos a–i) and
`reviews/triage-brainstorm-B.md` (O157, memos j–z plus corr/adv/tech; its §1 paragraphs are verbatim copies of
`reviews/triage-B-parts/part*.md`). **ES is not solved anywhere in this directory.** No memo proves any case of ES.

## How to read the table
* **memo verdict**: the memo's own verdict line, abbreviated.
* **validity**: triage verdict-validity on the memo's own verdict: AGREE / PARTIAL / DISAGREE.
* **calibrated verdict**: the verdict to cite. Triage B §0.1 found that every DISAGREE, and several PARTIALs, are
  *scope overreach* of a barrier citation: the memo shows that one displayed instantiation (a fixed slice, form,
  ambient set or power-error asymptotic) collapses, then writes "COLLAPSES" for the whole angle. The cited barriers
  are narrower: redteam-automorphic-2 Thm 2.2(iii) needs Θ₀ fixed independently of p (and is CONDITIONAL on H);
  CONDITIONAL_ES Prop 2.3 bounds main terms only (Remark 2.4 keeps "small main term + smaller error" open);
  LONGSHOT_PIGEONHOLE Thm 2.2 covers transparent coset-covering certificates only; LONGSHOT_FIBRED Thm 3.1 covers
  arithmetic-group orbits with a covolume count only. In those cases the index says
  **PARTIAL → H-x (displayed instantiation collapses)**. This is a wording correction, not a discovery: no memo
  contains a mechanism that escapes the barriers *and* has a plausible arithmetic input.
* **hatch**: the open escape hatch the residue reduces to (O132 §3 / STATUS.md): H-A growing family Θ(p) with moving
  modulus; H-B parity-breaking divisor count at fixed p; H-D non-abelian/higher-rank data; H-E signed/exact positive
  identities; H-F integral geometry beyond BM; H-G (Type I ∪ II, descent) is "not an escape". "none" = no live residue.
* **promise**: triage score 0–5. Nothing scored above 2.
* **errata**: memos with a `## Errata (triage O156/O157)` section appended at the end (verified by
  `scripts/errata_check.py`).

## Half A (triage O156): all 24 AGREE

| file | task | angle | memo verdict | validity | promise | hatch | by-products (labels per triage) | errata |
|---|---|---|---|---|---|---|---|---|
| addcomb_unit_fraction_density | O142 | Bloom-type additive combinatorics of unit fractions | COLLAPSES B3 | AGREE | 0 | none | none new (ET §2) | — |
| anal_dirichlet_series | O151a | Dirichlet series D_f over primes, continuation | COLLAPSES B6/T7, 3/4 ceiling; B2/H-E | AGREE | 0 | none | Prop A.1 PROVED (tautological); Prop A.2 overclaimed (see errata) | ✓ |
| anal_euler_product_law | O151c | Euler-product law of f in Legendre symbols | COLLAPSES B1 | AGREE | 1 | none | β·log p ≈ const law: EVIDENCE (expected from Haar model); averaged CONJECTURE | — |
| anal_moments_structured | O151b | moments of f; structured complements | COLLAPSES B3/B6, B1/B4, B2 | AGREE | 1 | H-A (EVIDENCE only) | Prop B.1 PROVED, folklore; variance-law numerics EVIDENCE | — |
| apollonian_reciprocity | O144b | HKRS/Apollonian reciprocity obstructions vs BM | COLLAPSES as route / PARTIAL as structure | AGREE | 1 | none (H-F screened) | Prop B.1/B.2 low-novelty readings of BL; quartic test EVIDENCE (null) | — |
| canonical_invariants | O153 W1 | canonical seeds (units, Cornacchia reps) | COLLAPSES (B3 units, B2 reps) | AGREE | 1 | H-D (untested unit-residue test) | Lemma A, Prop C folklore; Prop B PROVED | — |
| cayley_markoff_cm | O143 | Cayley cubic / Markoff moves / CM | PARTIAL / COLLAPSES B2 at fixed (K,β) | AGREE | 1 | none | P1/P2 classical; P4 CM dictionary plausibly new (relabelling) | — |
| covering_distortion_dual | O150c | covering systems, distortion duality | COLLAPSES B1/B6 | AGREE | 0 | none (Haar-side only) | dictionary, exposition | — |
| elliptic_fibration_es | O143 | elliptic pencil C_N, MW rank | COLLAPSES (integrality vs rationality; B2) | AGREE | 1 | none | fibre table probably known; per-point non-torsion is PROVED via Mazur (memo under-claims) | ✓ |
| farey_chain_frieze | O144 | Farey chains / friezes | PARTIAL (reformulation) / COLLAPSES B2 | AGREE | 0 | none | Lemma C.0 / Prop C.1 PROVED, folklore repackaging of ET SL₂ | — |
| farey_ford_cf | O144a | Ford circles, continued fractions, Zaremba | COLLAPSES B2/B1 | AGREE | 0 | none | restatement of ET Prop 2.2 | — |
| ff_erdos_straus | O140a | ES over F_q[t] | PARTIAL (no route) | AGREE | 1 (2 as FF curiosity) | none (FF-only) | Thm 2.1, Prop 4.1 PROVED, plausibly new, inert for ES | ✓ |
| gon_fermat_certificates | O148a | geometry-of-numbers / Fermat certificates | COLLAPSES B2 at "F ≡ t (M) ⇒ F = t" | AGREE | 2 | H-A (lattice clothing) | Lemma 3.1 folklore; "escapes B1/B3, not B2" screen plausibly new bookkeeping | — |
| gon_incidence_kloosterman | O148c | incidence / Kloosterman over boxes | COLLAPSES (all five) | AGREE | 1 | H-A | compact forms folklore; box census EVIDENCE | — |
| gon_lll_relation_lattice | O148b | LLL / relation lattice of e-slice | (b1) COLLAPSES, (b2) PARTIAL | AGREE | 1 | H-A | (b2) split restates PIGEONHOLE 1.1; "genus half is a theorem" mislabelled PROVED (see errata) | ✓ |
| graph_cayley_moves | O150a | chord/secant moves on the ES cubic | COLLAPSES B1 (M1–M3), B2 (M4) | AGREE | 0 | none | Thm A.1/A.2 PROVED, plausibly new, inert | — |
| greedy_algorithm_dynamics | O150b | greedy/Engel/Golomb algorithms | COLLAPSES B1; growing J → B2 | AGREE | 0 | H-A (X_win(C)) | Prop B.1 folklore; B.2 dictionary | — |
| hardness_law | O153 W2 | hardness law r ∝ L^{−0.37} | PARTIAL (EVIDENCE law) / COLLAPSES B2 as route | AGREE | 1 | none | law: EVIDENCE; fixed-exponent extrapolation pessimistic (see errata) | ✓ |
| ident_form_families | O145b | polynomial identity families on binary forms | PARTIAL | AGREE | 2 | H-E (two-variable identities) | Prop 3.2/3.4 plausibly new, PROVED; k=21/37 hard-prime families (verified); Lemma 3.1(a) small barrier extension | — |
| ident_invariants | O145a | class numbers, units as invariants | COLLAPSES B2 (B1 for h(−4p)) | AGREE | 0 | none | Lemma 3.1 folklore, diagonal scope only (see errata); null regressions EVIDENCE | ✓ |
| ident_numerators | O145c | m/n numerators, class of one | COLLAPSES B1 | AGREE | 0 | none | Lemma 3.1 = Schuh/TRANSFER 5.1(ii); m=12 tail EVIDENCE | — |
| invol_sign_identities | O152c | sign/parity identities | COLLAPSES; Prop S | AGREE | 0 | H-E (via windmill) | Prop S PROVED, elementary, plausibly new as stated | — |
| invol_topological | O152b | Euler characteristic / Smith theory on solution complex | COLLAPSES | AGREE | 0 | none | Prop K trivial | — |
| invol_windmill_signature | O152a | windmill-type involution, GF(2) signatures | UNCLEAR → leaning COLLAPSES as programme | AGREE | 2 | H-E (parity identity; only route outside every proved barrier) | (W) framing, E4 set plausibly new; nulls EVIDENCE (re-run on n ≡ 1 (24) by O156: null) | — |

## Half B (triage O157): 9 DISAGREE, 17 PARTIAL, 1 AGREE

| file | task | angle | memo verdict | validity | calibrated verdict | promise | hatch | by-products (labels per triage) | errata |
|---|---|---|---|---|---|---|---|---|---|
| adv_new_drivers | O154 | new global drivers (character tail, regulator, CF period) of f_II | COLLAPSES B1+B2 | PARTIAL | PARTIAL → H-A (only linear signal tested) | 1 | H-A | {a,c} identity PROVED but already in Lemma 2.1; ranking EVIDENCE; feature mislabel, conclusions unchanged on re-run (see errata) | ✓ |
| adv_stacked_primes | O154 | adversarial primes with many small QR | COLLAPSES at "drive count below 1" | PARTIAL | PARTIAL → H-A (displayed adversaries collapse) | 2 | H-A | none PROVED; dataset/saturation EVIDENCE only; D3 false (see errata) | ✓ |
| corr_joint_factorisation | O146 | joint factorisation correlations; SQ | COLLAPSES B5 at "forcing", PARTIAL | PARTIAL | PARTIAL → H-A (identity-only forcing collapses) | 2 | H-A | C1/C2 classical; Prop 3.1 folklore; V-emptiness certificates at 288/336 plausibly new for V (already W-escapes); SQ CONJECTURE | — |
| corr_parity_layers | O146 | sign layer vs size layer of parity | B3 COLLAPSES in size layer | PARTIAL | PARTIAL → H-B (size-layer exclusion is heuristic) | 2 | H-B | partition folklore; table EVIDENCE; §1 partition overlap (see errata) | ✓ |
| corr_typeI_typeII_joint | O146 | Type I/II joint emptiness via correlations | COLLAPSES ("no hedge exists") | DISAGREE | PARTIAL → H-A (displayed instantiation collapses); "no hedge" withdrawn | 1 | H-A (H-G) | Lemma 3.1 folklore; joint-count data EVIDENCE about positive values only | ✓ |
| logic_complexity | O141 | computational complexity of ES witnesses | PARTIAL | PARTIAL | PARTIAL → H-A (FQ open) | 1 | H-A | FQ ⇒ FP^FACTOR folklore-valid; "not FP" upgrade unjustified (see errata) | ✓ |
| logic_divisibility_lgp | O141 | local-global for divisibility formulas | COLLAPSES B5/B2 | DISAGREE | PARTIAL → H-A (displayed instantiation collapses) | 1 | H-A | CRT substitution false (see errata); D2 folklore | ✓ |
| logic_ominimal | O141 | o-minimality / Pila–Wilkie | COLLAPSES | PARTIAL | PARTIAL → none (displayed region/estimate collapses) | 0 | none | none (see errata) | ✓ |
| logic_weak_arithmetic | O141 | weak arithmetic (IOpen) nonprovability | PARTIAL | PARTIAL | PARTIAL | 1 | none | Thm S, C1, C4 equivalence plausibly new elementary model theory (PROVED); C4 unit-only claim needs ES in base (see errata) | ✓ |
| markoff_hasse_failures_vs_es | O143 | Ghosh–Sarnak Hasse failures vs ES | COLLAPSES B2/B6 | PARTIAL | PARTIAL → H-F (direct GS transfer collapses) | 1 | H-F | F3/F5 known; F2/F4 EVIDENCE; F5 size claim false (see errata) | ✓ |
| nonab_frobenius_redei | O147 | non-abelian Frobenius / Rédei | COLLAPSES B2 (D1), B1/B5 (D3/D2) | DISAGREE | PARTIAL → H-D (polynomial gating collapses) | 2 | H-D | D1 Artin dictionary folklore; D2 false as universalised (see errata); T1-invisible classes in A₅ (triage B §0.4) | ✓ |
| nonab_homogeneous_dynamics | O147 | homogeneous dynamics / equidistribution on quadrics | COLLAPSES B3 at "error ≤ main term" | PARTIAL | PARTIAL → H-A (displayed power-error estimates collapse) | 1 | H-A | Prop P folklore; H1 mislabelled (see errata) | ✓ |
| nonab_motivic_pointcounts | O147 | motivic point counts, cohomology of U_n | COLLAPSES at "attach Galois rep" | PARTIAL | PARTIAL → H-D (constant family collapses) | 1 | H-D | Prop 3.1 folklore after char-2 correction (see errata); Prop 3.3 EVIDENCE | ✓ |
| noncounting_shapes | O153 | non-counting proof shapes (compactness, profinite) | COLLAPSES | DISAGREE | PARTIAL → H-A (displayed shapes collapse) | 1 | H-A | Prop 1–3 known/folklore; §3 Q ≍ p claim false (see errata) | ✓ |
| other_rings | O140 | ES over other rings (real quadratic O_K) | PARTIAL | AGREE | PARTIAL | 1 | none | Lemma 3.1, Prop 3.2 folklore; Prop 3.3 plausibly new (needs N(ε) = −1); "exactly when" principle is Assessment (see errata) | ✓ |
| padic_adelic_scaling | O149 | p-adic/adelic scaling | COLLAPSES B1, B2/B6 | DISAGREE | PARTIAL → H-F (displayed instantiation collapses) | 1 | H-F | Prop A folklore; Prop B false (see errata) | ✓ |
| padic_functionfield_igusa | O149 | Igusa zeta / function-field transfer | COLLAPSES | PARTIAL | PARTIAL → H-A (fixed-place argument collapses; FF test bed open) | 2 | H-A | §3.3(i) folklore; odd-square obstruction does not transfer (see errata) | ✓ |
| polynomial_method | O140 | polynomial method (CHN, Combinatorial Nullstellensatz) | COLLAPSES (b1–b3) | DISAGREE | PARTIAL → H-A (displayed instantiation collapses) | 2 | H-A | none; "full ratio set needed" false (see errata) | ✓ |
| prob_lll_fixed_p | O142 | Lovász Local Lemma at fixed p | COLLAPSES (B2/B1/B6) | DISAGREE | PARTIAL → H-A (displayed instantiation collapses) | 2 | H-A | atom lemma folklore; Prop 3.2/Rem 3.3 false (see errata) | ✓ |
| prob_lottery_model | O142 | lottery/Poisson model of f_II | COLLAPSES as proof route | PARTIAL | PARTIAL → H-A (averaged model collapses) | 1 | H-A | five empirical findings EVIDENCE; X_e normalisation (see errata) | ✓ |
| rational_to_integral_cubic | O143 | rational → integral points on the cubic | COLLAPSES (M1–M4) | DISAGREE | PARTIAL → H-F (displayed instantiation collapses) | 2 | H-F | M2 PROVED, folklore; M3(b) false (see errata) | ✓ |
| tech_maynard_theta | O155 | Maynard sieve / theta weights | COLLAPSES B3 | DISAGREE | PARTIAL → H-A (displayed instantiation collapses) | 2 | H-A (H-B) | Lemma 1.1 PROVED folklore; Maynard misquote and N log³N (see errata) | ✓ |
| tech_smooth_level | O155 | smooth moduli / level of distribution | COLLAPSES | PARTIAL | PARTIAL → H-B (fixed-architecture cap collapses) | 1 | H-B | none; coverage EVIDENCE; §2 BFI/Zhang conflation (see errata) | ✓ |
| technique_transfer_list | O155 | 18-item technique transfer list | (items) collapse | PARTIAL | PARTIAL → H-A/H-B (off-the-shelf transfers collapse) | 2 | H-A | none; frame equivalence and item 13 false (see errata) | ✓ |
| thin_group_orbits | O144 | thin groups / affine sieve | COLLAPSES B3 | PARTIAL | PARTIAL → H-F (affine sieve collapses) | 1 | H-F | §3 finiteness, matrix identities known; nonsquare analogue Assessment; §4 pointwise-mass claim unsupported (see errata) | ✓ |
| tropical_newton | O149 | tropical geometry / Newton polygons | COLLAPSES B1/B2 | PARTIAL | PARTIAL → H-F (single Newton polygon collapses) | 1 | H-F | T1 folklore; T2 elementary; "never residue classes" scoped to one polygon (see errata) | ✓ |
| wildcard_list | O153 | wildcard pre-screens W1–W18 | pre-screens (Assessment) | PARTIAL | PARTIAL → H-A (W4/W15/W6/W7/W18 not excluded) | 2 | H-A | none; W1 premise false (see errata) | ✓ |

## Spark relay C (O176, untriaged): building on the O172 "T1 = Diff-parity" dictionary; deep file DIFF_DEEP.md

Self-assessed (not yet triaged). Memo prefix `bsC_`; scripts `scripts/bsC_*`.

| file | angle | memo verdict | promise | hatch | by-products (labels) |
|---|---|---|---|---|---|
| bsC_supersingular_transfer | ES as "some supersingular curve mod p has a certificate configuration" | COLLAPSES (B2): ∃E is genus-vacuous | 1 | H-A | Thm 1 transfer PROVED; Type I on p^{o(1)} curves (∀E false) PROVED rel. ET; Kaneko near-extremality EVIDENCE |
| bsC_eichler_orientation | ES congruence as level structure (Eichler orientation; involution on E[4cd]) | Type I COLLAPSES (B2); Type II → DIFF_DEEP | 2 | H-A | Eichler-order dictionary PROVED; deterministic lift nrd x ≡ −1 (M) on every curve PROVED |
| bsC_parity_quadratic_only | unitary / big-CM Diff-parity over any base field (O172 spark 4) | PROVED obstruction | 1 | none | Prop 1 (parity over any base = one quadratic Dirichlet character) PROVED; M \| 24 slices miss 71/9732 p ≡ 1 (24) < 10⁶ EVIDENCE |
| bsC_valence_borcherds | valence formula / Borcherds products as existence engine | COLLAPSES (B2/B3) | 0–1 | H-A | Galois-orbit obstruction PROVED rel. Siegel + ET; Type II certificate = Heegner point of Z(−4Mcp, 0) on X₀(M) |
| bsC_fourier_jacobi | certificate indices as Jacobi coefficients (O172 spark 3) | COLLAPSES (B1/B6, B2) | 0 | none | least Jacobi index records to 10⁶ EVIDENCE |
| bsC_isogeny_ramanujan | Pizer Ramanujan graphs / large-degree isogeny existence | COLLAPSES (B3, B2) | 0 | none | none new |
| bsC_arithmetic_topology | Morishita knots-and-primes: T1 = mod-2 linking, ES = ℤ/φ(M) linking of a sub-link | dictionary only | 0 | none | none |
| bsC_typeII_commutative | Type II as (2ad + k)(2bd + k) = de(1 + 2ck) in ℤ[√−dn] | PROVED identity, no mechanism | 1 | none | identity checked on 336357 tuples |

## Spark relay D (O177, untriaged): higher-order reciprocity escape and (LD_p); deep file LDP_DEEP.md

Self-assessed (not yet triaged). Memo prefix `bsD_`; scripts `scripts/bsD_*`.

| file | angle | memo verdict | promise | hatch | by-products (labels) |
|---|---|---|---|---|---|
| bsD_brauer_cores | order-m Brauer classes (−u₁/u₃, −u₂/u₃)_ζ on the ES surface over ℚ(μ_m) | PROVED obstruction (corestriction collapse on ℚ-points) | 1 | none | Thm 1 PROVED rel. BL Thm 1.6; cubic symbols non-constant on solutions EVIDENCE |
| bsD_frobenius_closure | Chebotarev closure of a slice; cubic reciprocity dictionary | PROVED obstruction (closure has index ≤ 2) | 1 | none | Thm 2 PROVED; no Kummer cubic/quartic signal EVIDENCE |
| bsD_missed_primes | the 71 primes missed by quadratic slices; cubic/quartic layers | EVIDENCE, negative | 0–1 | H-A | misses are locally square; quartic layer misses 2, sextic 12, exponent-12 none |
| bsD_eichler_degree_k | degree-k cyclic algebra "Diff-sum"; Eichler condition | PROVED structural negative | 1 (2 as FF spark) | none | ray condition = degree-k Diff-sums (tautology); forcing geometry only in degree 2 (Br ℝ = ℤ/2) |
| bsD_metaplectic_cubic | Weil index μ₈; Kubota–Patterson cubic theta | negative | 0–1 | none | Weil-index parity is still quadratic in ℓ; cubic theta sees f only via Dirichlet data |
| bsD_genus_vacuity_LDp | (LD_p) as reduction theory on Gross lattices | PROVED reduction (genus vacuous) | 1 | H-A | fixed order = lottery (Assessment; corrected DSP misuse) |
| bsD_artin_conjugation | −1 = complex conjugation in ℚ(ζ_M); F-rational loophole over ℚ(ζ_M)⁺ | dictionary; loophole closed in LDP_DEEP §A.4 | 1 | H-A | ray condition quadratic over F for F-norm divisors; O_F-certificates do not descend |
| bsD_drinfeld_rank_k | definite degree-k algebras over F_q(T), rank-k Drinfeld modules | spark (Assessment) | 1 | none | unique setting with order-k definite forcing; ES_q certificates quadratic |

## Spark relay H (O181, untriaged): degree-k Diff-parity over F_q(T), odd-degree descent; deep file DRINFELD_ES.md

Self-assessed (not yet triaged). Memo prefix `bsH_`; scripts `scripts/bsH_*`.

| file | angle | memo verdict | promise | hatch | by-products (labels) |
|---|---|---|---|---|---|
| bsH_kth_power_law | k-th power law of ES_q Type II moduli; Kummer CM data f^{1/k} at P | PROVED negative (always split at P, odd k) | 1 | none | k-th powers enriched ×≈k (EVIDENCE) |
| bsH_bl_order_q1 | BL classes of order q − 1 on the ES_q surface over F_q(T) | PROVED: odd part vanishes on monic integral points | 1 | none | Steinberg decomposition; inv_P = Kudla symbol |
| bsH_twisted_targets | A/P = c₁/X + c₂/Y + c₃/Z: order-m reciprocity restored | PROVED: order-m T1 on degree classes only | 1–2 | none | ∞-invariant = degree character (EVIDENCE 4 074 pts) |
| bsH_infinity_coordinate | F_∞^*/U₁ = sign × degree; what T1 needs | dictionary (Assessment) | 2 as explanation | none | — |
| bsH_odd_descent | odd-degree subfields of ℚ(ζ_M)⁺; N(−1) = −1 | PROVED closed (Props 4.1, 4.2) | 0 | none | — |
| bsH_carlitz_real | Carlitz real subfields of odd degree | dictionary; closed | 0–1 | none | — |
| bsH_rank_k_genus | rank-k supersingular class sets as forcing | COLLAPSES (B2, genus-vacuous) | 0–1 | none | — |
| bsH_lsv_ramanujan | LSV Ramanujan complexes | COLLAPSES (B3, B2) | 0 | none | — |
| bsH_lubin_tate_sterile | x*_c = rec_T((1+cT)^{−1}), wild inertia at T | dictionary ("T1 point with T1 removed") | 1 | none | — |
| bsH_shtuka_theta | Yun–Zhang / Feng–Yun–Zhang higher theta series | COLLAPSES as route (parity quadratic) | 0–1 | none | — |
| bsH_nagao_cf | Case B families as SL₂(F_q[T]) / unique CFs | dictionary | 0–1 | H-A | — |

## Cross-cutting notes
* **Brief-template error (B2 wording).** The briefs' barrier text said "a lottery with only polylog(p) expected
  winners (Σ_{p≤N} f(p) ≍ N log³N)". Over **primes**, Elsholtz–Tao give N log²N ≪ Σ_{p≤N} f(p) ≪ N log²N log log N
  (the campaign's (D)32b removes the log log for Type I). So the *average* of f(p) over p ≤ N is ≍ log³p, while
  N log³N is the sum over all integers n ≤ N. Harmless for the qualitative barrier.
  * Quotes the wrong form: `tech_maynard_theta.md` §2 (line 50: "Σ_{p≤N} f_II(p) ≍ N log³ N"; erratum appended).
  * Ambiguous: `nonab_homogeneous_dynamics.md` line 46 ("Σ f_II ≍ N log³N", range unstated; correct only as a sum
    over integers n ≤ N; noted in its erratum).
  * Correct forms: `adv_stacked_primes.md` l.28, `prob_lottery_model.md` l.24, `anal_dirichlet_series.md` l.25,
    `addcomb_unit_fraction_density.md` §3.3 (average log³p), `cayley_markoff_cm.md` l.98 (sum over n).
* **Convergent sub-question (H-A).** polynomial_method, wildcard_list W4/W15, markoff_hasse and technique_transfer
  item 13 converge on: do absolute A, C exist such that every large prime p ≡ 1 (24) has e ≤ C(log p)^A with
  −1 ∈ Σ_e((p+e)/4)? B4 does not exclude a target-specific argument using residues of the large prime factors.
  No such argument is proposed anywhere. Status: open (no label beyond CONJECTURE-level question).
* **Top depth candidates** (all promise 2): invol_windmill_signature (H-E), ident_form_families + canonical_invariants
  (H-E), gon_fermat_certificates (H-A), corr_parity_layers (H-B), the small-e cluster above (H-A),
  nonab_frobenius_redei (H-D), padic_functionfield_igusa (FF test bed), adv_stacked_primes (H-A).

## Script fixes (O160, from a deep-review note)
* `scripts/bs_adv_count.c` (O154): part B (e > E) solutions did not update the `emin` / `X_e (e ≤ 31)` metadata, so
  `emin` was reported 0 when every slice e ≤ E was empty, and X_e for E < e ≤ 31 was reported 0 when E < 31
  (e.g. p = 433, E = 3: old output "emin 0", X_e all 0; fixed output "emin 7", X = 0 6 0 4 2 2 0 2, matching E = 1000).
  The f_II totals were always correct. No O154 log is affected: all 351 records used the default E ≈ 2√p ≫ 64 and
  have part A > 0. Option `A` (skip part B) is now documented as giving slice-limited metadata.
* `scripts/bs_adv_drivers.py` (O154): the feature labelled "log τ(p−1), 100-smooth part" computed log of the smooth
  part itself. Renamed, a correct log τ version added, re-run (≈ 2 min); no conclusion changes. See the
  `adv_new_drivers.md` erratum.
* `scripts/errata_check.py` (new): verifies every computational counterexample quoted in the errata sections
  (17 checks, < 1 min).

## Spark brainstorm B (O175): the sign layer, ray classes, SQ, function-field sterile point (`bsB_*`, not yet triaged)

Deep-dive file: `SIGNLAYER_DEEP.md`. Report: `reviews/agent-reports/AGENT_REPORT_O175.md`. Promise = memo's own score.

| file | angle | verdict (own) | labels | promise |
|---|---|---|---|---|
| bsB_zolotarev_transpose | ES sign = sign of the ℤ/n-half of the transpose of the m × m'' rectangle (Zolotarev) | dictionary; class-+1 elements generate only even permutations → B2 | PROVED (elementary, classical in spirit) | 0 |
| bsB_theta_multiplier | ES sign = weight-½ theta multiplier of the certificate matrix; Waldspurger/Shimura screen | multiplier dictionary; Shimura zero-propagation **refuted** (W(105k²) > 0) | PROVED; EVIDENCE (W zeros ≤ 2·10⁶: squares + 26 composites, no prime) | 1 |
| bsB_rayclass_norm_pullback | which characters of Cl_(t)(ℚ(√−tp)) the condition uses | only χ∘N (Eisenstein; L = L(χ)L(χχ_K)); ES sign = genus χ_p on G[1+σ] | PROVED (elementary/standard CFT) | 0 |
| bsB_redei_oddpart | 2-power CFT (Rédei, governing fields, spins) vs the class condition | for prime t the 2-primary part IS the genus sign; fully 2-visible slices: t = 3·(Fermat products), finite | PROVED (items 1–3); Assessment (cubic spins) | 0–1 |
| bsB_salie_duality | Type II with p as Kloosterman modulus; Salié exact evaluation | certificate set not Γ_∞-bi-invariant (moving modulus) → B2/B6 | PROVED dictionary; Assessment | 1 |
| bsB_sterile_pretentious | FF sterile point as "Siegel zero" | inverted: sterile = maximally pretentious (anti-Siegel); Mordell transfer in F_q[T] gives only a degree-parity constraint | PROVED (items 1, 3); EVIDENCE corr = −0.49 | 1 |
| bsB_orthant_sign | sign layer = real orthant of one cubic | class +1 = negative orthant of cfg − c − f = n; orthant-crossing maps barred (T1 / group level) | PROVED | 1 |
| bsB_root_number_parity | BSD-parity template "sign forces a point" | rational points free, integral needs fixed module; parity of W(p) locally random | Assessment; EVIDENCE | 0 |

## Spark brainstorm A on the HJ/Farey reformulation (O174; memos bsA_*, deep file HJ_DEEP.md; not yet triaged)
| file | angle | verdict (own) | label of main items |
|---|---|---|---|
| bsA_farey_lnr_pigeonhole | Farey least non-residue λ(p): unconditional bounds | no ES content (B3 gap from ≍ ln²p to 3) | Lemmas 1–2, Thm 3 PROVED (λ ≤ (6/π²+o(1))ln²p, rel. Yao–Knuth) |
| bsA_selling_sandpile | words = Selling-reduced ternary lattices = 4-vertex multigraphs; genus G⁻(p) | dictionary; class layer = B2 | D1–D3 PROVED; links to Lorenzini's critical polynomial |
| bsA_lens_homotopy_surgery | lens spaces: homotopy type, Greene surgery, 2-bridge knots, Matveev | complement of classified (QR) world; no existence | P1–P2 PROVED rel. classical; T1 = "coarser than homotopy" |
| bsA_farey_graph_metric | true Farey-graph (signed CF) metric | sign freedom adds nothing | λ_F = λ EVIDENCE p < 6000 |
| bsA_fricke_vieta | Markoff/Vieta/BGS: word as point of the 4-holed-sphere Fricke cubic | Vieta acts on the fibre, ES lives on the base | F1–F3 PROVED |
| bsA_hecke_cusp_excursions | QNR = split-torus orbit of Hecke points; 3-excursion large deviation | dynamics blind at measure p^{−1} | H1, H3 dictionary; H2 expected |
| bsA_wu_rokhlin_sign | ES sign = Wu-square of the plumbing (Rokhlin mod 8) | clean sign formula; sign layer only | Thm W PROVED r ≤ 5 (EVIDENCE general lattices) — SHARP |
| bsA_toric_ksb_wahl | cyclic quotient singularities, KSB T-singularities | certificates never ℚ-Gorenstein smoothable | K2 PROVED rel. KSB |
| bsA_minkowski_stern | HJ length = popcount of Minkowski ?; ES via Stern's diatomic sequence | dictionary; divisor event | M1–M3 PROVED — SHARP |
| HJ_DEEP.md (deep) | master identity t/n = 1/(uv)+1/(un)+1/(vn); Type II = words of cp; SQ₅ = (W) ∧ (S) | no route; (W) = Lorenzini's open A₃ question | (W), (S) EVIDENCE to 10⁸ |

## Spark relay G on Lorenzini's A₃ question (O180; memos bsG_*, deep file LORENZINI_W.md; not yet triaged)
| file | angle | verdict (own) | label of main items |
|---|---|---|---|
| bsG_even_half | Lorenzini's 2^m − 2 (m odd) via a covering of the exponent mod 36 | **all even n ≥ 16 except 510 are values** | Thm 9.1 PROVED — SHARP |
| bsG_primes_trivial | (W) where ES needs it (primes p ≡ 1 (4)) | trivial by (2,2,·), (3,·,4); interior SQ₅(p) ⟺ (S)(p) | PROVED — SHARP (deflationary) |
| bsG_square_shadow | genus character at n = m² on the middle letter | T1 acts partially on (W); squares still all values except 1, 9 | Lemma 3.1, Prop 3.3 PROVED — SHARP |
| bsG_sterile_set | profinite set missed by all fixed-pair families | infinite, accumulates at −1 → compactness route closed | Prop 4.1, Thm 4.2 PROVED; EVIDENCE |
| bsG_short_block | least outer letter x*(n) (consecutive n + x) | x* ≤ 12 below 10⁸; CONJ x* ≪ log n/log log n | EVIDENCE; CONJECTURE |
| bsG_large_sieve_rate | large sieve with growing dimension | #exceptions ≪ N exp(−c√log N) | PROVED rel. Titchmarsh divisor thm |
| bsG_sister_Ak_stern | Stern popcount slices = V_{A_k}(2); Lorenzini's A₄–A₆ lists | dictionary; lists reproduced | Prop 7.1 PROVED; EVIDENCE to 10⁷–10⁸ |
| bsG_ternary_weinberger | Borwein–Choi/Weinberger analogue | no fixed class group → no exponent law | Assessment (negative) |
| bsG_lens_dinv | lens spaces / d-invariants / Dedekind sums | Floer invariants see Σ letters, not length | identity checked; Assessment |
| bsG_modular_hyperbola | (W) on aā ≡ 1 (n), Kloosterman | B3 gap n^{1/2} | Assessment |
| LORENZINI_W.md (deep) | forms F1–F4, shadow, sterile set, short blocks, rate, Stern, primes | (W) open; ES content of SQ₅ at primes is (S) alone | see file |

## Spark relay E (O178): depth aspect / prime-power moduli (memos bsE_*, deep file DEPTH_ASPECT.md; not yet triaged)

| file | angle | own verdict | hatch / status |
|---|---|---|---|
| bsE_qpower_moduli_Z | ET moduli restricted to q^s over ℤ | COLLAPSES (B2); 1233 explicit failures ≤ 10⁶ at q = 3 | none |
| bsE_sierpinski_moving_integer | q^s p + 1 as a Sierpiński family | COLLAPSES (B1) | none |
| bsE_padic_interpolation | Skolem–Mahler–Lech / exponential-polynomial witnesses | COLLAPSES (B1; Lemma 1.3 PROVED) | none |
| bsE_depth_characters | Postnikov / Kloosterman mod T^r | PARTIAL: wrong tool; elementary casework wins | — |
| bsE_et_casework_depth | ET casework at depth T^s: 2/5 beats O173's 1/2 | LIVE (FF, PROVED) | FF sterile points |
| bsE_large_q_char3 | no finite linear covering of ES_q(T^k), q = 3^r ≥ 3^27 | PROVED (FF), under review | — |
| bsE_large_r_sterile | sterile Mordell points for every large r | SHARP candidate, PROVED rel. cited, needs review | B1-side |
| bsE_caseAB_shift | #Case A(α) = #Case B(α+1) | CONJECTURE (EVIDENCE) | — |
| bsE_q3_explicit_constants | what is missing at q = 3, r = 13/17 | OPEN programme | — |

## Spark relay M (O188): steering by sterile Mordell points (memos bsM_*, deep file STERILE_STEER.md; not yet triaged)

| file | angle | own verdict | labels |
|---|---|---|---|
| bsM_boundary_escape | which classes certify primes near a sterile point | escape at the first primes beyond the trivial range; sterile ≡ square point | Lemma PROVED; EVIDENCE |
| bsM_borel_cantelli_patterns | S closed, ES ⟺ ℙ ∩ S = ∅; non-square patterns | divergent patterns ν-a.e. covered, sparse ones carry sterile points; integers are on the divergent side | Props PROVED; sparse side Assessment — SHARP (language) |
| bsM_shot_coverage | per-prime coverage, ℤ vs V_φ | sterile points = signature of finitely many shots | PROVED rel. ET; Assessment |

## Spark relay Y3 (O211): bridging the (h+1)- and (h−1)-worlds (memos y3_*, deep file BRIDGE_WORLDS.md; not yet triaged)

| file | angle | own verdict | labels |
|---|---|---|---|
| y3_semiprimitive_collapse | pure Gauss sums / uniform cyclotomy over F_{h²} at m = 4cd \| h+1 | COLLAPSES to the box: scaling collapse (p-blind), Stickelberger sign = (−1)^j, ∏(1−ζ) = c | PROVED; EVIDENCE (m²(a,b) ≡ 1, 1−m, 1−3m) |
| y3_salie_angle | Salié sum at modulus h: root angle of ν² ≡ −pd at 1/(2j) + 1/(2jh) | COLLAPSES to H-A (Planck-scale hit) | PROVED dictionary |
| y3_typeI_hasse_window | O207 spark 1: Type I dual Hasse window, CM, Type I overlap gcd(p+1, f−1) | COLLAPSES: window = g ∈ {1,3,5} (g = 3, f prime, for p ≡ 1 mod 4: greedy sub-family, B1); CM suggestion fails (no instance in 10 737) | PROVED; EVIDENCE |
| y3_euclid_schur_forcing | ES class −1 is one of the Schur–Murty Euclidean classes (a² ≡ 1) | COLLAPSES: single-integer forcing only for \|G\| = 2 (trivial slice); auxiliary-prime forcing = B1 | PROVED (E1); E3 withdrawn → remark |
| y3_lucas_dickson_trace | Lucas ranks, Dickson, trace, Cayley; Galois-descent classification | COLLAPSES (Prop G: algebraic bridges carry rationals = box) | PROVED |
| y3_frob_infinity | h ≡ −1 ⟺ Frob_h = c_∞: "h imitates ∞"; 2-group slices = genus theory | language; COLLAPSES B2/B4 | PROVED dictionary; check 0/72 905 mismatches |
| y3_gross_koblitz_box | Gross–Koblitz at semi-primitive level; mixed torus Gauss sums | COLLAPSES: Γ_h argument 1/m ≡ j (box); mixed sum Weil-bounded (B3) | PROVED (classical); numerics |
| y3_primemod_census | O207 spark 2: prime-modulus Type II census, growth, sieve screen | CONJECTURE PM-II (3361 only exception); no handle | EVIDENCE |
| y3_ordinary_bridge | R206 D3: ordinary reductions as bridges | COLLAPSES: Hom ≤ gcd(a_h−2, h−1) ≤ 2√h+2 unless a_h = 2; m-part orthogonal; Mazur-bounded canonical maps; box is trace-0 | PROVED; EVIDENCE |
| BRIDGE_WORLDS.md (deep) | three tiers of bridges (homomorphic ±1 / fixed symmetric rational expressions = rationals / Frobenius-invariant = K⁺ → F_h); unit twists (trivial unless totally positive) | no route; scoped negative + PM-II | see file |

## Synthesis III (O208): cross-combinations of (J)13–(J)38 aimed at the exits (E1)/(E2) (`s3_*`, deep file SYNTHESIS_SPARKS3.md; not yet triaged)

| file | combination | own verdict | labels |
|---|---|---|---|
| s3_numerator_blind | (J)23/(J)28 relaxations × (J)31/(J)32 numerator failures | **barrier: M^□ is a theorem for every M ≡ 0 (4) at all non-squares (shot mechanism T1-exact), while M/p fails at 278 known pairs (8/131 = 1/20 + 1/131 + 9/2620)** — SHARP | Thm 1.1 PROVED (Dirichlet); EVIDENCE (fixed S) |
| s3_order3_numerator | (J)19/(J)28 × (J)31 × (J)32 | TES^{□₃} true at all 16 TES failures; an order-3 SQ₅ and a χ₃-fibre theorem cannot both hold | PROVED (combination, logic); EVIDENCE to N ≤ 27000 |
| s3_box_bit | (J)28 × (J)25 box × (J)38 slicing | □-shot at prime g ⟺ (p/g) = −1 = the sign layer of the certificate at g; slicing relabels the box | PROVED; EVIDENCE (0/85939 box hits when (p/g) = +1) |
| s3_eps_mu_sieve | (J)23 sieve × (J)38 ε_μ | same shot n + 4t², Q = t forced small on the ES side | PROVED (identity); collapses to (J)25 |
| s3_min_scale | (J)25 × (J)28 × (J)30 | both searches end at polylog scale; box size is not the obstacle | EVIDENCE to 10⁷ |
| s3_lll_lenstra | (J)25 × (J)38 × Lenstra/Coppersmith | ≤ 11 certificates per Lenstra line, decision not existence | PROVED rel. Lenstra; EVIDENCE |
| s3_words_parity | (J)33 × (J)15 × involution parity | σ forces nothing; no parity law | PROVED (σ); EVIDENCE (negative) |
| s3_isogeny_mixing | (J)35 × (J)16 × expander mixing | mixing cannot robustly force a certificate edge | Assessment (counts PROVED/EVIDENCE) |
| s3_vphi_ringmaps | (J)21 × (J)25 × (J)17 | ring maps, Galois averaging, norms out of ℤ[φ] give only local / B2 data | PROVED for these operations |

## Spark relay Y2 (O210): A₂ friezes of the five ES slices (memos y2_*, deep file FRIEZE_ES.md; not yet triaged)

| file | angle | own verdict | labels |
|---|---|---|---|
| y2_even_edge | mod-2 rigidity + 2-adic weight of the unique even edge ⇒ DK Thm 4.5 in 3 cases, all formal words, all odd N | **(h′/N) = (−1/N)(−1)^{[8∣ee′]}** | PROVED; CERTIFIED (5.1 M words N ≤ 10⁵ + 2 M random) — SHARP |
| y2_farey_complex_lifting | SVZ Farey complexes mod 4/8; lifting with coefficient N | F₄ blind (all odd closed walks strongly contractible); mod-8 lifting = SQ₅ lottery | PROVED / EVIDENCE (negative) |
| y2_hexagon_degeneration | hexagon (4 terms) proof and where it degenerates at the pentagon | hexagon via (2,2,2,k); pentagon needs a length-2 word at 4w = B2 | PROVED — SHARP (statement) |
| y2_twoadic_tree_transport | 2-adic tree / tropical frieze | cherry depths; **(h′/N) = −(2/o) for N ≡ 1 (8)** | PROVED; CERTIFIED |
| y2_parity_involution | windmill/parity on frieze set | surface is multilinear, so only the reflection; #F₋(p) even | PROVED (negative) |
| y2_zamolodchikov_forcing | twisted period-5 dynamics | mod 2 forced, mod 4 never (T1) | PROVED (negative) |
| y2_coefficients_model | CHJ subpolygons / snake graphs | model exists, it is a relabelling | dictionary |
| y2_positivity_is_T1 | signed friezes / Farey distance | T1 = archimedean factor = positivity; signed friezes have no T1 | PROVED by inspection + EVIDENCE — steering |

## Spark relay Y5 (O213): the transport law (memos y5_*, deep file TRANSPORT_LAW.md; not yet triaged)

| file | angle | own verdict | labels |
|---|---|---|---|
| y5_transport_is_ptolemy | what (h′/N) = −(2/o) really is | Ptolemy relation through the even edge mod 8: ee′ ∈ {1+o, N+o, 1+No}; "(2/o)" = o mod 8 = slice condition | PROVED (negative reading); CERTIFIED 784 732 words |
| y5_five_positions | free o in each of the 5 positions (spark 2) | o-progression family exists (P_h: N ≡ −c mod o, c ∣ o+1) but density τ(o+1)/o, not 1/2; P_c = Type II, P_m = Type I | PROVED dictionary; negative |
| y5_ocensus_hard_primes | least certificate vertex o*(p), p ≡ 1 (8) ≤ 10⁷ | o* = 7 for 94 %; max 2431 at p = 21841 (unique interior certificate pair); hard primes ≡ 1 (120) | EVIDENCE |
| y5_mod16_shadow | second-order T1 shadow mod 16/32 (spark 4) | none; T1 is one bit | EVIDENCE (negative) |
| y5_general_r_jacobi | general-r frieze Jacobi law (spark 1) | (K_{r−1}/N) = ∏(K_i, −K_{i+1})₂ · ∏(K_i, −K_{i+1})_∞; ∞-factor = Maslov count of continuant signs; r-uniqueness (= R208) | PROVED; CERTIFIED |
| y5_narrow_wide | positivity as complex conjugation | ES slice condition = kernel of narrow → wide ray class mod e (−1 = c_∞); signed factorisations land in +1 | PROVED dictionary (relabelling) |
| y5_siegel_weil_chamber | Siegel–Weil with the sign at ∞ (spark 5) | full-rank SW = genus indicator; sign is the 2-adic genus label; path bases are p^{−2/3}-thin | PROVED (triviality) + Assessment (negative) |
| y5_even_middle | Mordell position alone (m even, 8 ∣ m·e) | SQ_H holds at all primes ≡ 1 (8) ≤ 10⁷; 22 composite exceptions ≤ 10⁶ | CONJECTURE / EVIDENCE |

## Spark relay Y4 (O212): hunting 4-specific inputs after the numerator-blindness barrier (`y4_*`, deep file FOUR_SPECIFIC.md; not yet triaged)
| memo | idea | outcome | label |
|---|---|---|---|
| y4_t1_numerators | which M carry T1 / blind relaxations | T1 in the M-shot family ⟺ M ≡ 0, 3 (mod 4) (−M a discriminant); M^□ a theorem for all M; failure-free T1 numerators: 3, 4, 7; new harness entry 11/37 | PROVED; CERTIFIED checks |
| y4_oneodd_slices | one-odd half on the five slices | parity = v₂ of the slot (2 ↔ one-odd, ≥ 3 ↔ 8/n); cells 100/100/40; S₄^{odd}(p) ≠ ∅ to 10⁷ but empty at composites 321, …; certificates of fixed n are ℤ₂-isometric (FOUR_SPECIFIC Thm 2.3) | PROVED; EVIDENCE |
| y4_harness_hatches | O208 harness on H-A/B/D/E/F, Rem 10.4, SQ₅ | all hatches are uniform skeletons + lottery; only SQ₅/χ-fibre passes as a stated 4-specific input | Assessment |
| y4_mordell_witness | universal one-slot χ-witnesses | exactly A ∈ {2, 3, 5, 7, 8, 15, 20}; their reach is exactly Mordell's 840 | PROVED (Dirichlet + finite check + RS bound); checked to 10⁶ |
| y4_catalogue | 4-vs-8 structural catalogue | 4 is the unique M ≥ 3 with an e ∈ {1, 3} slice at every prime; most facts are descriptions | PROVED; Assessment |
| y4_seven_control | 7/n as T1-bearing failure-free control | 7 has none of 4's slice/character structure yet no failure ≤ 10⁸ | EVIDENCE + Assessment |

## Spark relay Y1 on O205's two bad fibres / hyperbolic words (O209; memos y1_*, deep file TWO_FIBRES.md; not yet triaged)
| file | angle | verdict (own) | label of main items |
|---|---|---|---|
| y1_hurwitz_lift | χ = +1 fibre = Hurwitz order: n·G_w ↪ ℤ³ ⟺ Diff = {2}; square-det path lattices ⊂ ℤ³; 𝔊⁺_p = image of conic/S₄ (non-injective at p = 71, 79, …) | exact dictionary; ES-five = non-embeddability; B2 | H1–H4 PROVED (classical inputs); CERTIFIED n ≤ 3001 / 451 — SHARP |
| y1_gamma8_trace | words as hyperbolic classes; twisted trace formulas | χ is a function of M mod 8, not an SL₂(ℤ)-class function; ES = three-letter extraction (B3) | G1–G3 PROVED |
| y1_gl3_cuspidal | GL(m) cuspidal + GL(k) Eisenstein identities vs T1 | dead (twisted d_k + unitary GL(m) cusp coefficients, all finite families, incl. self-dual orthogonal), **by size at primes, T1 not used** (R214) | Prop G″ PROVED rel. PNT for GL(m) cusp forms; T1 Remark G conditional (fails for Ad(tetrahedral)) — SHARP (steering) |
| y1_cerednik_swap | Cerednik–Drinfeld / Ribet: two fibres = two trees of X^{2p} | dictionary; forcing hope screened (B2/B6); fibre split not mass-equidistributed | Assessment; EVIDENCE (census ratios) |
| y1_heegner_level_t | words = x = 4 GKZ terms of two root-2 Heegner points on X₀(t), index 4n | level-t condition = Heegner condition; B2 | K1 PROVED (congruence/index only; Heegner reading Assessment, imprimitive caveat); collisions trivial without level (t ≤ 11, p < 2·10⁵) |
| y1_reciprocal_parity | word reversal (involution) → parity | only fixed word (p ≥ 5) = (p+2,1,1), parabolic; N₋ mod 8 equidistributed | R1, R3 PROVED; R2 EVIDENCE (10⁶) |

## Spark relay Y7 (O215): the sibling numerator 7 (memos y7_*, deep file SEVEN_SIBLING.md; not yet triaged)
| memo | idea | outcome | label |
|---|---|---|---|
| y7_mordell_levels | shape of the identity-hard core per numerator | 4: square coset; **7: only the residue 1 survives at levels 14, 42, 70, 210: 7/p for all odd p ≢ 1 (mod 105)**; 8, 11, 12 have extra classes | PROVED + CERTIFIED — SHARP (dictionary) |
| y7_full_t1 | is 7's T1 full? | no: Type I/II solutions at 41–42 of 42 odd squares; full T1 for all 4 ∣ M (PROVED), fails for 5, 6, 7, 11 | PROVED + CERTIFIED |
| y7_free_inert | free slices (e = 1, 2) vs inert primes | exact iff M ∈ {4, 6, 7} (ℚ(i), ℚ(√−3), ℚ(√−7)) | PROVED (description) |
| y7_lattice_invariants | 7-adic analogue of (J)33 | S_M is not a function of the ℤ-isometry class of Q_w for M = 5, 7, 8, 11 (marking data) | PROVED by example (negative) |
| y7_near_misses | is 7 lottery-lucky? | f₇ = 1 at 43, 127, 211; consistent with a crude lottery model (≈ 0.28) | EVIDENCE + Assessment |
| y7_order3 | e = 3 / e = 6 double failures vs cubic residues | no detected association with cube indicators; 7 can doubly fail only at p ≡ 1 (21), 27.8 % do | EVIDENCE (negative) |
| y7_split_norm | residue class of π mod q in ℚ(√−7) | no detected association beyond p mod q (q = 5, 9) | EVIDENCE (negative) |

## Synthesis IV (O218): "ES must imitate the archimedean place" — cross-combinations of (J)39–(J)50 with (J)13–(J)38 (`s4_*`, deep file SYNTHESIS_SPARKS4.md; not yet triaged)

| file | combination / tool | own verdict | labels |
|---|---|---|---|
| s4_three_bits_meta | meta-statement: positive ⟺ definite (L1); D one real component (L2); three-bit law for all words; signed relaxations R₂ (no T1) and R_n (T1, finite, no forcing) | positivity = T1 anchor, not bottleneck; **CONJECTURE SQ_±** | L1, L2, P3(a,b) PROVED; three-bit law CERTIFIED (n ≤ 1001); SQ_± EVIDENCE to 10⁷; P3(d) CONDITIONAL (H) |
| s4_selling_voronoi_wall | Selling/Voronoi reduction on the χ = −1 genus | certificates = obtuse superbases with a (1,1,0) face (Voronoi wall); locates, no forcing (B2) | Lemma S PROVED; invariance CERTIFIED (3000) |
| s4_kudla_green_infinity | (J)13 × L1 | signed words = archimedean (Green) coefficients; at squares certificates have Diff = {∞} | PROVED given the three-bit law |
| s4_minkowski_sail | Minkowski/Thue/Siegel vs Klein sail | symmetric GoN sign-blind (50.0 % quadrant); one-quadrant GoN = HJ words; no volume theorem | Lemma M PROVED; EVIDENCE |
| s4_real_analytic_tools | θ > 0 on iℝ, IVT/degree, SOS, Hodge index/Hasse | all act on real/genus layer identical at squares | COLLAPSES (Assessment) |
| s4_two_and_infinity | (J)49 × (J)32 × (J)48 | numerator lives at 2, positivity at ∞; their coupling = Hamilton B_{2,∞} = TWO_FIBRES Thm A | elementary PROVED parts; reformulation |
| s4_mute_infinity | c_∞-imitation × mute place × relaxations | steering table: PROVED variants = fixed c_∞-modulus + infinite shots | Assessment |
| s4_maslov_inertia | (J)45 Maslov × HJ length 3 | Maslov count = ind_−/2; at length 3 all-or-nothing | PROVED; CERTIFIED (75 097 words) |
| SYNTHESIS_SPARKS4.md (deep) | R_n / SQ_±: finiteness, no forcing, unit-slot genus table, no finite t-set (H), numerics; Selling wall | no route; steering rule "test on SQ_± first" | see file |

## Spark relay Y8 (O217): the three-squares side and adelic "continuity of T1" (memos y8_*, deep file THREE_SQUARES.md; not yet triaged)

| file | angle | outcome | labels |
|---|---|---|---|
| y8_adelic_continuity | sign balance vs distance to squares | archimedean distance irrelevant at the √p scale (R224: NOT at bounded p − m²: T1-type levels tm² + c², THREE_SQUARES Lemma 1.4); clean levels (all primes of tp+1 QR mod p); T1 = all levels clean; calibrated reciprocity-constrained coin model fits clean-level rates | PROVED (L1–L4) + EVIDENCE — SHARP |
| y8_siegel_weil_sign | exact Siegel–Weil weighting of words | α₂ and α_p vanish together on χ=−1, so no weighting beyond the indicator (checkpoint formula withdrawn, R-O217); comparison with \|X_p\| circular | PROVED; negative |
| y8_lnr_level | least-non-residue level t₀ = −p⁻¹ mod q | Mordell (840) = "lnr ≤ 7 ⇒ lnr level admissible with A = q"; q ≥ 11: ≈ 0.85 success per translate, stable in p | PROVED + EVIDENCE |
| y8_three_squares_sq | SQ for composite n via ℤ³-embeddability | 3SQ: all words embed ⟺ n square; no exceptions to 10⁶ (105 is not one) | CONJECTURE/EVIDENCE — SHARP (formulation) |
| y8_conic_height | conic points carrying words | height(ℓ(w)) ≤ min letter; boundary words = principal-genus ideals dividing (1+√−p) | PROVED + EVIDENCE |
| y8_square_test_gap | n square ⟺ every level clean; ES-five = admissible version | the ES content is exactly the admissibility gap (A ≡ −1 mod t) | PROVED; steering |

## Spark relay Y10 (O221): T1 deformed to polynomially-near squares p = m² + k (memos y10_*, deep file NEAR_SQUARE.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| y10_poly_families_above | ET §10 in the variable m for p = m² + k, k > 0 | new (Aurifeuillean) families exist but every family's witness is a fixed character of n: polynomial families do no better than congruences at locally-square m (Thm 2.2, positivity of x² + ky²) | PROVED |
| y10_hecke_witness | witness (D(m)/p) = (D(−√−k)/(m + √−k))_K | escape ⟺ D(−√−k) ∉ ℚ; never happens for k > 0 | PROVED dictionary |
| y10_below_squares | p = m² − j | escaping families exist (e.g. j = 8, m ≡ 53 mod 56, reaching n ≡ 1 mod every L) | PROVED existence |
| y10_t1_points_positivity | positivity propagates to the largest real root of n | integer T1 points above the root obstruct every polynomial family (Thm 3.3); m₀ vs −m₀ differ | PROVED |
| y10_kadic_sterile | sterile set of polynomial families on m² − j | ⊇ closure of Z_K⁺ = {m − √j a local unit square in ℚ(√j)} (Thm 3.4); = at j = 8, L = 8064/4480 | PROVED ⊇; CONJECTURE Y10-S — SHARP |
| y10_clean_level_classification | levels clean along a whole quadratic family | ⟺ 4A − tΔ = □ (outside gcd-exceptional classes); per prime: T1-type = principal-form part of clean (82 % of clean words) | PROVED + EVIDENCE |
| y10_hardness_beyond_clean | does near-squareness predict N₋/N beyond adelic cells? | yes, monotone in p − ⌊√p⌋²; half survives removing all clean levels (mechanism open) | EVIDENCE |
| y10_hard_primes_m2minus3 | hard primes vs polynomial T1 points | 3361 and 1 249 921 are m² − 3 next to m₀ = 2 | EVIDENCE (anecdotal) |

## Wave Z-a (O224): a 4-specific input from the 2-adic χ-fibre (memos z1_*, deep file FOUR_ADIC_INPUT.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| z1_fano_pigeonhole | why S_4 = {χ = −1}: Q mod 4 on L/2L, frieze parity puts 2 pentagon points on the 3-point even line W, isotropy puts 2 zeros there | third proof (after cells and FRIEZE_ES Thm 1.2) of MODEL_SPECIFIC Thm 3.1(a), new lattice mechanism; certificate = path edge + pointer to an endpoint of the 2-isogeny edge (R229 repair) | PROVED (known statement) |
| z1_depth_bits | 2-adic density 4 vs 8 (brief angle 1) | one fair bit per extra power of 2 per isotropic pentagon vector: 7/12, 5/16, 31/192 exactly (PROVED at cell level); on actual words bits are strongly correlated (12 vs 0.82 predicted S₈-empty primes < 4000) | CERTIFIED + EVIDENCE |
| z1_marking_isometry | is S_M a lattice (isometry-class) property? | not for any M with φ(M) > 2 (norm-one triples, PROVED); S₂, S₃ trivial; S₄ genus; S₆ class but not genus (EVIDENCE); interior markings unique (EVIDENCE) | PROVED + EVIDENCE |
| z1_small_prime_pigeonhole | forced slices at ℓ-adic level | S_M genus-determined (for all n coprime to M) iff M ∈ {2, 3, 4}; not 7 (R229 repair) | PROVED |
| z1_legendre_levels | tp = 4^a(8b+7) ⇒ every level-t word certifies (ℤ³ + Legendre) | character-free sub-lottery; fails at 73, 1201, 1489, 9649, 21169, 23041, 44641 (p ≡ 1 mod 4 < 10⁶); T1 in Legendre form | PROVED + EVIDENCE |
| z1_glue_square_roots | Siegel–Weil on lattices ⊃ M_{v,t} in 𝔊⁻_p | gluing classes = square roots of −p/v mod A*; the fixed basis extends to a path basis ⟺ c ≡ ±1: genus shadow vs residue (B2) | PROVED (marked); negative |
| z1_isogeny_pointer | 2-isogeny walks crossing into χ = −1 (brief angle 2) | no crossing (lattice/Hecke walks preserve χ); pointer automatic; expansion cannot prove the thin path-edge set non-empty | PROVED + EVIDENCE; negative |
| z1_square_numerator | "4 = 2² is a square" (brief angle 3) | refuted by 9/p, 16/p; residue = v₂(M) = 2 (Fano) | dead |
| FOUR_ADIC_INPUT.md (deep) | Fano theorem, 2^k bit law, requirements (i)–(iv), glued-plane form of path classes | 4-specific 2-adic input is used up by Thm 1.3; (i) = SQ₅ remains the lottery | see file |
## Synthesis V (O230): cross-combinations of wave Y ((J)39–(J)56) (`s5_*`, deep file SYNTHESIS_SPARKS5.md; not yet triaged)
| file | question | finding | label |
|---|---|---|---|
| s5_three_sides | (J)48 × (J)53/(J)55: the three side numbers tp+1 = AB, p+u = Av, p+v = Bu | Lemma S: χ = genus character on every side; u-side deformation u(K+u) = □; exact three-side cleanliness explains ≈ 70–80 % of the residual near-square depletion (K0 = 16, 24 fully); K0 = 8 = defective (gcd 3) deformation | Lemma S + deformations PROVED; census EVIDENCE (169 410 primes to 5·10⁶, 0 violations) |
| s5_reciprocity_forcing | (ii) Maslov/Dedekind index × SQ_±; (iii) anti-T1 auxiliary field | Prop R: every local-invariant index of a word is a function of (w mod 8, sgn w), so index sums are cell-occupation sums; reciprocity relocates signs, never creates points; anti-T1 = the five-slice cells = ES itself | PROVED (negative, exact scope) |
| s5_gcd_sides | own: interaction of side numbers | gcd(tp+1, p+u) = tu−1 = A; ES-five ⟺ some such gcd is ψ-odd (two-moving-modulus form of H-A) | PROVED (dictionary); checked p < 1500 |
| s5_unforced_words | own: forced (clean-side) vs unforced words | N₋ ≤ U (PROVED); hard primes = almost fully forced (13/13 hard primes < 10⁶, all dyadic record primes to 3·10⁷); CONJECTURE U (U = 0 only at 105 among n ≡ 1 (4) non-squares ≤ 2·10⁵); N₋ ≥ U/2 REFUTED at p = 5 270 849 | PROVED / EVIDENCE / REFUTED — SHARP (descriptive) |
| s5_cm_frobenius | (iv) Frob = c_∞ × (h±1)-worlds × supersingular | Prop C: certificate primes = primes splitting completely in the CM field F_M = ℚ(ζ_M)⁺(√(p(θ²−4))) with Frob = c_∞·σ_p; T1 = the twisted conjugation ceases to exist; Chebotarev + divisibility = B2 | PROVED dictionary; checked |
| s5_sterile_uniform | (v) FF (J)56 vs ℤ (J)54 sterility | one profinite formulation; unavoidable global input = size/degree coupling of certificate modulus (box), not sign (SQ_±), not congruences (sterility) | PROVED (formal) + Assessment |
| s5_scale_law | own: scale behaviour of the sign ratio | N₋/U stable ≈ 0.75 (0.770 at 1 mod 8, 0.739 at 5 mod 8) from 2¹⁰ to 2²⁴ while N₋/N drifts 0.59 → 0.67; drift = forced fraction ≈ 0.5/√log p | EVIDENCE (928 779 primes to 3·10⁷) |
## Wave Z-e (O229): bounded cap with a growing mute set, PM-II and SQ_± on average (memos z5_*, deep file CAP_GROWING.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| z5_cap_dimension | cap e of ES^{(y,e)} (free S) as a large-sieve dimension: Σω_e(ℓ)/ℓ ≍ (log X)^{e+1} | exceptional primes ≪ N exp(−c_e (log N)^{(e+2)/(e+3)}) via the overflow cube (shots alone: (e+1)/(e+2)); every e ≥ 1 beats Vaughan's 2/3 | PROVED rel. BV + large sieve |
| z5_pmII_vaughan | Vaughan's classes are prime-modulus Type II certificates | PM-II fails for ≪ N exp(−c log^{2/3} N) primes; covering moduli only h = 3, 7 (≤ 2·10⁴) | PROVED rel. Vaughan; CERTIFIED range |
| z5_pm_sqpm | prime-modulus words of SQ_±: χ = (n/ℓ), free genus filter, shift slots n + u | exponent 1/2 only (signed twin harder on average); CONJECTURE PM-SQ_±, 0 exceptions ≤ 10⁶, adversarial ok — SHARP | PROVED + CONJECTURE/EVIDENCE |
| z5_fixed_field_orbits | x-orbits with Δ_x = D₀m_k² in one real quadratic field | no free point (norms ±(16n)^i r²); ring class group ≍ m kills the CL luck | PROVED lemma + Assessment (negative) |
| z5_pell_unit_T1 | Pell unit of ℚ(√n) as a T1-shaped existence mechanism | never acts on ES^{[2]} fibres (needs n | λ, reciprocity-killed); sign-blind | PROVED (squarefree n), negative |

## Spark relay Z1 (O231): forced vs unforced words, CONJECTURE U (`z7_*`, deep file UNFORCED_WORDS.md; not yet triaged)
| memo | angle | result | label |
|---|---|---|---|
| z7_automatic_families | words with a fixed small parameter (min ≤ 2; s = 3, 4, 7) | Prop F/F′: on families with fixed side X ∈ {p+1, p+2, 2p+1, p+3, 3p+1, p+4, 4p+1, p+7, 7p+1}, certificate ⟺ unforced ⟺ X unclean; n ≡ 5 (8) trivial | PROVED; 0 mismatches to 3·10⁷ |
| z7_landau_depth | Landau depth K(p) of the fixed sides | K(p) < q(p); CONDITIONAL (Dickson): K(p) unbounded, so no bounded-min family proves U (U-analogue of B2); max K = 10 below 3·10⁷ | CONDITIONAL + EVIDENCE |
| z7_family_parity | goal 2: parity across words sharing a side | Flip Lemma (family has a certificate ⟺ (−1,−1) in the divisor image mod X); family-exact forcing collapses U to ES-five; flip = e-slice B2 | PROVED (negative, exact scope) |
| z7_double_unclean | U2 = words with A, B both unclean | N₋ ≤ U2 ≤ U; CONJECTURE U2 (only 105); N₋/U2 ≥ 0.62 to 3·10⁷ | PROVED sandwich + EVIDENCE |
| z7_haar_strata | goal 3: the "¾" of N₋/U | Haar five-slice mass = 3/4 exactly (pointwise); large-min words obey it, deficit lives in automatic families; Lemma 5.2; **SHARP: all N₋ < U/2 failures at n ≡ 1 (8) have ψ-odd part of n+1 = 3²** | PROVED + EVIDENCE |
| z7_symbol_blind | goal 1: what a U-proof must supply | ψ(tn+1) ≡ 1: the t-side is symbol-blind; non-certificate unforced words need tn+1 ∉ C_n (anti-Landau kernel); least-NR families fail i.o. | PROVED kernel + EVIDENCE |
| z7_signed_3sq | goal 4: split on SQ_± and 3SQ | SQ_± records fully forced (0.84–0.94 vs 0.24–0.51); 105 = Jacobi genus collapse, per-prime forcing (Lemma 6.1) explains 3SQ's exception-freeness | EVIDENCE + PROVED lemma |
## Spark relay Z2 (O232): sign fields — exponential near-squares, numerators, non-genus layer (memos z8_*, deep file SIGN_FIELDS.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| z8_exp_near_square_cover | exponent coverings of n = 4^s + k (m = 2^s) | ES certified for all 4^s + k, k ∈ {9, 57, 81, 129, 153, 177, 201, 225, 249}; open 33, 105, 273, 297 | PROVED (computer-assisted) + EVIDENCE |
| z8_mixed_points | CRT-glued integer square points in Ẑ as sterile candidates | explain the residual classes of 4^s + 105 (every member Mordell-hard); none sterile so far; uncovered measure → 8.5·10⁻⁸, greedy stalls | EVIDENCE |
| z8_numerator_sign_fields | ν-sign field ℚ(ζ_{νu}, √−u) | t-slot T1 ⟺ √−u ∈ ℚ(ζ_{νu}); for all u ⟺ 4 \| ν; ν = 4 unique with slot set = full forbidden half | PROVED — SHARP (dictionary) |
| z8_eight_failures_frobenius | 8/131, 8/241 as a missed ζ₈-bit | all 4-slots ≡ 4 mod 8 at these p | EVIDENCE |
| z8_no_redei_abelian_levels | Rédei layer for near-square depletion | single abelian level sees only residues of prime factors: no forced non-genus layer | PROVED (trivial) + Assessment |
| z8_chebotarev_family_level | level u(p) with F ⊄ Σ by construction | disjointness free; hitting a divisor of p + u is B2/B3 | Assessment (negative) |
## Wave Z4 (O234): the cap as a sieve knob, uniformly; pointwise e*(n); the exact family 𝒟_e(M) (memos z10_*, deep file CAP_INTERPOLATION.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z10_uniform_cap | Gallagher instead of weighted BV; e = e(N) | c_e ≍ 1/(e log e); saturation at e ≍ log log N with N exp(−c log N/(log₂N log₃N)); matching Rankin ceiling for classes truncated to V < ℓ/4 (R237 D1: untruncated family gives a power saving at e = ∞) | PROVED rel. Gallagher + BV + LS; ceiling elementary |
| z10_pointwise_cap | minimal cap e*(n) | covering barrier (log₂p)^{1−o(1)} i.o.; GRH: e*(p) ≤ (log p)^{2+ε}, ≤ exp(O(√(log₂p log₃p))) | PROVED / CONDITIONAL (GRH, sketch) |
| z10_exact_family | solution depends only on D = c²d | ES^{(y,e)} ⟺ D ∈ 𝒟_e(M) (D \| A² lifted by even excess ≤ 2e); supply dimension e + 3, no tower; e = 0 = ℛ(M) — SHARP | PROVED; (e+3)/(e+4) Assessment |
| z10_pmsq_1e7 | C rerun of PM-SQ_± | 0 exceptions ≤ 10⁷; record least \|u\| = 41 | EVIDENCE |

## Spark relay Z6 (O236): pointwise minimal cap e*(n) (memos z12_*, deep file CAP_POINTWISE.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z12_window_cap | Type II window q = 4x − n with mute set = primes of x | (x/q) = −1 forces −1 ∈ ⟨S⟩: ES^{(y,e)}(n) with e < q*(n); e*(n) ≪ rad(n)^5 (Linnik), explicit (Ahn–Kwon), ≪ log²n (GRH, non-square n); first polynomial cap — SHARP | PROVED |
| z12_typeI_dichotomy | same trick in Type I shape | (a/p) = +1: no forced firing; dead at every cap if (pk′+1)/4 prime | PROVED + EVIDENCE |
| z12_grh_lattice_gap | GRH + box covering toward C log log p | below covering threshold = divisor lottery; P-loss of whole-lattice covering pinned to equidistribution of relation primes mod P | Assessment (tentative) |

## Spark relay Z3 (O233): global Fano over the supersingular 2-isogeny graph (memos z9_*, deep file GLOBAL_FANO.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| z9_frobenius_layers | why path edges are 4× enriched in loops of G_p/Frob | loop ⟺ edge lattice represents 2 (⟺ E/C ≅ E^(p)); layers r_L(m) > 0 = compatible degree-m isogeny E^(p) → E; path edges sit in the layers of their letters | PROVED (known in substance: Chenu–Smith 2021, R234); CERTIFIED (9489 edges, p ≤ 2000; R234 recertified) |
| z9_pointer_parity | parity/degree/pointer laws for path edges over G_p | none: P(p) even 47.6 %, no forced odd vertex (609 primes ≤ 10⁴) | EVIDENCE; negative |
| z9_depth_walks | O224's depth bits on the tree | depth-k pentagon vector = conic-marked non-backtracking walk of k − 1 half-steps in G_p; 8/p = marked X₀(4) refinement; bits constrained (not determined) by v₂ of a letter or v₂(tp+1) | PROVED; CERTIFIED (1190 pointers) |
| z9_order3_fano | "Q mod 3 on L/√−3L" for TES | no order-3 Fano: χ₃ does not control v_λ(T); target words exist at all 13 TES failures ≤ 787 → TES failures are bit failures | EVIDENCE (one Type II slice); Assessment |
| z9_triangle_shapes | widen target to near-orthogonal (cyclic plumbing) classes | decoupled from path classes (47/329 primes: triangles but no path); no Egyptian identity | EVIDENCE; negative |
| z9_brandt_screen | how Brandt/class-number counts fail Prop 10.3 | L1 eigen-covariant functionals see only the mass of path classes; L2 planes up to genus (glue invisible); L3 Schiemann = problem itself | PROVED (L1 narrow); Assessment |
| z9_heegner_layers | layer t of G_p as reductions of CM points of disc −4tp on X₀(2) | necessary ray-class condition mod t (norm A ≡ −1, A ∣ tp+1) on those CM points, plus the level-t ring condition; unifies (J)35 with Prop 10.3 | Assessment (algebra PROVED) |
| GLOBAL_FANO.md (deep) | global pigeonhole over G_p | no global law; what a global Fano must act on (ray classes mod varying t); 105 has the graph but no path edge | PROVED parts + negative |

## Spark relay Z5 (O235): exponential near-squares — label points, ℓ-lines, c₀·4^s + k (memos z11_*, deep file EXP_NEAR_SQUARE.md; not yet triaged)

| file | idea | outcome | labels |
|---|---|---|---|
| z11_label_cantor | mixed points = label points Π_ℓ{square points}; CRT of squares | only mixed primes can cover; binary core of 4^s + 105 covered by 10 classes; quaternary core open | PROVED + CERTIFIED + EVIDENCE |
| z11_lines_branching | per-branch Ẑ tree (C) instead of global period | measure → 3·10⁻¹¹ but stuck nodes multiply; cause = ℓ-lines through square points (also k = 297, one square point); 3-line of 297 itself covered | EVIDENCE + diagnosis |
| z11_unit_square_shapes | when c₀·4^s + k has a unit-square point | iff c₀ + k = 4^j: (3, 1), c₀ ≡ 7 mod 8 series uncoverable; survey c₀ = 2, 3, 5 | PROVED + EVIDENCE |

## Synthesis VI (O238): cross-combinations of wave Z (memos s6_*, deep file SYNTHESIS_SPARKS6.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| s6_exp_classes_105 | windows 4^j − k on 4^s + k with algebraically forced budget (cyclotomic factors of 4^r + 1) | **ES for all 4^s + 105** (one exponential class + 13 ET classes, L = 360) — SHARP | PROVED (computer-assisted) |
| s6_mixed_points_cuberoots | uniform reading of sterility (FF root-product law, window reciprocity, mixed points) | sterility is relative to the class menu (by definition; R245 repair: no sterile point on Λ₁₀₅ known; R246 repair: ET-alone coverability of k = 105 remains OPEN; the exp class is also a local non-square class mod 18837001); 105's mixed point = cube-root family 256u³ + 105 | Assessment (instance PROVED) |
| s6_divisor_pigeonhole | P ∩ −P at a forced window | \|P\| > (q−1)/2 ⟹ cap 0; structure-free versions need Ω(K) ≳ q/4 (sharp) | PROVED + EVIDENCE |
| s6_unique_forced_cap0 | when does the forced bit give cap 0 for all K | only m = 3 (2-elementary unit group) | PROVED |
| s6_witness_onesided | is (q/p) = −1 necessary for cap 0 at q | no (non-square d); rates 34 % vs 18 % | PROVED obs. + EVIDENCE |
| s6_numerator_windows | self-generated mute set for ν/n | (R245 repair) K odd ⟹ even ν only; window-shape T1 at odd squares PROVED for 4 \| ν; false for ν = 3, 7, 9, 25 under the valid 2-adic forcing | PROVED (4 \| ν) + counterexamples |
| s6_ydual_windows | 𝒟_e(M) vs windows | y-window (fixed mute set) vs x-window (self-generated): the pointwise/almost-all boundary | PROVED dictionary |
| s6_window_independence | glue many forced windows | gcd(K_m, K_m′) \| (m − m′)/4: almost coprime mute sets (independence heuristic) | PROVED (trivial) + Assessment |
| s6_exp_classes_primes | algebraic budget-forcing for primes | needs a thin family; B1/B2 for primes | Assessment (negative) |

## Spark relay Z10 (O241): sterility as Diophantine approximation — games, Cantor sets, percolation (memos z16_*, deep file STERILE_DIOPHANTINE.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z16_game_barrier | Schmidt/absolute/potential games for U_c | U_c closed, misses a ball ⟹ never winning (listed games); shrink-constant diagnosis Assessment | PROVED negative |
| z16_windowed_konig | Cantor/König tree instead of games | windowed local mass condition suffices (+ dim bound); per-depth count bounds collapse to their tail union bound (sharper counts or positional input needed) | PROVED reduction + EVIDENCE |
| z16_sibling | no alive cylinder has 3 covered children | implies O(3, T²) ≠ ∅; holds to depth 9 (never 3, two 2s) | CONJECTURE |
| z16_liouville_spectrum | approximation profile η_u decides protected levels | H_τ ≥ N + 1 − η_u(N+1) unless exact; only rationals protected (from non-exact tuples) at all large levels; exact tuples common | PROVED |
| z16_frobenius | u ↦ u³ maps Case B coverings to coverings | covered ⟹ covered (levels N ↦ 3N + 2), leaves the c-slice | PROVED (Case A + B) |
| z16_mahler_points | algebraic T-adic Liouville points (Mahler) | protected outside windows (9ⁿ, 3·9ⁿ]; alive to depth 9 | Assessment |
| z16_zz_sibling | r = 17 sterile point as 17-ary percolation | ≤ 4 of 17 children boxed through depth 7; alive 0.6771 | EVIDENCE + Assessment |

## Spark relay Z9 (O240): menu-relative sterility (memos z15_*, deep file MENU_STERILITY.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z15_proth_sophie_germain | Sophie-Germain window m = 11 through the ET-sterile point μ = 0 of 3·2^s + 1 | **ES for all 3·2^s + 1** (proved ET/divisor-uncoverable family) — SHARP | PROVED (computer-assisted) |
| z15_witness_descent | witness symbol = Brauer/2-descent pairing on w² = φ(u) | Theorem A: sterile set of one-parameter menus ⊇ descent set (unit locus); unifies Schinzel, Thm 3.4 | PROVED |
| z15_window_jacobi_mu0 | constant windows at glued rational points | m ≡ 7 (8) dead at μ = 0; SG menu at μ = 0 is finite (resultant) | PROVED + EVIDENCE |
| z15_near_square_algebraic | Thm 2.2 for m = 16v³ | Z_105^□ not sterile for polynomial-in-v families | PROVED |
| z15_density_thin | thin menus vs (J)54 points | cannot help on positive-density prime sets; norm forms keep T1 | PROVED (thin) + Assessment |
| z15_ff_frobenius | F_q[T] analogue | Frobenius kills Aurifeuille; Carlitz divisors as spark | Assessment |
| z15_other_sterile_families | 7·4^s + 9, 15·2^s + 1, … | 7·4^s + 9: μ = 0 covered (m = 19), 2/1785 lifts left; c = 15, 63, 255: no SG window found at μ = 0 (stated bounds) | EVIDENCE |

## Spark relay Z12 (O245): the menu ladder / genus ladder at unit-square points (memos z18_*, deep file MENU_LADDER.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z18_descent_dies_at_D2 | Bruin–Stoll genus ladder for root menus X = 2^{s/D} | μ = 0 descent-sterile iff θ(θ−1) ∈ (A⊗ℚ₂)^{×2}; non-square for every D = 2…10, six families — in the tested range descent obstructs only at D = 1 | PROVED + CERTIFIED (SHARP) |
| z18_two_specialisations | integrality near μ = 0 | ⟺ values at Y = 1 in ℤ[1/2] and at Y = 0 in ℤ_(2): a family is an interpolation between n = 4^J and n = k | PROVED |
| z18_witness_localisation | product formula on Theorem A | for k = 1, c₀ squarefree, c₀-places silent; W(f) = parity over primes of Res(f, φ) | PROVED |
| z18_real_place | positivity of normal form n = σTT′ − T − T′ | even D: T, T′ have no real roots; linear shapes die | PROVED + EVIDENCE |
| z18_rung2_positivity | D = 2 rung (c₀Y² + k) | every Type II family non-escaping ⟹ μ = 0 unreachable (not T1, not descent) | PROVED (Type II) |
| z18_shape_search | exact shape varieties for 15·2^s + 1, D = 3…8 | 110–148 algebraic families at D = 4, none integral; none elsewhere | EVIDENCE (negative) |
| z18_exp_cover_criterion | exponential Thm 1.4 | compactness criterion PROVED; pointwise "iff descent" false for z14 windows and Type II rung 2 | PROVED |
| z18_primes_slices | Y = 2^{v₂(n−1)} as a positive-density root parameter | full slice progressions collapse to ET ⟹ Schinzel; "ladder stops at positive density" | PROVED (narrow) + Assessment |
| z18_s_deformation | coefficients polynomial in s | decouples integrality from positivity; rung 2 still closed (Type II); blocked for known shapes | PROVED (rung 2) + Assessment |

## Synthesis VII (O247): cross-combinations of wave Z second half (memos s7_*, deep file SYNTHESIS_SPARKS7.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| s7_window_lottery | least Type II (cap-0) window m₀(p): structure vs lottery | m₀ ∈ {3, 7} off Mordell-hard classes (Mordell, window form); shuffle test: congruence data explain all inter-window correlation; m₀ ≤ 107 to 10⁷; Dickson all-fail classes to M = 99 | PROVED + EVIDENCE + CONDITIONAL |
| s7_certified_caps | forced witness + forced small primes on lnr lines | per-class cap certificates; cap ≤ 1 on Haar ≈ 0.93–0.96 of lnr = 17; blind at r-generic points | PROVED (per class) + EVIDENCE |
| s7_sibling_certificate | finite certificate for r = 17? | fixed windows on the r-generic line (include M17 P-boxes), parity law (ℤ-twin of (J)67); level-1 survivors match Comp 4.1 at r = 19, 23; Frobenius exactly critical; no certificate | PROVED + EVIDENCE (negative) |
| s7_ff_nonlinear | Sophie-Germain / Carlitz / Frobenius-digit menus over F_q[T] | Baire: thin menus cannot touch open coverings; lifted digit identities = Galois conjugation (general digit identities open) | PROVED (negative) |
| s7_normform_collapse | binary-form (norm-form) rung of the menu ladder | Type II families (valid at one point) in binary-form coordinates are identities in n (any irreducible Q); Type I too on cones, any level — closes POINTWISE_BINARYFORM §5's open question | PROVED (SHARP) |
| s7_gaussian_square_windows | positive-density forced budget via p = a² + b² | K = S² forced at windows m ≍ p; cap-0 rate 10⁻⁴ = random windows (B3) | PROVED identity + EVIDENCE |
| s7_lvalue_proxy | m₀ vs L(1, χ_p) | Spearman 0.35 (0.20 Mordell-hard): hardness = QR-richness | EVIDENCE / Assessment |
| s7_typeII_free_controls | non-squares with f_II = 0 as T1 controls | Type II has x ≤ n/2; 103 such n ≤ 2·10⁵ (3985 = 5·797 window-free to 1.2·10⁷) | PROVED + EVIDENCE |

### z23 — O251 lattice meeting point / class-group slice moves (deep file LATTICE_MEETING.md)
| memo | idea | outcome | label |
|---|---|---|---|
| z23_empty_meeting_locus | Thm 3.4(c)'s meeting point (2k, 1) as a target set | finite {a + b = k(4ab − p)}; empty for 99 primes ≤ 10⁶; 98 rescued on split slices (height √d), p = 3361 has no Type II solution on any slice lattice of ℤ[√−p] | PROVED + CERTIFIED (SHARP) |
| z23_norm_blind_predicate | carry k ∣ h along composition in Cl(−4p) | ES at slice g ⟺ ∃ k ∣ h: (−4k²p mod g) ∣ k; a class-based mechanism acts only through the norms it produces | PROVED + Assessment |
| z23_controlled_lift_tower | lifts g → gu, u ≡ 1 (4h), keep h ∣ h′ | ES propagates only down the tower (divisor lattice of 4k²p + d) | PROVED (negative) |
| z23_fixed_line_genus | Vieta/Gauss reduction on a fixed line k | k ∣ 6: genus property of coprime coefficients (B1), not preserved by all moves; else B2 datum; reduction moves nothing in practice | PROVED + EVIDENCE |
| z23_parity_budget | two forced slots | slices/levels never forced (4h ≡ 1); ≤ 1 forced slot per point | PROVED (negative) |
| z23_expander_walk | how far is an ES class | ≤ 4–8 steps when it exists (expander, JMV 2009): walk adds reachability only | EVIDENCE |
| z23_biquadratic_height | all ET d at once in ℚ(√−p, √d) | reciprocity could only correlate failures (B2/B5) | CONJECTURE-level spark |

### z28 — O257 non-congruential lifts + numerator-model laboratory (deep file NONCONG_LIFTS.md)
| memo | idea | outcome | label |
|---|---|---|---|
| z28_slice_vs_witness_level | classify lifts by the level they read | slice-level ⟹ O253 Cor 3.3; polynomial ⟹ Schinzel collapse; only witness-level (size-dependent modulus) escapes = B2 | PROVED |
| z28_espectrum_share | lifts sharing the source's factored number | exactly 4 share relations; validity ⟺ (θ, e) ∈ Spec(p): only the e-value is transported | PROVED (negative) |
| z28_complete_levels | levels where visibility suffices | k = 4: 7-smooth rule (CERTIFIED ≤ 6000); k = 8, 12: none ≤ 400k; **Thm 2.6: x_{ℓ,2} uncovered for all 4 ∣ k ≥ 8, for k = 4 iff ℓ ∉ {3, 5}** ⟹ no complete level through ℓ ≡ ±3 (8) | PROVED + CERTIFIED |
| z28_matched_profile | sources sharing p's non-residue primes | Lemma: B-smooth witnesses become visible; 0/1347 sources total at Mordell primes ≤ 10⁵; false in k = 8, 12, 16 models | PROVED + CERTIFIED (negative) |
| z28_size_information | do source sizes inform p's divisor events? | permutation test: no signal beyond size | EVIDENCE (negative) |
| z28_lottery_margin | exact E_k to 10⁸, f_k/log³ | exceptions where expected count is O(1); k = 4 margin ×2 (mean), ×6 (min); screen refutes only threshold-free laws | EVIDENCE |
## Synthesis VIII (O258): cross-combinations of wave AA (memos s8_*, deep file SYNTHESIS_SPARKS8.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| s8_mutual_shift_pairs | Type II = pairs x \| cn + y, y \| cn + x with 4c \| N | b = 1 / c = 1 lines = the two 2-adic faces of MP(p); b = 1 duality (Prop 1.3) | PROVED |
| s8_volume_dfi | DFI Kloosterman fractions at one p | DFI is uniform in a = p; failure is O(1) points per box (completion error ≥ (XY)^{1/2}) | PROVED + Assessment |
| s8_twisted_hyperbola_thue | Thue/Minkowski on Xε ≡ u (p) | height free, class tied to the height: not a lattice problem | PROVED equivalence + Assessment |
| s8_b1_line_census | one shift family p + 4d, divisor ≡ −1 (4d) | fails only at 193, 2521, 66529 ≤ 10⁸; b = 1 ∪ c = 1 never fails ≤ 10⁸ | EVIDENCE + CONJECTURE (SHARP) |
| s8_perj_lottery | per-j failure and cross-j correlation | near-independent (ratio 1.004); large primes private to one j (Lemma 2.3): pigeonhole across j void | PROVED + EVIDENCE |
| s8_forced_visibility | route lifts through forced windows | (K_q/p) = (q/p); every cap-0 certificate has (uv/p) = −1 — same parity, no totality | PROVED |
| s8_signed_genus_wall | signed → positive Type I move | d > 0 ⟹ (d/p) = −1, d < 0 ⟹ (\|d\|/p) = +1; no \|d\|-preserving move, no Vieta | PROVED |
| s8_profinite_proximity | smooth p − 1 = near the T1 point 1 | a few per cent beyond squareness; mostly QR-richness | EVIDENCE (weak) |
| s8_numerator_two_lines | k = 8 analogue of the two lines | fails at 34 primes < 8000 incl. 131, 241: 4-specific | EVIDENCE |
| s8_numerator_size_screen | (vi) is the 4-specific step a size inequality? | k-model = ES with (k/4) \| gcd(x, y, z); O257's inequality = 2-adic parity of d; threshold forms are stronger than ES | PROVED (trivial) + Assessment |

## Spark relay O259: the b = 1 line (memos z29_*, deep file B1_LINE.md; not yet triaged)

| memo | idea | result | label |
|---|---|---|---|
| z29_lopez_typeA | literature: is the b = 1 line known? | yes: López 2022/2024 Type A (Thm 7 = divisor form), Type B = (★), Conj 1 = union; 193, 2521, 66529 known | literature |
| z29_pair_genus_law | T1 as Jacobi law on pairs {S, T} | (ST/p) = −1, (S′T/p) = −(2/p)^k; 2-adic escape shared with (★) and only on trivial classes | PROVED (non-discriminating) |
| z29_dickson_least_shift | why smooth p − 1 is hard | M_σ \| p − 1 freezes shifts ≤ σ (Prop 4.1); least shift unbounded under Dickson (Thm 4.2); full line out of reach of the construction | PROVED + CONDITIONAL |
| z29_forced_level_characters | force the class −1 at a forced level d | χ₋₄(p + 4d) = +1 always: no level is forced by characters; needs a prime ≡ 3 (4) in p + 4d (Landau event) | PROVED (negative) |
| z29_twice_the_trials | why b = 1 ≫ (★) in robustness | same incidence main term (log p)²/8, but (★) incidences pair up by a swap: half the distinct trials, twice the exposed classes | PROVED + EVIDENCE |
| z29_nb_tail_model | calibrated tail model, finite failures | NB(μ = (log p)²/8, D ≈ 3) ×2-optimistic in back-test; expected failures beyond 10¹¹ < 10⁻⁵ | CONJECTURE (heuristic) |
### z27 — O256 balanced relation lattices: from Hypothesis W to GRH (deep file BALANCED_LATTICE.md)
| memo | idea | outcome | label |
|---|---|---|---|
| z27_pretentious_dual | dual of the relation lattice = characters; balance ⟺ no ℓ¹-pretentious character on S | in the class, GRH-Frobenius affords essentially only the index condition; extremal character has order ≍ N (99 %+ divisible by P⁺(N)) | PROVED + EVIDENCE (SHARP) |
| z27_fejer_blind_count | class-blind count of pretentious primes (Fejér pairs) | ≤ 48(6xε)^{(k+1)/(k−1)} log P/log x; P-loss exact, = CAP_INTERPOLATION 4.2(b) | PROVED |
| z27_sparsity_hypothesis | weakest replacement of W | GRH + EQ ⇒ (log₂p)^{13/2+o(1)}; GRH + S (p-free, class-free) ⇒ (log₂p)^{9/2+o(1)}; EQ uniform at toy scale | CONDITIONAL + EVIDENCE |
| z27_small_exponent_windows | composite windows with U_m of tiny exponent | Linnik adversary (primorial modulus) on the menus Q(E): cap ≳ log p i.o. (R269 repair: was the pre-repair (log p)^{c log₃p}) | PROVED obstruction |
| z27_smooth_shift_crt | (q−1) smooth ⇒ every ℓ-part visible | joint CRT law still invisible; smooth shifted primes with u → ∞ unknown | Assessment (dead) |
| z27_large_sieve_sunits | large sieve over moduli for the S-unit box | S-units too sparse (M = P^{2H} ≫ Q²) | PROVED (negative) |

### z36 — O266 Zaremba 2026 growth method → ES in CF coordinates (deep file ZAREMBA_TRANSFER.md)
| memo | idea | outcome | label |
|---|---|---|---|
| z36_density_threshold | exact input of Shkredov/Zhang | needs half-set density q^{−O(κ)} (1 − w ≤ κ/8, ε < 1/18), not just a power count ("M1⁺") | reading of sources (preprints unrefereed) |
| z36_farey_least_qnr | ES ladder λ(p) ≤ L | λ(p) ≪ log p log log p unconditional (Thm A; known in substance, Chang/Larcher); ≪ M log p under ZQ_M (Thm B) | PROVED + CONDITIONAL |
| z36_reciprocal_sum_gluing | ES-five as Möbius gluing | t ≡ ū + v̄, tuv − u − v < 2p (Lemma C); origin boxes, one expected solution per box; region knob vacuous (Lemma D) | PROVED + Assessment |
| z36_chi_twist_window | Zaremba with a non-residue (ZQ) | ε < 1/18 vs Burgess ε > 1/8; ZQ fails at squares so growth alone can't prove it; Zaremba(M) ⇒ ZQ_{4Mn_p} | CONJECTURE + Assessment; EVIDENCE ZQ₄ < 2·10⁴ |
| z36_numerator_free_rung | drop χ, keep length 3 | = Lorenzini's (W) (known: (J)15, bsG_even_half); 12 exceptions ≤ 2·10⁶ | no new claim |
| z36_hj_cantor_dimension | effective dimension of rungs | L = c log p: |S_L| = p^{θ(c)}, θ(1) ≈ 0.85; method window lies at L ≥ C₀ log p | EVIDENCE + Assessment |
| z36_reciprocity_obstruction_home | thin-orbit home of T1 | Rickards–Stange (Duke 2025) reciprocity obstructions: same source/obstruction/conjecture shape; proved fat case; Question R | dictionary (Assessment) — SHARP candidate |
