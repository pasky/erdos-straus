# OAI_DUMP_IMPACT — fixed zero-free strips change the tools, not ES

**Assessment, 2026-10-21.** The supplied collection would substantially strengthen the campaign's pointwise **relaxations**, effectivity, and algorithmic baseline if its claims survive verification. Family 003 gives least quadratic nonresidues and forced windows of size `O(log⁸ n)`, hence an effective `e*(n)≪log⁸ n`; it also suffices for `M_gen(p)≥(1−o(1))log log p` and, by an additional Halász argument, the **full BM main-term asymptotic**. It does **not** give a polylogarithmic least prime in an arbitrary progression, GRH-quality square-root errors, or Kummer-field GRH. A less obvious positive finding: **029's technical propositions, not merely its Artin headline, imply the one-fixed-mute-prime relaxation**. Neither finding supplies a divisor-class hit at cap zero. ES remains open, including after accepting all the audited claims.

**Verdict: PARTIAL — substantial conditional-on-the-dump tool upgrades; B2 unchanged. Promise for a new ES route: 1/5.** Every consequence below remains **CONDITIONAL on the specified unrefereed manuscript claims**. “New unconditional statement” in the table means what becomes unconditional *if those claims are accepted as theorems*, not what this audit establishes unconditionally today.

## Summary table

**Status convention for every family row: CLAIMED (OAI dump, unrefereed).** “L” adds “Lean-formalized per supplied comparator”; no independent Lean execution was possible. Exact quoted theorem environments, hypotheses, and scope pages are in the linked excerpts; formula summaries below do not replace them.

| Family | Claim | Lean? | Campaign items affected | New unconditional statement if accepted | Caveats |
|---|---|---|---|---|---|
| [003](sources/oai2026/003-excerpts.md) | Dirichlet/zeta and finite-order Hecke over `Q(√−3)` zero-free for `Re s>7/8`; real-zero logarithmic gap | L | A5/A6/A9/A12; CAP_POINTWISE/DOWN; M_gen, M_BM; SW/BV effectivity | `r(p),q*(n),e*(n)≪log⁸(2n)`; deterministic QNR in P; `M_gen≥log₂p−log₃p−O(1)`; `M_BM∼(3/(2π²))log²p`; effective Thm U and moving-window bound | Not GRH; not cap zero; all constants in these deductions effective but not numerically evaluated |
| [142](sources/oai2026/142-excerpts.md) | Deterministic dense polynomial factorization over prime fields in `O(((n+1)⌈log₂p⌉)^(10¹²))` bits | No located formalization | A5/A6/A7 | Prime-field square roots and QNR finding in P | Depends on 029's wider Hecke claim; not integer factoring; redundant for QNR if 003 holds |
| [029](sources/oai2026/029-excerpts.md) | Every admissible fixed base is primitive at `≫_a x/log²x` primes in `(x,2x)`; wider Hecke strip | No located formalization | A14, FROBENIUS_FIRING | **One fixed odd mute prime suffices for every n coprime to it**, using its fixed-progression reservoir and splitting bound (§4) | Main headline alone insufficient; constants depend on n,s; no small cap or V_phi theorem deduced |
| [007](sources/oai2026/007-excerpts.md) | Ordinary affine two-point Liouville correlation `O_forms(X/log^cX)`; corrected Elliott | L | Parity/hatch proposals | No ES or exceptional-exponent upgrade established | Fixed forms, two-point average; no uniform divisor-supported estimate |
| [011](sources/oai2026/011-excerpts.md) | PD(1) law for factors of `p−1`; `x^δ`-smooth predecessors at `x^(1−o(1))` primes; even-Ω squarefree predecessors infinitely often | No located formalization | Smooth-window proposals; input to 029 | Supplies technical reservoir machinery used by 029; no direct ES statement | Fixed shifts and power-scale averages, not `(p+q)/4` in a prescribed polylog window |
| [012](sources/oai2026/012-excerpts.md) | Joint Dickman density `ρ(1/a)ρ(1/b)` for `n,n+1` | L | Factorization-independence heuristics | None at fixed ES input | Density in n, fixed a,b; no residue classes of divisors |
| [015](sources/oai2026/015-excerpts.md) | Complete real torus-packet equidistribution in specified prime/quartic/sextic degrees | L for prime degree only | CONDITIONAL_ES §4 | None | Not quadratic CM points, not shrinking targets, no requisite rate |
| [020](sources/oai2026/020-excerpts.md) | Positive predicted density of `(d−2)`-power-free polynomial values, d≥4 (new paper range 4–8) | L, endpoint all d≥4 | Polynomial-shape approaches | None | Power-free shape is not a specified divisor class |
| [021](sources/oai2026/021-excerpts.md) | `h(k)≪k²/(log log(3k))²`, uniform interval position/modulus | L | Covering/sieve designs | Stronger coprime-in-interval tool | Survivor need not be prime, nonresidue, or divisor of prescribed N |
| [025](sources/oai2026/025-excerpts.md) | Worst-case distinct Egyptian-fraction length `Θ(log log b)` | L | Unit-fraction comparisons | Short many-term expansions, not an ES upgrade | Already `4/b` has a ≤4-term expansion by greedy descent; headline does not reach 3 |
| [028](sources/oai2026/028-excerpts.md) | Uniform finite component size for every fixed Gaussian-prime step bound D | L | Trapped forest/walk analogies | None transferred | Proves trapping, not escape; no uniform bound across growing D |
| [023](sources/oai2026/023-excerpts.md) | Patterson cubic Gauss-sum first moment `(6/5)c_*X^(5/6)/log X+o(...)`, fixed angular modes | L | Analytic-method comparison | None directly | Over Eisenstein primes; not a tied-modulus divisor sum; 003 explicitly does not use this result |
| [026](sources/oai2026/026-excerpts.md) | For every fixed C>0, positive lower density of gaps `>C log p_n` | L endpoint includes full claim | Prime-gap analogies | None | Prose Lean scope page is narrower than actual comparator; large gaps do not force ES witnesses |
| [027](sources/oai2026/027-excerpts.md) | Potential integral density on curve character varieties | Supporting lemma only | Hasse/log-K3 comparisons | None | Not integral BM sufficiency on the positive ES surface |
| [182](sources/oai2026/182-excerpts.md) | Power savings for intersective polynomial-difference-free sets, including prime arguments | L for square differences only | Exception propagation analogies | None without a propagation law | Prime-argument paper uses 003; ES exceptions have no proved difference-avoidance property |
| [279](sources/oai2026/279-excerpts.md) | Exact probability-one quantum integer factoring over a fixed finite gate set | L | Factoring-assisted search A7 | A different computational resource, not classical FP | Does not establish FQ, ordinary ES, or classical integer factoring |

