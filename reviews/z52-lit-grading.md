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
(TODO)

## 3. Cross-lane synthesis
(TODO)

## 4. Draft LITERATURE_2026.md additions
See `LIT_Z52_ADDITIONS.md`. (TODO)

## 5. Cross-model hostile review
(TODO)
