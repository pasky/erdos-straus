# ZF0 part 7

8 items completed: 5 interesting, 3 nothing; no skipped/covered/needs-compute.
Interesting: Z1227, Z1391, Z1434, Z1518, Z2539.
All mathematical conclusions carry the labels below; ES remains OPEN.
All computations stay below 8 GB and use at most two concurrent threads per job.
Artifacts: `data/z52b/pass2/ZF0/<mid>/`; records: `data/z52b/pass2/ZF0_part7.jsonl`.

## Z1227 — a learned partial-factor ranker actually transfers

**EVIDENCE.** For N=4Cp+1, factor N completely, assign exponents of the first ceil(ω(N)/2) prime factors, and label a partial assignment feasible exactly when an exhaustive assignment of the remaining factors gives a divisor d≡−1 (mod 4C). Train a 150-iteration, 15-leaf boosted-tree classifier on every prime p≤5000, C=1,…,8; there are 4,380 nontrivial factor-selection instances and 887 with both positive and negative partial assignments. Features are partial residue/size, target inverse residue, factor counts and smallest remaining prime residue; the completed-witness label is not a feature. This is the explicitly requested **small learned ranking alternative**, not a graph neural network or loopy BP implementation.

The larger held-out range 100001≤p≤10⁶ uses a systematic stride through the complete prime list, yielding 28,928 instances, 7,465 mixed-label instances. First-feasible-choice rate / MRR:

| Ordering | Top-1 | MRR |
|---|---:|---:|
| Learned | 0.990623 | 0.994877 |
| Increasing partial divisor | 0.387408 | 0.666083 |
| Seeded random | 0.450234 | 0.673983 |

Classification AUC is 0.985728. These comparisons use exactly the same (p,C) instances, so all mod-840 conditioning is matched, rather than comparing unrelated prime populations. The naive paired-instance bootstrap gain interval is [0.59095,0.61703]; it is not a prime-cluster confidence interval. With one remaining prime slot there are 4,351 instances and 100% top-1; with two, 3,086 and 97.80%; with three, only 28 and 92.86%. Thus the headline is dominated by genuinely small residue problems. Factorization and exact modular DP may be cheaper than learning; no runtime advantage or large-C generalization is claimed.

