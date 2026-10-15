# AGENT_REPORT_O233 — spark relay Z3: global Fano over the supersingular 2-isogeny graph

Branch side-agent/global-fano (merged side-agent/four-adic-input first, as instructed). Deep file `GLOBAL_FANO.md`. Seven memos
`BRAINSTORM/z9_*.md`, indexed in BRAINSTORM/README.md. Scripts `scripts/z9_*`, data `data/z9/`. **ES is not solved, nor any infinite case.**
No positive ES-type claim is made.

## SHARP:
1. **Loops = representations of 2 (PROVED, short; CERTIFIED on 9489 edges, p ≤ 2000).**
   * For p ≥ 11, an edge (E, C) of G_p is a loop of G_p/Frob (E/C ≅ E^{(p)}) ⟺ its lattice L ∈ 𝔊⁻_p represents 2.
   * More generally, for m < p/4, r_L(m) = #{x ∈ End(E, C) : deg x = mp}. Every such x has trace 0 because p | trd on the ramified prime.
   * Consequence: certificate edges sit in the "Frobenius layers" of their letters, so they are near the spine. This explains a 4×
     enrichment of path edges among loops (22.6 % vs 5.8 %, all p ≡ 1 (4) ≤ 10⁴). (z9_frobenius_layers)
2. **TES failures are bit failures, not character failures (EVIDENCE, one Type II slice).**
   * In the TES analogue of ES's slice-T words, the cubic symbol χ₃ at π does not control the λ-adic divisibility of the numerator.
   * At all 13 TES failure primes with N ≤ 787 there are hundreds of words with the target χ₃. At 7 of them some target words even have
     λ⁴ | T and fail only at the 2-primary anchor.
   * Reading (Assessment): 9 = λ⁴ is several trits above TES's character level, while ES's 4 is exactly at it (O224: zero bits).
     This is a coherent account of why TES has certified failures at primes and ES-five has none to 10⁸. (z9_order3_fano)
3. **Heegner-layer dictionary (Assessment; algebra PROVED).**
   * Layer t of G_p is the supersingular reduction, at the ramified prime p, of the CM points of X₀(2) with CM by orders ⊇ ℤ[√−tp]
     (ε = −(1 + ij), ε² = −tp).
   * Inside a layer, a certificate requires (necessary) that the attached ideal class contain an ideal of norm A ≡ −1 (mod t) with
     A | tp + 1. That is WINDMILL Prop 10.3's residue event. The level-t ring condition must be added (review repair).
   * This puts CONSTRUCTIVE_ES ((J)35) and the ℤ[√−tp] class-group framework on one geometric object. It is the precise place where a
     global Fano would have to act: ray classes mod a varying t. (z9_heegner_layers)
4. **Depth = walk (PROVED + CERTIFIED).**
   * A pentagon vector with v₂(Q(x)) = k is a conic-marked non-backtracking walk of k − 1 half-steps in G_p.
   * So 8/p five-slice certificates are certificate edges whose pointer half-vector is a conic point at the pointed endpoint, which
     makes them a marked X₀(4) datum. This turns O224's tree-depth Assessment into a theorem (with the marking, which the review showed
     is essential).
   * Bits are constrained, but not determined, by v₂(t) or v₂(tp + 1). (z9_depth_walks)

## Main conclusions (goal by goal)
* **(1) Global Fano.** There is no parity, degree or pointer law on G_p.
  * P(p) is even for 47.6 % of the 609 primes p ≡ 1 (4) ≤ 10⁴.
  * The path subgraph has no odd vertex at 5, 13 and 2521.
  * Both-end pointers are absent at 17 primes.
  * Structural reason: the only involutions are quotiented out, and every exactly computable global count is genus/mass level.
  * Control: at n = 105 the analogue graph exists (4 vertex classes, 4 edge classes) but has no path edge. So graph existence alone
    cannot force a certificate.
* **(2) Depth bits.** Proved (SHARP 4). The p = 131 numbers are reproduced. Counterexamples (p = 293, t = 3; p = 97, t = 2) show the bit
  is not a function of t alone.
* **(3) Order-3.** There is no "Q mod 3 on L/λL" Fano: a cubic symbol has no quadratic form behind it, and the ES pentagon symmetry is
  broken by the unequal coefficients (ω, ω², 2). The sharp test comes out negative (SHARP 2).
