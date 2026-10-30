## Wave z52 additions (2026-10-30)

These entries come from the z52 literature lanes L1–L7, graded in `reviews/z52-lit-grading.md`. I re-opened every
arXiv record below in the arXiv API on 2026-10-30 (`sources/z52/grade_lit/api_records*.txt`). Items marked "PDF"
were also read in the PDF (`sources/z52/grade_lit/pdf_excerpts.txt`). ES remains OPEN, and none of these items
changes its status. "New" means arXiv v1 dated after 2026-09-28. The other items predate the cutoff but were not
previously recorded in the repository.

**New since 2026-09-28**
* Y. Cao, X. Xu, "Prime Numbers of the Form 24m+1 and Erdös-Straus Conjecture", arXiv:2610.32302v1 (2026-10-23).
  * Statement: a polynomial primality criterion for 24m + 1, plus 56 "solvability polynomials". The abstract says
    "numeric test shows that they imply the conjecture". In §3 the authors state that they tested the claim for
    m ≤ 10¹¹ and "failed to get a logic proof".
  * Status: unproved covering conjecture (preprint).
  * Relation: a finite menu of polynomial families falls under FRONTIER B1 (Thm C), so it fails for infinitely many
    p ≡ 1 (24), CONDITIONAL on Hypothesis H. This is an Assessment, since the polynomial form of every family was not
    checked.
* M. Filaseta, A. Kalogirou, J. Klein, "Results for distinct covering systems with a prime minimum modulus q ≥ 11",
  arXiv:2610.34541v1 (2026-10-25).
  * Statement: if the least modulus of a covering system is a prime q ≥ 11, then Σ 1/mᵢ ≥ 1 + 10⁻²⁸. No covering
    system uses distinct multiples of q as moduli.
  * Status: preprint.
  * Relation: finite-system structure theory, outside B1; no ES relevance.
* H. Li, Z. Liu, "6 powers of 2 in the Linnik–Goldbach problem", arXiv:2610.15784v1 (2026-10-11), PDF.
  * Statement: Thm 1.1 says every sufficiently large even N is the sum of two primes and at most 6 powers of 2,
    with r₆″(N) ≥ N L⁶/1000 and L ≍ log N. Thm 1.2 lowers this to 5 under GRH. The previous record, per the paper's
    Table 1, was Johnston–Trudgian 2026 with 7 unconditional and 6 under GRH (Johnston–Trudgian not accessed).
  * Status: preprint.
  * Relation: a power-size Goldbach reservoir (FRONTIER §4.6). Every source states the problem with *two* primes.
    The natural one-prime rungs fail: p + 2^k fails on an arithmetic progression (Erdős 1950), and p + 2^a + 2^b
    (≍ log n witnesses) fails infinitely often (Crocker, Pacific J. Math. 36 (1971) Thm I, PDF; Pan 2011), as
    already recorded in `BRAINSTORM/s9_lower_tail_literature.md`.

**Not previously recorded (pre-cutoff)**
* S. Li, "Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306", arXiv:2609.32140v1
  (2026-09-26).
  * Statement: every positive a/b with b squarefree is a finite sum of distinct 1/(pq), with p ≠ q primes.
  * Method: a complete bipartite prime graph; a Fourier count of subgraphs with reciprocal sum ≡ a/b (mod 1); a
    positive main term from small frequencies; divisor counting plus no-wrap CRT for the other frequencies.
  * Provenance: Lean-formalised except one cited Ramanujan inequality; human–AI collaboration. The abstract credits
    **Tang's Lean development with the first proof**. The erdosproblems.com #306 page (accessed 2026-10-30; last edited
    2026-06-21) does not mention this result and links one forum "proof claim".
  * Status: preprint.
  * Relation: abundance over an unbounded number of terms (B3/B6), so it does not transfer to 3-term ES.
* O. Klurman, I. E. Shparlinski, J. Teräväinen, "On the generation of multiplicative groups by small primes",
  arXiv:2609.25393v1 (2026-09-21), PDF.
  * Statement (Thm 1.1): for fixed ε, A, there is a set of ≤ (log Q)^{1+ε} primes, each ≤ (log Q)^{C*(A+1)}, whose
    0/1 subset products give all of (ℤ/q)^× for all but O(Q(log Q)^{−A}) integers q ≤ Q. The exponent 1 + ε is
    optimal.
  * §1.2: the result holds pointwise under GRH, by orthogonality. Removing the exceptional set (even to a
    better-than-super-polylog saving) would settle Vinogradov's least-QNR conjecture.
  * Status: preprint.
  * Relation: free, shared primes and almost all q. Gate G4 (`EXSET_CHAR_FORCING.md` §2) needs the prime factors of
    one p-tied integer to hit −1 (B2, §4.9, §4.17).
* Y. Hashimoto, "Finiteness of Disjoint Covering Systems with Precisely One Repeated Modulus", arXiv:2603.26043v2
  (2026-09-25), PDF.
  * Statement (Thm 1.1): for each m ≥ 2 there are only finitely many disjoint covering systems with
    3 ≤ n₁ < … < n_{t−m} < n_{t−m+1} = … = n_t. This confirms the finiteness conjecture of Ekhad–Fraenkel–Zeilberger.
  * Status: preprint.
  * Relation: none for ES (B1).
