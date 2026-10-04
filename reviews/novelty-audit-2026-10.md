# Novelty audit of the campaign's "novelty unchecked" results (2026-10-04)

Scope: the four groups in the brief. This is a priority search, not a proof check.
Detailed notes are in `reviews/lit-audit-A-sieve-limits.md`, `-B-pointwise.md` and
`-C-exceptional-set.md`, and earlier in `reviews/theta-lit-notes.md`. Sources are
archived in `sources/lit2026/` (prefix `audit-`, listed in its README) or were
already in `sources/`. Page numbers are **PDF pages of the archived arXiv version**.

**Search limits.** The Jina search API returned HTTP 402, and Semantic Scholar
search was rate-limited. Searching used the arXiv API, OpenAlex, Semantic Scholar
citation lists, and the r.jina.ai reader for erdosproblems.com and Tao's blog.

The following were **not accessed** (metadata only, so there is no theorem-level
claim about them):
* Selberg, *Sieve methods* (PSPUM 20, 1971) and *Lectures on sieves*;
* *Opera de Cribro*;
* Prékopa 1988/1990 and Mádi-Nagy–Prékopa 2004;
* Linial–Nisan and Kahn–Linial–Samorodnitsky;
* Graham–Ringrose 1990;
* Schinzel 2000 and Yamamoto 1965;
* Vaughan 1970.

"New" below means **no prior source found in what was searched**. It is not a
certificate of priority.

## Headline

The main finding concerns item (1). The **exchangeable, single-level core of the
sieve-limit theorem is known**, in sharper form, in the probability/TCS literature
on k-wise independent bits:
* Benjamini–Gurel-Gurevich–Peled (BGP);
* Peled–Yadin–Yehudayoff (PYY), *Random Structures & Algorithms* 38 (2011)
  502–525;
* building on Prékopa's discrete-moment LP.

Neither the campaign nor `theta-lit-notes.md` cites this literature.

By LP duality, a level-k majorant sieve is the same thing as a lower bound on
`M(n,k,p)`. Here `M(n,k,p)` is the largest probability that all bits avoid, under
a k-wise independent law with the given marginals. PYY prove that Selberg's square
majorant is optimal up to a factor `e^{O(k)}`. The campaign obtained this only as
EVIDENCE (ET §2.5) or with a weaker constant (ET Lemma 2.2, KARY Lemma 2.3).

Apparently new are:
* the weighted lower-set (multi-band) extension with arbitrary biases;
* the Rankin-functional formulation;
* the sequential-law comparison;
* all Erdős–Straus applications.

Items (2)–(4) hold up as stated:
* No Ω-result for any least ES witness parameter was found.
* Theorem C is a procedural, H-conditional generalisation of known odd-square
  obstructions.
* As of 2026-10-04, no improvement of Vaughan's 2/3 exists in the searched
  literature.

## Table

