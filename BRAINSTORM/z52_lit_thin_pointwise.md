# z52 literature lane L5 — thin pointwise existence

## §0 Summary
- **New since 2026-09-28:** Li–Liu (arXiv:2610.15784, 11 Oct 2026) proves 6 powers of 2 unconditionally, 5 under GRH, with two primes. Ding–Li–Li (4 July 2026) is newly checked here, not new since the cutoff.
- **Source-check scope:** 20 named entries checked on 2026-10-30, drawing on 16 distinct directly consulted works plus historical claims checked secondarily; the memo distinguishes those evidence levels.
- **Verified thin-prime literature:** F-I x²+y⁴; Heath-Brown x³+2y³; Heath-Brown–Moroz; Maynard restricted digits; Pratt; Green–Sawhney p²+nq²; Merikoski n²+1 and aX²+bY³.
- **Structural features:** family averaging/Type I–II Fourier decorrelation; power-sized Goldbach or class-number representation reservoirs; fixed-modulus character control.
- **Does ES share them?** Not the decisive feature: a ≍log²p expected/main-term scale is often predicted for ES's tied, moving-modulus events (B2/B6); this is not a uniform actual witness count, and known R(p) can be super-polylogarithmic.
- **Verdict change:** None. No verified universal theorem with polylog witnesses and no local obstruction transfers to ES. Source-access gaps are listed in §4.

## §1 Verified entries

### Green–Sawhney: primes p²+nq²

Ben Green and Mehtaab Sawhney, “Primes of the form p²+nq²,” arXiv:2410.04189 v3 (6 June 2026; submitted 5 October 2024), accepted for *Acta Mathematica*. Abstract, accessed 2026-10-30: for each n ≡ 0 or 4 (mod 6), infinitely many primes p²+nq² with p,q prime, and an asymptotic count; n=4 proves the Friedlander–Iwaniec Gaussian primes conjecture. The method uses Type I/II sums over Q(√−n), with recent Gowers-norm inputs for Type II. Status: accepted preprint. Excerpt: `sources/z52/thin_pointwise/green_sawhney_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`, `BRAINSTORM/z31_small_count_pointwise.md` found by `git grep`; result counts a family of prime variables, not witnesses to each prescribed integer, so no B6 transfer.

### Merikoski: primes ax²+by³ (2025)

Jori Merikoski, “On primes represented by aX²+bY³,” arXiv:2503.05396 v1, submitted 7 March 2025. Abstract, accessed 2026-10-30: for coprime positive a,b, *conditionally* on a conjecture about Hecke eigenvalues along binary cubic forms, an asymptotic for primes ax²+by³ with x≤X^(1/2), y≤X^(1/3). Status: preprint, conditional theorem. Excerpt: `sources/z52/thin_pointwise/merikoski_ax2_by3_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`; family average under an explicit unproved input, not universal n representation.

### Merikoski: large prime factor of n²+1

Jori Merikoski, “On the largest prime factor of n²+1,” arXiv:1908.08816 v3 (2 November 2020; submitted 23 August 2019). Abstract, accessed 2026-10-30: infinitely often the largest prime factor of n²+1 exceeds n^1.279; under Selberg's eigenvalue conjecture, exponent 1.312. It highlights Type II estimates, Harman's sieve, and Kloosterman-sum bounds. Status: preprint v3. Excerpt: `sources/z52/thin_pointwise/merikoski_arxiv.txt`. Relation: `BRAINSTORM/z45_recent_pointwise_tools.md` and `BRAINSTORM/z31_small_count_pointwise.md`; subsequence large-factor result, not every-n prime/witness result.

### Friedlander–Iwaniec: primes x²+y⁴

John Friedlander and Henryk Iwaniec, “The polynomial X²+Y⁴ captures its primes,” arXiv:math/9811185 v1 (1 November 1998), published *Annals of Mathematics* 148 (1998), no. 3, 945–1040. Abstract, accessed 2026-10-30: infinitely many primes a²+b⁴; moreover a Λ-weighted asymptotic with main term proportional to x^(3/4), corresponding to unweighted count scale x^(3/4)/log x. Status: published. Excerpt: `sources/z52/thin_pointwise/friedlander_iwaniec_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`, `BRAINSTORM/s8_volume_dfi.md`, `BRAINSTORM/z45_recent_pointwise_tools.md`; the volume/counting theorem has no prescribed-target conclusion (B6).

