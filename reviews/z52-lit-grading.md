# z52 lane G — grading of the seven z52 literature dossiers (2026-10-30)

ES is OPEN. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Internal campaign results are internally reviewed only.

## Summary
(TODO)

## 1. Citation audit

**Method.** Re-opened on 2026-10-30 the arXiv API records (`https://export.arxiv.org/api/query?id_list=…`) of 118
arXiv items cited by the seven dossiers: 80 in the first batch (every "new since 2026-09-28" item, every item a
verdict depends on, and the tracked ES preprints) and 38 more in a random/spot batch. Records:
`sources/z52/grade_lit/api_records.txt`, `api_records2.txt` (script `scripts/z52_gradelit_arxiv.py`). I opened PDFs
for the nine decisive ones (Shkredov v2, Zhang v2, Li–Liu, Alkauskas v3, Hashimoto v2, KST, LLS, FKK, Carella v9);
excerpts are in `sources/z52/grade_lit/pdf_excerpts.txt`. I checked Crossref for DOI 10.1090/bull/1874 and for the
Chen Annals paper (`crossref_bull1874.txt`). All 118 ids resolve; **no item is hallucinated.** Authors, titles and
abstracts match the dossiers except for the items flagged below.

### 1.1 "New since 2026-09-28": what really is (cutoff = arXiv v1 or a substantive revision on/after 2026-09-28)

| Item (lane) | API record | Verdict |
|---|---|---|
| Cao–Xu 2610.32302 (L1) | v1 2026-10-23; abstract says the cover is supported by a "numeric test" only | **NEW, correct.** The lane quotes §3 ("we failed to get a logic proof"); I did not re-open the HTML, but the abstract agrees |
| Filaseta–Kalogirou–Klein 2610.34541 (L2) | v1 2026-10-25; Σ1/m ≥ 1+10⁻²⁸ when the least modulus is a prime q ≥ 11; no covering uses distinct multiples of q | **NEW, correct** |
| Li–Liu 2610.15784 (L5) | v1 2026-10-11; Thm 1.1 (≤ 6 powers, unconditional), Thm 1.2 (≤ 5 under GRH), two primes | **NEW, correct.** One flag: L5 says this "improves K = 8" (Pintz–Ruzsa 2020). Li–Liu's own intro and Table 1 give Johnston–Trudgian (2026) with 7 unconditional and 6 under GRH as the previous record. Thm 1.1 proves r₆″(N) ≥ N L⁶/1000 with L ≍ log N, a power-size count |
| Kadyrov–Kazin–Orynbassar–Shynarbek 2610.16530 (L3) | v1 2026-10-12 | NEW, but already cited in `QUESTION_R.md` §5 (2026-10-18). Not relevant |
| Korsky 2607.04157v2 (L2) | v1 2026-07-05, v2 2026-10-08 | Revision only; already in `LITERATURE_2026.md` |
| Ventas 2605.04551 (L1) | **v3**, updated 2026-10-15 (L1 says "v1, updated 2026-10-15") | Version mislabelled; heuristic paper, already in the repo |
| Parrochia 2609.22388v2 (L3) | v2 2026-09-30 | Revision; not relevant |
| R. Zhang 2503.08800v4 (L4) | v4 updated 2026-09-28T23:56Z | **Borderline** (revised on the cutoff day; v1 is from 2025). L4 contradicts itself: §0 says "none new", while the entry says "genuinely new in the window" |
| Li 2609.32140 (L1) | v1 **2026-09-26**, two days *before* the cutoff | L1 labels it correctly as from a wider 2026-09-01 sweep. It is new *to the campaign's verdicts* (only `reviews/lit-audit-C…` mentions it). Missed nuance: the abstract says **Tang's Lean development "gave the first proof"** of #306, and Li's construction removes Tang's anchor-synchronisation step. So Li's is the second proof, not the first |
| Klurman–Shparlinski–Teräväinen 2609.25393 (L6) | v1 **2026-09-21** | **Mis-dated by L6** ("genuinely new since 2026-09-28"). It is new to the campaign (no `git grep` hit) but predates the cutoff. The statement matches Thm 1.1 verbatim |
| Hashimoto 2603.26043v2 (L2) | v1 2026-03-27, v2 **2026-09-25** | **Mis-dated by L2** (predates the cutoff); new to the campaign. The abstract adds "namely the largest modulus" for the repeated one. L2 omits this, harmlessly: by Mirsky–Newman–Davenport–Rado the largest modulus of a disjoint covering system is always repeated |
| Shkredov 2603.14116v2 / X. Zhang 2605.02518v2 (L3) | v2s dated 2026-06-24 and 2026-05-08 | **Mis-scoped by L3** ("genuinely new since 2026-09-28"). The all-q claim is *already* recorded in `LITERATURE_2026.md:721`, `DISCOVERIES.md:1614`, `FRONTIER.md:375` and `BRAINSTORM/z31_zaremba_thin_orbits.md`. The PDF details L3 adds are accurate: Shkredov Thm 8 (∀q, ≥ q^{2w_M−1−o(1)} numerators with digits ≤ 100M; the method itself proves only q^{1−O(1/M)}) and Remark 9 ("we now possess a proof of Zaremba's conjecture in full generality", via Zhang–Tang expansion). Zhang Thm 1.2: "Zaremba's conjecture holds", with M large but absolute and effectively computable (Remark 1.3). They add precision, not news |
| Sothanaphan 2601.07421v5 (L7) | v5 updated **2026-01-26** (v1 2026-01-12) | **Wrong "new since 2026-09-28" claim by L7.** The statement (Thm 1, Kummer carries plus a counting argument, and the Erdős/Pomerance similarity) matches the abstract. It is new to the campaign only |

