# SIEVE_PAPER_V2 — changelog for paper/sieve-limits-note.tex (task O15)

Branch `side-agent/sieve-paper-v2`. Status: **checkpoint 1, ready for referee.**
Compiles clean (pdflatex, 3 passes; no undefined refs/citations, no overfull
boxes; three harmless underfull boxes). 33 pages (was 24 or so).
Author "Anonymous"; TODOs only as `%` comments (the existing
`TODO(submission)` was kept).

## Sources used (all in main, hostile-reviewed)
* EXCEPTIONAL_KARY.md §§1–4 (Thm 2.5, Cor 2.6, Rem 2.8, Thm 4.1, Lemmas 4.2/4.2′/4.3,
  Thm 4.5); reviews exceptional-kary-review.md and -review-2.md (E1, E2 used).
* EXCEPTIONAL_TWIN4.md (Lemma 2.3, Thm 7.1, Prop 9.1, Lemma 9.2/Cor 9.3,
  Thm 10.4; §9.3/§12 OPEN; §11 SKETCH); review rounds 1–2.
* EXCEPTIONAL_NONCRT.md (Prop 2.1, Lemma 2.2, Thm 2.3, Cors 2.4–2.5,
  Lemma 3.1, Thms 3.2–3.3, Rem 3.4, Props 4.1–4.2, Thm 8.1, Lemma 8.2,
  Cor 8.3, Prop 8.4, Prop 8.6/Cor 8.7, §8.3); review rounds 1–2.

## New structure
| § | content | change |
|---|---|---|
| abstract, §1 | rewritten around KARY Thm 4.5 as the main theorem; results list reordered (main thm, tools, campaign, Λ², non-CRT, exclusions); 8 internal docs + 9 reviews cited; label "Assessment" added to the label list; heuristic `θ=b/(b+1)` renamed from B to b (clash with the B-hypothesis) | rewritten |
| §§2–5 | forced classes, architecture, sieve-limit theorem, profiles | unchanged |
| §6 | "Dominant-prime families" (was "The three-quarter cap"); the main theorem moved out to §9 | retitled, pointer paragraph |
| §7 | "The quadratic-residue base and the capped measure" (was "Gapped moduli, unconditionally"): QR base, capped measure, leak, second moment kept as **tools**; Thm gapped / Thm resolved kept as **special cases** of Thm 4.5 | reframed |
| §8 NEW | weighted k-ary comparison (KARY §§1–3): coupled process, Lemma avoidance/inflation, locality, **binomial Lagrange extrapolation** (Lemma kextrap, bound (3.1) of KARY), thinned law via a **supermartingale** (Lemma kthin), Thm kcomp, Cor kmean, Remark weighted vs unweighted (counterexample; Conj 6.4 unweighted form OPEN) | new |
| §9 NEW | weighted sequential sieve limit (KARY Thm 4.1), sequential step, Lemma kmoments (= KARY 4.2(1)(3), 4.2′, 4.3), **Thm karycap (= KARY Thm 4.5)**, Thm main (architecture: case (i) dominant prime incl. Case A/(a,D); case (ii) all fixed-B ℛ(M)-families + W₀(B)-smooth classes, QR base) | new |
| §10 | campaign sieves | unchanged |
| §11 | Λ²: scope paragraph updated; Remark L2vsmain (under B the Λ² caps are superseded by Thm 4.5 since g² is a level-λ majorant — cites TWIN4 §11); new subsection: **rough-partner Brun–Titchmarsh from the arithmetic large sieve** (TWIN4 Lemma 2.3, full proof, cites Montgomery–Vaughan 1973 and van Lint–Richert 1965), Thm rprime (TWIN4 Thm 7.1), Prop 9.1 / Cor 9.3 in text, Thm noB (TWIN4 Thm 10.4); middle range r ≍ log L OPEN | extended |
| §12 NEW | non-CRT (NONCRT), **finite prime-slice families only**: Prop highlevel, Lemma walshfourier, Thm perfreq (w ≥ 1; no slice-prime size bound; explicit "not covered" list: Vaaler/ψ, floor/ceiling, exact |S_N|, smooth windows (CONDITIONAL on H_eq), dispersion over moduli); Thm primemaj (Dirichlet measure; primality sieve adds O((log log N)²)); Rem 3.4 kept as Assessment; moment methods (Props 4.1–4.2; prime moments of unbounded order only under the Assessment); direct interval counts (Thm 8.1 dichotomy, Lemma 8.2/Cor 8.3, Prop 8.4, withdrawn conjecture mentioned, Cor 8.7 CONDITIONAL on H_node, §8.3 EVIDENCE) | new |
| §13 | exclusions: item 4 rewritten (twins at fixed B now covered; remaining: log M/log P(M) unbounded, (a,D)/Case-A without dominant prime, mixed families; Λ² no-B at fixed r); items 1–3, 6 note partial coverage by §12; item 5 adds Thm 4.5; text after Lemma balancedsupply updated | rewritten |
| §14 | open problems: list (i)–(iv) rewritten; B-removal for general majorants listed as OPEN, TWIN4 §11 marked SKETCH, not claimed; Conj kary kept with note (weighted form proved, unweighted OPEN, not needed); Prop twinconditional kept, its conclusion now Thm 4.5; three-or-more-primes paragraph replaced by the Λ² middle-range and non-CRT open items | rewritten |
| bib | KA, KAr, KAr2, TW4, TW4r, NC, NCr, MV, vLR added | |