Reproduce: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 timeout 600s nice -n 10 uv run --with numpy --with sympy --with scikit-learn scripts/z52d_p2_ZF0_Z1227_rank.py` (37–52 seconds in these runs). Full paired ranks and summary are saved.

## Z1391 — all seven Salez equations, with an ordering warning

**CERTIFIED (computer).** `scripts/z52d_p2_ZF0_Z1391_census.c` implements equations (14a)–(15d) of [Salez, arXiv:1406.6307](https://arxiv.org/pdf/1406.6307), using the converse constructions of Proposition 3. For each family all its three constant parameters lie in [1,K]. Reconstructed A,B,C,D must be positive integers, satisfy the stated gcd and p-coprimality conditions, and satisfy the appropriate Rosati identity exactly (128-bit products). The equation is a genuine positive Egyptian-fraction certificate, not just a congruence hit. All seven families are checked independently before applying a reporting order.

| N | K | 14a first | 14b | 14c | 15a | 15b | 15c | 15d | Odd uncovered |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10⁷ | 24 | 664555 | 17 | 1 | 0 | 0 | 0 | 0 | 5 |
| 10⁸ | 24 | 5761255 | 173 | 5 | 1 | 3 | 0 | 1 | 16 |
| 10⁷ | 48 | 664578 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The prime 2 is handled separately and appears in its own column. CPU times are 16.4, 171.3, and 32.4 seconds respectively. Every table is also tabulated by p mod 840 in the corresponding CSV. At N=10⁸, independent coverage counts for the seven families are 5761255, 5684840, 5714976, 5684875, 5736138, 5615915, 5628567. Reversing the first-firing order gives 15d **5,628,567** first hits and leaves 14a only **17,209**. Family labels are strongly ordering-dependent, not intrinsic prime invariants. Equal bounds on different constant triples are also not equal search costs.

The 16 uncovered odd primes at K=24 are 5309329, 5719921, 5751001, 7586401, 8611201, 21746761, 24163441, 24738289, 53687929, 62103409, 63442201, 66707281, 67711081, 77869801, 81134089, 82134649. They are failures of this bounded menu only. We did not recover Salez's original program or original rule order. The 10⁹ target would extrapolate to about 28.5 CPU minutes for K=24 alone; the actual substantial census stops at 10⁸ rather than exceeding the remaining cap.

Reproduce:

```
timeout 20s gcc -O2 -Wall -Wextra scripts/z52d_p2_ZF0_Z1391_census.c -o /tmp/ZF0-salezcensus
ulimit -v 8000000
timeout 600s nice -n 10 /tmp/ZF0-salezcensus 100000000 24
```

Independent validation: `timeout 60s uv run --with sympy scripts/z52d_p2_ZF0_Z1391_validate.py` constructs tuples directly with exact rational arithmetic, checks explicit sums of three reciprocals, and compares all first-firing residue counts for p≤1000, K=4. All 961 checked family witnesses agree. For the identity 4ABCD=A+B+pC the denominators are pBCD,pACD,ABD; for 4ABCD=p(A+B)+C they are BCD,ACD,pABD.

## Z1434 — complete requested conference-abstract scan

**EVIDENCE (literature).** Downloaded the actual abstract PDFs, converted all pages with pdftotext, normalized whitespace, and searched `unit fraction`, `Egyptian`, `Straus`. This was not just a conference landing-page search.

* [CANT 2024 abstracts](https://www.theoryofnumbers.com/cant/CANT2024-abstracts.pdf): 635 extracted lines; no match.
* [CANT 2025 abstracts](https://www.theoryofnumbers.com/cant/CANT2025-abstracts.pdf): 1,132 lines; Vjekoslav Kovač, “Several irrationality problems for Ahmes series,” joint work with Terence Tao. Decisive text: “Proving (ir)rationality of infinite series of distinct unit fractions … resolve a question by Erdős on simultaneous rationality … [and] a negative answer to an ‘infinite-dimensional’ conjecture by Stolarsky.” Local lines 553–565.
* [CANT 2026 abstracts](https://www.theoryofnumbers.com/cant/CANT2026-abstracts.pdf): 1,177 lines; Collier Gaiser, “On Rado numbers for equations with unit fractions.” The abstract claims f₂(k)=O(k³), improving O(k⁶), and f₃(k)=O(k⁴³), for monochromatic solutions of Σ1/xᵢ=1/y. Its mechanism is an additive Ramsey set with controlled lcm. Local lines 303–316.
* [INTEGERS 2025 abstract page](https://sites.google.com/view/integersconference2025/abstracts) embeds [the actual Abstracts.pdf](https://drive.google.com/file/d/1RnsCoWIogiYK5A3rfrifDAAuE7sMsFP-/view): 1,385 lines; Rishika Agrawal, “Writing Rational Numbers as a Sum of Reciprocals of Shifted Golomb Primes.” Decisive text: Bloom's representation of 1 by reciprocals of shifted primes also holds for shifted Golomb primes, a density-zero recursively selected prime subset. Local lines 22–32.

These are three concrete Egyptian-fraction leads, **not** new ES results. Infinite-series irrationality, monochromatic representations with a variable target denominator, and unrestricted-length representations of 1 do not provide three reciprocals for every prescribed 4/p. No Straus/Egyptian keyword occurrence beyond these unit-fraction talks was found. `keyword_scan.json` preserves normalized matches; no 2027/ELAZ scan or talk-video review was attempted.

## Z1518 — 56 machine-readable families and 48 checked identities

**CERTIFIED (computer).** Read Cao–Xu [2610.32302](https://arxiv.org/pdf/2610.32302) and the two cited tame/wild papers [2605.23601](https://arxiv.org/pdf/2605.23601), [2609.29250](https://arxiv.org/pdf/2609.29250). Transcribed Tables 2.1, 3.1, 3.2, which together constitute the **56-family** claim. Tables 4.1/4.2 use a separately redefined 36-family Howerton numbering and must not be silently merged with this census.

`families.json` contains all formulas, parameter domains, types and independently synthesized certificates:

* Families 1–8: verify 24fᵢ+1=(24x+r)(24y+r), r=1,5,7,11,13,17,19,23. For r=1 both parameters are positive; otherwise they are nonnegative. These are **composite certificates, not ES identities**.
* Families 9–41: for f=a xy+b x+c y+d choose k=6bc/a−6d, factor X=6f+k, and enumerate polynomial divisor splits D·E=(nX)². Set Y=(D+nX)/(4k−1), Z=(E+nX)/(4k−1); select positive integer-valued polynomials.
* Families 42–56: recover a Type-II-style identity n=4ABD−A−B from the two linear factors of ∂f/∂z, then form the three denominator polynomials.
* All 48 solution families satisfy **4XYZ=n(XY+XZ+YZ)** identically in SymPy. Integer-valuedness is checked by exact values on the multivariate degree box, equivalently integral Newton/binomial coefficients. Nonnegative coefficients and positive constant terms establish positivity on the full nonnegative parameter domain. This is symbolic certification for every allowed parameter, not a finite numerical check.

For example, family 42 has u=4x+1, v=24y+5, A=2u, B=v, D=3z+2, n=4ABD−A−B. Its denominators are nBD,nAD,ABD. The general JSON stores the actual expanded/factored certificates for all families.

A crucial distinction surfaced in the requested residue test:

| n modulus | Classes n≡1 (24) | Genuine eventual ES classes found | Sufficient m threshold |
|---:|---:|---:|---:|
| 840 | 35 | 23 | 29 |
| 1680 | 70 | 46 | 29 |
| 3360 | 140 | 92 | 29 |
| 6720 | 280 | 184 | 55 |
| 20160 | 840 | 552 | 55 |
| 40320 | 1680 | 1104 | 79 |

“Genuine” here fixes x≤256 for the bilinear families, or x,z≤32 for the trilinear families, leaves y free, and retains only positive slopes dividing the modulus in m. Each marked class has an actual nonnegative-parameter preimage once past the stated threshold. This is a declared sub-menu, not all possible fixed-parameter choices. In contrast, the union of raw polynomial **images** is all m residues mod 840,1680,3360—even individual families often have full image. Having some parameter preimage modulo M does **not** imply every integer in that residue class has an integer preimage. The image result gives no proof of the global union claim.

Reproduce: `OPENBLAS_NUM_THREADS=1 timeout 300s nice -n 10 uv run --with sympy --with numpy scripts/z52d_p2_ZF0_Z1518_families.py` (104 seconds). Residue enumeration streams O(M)-sized vectors; no M³ array. We did not replay the paper's claimed m≤10¹¹ numerical union or prove that union.

## Z1776 — Walnut works, but not unrestricted multiplication

**CERTIFIED (computer).** Cloned `https://github.com/firetto/Walnut`; default Java 21 failed with Gradle's unsupported class version 65, then Java 17 built successfully using `JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 ./gradlew --no-daemon --max-workers=2 customFatJar`. Run the jar with `-Xmx1024m -XX:ActiveProcessorCount=2`. Commands and output automata are archived.

