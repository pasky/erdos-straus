# ZF0 part 5 — analytic-number-theory source and transplant audit

9 items completed: 6 nothing, 2 covered, 1 interesting.
Interesting: Z2412 corrects the proposed Ustinov/ES continued-fraction statistic.
Primary statements read for all named leads; Z2320 uses an explicitly identified modern source for Wigert, not a fictitious Linnik representation-function paper.
Computations: exact regular/HJ length-three census to 10⁶, and finite-field divisor-box diagnostics.
ES remains OPEN; no new exceptional-set estimate or pointwise theorem is claimed.

## Conventions and provenance

**PROVED (elementary).** The certificate considered here is (★), `p=4abC−a−b`, equivalently a divisor `d=4aC−1 | 4Cp+1` with `d≡−1 (mod 4C)`; its paired divisor is `4bC−1`. This is a sufficient ES certificate, NOT an equivalence with every possible ES solution. An ordered count counts the a/b swap twice. Its expected scale ≍log²p is a heuristic/local-density scale, not a uniform asymptotic. `E_ES(N)` denotes actual ES failures; `E_★(N)` denotes failures of this certificate family and is an upper bound for `E_ES(N)`, not an equal quantity. Odd squares show why this distinction matters.

The baseline published bound is Vaughan's `E_ES(N)≪N exp(−c(log N)^(2/3))`. The repo's exponent 3/4 is INTERNAL, UNREFEREED (`FRONTIER.md:59–65`, `paper/es-threequarter-note.tex`), not a published improvement attributed to Vaughan.

Repository search preceded source retrieval: `git grep` for Gupta/Murty/Pintz/Ruzsa/Ustinov/Harel/Mousset/Sawhney/Linnik and the paper titles. The relevant depth documents are cited in each section. PDFs were read via text extraction, except Gupta–Murty and Montgomery–Vaughan, whose scanned theorem pages were rendered and read visually. Source transcriptions live in `data/z52b/pass2/ZF0/<mid>/`; Gupta–Murty's already archived PDF is `sources/uo/gupta-murty-1984-invent.pdf`.

## Z2078 — Gupta–Murty: covered, with the actual inequality checked

**Source-verified PROVED.** Gupta–Murty, *A remark on Artin's conjecture*, Invent. Math. 78 (1984), 127–130, DOI https://doi.org/10.1007/BF01388719. Read all four scanned pages of the repo PDF (there is an introductory statement rather than a separate abstract). For three distinct primes q,r,s their explicit 13-element monomial set S contains an element which is a primitive root for ≥δX/log²X primes ≤X. This is neither a theorem that all 13 are primitive roots nor the later three-candidate result.

The actual mechanism is unusually precise: Lemma 1 plus distribution beyond level 1/2 gives ≫X/log²X primes whose odd factors of ℓ−1 exceed X^(1/4+ε), with a prescribed quadratic nonresidue. Lemma 2 gives `#{ℓ: |⟨q,r,s⟩ mod ℓ|<Y}=O(Y^(4/3))`. A failure of full generation has size <X^(3/4−ε), so costs O(X^(1−4ε/3)), smaller than the sifted supply. Lemma 4 supplies at least seven odd discrete-log candidates, while each of at most three large odd factors of ℓ−1 eliminates at most two: `7>2·3` forces one survivor. Thus the union lower bound depends on a determinant/nonvanishing lemma and subgroup generation, not on a general inequality for correlated thin events.

**ES transplant (PROVED identities; Assessment of applicability).** For a fixed finite line menu J, put `W_J(p)=Σ_(a,C)∈J 1[p≡−a (mod 4aC−1)]`, with `b=(p+a)/(4aC−1)≥1`. A valid general union bound is
`#{p≤X:W_J(p)>0} ≥ (Σ_p W_J(p))² / Σ_p W_J(p)²`.
It needs actual first and joint moments and gives an average over p, not a certificate for each p. Alternatively sieve the auxiliary prime ℓ at fixed p: the correct per-ℓ set is `A_ℓ=−{c/j:cj|(ℓ+1)/4}`, not a subgroup orbit. Its size is at most τ₃((ℓ+1)/4)=ℓ^o(1), versus a positive-density coset for the unit-orbit argument. Large subgroup generation does not force membership in that bounded exponent box, and the usable ℓ are bounded by O(p²), so one cannot send X to infinity at fixed p.