## Statements whose labels/hypotheses I checked against the sources
* Thm karycap: B fixed, ℛ(M) only, W = W₀(B), λ ≥ λ₀(B), plus W-smooth classes, base R_W, all primes > W charged. Constants untracked.
* Thm main (ii) combines with case (i) only as "either/or"; mixed families stated as not covered (DISCOVERIES (D)17).
* Thm perfreq carries "Case A proved mod ET Prop 1.4" inherited from Cor sliceCap (NONCRT itself labels Cor 2.5 PROVED via ET Lemma 3.7, which is the "mod" result).
* Remark L2vsmain is my observation (g² ≥ 0, level λ, ≥ 1 on avoiders in R_W ⇒ Thm 4.5 applies); it matches TWIN4 §11's "supersedes Thm 7.1 and Prop 9.1 under the B-hypothesis".
* No statement was strengthened; the old "residual open" claims are replaced by references to Thm 4.5 with its hypotheses.

## Points for the referee
1. §8 proof of Lemma kextrap gives only the node sets for (3.1), citing KARY §3 for the computation.
2. §9 Thm karycap proof cites ETw Prop 4.1 (singletons) and Lemma 4.2/Cor 4.3 (top block) rather than reproving.
3. §11 Thm rprime / Thm noB are proof sketches with precise citations.
4. §12 is a summary of NONCRT with short proofs for Lemma walshfourier and sketches elsewhere.

## Round 2: referee v2 (`side-agent/review-sieve-v2:reviews/sieve-limits-note-review-v2.md`) — all D-items applied

Recompiled clean (3 passes; no undefined refs, no overfull boxes, no warnings), 34 pages.

| item | fix |
|---|---|
| D1 finiteness | Thm karycap and Results item 1: "every *finite* family"; Lemma kmoments' family is finite, the W-smooth classes may be infinite (avoided by R_W, Lemma QR(1)), Q₀ built from the finitely many other moduli; Thm main proof: (A3)+B (resp. C) give M ≤ N^{A(1+B)}, finitely many classes |
| D2 non-family primes | Thm main proof: first average ν over the CRT coordinates of primes dividing no modulus and not Q₀ (A is a union of full fibres; mean unchanged; Σ|a_i| and level do not increase); then every charged prime is a family prime and (A3) applies. Covers both cases |
| D3 (eq:kB) | full computation printed in the proof of Lemma kextrap, cases (i) z ≤ d, (ii) z > d and zt ≤ 2d (disjoint), (iii) zt > 2d, using only Lemma binom |
| D4 notation | replaced set J(ω) → 𝒥(ω); Remark kweighted coordinates Z_1..Z_q, μ = q/4; K′ defined in the proof of Thm karycap (constant of TW Prop 4.1, = Lemma kmoments(2) on (W, e^{s₁}]) |
| D5 provenance | §1: "…or is assembled here from such results … (marked 'observation of this note')"; Remark L2vsmain labelled observation of this note, [proved], with the TW2 all-primes-charged link, TW4 §11 cited as "anticipated in"; Results item 1 restated with R_{W₀(B)}, λ ≥ λ₀(B), and the one-line link to the whole avoider set; O_B → O_{A,B} in abstract and item 1 |
| D6 | middle-range "carries most of the mass" labelled *Assessment* (TW4 §9.3), end of §11 and §14 |
| D7 | prime moments beyond A log N: Assessment of NC Rem 3.4 **plus** Σ_high|a_i| < π(N) and slice primes ≤ N^{O(1)} (NC Prop 4.1), in §12 and §13 item 3 |
| D8 | (a) "for all λ ≥ s_*, α > 0" in Thm perfreq; (b) Thm primemaj(1) assumes |F_ℓ(c)∖{0}| ≤ (ℓ−1)/4; (c) Cor 8.7's extra hypothesis m ≥ 16(log N)^{3/4+δ} stated, its support for the full family labelled evidence; (d) dichotomy rephrased as in NC §8.1 (holds at every λ; the range is where branch (D) is non-vacuous); (e) Prop 8.4 mean ≤ ¼(1+1/N)(1+log N)² |
| D9 | (a) "first version" → "the corresponding list in [ET, §6]"; (b) ϖ(x) = 0 case restored in Lemma kthin; (c) remark after Thm main: any admissible set R ⊇ R_{W₀(B)} (or none) is covered — observation of this note, [proved] |

Nothing anticipates the B-removal work of the kary-no-b agent: §14 still lists B-removal for general majorants as OPEN with TW4 §11 as an unchecked sketch.