The base-4 regular language `0*10*` represents 4ˢ, s≥0. The menu is n≡0 (5) or n≡13 (20). Its ES identities are elementary: if n=5q, scale 4/5=1/2+1/4+1/20; if n≡13 (20), put D=(3n+1)/20 and use 4/n=1/(10D)+1/(2D)+1/(5nD). Positivity and integrality hold for positive n in these classes.

Walnut returns TRUE for all powers t: menu(t+9); FALSE for menu(t+297). The latter only refutes this particular menu, not ES for the open family. We then submitted the actual equation `4*x*y*z=(n+297)*(x*y+x*z+y*z)` with positive existential witnesses. Walnut rejects it at the first variable-times-variable operation: “the operator * cannot be applied to two variables.” Addition and multiplication by constants are automatic; unrestricted multiplication is not a synchronous fixed-base regular relation. Thus finite regular menus can be certified, but this direct unrestricted ES encoding is outside the supported arithmetic. No blanket impossibility of a future clever restricted encoding is asserted.

## Z1890 — fitted posterior, exposed the extrapolation nonidentifiability

**Assessment.** The assembled table contains actual sibling domains and failure lists, not just previously quoted expected counts: 6/99,999 pencil failures, 6/39,175 Gaussian-prime failures, 6/2,999 failures of 8/n. Bins explicitly show failures disappear in later tested ranges. `sibling_counts.json` gives exact file provenance and all lists.

