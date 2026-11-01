# Z53_LIT — literature and tool sweep 2020–2026 for the B2 wall (wave z53, lane LIT)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only. A literature statement is quoted from the opened arXiv PDF
(theorem number + PDF page) unless marked "abstract only"; the proofs of cited papers were **not** re-checked, and every
cited preprint is unrefereed unless a journal is named. Access date for all sources: 2026-11-01.

Files: sweep script `scripts/z53_lit_arxiv_sweep.py` (queries `data/z53/lit/queries*.txt`, output `data/z53/lit/sweep*.tsv`,
587 distinct arXiv records, 2020–2026); fetch/extract `scripts/z53_lit_fetch.py`; verbatim theorem excerpts
`sources/z53_lit/excerpts_lane.txt` (generator `scripts/z53_lit_excerpts.py`) plus the two research-subagent excerpt files
`sources/z53_lit/excerpts_{analytic,pointwise}.txt`; PDFs and SHA-256 in `sources/z53_lit/README_*.md`; computations
`scripts/z53_lit_inverse_window*.py`, `scripts/z53_lit_invwin_census.c`, `scripts/z53_lit_invwin_analyze.py`, data in
`data/z53/lit/`. The repo already cites 685 arXiv identifiers (`data/z53/lit/repo_arxiv_ids.txt`); "new" below means "not
cited anywhere in the repo before this lane".

---

## 0. Bottom line and hot leads (read this first)

**Labels.** Everything in §§0, 4, 5 and 7 that is a verdict, routing judgement or "barrier confronted" is **Assessment**
unless explicitly labelled otherwise. Lemma L1, Lemma L2 and Remark Z are **PROVED** (elementary). F2 is **EVIDENCE**.
Literature statements are quotations, not lane claims.

**No verified result found, old or new, supplies the B2 step** (Assessment): a divisor of one p-tied integer in a class
whose modulus is tied to the solution. **Nothing found contradicts the Assessment (J)103** once its scope is stated
precisely (§6.4). The sweep did produce material that changes what other lanes should do:

1. **Kill-side tool for §7.2 (HCSHIFTS, FORESTCLASS, HCHYP):** Garaev–Shparlinski, arXiv:2304.07953v1, Thm 1.1 (p. 3; proof
   §3.1, pp. 6–7). For every fixed A > 1 and large N there is a prime p with (log p)^A ≍ N such that the inverses
   x̄ (mod p), x ≤ N, are badly distributed (D_p(N) ≫ 1). The construction is **unconditional**: Linnik/Xylouris gives a
   prime p ≡ −1 (mod m), where m = lcm of the (2N)^{1/A}-smooth integers in [N, 2N], with log p ≍ log m ≍ N^{1/A}. It
   controls a **positive proportion ρ(A)** (Dickman) of a window of polylog length (log p)^A by congruences, for an
   existentially chosen p. Caveat: the class −1 itself makes (★) *easy*, since any s ≡ 3 (mod 4) dividing p + 1 gives the
   u = 1 certificate. A kill must use the Linnik-lcm mechanism with a different class. With that caveat, this is a
   published, explicit-scale template for how far a Dickson-free congruence construction reaches at growing windows.
   Lemma L2 (§6.2, PROVED) shows the statistic depends only on p mod lcm(1..N). Note that this modulus exceeds p, so it is
   *not* bounded congruence data. F2 (§6.3, EVIDENCE) finds a raw correlation r = −0.167 between D_p(⌊log²p⌋) and
   R(p)/log²p over 64 380 primes, falling to r = −0.019 after adjusting both for small-divisor covariates of p ± 1.
2. **Quantified limit for "Type II at fixed modulus" (HYPKLOOST, HYPSUMPROD):** Pascadi, arXiv:2511.08445v2, Thm 1.1 (PDF
   p. 3) is new to the repo. It bounds bilinear Kloosterman sums S(am, n; c) with arbitrary coefficients for **every**
   modulus c (so c = 4p is allowed), M, N ≪ c^{1/2+o(1)}, with saving c^{1/700}. Lemma L1 (§6.1, PROVED) is scoped to
   length-independent bounds ‖α‖‖β‖c^{1−η} at dual lengths ≤ c^{1/2}. Such bounds give an asymptotic for a
   modular-hyperbola box count beyond Weil only if **η > 1/4**, which is exactly the perfect-orthogonality level that
   Pascadi calls "the best one could hope for" at M = N = √c. Even perfect orthogonality (a length-dependent bound) would
   reach only boxes of area ≥ q^{4/3+o(1)}. Separately, Dong–Robles–Zeindler arXiv:2601.00292 (claimed improvement of DFI
   to a 1/12 saving) is **withdrawn** (v2 comment: a missed factor L², "does not lead to an improved bound"). Do not use it.
3. **Calibration for target 5 / NONCRTSMOOTH / HCHYP (Assessment, analogy only):** the Erdős–Odlyzko–Sárközy (EOS)
   conjecture is **open even under GRH** (Banks arXiv:2609.37434v1, p. 1). EOS asks that every reduced class mod q be
   ℓ₁ℓ₂ with primes ℓ₁, ℓ₂ ≤ q. Banks's explanation: "the loss comes from the sum over the characters, not from any single
   character. The square-root saving in each individual sum, which is all that GRH provides, does not recover this loss."
   This is an independent external statement of the campaign's (J)98 phenomenon. EOS is a different problem from B2
   (primes, every class, size bounds), and no reduction between them is claimed. State of the art:
   * Matomäki–Teräväinen arXiv:2301.07679: ≥ (2/3 − ε)φ(q) classes; three primes for cube-free q.
   * Banks–Shparlinski arXiv:2610.19597: for q = ℓ^γ with ℓ fixed and γ large, all but
     exp(−c(log q)^{1/3}(log log q)^{−1/3})φ(q) classes. Under QRH/GRH, for general q: all but O((log q)³) classes, and a
     third prime ≪ (log q)⁴.
4. **For GENUSLVAL:** three human-authored write-ups of the OpenAI claim that Landau–Siegel zeros do not exist appeared in
   October 2026: Banks arXiv:2610.15483 (Thm 1.1: (1 − β) log q ≥ 3.0·10⁻³ for every real zero of every primitive real χ,
   all q ≥ 3), Kerr arXiv:2610.21099, and Guo arXiv:2610.30476 (constant 1/100). All are unrefereed. They concern **real
   zeros only**. They do **not** give the fixed zero-free strip that `LOWERTAIL_DEEP_ASTRA.md` Thm 5.4 needs for
   M_gen(p) ≫ (log p)², and they leave B2 untouched. They would make Siegel-ineffective inputs effective;
   `OAI_DUMP_IMPACT.md` §2.3 anticipated exactly this "real-zeros-only" scenario.
5. **(J)103 needs a wording repair, not a retraction.** The sentence "no every-n theorem with a polylog main term for any
   natural problem" (FRONTIER §1, §3) is literally false: two squares gives r₂(p) = 8 at every p ≡ 1 (4). Under GRH, the
   least quadratic non-residue ≤ (log p)² (Lamzouri–Li–Soundararajan) is an every-p theorem with a polylog expected count
   (M2). The repo's own catalogues already classify such theorems (T thick object, R rigidity/size squeeze, M2, M4).
   §6.4 gives a wording consistent with everything found.

**Verdict: narrowed** (§7). No hot lead for B2 itself.

---

## 1. Precise questions attacked (unchanged from Checkpoint 1)

For each question, success means a theorem (opened, theorem number quoted) that (i) is pointwise at one fixed integer or
modulus and (ii) supplies the named missing input.

* **Q(a) divisors of one integer in a class.** Is there a 2020–2026 theorem that gives, for every large N in a natural family,
  a lower bound (existence) for #{d | N : d ≡ a (mod q)} with q ≥ (log N)^c? Alternatively, any pointwise statement about
  the divisor classes of {p + u : u ≤ (log p)^A} at one p? (§7.2, §7.3.)
* **Q(b,c,d) fixed-modulus cancellation.** Is there a theorem that beats the trivial or Weil bound for
  #{(x,y) ∈ I × J : xy ≡ 1 (mod 4p)} with |I||J| < p^{3/2}, or for its height-tied subset? Alternatively, a bilinear
  Kloosterman / Kloosterman-fraction bound whose averaged variable is *not* attached to p and that improves
  E(p) ≪ p^{1/3+o(1)} (`Z52D_HYPERBOLA.md` Thm 1)? (§7.1.)
