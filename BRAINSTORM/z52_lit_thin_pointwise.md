# z52 literature lane L5 — thin pointwise existence

## §0 Summary
- **NEW since 2026-09-28:** None identified. Source checks confirm earlier-known Maynard (family-level) and Heath-Brown–Puchta (two primes plus powers of two) results.
- **Transferable features:** (1) Fourier/Type I–II decorrelation can find primes in an infinite thin family; (2) bounded sparse summands can be absorbed when a power-size Goldbach supply is present.
- **Does ES share them?** No: ES is a prescribed-prime, ≍ log²p tied-modulus problem (B2/B6), not a family average or power-sized reservoir.
- **Campaign verdict change:** None. No new pointwise, polylog-count theorem transferable to ES found; unverified leads are explicitly listed in §4.

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

### Pintz–Ruzsa: Linnik–Goldbach with eight powers of two

J. Pintz and I. Z. Ruzsa, “On Linnik’s approximation to Goldbach’s problem. II,” DOI 10.1007/s10474-020-01077-8, *Acta Mathematica Hungarica* 161 (2020), 569–582 (published 22 July 2020). Abstract, accessed 2026-10-30: every sufficiently large even integer is a sum of two primes and K=8 powers of two, unconditionally. Status: published. Excerpt `sources/z52/thin_pointwise/pintz_ruzsa_2020.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; this is pointwise but has a power-sized two-prime supply, not a polylog-only mechanism.

### Erdős and Cohen–Selfridge: covering obstructions around powers of two

Theorem/claim checked via Tao, “A remark on primality testing and decimal expansions,” arXiv:0802.3361v4 (accessed 2026-10-30), which cites Erdős (1950) and Cohen–Selfridge (1975). Tao records Erdős's AP of odd m for which |m−2^i| is always composite and Cohen–Selfridge's strengthening making both |m−2^i| and m+2^i composite. This is a secondary-source verification of those claims; it does not justify the stronger unqualified claim that the AP contains no p+2^k representations. Status: original publications cited, secondary source checked. Excerpt `sources/z52/thin_pointwise/erdos_covering_tao_arxiv.txt`. Relation: `BRAINSTORM/z31_small_count_pointwise.md`; finite congruence covering of an exponential orbit produces failures, illustrating B1, but no direct ES transfer.

## §2 Structural-feature table

| Problem | Structural feature that made it solvable | Does ES share it? | Transfer verdict |
|---|---|---|---|
| Primes omitting a digit (Maynard) | Averaging over an infinite prime family; circle method and Type I/II minor-arc control for the joint prime/digit constraints. | No for the pointwise conclusion: the result is infinitely-many, not prescribed-n; B6 asks for dominance at one object. | Known-dead as direct transfer: `BRAINSTORM/technique_transfer_list.md` and `BRAINSTORM/z45_recent_pointwise_tools.md`; no change to those verdicts. |
| Every sufficiently large even n = two primes + 13 powers of 2 (Heath-Brown–Puchta) | The two-prime Goldbach component gives a power-sized supply; bounded powers of two ride on the analytic main term. | No: ES has only ≍ log²p expected tied-modulus events, not a power-sized reservoir (B6/B2). | Known-dead as direct transfer; `BRAINSTORM/z31_small_count_pointwise.md` §(c) already identifies the power-main-term dependency. |
| Least QNR / least prime in an AP | Character-sum/L-function control for a character at a fixed modulus; short-window pointwise bounds need strong hypotheses or power-length windows. | Partial: the quadratic-character sign in ES is analogous, but the divisor modulus varies with the certificate; see B2 and FRONTIER §3 (F3). | Known-dead as direct transfer: `BRAINSTORM/z31_small_count_pointwise.md`; no novelty claimed. |
| Ternary quadratic-form representation / three-square pointwise theorems | Class-number or representation-count main terms, plus local conditions; ternary forms can have class-number-scale supply (Duke–Schulze-Pillot). | No identified shared supply: ES's count is polylogarithmic and subject to the tied-modulus forcing bottleneck (B2/B6). | Known-dead as direct transfer: `BRAINSTORM/z31_quadratic_forms.md` and `BRAINSTORM/z31_small_count_pointwise.md`. These are repo leads, not independently source-verified in this lane. |
| n = p + 2^k | The expected count is O(1); Romanoff gives positive density, while a covering-congruence construction produces an AP of failures. | No: its failure relies on periodic exponents modulo fixed moduli; ES primes do not furnish that covering mechanism (B1). | Known-dead as failure analogue, `BRAINSTORM/z31_small_count_pointwise.md`; no inference about ES failures. Source not independently checked here. |

## §3 NEW candidates

None. The verified thin-prime theorem is a family-count result; the verified pointwise sparse-summand theorem still has a power-sized two-prime component. Neither supplies an approach to single-prime ES. The possible “between” examples found in the campaign files (least witnesses and quadratic forms) are already screened in `BRAINSTORM/z31_small_count_pointwise.md`; source verification here did not change their transfer assessment.

## §4 Not accessed / could not verify

- **Not independently source-verified in this lane:** Friedlander–Iwaniec primes of the form x²+y⁴; Heath-Brown's x³+2y³; Heath-Brown–Moroz; Green–Sawhney (title and precise result); Merikoski and Grimmelt–Merikoski; Pratt; Li; 2025–26 “x²+y³” lead; Linnik least-prime-in-AP theorem; Burgess least-QNR bounds; Romanoff/Erdős covering result; Sierpiński/Riesel; Heath-Brown–Puchta refinements beyond their abstract; three squares/genus and Duke–Schulze-Pillot. Prior campaign summaries are cited above but are not substitutes for the required source verification.
- **Potentially wrong lead:** “every n is a sum of a prime and boundedly many powers of 2” should not be conflated with Linnik's theorem as stated in the brief: the verified Heath-Brown–Puchta theorem has *two* primes, and its precise statement is given in §1. No one-prime theorem verified.
- No exact theorem or manuscript for the brief's Green–Sawhney title was identified/accessed in this lane; do not use that lead as a citation.