### Heath-Brown: primes x³+2y³

D. R. Heath-Brown, “Primes represented by x³+2y³,” *Acta Mathematica* 186 (2001), 1–84. Oxford repository record and linked article opened 2026-10-30; Theorem 1: infinitely many primes of this form, x,y integers. Status: published. Excerpt: `sources/z52/thin_pointwise/heath_brown_cubic_ora.txt`. Relation: `BRAINSTORM/technique_transfer_list.md` and `BRAINSTORM/z45_recent_pointwise_tools.md`; family-level infinitude does not force an individual n.

### Heath-Brown–Moroz: primes represented by cubic forms

D. R. Heath-Brown and B. Z. Moroz, “Primes represented by cubic forms,” 2002. Oxford repository record and linked paper PDF opened 2026-10-30. Theorem 1.1 assumes an irreducible integral binary cubic form and handles the all-even case separately: if every value of f is even, it proves that f/2 represents infinitely many primes; otherwise the theorem gives infinitely many prime values of f. A fixed-divisor form does not directly yield prime values of f. Status: published paper. Excerpt: `sources/z52/thin_pointwise/heath_brown_moroz_ora.txt`. Relation: `BRAINSTORM/technique_transfer_list.md` and `BRAINSTORM/z45_recent_pointwise_tools.md`; again an infinitude over the form's values, not every target integer.

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

### Romanoff: p+2^k has positive lower density

N. P. Romanoff, “Über einige Sätze der additiven Zahlentheorie,” Math. Ann. 109 (1934), 668–678. The statement is quoted explicitly in Ding–Li–Li, arXiv:2607.03662v1 §1, opened 2026-10-30: {p+2^k} has positive lower density. Status: published original bibliographic data and statement checked via a 2026 secondary source; original not opened. Excerpt `sources/z52/thin_pointwise/ding_romanoff_2026.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; positive-density target set is not every target (B6).

### Erdős: an arithmetic progression avoiding p+2^k

P. Erdős, “On integers of the form 2^k+p and some related problems,” Summa Brasil. Math. 2 (1950), 113–123. Ding–Li–Li arXiv:2607.03662v1 §1 states Erdős constructed an AP, common difference 11,184,810, whose terms are not p+2^k (opened 2026-10-30). Status: original publication identified; result checked via secondary source. Excerpt `sources/z52/thin_pointwise/ding_romanoff_2026.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; finite covering failure mode for a periodic exponent orbit, unlike ES (B1).

### Cohen–Selfridge: prime-power covering variants

