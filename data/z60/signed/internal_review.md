# Hostile internal review — Z60_SIGNED.md

**Verdict: NOT READY.** S1 and the quadratic-nebentypus ternary S2 survive review; the advertised mixed higher-weight S3 is false. The support-proxy linear algebra in S5 is sound, but several claimed consequences, especially its signed version, do not follow. Findings: **1 FATAL, 7 MAJOR, 5 MINOR**. ES and (MS) remain open.

Reviewed the requested context and briefs. Independently downloaded/read Duke and Sarnak, reran the requested rank/statistics computations, and recomputed the §6.2 table from the saved rows. No memo or script edits.

## Findings and fixes

### R1 — FATAL: mixed-nebentypus S3 is false (§4.1, lines 192–207)

The rank-three genus-separation argument depends on divergence of ∑1/ℓ. In rank k = 2r+1 ≥ 5, the normalized genus square factor is

`M_ψ(ℓ)/ℓ^(2r−1) = 1 + ℓ^(−(2r−1)) − ε_ψ(ℓ)ℓ^(−r)`.

Its character-dependent corrections are absolutely summable. S2(b) Step 1 does NOT extend: prime squares give only `Σ E_ψ(1) ≤ 0`, and products of sufficiently large primes cannot isolate a character.

**Explicit counterexample to S3 as stated.** Let E₁ and E₂ be the genus theta series of the rank-five lattices `⟨1,1,1,1,1⟩` and `⟨1,1,1,1,2⟩`, normalized to E₁(1) = E₂(1) = 1. They have common level 8 and nebentypus 1 and χ₈. Put `g = E₂ − (3/2)E₁`. Both are in S3's theta-plus-cusp class, since a genus theta differs from the individual theta by a cusp form.

For squarefree m whose prime factors are ≥ 11, unimodular rank-five densities give

`E₂(m²)/E₁(m²) = ∏_{ℓ|m, (2/ℓ)=−1} (ℓ³+ℓ+1)/(ℓ³−ℓ+1)`.

The logarithm is at most `Σ_{n≥11} 2/(n²−1) = 21/110 < log(3/2)`. Thus `g(m²) < 0` for EVERY good m, including m = 1.

On the other hand, for a prime p ≡ 17 (mod 24), p belongs to 𝒞₁(4). The same density formula, normalized at 1, gives

`E₂(p)/E₁(p) = ∏_{ℓ odd, (2/ℓ)=−1, (p/ℓ)=−1} ((1+ℓ⁻²)/(1−ℓ⁻²))² ≥ (10/8)² = 25/16 > 3/2`.

The factor at p cancels because (2/p) = 1; bad-prime factors cancel against the normalization at 1. The ℓ = 3 factor gives the displayed lower bound. Therefore `g(p) > 0` at infinitely many 𝒞₁-primes, while its genus part is not zero. Neither alternative of S3 holds.

This disproves the stated **good-square hypothesis** version, not a theorem about genuinely valid ES minorants. **Fix:** retain S3 for ONE nebentypus; remove the mixed signed extension unless a substantially stronger, separately proved hypothesis is supplied. Correct the title, §7.1, §7.2, §7.4–7.6 accordingly. “Any mixture, any odd rank” is not established.

### R2 — MAJOR: coset dichotomy does not follow even assuming (SWc) (§4.2, lines 209–224)

The sketch establishes class-dependent numbers β(s). It does not establish that either every β(s) is negative or every β(s) is zero. Some classes can have negative genus density and others zero. This is not fixed by assuming Siegel–Weil.

A concrete obstruction is the valid signed proxy `g = −θ_{5ℤ³+(1,0,0)}` for the sum-of-three-squares norm: it is everywhere nonpositive, is identically zero at indices ≡ 4 (mod 5), and has nonzero genus density at unit indices ≡ 1 (mod 5). Both residues occur among unit squares at 5 and among primes of the relevant 𝒞₁. Consequently g is neither eventually strictly negative at ALL 𝒞₁-primes nor genus-free there.

Also, different underlying determinants do not share a single B(n), and invoking S2 Remark (2) is not a proof of the nonquadratic extension: S2's genus separation explicitly uses odd QUADRATIC characters and their negative-value sets. Residue-restricted Rankin–Selberg orthogonality cannot simply be assumed either (twist-related systems can coincide there).