## 1. Provenance, scope, and formalization audit

**CERTIFIED (static source inventory, not proof certification).** Checkout `/tmp/oai-math`, HEAD `1581d4cbdd69a0faf34b2089614fe2a814316a6a`; source URL https://github.com/openai/math . The supplied README/history advertise 719 manuscripts, 372 families, and 300/719 top-line results formalized. The October 7 history withdraws three Hodge/K3 manuscripts after a stabilization-trace sign error, lists 14 other revisions, and 13 consequential reference updates. These are reasons to audit dependencies, not evidence that unrelated mathematics is either correct or incorrect. This report assesses that snapshot; it does not independently authenticate the public release. `LITERATURE_2026_UPDATE.md` missed it; no existing campaign file is edited here.

The campaign keyword harvest uses the requested `git grep` terms and is retained compressed. Relevant antecedents include `FRONTIER.md` §§2–7, `BREADTH_Z45.md` §5, the brainstorm index, `BRAINSTORM/z45_siegel_dichotomy.md`, `HARDNESS_MAP.md`, and the cap/count/exception documents cited below. In particular, “no Siegel zero” was already studied as a possible B2 input. The present new input is a **fixed all-height strip**, much stronger than removing a real exceptional zero.

### 1.1 What the machine-readable endpoints actually assert

**CERTIFIED (source inspection).** The comparator for 003 uses Mathlib's actual Dirichlet `LFunction`:

> `... (χ : DirichletCharacter ℂ q) ... (hs : (7 / 8 : ℝ) < s.re)`
> `(hpole : ¬ (χ = 1 ∧ s = 1)) :`
> `_root_.DirichletCharacter.LFunction χ s ≠ 0`.

The solution is `OAI.NumberTheory.DirichletL.Nonvanishing`, theorem `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`. Its final assembly calls `SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero`; there is no additional analytic hypothesis at that endpoint. The Hecke comparator constructs finite-order characters on Eisenstein residue rings, trivial on units, and defines the continuation through a theta Mellin transform. Identifying that bespoke construction with the conventional Hecke function is an additional semantic audit, unlike the directly Mathlib-based Dirichlet endpoint. It is not needed for the Dirichlet deductions here.

The checked endpoints agree with the stated mathematical scope for 007, 012, prime-degree 015, 021, 023, 025, 028 and 279. This means **statement-level agreement**, not validation of thousands of supporting proofs. Important qualifications:

* **011, 029, 142:** no matching formalization located in the manifest/docs; do not inherit a Lean badge from 003.
* **015:** arbitrary-local-type prime degree ≥5 only; quartic and sextic companions are not covered by its comparator.
* **020:** `allDegrees` covers every degree ≥4 with irreducibility over Q and local admissibility; the manuscript's new proof range is 4–8, completed using the cited higher-degree theorem.
* **026:** `lean/docs/026.md` describes only prime-ratio increases. Actual `PrimeGaps.lean`/`RatioCorollary` endpoint `large_gaps_and_ratio_density` is a conjunction including **all fixed C>0 large-gap lower densities**. The implementation's `LargePrimeGaps.main` supplies that component. The page understates the endpoint; it is not evidence of missing coverage of the headline.
* **027:** the formal statement starts with an existing diagram solution and proves seam compatibility of produced values. Potential integral density is explicitly outside its scope.
* **182:** the square-difference case, not general intersective polynomials or prime arguments, is formalized.

**CERTIFIED (limited lexical audit).** Starting at each comparator's configured solution module, the script follows local `OAI.*` imports and records `sorry`, `admit`, `axiom`, `sorryAx` hits, streaming one source file at a time. There are no missing local imports. Representative closure sizes: 003 Dirichlet 2,924 modules; its separate Siegel theorem 306; 007 two-point 1,539; 012 1,792; 015 877; 021 819; 023 3,594; 025 290/58; 028 41. All 16 distinct lexical hits were manually read: they are English comments (“admit”, “not an axiom”, etc.), **not proof admissions or axiom declarations**. Complete per-endpoint records are in `data/z47_oai_impact/lean-audit.json`.

Comparator challenge files intentionally contain `sorry`: they are templates specifying the goal, **not the solution proof**. The inspected configurations allow only `propext`, `Quot.sound`, `Classical.choice`, with `enable_nanoda: false`. Neither `lean` nor `lake` is available on PATH here. No comparator run, `#print axioms`, external-kernel verification, Mathlib import audit, or full definition-equivalence audit was performed. A clean lexical scan cannot replace any of those checks; “CLAIMED … Lean-formalized” remains the appropriate label.

### 1.2 Manuscript claims, dependencies, and plausibility screen

**All statements in this subsection are CLAIMED (OAI dump, unrefereed), with the formalization qualifications above.** Quotes below identify especially consequential assertions; the numbered excerpt files quote the remaining main theorems verbatim, not just their abstracts.

**003.** Main theorem:

> “Every finite-order Hecke L-function over F=Q(√−3) has no zero in Re s>7/8. The same holds for every Dirichlet L-function, including ζ(s). A pole at s=1 for a principal character is allowed.”

The boundary is excluded from the zero-free region, not from the allowed zeros. A companion proves `11/12`; another states `∃c>0: (1−β)log q≥c` for every real zero of every primitive nonprincipal real character, q≥3, both parities. Its formalization supplies no numerical c. **No contradiction with RH/GRH or known zeros is apparent:** a fixed 7/8 strip is weaker than GRH but vastly beyond the established classical region. This is not a routine density improvement.

The claimed mechanism is specific: complete cubic-theta sums over Eisenstein integers retain indices `cn³` (including common factors), compare a reflected expansion with Poisson summation, decompose nonzero frequencies as `ua⁶`, and identify the principal Euler quotient as a reciprocal of the target L-function times a nonvanishing factor. Quadratic/sextic/planar large-sieve moments control the other rows. A continuation argument across the supremum β_* of zero real parts first gives 11/12; prime compensation, asymmetric scales, and extra moments yield 7/8. Fixed-character constants may depend on the character; the **exponent margins** must not. The reflection, zero-on-nonunit conventions, principal-term noncancellation, and uniform continuation margin are the critical proof obligations. Its cited cubic first-moment manuscript 023 is explicitly **not an input**, nor is the GRH-conditional prime asymptotic of Dunn–Radziwiłł. This screen identifies the mechanism; it does not verify it.