This actual step is already done in **`FIXED_MODULUS_SHOTS.md` §3, Thm 3.1/Cor 3.2/Assessment 3.3 and §6 Prop 6.1**. Decisive lines: “In ES the set at r is A_r, of r-density ≤ τ₃(k)/r = r^{−1+o(1)}” and “the certifying moduli of p form a finite set bounded by O(p²).” `UNIT_ORBIT_ES.md` §2 explains the different, unbounded relaxed problem. Outcome **covered**, not a new impossibility theorem for arbitrary Artin-inspired methods.

## Z2082 — Pintz–Ruzsa: nothing from the concrete Fourier transplant

**Source-verified PROVED.** *On Linnik's approximation to Goldbach's problem. II*, Acta Math. Hungar. 161 (2020), 569–582, DOI https://doi.org/10.1007/s10474-020-01077-8; full author manuscript https://real.mtak.hu/124682/1/PintzRuzsa200219.pdf. Read the abstract at https://real.mtak.hu/124682 and Theorem 1, Lemmas 6–9 in the manuscript. K=8 is the unconditional 2020 theorem; part I, Acta Arith. 109 (2003), 169–194, supplies K=7 on GRH and the exponential-sum lemma. It is not accurate to cite part I alone as the completed unconditional K=8 proof.

Writing `G(α)=Σ_(j=1)^L e(2^j α)`, Lemma 6 states `|G(α)|<0.789401 L` outside a set of measure `≪N^(−3/5)L^(−100)` (L as in §2). Lemma 9 combines this with prime-pair estimates and moments of G. The Goldbach count has a power-sized N reservoir times powers of log N.

**PROVED ES-side calculation.** A single ES line with fixed a,b and H admissible consecutive C-values has
`S_ab(α)=e(−(a+b)α) Σ_(C=1)^H e(4abCα)`.
At every `α=k/(4ab)` its modulus is exactly H. On intervals of width `1/(100·4ab·H)` about those points it is ≥0.99H (triangle inequality applied to the phase differences); the union has measure ≥1/(100H). Consequently a uniform analogue of the 0.789401 large-value lemma with exceptional measure ≪N^(−3/5)log^(−100)N is false for the short lines H=polylog N, and is maximally false for H=1. Such lines occur when ab is large in the full range `4abC−a−b≤N`. Long lines do have ordinary geometric-sum cancellation, but that alone neither controls the moving family of resonances nor supplies a product `S(α)^2G(α)^8` for ES. One would need a new summed minor-arc bound with error below the log²p main scale (or a one-sided equivalent), not the cited lacunary lemma. No ES exponent follows.

Prior: `BRAINSTORM/s9_lower_tail_literature.md` table and `BRAINSTORM/z31_small_count_pointwise.md` item 3 already distinguish the Goldbach power reservoir; `BRAINSTORM/z52_lit_thin_pointwise.md` Pintz–Ruzsa section checked only the published abstract. The explicit geometric-sum transplant is the additional step here. No numerical Fourier plot is needed for this exact counterexample to the proposed uniform estimate.

## Z2303 — exceptional sets: nothing; identify the precise 3/4 cost

**Source-verified PROVED.** Montgomery–Vaughan, *The exceptional set of Goldbach's problem*, Acta Arith. 27 (1975), 353–370, https://matwbn.icm.edu.pl/ksiazki/aa/aa27/aa27126.pdf. Read the introduction (no separate abstract), Theorem 1 and §§2–3 on scanned pp. 353–355. Theorem 1 gives `E_G(X)<X^(1−δ)` for an effectively computable δ>0. Their weighted sum is `S(α)=Σ_(p≤X)(log p)e(pα)`, with coefficients of S² split into major/minor arcs; zero-density input controls the major-arc exceptions as well, so this is not merely an automatic application of Parseval.

