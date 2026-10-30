# z52 literature lane L5 — thin pointwise existence

## §0 Summary
- **Genuinely new since 2026-09-28:** Li–Liu (arXiv:2610.15784, 11 Oct 2026): 6 powers of 2 unconditionally, 5 under GRH, with two primes; Ding–Li–Li (arXiv:2607.03662): positive density for P₂+aᵃ.
- **Verified thin-prime literature:** F-I x²+y⁴; Heath-Brown x³+2y³; Heath-Brown–Moroz; Maynard restricted digits; Pratt; Green–Sawhney p²+nq²; Merikoski n²+1 and aX²+bY³.
- **Structural features:** family averaging/Type I–II Fourier decorrelation; power-sized Goldbach or class-number representation reservoirs; fixed-modulus character control.
- **Does ES share them?** Not the decisive feature: ES has ≍log²p tied, moving-modulus events (B2/B6), with no power-size supply.
- **Verdict change:** None. No verified universal theorem with polylog witnesses and no local obstruction transfers to ES. Source-access gaps are listed in §4.

## §1 Verified entries

### Green–Sawhney: primes p²+nq²

Ben Green and Mehtaab Sawhney, “Primes of the form p²+nq²,” arXiv:2410.04189 v3 (6 June 2026; submitted 5 October 2024), accepted for *Acta Mathematica*. Abstract, accessed 2026-10-30: for each n ≡ 0 or 4 (mod 6), infinitely many primes p²+nq² with p,q prime, and an asymptotic count; n=4 proves the Friedlander–Iwaniec Gaussian primes conjecture. The method uses Type I/II sums over Q(√−n), with recent Gowers-norm inputs for Type II. Status: accepted preprint. Excerpt: `sources/z52/thin_pointwise/green_sawhney_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`, `BRAINSTORM/z31_small_count_pointwise.md` found by `git grep`; result counts a family of prime variables, not witnesses to each prescribed integer, so no B6 transfer.

### Merikoski: primes ax²+by³ (2025)

Jori Merikoski, “On primes represented by aX²+bY³,” arXiv:2503.05396 v1, submitted 7 March 2025. Abstract, accessed 2026-10-30: for coprime positive a,b, *conditionally* on a conjecture about Hecke eigenvalues along binary cubic forms, an asymptotic for primes ax²+by³ with x≤X^(1/2), y≤X^(1/3). Status: preprint, conditional theorem. Excerpt: `sources/z52/thin_pointwise/merikoski_ax2_by3_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`; family average under an explicit unproved input, not universal n representation.

### Merikoski: large prime factor of n²+1

Jori Merikoski, “On the largest prime factor of n²+1,” arXiv:1908.08816 v3 (2 November 2020; submitted 23 August 2019). Abstract, accessed 2026-10-30: infinitely often the largest prime factor of n²+1 exceeds n^1.279; under Selberg's eigenvalue conjecture, exponent 1.312. It highlights Type II estimates, Harman's sieve, and Kloosterman-sum bounds. Status: preprint v3. Excerpt: `sources/z52/thin_pointwise/merikoski_arxiv.txt`. Relation: `BRAINSTORM/z45_recent_pointwise_tools.md` and `BRAINSTORM/z31_small_count_pointwise.md`; subsequence large-factor result, not every-n prime/witness result.

### Friedlander–Iwaniec: primes x²+y⁴

John Friedlander and Henryk Iwaniec, “The polynomial X²+Y⁴ captures its primes,” arXiv:math/9811185 v1 (1 November 1998), published *Annals of Mathematics* 148 (1998), no. 3, 945–1040. Abstract, accessed 2026-10-30: infinitely many primes a²+b⁴; moreover a weighted asymptotic of order x^(3/4). Status: published. Excerpt: `sources/z52/thin_pointwise/friedlander_iwaniec_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/s8_volume_dfi.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`; the volume/counting theorem has no prescribed-target conclusion (B6).

### Heath-Brown: primes x³+2y³