| # | Campaign result | Verdict | Closest prior work (checked in source unless marked) | Notes |
|---|---|---|---|---|
| 1a | LP-duality reformulation: the best level-λ majorant mean equals the largest avoider mass over laws matching all level-λ marginals (implicit in ET §2, KARY) | **KNOWN** (standard) | Tao, *254A Notes 4: Some sieve theory* (blog, 21 Jan 2015), Theorem 5 "Dual sieve problem" (archived `audit-tao-254a-notes4-sieve-theory.md`). BGP arXiv:1201.3261 §3.1, Prop. 4 (p. 4): `max_{Q∈A(n,k,p)} Q(f=1) = min E_p P` over degree-≤k majorants. PYY arXiv:0801.0059v3 (2.5), p. 9. Selberg's LP view: not accessed | Standard. Cite it; do not present it as a contribution. |
| 1b | Exchangeable single band (ET §2.5; ET Lemma 2.2; KARY Lemma 2.3 "binomial extrapolation"): the LP optimum vs the Selberg/Christoffel value | **KNOWN, in sharper form** | **PYY Thm 1.1 (p. 5), Cor. 1.2–1.3 (pp. 5–6):** for even k ≤ c₁N with N = np(1−p)−1, `M(n,k,p) ≥ (c₃/k)·exp(−c₂k/V(N/k))·M̃`. **BGP Thm 23 (p. 10):** `M ≤ M̃ = pⁿ/P(Bin(n,1−p) ≤ k/2)`. PYY (3.3) (p. 11): M̃ is the optimum over squares (Markov–Lukács), i.e. the Selberg value. PYY Thm 2.2 (p. 10) quotes Prékopa 1988 Thm 9 on the shape of the optimal polynomial. Exact small-p and near-1 formulas: Berend–Ernst–Kontorovich–Kumar arXiv:2407.18688 | In the dictionary `p_PYY = 1−q`, PYY's (2.5) is literally ET's exchangeable LP `min E Q(K)` with `Q ≥ 1_{0}` and `K~Bin(n,q)`. KARY Lemma 2.3 is literally `M(n,d,t) ≥ 1/B(n,t,d)`. The campaign's bounds are weaker (exponent d vs d/2; constant 19) but cover all ranges, which PYY does not (k ≤ c₁N). **ET §2.5's "Selberg attains the LP optimum" EVIDENCE is a theorem in the binomial model: PYY Thm 1.1.** The Poisson model is the limit, which PYY do not state. |
| 1c | ET Prop 2.4 / Thm 2.5: weighted lower sets Λ={Σ j_g s_g ≤ λ}, arbitrary p_i ≤ 1/4, `log(1/Ef) ≤ 19αλ + C₄Σ p_i e^{−αs_i} + O(G log)`; the Rankin functional Ψ(λ) as a universal cap; CRT prime-slice form | **PARTIAL → apparently new as stated** | Ingredients are known: thinning plus symmetrisation (PYY §2, Lemma 2.1, after BGP), the single-band bound (1b), and the combination technique (Delvos 1982, per theta-lit-notes). GKM arXiv:1606.06781 Thms 1.3–1.4 (pp. 9–10) cover only Selberg-type weights; their Remark 1.4 leaves combinatorial weights open. Tao 254A Ex. 18: the fundamental-lemma error is best possible for κ=1. No multi-weight / non-identical-marginal version of `M(n,k,p)` was found. The closest literature is pairwise only (arXiv:2006.00516). Leads not accessed: Mádi-Nagy–Prékopa 2004 (multivariate discrete moment problem with total-order moments); Selberg's large-κ remarks; *Opera de Cribro* Ch. 7/11 | The new content is the multi-band synthesis, the uniform Rankin-functional cap for arbitrary densities, and the CRT reduction. The interpolation certificate is the same kind of argument as PYY's (quadrature/moment problem), so the method is not new. The open check is Mádi-Nagy–Prékopa 2004 (MOR 29:229–242), which needs library access. |
| 1d | ET Cor 3.4–3.6, KARY Thm 4.5, NONCRT, TWIN*: the 3/4 cap for every forced-class CRT majorant for ES | **NEW** (application) | No ES or Egyptian-fraction source discusses limits of sieve majorants. PW §4 and Vaughan use one sieve, and nobody remarks on optimality (audit C) | Novelty rests on 1c plus the ES supply profile. |
| 1e | KARY Thm 2.5: k-ary comparison of a sequential (dependent) law with a product law for d-local f, with random step costs | **Apparently new** | The closest work is k-wise-independence "fooling" (BGP §3) and the Haeupler–Saha–Srinivasan conditional LLL (campaign-cited). No matching statement found | Lemma 2.3 inside it is item 1b. |
| 2a | POINTWISE_OMEGA/2/3: `W(p) ≥ (log p)^k e^{−C_k log₂p/log₃p}` i.o., every k; `log L_h(T) ≤ T^{o(1)}` | **NEW** (as a statement) | No Ω-result for any least ES witness parameter: ET (Prop 1.6 p. 6 and Prop 1.9 p. 8 are vanishing/classification results), PW Thm 1.1 p. 2 (exceptions for **varying m**), Dahan Prop 3.8 / Thm 4.3 / Thm 4.14 (fixed-depth or blind-family counts, not least depth), Salez §3 (filters, no lower bound). The method is classical: a CRT residue choice plus a least prime in progressions. Same pattern as Fridlender/Salié/Chowla–Turán `n_p = Ω(log p)` (quoted in Lau–Wu p. 2, (1.7)) and Jacobsthal-type constructions | W is campaign-defined (`W(m²)=∞`), so the interest depends on W being natural. The multilevel minorant / LLL machinery is the technical novelty. |
| 2b | POINTWISE_OMEGA4: `log W ≥ (1+o(1)) log₂p·log₃p/log₄p` i.o. | **NEW** (as a statement) | Same as 2a | Modulo Thorner–Zaman and ET Prop 1.4. |
| 2c | POINTWISE_OMEGA Thm 8.5: `ck_min(p) ≫ log p·log₃p` i.o.; congruence methods certify exactly `n_p` | **PARTIAL: known in substance** | Graham–Ringrose 1990 (Progr. Math. 85, 269–309): `n_p = Ω(log p·log₃p)`, as stated in Lau–Wu p. 2 (archived; G–R itself not accessed). Lemma 8.1 `ck_min ≥ n_p` is the Yamamoto QR condition (BL Cor 1.3 p. 2, "unifies … Yamamoto"; ET p. 6) | The Ω-result is G–R transported by an elementary lemma, so cite G–R as the primary source. Only the "certify exactly n_p" equivalence (Prop 8.3 / Cor 8.4) is campaign content. |
| 3a | POINTWISE_SIZE Theorem M: formal run at a profinite point = actual run at admissible q | **Apparently new as a formal statement; folklore principle** | The generic-point principle under Hypothesis H is standard in its use (Colliot-Thélène–Sansuc style fibration arguments; not accessed). No ES paper states a procedure-level transfer | Present it as a formalisation, not a discovery. |
| 3b | Theorem C: under H, every correct bounded witness-producing procedure fails for infinitely many p≡1 (24) | **PARTIAL** (generalises known obstructions) | ET Prop 1.6 and the remark on p. 6: methods "must necessarily fail when p is replaced by an odd square … rules out … finite set of covering congruence strategies, or the circle method". ET p. 8: square classes are not solvable by polynomials (Mordell 1969, Schinzel 2000; not accessed directly). BL Cor 1.3–1.4 (p. 2). Dahan Prop 3.8 | The unconditional instances (notes Thms 5.1 / 17.3, "finite congruence coverings cannot settle ES") are **known** (Mordell/Schinzel via ET p. 8). The procedure-level, H-conditional form with factorisation steps is the new part. |
| 3c | DEPTH3 Thm 2 / Theorem F (seed component, H-conditional) | Unchanged: an instance of 3b | as 3b | (G)7 wording is already accurate. |
| 4 | `E(N) ≪ N exp(−c(log N)^{3/4})` (es-threequarter-note); 2/3·loglog note | **NEW as of 2026-10-04** (internally proved, not refereed) | Vaughan 1970 is still the record per ET p. 3 ("compare [48, 84, 39, 89] for some weaker results"), PW p. 2 ("strongly improved, though not recently: In 1970, Vaughan…") and PW Thm 1.3 (exponent 2/3 at fixed m), and erdosproblems #242 (page last edited 7 May 2026; forum's last post 13 Feb 2026). arXiv API, 2026-09-28 → 10-04: nothing relevant (2609.29250 Xu II, 2609.32140 #306, 2610.00946 Engel/Pierce are irrelevant). No source states the B/(B+1) heuristic, the cubic forced-class mass or the 3-denominator multiplier identity | The cubic average solution count is ET Thm 1.1 (pp. 3–4) and Remark 1.2's Poisson heuristic. That is the same scale, but a different statistic. Vaughan's primary text was not accessed. |

