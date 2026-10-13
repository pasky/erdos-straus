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