D. R. Heath-Brown, “Primes represented by x³+2y³,” *Acta Mathematica* 186 (2001), 1–84. Oxford repository record and linked article opened 2026-10-30; Theorem 1: infinitely many primes of this form, x,y integers. Status: published. Excerpt: `sources/z52/thin_pointwise/heath_brown_cubic_ora.txt`. Relation: `BRAINSTORM/technique_transfer_list.md` and `BRAINSTORM/z45_recent_pointwise_tools.md`; family-level infinitude does not force an individual n.

### Heath-Brown–Moroz: primes represented by cubic forms

D. R. Heath-Brown and B. Z. Moroz, “Primes represented by cubic forms,” 2002. Oxford repository record and linked paper PDF opened 2026-10-30. Theorem 1.1: every admissible integral binary cubic form represents infinitely many primes. Status: published paper. Excerpt: `sources/z52/thin_pointwise/heath_brown_moroz_ora.txt`. Relation: `BRAINSTORM/technique_transfer_list.md` and `BRAINSTORM/z45_recent_pointwise_tools.md`; again an infinitude over the form's values, not every target integer.

### Pratt: primes from two squares with missing digits

Kyle Pratt, “Primes from sums of two squares and missing digits,” arXiv:1806.02699 v1 (7 June 2018), related DOI 10.1112/plms.12307. Abstract, accessed 2026-10-30: asymptotic count of primes p=m²+ℓ² where ℓ omits any three fixed decimal digits. Status: published journal article (DOI metadata) and arXiv preprint. Excerpt: `sources/z52/thin_pointwise/pratt_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`; thin-family count, no B6 pointwise implication.

### Maynard: primes omitting a fixed decimal digit

James Maynard, “Primes with restricted digits,” arXiv:1604.01041, v2 (28 October 2019; submitted 4 April 2016). Abstract, accessed 2026-10-30: for each decimal digit, infinitely many primes omit that digit. The paper describes this as a Hardy–Littlewood circle-method binary problem; the abstract points to Type I/II information for Harman's sieve and decorrelation of the Fourier-large conditions for primes and restricted-digit numbers. Status: preprint (arXiv page; abstract verified), no individual prescribed integer is represented. Excerpt: `sources/z52/thin_pointwise/maynard_restricted_digits_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`, and `BRAINSTORM/z31_small_count_pointwise.md` found by `git grep`; the theorem is family-level, so its minor-arc machinery does not supply B6's single-p main-term dominance.

### Heath-Brown–Puchta: primes plus powers of two

D. R. Heath-Brown and J.-C. Puchta, “Integers Represented as a Sum of Primes and Powers of Two,” arXiv:math/0201299, v2 (2 April 2002; submitted 30 January 2002), published in *Asian Journal of Mathematics* 6(3) (2002), 535–565. arXiv abstract, accessed 2026-10-30: every sufficiently large even integer is a sum of two primes and exactly 13 powers of 2; under GRH, 13 can be replaced by 7. Source identifies the key analytic input as bounding the measure of the set where the powers-of-two exponential sum is large. Status: published; source excerpt in `sources/z52/thin_pointwise/heath_brown_puchta_arxiv.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md` already records the theorem; this source check confirms it, without changing the verdict that the Goldbach component supplies a power-size count (barrier B6 / FRONTIER §3), unlike ES's polylog count.

### Li–Liu: Linnik–Goldbach with six powers of two (new 2026 preprint)

Huixi Li and Zhixin Liu, “6 powers of 2 in the Linnik–Goldbach problem,” arXiv:2610.15784 v1, submitted 11 October 2026. Abstract and full HTML opened 2026-10-30: Theorems 1.1–1.2 state every sufficiently large even integer is a sum of two primes and six powers of 2 unconditionally, and five powers under GRH. The full paper combines circle-method estimates, dyadic-sum large deviations, and a quadratic-form optimization over representation counts. Status: preprint. Excerpt: `sources/z52/thin_pointwise/linnik_goldbach_six_arxiv.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; this is genuinely new since the cutoff and improves K=8, but remains powered by the Goldbach pair main term (not an ES-type polylog-only existence proof).

### Pintz–Ruzsa: Linnik–Goldbach with eight powers of two

J. Pintz and I. Z. Ruzsa, “On Linnik’s approximation to Goldbach’s problem. II,” DOI 10.1007/s10474-020-01077-8, *Acta Mathematica Hungarica* 161 (2020), 569–582 (published 22 July 2020). Abstract, accessed 2026-10-30: every sufficiently large even integer is a sum of two primes and K=8 powers of two, unconditionally. Status: published. Excerpt `sources/z52/thin_pointwise/pintz_ruzsa_2020.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; this is pointwise but has a power-sized two-prime supply, not a polylog-only mechanism.