**PROVED comparison identity.** If an ES count were `R(n)=M(n)+r(n)`, with `M(n)≥c log²N` on a dyadic target set, then
`#{n:R(n)=0} ≤ (c log²N)^(−2) Σ_n |r(n)|²`.
To obtain an exponent θ one needs a residual second moment `≪N log⁴N exp(−c'(log N)^θ)`; to obtain a Goldbach-style power saving one needs `≪N^(1−δ)log⁴N`. The Goldbach theorem provides neither bound for the ES restricted-divisor sum. Positive spikes alone do not logically rule out all useful one-sided/truncated decompositions, so no universal variance no-go is asserted.

**Exact internal sieve loss.** Read `paper/es-threequarter-note.tex`, abstract and introduction pp. 1–3 (source lines 35–49, 102–128). Set t=log X. The ordinary class supply is μ≈t²; detecting its void needs order r≈μ, and coefficient-sum/CRT bookkeeping costs `X^O(r)=exp(O(t³))`. Balancing against N gives t≈(log N)^(1/3) and Vaughan's exponent 2/3. Multipliers k≤X^κ increase supply to μ≈t³, but the r≈t³ expansion costs `exp(O(t⁴))`, forcing t≈(log N)^(1/4) and exponent 3/4. The loss is the growing-order joint-class expansion and its interval error, not simply replacing Bombieri–Vinogradov level 1/2 by a slightly better fixed level. `EXCEPTIONAL_KARY3.md` Cor 4.2 caps the audited CRT architecture at this exponent; it does not cap every circle method.

Prior: `EXSET_BEYOND_CRT.md` §4.3 already discusses the Montgomery–Vaughan analogy but explicitly calls its objections Assessments, not a theorem ruling out a new ES L² representation. The requested comparison therefore ends with a missing ES moment estimate, not an imported power-saving theorem. The Elsholtz–Tao Egyptian-fraction counting paper in the item's references is not the source of this repo's internal 3/4 exceptional-set result.

## Z2320 — maximal fluctuations: covered after disambiguating the citation

The item supplies no identifiable title; pass1 even changed “Linnik” to “Harman”. No such unspecified paper is claimed verified. The actual relevant results are Wigert's maximal divisor order plus Linnik's least-prime theorem used in **`BM_CORRECTED_COUNT.md` §3.1, Proposition 3.1**.

**Source-verified PROVED (Wigert quoted in a modern primary paper).** Elsholtz–Technau–Technau, *The maximal order of iterated multiplicative functions*, https://arxiv.org/abs/1709.04799, abstract and §1.1, state
`max_(n≤x) log τ(n)=(log 2+o(1))log x/log log x`.
Their new theorems concern iterates, which are not needed here; this audit does not attribute Wigert to Linnik.

**PROVED ES consequence.** For each fixed C,
`D_C(p):=#{d|4Cp+1:d≡−1 mod4C} ≤ τ(4Cp+1)`;
thus for C≤p^A, uniformly `D_C(p)≤exp(((A+1)log 2+o(1))log p/log log p)`. For a truncated sum C≤B the immediate upper bound has an additional factor B. These are upper bounds, never a positive lower bound or log²p uniform asymptotic.

The repo gives the matching qualitative warning on primes: choose `Q_k=∏_(j≤k)ℓ_j` with ℓ_j≡3 mod4 and a prime `p≡−1 modQ_k`, `p≡1 mod4`, `p≪Q_k^L` by Linnik. Every odd-cardinality divisor d|Q_k gives the distinct certificate `(a,b,C)=(1,(p+1)/d,(d+1)/4)`. Hence `R(p)≥2^(k−1)≥exp((log2/L−o(1))log p/log log p)` infinitely often. Use any admissible fixed L; no claim about the best L is necessary. The decisive prior line is “every two-sided hypothesis |R−M|≤E with E=(log p)^O(1) … is false infinitely often.” This actually completes the requested fluctuation step, so outcome **covered**. Original Wigert/Linnik papers were not re-read; the modern statement and the full elementary transplant proof were checked.