Fitted yᵢ|θᵢ∼Binomial(Nᵢ,θᵢ), θᵢ∼Beta(μκ,(1−μ)κ), with a uniform 181×181 grid prior in log₁₀μ∈[−8,−0.3], log₁₀κ∈[−1,7]. Posterior median μ=0.0007528, 95% interval [0.0001411,0.03508]; κ median 599.5. Posterior grid boundary mass is 0.0001466. For a fresh exchangeable sibling, the predictive probability of at least one failure in 1000 trials is 0.36689, and in 10⁶ trials 0.90736.

The stationary model has θ_ES>0 almost surely, so its requested infinite-tail probability is exactly **1**, for **any** threshold including 10¹⁸. That is a prior-support/model artefact, not evidence against ES. An independent ES-specific zero-rate spike of mass 0.1,0.5,0.9 changes this answer to 0.9,0.5,0.1 with no change in sibling likelihood. Hence no defensible arithmetic posterior for ES follows without a specified nonstationary transfer law, ES verification history, and an ES-specific prior. This is why the completed first step receives `nothing`, not a sensational probability claim.

Reproduce: `OPENBLAS_NUM_THREADS=1 timeout 90s uv run --with numpy --with scipy scripts/z52d_p2_ZF0_Z1890_bayes.py`.

## Z2539 — ten Lean-checked extracted algebraic components

**CERTIFIED (computer).** I acted as the LLM prover, supplying statements and proofs to the installed Lean kernel. The toolchain is present but no default is configured; the explicit selector works. The repo's Lean project has no installed `.lake/packages` Mathlib checkout, so this attempt deliberately uses `import Std` only. Default thread creation exceeded the bounded process resources; `-j2` fixes it.

| Statement | DISCOVERIES.md source | Result |
|---|---|---|
| Master identity with denominators cleared | line 629, Lemma 1.1 | omega |
| (★) pair/product identity | line 1662, Lemma 1.1 | grind |
| (★) determinant identity | line 1662, Lemma 1.1 | grind |
| Common divisor of jp+1,j′p+1 divides j−j′ | line 1554, Lemma 2.3 | witnesses + grind |
| 4·64(u³+1)−(256u³+105)=151 | line 1362, Thm 1.1 component | grind |
| 64u³+2u²−2u+66=2(32u+33)(u²−u+1) | same | grind |
| u≡32 (151) implies 151 divides 32u+33 | same | omega |
| Sophie-Germain factorization | line 1404, Thm B/C component | grind |
| Positive multiple of p below 2p equals p | line 1631, Lemmas C/D component | order lemmas + omega |
| Odd-n ES solutions have zero or one odd denominator | line 862, Lemma 2.1 | parity cases + simp + omega |

The first direct tactic attempt closed 8/10; order and parity repairs closed 10/10. Every final `#print axioms` reports only propext, Classical.choice and Quot.sound (or a subset), **no sorryAx**. Precise scope: these are ten short extracted components, several from the same parent theorem, not ten complete geometric/analytic campaign lemmas. The common-divisor statement is general enough to instantiate the gcd lemma; the rational master identity is checked only in its denominator-cleared algebraic form.

Reproduce: `ulimit -v 8000000; timeout 120s nice -n 10 ~/.elan/bin/lean +leanprover/lean4:v4.34.1 -j2 scripts/z52d_p2_ZF0_Z2539_lemmas.lean`. Final stdout: `Z2539/lean.log`; initial failures: `Z2539/first_attempt.log`.

## Z1878 — Fujimoto folds are not three Egyptian summands

**EVIDENCE (literature), PROVED (elementary distinction).** The fetched [Folding π, §3](https://arxiv.org/html/2403.09277v1#S3) identifies Fujimoto edge-to-crease folds as L(t)=t/2, R(t)=(t+1)/2; backwards numerators multiply by 2 modulo an odd denominator. After k folds the affine map is (t+j)/2ᵏ, so a fixed-point fraction has denominator dividing 2ᵏ−1. For three folds that denominator divides 7; starting with a dyadic crease, every finite output is dyadic. An arbitrary initial approximate crease retains error scaled by 2⁻ᵏ, not an exact fraction. There is no natural equivalence between three folds and three unit-fraction summands. This says nothing against exact rational constructions using richer origami axioms.