**Fix:** state only the class-by-class conclusion actually proved, or formulate an effectiveness-on-every-class hypothesis and supply the remaining cusp argument. Keep the termwise nonnegative-recipe observation separate. Label the current general extension an Assessment, not a consequence conditional ONLY on (SWc).

### R3 — MAJOR: the “Signed version” uses the wrong validity space (§5, lines 310–317; §6.1, lines 333–334)

Signed validity means `⟨K,S(z)⟩ ≤ 0` at R-zeros, not equality. Its coefficient domain is the closed convex cone

`C = {K : ⟨K,S(z)⟩ ≤ 0 for every z ∈ Z}`,

not W⊥. S1/S2 kill square-orbit anchors in the nonnegative-effective case; they do NOT make a signed minorant vanish at every nonsquare R-zero. Thus the §5 half-space criterion describes **support-valid proxies additionally positive at primes**, not all signed minorants. Likewise S2(b) does not reduce signed proxies to §6.1's kernel with all R-zero equality rows, even “asymptotically.”

**Fix:** replace W⊥ by the validity cone in a genuine signed formulation, or explicitly restrict the paragraph to the smaller support-valid class. Delete the claimed transfer of the finite support certificates to signed minorants. A conjecture excluding every fixed linear combination also requires joint sign distribution, not merely sign changes of each individual line. Finite occurrences of both signs do not refute eventual constant sign.

### R4 — MAJOR: S5's exceptional-line/L-value interpretation silently enlarges the proven scope (§5, lines 260–262, 278–295; §7.1 and §7.5)

Λ is defined using ALL of `⊕ M_{3/2}`, whereas S2 assumes theta-genus Eisenstein part plus cusp forms. TERNARY explicitly leaves non-genus Eisenstein components outside its theorem. S5 as abstract finite-dimensional linear algebra remains valid, but its claimed exceptional decomposition does not follow for this Λ.

Furthermore W1′ requires, for EACH contributing eigensystem, an L-nonzero anchor or the stated (H2) alternative. Those hypotheses are not globally imposed here. Even when they hold, coefficients are **signed square roots** of central values, with fixed local factors; a vector of central values is not the coefficient vector S(p). General linear-span/annihilator tests cannot discard those signs.

**Fix:** either restrict Λ to the ternary-theta class and explicitly assume W1′'s hypotheses for the dictionary, or keep S5 entirely abstract and label the additional dictionary conditional. In §7.5 replace “vector of twisted central values avoids the span of its values at R-zeros” by the actual coefficient-vector criterion. Only the special full-line-span, W = 0 case reduces to a disjunction of scalar nonvanishings.

### R5 — MAJOR: equivalence to MS⁺ and blanket circularity claims overreach (§5 consequence 4, lines 296–301; §7.2, §7.5–7.6)

S5 requires effectiveness at PRIMES. It does not imply R(n) > 0 at all large nonsquare composite n, so the asserted exact reformulation as “(MS⁺ on 𝒞₁) ∧ non-degeneracy” is unjustified. The condition `S(p) ∉ W` already excludes prime R-zeros beyond P₀; adjoining (MS) to it is redundant, not an independent decomposition.

Knowing Z completely is also not a logical prerequisite to proving validity: an identity can prove annihilation of all zeros without enumerating them. WALDS W5 explicitly warns that equivalence to (MS) is NOT a theorem that every proof by reformulation is circular. “Nothing in the modular world supplies the former” / “it never supplies validity” is not established by S5.

**Fix:** retain the exact S5 criterion, say it entails the prime-target statement and gives no validity mechanism by itself, and replace universal impossibility/circularity wording with “no independent mechanism is supplied here.” The brief's individual-line-vanishing proposal is indeed insufficient for unrestricted real support coefficients; this is a valid narrow criticism, not a closure of the whole automorphic route or of rational-coefficient cancellation questions.

### R6 — MAJOR: S4′ requires stronger asymptotic hypotheses and has an invalid fallback (§4.3, lines 232–240)

A general principal part has several polar indices m, so the exponential rates are `√m/c`, not one common m₀ with the least nonzero c automatically dominant. A standard Rademacher expansion alone does not justify the displayed single-scale form or uniform tail domination after cancellations. Those must be assumptions or proved for the particular class.

Also, `o(exp(ε√n))` on progressions whose moduli depend on ε does NOT imply polynomial growth on any fixed progression. Even globally `exp(n^(1/4))` is subexponential in this sense but not polynomial.