**142/029/011 dependency chain.** The exact 142 theorem says “a uniform deterministic algorithm”, prime p **in binary**, **nonzero dense** degree-n polynomial, complete monic irreducible factors and multiplicities, absolute bit bound with exponent `10¹²`, no random/factoring/primitive-root oracle and no GRH. Its §10 explicitly imports **029 Theorem 1.2**, zero-freeness for finite-order Hecke functions over every cyclotomic field containing μ₁₂ in `Re s>1−10⁻⁶`; 003's `Q(√−3)` statement alone is not that theorem. Family 029 constructs a broader version of 003's reflection/Poisson method rather than citing the narrow theorem as sufficient. Its marked Type-II input is from 011's PD paper; it also cites the weighted-dilation and prime-predecessor machinery. The PD paper in turn uses the dilation/ideal-kernel results of the weighted-dilation paper; the latter distinguishes its smoothness conclusion from the stronger PD law. These claims are not independent corroborations of one another.

029's primitive-root theorem concerns every integer a neither −1 nor an integer square, with constants depending on a, lower bound `c_a x/log²x` for **every sufficiently large dyadic interval**. It does not claim the full Artin density. The simultaneous-prime-bases companion explicitly assumes four analytic/sieve inputs. No conflict with established Artin obstructions is apparent. Crucially, §2 contains a fixed-progression prime reservoir and a q-uniform splitting estimate. These permit the extra deduction in §4; dismissing 029 solely because the headline lacks a progression would miss real content.

**007.** Its affine Liouville quote has fixed positive slopes, nonnegative intercepts, nonzero determinant, an absolute c>0, and a constant depending on all four coefficients. Corrected Elliott requires uniform nonpretentiousness, not merely nonperiodicity. No contradiction with known two-point results is apparent. It is genuinely stronger than logarithmically averaged Chowla, but is not uniform in a growing ES input p or in arbitrary divisor weights. No external-dump theorem dependency was identified in the relevant introduction/source-reference screen.

**011/012.** The PD statement is ordinary equal weighting over primes; finite-dimensional convergence is for fixed k and bounded continuous test functions. Smooth predecessors use fixed `0<δ<1/4`; the even-Ω companion asserts infinitely many squarefree p−1 of even Ω. The joint Dickman statement is for fixed a,b∈(0,1), thresholds `n^a,n^b` at n and n+1. These agree with the usual predicted laws; no evident contradiction, but they are distribution/averaging breakthroughs, not deterministic assertions about each shifted integer. No cross-dump input into 012 was identified in the source-reference screen.

**015/020.** Prime-degree complete packet measures converge weakly with no escape of mass; the companions concern primitive totally real quartic **orders**, and primitive sextic **maximal-order ideal-class packets**. Companion citations are not a rate uniform in degree, a quadratic CM result, or a shrinking-target estimate. 020 has irreducibility and a positive local Euler product, so it does not assert squarefreeness in the presence of a fixed square divisor. Its higher-degree completion cites Browning, not another dump theorem. No direct contradiction was found in these statements; neither local admissibility nor weak equidistribution supplies the ES real-positive integral point.

**021/025/028.** Jacobsthal's quantifiers are all moduli with at most k distinct factors and every signed interval start. The small `log log(3k)` at k=1 is harmless with an unspecified constant. No conflict with known lower bounds is apparent. 025 explicitly maximizes over numerators; its Θ lower bound is not a lower bound for each fixed numerator. Its proof uses a freely chosen auxiliary denominator, residue-selected divisors, exceptional-set descent, and adding two short expansions; these operations increase the number of terms. 028's main theorem is a uniform component bound, stronger than merely no infinite path. The claimed finite periodic sieve obstruction deletes zero classes modulo finitely many split Gaussian primes, then uses geometric sampling, coverage transfer and entropy budgets for bounded-increment self-avoiding walks. The uniformity over the starting point is genuinely in the comparator. None of these statements immediately contradicts an established theorem located in this screen; their claimed proofs still require specialist checking. No cross-dump theorem input was identified in their source-reference screen.

**023/026/027/182/279.** Patterson's normalized cubic moment and fixed angular-mode companions concern a prime average of size `X^(5/6)/log X`, not individual ES factorizations. 026's large-gap lower density is compatible with mean-gap bounds because its c(C) may tend to zero with C. 027 allows a finite extension of the number field and changes the variety/problem; positive rational ES denominators are not a specialization. 182's prime-argument theorem explicitly imports 003 and companion difference-set machinery; even a valid power saving cannot apply to ES exceptions without a difference-avoidance theorem. 279 is an **exact quantum**, not classical deterministic, complexity assertion. No contradiction is identified by these scope checks. This is a deliberately limited plausibility screen, not a referee report or a probability of correctness.

The full catalogue was searched for progression/least-prime/nonresidue/character-sum/Burgess/divisor/BV/EH/sieve/class-number/CM/Kloosterman/Hasse/log-K3/Zaremba/continued-fraction/unit-fraction terminology. Additional hits include 027, 182, 279 above; 159 is additive-pattern density rather than a multiplicative divisor-class theorem. The Hodge/K3 and Oka hits concern complex geometry, not the integral Hasse principle on `U_n`. No ES theorem, Zaremba/continued-fraction theorem giving the required ES transport, or single-integer tied-modulus divisor lower tail was located. This is a catalogue-level negative search, not a proof that no hidden lemma could be useful.

## 2. What a fixed strip actually gives: derive the exponent

**Definition.** `H_θ` means every primitive Dirichlet L-function, including ζ, has all nontrivial zeros in `Re s≤θ`, for a fixed `1/2≤θ<1`. By functional equation and conjugation their real parts are also ≥1−θ. Constants below depend effectively on θ. Family 003 asserts `H_(7/8)`.

### 2.1 Smoothed explicit formula and fixed-density detectors

**PROVED implication, conditional on H_θ.** For a character χ modulo Q, put

```
Ψ₁(x,χ) = Σ_{m≤x} Λ(m)χ(m)(1−m/x).
```

For primitive χ of conductor q the standard Mellin kernel is `1/(s(s+1))`, so shifting the contour in