* **Q(e) multiplicative representation mod a fixed modulus.** Is there a "two-modulus" representation theorem? (Target 5.)
* **Q(f) ES itself.** Is there a new pointwise or exceptional-set result, proof claim or formalisation since the repo's
  last sweeps (arXiv to 2026-10-30; erdosproblems #242 to 2026-10-17)?
* **Q(g) Zaremba.** What is the pointwise input of Shkredov arXiv:2603.14116 / Zhang arXiv:2605.02518, and could it work
  at a polylog count?
* **Q(h) the (J)103 test.** Is there an every-n theorem with a polylog expected witness count for a natural problem?

## 2. Why this was not already closed

Earlier sweeps exist: `LITERATURE_2026.md` (to 2026-09-28 plus the Wave Y/Z/AA/z52 additions to 2026-10-30) and
`PARITY_AUDIT.md` §1 (tables 1A–1E). Further sources are the z52 lanes `BRAINSTORM/z52_lit_*.md`, the z52 deep catalogues
`BRAINSTORM/z52_deep_thin_pointwise_{opus,astra}.md`, `OAI_DUMP_IMPACT.md` and `ES_CONNECTIONS_TODO.md`. They cover the
classic tools well. Four gaps remained:
* post-2023 work in areas (b)–(e) and on Hooley's Δ;
* the Zaremba pointwise input ("statements only checked", LITERATURE_2026 z52);
* a precise scope for (J)103;
* the October 2026 human follow-ups to the OpenAI Siegel-zero claim.

One open "Next" item in `ES_CONNECTIONS_TODO.md` (Z-item at l. 10581–10584: check Klurman–Mangerel–Teräväinen for modulus
4p) concerned a source we located: the relevant KMT paper on EOS is cited in Banks–Shparlinski. That item's own Avenue
line ("the indicator changes with C ... not one multiplicative function") already explains why it cannot supply B2; we
add nothing to it.

## 3. Method and coverage

* 4 sweeps, 118 arXiv API queries (phrase/abstract/author; queries in `data/z53/lit/queries{,2,3,4}.txt`), filtered to
  2020–2026 (author sweep: 2023–2026). Of the 587 distinct records, 505 are not cited in the repo. Most are noise (physics/CS hits of
  keyword queries). About 60 were triaged by abstract and about 50 were opened in full text (47 by the lane, the rest by
  the subagents).
* 2 research subagents (mode `research`): (a)–(d) and (e)–(h). Their reports were cross-checked; the theorems cited below
  were re-opened by the lane, except Chan, Zhi and Shkredov, which are quoted from the subagents' excerpt files. Shkredov's
  Thm 8 count is for the class 𝒵, as the repo already said.
* Coverage claim: "none found" means none found by these queries and this reading. The sweep is not exhaustive.
* erdosproblems.com/forum/thread/242 was opened on 2026-11-01. The page was last edited 07 May 2026. It has 18 comments;
  the newest is dated 13 Feb 2026 (Bradford claim; Tao's "low-quality attempts" note). There is 1 "proof claim" and a
  formalised statement link (google-deepmind/formal-conjectures 242.lean, already in the repo). **Nothing after
  2026-10-17.**
* An arXiv search on `all:Straus`, sorted by date, shows **no ES preprint after Cao–Xu arXiv:2610.32302 (2026-10-23)**,
  which is already in the repo.

---

## 4. Lane-by-lane routing (the actionable output)

| z53 lane | items to read (verified) | what they give / why they do not close the target |
|---|---|---|
| HYPKLOOST (§7.1) | Pascadi 2511.08445 Thm 1.1; Steiner 2302.06409 Thms 1–2; Blomer–Risager–Shparlinski 2411.17823 Thm 1.1; Wright 2608.27732 Thm 1.1; **DRZ 2601.00292 withdrawn** | Pascadi: every modulus, arbitrary supports, saving c^{1/700} (for prime or interval-supported cases the repo's KMS p^{1/64} and Blomer–Pascadi c^{1/32} are stronger). L1 (scoped to length-independent bounds) shows η > 1/4 is needed for box asymptotics beyond Weil; Pascadi's own benchmark ('the best one could hope for', perfect orthogonality ‖α‖‖β‖√((M+N)c)) is η = 1/4 at M = N = √c. Steiner: Σ_{c≤C, c≡a (Q)} S(m,n;c)/c ≪_{m,n} …, with **implied constants depending on m, n** (uniform version: his Thm 18). For m, n ≍ p it is useless unless that dependence is polynomially small. BRS: triple sums over c ~ X, i.e. averaged over moduli (B6 if the modulus is p-attached; free here). Wright: dispersion over q ~ Q (B6). |
| HYPSUMPROD (§7.1) | Garaev–Shparlinski 2304.07953 Thms 1.1–1.4; Garaev–Shparlinski 2304.08689 Thm 1.1; Garaev–Pardo–Shparlinski 2410.03991 Thms 1.1–1.3; Zhi 2608.15458 Thms 1.2, 1.4; Chan 2506.04087 Thms 1–2; Shen 2607.07710 Thm 1 | GS Thm 1.3/1.4: for some p, **no square-root cancellation** in Σ_{x≤N} e_p(a x̄) at N ≤ exp((log p)^{1/3}) (their remark p. 5). So no bound with square-root (or better) cancellation can hold for all p at those lengths. This is a literature obstruction to "short-segment beyond square root" at polylog/subexponential length. GPS Thm 1.3: m₁/x₁ + m₂/x₂ ≡ λ (p) is solvable for intervals of length ⌊√(8p)⌋ (power size). Shen: Lehmer-type parity condition on (x, x̄) in very short intervals, **only for smooth squarefree q** (q = 4p excluded). |
| HYP2CYCLE (§7.1) | Kala–Miska 2212.07198 (abstract); Battistoni–Grenié–Molteni 2401.13118, Korolev 2403.08616 (abstracts) | CF-period moments of √d are averages over d (B6). Kala–Miska is a pointwise structural statement about partial quotients of √p, √2p (for each a, only finitely many p have a an odd number of times in the period); there is no visible link to 2-cycles of x ↦ (−p mod x). |
| HCSHIFTS / FORESTCLASS (§7.2) | **Garaev–Shparlinski 2304.07953 Thm 1.1 + proof §3.1**; Lemma L2 + F2 here; Fan–Pomerance 2401.10427, Abi Abdallah et al. 2608.27356, Haddad 2512.13669 (averaged) | GS is the unconditional Linnik-lcm template: a ρ(A) fraction of a (log p)^A window is controlled by congruences, for existentially chosen p (the class −1 they use makes (★) easy; a kill needs another class). To control the *whole* window one needs the non-smooth members too; they carry prime factors > N^{1/A}, and fixing their residues needs a modulus of size e^{≫N}, which exceeds p. That is the HCSHIFTS observation, now with a published construction to cite. The averaged divisor-in-interval results are B6. |
| HCHYP (§7.2/§7.4) | Banks 2609.37434 §1 (EOS open under GRH, with reason); Banks–Shparlinski 2610.19597 Thms 1.3–1.4 (QRH-conditional); Matomäki–Teräväinen 2605.27833 Thm 1.1 | MT: for multiplicative h, every reduced class a mod q contains squarefree n₁, n₂ ≤ q^{2+ε} with h(n₁) < 0 < h(n₂), **unless** some real χ mod q satisfies Σ_{p≤q^{1/3}, h(p)χ(p)<0} 1/p ≤ c/q^{ε/100} (sgn h strongly pretends to be χ). This is a pointwise class-level theorem whose only exceptional alternative is a real-character one, at power scale with free n (M1a/M4). Assessment: it is the closest analogue found of "only the quadratic layer obstructs"; an analogy to T1, not an identification. It is not ES-transferable (the n are not divisors of a tied integer). |
| GENUSLVAL (§7.3/§7.4) | Banks 2610.15483 Thm 1.1; Kerr 2610.21099 Thm 1; Guo 2610.30476 (abstract) | Real zeros only, explicit constants: (1 − β) log q ≥ 3·10⁻³ (Banks, q ≥ 3 with Lu–Zaman–Zhao). This is not a zero-free strip (Thm 5.4 needs one). The OAI-003 quasi-RH (7/8) claim is separate and still has no independent human write-up found. |
| GENUSREDEI (§7.3/§7.6) | Koymans–Pagano 2005.14157 (abstract); Xu–Zhu 2608.00387 (abstract); Xu 2609.03238, 2609.23419 (abstracts); Fischer–Uttenthal 2512.14901 (abstract); Koymans–Morgan–Smit 2101.03407 (title) | Higher Rédei reciprocity gives the solubility of N_d(x, y) = l **as d varies** (averaged, B6). Xu–Zhu: 4-ranks of Q(√−d), Q(√−d₀d) are asymptotically independent over d, a correlated-pair statement, averaged. Fischer–Uttenthal: spins, conditional on a short character-sum conjecture. **No pointwise-in-p joint-class statement found**; this supports the §7.6 expectation that joint realisation is free, but proves nothing. |
| NONCRTSMOOTH (target 5) | Matomäki–Teräväinen 2301.07679 Thm 1.1; Banks–Shparlinski 2610.19597 Thms 1.1–1.4; Banks 2609.37434 Thm 1.1 + Table 1; Xie 2606.30567 Thm 1.1; Martin–Parvardi 2008.10198 (abstract) | The best "every class mod q" product theorems use free primes and power counts. Even the two-prime binary case is open under GRH (item 3 above). Assessment (analogy only, no reduction): a tied two-modulus representation statement looks harder than EOS on every axis (§6.6); no theorem of that shape was found. |
| NONCRTLOGIC (target 5) | Garaev–Shparlinski 2304.07953 (via L2); Ford–Gabdullin–Granville 2410.04649 (abstract) | L2: inverse statistics on a window x ≤ N are functions of p mod lcm(1..N). For N ≍ log²p that modulus exceeds p, so they are a growing p-dependent family (B1's E1 hatch), **not** bounded congruence data; L2 does not kill them. F2 found their (★)-predictive content small after small-divisor adjustment (EVIDENCE). FGG: least primitive root ≤ p^{1/4−δ(p)} for a density-one explicit set of primes (B6). |
| LATTICE | Baird–Kerr–Shparlinski 2310.20342 (abstract); Gao–Feng–Hu–Pan 2512.19076 (abstract); Hales 2410.05030 (repo) | Many-variable Coppersmith heuristics hold "with high probability" (averaged); rank-3 lattices give factoring/power-divisor *algorithms*. Upper bounds and algorithms, not existence (same gap as PARITY_AUDIT A1–A2). |
| WILDCARD | §6.4 table | — |

---

## 5. Verified catalogue (by area)

Columns: **item** · statement (theorem, page) · new? · verdict for [7.1] height-tied hyperbola at one p / [7.2] polylog
one-coordinate windows / [7.3] class beyond quadratic / [T5] non-CRT lower bound · barrier confronted.
"UB" means a pointwise *upper* bound or algorithm, i.e. the wrong direction for existence.

### (a) Divisors of one integer in residue classes / intervals
| item | statement | new? | verdicts · barrier |
|---|---|---|---|
| Ford–Green–Koukoulopoulos, arXiv:1908.00378v3 (Invent. Math. 2023) | Thm 1: Δ(n) ≥ (log log n)^{η−ε} for almost all n, η = 0.35332… | new id (named without id in z52b brainstorm files) | 7.1 –, 7.2 –, 7.3 – (interval, not class), T5 – · B6 (almost all n) |
| Koukoulopoulos–Tao, arXiv:2306.08615v4 | Thm 1: Σ_{n≤x} Δ(n) ≪ x(log log x)^{11/4} | new id | mean value · B6, UB |
| Ford–Koukoulopoulos–Tao, arXiv:2308.11987v2 | Thm 1 (quoted as [10]): Δ(n) ≥ (Log₂x)^{η*−ε} for all but o(x) n ≤ x, η* ≥ η | new | B6 |
| de la Bretèche–Tenenbaum, arXiv:2512.05652v1 | abstract: new upper bounds for weighted moments of Δ | new | B6, UB |
| Haddad, arXiv:2512.13669v3 | Thm 1: H(x,y,z) = x·h(log y/log x, log z/log x) + O(x(log y_min)^{−δ}(log₂ y_min)^{3/2}) | new | B6 (counts n ≤ x) |
| Abi Abdallah–Kovaleva–Schlitt–Tardy, arXiv:2608.27356v1 | Thm 1.1: H*(x,y,z) (divisor of the form ℓ − 1 in (y,z]), phase transitions | new | B6 |
| Drappeau–Mounier, arXiv:2606.30428v1 | abstract: rigorous numerics for the density h(α,β) of n with a divisor in [n^α, n^β] | new | B6 |
| Grimmelt–Merikoski, arXiv:2508.17979v2 | Thm 1.1: τ in APs, Q < X^{2/3+ε}, for all but O(√ε Q) moduli; Thm 1.2: Σ_{n₁,n₂≤X} τ(n₁n₂² + 1) ∼ (3/ζ(2)) X² log X | new | 7.1/7.2: class-blind; the Type I side numbers p² + 4c²d have this binary-cubic shape, but with constant p² and with the class condition f ≡ −p (mod 4cd) tied to (c, d) · B6 (almost all q), tied modulus |
| Nguyen, arXiv:2205.02354v2 | Thm 1: variance of d_k over residues mod one composite d, smoothed, X = d^c | new | averaged over residues a (B6-type) |
| He–Sahai, arXiv:2608.06681v1 | abstract: n-divisor APs need length ≫ n^{3/4}/√(log n) | new | unrelated (covering by multiples) |
| Hales 2410.05030, Bernstein 2008, Lenstra 1984, CHGN 2008, Erdős–Hall | — | repo | UB / B6 (PARITY_AUDIT A1–A3) |

**Answer to Q(a): no.** Every item is averaged over n (B6) or is an upper bound or algorithm (Lenstra/Coppersmith). In
every 2020–2026 item, Hooley's Δ concerns concentration in *intervals*, not classes. The repo's Z0501 test already showed
that the class version Δ_m is dominated by the trivial class.

### (b) Modular hyperbola, boxes, short segments, modular inverses
| item | statement | new? | verdicts · barrier |
|---|---|---|---|
| **Garaev–Shparlinski, arXiv:2304.07953v1** | Thm 1.1 (p. 3): ∀ A > 1, ∀ large N, ∃ prime p, (log p)^A ≍ N, D_p(N) ≫ 1. Thm 1.2: Σ_{a≤k}\|Σ_{x≤N} e_p(a x̄)\| ≫ kN. Thms 1.3–1.4: ∃ p with exp(c₁(log p log log p)^{γ/(1+γ)}) > N > exp(c₂(…)) and D_p(N) ≫ N^{−γ} | new | 7.1: obstruction: no bound with square-root (or better) cancellation can hold uniformly in p for N ≤ exp((log p)^{1/3}) (Thm 1.4 with γ → 1/2; authors' remark p. 5); 7.2: kill-side template (§0 item 1); T5: the construction is a Linnik prime in a class mod lcm (L2: the statistic depends on p mod lcm(1..N)) · existential p, not a prescribed one |
| Garaev–Shparlinski, arXiv:2304.08689v1 | Thm 1.1: #(HM) = p + O(p^{1−η}) for interval H, arbitrary set M, if H ≥ p^{2/3}, HM ≥ p^{1+ε} or (H < p^{2/3}, M ≥ p^{1/3}, HM^{1/4} ≥ p^{3/4+ε}) | new | power-size sets (B3), free sets (M4) |
| Garaev–Pardo–Shparlinski, arXiv:2410.03991v1 | Thm 1.1: λ ≡ Σ_{i≤3} m_i/x_i^s (p), \|M\| = ⌊p^{14/29}⌋, H = ⌊p^{14/29+ε}⌋. Thm 1.2: binary, s = 1, for almost all p, \|M\| = ⌊√p⌋, H = ⌊√p(log p)^{6+ε}⌋. Thm 1.3: binary with m_i ∈ I, x_i ∈ J, intervals of length ⌊√(8p)⌋ | new | Egyptian-fraction-shaped congruences mod p with free power-size sets; B3, M4; Thm 1.2 B6 |
| Zhi, arXiv:2608.15458v1 | Thms 1.2, 1.4: T_r(λ) = (N^{2r}/p)(1 + O(p^{−δ})) for r ≥ 5 sets × shifted intervals, N > p^{α_r+ε}, α_r = 1/3 + 4/(9√r) + O(1/r) | new (subagent) | B3, M4 |
| Chan, arXiv:2506.04087v1 | Thm 1: ∃ infinitely many p ≡ 1 (4) and c_p with ≤ 1 point of xy ≡ c_p in every box of side ⌊0.1 log p⌋. Thm 2: for all p, c, M multiplicatively closed of positive density: (x+h, y+k), (x, y) ∈ H_p^c with h, k ≤ C p^{1/4} exp((log p)^{1/2+ε}) | new (subagent) | 7.1: c_p special, not c = 1; Thm 2 free shifts · M4 |
| Shen, arXiv:2607.07710v1 (+ part II 2607.06575) | Thm 1: Lehmer count L(N,q) = ½Nφ(q)/q + O(N^{λ−κ+O(η)}q^{κ+ε}) for squarefree q with prime factors ≤ q^η; Cor 1: a ≪ q^ε with 2 ∤ a + ā | new | 7.1: parity condition on both hyperbola coordinates (a fixed modulus-2 analogue of x ≡ y ≡ −1 (4C)); needs smooth q, so q = 4p is excluded · tied modulus (C varies) |
| Shparlinski, arXiv:2311.16640v2 | Thm 1.1: average smallest denominator in short intervals S(N) = (16/π²)N^{3/2} + O(N^{29/22+o(1)}), via Kloosterman-fraction bilinear bounds | new | averaged · B6 |
| Shparlinski *Modular hyperbolas* 1103.2879, Cilleruelo–Garaev 1007.1526, KSWX 2204.05038, Bourgain–Garaev 1211.4184 | — | repo | PARITY_AUDIT B1, B4, B5 |

### (c) Kloosterman fractions, bilinear / trilinear Kloosterman sums, sums over moduli
| item | statement | new? | verdicts · barrier |
|---|---|---|---|
| **Pascadi, arXiv:2511.08445v2** | Thm 1.1 (PDF p. 3): for c, M, N ∈ ℤ⁺, M, N ≪ c^{1/2+o(1)}, a ∈ (ℤ/c)^×: Σ_{m≤M,n≤N,(m,n,c)=1} α_mβ_n S(am, n; c) ≪ ‖α‖‖β‖c^{1−1/700+o(1)}; if \|α_m\| ≤ 1: Σ_{(n,c)=1} … ≪ √M‖β‖c^{1−1/276+o(1)}. p. 2: the trivial bound is ‖α‖‖β‖c^{o(1)}min(c, √(MN c)); "the best one could hope for is the perfect-orthogonality bound ‖α‖‖β‖c^{o(1)}√((M+N)c)" | new | 7.1: every modulus, so c = 4p is allowed; L1 (§6.1) shows length-independent savings η ≤ 1/4 give no box asymptotics beyond Weil · tied modulus + L1 |
| Steiner, arXiv:2302.06409v1 | Thm 1: Σ_{c≤C} S(m,n;c)F(c)/√c ≪_{m,n,F} C^{1−9/32+o(1)} for periodic F; Thm 2: Σ_{c≤C, c≡aq (Q)} S(m,n;c)/c ≪_{m,n} (QC)^{o(1)}(…C^{1/6} + …) | new | 7.1: sums over moduli c with fixed (m, n); for ES at fixed p the natural Kloosterman sums have modulus 4p (fixed), and in SL₂ form the class a ≡ d ≡ −1 (mod c) is a single residue, so no Kloosterman sum over c arises (§6.1 remark). The implied constant depends on m, n · B6/tied |
| Blomer–Risager–Shparlinski, arXiv:2411.17823v3 | Thm 1.1: K(M,N;X) ≪ (MNX + (MN)^{2/3}X^{7/6})(MNX)^{o(1)} (triple sums of Kloosterman sums; discrepancy of modular inverses mod c ~ X) | new | averaged over c · B6 if c is attached to p |
| Wright, arXiv:2608.27732v1 | Thm 1.1: equidistribution of α ⋆ β in APs on average over q ~ Q, for N^{56/23}X^{−17/23+ε} ≤ Q ≤ NX^{−ε}; sharpens Bettin–Chandee on subdyadic intervals | new | B6 (average over q) |
| Shao–Shparlinski–Wijaya, arXiv:2411.12113v1 | Thm 1.1: sums of S(·;p) over s-free / smooth arguments N ∈ [p^{1/2+2/ℓ}, p] | new | fixed prime modulus, power-length sums · B3 |
| **Dong–Robles–Zeindler, arXiv:2601.00292** | claimed 1/12 saving for DFI-type bilinear forms | new | **withdrawn** (v2: "missed a factor of L² … does not lead to an improved bound"; error found by Pascadi) — do not cite |
| DFI 1997, Bettin–Chandee 1502.00769, KMS, Blomer–Pascadi 2607.24311 | — | repo | PARITY_AUDIT B2, B2′, B7 |

### (d) Sum-product and energy over ℤ/q
| item | statement | new? | verdicts · barrier |
|---|---|---|---|
| di Benedetto–Garaev–García–González-Sánchez–Shparlinski–Trujillo, arXiv:2003.06165v1 | abstract: max_a \|Σ_{x∈𝓗} e_p(ax)\| ≤ H^{1−31/2880+o(1)} for subgroups of order H > p^{1/4}; double sums with short intervals | new | subgroup sums; no tie · M3-type structure ES lacks |
| Garaev–Konyagin 2608.26349, Shkredov 2307.03156, 2502.20702, Hanson–Rudnev–Shkredov 2305.04038 (titles/abstracts) | sum-product/expanders | new | power-size sets (B3) |
| Bourgain–Garaev 1211.4184, KSSZ 2103.09405, Kerr–Shparlinski–Yau 1711.10582 | — | repo | PARITY_AUDIT B5 |

**Answer to Q(b,c,d): no.** Every new bound is either an average over moduli or residues (B6), a power-size free-set
statement (B3/M4), or a fixed-modulus bilinear bound. Lemma L1 shows that length-independent bounds of the last kind cannot beat
Weil for hyperbola box counts unless η > 1/4. The one new pointwise statement about short segments (Garaev–Shparlinski Thms 1.3–1.4) is an
*obstruction*.

### (e) Multiplicative representation of residues by primes / smooth numbers
| item | statement | new? | verdicts · barrier |
|---|---|---|---|
| **Matomäki–Teräväinen, arXiv:2301.07679v3** | Thm 1.1: (i) q cube-free large ⇒ E₃(q) = (ℤ/q)^×; (ii) E₃(q^{1+ε}) = (ℤ/q)^×. Thm 1.3: \|E₂(q)\| ≥ (2/3 − ε)φ(q) | new | T5: free primes ≤ q, power count · M4, B3 |
| **Banks–Shparlinski, arXiv:2610.19597v1** | Thms 1.1–1.2 are for q = ℓ^γ with the prime ℓ **fixed** and γ ≥ γ₁(ℓ) large, constants depending on ℓ (not uniform in ℓ; nothing for q = p or 4p as p varies). Thm 1.1: Σ_{ℓ₁ℓ₂ℓ₃ ≡ a} log ℓ₁ log ℓ₂ log ℓ₃ = (q²q•/φ(q))(1 + O(…)) for ℓ₁, ℓ₂ ≤ q, ℓ₃ ≤ q•, log q• ≥ C₁(log q)^{2/3}(log log q)^{4/3}; Thm 1.2: \|(ℤ/q)^× ∖ EOS₂(q)\| ≤ φ(q)exp(−C₂(log q)^{1/3}(log log q)^{−1/3}); Thm 1.3 (QRH[q,σ₀]): ℓ₃ ≤ C(log q)^{2/(1−σ₀)}; Thm 1.4: \|(ℤ/q)^× ∖ EOS₂(q)\| ≪ φ(q)q^{−2(1−σ₀)}(log q)³ | new | T5 calibration: a polylog *third* prime under GRH, but the count is a power (ℓ₁, ℓ₂ ≤ q) · B3, M4 |
| **Banks, arXiv:2609.37434v1** | Thm 1.1: in Granville's random model, a.s. every reduced class mod every large q is g₁g₂ with g_i ∈ (X_q, 2X_q], X_q ≍ q^Θ, Θ > 3/4, with asymptotic counts. p. 1: EOS "remains open even under GRH" (reason quoted in §0 item 3). p. 3: 3/4 is sharp for the method (Weil–Estermann error q^{1/2+o(1)} vs main N²/q). Table 1 (p. 2): Walker, Szabó, Matomäki–Teräväinen, KMT | new | T5 calibration; mechanism = Bernoulli count over orbits n ↦ a n̄, i.e. the same orbit pairing as the repo's swap-Poisson model · model, not theorem about primes |
| Xie, arXiv:2606.30567v1 | Thm 1.1: every narrow ray class mod 𝔮 (fixed K) is a product of 3 prime ideals of norm ≤ (N𝔮)^{103/64+κ}; Thm 1.2: ≥ (2/3 − ε) of classes are products of two | new | the number-field analogue of MT; free prime ideals · M4, B3 |
| Matomäki–Teräväinen, arXiv:2605.27833v1 | Thm 1.1: for multiplicative h with h(p) ≠ 0 (p ∤ q), the least scale R(h;q) at which every reduced class a mod q contains squarefree n₁, n₂ with h(n₁) < 0 < h(n₂) is ≤ q^{2+ε} (ε small, q large in terms of ε, c), **unless** some χ mod q of order ≤ 2 has Σ_{p≤q^{1/3}, h(p)χ(p)<0} 1/p ≤ c/q^{ε/100} (1.1) (read with pdftotext; pypdf drops the fraction) | new | 7.3 analogue (Assessment): the only exceptional alternative is real-character pretentiousness; pointwise in (q, a), but free n · M4, B3 |
| Martin–Parvardi, arXiv:2008.10198v1 | abstract: y(p) ≪ p^{1/(4√e)+ε}, where y(p) is least such that subset products of {1,…,y} cover (ℤ/p)^× | new | power scale, free generators · M4 |
| Banks–Shparlinski, arXiv:2009.06800v1 | abstract: Soundararajan's smooth-numbers-in-APs conjecture for smooth moduli q | new | free smooth numbers · M4 |
| Ramaré–Walker, Szabó, Harman–Shparlinski, Munsch, KST 2609.25393, Pilatte | — | repo | PARITY_AUDIT D11, z52 lit |

**Answer to Q(e): none found.** No two-modulus representation theorem supplying the target was found. Even the one-modulus
binary statement with free primes (EOS) is open, also under GRH. See §6.6 (Assessment).

### (f) Erdős–Straus and Egyptian fractions, 2020–2026
* **No new ES research preprint since the repo's last sweep.** The newest arXiv item is Cao–Xu arXiv:2610.32302v1
  (2026-10-23; unproved 56-family covering claim; already in the repo). erdosproblems #242: nothing after 2026-02-13 (see §3).
* New, outside the repo: **carlok/erdos-straus-offset-lean** (GitHub README read 2026-11-01). It is a Lean 4 formalisation
  of a "classical divisor-split" offset construction and of transport along progressions n ↦ n + 4pdk (least period 4pd),
  with explicit families. The README says "The Erdős–Straus conjecture remains open". Verdict: congruence families (B1);
  no claim.
* Tao, "Changes to the Erdős problems web site", terrytao.wordpress.com 2026-10-06 (search-result description only): the
  site stopped displaying solved status. It is not ES-specific.
* Egyptian-fraction preprints 2020–2026 not in the repo are on other problems (underapproximation Chu 2302.01747,
  2306.12564; Kamio 2503.02317; Steihaug–Gardner 2502.05607; Pham–Zakharov 2410.14624 and Conlon–Fox–Pham 2311.01416 on the
  *Erdős–Straus non-averaging set* problem, a different problem). None bears on 4/p.

### (g) Zaremba pointwise claims — the key pointwise input
* **Zhang arXiv:2605.02518v2** (PDF, re-read by the lane). Thm 3.6 (p. 6): with A, B (Cantor-type numerator sets) and a
  q-dependent generating set S with |S| ≈ q^{2τ} ((3.2), (3.5); Remark 1.4, p. 2; N ∼ q^{2τ}, t ∼ q^{1/2−τ}, p. 6),
  Σ_{s,a,b} 1_{sa=b} = (φ(q)/q²)|A||B|N + O_ε(q^ε√(|A||B|)N^{1−η}) (3.7). Immediately after (p. 7): "the error term in (3.7)
  is smaller than the main term if we take τη > 1/M" (3.8). The pointwise engine is spectral gap / expansion in
  SL₂(ℤ/q) for a generating set that grows with q (Bourgain–Varjú does not suffice, Remark 1.4).
* **Shkredov arXiv:2603.14116v2** (PDF via the subagent; excerpts in `excerpts_pointwise.txt`). Cor 1 (p. 1): bounded
  partial quotients for every prime or squarefree q. Thm 8 (p. 6): ≥ q^{2w_M−1−o(1)} good numerators **for q in the class
  𝒵** (p. 4). Cor 16 (p. 8): |A ∩ B^{−1}| − |A||B|/q ≪ √(|A||B|)N^{−κ}. Remark 9 (p. 7): all-q existence via Zhang–Tang
  expansion; "the remaining results of the paper remain unchanged". The subagent's summary agrees with the repo's existing
  correction (Thm 8 is class-𝒵 only).
* Moshchevitin–Murphy–Shkredov arXiv:2212.14646v1, Thm 1: every large q with sufficiently large prime factors (and every
  large squarefree q, and q = pⁿ for large n) has a with all partial quotients O(log q/log log q). This improves Korobov's
  O(log q). It is pointwise; the good-numerator count is a power of q (as in Korobov's method).
* **Why this cannot run at a polylog count.** *Remark Z (PROVED, elementary, about the shape of the estimate).* Suppose an
  incidence count I = Σ_{s∈S,a∈A,b∈B} 1_{sa=b} modulo q satisfies I = 𝔐 + O(q^ε√(|A||B|)N^{1−η}) with 𝔐 = φ(q)|A||B|N/q²,
  |S| = N, and 0 < η < 1/2 (Zhang (3.7)). Eliminating √(|A||B|) = q√𝔐/√(φ(q)N) gives
  error/𝔐 = q^{1+ε}N^{1/2−η}/√(φ(q)𝔐) ≥ q^{1/2+ε}N^{1/2−η}/√𝔐. So the estimate certifies I > 0 only if
  𝔐 > q^{2+2ε}N^{1−2η}/φ(q) ≥ q^{1+2ε}. **The expected incidence count must exceed the modulus.** *Assessment:* no
  encoding of (★) into such an incidence count is known. For any encoding modulo q ≥ p^c, the polylog expected count of
  ES falls short of this requirement by a power of p. This is FRONTIER M1a/B3 for this method. Expansion also holds at odd
  squares, so the method is T1-blind.

### (h) Every-n theorems with small witness counts — see §6.4.

---

## 6. Results of the lane (proofs and computations)

### 6.1 Lemma L1 — length-independent bilinear Kloosterman bounds versus hyperbola box counts (PROVED, elementary)

*Setting.* q ≥ 3, (λ, q) = 1, ε > 0 fixed, q^{1/2+ε} ≤ X, Y ≤ q. Fix smooth bump functions w₁, w₂ supported in [1, 2] and
put 𝒩 := Σ_{x,y} w₁(x/X)w₂(y/Y)·1[xy ≡ λ (mod q)] (a smoothed box count).

*Hypothesis BB(η)* (a length-independent bilinear bound). For all 1 ≤ M, N ≤ q^{1/2} and all complex α, β supported on
0 < |m| ≤ M, 0 < |n| ≤ N: |Σ α_mβ_n S(m, λn; q)| ≤ ‖α‖₂‖β‖₂ q^{1−η+o(1)}.

*Status of BB.* We have S(m, λn; q) = S(λm, n; q) (substitute x ↦ λx), so this is the shape of Pascadi's Thm 1.1 with
a = λ. That theorem holds for every modulus with η = 1/700, under the restriction (m, n, q) = 1. Two adjustments are needed.
1. Negative frequencies: S(−m, n; q) = S(m, −n; q), i.e. replace λ by −λ on the corresponding quarter.
2. For q = 4p and |m|, |n| ≤ q^{1/2} < p, the only pairs with (m, n, q) > 1 have 2 | m and 2 | n. For these, twisted
   multiplicativity S(m, n; 4p) = S(p̄m, p̄n; 4)·S(4̄m, 4̄n; p) applies. The first factor depends only on (m, n) mod 4, so
   split into ≤ 16 classes. The second factor equals S(16̄ m, n; p) (by S(am, an; p) = S(m, a²n; p) and symmetry), with
   (m, n, p) = 1. Pascadi's theorem mod p then bounds each piece by ‖α‖‖β‖p^{1−η+o(1)}.

Hence BB(1/700) holds for q = 4p. The repo's KMS (prime modulus, p^{1/64} at √p) and Blomer–Pascadi (c^{1/32} at √c, for
intervals) give larger η in their settings. L1 only uses η ≤ 1/4.

**Claim.** Write 𝒩 = MT + E with MT = φ(q)ŵ₁(0)ŵ₂(0)XY/q². Weil gives |E| ≪ q^{1/2+o(1)}; BB(η) gives |E| ≪ √(XY)·q^{−η+o(1)}.
Consequently:
(i) the BB(η) bound is smaller than the Weil bound only when XY < q^{1+2η};
(ii) the BB(η) bound is o(MT) only when XY > q^{2−2η+o(1)};
(iii) the two ranges intersect only if η > 1/4.

So, for η ≤ 1/4, the specific argument "complete both variables (Poisson) and bound the dual bilinear form by a
length-independent BB(η)" never yields an asymptotic for a smoothed box count beyond what Weil gives (threshold
XY > q^{3/2+o(1)}).

*Proof.* Poisson summation in both variables modulo q gives
  𝒩 = (XY/q²) Σ_{h,k ∈ ℤ} ŵ₁(hX/q) ŵ₂(kY/q) S(h, λk; q).
Here S is the Kloosterman sum; it is a Ramanujan sum c_q(·) if exactly one of h, k is 0, and equals φ(q) at h = k = 0,
which gives MT.

*Truncation.* Since |ŵ_i(ξ)| ≪_A (1 + |ξ|)^{−A}, and |h| > q^{1/2} implies |hX/q| ≥ q^{ε}, the terms with |h| > q^{1/2}
or |k| > q^{1/2} contribute O_A(q^{−A}) in total (use |S| ≤ q). So only 0 < |h|, |k| ≤ q^{1/2} matter, which is
inside BB's range. No q^{ε} is lost: the cut is at q^{1/2}, not at q^{1+ε}/X.

*Axis terms.* For k = 0, |Σ_{0<|h|≤q^{1/2}} ŵ₁(hX/q)c_q(h)| ≤ Σ_{d|q} d Σ_{d|h, h≠0} |ŵ₁(hX/q)| ≪ Σ_{d|q} d·(q/(dX))·q^{o(1)} ≪ τ(q)q^{1+o(1)}/X.
For d > q/X the inner sum is ≪ (dX/q)^{−A}, so those d contribute ≪ q/X as well. Hence the axis terms are
≪ (XY/q²)·q^{1+o(1)}/X = Y q^{−1+o(1)}, and symmetrically X q^{−1+o(1)}. Both are ≤ q^{o(1)}, negligible below.

*BB part.* Put α_h = ŵ₁(hX/q) and β_k = ŵ₂(kY/q) on 0 < |h|, |k| ≤ q^{1/2}. Then ‖α‖₂² ≪ Σ_h (1 + |h|X/q)^{−2} ≪ q/X
and ‖β‖₂² ≪ q/Y. BB(η) bounds this part of E by
  (XY/q²)·√(q/X)√(q/Y)·q^{1−η+o(1)} = √(XY)·q^{−η+o(1)}.

*Weil part.* |S(h, λk; q)| ≤ τ(q)(h, k, q)^{1/2}q^{1/2}. Summing over the gcd,
Σ_{h,k≠0} |ŵ₁||ŵ₂|(h, k, q)^{1/2} ≤ Σ_{d|q} d^{1/2} Σ_{d|h, d|k} |ŵ₁(hX/q)ŵ₂(kY/q)| ≪ Σ_{d|q} d^{1/2}(q/(dX) + 1)(q/(dY) + 1).
The terms with d ≤ q/X give ≪ q^{2+o(1)}/(XY); for larger d, Fourier decay again makes them ≪ q^{2+o(1)}/(XY). So the
Weil part is ≪ (XY/q²)·q^{1/2+o(1)}·q²/(XY) = q^{1/2+o(1)}.

*Comparisons.* (i) √(XY)q^{−η} < q^{1/2} ⟺ XY < q^{1+2η}. (ii) √(XY)q^{−η} = o(XY/q^{1+o(1)}) ⟺ XY > q^{2−2η+o(1)},
using φ(q)/q = q^{−o(1)}. (iii) 1 + 2η > 2 − 2η ⟺ η > 1/4. ∎

*Remark (perfect orthogonality).* Pascadi (p. 2) calls ‖α‖‖β‖c^{o(1)}√((M+N)c) "the best one could hope for". This bound
is length-dependent. Inserted in the same argument with M = q/X, N = q/Y, it gives
|E| ≪ (XY/q²)·√(q/X)√(q/Y)·√((q/X + q/Y)q)·q^{o(1)} = √(X + Y)·q^{o(1)}, which beats MT once (for X = Y) X > q^{2/3+o(1)},
i.e. area q^{4/3}. So even an optimal bilinear estimate keeps this method above area q^{4/3}. At the balanced point
M = N = √c the perfect-orthogonality bound corresponds to η = 1/4, consistent with (iii).

*Scope.* L1 concerns smoothed box counts with sides ≥ q^{1/2+ε}, the range where the dual lengths fit, and one specific
argument. It does not exclude:
* other bilinear methods or length-dependent bounds;
* methods that keep one variable short and use incomplete-sum or Kloosterman-fraction bounds (averaged over λ in KSWX,
  PARITY_AUDIT B4, or needing smooth q as in Shen).

ES needs the height-tied subset, a union of ≍ p height slices. L1 only *quantifies*, at the box level, the FRONTIER line
"Type II/bilinear fixed-modulus savings need saving p^{1−o(1)} on unit coefficients".

### 6.2 Lemma L2 — modular inverses on short windows (PROVED, elementary)

Let p be prime and 1 ≤ x < p. Let x̄ ∈ [1, p) be the inverse of x and k_x := (x x̄ − 1)/p. Then k_x ∈ [0, x),
k_x ≡ −p^{−1} (mod x), and

  x̄/p = k_x/x + 1/(xp).

*Proof.* We have x x̄ ≡ 1 (mod p), so k_x is an integer, and 0 ≤ k_x < x because 1 ≤ x x̄ < xp. Reducing x x̄ = 1 + p k_x
modulo x gives p k_x ≡ −1 (mod x). Divide by xp. ∎

*Consequences.*
(a) For N < p, the configuration {x̄/p : x ≤ N} equals {k_x/x : x ≤ N}, each point shifted by 1/(xp) ≤ 1/p. The data
(k_x)_{x≤N} depends only on p mod lcm(1,…,N). For N ≍ log²p this modulus is ≈ e^{N}, far larger than p. So this is a
growing p-dependent family of residues (B1's E1 hatch), not bounded congruence data. **L2 does not place such statistics
inside B1's no-go**; it only identifies what they are made of. Statistics that are Lipschitz in the point positions
(e.g. Weyl sums Σ e(a x̄/p) for bounded a) change by O(aN/p) under the shift. Discontinuous statistics such as the
sup-discrepancy need not be stable.
(b) Dual (Farey) form of the (★) trial event. For x ≡ 3 (mod 4) with x < p, there is a (★) triple with 4uC − 1 = x if
and only if some e with 4 | e and e | x + 1 satisfies e ≡ k_x (mod x).
*Proof.* Take e = 4C and u = (x + 1)/e. Then 4Cp ≡ −1 (mod x) and 4Cu ≡ 1 (mod x), so x | p + u, and B = (p + u)/x ≥ 1.
Conversely, a triple gives e = 4C.
*The two cases.* Since 4 ≤ e ≤ x + 1, either e = k_x, or e = x + 1, the latter exactly when k_x = 1, i.e. u = 1 and
x | p + 1. In words: x̄/p equals, up to 1/(xp), the fractional part {e/x} of one of the ≤ τ(x + 1) special fractions
e/x with 4 | e | x + 1. For e = x + 1 the fractional part is 1/x, not e/x: e.g. p = 5, x = 3 gives x̄/p = 2/5 =
1/3 + 1/15. This is a restatement of the trial form (PARITY_AUDIT Lemma 2.1), recorded only as the bridge between the
GS statistic and (★).

### 6.3 Falsifier F2 — does (★)-hardness track Garaev–Shparlinski-type inverse discrepancy? (EVIDENCE)

*Question.* GS-type primes have badly distributed inverses on polylog windows. Do (★)-hard primes, and if so beyond simple
small-divisor data?

*F2a: hard primes vs controls (EVIDENCE).* Script `scripts/z53_lit_inverse_window.py`, revised after review; outputs
`data/z53/lit/inverse_window.tsv`, `inverse_window_summary.txt`, `inverse_window_adjust.txt`.
Setup:
* D(n) is the sup-discrepancy of {x̄/n : x ≤ N, (x, n) = 1}, with N = ⌊log²p⌋ fixed **at the hard prime's value** for the
  prime and all its controls.
* Hard set: all **14** (★)-zero primes p ≡ 1 (4) ≤ 10⁷, recomputed by direct enumeration (409, 577, 5569, 9601, 23929,
  83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281, matching FRONTIER's count of 14 ≤ 10¹⁰);
  the three b = 1 failures; 3361; and 5 101 441. That is 19 primes.
* Controls: up to 200 nearest (two-sided) primes ≡ 1 (24), odd squares, and near-square primes, all inside [p/2, 2p]. For
  p < 10⁴ there are few controls (4–156), so those rows are weak.

Results:
* Rank among the prime controls: P(D_c ≥ D) ≤ 0.15 for **9 of 19** hard primes: 83449 (0.075), 329617 (0.115), 712321
  (0.065), 1726201 (0.000), 8813281 (0.015), 2521 (0.000), 66529 (0.050), 3361 (0.068), 5101441 (0.135). Under the null,
  about 2.9 are expected.
* Several hard primes have *low* D: 5212561 (rank 0.910, D = 0.038, below the F2b mean 0.067), 409, 577, 23929 and
  1724209. **The effect is heterogeneous, not a property of hard primes as such.**
* Odd squares have higher D than primes at equal N: n − 1 = (m − 1)(m + 1) is divisible by many small x, and coprimality
  thins the sample.
* A linear adjustment of D for t = #{x ≤ N : x | p − 1} + #{x ≤ N : x | p + 1}, fitted on the prime controls with the same
  N, leaves mean residual z = +0.68 over the 19 (Σz/√19 = 2.95).

*F2b: large sample (EVIDENCE).* `scripts/z53_lit_invwin_census.c` computes R(p) by direct enumeration of all
4uBC − u − B ≤ X, and D, for all 64 380 primes p ≡ 1 (24) in [2·10⁶, 10⁷]. Output `data/z53/lit/invwin_2e6_1e7.tsv`;
analysis `scripts/z53_lit_invwin_analyze.py` → `data/z53/lit/invwin_analysis.txt`. The census reproduces the two (★)
zeros ≡ 1 (24) in range, 5 212 561 and 8 813 281. The hostile reviewer re-checked R against brute force at 143 small
primes. Let y = R/log²p.
* Pearson corr(y, D) = −0.167 (Spearman −0.147).
* Covariates: t₋, t₊, #{primes ℓ ≤ 47 dividing p − 1}, indicators p ≡ 1 mod 8, 5, 7, 11, 13, and log p. They explain
  R² = 0.48 of var(D) and 0.12 of var(y).
* Partial correlation of y and D given the covariates: **−0.019** (p = 1.3·10⁻⁶; Spearman of residuals −0.025). The
  squared-correlation ratio is 0.013; the residual covariance is 7.7 % of the raw covariance.
* The top 1 % of residual D have mean y = 0.1348, against 0.1427 for the rest.
* Near-square primes (|p − m²| ≤ 100, n = 2858) have mean y 0.1393 vs 0.1428, and mean D 0.0696 vs 0.0671. Adding a
  near-square indicator leaves the partial correlation of y and D at −0.019. The near-square coefficient in y ~ covariates
  + near-square + D is −0.0035, essentially unchanged by D. So in this sample D and near-square proximity carry nearly
  independent (and both small) information about y.

*Reading (EVIDENCE).* On log² windows, the correlation between inverse discrepancy and (★)-hardness is mostly shared with
small-divisor data of p ± 1, the residue-class effect already modelled in `RESIDUE_HARDNESS.md`. A small residual
association remains. No mechanism is identified, and none is claimed. The GS phenomenon does not look like a new lever
for (★) at this scale.

### 6.4 The (J)103 test: every-n theorems with small witness counts (Assessment, with verified items)

| theorem (every n / every p in a class) | expected witnesses at n | unconditional? | mechanism | consistent with (J)103? |
|---|---|---|---|---|
| p ≡ 1 (4) ⇒ p = x² + y² (Fermat; Thue/Brillhart pigeonhole; Zagier) | r₂(p) = 8 (constant) | yes | M1b thick lattice / R rigidity / M5 | yes, *if* (J)103 excludes T/R (the repo's z52 opus catalogue row β′ already lists r₂(p) = 8) |
| idoneal forms x² + ny², one class per genus | O(1) | yes | R (genus = class) | same |
| Chebyshev: n has a prime non-divisor ≤ (1 + o(1)) log n; Sylvester–Schur; Bang–Zsigmondy primitive divisors | ≍ log n / log log n; ≍ log n | yes | size/valuation squeeze (z52 opus row μ) | yes (structural). Witness events are non-divisibility or primitive-divisor events, so failure forces an impossible size. ES's witness events are divisibility events, whose joint failure has positive CRT density for any fixed finite menu (B1), so no size squeeze is known |
| least QNR ≤ (log p)² (GRH; Lamzouri–Li–Soundararajan Cor 1.1, repo); least QNR ≪ (log p)⁸ *if* the OAI-003 quasi-RH claim holds (`OAI_DUMP_IMPACT.md`; `BREADTH_Z45.md` §10) | ≍ (log p)² resp. (log p)⁸ non-residues in the window | GRH / claimed | M2 fixed-modulus character | yes, *if* (J)103 excludes M2. If OAI-003 is accepted, this becomes an **unconditional** natural every-p theorem with a polylog window (M2) |
| Korobov / MMS 2212.14646: a/q with partial quotients O(log q / log log q) | power of q | yes | M1a | yes |
| Zaremba (Zhang, Shkredov) | q^{2w_M−1} (power) | claimed | M1a + expansion | yes |
| EOS under QRH, third prime ≤ (log q)⁴ (BS 2610.19597 Thm 1.3) | power (ℓ₁, ℓ₂ ≤ q) | QRH | M1a | yes |
| Erdős–Tetali / Kolountzakis thin bases | ≍ log n | yes | M4 (designed set) | yes (repo s9 table) |
| p + 2^a + 2^b, Markoff k, xyz − x − y − z (repo sibling) | ≍ log n, (log k)² | — | — | natural polylog problems **with** infinitely many exceptions (repo) |

**Proposed precise wording of (J)103** (Assessment; replaces "no every-n theorem … with a polylog main term for any natural
problem"):
> No every-n theorem is known, for a natural problem, whose expected number of witnesses at n is (log n)^{O(1)} and whose
> proof does not rest on one of:
> * (T) a thick auxiliary object of size n^c with an exact extraction rule (Thue lattice, Zaremba reservoir);
> * (R) algebraic rigidity or a size/valuation squeeze (class-number one, Zsigmondy, Chebyshev);
> * (M2) a fixed-modulus character or group event (least non-residue under GRH);
> * (M4) a designed set.
>
> For ES's (★) event no sufficient mechanism of these kinds is known: no thick object with an exact extraction rule,
> no rigidity or squeeze, and a modulus tied to the solution. (The modulus is fixed only in continued-fraction
> coordinates, where M1 fails: FRONTIER §3 M-table.)

The 2026 literature checked here adds no counterexample. The nearest new items are MT 2605.27833 (class-level, but free n
and a power scale) and BS 2610.19597 Thm 1.3 (a polylog variable, but a power count).

### 6.5 Zaremba transfer — see §5(g), Remark Z (PROVED) plus Assessment.

### 6.6 EOS as a calibration for "two-modulus" representations (Assessment, analogy only)

The literal "two-modulus" target for target 5 would be: for every p, the class 1 mod 4p contains a product xy with
x ≡ y ≡ −1 (mod 4C), where C = (xy − 1)/4p. This is (★) itself. Dropping the tie (fixed m instead of 4C) gives a
fixed-modulus representation question mod lcm(4p, m). Its closest literature relative is EOS (two primes, every class,
ℓ_i ≤ q), which is open even under GRH (Banks); the three-prime version is a theorem with power counts (MT, BS). EOS is
*not* a relaxation of (★): primes are a restriction, and EOS quantifies over every class with size bounds. **No reduction
in either direction is claimed.** The calibration is only this:
* the closest proved representation theorems need free primes, power-size counts and a fixed modulus;
* (★) has none of the three;
* no literature statement was found that keeps even one of them.

---

## 7. Verdict

**Narrowed** (Assessment). For the stated questions: about 60 abstracts were triaged and about 50 papers read in full
text; the rest were discarded by title or abstract. No literature item found supplies B2, a fixed-p cancellation for the
height-tied hyperbola, or a pointwise divisor-in-class lower bound.

Scoped statements obtained:
* (PROVED, L1) length-independent fixed-modulus bilinear Kloosterman bounds give box asymptotics beyond Weil only if the
  saving exponent exceeds 1/4. Even perfect orthogonality stops at area q^{4/3}. The new general-modulus Pascadi bound
  has η = 1/700.
* (PROVED, L2) inverse statistics on windows are functions of p mod lcm(1..N), a growing family. (EVIDENCE, F2) their
  correlation with (★)-hardness is mostly shared with small-divisor covariates of p ± 1; it is heterogeneous across hard
  primes; and it is nearly independent of the near-square deficit.
* (PROVED, Remark Z) a Zhang-type incidence estimate certifies existence only when the expected count exceeds the modulus.
* (Assessment) the representation-theorem literature (EOS) offers no statement that keeps the tie, the polylog count or
  "divisors of one integer".

What survives:
* cancellation methods outside L1's scope (length-dependent bilinear bounds; one short variable at a *fixed* residue,
  where no current tool exists);
* the GS Linnik-lcm template, as a kill-side instrument for HCSHIFTS;
* (J)103, in the repaired wording of §6.4.

## 8. FRONTIER §4 hard screens for the best items found (Assessment)

| item | T1 (fails at odd squares?) | 8/131 (numerator-specific?) | tied modulus | fixed p |
|---|---|---|---|---|
| Pascadi bilinear Kloosterman (as a §7.1 tool) | no: the theorem (with its gcd restriction) applies to any modulus, including 4m²; it carries no quadratic-character input | no: numerator-blind | **fails**: it controls bilinear forms mod a fixed modulus; the height tie is not seen; L1 caps even box counts | passes (pointwise in the modulus) |
| MT "Linnik for multiplicative functions" (as a §7.3 model) | its exceptional alternative is real-character pretentiousness, an *analogy* to T1, not an identification | n/a | **fails**: free n, not divisors of a tied integer | passes (every q, a) |
| GS Linnik-lcm construction (as a kill-side tool for §7.2) | n/a | n/a | n/a | n/a: it constructs existentially chosen p, it is not a statement at a prescribed p |
| EOS-type product theorems (target 5) | no (hold for every modulus) | no | **fails**: free primes, fixed modulus | passes |

None passes all four. That is expected for literature tools; the table records which screen each would need to beat.

## 9. Proposed FRONTIER text (do not apply here; for the parent)

*§7.1, append:*
> (z53 LIT, `Z53_LIT.md` §6.1) Pascadi arXiv:2511.08445 bounds bilinear Kloosterman sums S(am, n; c) with arbitrary
> coefficients for every modulus (saving c^{1/700}; for bounded α, with (n, c) = 1, c^{1/276}). For the specific argument
> "Poisson in both variables + a length-independent bilinear bound ‖α‖‖β‖q^{1−η}", modular-hyperbola box asymptotics
> beyond Weil need η > 1/4. Even the perfect-orthogonality bound stops at area q^{4/3} (PROVED, elementary). Garaev–Shparlinski
> arXiv:2304.07953 Thms 1.3–1.4: for some p, sums of e_p(a x̄) over x ≤ N admit no square-root cancellation at
> N ≤ exp((log p)^{1/3}). The DFI improvement arXiv:2601.00292 is withdrawn.

*§7.2, append:*
> (z53 LIT §§0, 6.2–6.3) Unconditional kill-side template: Garaev–Shparlinski arXiv:2304.07953 Thm 1.1 picks p ≡ −1
> (mod lcm of the N^{1/A}-smooth s ∈ [N, 2N]) with (log p)^A ≍ N, controlling a ρ(A) fraction of a polylog window by
> congruences (the class −1 itself makes (★) easy; a kill needs another class). Inverse statistics on windows are functions
> of p mod lcm(1..N) (x̄/p = k_x/x + 1/(xp), k_x ≡ −p̄ mod x; PROVED). Their correlation with (★)-hardness (r = −0.17 over
> 64 380 primes in [2·10⁶, 10⁷]) drops to −0.02 after small-divisor covariates of p ± 1 (EVIDENCE).

*§3 M-table / §1:* replace the (J)103 sentence by the §6.4 wording. *Add to the M2 row:* "If the OAI-003 quasi-RH claim is
accepted, least-QNR ≪ (log p)⁸ becomes an unconditional M2 instance."

*§7.4, append:*
> Human write-ups of the OpenAI no-Siegel-zero claim (Banks arXiv:2610.15483: (1 − β) log q ≥ 3·10⁻³ for all real zeros,
> all q ≥ 3; Kerr arXiv:2610.21099; Guo arXiv:2610.30476; unrefereed) concern real zeros only. They do not give the fixed
> zero-free strip that LOWERTAIL_DEEP_ASTRA Thm 5.4 needs.

*Target 5 / §6, append:*
> EOS (every reduced class mod q is ℓ₁ℓ₂, ℓ_i ≤ q) is open even under GRH (Banks arXiv:2609.37434 p. 1). As an analogy
> only (no reduction), product/representation routes to B2 have no literature statement that keeps the tie, the polylog
> count or "divisors of one integer" (`Z53_LIT.md` §6.6).

*LITERATURE_2026.md:* add a "Wave z53 additions" block from §5 (the items marked new, with the corrections of §10).

**One-paragraph bottom line.** A verified 2020–2026 sweep (118 arXiv queries, 587 records, about 60 abstracts triaged,
about 50 papers read in full text, plus erdosproblems #242 and GitHub/Lean sources) found no tool that controls the class
of a divisor of one p-tied integer, and no new ES result after Cao–Xu (2026-10-23). The new tools are:
* a general-modulus bilinear Kloosterman bound (Pascadi);
* unconditional polylog-window inverse obstructions (Garaev–Shparlinski);
* a class-level "only a real-character exception" theorem for multiplicative functions (Matomäki–Teräväinen);
* EOS progress (Matomäki–Teräväinen, Banks–Shparlinski);
* human write-ups of the no-Siegel-zero claim.

Each is averaged, power-scale with free objects, or, for the specific arguments analysed (L1, Remark Z), structurally
unable to reach the height-tied event. The lane's mathematical output is negative but sharp:
* L1: length-independent bilinear fixed-modulus bounds need η > 1/4 to beat Weil on hyperbola boxes, and perfect
  orthogonality stops at area q^{4/3};
* Remark Z: Zhang-type incidence estimates need an expected count above the modulus;
* L2 + F2: inverse-window discrepancy tracks (★)-hardness only weakly beyond p ± 1 small-divisor data;
* (J)103 survives once worded as "no polylog every-n theorem without a thick object, rigidity/squeeze, an M2 character
  event or a designed set".

## 10. Review record

**Hostile review (deep-mode subagent, 2026-11-01; no edits by the reviewer).** 17 items: 16 MAJOR, 1 MINOR, no FATAL.
The reviewer independently re-checked the C census against brute force at 143 small primes and 7 large primes, reproduced
the F2b numbers, re-opened the priority sources, the 2601.00292 withdrawal notice and the latest-ES arXiv query. All
items were addressed in this version:
1. L1 dropped fixed powers q^{ε}: the truncation is now at q^{1/2}, norms come from Fourier decay, and the Weil part sums
   the gcd factor over d | q. Axis terms are bounded explicitly.
2. L1 overstated its scope: the claim is now scoped to "Poisson + length-independent BB(η)". The perfect-orthogonality
   benchmark (Pascadi p. 2) is quoted, and the false "square-root cancellation = η 1/2" remark is replaced by the
   perfect-orthogonality remark (area q^{4/3}).
3. Pascadi was misquoted: the page is now p. 3, the (n, c) = 1 restriction and the √M‖β‖ form are given, and stronger
   prime/interval results (KMS, Blomer–Pascadi) are acknowledged. The "69× too small" comparison is removed.
4. L2 overclaimed a B1 kill: removed. lcm(1..N) ≫ p is now stated explicitly.
5. The Farey wraparound case e = x + 1 is fixed (fractional part; example p = 5, x = 3); the shift is now ≤ 1/p, and the
   stability claim is restricted to Lipschitz statistics.
6. The MT exception condition is corrected to Σ_{p≤q^{1/3}, h(p)χ(p)<0} 1/p ≤ c/q^{ε/100}, verified with pdftotext.
7. The EOS "harder than / relaxation" language is removed; EOS is now an analogy only (§0 item 3, §4, §6.6, §9).
8. F2a omitted the known zero 5 212 561 and miscounted ranks: the hard set now has all 14 (★)-zeros ≤ 10⁷ (recomputed),
   ranks are unrounded, and low-D hard primes are reported.
9. F2a used inconsistent windows: controls now use the hard prime's N, rows store the control's own coprime count, and
   the adjustment uses the same N.
10. Controls were unmatched: they are now the nearest two-sided controls in [p/2, 2p], with counts reported. The
    near-square interpretation now uses F2b, where R is measured.
11. "99 % explained" was an overinterpretation: replaced by the defined correlations (raw, partial, squared ratio,
    covariance ratio) with no causal wording.
12. Banks–Shparlinski quantifiers (ℓ fixed, γ large) are added.
13. "First unconditional …" is deleted; the (J)103 wording now says "no known sufficient mechanism", with the
    CF-coordinate caveat.
14. The Zaremba deficit argument is replaced by the PROVED Remark Z, about the shape of the estimate, plus an explicit
    Assessment.
15. §8 now distinguishes theorem scope, existential construction and screen performance.
16. A label convention is added (§0) and mixed labels are split (§6.3, §7).
17. Coverage wording is "none found"; the GS proof excerpt anchor is fixed (`excerpts_lane.txt`); the MT condition and the
    DRZ withdrawal text are appended there.

A cross-model review is expected next; this section will record its fixes.