**Fix:** formulate the corollary for a verified eventually nonzero dominant periodic exponential term with a uniform smaller remainder (or treat all polar-index/denominator pairs). Delete the claimed fallback to polynomial-growth analysis when all k_c(1) vanish; mark that case unresolved. The elementary Lemma S4 itself is correct.

### R7 — MAJOR: numerical/BSD-dependent invalidity becomes unconditional in summaries (§0 F4; §7.2; §7.3 F4; §7.5–7.6)

§6.3 correctly admits that rank upper bound 0 does NOT prove central nonvanishing, and that identifying the finite survivor line with the stated eigensystem is EVIDENCE. But the screen/verdict/FRONTIER text subsequently says that neither line nor any combination is prime-valid without preserving these qualifications. For χ₁₀₅ at 712321 only algebraic rank 0 is established here. The two-row argument excluding combinations additionally needs the eigensystem identification and the nonzero-anchor/Waldspurger dictionary for the zero coefficient on the other line.

**Fix:** consistently say “numerical/BSD-dependent evidence against prime-validity; exclusion of combinations conditional on the identifications and required central nonvanishing.” Exact rank bounds alone are CERTIFIED. The table has two intervals [0,2], so “ranks of 18 twists” should be “rank bounds for 18 twists.” Finite tests do not exclude effectiveness/validity required only beyond a larger threshold.

### R8 — MAJOR: the purported “Selmer rank 0” statistic is NOT Selmer rank (§6.3, lines 390–393; baserate_stats output)

The script counts `ellrank(...)[1] == 0`, i.e. the **descent rank upper bound** R = 0. PARI documents `R = C − T − s`, where C is 2-Selmer dimension, T is 2-torsion dimension, and s is the computed dimension of `Sha[2]/2Sha[4]`. This is not even torsion-adjusted Selmer rank unless s = 0.

Independent checks, printing `[lo,hi,s]`:

- χ₂₁, 102001 and 8813281: `[0,0,2]`, torsion `[2]`; torsion-adjusted Selmer dimension is 2, not 0.
- χ₁₀₅, 712321 and 8813281: `[0,0,4]`, torsion `[2,2]`; torsion-adjusted Selmer dimension is 4, not 0.
- χ₁₀₅, 102001 at effort 0: `[0,2,2]`; “upper bound 2” likewise is not “Selmer rank 2.”

**Fix:** rename the statistic and reinterpret the final explanatory sentence accordingly. To discuss Selmer ranks, save s and torsion dimensions and actually reconstruct them. The χ₂₁ proven-rank-2 fractions among upper-bound-2 base twists are `29/55 = 52.7%`, `20/58 = 34.5%`, `14/64 = 21.9%`; “roughly 35–50%” misses the highest band. The numerical tail probabilities themselves reproduce correctly.

### R9 — MINOR: S2 Remark (1) overstates what its displayed relation proves (§3, lines 183–187)

The equalities `Σ E_ψ(1)=0`, `C_φ=0`, `E_ψ(1)+D_ψ=0` describe the ZERO prime-square hypothesis, not the signed one in general (e.g. a negative genus theta has negative total anchor). Also, failure of these linear equations to determine all formal coefficients is not by itself an existence proof of modular forms realizing a counterexample.

**Fix:** specify the support/zero hypothesis and either supply a realizable mixed-nebentypus example or weaken “does not suffice” to “the prime-square argument alone does not separate these terms.” This does not undermine S2 itself.

### R10 — MINOR: S5 coordinate/finite-constraint wording (§5, lines 263–272, 289–295)

- The residue projector is modular, but generally raises the level; say so when discussing existence at a “fixed level.”
- Algebraic independence must concern free coordinates in a chosen basis of W⊥, not all ambient K_j (which obey linear equations if W ≠ 0).
- There are infinitely many squares with gcd(m,2N) > 1. Finite dimensionality implies that their constraints have a finite spanning subset; it does not make the squares themselves finite or identify an effective cutoff.
- “W = 0 (𝒞₁ contains no R-zero)” is not an equivalence, and the parenthetical is impossible literally: 1 and infinitely many unit odd squares belong to Z. W = 0 means all S(z) are zero. If intended, say “no nonsquare R-zeros” as a sufficient condition, not an equivalence.

### R11 — MINOR: partial Euler product is wrong at primes dividing n (§6.2; scripts/z60_signed_pseudosq.py, PY)