```
(1/(2πi)) ∫_{(2)} −(L′/L)(s,χ) x^s/[s(s+1)] ds
```

gives a principal contribution `δχ x/2`, zero contribution `−Σ_ρ x^ρ/[ρ(ρ+1)]`, and trivial-zero/archimedean terms bounded by `O_θ(log(2q)+log(2x))`. Possible residues at zero are included in this bound. Using the functional equation to keep nontrivial zeros away from zero and the standard zero count

```
N(T,χ) ≪ (T+1) log(2q(T+2)),
Σ_ρ 1/|ρ(ρ+1)| ≪_θ log(2q),
```

(the second follows by dyadic summation/integration against `(1+T²)⁻¹`) yields

```
Ψ₁(x,χ) = δχ x/2 + O_θ(x^θ log(2Q) + log(2Q)log(2x)).             (2.1)
```

The last term safely covers removing prime powers of primes dividing an inducing modulus Q. This uses **zero counting**, not an unproved stronger zero-density theorem. With only one unsmoothed cutoff an extra logarithm is easily lost; that would incorrectly turn 8 into 16 for the least-prime deduction. The explicit formula/zero-count ingredients are the classical ones used in the campaign's Ankeny estimates; the exponent computation is given here rather than imported from a GRH bound.

Let a nonnegative detector on units modulo Q have expansion

```
f(a)=Σ_χ cχ χ(a),      cχ₀=δ>0,      B=Σ_χ |cχ|.
```

Its smoothed prime-power sum is `δx/2+O_θ(Bx^θlog(2Q)+B log(2Q)log(2x))`. Since `|f|≤B`, the contribution of powers of primes with exponent ≥2 is `O(B√x log²(2x))`. Thus a **prime** detected by f exists once

```
x^(1−θ) > C_θ(B/δ)log(2Q),
δx > C B√x log²(2x),                                            (2.2)
```

and the harmless logarithmic error is absorbed. For fixed B,δ and θ=7/8, the second inequality is automatic at `x=C(log(2Q))⁸` for sufficiently large C; finitely many small Q are absorbed effectively. This proves

```
A(θ)=1/(1−θ),               A(7/8)=8.                            (2.3)
```

At θ=1/2 this recovers the familiar exponent 2 for fixed-density detectors: the prime-power/main ratio is `O((log log Q)²/log Q)`, which tends to zero. For the weaker 11/12 manuscript, the same argument gives 12.

**Examples, PROVED relative to H_(7/8).** A quadratic nonresidue uses `(1−χ)/2`, δ=1/2, B=1. A compatible pattern of k independent quadratic signs uses `2^(−k)∏(1+ε_jχ_j)`, δ=2^(−k), B=1. Fixed k gives a `log⁸ Q` prime. The pattern's compatibility is essential: if a purported nonprincipal product is actually principal with the wrong sign, δ is zero and there is no conclusion. Odd-square n is exactly such a failure for χ_n=−1.

### 2.2 An arbitrary progression is NOT a fixed-density detector

For a single reduced class a modulo Q, δ=1/φ(Q), B=1 by character orthogonality. Formula (2.2) gives, at θ=7/8,

```
least prime ℓ≡a (Q) ≪ (φ(Q)log(2Q))⁸,                          (2.4)
```

not `log⁸ Q`. Prime-power removal is harmless on this much larger scale. This is weaker than the campaign's effective Linnik exponent 5 for general Q. A uniform polylog least-prime bound for **all** reduced classes is impossible by counting: fewer than φ(Q) primes lie below any fixed power of log Q for large prime Q.

For a fixed-degree abelian extension with character conductors polynomially bounded in a parameter, prescribed Frobenius has fixed positive density and reduces to §2.1. For degree d growing, the density and character-expansion costs must remain in (2.2); “Chebotarev” does not remove them. Family 003 does not assert zero-freeness of arbitrary nonabelian Dedekind zeta functions. In particular it cannot be applied to the campaign's Kummer composita just by replacing `√x` with `x^(7/8)`.

For a prescribed class modulo P **and** a quadratic sign of conductor ≍p, the same calculation gives candidate scale

```
X ≫ [φ(P)log(2Pp)]⁸.                                          (2.5)
```

This is the useful replacement for the GRH `P²·polylog(p)` window count, not a prime of size `log⁸(Pp)`.

### 2.3 Effective constants and the separate Siegel claim

**PROVED implication.** H_(7/8) itself implies the real-zero statement with the explicit choice

```
c = (log 3)/8 = 0.1373265...,
(1−β)log q ≥ (log q)/8 ≥ c       (q≥3).
```

Thus the nonexplicit c in the *separate* Siegel paper is not an effectivity obstacle if the fixed strip is accepted. Conversely an existential c/log q gap for **real zeros only** is not H_θ, does not exclude complex zeros close to 1, and does not yield the log⁸ nonresidue bound. If only that weaker theorem survives, effectivity must include an effective lower bound for its c; a Lean existential real constant does not by itself supply an executable numerical value.

All `≪` constants derived from the numerical strip and the classical explicit formula are effectively computable. This memo does not evaluate them. It especially does **not** replace `(16 log n+70)²` by an invented explicit eighth-power expression with the same constants.

## 3. Propagation through the campaign

### 3.1 Pointwise caps, Pollack, and computational arrows

**PROVED implications, conditional on 003.** For nonsquare odd n with all prime factors 1 modulo 4, write `n=n₀m²`, n₀>1 squarefree. The `CAP_POINTWISE` window asks for

```
q≡4−n (8),          χ_n₀(q)=−1.
```

Its three independent quadratic characters have conductors ≤8n₀; the target has density 1/8, not `1/φ(8n₀)`. Therefore

```
q*(n) ≪ [log(2n₀)]⁸,
e*(n) ≤ q*(n)−3 ≪ [log(2n₀)]⁸.                                (3.1)
```

If n has a prime factor 3 modulo 4, the classical ES identity gives e*=0. For an odd square `n=a²`, choose a prime t|a and apply the construction to `d=n/t`; its squarefree part is t. Scaling by t preserves the denominator-root coprimality, since the primes used divide `(d+q)/4`, coprime to d and hence to t. Thus `e*(a²)≪log⁸(2t)≤log⁸(2n)`. This is the repaired square route of `CAP_POINTWISE` Corollary 1.2, **not** a quadratic-nonresidue assertion for a square.