## Recommended wording changes

1. **`paper/sieve-limits-note.tex`, lines 104–106.** Replace "No prior source … folklore in spirit. Novelty is not claimed" with an explicit attribution:
   * The LP duality and the exchangeable single-level case are known: BGP Prop. 4 and Thm 23; PYY Thm 1.1, which builds on Prékopa 1988.
   * The weighted lower-set / arbitrary-density extension (Thm `thm:slice`) and the ES applications are, to our knowledge, new.
   * Add bib entries for PYY, BGP and Prékopa, plus Tao's 254A Notes 4 Thm 5 for the dual sieve problem.
2. **`sieve-limits-note.tex` lines 1120–1124 and `EXCEPTIONAL_THETA.md` §2.5.** "That Selberg … attain the same order … is only evidence" should become: in the exchangeable **binomial** model this is a theorem, since by PYY Thm 1.1 / Cor 1.3 the LP optimum is within `e^{O(k)}` of the Selberg (square) value. Keep EVIDENCE only for the Poisson model and the multi-band case.
3. **`EXCEPTIONAL_KARY.md` Lemma 2.3.** Add: "equivalently `M(n,d,t) ≥ 1/B`, in the notation of BGP/PYY; PYY Thm 1.1 gives the sharp order for d ≤ c·nt; our crude bound covers all ranges".
4. **`DISCOVERIES.md` (D)9.** Replace "no prior source found, `reviews/theta-lit-notes.md`" with "single-band exchangeable core known (PYY 2011, BGP; see `reviews/novelty-audit-2026-10.md`); weighted / Rankin-functional form and ES cap apparently new". Add the same note to (D)17 for KARY Thm 2.5 / Lemma 2.3.
5. **`DISCOVERIES.md` (H)9 and `POINTWISE_OMEGA.md` Thm 8.5.** Cite Graham–Ringrose 1990 as the source of `Ω(log p·log₃p)` (Lau–Wu Prop 5.1 is a later refinement). Say that the Ω-bound is G–R transported via the Yamamoto-type Lemma 8.1, and that only the "certifies exactly n_p" equivalence is campaign content.
6. **`DISCOVERIES.md` (H)1 and (H)3.** Add "Theorem M is a formalisation of the standard generic-point / Hypothesis-H principle; Theorem C generalises ET Prop 1.6 / p. 6 remark and Mordell–Schinzel (ET p. 8) to procedures; its unconditional instances (notes Thms 5.1, 17.3, (C)7) are known in substance". In (C)2 and (C)7, add "cf. Mordell 1969, Schinzel 2000 via ET p. 8".
7. **`DISCOVERIES.md` (H)8, (H)11, (H)13, (H)14 and the es-omega-note intro.** Optionally add: "no prior Ω-result for a least ES witness parameter found (audit 2026-10); method in the Fridlender–Salié / least-prime CRT tradition".
8. **Maintainer item "2/3 loglog after external priority audit".** It can be ticked for the searched sources: no improvement of Vaughan's 2/3, or of its loglog factor, was found up to 2026-10-04. The remaining gap is that Vaughan's primary text and the Chinese literature were not accessed.

## Open checks (need library access)

* Mádi-Nagy & Prékopa, MOR 29 (2004) 229–242, and Prékopa, DAM 27 (1990): do they contain the multivariate lower-set version of 1c?
* Selberg, *Lectures on sieves* (Collected Papers II): large-κ optimality of Λ².
* *Opera de Cribro* Ch. 7 and 11.
* Kahn–Linial–Samorodnitsky 1996.
* Graham–Ringrose 1990, to confirm the exact theorem.