Net: since the cutoff, **four** genuinely new arXiv items bear on the campaign at all: Cao–Xu, FKK, Li–Liu and
Kadyrov et al. (the last already cited). **None touches ES status.** Li #306, KST, Hashimoto, Alkauskas and #728 are
new *to the repository* (no earlier `git grep` hit, except Li in one audit), not new in time.

### 1.2 Mis-attributions and errors found

1. **Chen (L3 §1.4): wrong title.** L3 cites W. Y. Chen, "A proof of the Markoff conjecture", arXiv:2011.12940. The
   real arXiv/Annals title is **"Nonabelian level structures, Nielsen equivalence, and Markoff triples"**, *Ann. of
   Math.* 199 (2024), DOI 10.4007/annals.2024.199.1.5 (Crossref; arXiv v2 2021-06-19). The invented title is
   misleading: the classical *Markoff uniqueness conjecture* is still open. Chen proves the divisibility-by-p theorem,
   which with BGS gives connectivity of the Markoff graph mod p for all large p. The content L3 states is right;
   only the title is fabricated.
2. **HKRS authors (L3):** "J. Haag, A. Kertzer". The arXiv record has **Summer Haag, Clyde Kertzer**, J. Rickards,
   K. E. Stange.
3. **Kingsbury-Neuschotz (L3):** the title is "Strong Approximation for the **Relative** Character Variety of the
   Four-Times Punctured Sphere". The density-one-primes statement is correct.
4. **Ma–Yang–Yang 2608.07880 (L3):** the current version is v2 (2026-09-03), not v1. **Chaubey–Ray 2609.12177 (L3):**
   cited as "A. Ray" alone; the first author is Sneha Chaubey.
5. **L4:** arXiv:2204.13472 is cited without an author (it is **H. Uppal**). L4 §7 lists Gvirtz-Chen–Mezzedimi as "NOT
   VERIFIED" while §4 records it as verified from full HTML. This is an internal inconsistency: the API record
   matches §4.
6. **Repo error surfaced (not a lane error):** `QUESTION_R.md` §5 attributes the *Bull. AMS* 63 (2026) survey "the
   rise and fall of the local-to-global conjecture" to **Kontorovich**. Crossref has **Elena Fuchs**, "Apollonian
   packings: The rise and fall of the local to global conjecture", *Bull. AMS* 63(1) (2026) 59–77, DOI
   10.1090/bull/1874 (online 2025-10-15). L3 has this right. Fix to apply in `QUESTION_R.md`.
7. **Carella 2106.00544v9 (L6): gap claim confirmed.** In (7.6) the sum over 1 ≤ v < p/x is replaced by one over
   1 ≤ v < p while the text still asserts "uv < p" and uses 1/|sin πuv/p| ≪ p/(uv). That bound fails for uv ≥ p,
   and nothing bounds the added terms. Independent red flag (Assessment): the claimed unconditional
   n(p) ≪ log p (log log p)^{1+ε} would beat the GRH bound (log p)² (LLS Cor 1.1, checked) and nearly reach
   Montgomery's GRH lower bound Ω(log p log log p). L6's "unusable" verdict stands.