`CAP_DOWN`'s simpler density-1/4 detector for n≡1 (8), and density-1/8 detector for n≡5 (8), give the same eighth-power order (and its construction has `e≤(q−3)/4`). These supersede its ineffective `n₀^(1/4+ε)`/`n₀^(1/2+ε)` bounds. In particular the weaker power bounds become effective by comparison, without reauditing every constant in Pollack's Burgess proof. The previous explicit elementary prime bound `(p−5)/8` remains valid; (3.1) is an asymptotic improvement, not necessarily a numerical improvement at tested p.

**A5/A6/A9.** Search integers `1,2,…` and compute their Legendre symbols by modular exponentiation. Equation (2.3) guarantees a nonresidue by `C log⁸p`; bit complexity is polynomial in log p. One need not know C in advance: stop at the first success. Trial division through the same small range can find a prime nonresidue if desired; or use the fact that the least integer nonresidue is prime. Tonelli–Shanks then gives prime-field square roots in deterministic polynomial time. Thus **003 alone**, independently of 142, removes A5's unresolved-derandomization consequence. The logical witness transformation `efficient ES⇒QNR` remains correct, but its target is now in P under the accepted input.

For 142 independently, factor `X²−a` on residue inputs; its n=2 case has bit bound `O((3⌈log₂p⌉)^(10¹²))`. Repeated square-root extraction starting at −1 doubles the 2-power order until obtaining a nonresidue, in at most `v₂(p−1)` steps, exactly A6. Prime p=2 is trivial. This is polynomial in the ordinary binary input length, though not a plausible practical algorithm. Neither result is classical integer factoring or an ES solver.

**A1/A4 assessment.** A1's forward `H4≤f⇒r≤f` remains true. Knowing `r≪log⁸p` neither attaches a forest edge to that nonresidue nor supplies `H4≪log⁸p`. A1's hypothetical `H4≪log²p` still implies a quantitatively stronger least-positive-nonresidue bound than obtained here. A4's unconditional infinite lower bound `r,H4,J,B≫log p·log₃p` survives unchanged; exponent 8 is fully compatible with it. A7's FQ and factoring-oracle caveats also survive: factoring polynomials over F_p does not factor the integer `tp+1`, and an efficient residue-DP still needs a successful slice.

### 3.2 M_gen: the same lower bound no longer needs GRH

**PROVED implication, conditional on 003.** The ordinary explicit formula, truncated with T comparable to x, gives for nonprincipal χ modulo Q

```
Σ_{ℓ≤x, ℓ prime} χ(ℓ)log ℓ ≪ x^(7/8)log²(2Qx),                (3.2)
```

with effective constants; omitted Euler factors and higher powers are absorbed. For the four-character detector in `SINGLE_P_COUNT` Proposition 4.1, take `y=(log p)²⁴` and `z=(p+1)/6`. Partial summation of (3.2), uniformly on `[y,z]`, makes each nonprincipal reciprocal-prime sum `O(y^(−1/8)log²(py)/log y)=o(1)`. The principal reciprocal sum is `log log z−log log y+O(1)`. Consequently

```
M_gen(p) ≥ log₂p−log₃p−O(1) = (1−o(1))log₂p.                   (3.3)
```

The exact quadratic and mod-4 conditions remain those of that proposition; both p≡1 and 5 modulo 8 are covered. A lower bound for a **genus main term** is not a lower bound for R(p). Order≥3 character contributions at the tied moduli are untouched.

### 3.3 M_BM: do not substitute GRH, but do not miss the weaker sufficient input

**PROVED implication, conditional on 003 and the published Halász theorem.** `BM_CORRECTED_COUNT` Proposition 2.3 uses GRH via Granville–Soundararajan short character sums to show

```
g(p):=sup_{t≥1}|Σ_{m≤t} χ_p(m)/m| = o(log p),
|T(p)| ≪ log p·g(p),            M_BM=M₀−T.
```

003 does not automatically license citing that GRH theorem. Nevertheless its weaker strip suffices for this application. Here is a replacement proof, uniform over the nonprincipal χ_p.

Put `Y=(log p)⁴⁰`, `a=log Y`. For `1<σ≤2` and `|t|≤log p`, partial summation of (3.2) bounds

```
Σ_{ℓ>Y} χ_p(ℓ)/ℓ^(σ+it)
  ≪ (1+|t|)Y^(−1/8)log²(pY)/log Y = O(1).
```

Terms of prime-power exponent ≥2 in `log L` are absolutely bounded. Small primes contribute at most `Σ_{ℓ≤Y}1/ℓ=log log Y+O(1)`. Hence

```
|L(σ+it,χ_p)| ≪ log Y = a.                                    (3.4)
```

This argument occurs in σ>1 where the Euler logarithm converges absolutely; no unproved branch or reciprocal-L bound is used. Apply Granville–Harper–Soundararajan, *Compositio Math.* 155 (2019), Corollary 1.2, with κ=1 and `F=L(s,χ_p)`; its exact statement and class hypotheses were rechecked at https://arxiv.org/html/1706.03749v1 and excerpted locally. For `Y≤v≤p`, its t-range `|t|≤log v` is covered by (3.4). Writing `u=log v`, it gives

```
|Σ_{m≤v}χ_p(m)|/v
 ≪ min(1, (a/u)(1+log⁺(u/a))) + (log u)/u.                      (3.5)
```

For u within a fixed factor of a use the trivial bound; outside it `(1+M)e^(−M)` decreases with M and `e^(−M)≪a/u`, justifying (3.5). Integrating by parts from Y to p, and using the trivial bound below Y,

```
g(p) ≪ a + a∫_a^(log p)(1+log(u/a))du/u
             + ∫_a^(log p)(log u)du/u + O(1)
     ≪ (log₂p)³ = o(log p).                                  (3.6)
```

For t>p periodicity gives `|Σ_{m≤t}χ_p(m)|≤p`, so the additional harmonic tail is O(1); thus the supremum genuinely includes all t. The campaign's purely algebraic summation bound for T now yields

```
T(p) = O(log p·(log₂p)³),
M_BM(p) = (3/(2π²)+o(1))log²p.                                (3.7)
```

No square-root error or full short-character-sum GRH estimate is claimed. This upgrade concerns **M_BM**, not R. The Linnik counterexamples to a two-sided polylog error `R−M_BM` remain valid. The existing unconditional lower main term already made `H_BM^-⇒eventual ES` possible; (3.7) does not prove `H_BM^-`.