## Z2389 — Green–Sawhney: nothing for fixed-p divisor classes

**Source-verified PROVED.** https://arxiv.org/abs/2410.04189, *Primes of the form p²+nq²*, submitted 2024; the retrieved PDF is v3 (6 June 2026). Theorem 1.1 for fixed n≡0,4 mod6 is
`Σ_(x,y) Λ(x)Λ(y)Λ(x²+ny²)W(x/N,y/N) = κ_n N²∫W + O_(W,n)(N²(log log N)²/log N)`.
Proposition 4.3 is the precise Type II input: for product-form ideal weight w built from 1-bounded f,f′, a bilinear sum of size ≥δX at norm level `δ^(−C)≪L≤X^(3/8)` forces both appropriate U^k norms to be ≥`(δ/((|ℓ|+1)log X))^O(1)`. The remark allows L≤X^(1/2−κ) with k depending on κ. Theorem 1.1 uses Gowers uniformity of Λ−Λ_Cramér, not arbitrary prime-looking or divisor weights.

**Transplant calculation/Assessment.** The ES Type I expression is `p²+4dc²` with p fixed, c,d varying, and divisor `g≡−p (mod4cd)` (not the ★ residue −1). One could set n=4d and (x,y)=(p,c), but the theorem fixes d and averages both x,y. Isolating x=p by a normalized smooth window of width 1/N makes its first three derivative bounds grow like N³; the published error is then not small even compared with the N-sized row count. More fundamentally, the demanded weight `1[g|p²+4dc²]1[g≡−p mod4cd]` couples the divisor to c,d and is not the paper's independent-coordinate product-form weight. Neither its relevant Gowers norm nor Type II estimate is supplied. Allowing d to vary also loses the fixed-field constants.

A simple sanity check shows why prime values are not the desired output: for p≡1 mod4, if `p²+4dc²` itself is prime then its only divisors are 1 and that prime, both ≡1 mod4, whereas g must be ≡3 mod4. Such a prime value gives no Type I certificate on that line. Thus the very event counted by the source is not a certifying divisor event. No exceptional-set exponent or fixed-p equidistribution follows.

Prior: `BRAINSTORM/z45_recent_pointwise_tools.md` §5 (around lines 93–116), `BRAINSTORM/z52_lit_thin_pointwise.md` Green–Sawhney section, and `FIXED_MODULUS_SHOTS.md` §4 give the family/fixed-p distinction and the exact residue. This audit additionally checks Proposition 4.3 rather than stopping at the title/abstract.

## Z2399 — FKM: nothing; actual indicator fails the advertised trace-weight test

**Source-verified PROVED.** Fouvry–Kowalski–Michel, *Algebraic trace functions over the primes*, https://arxiv.org/abs/1211.6043, Definition 1.3 and Theorem 1.5. For a nonexceptional geometrically isotypic pure weight-0 middle-extension Fourier sheaf, with conductor c, the unsmoothed bound is
`Σ_(p≤X)K(p) ≪_η,c X(1+q/X)^(1/12)q^(−η/2)`, `η<1/24`.
Constants are polynomial in c; the bounded-conductor nontrivial range is X≥q^(3/4+ε). Exceptional constituents include `χ(x)ψ(x)`, including constants and pure additive characters. “Arbitrary residue indicator” is not a hypothesis of this theorem.

**PROVED local identification.** `FIXED_MODULUS_SHOTS.md` Thm 3.1 has
`A_q=−{c/j:cj|(q+1)/4}`, q prime ≡3 mod4, and local failure on units `F_q(x)=1−Σ_(r∈A_q)δ_r(x)`.
This is failure of certification by ONE q, not full failure of the integer shots, which depends on their other prime/divisor factors and is not determined by p modq. The full box has m=|A_q|≤τ₃((q+1)/4)=q^o(1). The direct construction is a constant plus m point-supported functions, not a nonexceptional middle-extension trace weight. Fourier-expanding each δ uses pure additive characters, precisely excluded by Theorem 1.5. A fixed finite menu may have boundedly many such points, but the same exclusion still applies; growing-box complexity is an additional problem, not the sole problem.