8. **L5 Linnik history:** "improves K = 8" omits Johnston–Trudgian 2026 (7, or 6 under GRH), per Li–Liu Table 1.
   L5's flag that the brief's "one prime + powers of 2" phrasing is wrong is **correct**: every source has two
   primes.

### 1.3 Random spot-checks (beyond the verdict items), all OK

These 21 entries match in authors, title, version/date and abstract-level statement. Unit fractions and coverings:
Bloom 2112.03726v2; Liu–Sawhney 2404.07113v1; Conlon et al. 2404.16016v2 (*Discrete Analysis* 2025:28); Sawin
2607.15419v1; Kovač–Tang 2607.28387v2; van Doorn–Tang 2512.22083v2 (v(k) ≥ e^{ck²}); Hough 1307.0874v3 (abstract
bound 10¹⁸, as L2 notes); Harrington–Klein–Lowrance–Trifonov 2605.18644 (m ≤ 9; m = 8 example). Primes and
pointwise problems: Heath-Brown–Puchta math/0201299v2 (13; 7 under GRH); Ding–Li–Li 2607.03662v1; Green–Sawhney
2410.04189v3. Divisors, characters and groups: Pilatte 2404.16450v3 (*Forum Math. Pi* 14 (2026) e5); LLS 1309.3595
(Cor 1.1 "below (log q)²", read in the PDF). Geometry and thin orbits: Kingsbury-Neuschotz 2603.04096v3;
Alkauskas 2508.05347v3 (Thm 2 read in the PDF); Shi–Shi–Whitehead–Williams-Tracy–Zhang 2510.21702v2; Bright–Loughran
1908.02526v2. ES computations and preprints: Mihnea–Dumitru 2509.00128v1; Salez 1406.6307v1; Jiang 2609.09204v2;
Dahan 2608.24035v1. A further ~70 records match at the metadata level (see the two API files). **Not re-checked by
me:** non-arXiv items (Lenstra 1984, Bernstein 2008, Heath-Brown 2001, Heule–Scheucher 2024, Bourgain IHÉS 1989,
Pintz–Ruzsa 2020, the erdosproblems.com pages, ProofAtlas); I treat them at the lanes' stated access level.

## 2. Verdict grading

Key: AGREE / PARTIAL / DISAGREE with the lane's transfer verdict. "§4.k" is FRONTIER §4 checklist line k; B1–B6 as
in FRONTIER §3. Overall calibration: no lane over-scopes a barrier the way the README "calibrated verdict" note
describes. They consistently write "known-dead *as a direct transfer*" or "at current hypotheses", which is the right
scope. The errors run the other way: two cases of **under-scoped enthusiasm** (L1 §3, L5 §3 "next test") and one
**missed repository fact** (L5 on p + 2^a + 2^b).