### 3.4 Ineffectivity, density transitions, and moving windows

**PROVED implication, conditional on 003.** Effective Siegel–Walfisz follows immediately from (3.2): for each fixed A,B, q≤log^B x has prime-distribution errors `O(x^(7/8)log²x)=O_(A,B)(x/log^A x)` after an effective threshold. Classical BV retains level 1/2 with its usual large-sieve machinery once the small-conductor Siegel obstruction is removed; it is **not** obtained by summing (3.2) to x^(1/2).

For the particular `EXCEPTIONAL_MN2` Theorem U, one can avoid that general effectivity assertion altogether. Sum (3.2) over q≤N^(1/10):

```
Σ_{q≤N^(1/10)} max_a |Δ(N;q,a)| ≪ N^(39/40)log²N,
```

up to harmless logarithmic conventions in π versus ψ. This beats `N/log^A N` effectively for every fixed A. In its Theorem 1.3 proof enlarge C₁ by a fixed factor (e.g. 5), reducing the maximal Bonferroni modulus from N^0.45 to N^0.09. All fixed-depth divisor moments and the Cauchy–Schwarz step are unchanged. The result is

```
ρ_exc(m,N) ≤ 3e^(−as)
if log N ≥ C₁' s^(4/3)m^(1/3) and N≥N₀'(s),                    (3.8)
```

with effective N₀'(s), hence an effective A_ε in Theorem U. The m^(1/3) transition scale and the fixed-s exponent 3/4 in A are unchanged. This does **not** justify letting depth grow without tracking its constants, nor a new 1/log N rate. The lower-side L/L′ is not made new: its cited ET/BT/Shiu/PV inputs are already effective. The remaining SEL_m premise for sharp uniform order is spectral and survives.

`FORCED_WINDOW` Lemma 8.4 and Theorem 8.5 similarly become effective; the original exceptional bound

```
O_(α,ε)(X/(log X)^(4/3−2α−ε)),       0<α<1/6,
```

keeps the same meaning: almost every p, not each p. One can also remove that arbitrary ε loss in the displayed proof at the cost of a log-log factor. Put `L=log X` and start the reciprocal-prime sum at `w=L^B`, B>8α+16, rather than `exp(L^η)`. Summing (3.2) over at most 2L^α classes gives tail error `O(L^(α−B/8)(log L)²)=O(1)`; the surviving principal mass is `log L−log log L−O_(B)(1)`. Lemma 8.2 supplies its 1/3 factor. The same q,χ union bound therefore gives

```
E_windows(X) ≪_α X (log log X)^(1/3)/(log X)^(4/3−2α).           (3.9)
```

This is still much weaker as an exceptional-set estimate than Vaughan or the campaign's 3/4 chain; its value is witness location at every window in a prescribed band. Effectivity is not elimination of the exceptional inputs.

### 3.5 GRH uses that do not simply disappear

| Campaign result/input | Conclusion of this audit |
|---|---|
| CAP_POINTWISE `(16 log n+70)²` | Replaced by effective `C log⁸(2n)`, **not** the original quadratic bound |
| CAP_INTERPOLATION Thm 4.2(a), fixed mute base and `(log p)^(2+ε)` cap | 003's self-generated-mute cap is different; the fixed-base quantitative theorem requires Kummer estimates, not established from 003 |
| CAP_INTERPOLATION Thm 4.2(b), `exp(O(√(log₂p log₃p)))` | Still conditional: its Hooley sieve uses many Kummer fields and square-root errors |
| FORCED_WINDOW Hypothesis W / Cor. 4.4 | W was already an extra existence hypothesis, not a consequence of GRH; unchanged. Replacing candidate scale by (2.5) would give the **formal random-lattice exponent 8+o(1)** in place of 2+o(1), but would require a newly rescaled W, not the old theorem |
| BALANCED_LATTICE GRH+EQ and GRH+S caps `log₂^(13/2+o(1))p`, `log₂^(9/2+o(1))p` | Not unconditional: EQ/S remain missing, and the small-order index exclusion uses Kummer-field Chebotarev. Changing the AP candidate exponent alone cannot discharge these hypotheses |
| A14 one fixed mute prime | Not from 003; **does follow from the stronger technical claims of 029**, proved in §4 |
| A16 V_phi/golden-unit orbit | Not discharged: algebraic unit, norm/sign constraints, and its own Kummer fields; 029 is for integer bases. No transfer supplied |
| EXCEPTIONAL_TYPEI_LOGLOG Thm 8.1 / SEL | Dirichlet zero-free regions do not prove Selberg eigenvalue conjecture or remove complementary-spectrum errors. The later internal unconditional D32b is separate work, not an OAI consequence |
| EH / improved BV level / H-B hatch / prime-law exceptional exponent | No such upgrade follows by substitution; a fixed-strip individual error summed to Q gives at most Q below x^(1/8) by this crude method |
| CONDITIONAL_ES / R(p) lower tail | No main-term→occupancy step is supplied; GRH alone was not known to imply ES in the first place |

## 4. The additional 029 consequence: one fixed mute prime

**PROVED implication, CONDITIONAL on 029's controlled-predecessor and uniform-splitting propositions (hence their dump dependencies).** For every fixed odd prime s and every n>1 coprime to 2s, `ES^({s})(n)` holds. This removes the GRH premise from the **existence** part of A14 if those propositions are accepted. It is not a uniform cap bound and does not solve ES.

The exact two imported propositions are quoted in `029-excerpts.md`, source `sections/01a-reduction.tex`:

1. For fixed `8|M`, c∈{2,4}, `(u,M)=1`, `c|u−1`, `gcd((u−1)/c,M/c)=1`, there are `≫_(M,c,u) x/log²x` primes r≡u (M) in `(x,2x)` with
   `r−1=c v Q`, Q>x^0.9 prime, every prime factor of v in `(exp(log^0.1x),exp(log^0.3x))`.
2. For fixed integer a with |a|>1 and primes ℓ sufficiently large in terms of a, ℓ≤exp(log^0.3x), the number of r∈(x,2x] splitting completely in `Q(μ_ℓ,a^(1/ℓ))` is
   `≪_a x/[ℓ(ℓ−1)log x]+x^(1−10⁻⁶)`, with constant and threshold independent of ℓ.

**Proof of the specialization.** It suffices first to treat nonsquare n whose prime factors are all 1 modulo 4; if n has a 3-mod-4 prime factor it already has an ordinary scaled ES identity. Set `M=8s rad(n)`, c=2. Choose by CRT