At a good prime ℓ dividing the squarefree twisting index n, the ramified twist has local L-factor 1, not `(1+1/ℓ)^−1`. The script sets the trace term to zero but leaves `+1/ℓ`. This affects the prime row n = 193 in `(168,168)` and numerous composite rows. The saved numbers/table agree with the implemented statistic, but it is not exactly the stated partial Euler product.

**Fix:** omit ℓ | n (equivalently use the determinant term `χ_n(ℓ)²/ℓ`) and recompute summaries, or explicitly define this as a surrogate statistic. The central-value interpretation of w also inherits the unproved line identifications, not just the formal Waldspurger identity.

### R12 — MINOR: falsifier-table inventory and small counting errors (§0 and §7.3)

Neither table explicitly inventories the mandatory 285 composite zeros and all 14 (★)-zero primes; the nine in-𝔐 primes are not the full mandatory set, and some of the other five can lie in a larger level-dependent 𝒞₁. §7.3 acknowledges unscreened 𝔊*-zeros but §0 omits them and neither gives the required 38-count. This is an incomplete audit trail, not evidence of false positivity.

**Fix:** state the full counts and distinguish screened ≤B/in-class subsets from unscreened entries; retain the legitimate explanation that non-R 𝔊*-zeros impose no R-support constraints. §7.3 F4 says 5569/9601 are nonzero “for four lines”; among the five §6.2 lines it is THREE. F2 needs `P₀ ≥ 10 868 474 401`, not strict `>`, for a target defined by p > P₀.

### R13 — MINOR: evidence trail / finite-sign wording (§5 signed paragraph; §6.1; §8)

The L = 168 no-zero-row rank 3 and B = 4000 excess 16 are only claimed as console outputs; `mixed_runs.txt` contains neither. Preserve those outputs if the numbers remain in the table. “Both signs occur” is verified, including after restricting to 𝔐, but “eventually constant fails numerically” should be “both signs occur in the tested finite range.” §5 refers to literature “§8 item 4” for sign changes and “item 5” for simultaneous nonvanishing; the actual items are 7 and 8.

## Proof audit: what survives

### S1 — passes, relative to the stated classical inputs

1. **(2.1):** the unimodular ternary identity is exactly `ℓ α_ℓ(ℓ²)/α_ℓ(1) = 1+ℓ−ε(ℓ)`. The good-prime cusp recurrence at n = 1 gives `a_ℓ−ε(ℓ)`. Only t = 1 unary terms reach ℓ², with coefficient `2ℓχ(ℓ)`; the primitive odd characters give odd u. With quadratic ψ, the real decomposition gives real u and real cusp anchors.
2. **Step 1:** dividing by ℓ and using Dirichlet in a and −a gives `E(1)+2u(a) ≤ 0` and its companion, hence E(1) ≤ 0.
3. **Step 2:** at good ℓ ≠ p, `α_ℓ(p)=1+χ(ℓ)/ℓ`; at p, `α_p(p)=1−p⁻²`. Removing the finitely many bad factors makes B(p) comparable to `√p L(1,χ_D)`, with conductor O(p), so Siegel gives the asserted lower bound. Choosing ε sufficiently small makes the Duke cusp exponent strictly smaller. Unary terms vanish at p ∤ N. The resulting threshold is ineffective, as stated.
4. **Step 3:** oddness and u ≤ 0 imply u = 0. Primitive-character independence kills the individual t = 1 coefficients. The genus restriction is zero by TERNARY Step 1.
5. **Step 4, RS:** use UNITARY L-functions (for weight 2, `L_unit(s)=L_classical(s+1/2)`). The first logarithmic derivatives give first moments and the degree-four Rankin–Selberg derivative gives the cross moments. Prime powers contribute at most a constant times `Σ_ℓ logℓ Σ_{j≥2}ℓ^(−j) < ∞`; finitely many omitted local factors are regular at s = 1. Thus (RS*) follows just from the local behavior at 1, with no prime-number theorem. Distinct normalized newforms must be indexed separately, without duplicating oldvectors.
6. **Step 4, sign:** the inequality `Σ|G|w_s ≤ 2Σδw_s − ΣGw_s = O(1)` is correct (finite omitted-prime discrepancies are O(1)). Both terms on the right are bounded as s ↓ 1. Deligne bounds G, hence the second moment is O(1), contradicting `(Σc_φ²)/(s−1)` unless every real c_φ is zero. The real-coefficient invariance argument is valid for quadratic ψ and trivial-character newforms.
7. **Step 5:** W-C2 with (1,t) gives exactly `g_φ(t)² L(G_φ,1/2)=0`. No (H2) or nonzero t-anchor is needed for this ZERO implication. Genus/unary terms vanish on squarefree 𝒞₁, t > 1. Do not confuse this valid implication with the stronger line dictionary in R4.
8. **Remark (1):** W1 from prime-square equality alone is correct: equality gives E(1) = u = 0 directly, then the RS argument kills the anchors; no Duke/Siegel case-(a) argument is needed.