### L1 es_direct
| Row / candidate | Lane verdict | Grade | Reason |
|---|---|---|---|
| Cao–Xu composite-n test | none | AGREE | A primality criterion by divisor residues mod 24 is congruence plus factorisation shape (§4.8) |
| Cao–Xu 56-family cover | none; unproved | AGREE, *sharper* | A finite menu of polynomial families falls under B1 Thm C. CONDITIONAL on Hypothesis H, any such correct bounded procedure fails for infinitely many p ≡ 1 (24). So the cover is not merely unproved but **conditionally false** (Assessment: I did not check that every family is polynomial in m. The abstract calls them "solvability polynomials") |
| Li #306 (semiprime unit fractions) | partial; "new candidate for experiments" | PARTIAL | The structural reading is right. The mechanism is abundance: a Fourier count over ~2^{#edges} subgraphs with a positive main term, plus "small total mass forces equality". ES has three terms and a ≍ log²p count. That is exactly §4.6 (B3) and the free-term-count relaxation of §4.12. The "experiments" label is too generous |
| 19 recently-updated tagged problems | no/partial each | AGREE | Colouring, density, many-term or metric inputs (B6, §4.5–6). L1 rightly separates database `last_update` from proof dates |
| §3 cand. 1 (switches from #283 down to 3 terms) | speculative candidate | DISAGREE (not a candidate) | Reaching exactly three distinct denominators *is* ES. Sum-preserving switches do not control the term count. This is §4.12 (relaxation then transport, with no transport theorem), and no step fails at odd squares (§4.1) |
| §3 cand. 2 (3-edge semiprime Fourier count) | weak candidate | DISAGREE (not a candidate) | The 3-edge count for 4/p is a sub-slice of (★) with extra constraints. Its Fourier expansion at one p has no averaged variable to exploit and lands on B2 (§4.4). The lane half-concedes this ("may fail at the outset") |

### L2 unitfrac_cover
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| Bloom; Liu–Sawhney | known-dead | AGREE | They need a large, freely chosen denominator pool (B6, §4.5–6). See `addcomb_unit_fraction_density.md` |
| Conlon et al. counts | known-dead | AGREE | Exponentially many long representations say nothing about the 3-term count (B3) |
| Bloom, shifted-prime denominators | partial at most | AGREE | Denominators are freely chosen and the term count is unbounded. ES needs divisors of a p-tied integer (B2) |
| Sawin; Korsky; Kovač–Tang | none | AGREE | Avoidance, approximation and greedy dynamics are not exact 3-term existence (B3) |
| BBMST distortion; Hough | partial; known-dead pointwise | AGREE (scope) | Pointwise *in each finite system*. ES's obstruction systems are p-dependent, and B1 already kills fixed finite menus. `covering_distortion_dual.md` stands |
| Filaseta–Kalogirou–Klein | none | AGREE | A finite-system reciprocal-mass bound; no p-indexed event |
| Deterministic subset-product / zero-sum | partial; known-dead at current hypotheses | AGREE | Quantitative reason the lane leaves implicit: a divisor box from ω(x) ≈ log log x prime factors has ≤ τ(x)² elements. Olson-type completeness needs > 2√q *distinct* generators. The scale fails (§4.17, B4) |
| §3 "none" | — | AGREE | |

### L3 localglobal_thin
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| Apollonian missed families (HKRS) | partial; known-dead as positive route | AGREE | T1 is a reciprocity obstruction of the same class (`z36_reciprocity_obstruction_home.md`). But ES has no infinite Vieta/tangency orbit to carry an invariant: the fixed-n equation is linear in each variable (`apollonian_reciprocity.md`) |
| Zaremba (BK almost-all; Shkredov/Zhang all-q claims) | partial/no; known-dead at present scale | AGREE | The count is a power q^{2w_M−1}, against ES₅'s ≍ log²n (B3, §4.6). ES₅ matrices are also *self-levelled*: the modulus is the entry c (B2; `QUESTION_R.md` Prop 1.1) |
| Markoff mod-p connectivity (Chen + BGS) | no; known-dead | AGREE | Connectivity of a ≍ p² fibre using a giant component. Not a varying-target existence statement (B6/B3) |
| Markoff integral Hasse principle (Ghosh–Sarnak) | no | AGREE | Almost-all in the parameter, with infinitely many failures: an anti-precedent |
| §9 thin-regime audit: RS Thm 2.6/2.8 as "near-example" | near-example | AGREE | The decisive feature is *fatness*: numerators fill an arithmetic progression of length ≍ n/(8xy) on a line, and Pólya–Vinogradov finishes. ES₅'s numerator set has size ≍ log²n (B3; `QUESTION_R.md` table §2) |
| §3 "none" | — | AGREE | One omission, taken up in my §3: Alkauskas's flea orbit is a new thin data point with "squares + finitely many sporadic", the same *shape* as U(n) |

### L4 points_automorphic
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| Bright–Loughran | partial; known-dead standalone | AGREE | §4.13: BM-set nonemptiness is not existence, and "BM is the only obstruction" is ES itself |
| Linowitz–Thompson | none | AGREE | A uniqueness theorem from signs on a positive-density set of primes; nothing about one coefficient (B6) |
| Harpaz; Wilsch; Santens; Loughran–Mitankin; Lyczak; R. Zhang; Chambert-Loir–Tschinkel; Cao–Xu/Wei; Derenthal–Wilsch; Uppal | relation notes only | AGREE | These are fixed-variety height asymptotics, conditional fibration theorems, or BM-obstruction constructions. The ES model is non-toric, and U_n has finitely many positive integral points |
| §6 automorphic positivity | no ES encoding | AGREE | Careful and correct: R(n) is not a coefficient of a fixed theta series with a positive local-density main term (FRONTIER §2.3, Thm K) |
| §3 "none" | — | AGREE | |

### L5 thin_pointwise
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| F–I, Heath-Brown, HB–Moroz, Maynard, Pratt, Green–Sawhney, Merikoski (×2) | no; family-level | AGREE | Infinitude over a family, with no prescribed target (B6) |
| HBP / Pintz–Ruzsa / Li–Liu (two primes + K powers of 2) | no; power-size reservoir | AGREE | Li–Liu Thm 1.1 proves r₆″(N) ≥ N L⁶/1000 from the Goldbach main term (§4.6) |
| Romanoff / Erdős AP (p + 2^k) | failure analogy (B1) | AGREE | The O(1)-witness problem fails on an AP via a covering. ES failures cannot form an AP: any AP of odd n coprime to its modulus contains n with a prime factor ≡ 3 (mod 4), and those satisfy ES classically |
| p + 2^a + 2^b (≍ log n witnesses) | "no every-n or almost-all theorem or covering failure verified" | **DISAGREE (missed fact)** | Already in the repository (`BRAINSTORM/s9_lower_tail_literature.md`, R282-checked). Crocker, *Pacific J. Math.* 36 (1971) 103–107, Thm I (re-opened by me, excerpt `sources/z52/grade_lit/crocker1971_excerpt.txt`): infinitely many odd n are not p + 2^a + 2^b. The mechanism is the Fermat-number factorisation of 2^{2^n} − 1 (Lemma I: 2^{2^n} − 1 − 2^a − 2^b is divisible by some 2^{2^r} + 1) combined with a covering. Pan 2011 (per repo) gives ≫ x^{1−ε} exceptions. So the *natural* ≍ log n model **fails**, on a structured family. That is the opposite of L5's "intermediate model, no failure known" |
| Four/three squares, triangular, ternary forms, 290, Blomer | no | AGREE | Universality without a uniform witness-count floor. The lane rightly notes r₃(4^a) = 6 |
| Least prime in AP; Burgess | partial analogy | AGREE | Fixed modulus (§4.4) |
| §3 "concrete next test": a second-moment bound for the fixed-p divisor count "with the modulus held fixed first" | exploratory test | DISAGREE | Romanoff's second moment averages over targets (B6). Holding the modulus fixed removes exactly the tied modulus that B2 is about (§4.4), so the test cannot inform ES |

### L6 divisor_class
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| Lenstra / CHGN / Hales / Bernstein | known-dead (existence) | AGREE | Upper bounds and enumeration only. They never force a hit (B2) |
| Ford H(x,y,2y); Koukoulopoulos | known-dead | AGREE | Population counts (B6) |
| Munsch; Harman–Shparlinski | partial; known-dead direct | AGREE | Freely chosen small representatives. ES's generators are the prime factors of a p-tied integer (§4.17) |
| Least QNR; Carella | partial; Carella unusable | AGREE | Gap confirmed (§1.2 item 7) |
| LLS coset theorem (GRH) | partial; known-dead direct | AGREE | It delivers the *class*, not just the parity (§4.9), but for freely chosen primes, not divisors of one N (B2) |
| KST; Pilatte | no; known-dead direct | AGREE | Strengthened by KST §1.2 itself: dropping the almost-all exceptional set, even to a better-than-super-polylog saving, would require Vinogradov's least-QNR conjecture. The pointwise version holds under GRH by orthogonality, for *free* primes ≤ (log q)^B, B > 4 |
| §3 "none" | — | AGREE | |

### L7 nonant
| Row | Lane verdict | Grade | Reason |
|---|---|---|---|
| SAT landmarks (Schur 5, Keller 7, Pythagorean triples, h(6), R(3,8/9)) | known-dead as template | AGREE | Finite encodings. An ES-to-finite reduction would be a covering/identity menu (B1, §4.8) |
| #728 (Kummer carries + counting) | partial; known-dead as stated | AGREE | m is chosen from an interval of candidates (B6, §4.5) |
| Automata (palindromes) | not a transfer; undecided | AGREE | Correctly refuses an unexhibited Walnut encoding |
| Dynamics / Duke / effective unipotent | no | AGREE | Averages over growing orbits (B6) |
| O-minimal counting | conditional only | AGREE | The volume main term needs thickening, which averages over neighbouring n (B3) |
| Hough + LLL | no | AGREE | Positive uncovered density per finite system. Wrong direction and wrong target |
| §3 "none" | — | AGREE | |

## 3. Cross-lane synthesis: what the z52 literature says about ES itself

**Bottom line (Assessment).** The seven dossiers contain **no** result that changes the ES map. Every result that is
solved and pointwise has one of these features: (i) a power-size witness reservoir (Goldbach pairs, q^{2w_M−1}
Zaremba numerators, ≍ p² Markoff fibres, Apollonian X^{0.3} multiplicity); (ii) an arithmetic progression of length
≍ n inside the fibre (Rickards–Stange's fat case); (iii) free choice of the witnesses (unit-fraction denominators,
small primes for subset products); or (iv) averaging (almost all q, density one, an interval of m). ES at one prime
has none of the four: its count is ≍ log²p, its witnesses are divisors of p-tied integers (B2), and p is fixed (B6).
That sentence already describes `FRONTIER.md` §§3–4. The findings below are the items where z52 adds a fact, a
calibration or a correction.

**F1. Zaremba is now claimed in full (CLAIMED, unrefereed; not new to the repository).**
* *Sources.* Zhang 2605.02518v2 Thm 1.2 ("Zaremba's conjecture holds"; M absolute, large, effective). Shkredov
  2603.14116v2 Thm 8 (∀q, ≥ q^{2w_M−1−o(1)} numerators with digits ≤ 100M) and Remark 9 (full generality via
  Zhang–Tang general-modulus expansion). Both already in `LITERATURE_2026.md:721`.
* *What made it solvable.* Expansion and gluing in SL₂(ℤ/q) on Cantor-type digit sets, with a count that can be
  **tuned** to near q¹ by enlarging the alphabet. The method itself certifies q^{1−O(1/M)} numerators, so the count
  is power-size.
* *Does ES share it?* **No.** ES₅'s word length is fixed at 3, so its count ≍ log²n cannot be tuned (B3). Its
  matrices are self-levelled, with the congruence modulus equal to the entry c (B2; `QUESTION_R.md` Prop 1.1). And
  expansion holds at n = m² too, so it cannot see T1 (`QUESTION_R.md` Prop 2.2).
* *First problem.* None new. Question R / Hypothesis TG (`QUESTION_R.md` §2) remains the hinge, and Zhang's
  expansion does not touch TG.

**F2. "Squares + finitely many sporadic": four instances. Is ES₅/U(n) literally one of them?**

| Instance | Obstructed set | Sporadic set | Status | Fibre size |
|---|---|---|---|---|
| Rickards–Stange Thm 2.8, Ψ-orbit of 2/3 (Duke 2025) | squares | 15 explicit values | **PROVED** (effective cofinite) | fat: an arithmetic progression of length ≍ n/(8xy) on each line; Pólya–Vinogradov finishes |
| HKRS Apollonian packings (Annals 2024) | u·m², u·m⁴ families | finite? (Conj 1.5) | OPEN; Bourgain–Kontorovich density one | power, ≍ N^{δ−1}, δ ≈ 1.31 |
| Alkauskas flea areas, 2508.05347v3 (2026-09-09) | squares (Thm 2(ii), PROVED via an HKRS-type character) | {5, 29, 80, 99, 179} up to 10¹² (CERTIFIED); completeness "still unproved" | OPEN | power; see below |
| U(n), n ≡ 1 (4) (campaign) | odd squares (T1, PROVED) | {105, 2961, 3985, 25305, 111969, 978145} up to 10⁹ (CERTIFIED) | CONJECTURE | ≍ log² n |

* *Literal instance? No, for three exact reasons.*
  * (a) Both RS and HKRS sets are orbits of a finitely generated semigroup or group. The sign is carried along the
    orbit by a homomorphism (RS: σ on Γ₁(4)_{≥0}, the theta multiplier; `QUESTION_R.md` Thm 1.5). ES₅/U(n)
    certificates are self-levelled matrices [[A, n], [t, A*]] with A ≡ A* ≡ −1 (mod t) (`QUESTION_R.md` Prop 1.1),
    and the slice numerator sets meet RS Def 2.4 but are not semigroup orbits (R276).
  * (b) Elementary sharpening (PROVED, two lines): the (A)3 certificate matrices have 4 | c and a ≡ d ≡ 3 (mod 4)
    (`QUESTION_R.md` Prop 1.4). Any product of two such matrices has a ≡ d ≡ 1 (mod 4) and 4 | c (since
    a₁a₂ + b₁c₂ ≡ 9 and c₁b₂ + d₁d₂ ≡ 9 mod 4), i.e. it lies in Γ₁(4)_{≥0}, where RS's unflipped law (a/b) = (c/d)
    holds. So no nontrivial semigroup has all its elements in the certificate coset. An orbit model would have to
    alternate cosets, and −I, which repairs the coset, leaves the positive cone. This is the "place at infinity" of
    `QUESTION_R.md` Thm 1.5 again.
  * (c) Scale: fat ≍ n, Question R ≍ n^{2δ−1}, U(n) ≍ log²n.
  HKRS's revised conjecture (admissible, non-obstructed values occur with finitely many exceptions) is OPEN for
  every packing type. It is proved only in RS's fat case. Nothing in 2024–26 proves it for a thin orbit, which agrees
  with `QUESTION_R.md` §5. The Shi–Shi–Whitehead–Williams-Tracy–Zhang and Alkauskas papers add obstructions, not
  local-global theorems.
* *What made RS Thm 2.8 solvable.* Fatness: lines inside the orbit turn the reciprocity question into a character
  sum over an interval. Alkauskas's *proved* half (every half-integer area) comes from the same feature: the linear
  family s(U^t G) = 1 + 2t. In every known instance, the obstructed part is proved only when the fibre contains an
  arithmetic progression of length ≍ n. **ES does not share this** (B3).
* *New calibration (EVIDENCE, my computation).*
  * `scripts/z52_gradelit_fleas.py` (geometric simulation of outward-square jumps from G and its three
    negative-jump neighbours) reproduces Alkauskas's sporadic list {5, 29, 80, 99, 179} and finds no square area up
    to doubled area 10⁶.
  * The orbit has 1.03·10⁸ nodes against 0.999·10⁶ attained values, so the average multiplicity is 102.9. This
    multiplicity grows by ×2.1 per decade, ≈ X^{0.32}, which matches the Apollonian exponent δ − 1 ≈ 0.31 (the flea
    states lie in a Descartes-quadruple orbit, Alkauskas eq. (8)). Data: `data/z52_gradelit/fleas_counts.txt`.
  * So the flea problem is a power-count model, like RS and HKRS, and **not** a polylog model of U(n).
  * By-product (`fleas_nearsq*.txt`): after normalising by A mod 9240, areas A = m² + K show deficits of 5–7 %
    (each ≈ 5–7σ) at K ∈ {±1, ±4, 9, 16, 25} and excesses at K ∈ {±3, 2, 6, 8}. That mirrors the near-square deficits
    of the ES five-slice count (`QUESTION_R.md` §3.2) at K = 1, 4, 16, 25 and the non-deficit at K = −3, but not at
    K = 8 (deficit for ES, excess here). This is crude, since densities at primes > 11 are not normalised. It suggests,
    as Assessment only, that near-square deficits are generic to reciprocity-obstructed sets rather than specific to
    ES.
* *First problem.* None at the ES scale. The only polylog member of the table is U(n) itself.

**F3. The natural "prime + powers of 2" ladder (Li–Liu 2610.15784, NEW; Crocker 1971 and Pan 2011, already in the repository).**
* *Sources.* Two primes + K powers: K = 6 unconditional, K = 5 under GRH (Li–Liu Thms 1.1–1.2; the previous record
  was Johnston–Trudgian 2026, K = 7/6). One prime + one power: fails on an arithmetic progression (Erdős 1950
  covering). One prime + two powers, with ≍ log n expected witnesses: **fails infinitely often** (Crocker Thm I, via
  the Fermat factorisation of 2^{2^n} − 1), and ≫ x^{1−ε} times by Pan 2011 (per `s9_lower_tail_literature.md`).
* *What made the top rung solvable.* The Goldbach pair main term N/log²N, a power, carried by the circle method.
* *Does ES share it?* **No.** ES's ≍ log²p sits at the rung where every *natural* example has an infinite structured
  exceptional set. That is the existing lesson of `s9_lower_tail_literature.md`, and L5 missed it.
* *One structural difference (PROVED, elementary).* ES failures cannot contain an arithmetic progression of n
  coprime to its modulus. Such a progression contains qr with q, r ≡ 3 (mod 4) primes, and ES(qr) follows from
  ES(q). So the Erdős mechanism is excluded for ES; the Crocker and reciprocity (T1) mechanisms act on structured
  composite n.
* *First problem.* None new.

**F4. Subset-product generation (Klurman–Shparlinski–Teräväinen 2609.25393, new to the repository; Pilatte 2404.16450v3; LLS).**
* *What made it solvable.* Freely and randomly chosen small primes, plus character-sum control *on average over q*.
* *Does ES share it?* **No.** In gate G4 (`EXSET_CHAR_FORCING.md` §2) the generators are the prime factors of
  x = (p + q)/4, so there are only ω(x) of them and they are tied to p (B2, §4.17). KST §1.2 adds a calibration: even
  for *free* primes, removing the almost-all restriction requires Vinogradov's least-QNR conjecture, while the
  GRH pointwise version is easy (orthogonality). In ES the QNR layer is supplied by forcing ((q/p) = −1). What
  remains open is the *class* layer (the target −1 itself), which is §4.9's "class, not parity". No literature
  item touches it.
* *First problem.* None.

**F5. Li's #306 and the 2025–26 AI/Lean crop (#283, #306, #728, #729, #401, #90).**
* *What made them solvable.* Abundance: Fourier counts over exponentially many configurations (#306, building on
  Tang's earlier Lean proof), counting a good m inside an interval (#728, #729, #401), random or algebraic
  constructions (#38, #90), or complete-sequence switching with unbounded term count (#283).
* *Does ES share it?* **No.** None of these problems has ES's quantifier shape ("every n, with a polylog witness
  count").
* *Calibration (Assessment).* The current AI+Lean pipelines resolve exactly the problem types that the campaign's
  barriers say are reachable (B6, §4.12). No 2025–26 AI-assisted result breaks that pattern.
* *First problem.* None. L1's two "candidates" do not survive (§2).

**F6. Direct ES literature since 2026-09-28: one item, conditionally false.**
* Cao–Xu 2610.32302 proposes a 56-family polynomial "cover", tested to m ≤ 10¹¹ and unproved by the authors' own
  account. By B1 Thm C it fails for infinitely many p ≡ 1 (24), CONDITIONAL on Hypothesis H (Assessment, since I did
  not check that the families are polynomial).
* Status of the field: ES OPEN; record verification 10¹⁸ (Mihnea–Dumitru); Bradford's claim unaccepted.

**F7. Markoff connectivity, now with general parameters.**
* *Sources.* Kingsbury-Neuschotz 2603.04096v3: density-one primes for any nondegenerate (A, B, C, D). Chen's
  all-large-p theorem: "every orbit has size divisible by p" + BGS giant component.
* *What made Chen's case pointwise.* A divisibility invariant of orbit sizes.
* *Does ES share it?* **No.** It has no infinite group on the fibre and no divisibility pattern in its graph orbits
  (`z31_markoff_chen.md` (c)).
* *First problem.* None.

**F8. Covering systems (Filaseta–Kalogirou–Klein NEW; Hashimoto; Harrington–Klein–Lowrance–Trifonov).** Structure
theory of finite systems. B1 says finite congruence menus cannot prove ES, so these results cannot bear on it.
Irrelevant.

**Answer to the brief's specific question (Assessment).** ES₅/U(n) is *not* literally an instance of a
Rickards–Stange semigroup orbit or of an HKRS packing, by (a)–(c) of F2. It matches their *exception shape*
exactly: a quadratic family, plus finitely many sporadic values in every computed range. Where that shape is
*proved* (RS fat orbits), the proof runs on a feature U(n) provably lacks at its scale: an arithmetic progression
of length ≍ n in the fibre. The literature therefore offers U(n) a *model of the statement*, not a *method*. Nothing
of this changes since `QUESTION_R.md` and `z36_reciprocity_obstruction_home.md`; z52 adds Alkauskas (a fourth
instance, power-count) and the Fuchs correction.

**Weak points / first problems ranked (Assessment).** No literature-derived first problem survives the screen. The
best candidates are already in `FRONTIER.md` §7: Question R/TG (item 11), Conjecture I3 (item 17), and RLD-U. z52
confirms rather than reorders them. One cheap follow-up is optional. If someone pursues the reciprocity singular
series of `QUESTION_R.md` §3, the flea orbit gives a decidable, obstructed control set on which to test whether
M_R-type corrections predict near-square deficits. My crude by-product suggests they exist there too.

## 4. Draft LITERATURE_2026.md additions
`LIT_Z52_ADDITIONS.md` (worktree root) is ready to append to `LITERATURE_2026.md`. It contains verified items
only: 3 new since the cutoff, 8 not previously recorded, and 5 updates/corrections, among them the Fuchs
attribution in `QUESTION_R.md` and the Chen title. Items the lanes cite that I did not re-verify are left out.
These include the non-arXiv entries, ProofAtlas, and the Johnston–Trudgian record (cited only through Li–Liu).

## 5. Cross-model hostile review
(TODO)