* G. Alkauskas, "Squares, three fleas, sporadic sets, and squares", arXiv:2508.05347v3 (2026-09-09), PDF.
  * Statement: the flea orbit of G = {(0,0), (2,1), (3,2)} lies inside a Descartes-quadruple (Apollonian-type) orbit.
    Thm 2 proves three things: every half-integer area occurs, via the linear family s = 1 + 2t; integer areas meet
    every residue class mod every m; and **no square occurs**, by an HKRS-type quadratic-reciprocity character.
  * Up to 10¹² the only missing non-squares are 5, 29, 80, 99, 179. Completeness is "still unproved".
  * Status: preprint.
  * Relation: a fourth instance of the "squares + finitely many sporadic" shape, after Rickards–Stange Thm 2.8
    (proved, fat), HKRS (open) and U(n) (campaign, open).
  * Campaign reproduction (`scripts/z52_gradelit_fleas.py`, EVIDENCE): the same 5 sporadic values up to doubled
    area 10⁶; average multiplicity ≈ X^{0.32} (power-size), so the flea problem is not a polylog model of U(n).
* N. Sothanaphan, "Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof", arXiv:2601.07421v5
  (2026-01-26).
  * Statement: for 0 < C₁ < C₂ and 0 < ε < 1/2 there are infinitely many (a, b, n) with εn ≤ a, b ≤ (1−ε)n,
    a!b! | n!(a+b−n)! and C₁ log n < a+b−n < C₂ log n. The proof uses Kummer carries plus a counting choice of m in
    [M, 2M].
  * Status: preprint with a Lean proof; similar to arguments of Erdős and Pomerance.
  * Relation: averaging over m (B6). No 2025–26 AI-assisted Erdős resolution recorded by the lanes (#283, #306, #728,
    #729, #401, #38, #90) has ES's "every n, polylog witnesses" shape.
* N. Kingsbury-Neuschotz, "Strong Approximation for the Relative Character Variety of the Four-Times Punctured
  Sphere", arXiv:2603.04096v3 (2026-07-29).
  * Statement: for nondegenerate (A, B, C, D), Γ acts transitively on the bulk of the F_p-points of
    X² + Y² + Z² = XYZ + AX + BY + CZ + D for a density-one set of primes. There are two or four large orbits in the
    degenerate cases.
  * Status: preprint.
  * Relation: a density-one result (B6). Chen's all-large-p mechanism (divisibility of orbit sizes) has no ES
    analogue (`BRAINSTORM/z31_markoff_chen.md`).
* N. A. Carella, "Upper Bound of the Least Quadratic Nonresidues", arXiv:2106.00544v9 (2025-10-09), PDF.
  * Claim: n(p) ≪ log p (log log p)^{1+ε} unconditionally.
  * Status: **gap**. In (7.6) the v-range is extended from v < p/x to v < p while "uv < p" is still used for
    1/|sin πuv/p| ≪ p/(uv). The claimed bound would also beat the GRH bound (log p)².
  * Relation: unusable.
* Y. Lamzouri, X. Li, K. Soundararajan, Math. Comp. 84 (2015), arXiv:1309.3595v3, PDF.
  * Statement: Cor 1.1, under GRH, the least quadratic non-residue mod a prime q ≥ 5 is below (log q)². Thm 1.4
    gives the least prime in a coset aH of index h.
  * Relation: under GRH this supplies the character side of the campaign's "(q/p) = −1 for some prime
    q ≤ 2 log²p" reformulation. It gives no divisor-class input.

**Updates and corrections to existing entries**
* Shkredov arXiv:2603.14116v2 (PDF):
  * Thm 8: for all M ≥ M₀ and every q there are ≥ q^{2w_M−1−o(1)} numerators with partial quotients ≤ 100M. The
    method itself proves q^{1−O(1/M)}.
  * Remark 9: via Zhang–Tang general-modulus expansion, Cor 1 "is valid for any q … we now possess a proof of
    Zaremba's conjecture in full generality".
  * X. Zhang arXiv:2605.02518v2: Thm 1.2 "Zaremba's conjecture holds"; Remark 1.3, M is effective but large.
  * Both remain unrefereed. The entry at `LITERATURE_2026.md` §Wave AA stands.
* The *Bull. AMS* 63(1) (2026) 59–77 survey "Apollonian packings: The rise and fall of the local to global conjecture"
  is by **Elena Fuchs** (DOI 10.1090/bull/1874, Crossref), not Kontorovich as `QUESTION_R.md` §5 says.
* Chen's Markoff paper is "Nonabelian level structures, Nielsen equivalence, and Markoff triples", *Ann. of Math.*
  199 (2024), DOI 10.4007/annals.2024.199.1.5. The z52 lane L3's title "A proof of the Markoff conjecture" is wrong,
  and the Markoff uniqueness conjecture remains open.
* Shi–Shi–Whitehead–Williams-Tracy–Zhang arXiv:2510.21702v2 (2026-03-25) and Kadyrov et al. arXiv:2610.16530v1
  (2026-10-12) were re-verified and are already cited in `QUESTION_R.md`.
* Ventas arXiv:2605.04551 is at **v3** (2026-10-15); the content is unchanged (heuristic Borel–Cantelli).