### Romanoff positive density; Erdős covering failures; Tao partial covering

Romanoff's 1934 theorem, as explicitly cited and stated in Ding–Li–Li, “A Romanoff-type theorem for P₂+{aᵃ:a≥1},” arXiv:2607.03662v1, §1 (accessed 2026-10-30): the set {p+2^k} has positive lower density. The same source states Erdős 1950's covering result: an arithmetic progression of common difference 11,184,810 whose terms are not p+2^k. This corrects my earlier cautious note: the exact p+2^k failure claim is supported by this source. It is secondary verification; Romanoff's and Erdős's originals not opened. Tao's arXiv:0802.3361v4 §1 separately records Erdős and Cohen–Selfridge prime-power covering variants and proves Theorem 1.2: a positive proportion of primes avoid a growing logarithmic family of digit modifications, via partial covering then Selberg sieve. Status: sources accessed today, historical claims secondary, Tao's theorem primary. Excerpts: `sources/z52/thin_pointwise/erdos_covering_tao_arxiv.txt`, `sources/z52/thin_pointwise/ding_romanoff_2026.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; shows fixed-orbit covering failures / positive-density results, not a direct ES transfer (B1/B6).

### Croot: Erdős–Graham coloring theorem for unit fractions

Ernest S. Croot III, “On a coloring conjecture about unit fractions,” arXiv:math/0311421 v1 (24 November 2003), *Annals of Mathematics* 157 (2003), no. 2, 545–556. Abstract, accessed 2026-10-30: for some b>0, every r-coloring of [2,br] has a monochromatic set S with Σ_{n∈S}1/n=1. Status: published. Excerpt `sources/z52/thin_pointwise/croot_arxiv.txt`. Relation: `BRAINSTORM/addcomb_unit_fraction_density.md`, `BRAINSTORM/technique_transfer_list.md`; theorem is coloring-forcing, not a statement about every prescribed target n.

### Bhargava–Hanke: 290 theorem

Manjul Bhargava and Jonathan Hanke, “Universal quadratic forms and the 290-Theorem,” authors' 16-page preprint PDF, opened 2026-10-30. Theorem 1: a positive-definite integer-coefficient quadratic form representing the 29 listed critical integers up to 290 represents all positive integers. Theorem 2 establishes necessity of each test integer. Status: published in *Annals of Mathematics* (2005). Excerpt `sources/z52/thin_pointwise/bhargava_hanke_290.txt`. Relation: `BRAINSTORM/z31_quadratic_forms.md`, `BRAINSTORM/technique_transfer_list.md`; this is a finite criterion for a form being universal, not a sparse per-n witness theorem.

### Blomer: ternary forms and restricted three-square variables

Valentin Blomer, “Ternary quadratic forms, and sums of three squares with restricted variables,” in *The Anatomy of Integers*, CRM Proc. Lecture Notes 46 (2008). Author abstract PDF opened 2026-10-30: survey of positive integral ternary forms, improved uniform asymptotic formulas for representation counts, and Gauss-type three-square results with almost-prime, squarefree, or smooth variables. Status: published chapter; abstract only verified here, precise theorem hypotheses not extracted. Excerpt `sources/z52/thin_pointwise/blomer_abstract19.txt`. Relation: `LITERATURE_AUTOMORPHIC.md` §§ Blomer and `BRAINSTORM/z31_quadratic_forms.md`; not an every-n theorem absent additional hypotheses.

### Ding–Li–Li: 2026 Romanoff-type positive-density result

Yuchen Ding, Huixi Li, and Junfeng Li, “A Romanoff-type theorem for P₂+{aᵃ:a≥1},” arXiv:2607.03662 v1, submitted 4 July 2026. Abstract, accessed 2026-10-30: with P₂={m:Ω(m)≤2}, P₂+{aᵃ:a≥1} has positive lower density; the argument uses a Romanoff second moment and bounds an average singular factor. Status: preprint. Excerpt `sources/z52/thin_pointwise/ding_romanoff_2026.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md` and `BRAINSTORM/technique_transfer_list.md`; this is a genuinely recent family-density result, not every n and not evidence for a fixed-n polylog witness theorem.

## §2 Structural-feature table

| Problem / verified status | Expected witnesses at fixed n (heuristic where stated) | Mechanism; pointwise scope | ES comparison / transfer |
|---|---|---|---|
| Friedlander–Iwaniec, primes a²+b⁴ | Family count ∼ x^(3/4); not fixed-target n. | Weighted asymptotic over (a,b), sieve/dispersion. Infinitely many represented primes. | No prescribed target; family count only (B6). |
| Heath-Brown, primes x³+2y³ | Family count; no per-target assertion. | Binary cubic form/cubic field methods; infinitely many primes. | No single-n dominance; no transfer. |
| Heath-Brown–Moroz, admissible binary cubic forms | Family count; no per-target assertion. | Generalizes cubic-form prime infinitude. | Same B6 mismatch; no transfer. |
| Maynard, primes missing a digit | Positive infinitude, no prescribed integer. | Circle method + Type I/II sieve; decorrelates prime and digital Fourier large spectra. | No; `technique_transfer_list.md`, `z45_recent_pointwise_tools.md`; family-only. |
| Pratt, restricted-coordinate sum of two squares primes | Asymptotic over p=m²+ℓ² with ℓ digit-restricted; no fixed-target count. | F-I plus Maynard ideas. | No; family average. |
| Green–Sawhney, p²+nq², p,q prime (n≡0,4 mod 6) | Asymptotic family count; not prescribed n. | Type I/II in Q(√−n), Gowers norm inputs. | No; family result (B6). |
| Merikoski, P(n²+1)>n^1.279 | Infinitely many n; at such n at least one large prime factor, not a prime value. | Type II estimate + Harman sieve, Kloosterman bounds. | Not an every-n witness theorem; no transfer. |
| Merikoski, primes ax²+by³ (a,b coprime) | Asymptotic count over x,y in boxes; no fixed-target statement. | Conditional on Hecke-eigenvalue conjecture; sieve, quadratic forms, GL(2) spectrum. | Conditional family average; no ES pointwise conclusion. |
| Heath-Brown–Puchta, two primes + 13 powers (2002) | Per target, Goldbach pair reservoir has expected scale ≍ n/log²n; powers add ≍log^13 n choices before coincidences/singular factors. | Every sufficiently large even n; circle method + powers-of-two exponential-sum large-deviation bound. | No: power-size supply vs ES ≍log²p events (B2/B6). `z31_small_count_pointwise.md`. |
| Li–Liu, two primes + 6 powers (2026); 5 under GRH | Same power-size two-prime reservoir; not polylog-only. | Every sufficiently large even n; circle method, major/minor arcs, dyadic-sum large deviations, representation-count quadratic form. | New result, but no ES-like sparse-witness mechanism (B6). |
| Pintz–Ruzsa, two primes + 8 powers | Same power-size reservoir. | Every sufficiently large even n, unconditional; theorem verified from published abstract. | Same: doesn't bridge B2. |
| Linnik: two primes + bounded K powers | K unspecified in original theorem; expected representation count has a power-size Goldbach factor. | Every sufficiently large even n. | No; not one-prime-plus-powers. One-prime phrasing in the brief is not supported by the sources checked. |
| Gallagher / Linnik–Gallagher almost-all regime | For p₁+p₂+2^k, about log n power choices × n/log²n prime-pair supply (heuristic). | Almost-all or density theorem depending on precise cited result; full source statement NOT independently checked here. | Doesn't address polylog-only single-n. |
| n=p+2^k; Romanoff | Expected count ≍ Σ_{k≤log₂n}1/log n=O(1); positive lower density of represented n, not every n. | Romanoff second moment proves positive density; Erdős covering construction gives an AP of failures (verified in Tao secondary source). | Failure analogy, not a transfer; fixed-modulus periodic orbit unlike ES. B1. |
| n=p+2^k+2^ℓ | Expected witnesses ≍ log n (two exponent choices divided by prime density factor log n). | No every-n theorem verified; Linnik–Gallagher cited for almost all only. | Example in the prompt is an intermediate O(log n) scale; no ES transfer, and theorem scope must not be promoted to every n. |
| Sierpiński / Riesel k2^m±1 | For fixed k, one candidate per m; covering produces no prime values at all, rather than a prescribed n witness. | Finite prime-divisor covering; 78557 Sierpiński and 509203 Riesel are standard examples. | Same periodic-covering obstruction, irrelevant at ES primes. |
| Croot, Erdős–Graham coloring theorem | Number of unit-fraction solutions depends on coloring/range; not a statement about each target n. | For every r-coloring of [2,br], a monochromatic set has reciprocal sum 1 (arXiv abstract). | Different combinatorial forcing structure; no ES single-prime analogue. |
| Four squares, r₄(n) | ≍ n up to singular factors; power-size witnesses. | Every positive n by Lagrange; Jacobi formula counts representations. | Yes only in the trivial sense of abundant count; ES has no such power reservoir. |
| Three squares, r₃(n) | For admissible n, order ≍√n times class/L-value factors (not uniformly a bare constant); local obstruction exactly n=4^a(8b+7). | Gauss–Legendre: every admissible n; class-number / genus arithmetic. | No local obstruction for ES hard primes, but count scale differs radically. |
| Three triangular numbers | Via 8n+3 as a sum of three odd squares, ≍√n representations in the associated ternary form. | Every n (Gauss); inherited three-square identity. | Same class-number-size reservoir, not shared by ES. |
| Duke–Schulze-Pillot ternary positive forms | Representation numbers typically scale like √n times local/class factors; theorem is not an unconditional assertion for every locally represented n without spinor-exception qualifications. | Equidistribution of lattice points / cusp-form bounds; excludes spinor-exception square classes in its standard application. | No; ES has only polylog events and tied moving moduli (B2/B6). Prior `z31_quadratic_forms.md`. |
| Bhargava–Hanke 290 theorem | Not a witness-count theorem: finitely many 29 test values decide universality of a quadratic form. | Universal form represents all integers iff it represents critical set; proved via escalation, local densities, modular forms, finite computation. | Formal finite testing rather than per-n witness; no transfer. |
| Blomer, ternary forms / restricted three squares | Representation counts over n with uniform asymptotics; Gauss-type almost-prime/squarefree/smooth coordinates; not every prescribed n by itself. | Weight-3/2 theta series, subconvexity, ternary-form representation analysis (author abstract opened). | Count asymptotics do not overcome B2; not a new candidate. |
| Least prime in AP (Linnik–Xylouris) | Least witness bounded by q^5 (Linnik exponent L=5); count in search interval is a power-window, not polylog. | Zero-free region / Dirichlet L-functions, pointwise for each reduced residue class. | Fixed modulus, power scale; partial analogy only. B2 has moving modulus. |
| Least quadratic nonresidue (Burgess) | Unconditional least witness ≪ p^(1/(4√e)+ε); GRH gives O(log²p). | Burgess short character sums; GRH via L-functions. | Character value is analogous, but ES needs divisor in moving residue class; B2/F3. |

Count labels caveat: “expected” counts are heuristic local-density estimates, not source theorems; asymptotic statements above are recorded only where the cited paper proves them. The brief's “every n is prime + bounded powers of two” conflation is rejected: verified Linnik/HBP/Pintz–Ruzsa statements use **two** primes.


## §3 Dichotomy and NEW candidates

### What fails, what succeeds, what lies between

| Witness scale at one target | Examples checked | Status / mechanism |
|---|---|---|
| O(1) expected witnesses; covering failures | n=p+2^k; Romanoff-positive-density set versus Erdős AP of failures | Demonstrates positive density can coexist with an infinite arithmetic progression of failures; fixed-modulus covering controls the exponent orbit. Not every n and not ES-like divisor events. |
| ≍log n expected witnesses; covering failures | n=p+2^k+2^ℓ (heuristic count) | Finite coverings are known for one power orbit, but no source-verified theorem here gives an AP of failures for precisely the two-power-plus-prime equation. Do not infer one. Linnik–Gallagher results are almost-all/density, not universally established by these sources. |
| Power-size witness reservoirs; every n | Two primes + K powers of 2; 4 squares; suitable three-square/ternary-form representation counts | Success supplied by Goldbach/representation main term or class-number-scale count. Analytic circle method / local-global quadratic-form theory, not O(log n) event control. |
| Polylog at each n, no local obstruction, universal theorem | No verified example found | This is the crucial gap. The closest positive-density/power-orbit and fixed-character cases do not settle every target. ES's ≍log²p count is intermediate in size but has tied moving moduli (B2), and no theorem found turns it into pointwise existence. |
| Polylog but only almost-all / positive-density targets | Romanoff p+2^k; Ding–Li–Li P₂+aᵃ; Maynard/F-I/Green–Sawhney prime families | Averaging over targets or a growing family supplies the mass; this cannot be transferred to each n (B6). |
| Fixed-modulus character witness, conditional pointwise | Least QNR under GRH; least prime in AP with fixed q | L-function zero control yields log-scale windows; ES's modulus moves with the certificate, so only partial analogy (B2/F3). |

No NEW candidate. The October 2026 Li–Liu advance (K=6 unconditional, K=5 under GRH) is a genuine new literature update but retains the two-prime main term; it changes the state of the comparison, not the ES transfer verdict. The July 2026 Romanoff-type theorem similarly adds a fresh positive-density model of correlated sparse shifts, not a fixed-n theorem. A concrete next test, if pursuing the sparse-shift analogy, is to quantify whether the ES certificate parameter set has any analogue of the mean singular-factor bound for aᵃ−bᵇ in Ding–Li–Li §3; the non-obvious input would need to control *moving divisors in the prescribed residue class*, and it still faces B2 and checklist lines B6/F3. Cheapest test: state and try to prove a second-moment bound for the campaign's fixed-p divisor-counting function with the modulus held fixed first; this is exploratory, not a claim of transfer.

### Relation to earlier verdicts

No prior negative transfer verdict changes. `BRAINSTORM/z31_small_count_pointwise.md` already screened Romanoff/covering and HBP; `BRAINSTORM/z31_quadratic_forms.md` and `BRAINSTORM/z45_recent_pointwise_tools.md` already screen class-number/ternary-form routes; `BRAINSTORM/technique_transfer_list.md` includes Maynard, F-I, and additive combinatorics. The new source checks and 2026 papers sharpen the inventory but do not remove B2/B6.

## §4 Not accessed / could not verify

- **Brief §1 checked from source:** Friedlander–Iwaniec, Heath-Brown x³+2y³, Heath-Brown–Moroz, Maynard, Green–Sawhney, Merikoski n²+1, Pratt, Merikoski aX²+bY³. **Not yet checked at source:** Grimmelt–Merikoski specifically; the 2025–26 arXiv API query did not return data (network returned empty response). Found and opened the arXiv record for Merikoski 2503.05396 as a confirmed “newest” example, but cannot claim a comprehensive API census.
- **Brief §2 source limitations:** Croot and Bhargava–Hanke are source-opened. Erdős (1950) covering failure and Romanoff theorem were checked via the 2026 Ding–Li–Li article's explicit historical account and citations, plus Tao's secondary paper; original articles were not accessed. Linnik/Xylouris, Burgess, Gallagher's exact almost-all theorem, Sierpiński/Riesel, Gauss's three-square/triangular and Lagrange four-square primary sources, Duke–Schulze-Pillot full theorem, and Blomer's exact estimates remain **NOT ACCESSED** as standalone original statements in this lane. Their entries in §2 are sourced as structural comparisons, not represented as primary-source-verified here.
- The “one prime plus boundedly many powers of 2” formulation in the brief is unsupported by sources opened: Linnik, Heath-Brown–Puchta, and Pintz–Ruzsa concern **two** primes plus powers of 2. The 2026 Li–Liu preprint further improves the unconditional number to six (five under GRH). No every-n one-prime-plus-bounded-powers theorem verified.
- No proof claimed for ES. The heuristic counts in the table are explicitly labelled heuristic and should not be mistaken for theorem asymptotics.
