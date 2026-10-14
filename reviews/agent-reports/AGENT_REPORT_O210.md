# AGENT REPORT O210 — spark relay Y2: friezes (FRIEZE_ES.md, memos BRAINSTORM/y2_*)

Branch side-agent/frieze-es (main merged in, incl. R205 repairs of LENGTH_THREE). **ES is not solved; no infinite case
of ES is claimed.**

## SHARP
1. **Even-edge theorem (PROVED, 3-case proof; CERTIFIED).** For every positive formal word (c, m, s) at odd N, the five
   cluster variables (h′, c, m, s, h) contain **exactly two even ones, and they are adjacent** (mod-2 rigidity of the
   A₂ frieze). If e, e′ are those two, then
   `(h′/N) = (−1/N)·(−1)^{[8 | ee′]}`.
   * For N ≡ 1 (4): sign −1 ⟺ 8 | ee′ ⟺ some cluster variable is ≡ 0 (4). This is DK Thm 4.5 without the 512-cell
     check, extended to formal words and to N ≡ 3 (4).
   * At odd squares, every frieze has ee′ ≡ 4 (8) (T1).
   * CERTIFIED on all 5 115 860 formal words with odd N ≤ 10⁵, plus 2·10⁶ random words with N up to ~10¹², plus 28 474
     square-control words.
2. **Transport law (PROVED).** For N ≡ 1 (8): (h′/N) = −(2/o), where o is the odd cluster variable opposite the even
   edge (h, s, c or m). The Legendre symbol at the big modulus N equals minus the character of 2 at a small modulus.
   Tree picture: the five ends form two cherries in the 2-adic Bruhat–Tits tree. The sign is "cherry depths sum ≥ 3",
   and T1 is "depths (1, 1)".
3. **T1 lives exactly in positivity.**
   * The proof uses positivity only in the reciprocity steps (archimedean Hilbert factor). Signed (tame) friezes at
     every odd square have zero-mod-4 quiddities.
   * Hence the Short–Van Son–Zabolotskii lifting theory, which is about tame integral friezes, is T1-blind. Indeed every
     closed odd walk (lengths 3, 5, 7) on F₄ (the octahedron) is strongly contractible.
   * Finite-ring frieze counts are N-blind beyond N mod 8.
   * Steering rule: *a frieze-theoretic ES proof must use the positivity of the frieze archimedeanly.*
4. **Hexagon vs pentagon (PROVED).**
   * The 4-term analogue has the uniform frieze proof (2, 2, 2, k) at N = 4k − 3: the diagonal K(2,2,2) = 4 cuts off
     a free triangle containing the N-side. The identity is
     4/N = 1/k + 1/(k(2k−1)) + 1/((2k−1)(3k−2)) + 1/(N(3k−2)).
   * In the pentagon the same cut needs a length-2 word at 4w, i.e. 4w + 1 = xy with y ≡ −N (mod 4w): B2. For w = 1 it
     needs 5 = xy, which has only the formal factorisations, and those give N ≡ 3 (4).
   * Polygon-size uniqueness: r = 3 is the only HJ length whose zero-mod-4 locus is a Jacobi fibre, PROVED for r = 2, 4
     and r ≡ 0 (4), witnesses for r ≤ 12; CONJECTURE for all r. This parallels (J)32's "m = 4 unique".

## Brief items
* (a) Frieze proof: SHARP 1.
  * SL₂(ℤ/8) theory: there are 80 classes per N mod 8. The only local obstruction to lifting a spur-walk to a positive
    frieze at N is N = □. EVIDENCE: every class is realised with positive frequency at non-squares (N ≤ 2·10⁴), but at
    a given N the lifting is a coupon-collector lottery, namely SQ₅.
  * Local–global: yes, with T1 as the sole local obstruction, and that obstruction is archimedean (positivity).
* (b) SHARP 4.
* (c) A model exists (CHJ sub-polygons of Farey triangulations / snake graphs), but it is a relabelling. #F(N) has no
  closed form (divisor convolution).
* (d) Twisted period 5: it forces an even edge mod 2; mod 4 is impossible by T1.
* (e) 2-adic tree / tropical (SHARP 2); signed friezes and Farey distance (SHARP 3).
* Also: windmill/parity is closed. The frieze surface mcs − c − s = N is multilinear, so the only involution is the
  reflection, and #F₋(p) is always even.

## Files
* FRIEZE_ES.md (§1 proof, §2 transport, §3 positivity, §4 polygon size, §5 constructive table, §6 verdict).
* Memos y2_even_edge, y2_farey_complex_lifting, y2_hexagon_degeneration, y2_twoadic_tree_transport,
  y2_parity_involution, y2_zamolodchikov_forcing, y2_coefficients_model, y2_positivity_is_T1 (indexed in
  BRAINSTORM/README.md).
* Scripts y2_even_edge (+_random), y2_f4_walks, y2_lift8, y2_hexagon, y2_transport, y2_signed, y2_witness.
* Log: logs/y2_even_edge_1e5.txt.

## Honesty notes
* Thm 1.2 is a reproof plus mild extension of a known equivalence (DK/CHI_FLIP); its novelty is the form.
* The transport law is Hilbert reciprocity localised.
* "No hidden mod-8 obstruction" is EVIDENCE at N ≤ 2·10⁴ only.
* The polygon-size uniqueness is proved only for the listed r.
* Literature: SVZ Thm 1.6 was read in the PDF. CHJ authors were verified via the arXiv API: Cuntz–Holm–Jørgensen,
  not "Cuntz–Holm–Pagano" as in the orchestrator note. Guo (tropical friezes), Beardon–Hockman–Short and MSW are cited
  from memory.
* No self-review subagent was run (left to the parent).

## Sparks (not pursued)
1. **General-r frieze Jacobi law.** For any (r+2)-gon with frozen (1, …, 1, N), (A/N) is a function of the mod-8
   frieze. Find the closed form, presumably a product over the "backtrack runs" of the K₃ winding walk. Then prove the
   r ≥ 4 uniqueness CONJECTURE.
2. **Transport + Chebotarev in the o-aspect.** For N ≡ 1 (8) the sign is −(2/o). Is there a family of words whose
   opposite vertex o runs over primes in a progression *independent of N*? That would turn the sign question into
   "o ≡ 7 (8)", which has density 1/2 with no T1. T1 must then show up as non-existence of such families at squares.
   This is an H-A statement in a new coordinate.
3. **Eisenstein friezes and the order-3 T1 ((J)19).** Repeat the even-edge analysis over ℤ[ω] at the prime 1 − ω. Is
   there a mod-(1−ω) rigidity and a "cherry depth" law for TES?
4. **Mod-16 refinement.** Does the joint law of (sign, o mod 16) carry information at squares (a second-order T1
   shadow)?
5. **Positivity as the archimedean place.** Formalise "frieze positivity = (·,·)_∞" as a statement about the real
   points of the A₂ cluster variety (the positive chamber). Is the positive chamber's integral-point count at N
   expressible by a Siegel–Weil-type product in which the ∞-factor carries the sign? That would connect to (J)13
   Kudla.