* **(4) Prop 10.3 / Brandt screen.**
  * L1: Hecke eigen-covariant linear functionals see only the mass of the path classes. This is PROVED for such functionals; the
    general trace-formula claim is Assessment.
  * L2: degree-2 Siegel–Weil sees binary planes only up to genus, so the glue residue ±1 is invisible.
  * L3: class-wise theta series determine the class (Schiemann), so they see everything, but asking that some class have the path
    property is the original problem (B2).
* **Shape widening.** Triangle (cyclic plumbing) classes are decoupled from path classes. At 47 of 329 primes ≤ 5000 there are
  χ = −1 triangle classes but none of them is a path class.

## Self-review (deep reviewer, `review` tool): no FATAL; 5 MAJOR, all accepted and repaired
* **Depth walks.** An unrestricted continuation exists even without the conic condition (p = 5, w = (1, 3, 4)). The lemma is now
  stated for conic-marked walks, and the S₈ characterisation uses the marking.
* **Bits.** "One bit per letter t" was false. It is now "constrained by, not determined by", with the two counterexamples.
* **L1.** The claim was over-broad. It is narrowed to eigen-covariant functionals. Mass of path classes and the mass-weighted count
  of path bases are now distinguished.
* **Heegner converse.** It dropped the level-t ring condition (counterexample (3, 1, 7), p = 13, with signs flipped). The condition is
  now reinstated, and the class condition is labelled as necessary.
* **TES radius.** The search radius was wrong for c_i = 2: 4 words were missed at N = 97, plus omissions at 151 and 769. Fixed and
  data regenerated; the aggregate numbers are unchanged to 3 digits.
* **Minor.**
  * Layers above p/4 need the trace-zero qualification.
  * A walk length is not a graph distance.
  * The 105 wording was too strong and is weakened.
  * The float search bounds in z9_lib are now documented.
  * The triangle scope is narrowed.
* **Reproduced by the reviewer.** The loop table (9489 edges / 1191 loops), the depth checks (612 and 1190 pointers), the triangle counts,
  the parity statistics and the 105 control.

## Labels
* PROVED: z9_frobenius_layers Lemma 1; z9_depth_walks Lemma 1, Cor 2 and Prop 3(i)–(iii) (with marking); z9_brandt_screen (L1,
  narrow); the z9_heegner_layers (a) forward algebra.
* CERTIFIED: loop ⟺ represents 2 (p ≤ 2000); marked walk length (p ≤ 200); the 105 control.
* EVIDENCE: no parity laws (10⁴); TES χ₃ independence (N ≤ 787, one slice); triangle decoupling (5000).
* Assessment: the Heegner-layer ideal-class reading; the TES "trits above the character level" explanation; L2/L3 placements.

## Verification
* Commands, each well under 30 min on one core:
  * `cd scripts && uv run python z9_stats.py 5 10000`
  * `z9_loops.py 5 2000`
  * `z9_depth_walk.py 200`
  * `z9_triangle.py 5 5000`
  * `z9_tes_agg.py 800`
* The edge counts of `z9_graph.py` match CONSTRUCTIVE_ES |𝔊⁻_p| at 37, 73, 97, 193, 1009 and 2521.

## Sparks (not pursued)
* **Ray-class Galois action on layer-t CM points.** Remark 10.4 says ray classes mod t see the certificate condition. For a fixed
  small t, Gal(ray class field mod t of ℚ(√−tp)) acts on the layer-t CM points of X₀(2) mod p. Is there a reciprocity law (Shimura)
  that ties the ray class of the reduction to a Frobenius at p? If so, the B2 obstruction would become a Chebotarev statement at fixed
  t, and unions over t ≤ T would be a moving family.
* **Loop layer as the "Mordell q = 2" engine.** Layers 1 and 2 reproduce the q ∈ {2, 3, …} Mordell classes. Test whether every certificate
  at hard primes lies in some layer m ≤ 7 at a *non-letter* position (a vector of norm m that is not a basis vector).
* **Marked X₀(4) count.** Count S₈ certificates as marked 2-walks. The marking is a conic point, so does the mod-2 conic geometry at
  the middle vertex give a cell law for 8/p (an analogue of the 7/12) at the graph level?
* **TES Type I slice and other shapes.** Complete the χ₃ test over all TES shapes. Check whether any TES failure is a genuine
  "no target word" failure.
* **Composite controls.** For composite non-square n (105, 1155, …) the 2-neighbour graphs exist in several genera. Locate exactly
  which genus the words of n occupy. 1155 has isotropic words, but none in the component of ⟨1, 3, 385⟩.