F. Cohen and J. L. Selfridge, “Not every number is the sum or difference of two prime powers,” Math. Comp. 29 (1975), 79–81. Tao's arXiv:0802.3361v4 §1, opened 2026-10-30, says they exhibit an AP of odd m for which both |m−2^i| and m+2^i are composite for every i. Status: primary source not opened; exact result checked through Tao's secondary article. Excerpt `sources/z52/thin_pointwise/erdos_covering_tao_arxiv.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; periodic covering counterexample, not direct ES failure mechanism.

### Tao: primes resistant to digit modification

Terence Tao, “A remark on primality testing and decimal expansions,” arXiv:0802.3361v4, accessed 2026-10-30; the arXiv record says “to appear, J. Aust. Math. Soc.” Theorem 1.2: for fixed K and sufficiently large N, at least c_K N/log N primes in [N,(1+1/K)N] have |kp±ja^i| composite for all 1≤a,j,k≤K and 1≤i≤K log N. Proof uses partial covering followed by Selberg sieve. Status: theorem directly checked in preprint. Excerpt `sources/z52/thin_pointwise/erdos_covering_tao_arxiv.txt`. Relation: `BRAINSTORM/technique_transfer_list.md`; a prime-family/digit statement, not representation of each given n (B6).

### Lagrange: four squares

Joseph-Louis Lagrange's four-square theorem, as stated in Bhargava–Hanke's source-opened “Universal quadratic forms and the 290-Theorem” (preprint PDF, accessed 2026-10-30, introduction): every positive integer is a sum of four integer squares. This lane verified the statement through that scholarly source's explicit historical/theorem statement, not by opening Lagrange's 1772 memoir. Jacobi's exact r₄ formula is not stated in the opened source; this comparison is standard background, not source-verified here. Relation: `BRAINSTORM/z31_quadratic_forms.md`; universality alone does not imply a large representation count.

### Croot: Erdős–Graham coloring theorem for unit fractions

Ernest S. Croot III, “On a coloring conjecture about unit fractions,” arXiv:math/0311421 v1 (24 November 2003), *Annals of Mathematics* 157 (2003), no. 2, 545–556. Abstract, accessed 2026-10-30: for some b>0, every r-coloring of [2,b^r] has a monochromatic set S with Σ_{n∈S}1/n=1. Status: published. Excerpt `sources/z52/thin_pointwise/croot_arxiv.txt`. Relation: `BRAINSTORM/addcomb_unit_fraction_density.md`, `BRAINSTORM/technique_transfer_list.md`; theorem is coloring-forcing, not a statement about every prescribed target n.

### Bhargava–Hanke: 290 theorem

Manjul Bhargava and Jonathan Hanke, “Universal quadratic forms and the 290-Theorem,” authors' 16-page preprint PDF, opened 2026-10-30. Theorem 1: a positive-definite integer-coefficient quadratic form representing the 29 listed critical integers up to 290 represents all positive integers. Theorem 2 establishes necessity of each test integer. Status: authors' preprint checked; publication venue/year not independently verified in this lane. Excerpt `sources/z52/thin_pointwise/bhargava_hanke_290.txt`. Relation: `BRAINSTORM/z31_quadratic_forms.md`, `BRAINSTORM/technique_transfer_list.md`; this is a finite criterion for a form being universal, not a sparse per-n witness theorem.

### Blomer: ternary forms and restricted three-square variables

Valentin Blomer, “Ternary quadratic forms, and sums of three squares with restricted variables,” in *The Anatomy of Integers*, CRM Proc. Lecture Notes 46 (2008). Author abstract PDF opened 2026-10-30: survey of positive integral ternary forms, improved uniform asymptotic formulas for representation counts, and Gauss-type three-square results with almost-prime, squarefree, or smooth variables. Status: published chapter; abstract only verified here, precise theorem hypotheses not extracted. Excerpt `sources/z52/thin_pointwise/blomer_abstract19.txt`. Relation: `LITERATURE_AUTOMORPHIC.md` §§ Blomer and `BRAINSTORM/z31_quadratic_forms.md`; not an every-n theorem absent additional hypotheses.

### Ding–Li–Li: 2026 Romanoff-type positive-density result

Yuchen Ding, Huixi Li, and Junfeng Li, “A Romanoff-type theorem for P₂+{aᵃ:a≥1},” arXiv:2607.03662 v1, submitted 4 July 2026. Abstract, accessed 2026-10-30: with P₂={m:Ω(m)≤2}, P₂+{aᵃ:a≥1} has positive lower density; the argument uses a Romanoff second moment and bounds an average singular factor. Status: preprint. Excerpt `sources/z52/thin_pointwise/ding_romanoff_2026.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md` and `BRAINSTORM/technique_transfer_list.md`; this is a genuinely recent family-density result, not every n and not evidence for a fixed-n polylog witness theorem.

## §2 Structural-feature table

| Problem / verified status | Expected witnesses at fixed n (heuristic where stated) | Mechanism; pointwise scope | ES comparison / transfer |
|---|---|---|---|
| Friedlander–Iwaniec, primes a²+b⁴ | Λ-weighted family asymptotic has main scale x^(3/4), corresponding to unweighted count x^(3/4)/log x; not fixed-target n. | Weighted asymptotic over (a,b), sieve/dispersion. Infinitely many represented primes. | No prescribed target; family count only (B6). |
| Heath-Brown, primes x³+2y³ | Family count; no per-target assertion. | Binary cubic form/cubic field methods; infinitely many primes. | No single-n dominance; no transfer. |
| Heath-Brown–Moroz, admissible binary cubic forms | Family count; no per-target assertion. | Generalizes cubic-form prime infinitude. | Same B6 mismatch; no transfer. |
| Maynard, primes missing a digit | Positive infinitude, no prescribed integer. | Circle method + Type I/II sieve; decorrelates prime and digital Fourier large spectra. | No; `technique_transfer_list.md`, `z45_recent_pointwise_tools.md`; family-only. |
| Pratt, restricted-coordinate sum of two squares primes | Asymptotic over p=m²+ℓ² with ℓ digit-restricted; no fixed-target count. | F-I plus Maynard ideas. | No; family average. |
| Green–Sawhney, p²+nq², p,q prime (n≡0,4 mod 6) | Asymptotic family count; not prescribed n. | Type I/II in Q(√−n), Gowers norm inputs. | No; family result (B6). |
| Merikoski, P(n²+1)>n^1.279 | Infinitely many n; at such n at least one large prime factor, not a prime value. | Type II estimate + Harman sieve, Kloosterman bounds. | Not an every-n witness theorem; no transfer. |
| Merikoski, primes ax²+by³ (a,b coprime) | Asymptotic count over x,y in boxes; no fixed-target statement. | Conditional on Hecke-eigenvalue conjecture; sieve, quadratic forms, GL(2) spectrum. | Conditional family average; no ES pointwise conclusion. |
| Heath-Brown–Puchta, two primes + 13 powers (2002) | Per target, Goldbach pair reservoir has expected scale ≍ n/log²n; powers add ≍log^13 n choices before coincidences/singular factors. | Every sufficiently large even n; circle method + powers-of-two exponential-sum large-deviation bound. | No: power-size supply vs ES's predicted ≍log²p expected/main-term scale, not a uniform actual count (B2/B6). `z31_small_count_pointwise.md`. |
| Li–Liu, two primes + 6 powers (2026); 5 under GRH | Same power-size two-prime reservoir; not polylog-only. | Every sufficiently large even n; circle method, major/minor arcs, dyadic-sum large deviations, representation-count quadratic form. | New result, but no ES-like sparse-witness mechanism (B6). |
| Pintz–Ruzsa, two primes + 8 powers | Same power-size reservoir. | Every sufficiently large even n, unconditional; theorem verified from published abstract. | Same: doesn't bridge B2. |
| Linnik: two primes + bounded K powers | K unspecified in original theorem; expected representation count has a power-size Goldbach factor. | Every sufficiently large even n. | No; not one-prime-plus-powers. One-prime phrasing in the brief is not supported by the sources checked. |
| Gallagher as cited by Heath-Brown–Puchta | Gallagher's exact witness count not estimated here. | HBP cites Gallagher as a methodological predecessor for two-prime-plus-powers arguments; its standalone theorem was not accessed, so no almost-all scope is asserted. | A literature lead only; not evidence for the p+2^k+2^ℓ equation. |
| Odd n=p+2^k, k≥1; Romanoff | Expected count ≍ Σ_{k≤log₂n}1/log n=O(1), coarse heuristic; positive lower density of represented n, not every n. | Romanoff second moment proves positive density; Erdős covering construction gives an AP of failures (verified in Tao secondary source). | Failure analogy, not a transfer; fixed-modulus periodic orbit unlike ES. B1. |
| Odd n=p+2^k+2^ℓ, k,ℓ≥1 | Expected witnesses ≍ log n from ≍log²n exponent pairs and prime density 1/log n, a coarse heuristic only. Even n is exceptional for positive exponents (then p=2). | No every-n or almost-all theorem for this precise equation verified here. | Intermediate O(log n) model on odd targets only; no source-verified covering failure or ES transfer. |
| Sierpiński / Riesel k2^m±1 | For fixed k, one candidate per m; covering produces no prime values at all, rather than a prescribed n witness. | Finite prime-divisor covering; 78557 Sierpiński and 509203 Riesel are standard examples. | Same periodic-covering obstruction, irrelevant at ES primes. |
| Croot, Erdős–Graham coloring theorem | Number of unit-fraction solutions depends on coloring/range; not a statement about each target n. | For every r-coloring of [2,b^r], a monochromatic set has reciprocal sum 1 (arXiv abstract). | Different combinatorial forcing structure; no ES single-prime analogue. |
| Four squares, r₄(n) | Jacobi's formula has a main scale n times local factors, but these factors can suppress growth: r₄(4ᵃ)=24. | Every positive n by Lagrange; representation count is not uniformly power-sized. | Universality illustrates local-global existence only; do not classify it as a uniform large-witness reservoir. |
| Three squares, r₃(n) | For admissible n, often class/L-value scale, but not uniformly power-sized: r₃(4ᵃ)=6; local obstruction exactly n=4^a(8b+7). | Gauss–Legendre: every admissible n; class-number / genus arithmetic. | No local obstruction for ES hard primes, but count scale differs radically. |
| Three triangular numbers | Via 8n+3 as a sum of three odd squares; representation count involves ternary class/L-value factors and is not asserted uniformly ≍√n here. | Every n (Gauss); inherited three-square identity. | Universal existence is distinct from a uniform power-size reservoir; not shared by ES. |
| Duke–Schulze-Pillot ternary positive forms | Representation numbers typically scale like √n times local/class factors; theorem is not an unconditional assertion for every locally represented n without spinor-exception qualifications. | Equidistribution of lattice points / cusp-form bounds; excludes spinor-exception square classes in its standard application. | No; ES has only polylog events and tied moving moduli (B2/B6). Prior `z31_quadratic_forms.md`. |
| Bhargava–Hanke 290 theorem | Not a witness-count theorem: finitely many 29 test values decide universality of a quadratic form. | Universal form represents all integers iff it represents critical set; proved via escalation, local densities, modular forms, finite computation. | Formal finite testing rather than per-n witness; no transfer. |
| Blomer, ternary forms / restricted three squares | Representation counts over n with uniform asymptotics; Gauss-type almost-prime/squarefree/smooth coordinates; not every prescribed n by itself. | Weight-3/2 theta series, subconvexity, ternary-form representation analysis (author abstract opened). | Count asymptotics do not overcome B2; not a new candidate. |
| Least prime in AP (Linnik–Xylouris) | Commonly cited Linnik exponent L=5 gives a q^5-type bound; exact theorem text was not opened in this lane. | Zero-free region / Dirichlet L-functions; pointwise for each reduced residue class, as a secondary-source structural comparison. | Fixed modulus, power scale; partial analogy only. B2 has moving modulus. |
| Least quadratic nonresidue (Burgess) | Standard cited bounds are ≪ p^(1/(4√e)+ε) unconditionally and O(log²p) under GRH; original sources were not opened here. | Burgess short character sums; GRH via L-functions (secondary-source comparison only). | Character value is analogous, but ES needs divisor in moving residue class; B2/F3. |

Count labels caveat: “expected” counts are heuristic local-density estimates, not source theorems; asymptotic statements above are recorded only where the cited paper proves them. The brief's “every n is prime + bounded powers of two” conflation is rejected: verified Linnik/HBP/Pintz–Ruzsa statements use **two** primes. Four-square representation counts can be small on scaled targets (r₄(4ᵃ)=24), so universality is not classified as a uniform power-size reservoir.


## §3 Dichotomy and NEW candidates

### What fails, what succeeds, what lies between

| Witness scale at one target | Examples checked | Status / mechanism |
|---|---|---|
| O(1) expected witnesses; covering failures | n=p+2^k; Romanoff-positive-density set versus Erdős AP of failures | Demonstrates positive density can coexist with an infinite arithmetic progression of failures; fixed-modulus covering controls the exponent orbit. Not every n and not ES-like divisor events. |
| ≍log n expected witnesses | Odd n=p+2^k+2^ℓ with k,ℓ≥1 (coarse heuristic) | Even targets are exceptional (p=2); no every-n or almost-all theorem or covering failure for odd targets verified here. |
| Every-target theorems with a power-size main term | Two primes + K powers of 2; three triangular numbers (class-number scale) | Circle-method Goldbach main term gives many representations for every sufficiently large even n. Three triangular numbers correspond to 8n+3 and have class-number-scale counts; Siegel gives an ineffective ≫ε n^(1/2−ε) lower bound. By contrast, r₃(4ᵃ)=6 and r₄(4ᵃ)=24 show ordinary square counts can degenerate. |
| Unconditional tied/moving-modulus polylog theorem, universal target, no local obstruction | No verified example found | This is the relevant gap for ES. This does not assert that no conditional fixed-modulus examples exist: under GRH, least quadratic nonresidues have O(log²p) bounds. ES's predicted ≍log²p expected scale is not a uniform actual count and involves tied moving moduli (B2). |
| Family-count / infinitude results (not fixed-target witness counts) | Maynard; Friedlander–Iwaniec; Green–Sawhney; Pratt | Prime variables range over growing families; no polylog fixed-target witness count is asserted. Family averaging is not a target-by-target theorem (B6). |
| Positive density among integer targets | Romanoff p+2^k; Ding–Li–Li P₂+aᵃ | Second-moment/mean singular-factor methods; positive density is not every-target existence (B6). |
| Fixed-modulus character witnesses | Least QNR: GRH gives O(log²p); least prime in a reduced class mod q: GRH gives a power-of-q bound, not a logarithmic window | Character-sum / L-function zero control; these have fixed moduli, unlike ES's moving modulus (B2/F3). |

No NEW candidate. The October 2026 Li–Liu advance (K=6 unconditional, K=5 under GRH) is a genuine new literature update but retains the two-prime main term; it changes the state of the comparison, not the ES transfer verdict. The July 2026 Romanoff-type theorem similarly adds a fresh positive-density model of correlated sparse shifts, not a fixed-n theorem. A concrete next test, if pursuing the sparse-shift analogy, is to quantify whether the ES certificate parameter set has any analogue of the mean singular-factor bound for aᵃ−bᵇ in Ding–Li–Li §3; the non-obvious input would need to control *moving divisors in the prescribed residue class*, and it still faces B2 and checklist lines B6/F3. Cheapest test: state and try to prove a second-moment bound for the campaign's fixed-p divisor-counting function with the modulus held fixed first; this is exploratory, not a claim of transfer.

### Relation to earlier verdicts

No prior negative transfer verdict changes. `BRAINSTORM/z31_small_count_pointwise.md` already screened Romanoff/covering and HBP; `BRAINSTORM/z31_quadratic_forms.md` and `BRAINSTORM/z45_recent_pointwise_tools.md` already screen class-number/ternary-form routes; `BRAINSTORM/technique_transfer_list.md` includes Maynard, F-I, and additive combinatorics. The new source checks and 2026 papers sharpen the inventory but do not remove B2/B6.

## §4 Not accessed / could not verify

- **Brief §1 checked from source:** Friedlander–Iwaniec, Heath-Brown x³+2y³, Heath-Brown–Moroz, Maynard, Green–Sawhney, Merikoski n²+1, Pratt, Merikoski aX²+bY³. **Not yet checked at source:** Grimmelt–Merikoski specifically; the 2025–26 arXiv API query did not return data (network returned empty response). Found and opened the arXiv record for Merikoski 2503.05396 as a confirmed “newest” example, but cannot claim a comprehensive API census.
- **Brief §2 source limitations:** Croot and Bhargava–Hanke are source-opened. Romanoff (1934), Erdős (1950), and Cohen–Selfridge (1975) historical statements were checked in the 2026 Ding–Li–Li and Tao papers; those original articles were not accessed. Linnik/Xylouris theorem text, Burgess, Gallagher's exact theorem, Sierpiński/Riesel, Gauss's three-square/triangular and Lagrange four-square primary sources, Duke–Schulze-Pillot full theorem, and Blomer's exact estimates remain **NOT ACCESSED** as standalone original statements in this lane. Their entries in §2 are sourced as structural comparisons, not represented as primary-source-verified here.
- The “one prime plus boundedly many powers of 2” formulation in the brief is unsupported by sources opened: Linnik, Heath-Brown–Puchta, and Pintz–Ruzsa concern **two** primes plus powers of 2. The 2026 Li–Liu preprint further improves the unconditional number to six (five under GRH). No every-n one-prime-plus-bounded-powers theorem verified. Gallagher's exact theorem is not claimed here; its standalone source remains unchecked.
- No proof claimed for ES. The heuristic counts in the table are explicitly labelled heuristic and should not be mistaken for theorem asymptotics.