There is a direct contradiction to treating F_q itself as a uniformly bounded-conductor nonexceptional trace weight: at X=q,
`Σ_(p≤q)F_q(p) ≥ π(q)−m−1 ≍q/logq`,
whereas Theorem 1.5 would give `O(q^(47/48+ε))`. Centering removes this immediate contradiction, but no admissible bounded-conductor representation for the centered divisor-box function is furnished by the paper. We do NOT assert a lower bound for the minimal conductor of every imaginable sheaf representation. Even a hypothetical generic error `q^(47/48+ε)` dwarfs the expected success main term m/logq, so it cannot prove that this sparse class union contains a prime below q.

**CERTIFIED finite diagnostic.** `scripts/z52d_p2_ZF0_Z2399_box.py` independently compares the quotient-box and direct cube residue sets. `(q,|A_q|)` is `(7,3),(11,3),(19,3),(31,5),(127,7),(942479,1977),(999983,127)`, all residues quadratic nonresidues. The last two local prime-failure densities are 0.9979023383 and 0.9998729977. These are explicit point-term counts, NOT measurements of minimal sheaf conductor. For each fixed q, ordinary PNT in arithmetic progressions gives the exact limiting prime-failure density `1−m/(q−1)`; no FKM input is needed. Reproduce with `ulimit -v 8000000; timeout 30s uv run python scripts/z52d_p2_ZF0_Z2399_box.py`. Prior treatment is `FIXED_MODULUS_SHOTS.md` §§3,6, which does not contain this FKM hypothesis test.

## Z2403 — Ford–Maynard: nothing, but distinguish admissible weights from detector

**Source-verified PROVED.** https://arxiv.org/abs/2407.14368 (2024 v1), abstract, equations (I),(II), Theorems 2.1–2.2. The target is `Σ_(ℓ prime)a_ℓ` for arbitrary nonnegative sequences compared with b_n, with `w_n=a_n−b_n`. Type I controls divisor sums with m≤x^γ; Type II controls all divisor-bounded bilinear coefficients for `(x/2)^θ<m≤x^(θ+ν)`. Theorem 2.1 constructs bounded a_n with a_ℓ=0 at every prime despite those estimates when ν≤ν₀(γ). Theorem 2.2 characterizes the asymptotic region by (A1),(A2). This is a genuine optimal-information theorem for a prime detector.

**PROVED encoding; Assessment of failed hypothesis.** It is false to say divisor conditions are forbidden as *weights*: for fixed target p define on a dyadic d-range
`a_d=Σ_(C≤B)1[d|4Cp+1]1[d≡−1 mod4C]`.
This nonnegative sequence is formally admissible if a comparison b_d and the paper's Type I/II estimates are proved. A lower bound on `Σ_(ℓ prime)a_ℓ` would yield the stronger prime-divisor certificate. But the source proves no such estimates for these fixed-p divisor weights, and its detector does not count arbitrary composite d.

Concrete distinction: `p=103,C=2`, `8p+1=825=3·5²·11` has d=15≡7 mod8 and cofactor 55≡7 mod8, yielding `(a,b,C)=(2,7,2)`. None of its prime factors is 7 mod8. Hence prime-divisor detection can miss a genuine line certificate. Alternatively choosing a_n as an ES witness count and detecting prime n would only count primes *with* witnesses on average. No theorem here bounds ES failures by more than Vaughan, nor do the authors' prime-free examples prove a parity barrier for all divisor-class targets. Prior relevant discussion: `EXSET_BEYOND_CRT.md` §4.3 (Type I/II on avoider weights); no earlier Ford–Maynard application found.

## Z2408 — HMS: nothing after writing the exact polynomial