### S2 — passes for the stated quadratic ternary setting

- **Lemma 3.1:** all three factorizations are correct for good squarefree m. The genus formula should be understood multiplicatively without dividing by E_ψ(1) when that number is zero.
- **Distinctness:** distinct ε_ψ disagree on infinitely many primes; genus/unary terms have order ℓ, cusp terms order √ℓ. For unequal φ, eventual equality would make the normalized difference square-summable against w_s, contradicting its RS second moment `2/(s−1)+O(1)`. The t = 1 unary family must remain a deduplicated primitive basis, as inherited from TERNARY. In this quadratic setting its χ are quadratic, so the displayed ±ℓ assertion is legitimate.
- **Dedekind independence:** the induction works on squarefree m after excluding each newly chosen prime. Infinitely many distinguishing primes is exactly the required property.
- **Signed Step 1:** ε_ψ is odd/nontrivial, hence each S_ψ has half the unit classes, and distinct sets have strictly smaller intersection. Reciprocal-prime divergence in each class permits the finite products P_c ∈ [T,2T]. The ψ₀ term has uniquely maximal degree in T, while cusp/m and u remain bounded. This correctly forces EACH E_ψ(1) ≤ 0. This is precisely the ingredient missing in S3.
- **Steps 2–3:** negative genus components cannot cancel each other on 𝒞₁; Duke/Siegel finish Step 2. For Step 3 it is enough to use primes in each residue class, avoiding any unnecessary uniform-o(1) issue over composite m.
- **Step 4:** RS yields C_φ = 0. Then D(a) ≥ 0 has average zero, hence is identically zero and all D_ψ vanish.
- **Step 5:** expansion gives `−Σ_φ[a_{ℓ₂}H_φ(ℓ₁)+a_{ℓ₁}H_φ(ℓ₂)]`; both omitted double/constant terms vanish by C_φ = D_ψ = 0. Fixing ℓ₁ and letting ℓ₂ vary gives a bounded O_{ℓ₁}(ℓ₂⁻¹/²) lower error. Applying the signed RS lemma to the negative linear combination kills H_φ(a); character independence kills every c_{φ,ψ}. Correct.

### S3–S5 remainder

- **S3 for one ψ:** the genus has size ℓ^(2κ−2), the cusp square term size ℓ^(κ−1), and the normalized ε-term is O(ℓ⁻¹/²). Absolute convergence gives E(p) comparable to p^(κ−1). The one-character proof works. The mixed version fails by R1.
- **S4:** elementary lemma and the positive-density intersection with 𝔐 are correct (use primes 1 mod lcm(M,840)). S4′ needs R6's changes.
- **§4.4:** appropriately labelled Assessment, not a new theorem. The mod-4 discriminant comparison is correct. It does not establish an exhaustive classification of Fourier–Jacobi/indefinite constructions.
- **S5 itself:** validity is exactly K ∈ W⊥ for SUPPORT proxies. `S(p) ∉ W` makes each forbidden hyperplane proper. Countably many proper subspaces are measure-null in W⊥, so one K avoids all simultaneously. The field generated by countably many coefficient values is countable; algebraically independent FREE coordinates exist. The residue projector is a finite combination of character twists and preserves T1 after zero extension, at a possibly enlarged fixed level. These facts do not require Waldspurger. Consequences 1–2 are valid with this support/real-coefficient scope; consequence 3 needs R4/R10, consequence 4 needs R5, and consequence 5 is only its explicitly independent-CKRS Assessment.

## Computation audit

All reviewer computations were sequential, with timeout ≤ 900 seconds. The rank rerun used `ulimit -v 4000000`, a 1 GB PARI stack, and the requested command `timeout 900 uv run --with cypari2 python scripts/z60_signed_zeros_rank.py 102001,712321,8813281 3`. Small parsing/statistics jobs used uv and lower limits. No dense-matrix recomputation was attempted.

### Requested reruns

| p | χ₂₁ bounds | χ₁₀₅ bounds |
|---|---|---|
| 102001 | [0,0] | [2,2] |
| 712321 | [2,2] | [0,0] |
| 8813281 | [0,0] | [0,0] |

