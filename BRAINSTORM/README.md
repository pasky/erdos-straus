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
| BRIDGE_WORLDS.md (deep) | three tiers of bridges (homomorphic ±1 / fixed symmetric rational expressions = rationals / Frobenius-invariant = K⁺ → F_h); unit twists (trivial unless totally positive) | no route; scoped negative + PM-II | see file |