```
u≡3 (8),      u≡−1 (s),      u≠0,1 (t) for every prime t|n,
(n/u)=−1.
```

Such a class exists. Write n₀ for the nontrivial squarefree part. At one t|n₀, t≥5, choose a nonresidue; at all other t|n choose −1. All these t are 1 modulo 4, so the latter choices are quadratic residues. Reciprocity gives `(n/r)=−1` for r≡u. Also `(u−1)/2` is odd and coprime to every odd prime of M; hence all reservoir hypotheses hold. The fixed s is coprime to n, so the s-condition does not collide with a t-condition. Reciprocity and `r≡3 (4), r≡−1 (s)` give `(s/r)=+1`, including s=3.

For reservoir primes r, `v₂(r−1)=1`. To force `<s>` to equal the square subgroup it is enough to remove every **odd** prime divisor ℓ of the index `(r−1)/ord_r(s)`. Such an ℓ divides vQ and forces complete splitting in the field of proposition 2. Summing over the v-range loses at most

```
≪_s x exp(−(log x)^0.1)/log x
       + x^(1−10⁻⁶) exp((log x)^0.3) = o(x/log²x).
```

If ℓ=Q, then `ord_r(s)≤2x^0.1`, so r divides `∏_{j≤2x^0.1}(s^j−1)`. Its logarithm is `O_s(x^0.2)`, losing at most `O_s(x^0.2/log x)` primes. These losses are global upper bounds, hence valid in the selected progression; their o-term beats its **fixed** positive reservoir constant. Some r remain, with index exactly 2 and an odd-order square subgroup.

Now `(−n/4 / r)=+1` and squaring is an automorphism of that odd-order subgroup. Thus `4s^(2j)≡−n (r)` for some j≥0. The shot construction of A13/A14, Q=s^j, yields `ES^({s})(n)`. Odd-square inputs follow by scaling from a nonsquare divisor; scaling is coprime to s. This completes the implication. ∎

**Why this is not just plain Artin.** The main theorem alone does not locate primitive-root primes in the n-dependent Frobenius class. Furthermore, s=3 is naturally a **quadratic residue** in the selected reservoir, so demanding primitiveness there would be wrong. Allowing index 2 is exactly what A14 needs. The technical fixed-progression statement and uniform splitting bound are the extra input. Constants depend on M, hence n; there is no implied polylog cap, no effective threshold claimed here, and no argument for algebraic-unit V_phi.

**CERTIFIED finite compatibility audit, not an analytic check.** Existing cap/window scripts already test many rational identities, so they were not duplicated. `scripts/z47_oai_impact_check.py` tests the new fixed-progression/index-two specialization on 35 pairs `(n,s)`, with n∈{5,13,17,29,193,409,577,2521,3361}, s∈{3,5,7,11}, n≠s. Each constructed CRT class satisfies the reservoir's local hypotheses; a prime in it with `ord_r(s)=(r−1)/2` was found in the first 200 progression candidates. Maximum r: **5,512,051**. At s=3, examples include `(n,u,M,r)=(193,1163,4632,1163)`, `(409,1643,9816,50723)`, `(577,3467,13848,3467)`, and `(2521,11,60504,11)`. This verifies local compatibility and target membership only; it does not test the enormous asymptotic controlled-factor ranges or the claimed splitting estimate.

## 5. Adversarial B2 analysis

**Assessment.** B2 asks for the **class of a divisor of one fixed integer in a tied modulus**, for example a divisor `d≡−1 (4C)` of `4Cp+1`, or the exact cap-zero box in a forced window. A fresh prime of prescribed quadratic sign is not such a divisor. Knowing every prime's factorization algorithmically would still not establish that one of these target classes is populated.

* **003/029/142:** their positive consequences reach quadratic signs, subgroup generation, or factorization. At the self-generated window, `<primes of K>` already contains the target; the cap absorbs exponent overflow. At a single-mute shot the powers of s are unrestricted. Neither controls the allowed box of actual divisor exponents. Deterministic QNR is a solved subroutine under these inputs, not a witness-completion theorem.
* **007 and the Heath–Brown hatch:** ordinary two-point parity cancellation is a serious new averaged theorem, but `λ(L₁(n))λ(L₂(n))` with fixed forms is not a uniform estimate for the campaign's divisor-weighted moving-modulus sums. The constants may depend on p if p enters the forms. There is no automatic higher-correlation, prime-restricted, short-interval, or one-sided divisor-class estimate. The campaign's CRT/prime-law exceptional-exponent barriers are theorems about those architectures; a new non-CRT weighted estimate could evade their hypotheses, but it must be stated and proved. “Parity barrier broken” by itself supplies no new exponent or pointwise lower tail.
* **011/012:** neither typical PD factor sizes nor independent smoothness at consecutive integers identifies a particular divisor's residue. Even the stronger smooth-predecessor result is for p−1 and fixed δ, not K=(p+q)/4 with p fixed and q polylogarithmic. Smoothness does not imply a large enough box or balanced discrete logs. Quantifier and support gaps remain after granting all stated conclusions.
* **021:** every short interval contains a survivor after forbidding one residue per prime (CRT makes this equivalent to coprimality). This is an **avoidance** theorem on free consecutive integers. ES needs a **hit** in a sparse divisor set of one integer; that set is not an interval to which Jacobsthal applies. Better avoidance lengths neither turn survivors into primes nor ensure a prescribed sign/class. No campaign theorem was found whose only missing premise is the advertised Jacobsthal bound.
* **025:** the most interesting methodological overlap is exceptional-set descent for divisor residues. But it chooses an auxiliary M freely and joins expansions by addition, freely spending `O(log log b)` terms. For fixed numerator 4 an elementary greedy step `4/b−1/⌈b/4⌉` already leaves numerator ≤3 over an integer denominator; repeating decreases the numerator and gives ≤4 terms. Therefore even the headline's asymptotic length bound is not an improvement for ES. Adapting its descent while spending **exactly three terms** would need a new arithmetic invariant; arbitrary addition doubles the length, and auxiliary denominators are not divisors of `4Cp+1` automatically. Numerator-8 counterexamples kill an unrestricted fixed-three-term transport.
* **028:** finite periodic obstructions plus bounded-step geometry prove **all components trapped**. ES forest edges obey divisibility and can jump by p-dependent distances; bounded-increment entropy and planar separation have no demonstrated analogue. For a fixed bounded menu, existing Dickson obstructions already make monochromatic traps plausible. If a growing-menu ES walk were put into this framework, one would still need a theorem that a trapped component is bichromatic, or that an arithmetically chosen root avoids all monochromatic traps. Neither follows from a moat theorem. Uniformity in fixed D is not uniformity in D(p).
* **015/020/023/026/027/182:** respectively wrong degree/scale, factorization shape without class, a different prime average, gaps without divisibility, a different integral-point model, and additive recurrence without an ES exception law. None removes B2. In particular “potential integral density after a field extension” says nothing about a positive integral point on `4xyz=n(xy+yz+zx)` over Z; Bright–Loughran already show there is no BM obstruction there.