All match `zeros_rank_420.txt`. The full nine-prime table matches that file. `t420_screen_run1.txt`, `t420_screen.txt`, and `t420_screen_102001.txt` support the reported numerical ranks, with χ₂₁ central value at 102001 equal to `0.379908466069321`. These are numerical, not certified nonvanishing calculations.

`uv run python scripts/z60_signed_baserate_stats.py` reproduces `baserate_stats.txt` exactly: χ₂₁ observed 4/7, expected 1.22, tail 0.0194; χ₁₀₅ observed 2/7, expected 1.27, tail 0.3739. Upper-bound-zero expectations are 3.57 and 2.77. Base counts are 120 per band per line. For four tests, Bonferroni gives about 0.0776 for the smallest p-value; “not significant” at familywise 5% is defensible. These are plug-in, exploratory Poisson-binomial calculations, not a proved sampling model. The statistic-name error is R8.

### §6.1

`mixed_runs.txt` supports all three zero-row certificates, dimensions 176/272/240, row counts 169/150/150, and zero-row counts 168/149/149. It also supports no-zero-row ranks 9 and 6 for 240 and 280, with per-character rank sum 1. The script's exact-kernel argument really does certify the finite-range SUPPORT statement without stabilization assumptions. The missing L = 168 comparison log is R13. No numerical certificate here covers signed validity.

### §6.2: independent recomputation from saved tables

| (L,D) | primes | zero counts by tercile | ρ(w,PY) | ρ(R,w) | ρ(R,n_p) | +/− |
|---|---:|---|---:|---:|---:|---|
| (168,168) | 238 | 31/80, 19/79, 7/79 | .584075 | .008286 | −.291577 | 81/100 |
| (280,56) | 238 | 32/80, 14/79, 13/79 | .507997 | −.121505 | −.628878 | 87/92 |
| (560,280) | 238 | 24/80, 23/79, 7/79 | .490004 | .125400 | −.628878 | 92/92 |
| (420,21) | 108 | 14/37, 6/36, 3/35 | .487240 | −.079171 | .112434 | 43/42 |
| (420,105) | 108 | 18/37, 11/36, 7/35 | .426198 | .061021 | .112434 | 40/32 |

Every displayed §6.2 number rounds correctly, and coefficients at 5569/9601 match. Restricting further to 𝔐 gives positive/negative counts respectively `30/42, 43/45, 40/40, 43/42, 40/32`; both signs really occur in every tested line. Composite-only ρ(R,w) is also small, between −.036 and .093. These support a finite-range “small rank correlation” observation, not statistical independence from R or an asymptotic sign theorem. The PY local-factor issue is R11.

## Independent source verification

Downloaded with curl and extracted with pdftotext:

- `https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf`
- `https://publications.ias.edu/sites/default/files/ShalikaBday2002.pdf`

**Duke:** printed p. 85, Theorem 5, gives `ρ(n) ≪ |n|^(−2/7+ε)` for squarefree n/fundamental discriminants at fixed form/weight. Printed p. 78, equation (2.5), explicitly relates the holomorphic normalization by `a(n) = (4πn)^(κ/2)ρ(n)`. Thus at κ = 3/2 the exponent is `3/4−2/7 = 13/28 = 1/2−1/28`, exactly as used. Printed pp. 75–76 explicitly say Theorem 5 includes holomorphic weight 3/2. The theorem covers the half-odd-integral weights claimed; its dependence on level/multiplier is harmless here because these are fixed. **The Duke claim is verified, not a defect.**

**Sarnak:** abstract/§1 state Jacquet–Shalika nonvanishing of standard cuspidal L-functions on Re(s) = 1. §1 immediately after equation (5) states Rankin–Selberg nonvanishing, attributing GL₂ × GL₂ to Ogg and the general result to Shahidi. The note also uses the diagonal simple-pole input. For the distinct self-dual newforms and unitary normalization here this supports RS1/RS2 exactly as needed. **The Sarnak attribution and RS* derivation pass review.**

## Required disposition

Preserve S1, quadratic ternary S2, elementary S4, the abstract SUPPORT version of S5, and the finite exact certificates. Remove the false mixed S3 extension, narrow the coset claim, repair the signed cone and dictionary scopes, and propagate every numerical/conditional qualification into the title/verdict/FRONTIER/bottom line. No claim here settles ES or (MS).