**Source-verified PROVED.** Harel–Mousset–Samotij, *Upper tails via high moments and entropic stability*, https://arxiv.org/abs/1904.08212, abstract and Theorem 3.1. For a fixed degree d, a nonzero polynomial X in independent identically distributed Bernoulli(ρ) coordinates, with nonnegative coefficients, suitable Φ_X lower bound and an entropically stable family of cores, the theorem sandwiches `−log P(X≥(1+δ)EX)` between `(1±ε)Φ_X(δ±ε)`. Section 3's preliminary moment definitions allow general measures; the stated sharp theorem specifically assumes independent Bernoulli inputs. This distinction is important here.

**PROVED polynomial identities.** For a finite ★ menu J (with validity/positive-b checks absorbed into the indicators), let `I_j(n)` indicate its jth certificate and put
`E_J(N)=Σ_(n≤N) ∏_(j∈J)(1−I_j(n))`.
This is a multilinear polynomial of degree |J| with alternating signs in success coordinates. In failure coordinates `Y_j(n)=1−I_j(n)` it has nonnegative coefficients, but its degree grows with the menu, and the arithmetic coordinates are correlated, neither independent nor identically distributed Bernoulli variables. Moreover E_J(N) is a deterministic count. Choosing n uniformly makes ONE row random with mean E_J(N)/N; it does not make all its arithmetic coordinates independent. The ★ family only yields `E_ES(N)≤E_J(N)` for sufficiently exhaustive J, not equality.

For literal equality, take the finite set T_N of all sorted denominator triples capable of solving 4/n for n≤N and let `I_t(n)=1[4xyz=n(xy+xz+yz)]`. Then
`E_ES(N)=Σ_(n≤N) ∏_(t∈T_N)(1−I_t(n))`.
Finiteness can be made explicit: `n/4<x≤3n/4`, `y≤2nx≤3n²/2`, and `z=nxy/(4xy−n(x+y))≤nxy≤9n⁴/8`, so all triples lie below 2N⁴. Again it is a growing-degree correlated deterministic polynomial, not an HMS input. Declaring each whole row-failure to be a new degree-one variable merely hides the unknown mean E_ES(N)/N in that variable's distribution.

**Precise missing estimate.** Averaging products of k arithmetic indicators requires counts of simultaneous congruences. For prime-line indicators with moduli q_j, the count is `N/lcm(q_j)+O(1)` when compatible, but the O(1) errors accumulate over the growing-order expansion. Replacing these by independent probabilities is exactly an unproved high-correlation/CRT-to-interval transfer. Entropic stability has not been established either. A model with independent sparse witnesses of mean μ≈log²n would predict zero probability around exp(−μ); that is a MODEL assumption, not an application to ES. Thus no exponent beyond 2/3 (or the internal 3/4 result) results. Prior: `EXSET_BEYOND_CRT.md` §4.2 already identifies these high-lcm factorial moments as simultaneous restricted-divisor correlations; no prior HMS-specific verification found.

## Z2412 — interesting: the proposed Ustinov statistic is not the ES statistic

**Source-verified PROVED.** The actual relevant paper is Ustinov, *On the number of solutions of the congruence xy≡l (mod q) under the graph of a twice continuously differentiable function*, Algebra i Analiz 20:5 (2008), 186–216; St Petersburg Math. J. 20:5 (2009), 813–836. Full English author PDF: http://www.iam.khv.ru/articles/Ustinov/nth20_eng.pdf. Read its abstract and Theorems 1–2. Theorem 1 estimates modular-hyperbola points below a smooth curved graph with explicit curvature/gcd-dependent Kloosterman error. Theorem 2 is
`Σ_(1≤a≤b,(a,b)=1) s_x(a/b) = 2φ(b)/ζ(2) [log(1+x)log b+C(x)] + O_(ε,x)(b^(5/6)log^(7/6+ε)b)`.
Here `s_x` counts positions of REGULAR continued-fraction tails falling in [0,x]; x=1 gives the total regular Euclidean length. It does NOT give `#{a:s(a/b)=3}`. The earlier 2005 paper is *On the statistical properties of finite continued fractions*, https://www.mathnet.ru/eng/znsl401, whose abstract averages Gauss–Kuzmin statistics over a growing disk in (a,b); this also is not a fixed exact-length-three theorem.