### A modest organizing framework, not a new solution theory

**Assessment / new-theory sketch.** Use a **detector budget** `(δ,B,conductor,field,exponent budget)` to classify what an analytic theorem buys. For a free-prime detector, Theorem (2.2) is the toy theorem: cost is `(B/δ)log Q`, not merely log Q. Fixed quadratic patterns have fixed δ, APs do not. The further operation “restrict the sampled integer to the divisors of N_p” is not licensed by the explicit formula.

The first genuinely new theorem this framework would need is a target-sensitive restriction principle controlling the **negative** character contribution on those actual divisors, at one p and below its polylog main term, while vanishing on the odd-square shape. That is still B2, not a conjecture claimed easier than ES. A toy positive transfer really does work at subgroup level: §4's 35 fixed-progression examples have the target in an odd-order cyclic subgroup; no allowed-box restriction is asserted. This separates the working analytic-to-subgroup step from the missing subgroup-to-divisor step.

## 6. Full screening checklist and decision

**Assessment.** PASS means the reported implication respects the screen, not that an ES proof passes it. FAIL names what remains missing in a proposed dump→ES transfer.

| FRONTIER §4 line | Result | Reason |
|---:|---|---|
| 1 | PASS | Quadratic-sign detector is empty at odd squares; squares use explicitly checked scaling instead |
| 2 | PASS | No three-term numerator-8 conclusion; many-term and square relaxations cannot be transported freely |
| 3 | PASS | No numerator-uniform fixed-length law is imported from 025 |
| 4 | **FAIL for ES** | None of the imported estimates controls a divisor class at a tied modulus |
| 5 | PASS in §§2–4; **FAIL for averaged transfers** | Input n/p fixed in auxiliary-prime searches; PD/Chowla/Dickman averages are not silently specialized |
| 6 | PASS | Detector density and φ(P) costs explicit; no power-size ES main term |
| 7 | PASS | Only M_BM gets an asymptotic; no false two-sided R estimate |
| 8 | **FAIL for fixed menus** | Algorithms and subgroup generation do not repair bounded congruence/factorization menus |
| 9 | **FAIL for ES** | Quadratic parity and index two are not divisor-class occupancy |
| 10 | PASS | No large primes pooled across shifts; §4 bounds losses in a genuine auxiliary-prime reservoir |
| 11 | N.A. | No signed reflection transport to positive ES; analytic theta reflection is not an ES coordinate move |
| 12 | **FAIL for ES** | Caps and mute-prime powers stay relaxations; no cap-zero transport |
| 13 | PASS | No BM/local-global shortcut; 027 is explicitly rejected as such an input |
| 14 | PASS, finite scope | 193,409,577,2521,3361 enter the new CRT/index audit; existing slice failures are not contradicted |
| 15 | PASS, scope | Sign bounds are uniform in the input, including Mordell/near-square primes; no unproved nondegeneracy exclusion |
| 16 | N.A. | No thin-family solution is promoted to all inputs |
| 17 | **FAIL for covering** | No theorem on residues of the large prime factors of the actual K; lattice balance remains missing |

**Explicit final-decision review.** The tempting overclaims were checked against their sources and rejected: (i) log⁸ for every AP loses φ(Q); (ii) a clean `sorry` scan is not a Lean verification; (iii) the 026 prose page is not the full endpoint; (iv) merely replacing GRH in the BM proof is invalid, so §3.3 supplies a separate verified-Halász derivation; (v) merely rejecting Artin as progression-free misses 029's technical propositions, but demanding a primitive root for s=3 in the chosen class would also be wrong—index two fixes the specialization. These decisions are supported by the exact displayed hypotheses, not by manuscript titles.

**What changes ES's status?** Nothing here proves a new every-prime ES assertion or reduces ES to a finite check. A bounded/polylogarithmic **cap** still is not cap zero; a main term still is not the actual count; an effective exceptional bound still permits infinitely many exceptional primes. `H_BM^-`, X_slice, and the proposed exception-propagation law remain additional ES-strength inputs. Even if all relevant formalizations compile and all unformalized papers are correct, the strongest demonstrated changes are to tools and relaxations.

**Next steps, in order.** Independently run the 003 comparator/axiom and definition checks before changing any campaign status; separately audit 029's fixed-progression reservoir and uniform Kummer splitting estimate (the one-mute consequence does not depend on accepting its whole headline by faith); retain the explicit-formula/Halász deductions as reusable lemmas; investigate 025's divisor-residue descent only if an exact three-term invariant can be stated before any new experiments. Do not spend ES-search effort re-solving QNR under an accepted 003.

## 7. Artifacts and reproduction

**CERTIFIED (local execution).** The static inventory records 16 families, 25 manuscripts, 19 comparator endpoints, and approximately 67 KB of theorem/scope excerpts. All local import closures resolve; comment-only lexical hits are described in §1.1. The independent finite specialization check passes all 35 examples. Total retained data is below 2 MB. These are source/data checks, not mathematical validation of the dump.

```sh
ulimit -v 2000000
timeout 180 uv run python scripts/z47_oai_impact_audit.py
ulimit -v 1000000
timeout 90 uv run python scripts/z47_oai_impact_check.py
```

Files: this memo; `sources/oai2026/README.md`, numbered theorem/scope excerpts and `halasz-excerpt.md`; `scripts/z47_oai_impact_{audit,check}.py`; `data/z47_oai_impact/{provenance,inventory,lean-audit,specialization-check}.json` and compressed campaign keyword harvest. Only these files are committed. External Halász statement was checked directly; campaign theorem citations retain their existing internal-review status. No independent referee certification is claimed for either campaign proofs or the new manuscript collection.