For cross-checking, Bykovskii–Frolenkov, *The average length of finite continued fractions with fixed denominator*, Sb. Math. 208 (2017), 644–683, DOI https://doi.org/10.1070/SM8718, Theorems 1–2 improve the fixed-denominator errors to `b^(17/21+ε)` (general x) and `b^(23/29+ε)` (x=1). Their introduction explicitly attributes the previous formula to Ustinov. These are large mean-statistic errors, not small-count errors.

**PROVED ES specialization.** At b=p, Ustinov gives a regular-length sum with main term ≍p logp and error `p^(5/6)log^(7/6+ε)p`. The ES₅ dictionary instead uses **negative Hirzebruch–Jung length** `r(p/A)` and a quadratic-nonresidue restriction; for p≡1 mod8 the target is λ(p)≤3. It is not ordinary CF length≤3. `DEDEKIND_ES.md` Lemma 1.1, Thm 4.5 and Cor 4.6 prove this dictionary; the R276 correction in §2 also matters. Even the newer error p^(23/29+ε) vastly exceeds the expected log²p number of short HJ witnesses. A mean-length statistic cannot be inverted into an exact length-three count, and introducing the Legendre twist is another new hypothesis.

**CERTIFIED exact substitute for the nonexistent claimed count.** This is explicitly a direct enumeration, not a numerical verification of an Ustinov exact-length theorem:
* Canonical regular `[0;x,y,z]`, x,y≥1,z≥2, has denominator `b=xyz+x+z`, numerator `a=yz+1`.
* HJ `[[v,t,u]]`, t,u,v≥2, has numerator `b=tuv−u−v`, denominator `A=tu−1`.
Both parametrizations are unique and reduced. `scripts/z52d_p2_ZF0_Z2412_cf.c` enumerates both to b≤10⁶ and cross-checks against independent Euclidean algorithms for all **76,115** reduced fractions with 2≤b≤500. The large census costs O(N) memory; no pair/triangle Cartesian arrays occur.

| b | regular length 3 | HJ length 3 | HJ length 3 with (A/b)=−1 (b≡1 mod8) | HJ middle entry divisible by 4 |
|---|---:|---:|---:|---:|
| 17 | 7 | 2 | 2 | 0 |
| 25 | 6 | 4 | 0 | 0 |
| 41 | 12 | 2 | 2 | 2 |
| 49 | 12 | 6 | 0 | 0 |
| 241 | 26 | 14 | 6 | 0 |
| 409 | 38 | 16 | 8 | 0 |
| 577 | 45 | 28 | 18 | 0 |
| 5569 | 70 | 32 | 16 | 0 |

Across all **19,552 primes p≡1 mod8 up to 10⁶**, regular length-three total = **2,766,831**, HJ length-three total = **1,929,022**, and HJ nonresidue total = **1,350,392**; none has zero HJ nonresidue witnesses. All odd-square controls have zero HJ nonresidue witnesses. This does not extend the existing ES₅ range in `DEDEKIND_ES.md` §4.6 (already 10⁶); the new comparison is the different regular statistic and independent formula cross-check. It is useful because transplanting the wrong CF convention can falsely manufacture a source theorem for ES.

Reproduce:
```
timeout 20s gcc -O2 -Wall -Wextra scripts/z52d_p2_ZF0_Z2412_cf.c -o /tmp/z2412_cf
(ulimit -v 8000000; timeout 180s nice -n 10 /tmp/z2412_cf 1000000)
```
Outputs: `data/z52b/pass2/ZF0/Z2412/counts.csv`, `check.txt`. Next mathematical input would have to be a **twisted, short negative-CF cylinder count at each prime denominator with error o(log²p)**; neither Ustinov nor the later mean-length improvement supplies it.
