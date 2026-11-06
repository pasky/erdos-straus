# Hostile internal review — z60 TRACE

Reviewed `00d891ae..7580fa34` (all seven commits, all changed files). Line references below refer to `7580fa34`. **ES and (MS) remain open.** No claim in this review proves or disproves either.

**Verdict: changes required before accepting the PROVED labels or exporting the proposed FRONTIER text.** The displayed trace identity survives the checks, including previously untested weights/levels. Its written proof does not: Lemma 1(vi) and the conclusion of Lemma 2 miss an elliptic orientation factor of two. The positivity section also promotes conditional observations into overly broad impossibility claims. These are not numerical discrepancies in Theorem 2.

Severity: FATAL means fatal to a stated proof/result *as written*, not a disproof of the numerically tested identity or of ES. MAJOR changes affect mathematical scope, attribution, or the verdict. MINOR changes are local corrections or reproducibility improvements.

## Defects

### D1 — FATAL: elliptic class counting is off by two

**Locations:** `Z60_TRACE.md:63–64,69–78,102–103` (Lemma 1(vi), Lemma 2, Theorem 2 derivation (a)).

With the stated convention H(4)=1/2, the total weight of **all** SL₂(ℤ)-conjugacy classes of matrices of trace w and determinant s, weighted by `1/|Z_PSL₂(γ)|`, is **2H(4s−w²)**, not H. Positive and negative definite associated forms give the two elliptic orientations. SL₂-conjugation does not identify them.

Explicit counterexample: C=1, n=4, (s,w)=(1,0). Set

```
J = [[0,-1],[1,0]],       -J = [[0,1],[-1,0]].
```

Both have characteristic polynomial x²+1. They are not SL₂(ℤ)-conjugate: a matrix anticommuting with J has form `[[a,b],[b,-a]]` and determinant `−a²−b²`, never +1. Each centraliser in SL₂ has order 4, hence each PSL₂ centraliser has order 2. Their combined weight is 1, not H(4)=1/2.

The corresponding matrices `4J−I` and `−4J−I` both belong to Δ₁(17). Each SL₂-class splits into 48/4=12 Γ(4)-classes; there are **24**, not the claimed `μ₁H(4)=12`. The exclusion of `−ξ` at line 78 does not fix this: the two matrices here are not negatives of one another, and both are congruent to −I.

**What is correct:** `[SL₂:Γ(Q)]=2μ_C`, torsion-freeness, trivial intersection of the finite centraliser with Γ(Q), and the individual orbit-splitting formula in Lemma 2 are all correct. The erroneous input is Lemma 1(vi).

**Fix:** either restrict to one explicitly defined elliptic orientation, or replace H by 2H in Lemma 1(vi) and the total class count in Lemma 2. Then repair the trace derivation consistently. **Do not double the elliptic coefficient in Theorem 2:** Popa computes `M_k+S_k^c`, and passing to the cusp trace introduces the compensating factor 1/2 after handling Eisenstein forms. This is exactly why the final formula can be right while the stated class-counting proof is wrong.

### D2 — MAJOR: the claimed relative proof omits more than the hyperbolic constant

**Locations:** `Z60_TRACE.md:83,93–111,113,139,145,154,175,228–250`; `data/z60/trace/LIT_CHECK.md:40–57`.

“Derivation PROVED relative to a general trace formula up to the bookkeeping of the hyperbolic constant” is not an adequate PROVED label under FRONTIER's definition of a complete proof relative to a named theorem.

* Popa, PAMS 2018, Theorem 1 gives the trace on **M_k+S_k^c**, not S_k. The literature report explicitly warns about this. Its elliptic coefficient is not directly the claimed local coefficient for the cusp-only trace. One must verify the reflection symmetry, replace S_k^c by S_k, subtract the Eisenstein trace, and divide by two. This also repairs D1.
* Popa requires the coset-count hypothesis; Shimura Theorem 4.5 has the additional hypotheses itemised in LIT_CHECK. Calling either “any double coset” without checking its hypotheses is too broad. Δ for composite N may be a union of double cosets, so mention additivity where used.
* Repeated-root/parabolic contributions occur for even n and are not derived by the discussion of split hyperbolic elements. The min-divisor sum includes diagonal pairs. Their treatment cannot be omitted from a theorem for every n.
* Line 108 imports a cusp constant from level 1 without showing how cusp width Q and the allowed upper-right entries change multiplicities. Numerical agreement does not prove this step.
* Define the GL₂⁺ slash normalisation explicitly. With the raw slash `f(αz)(cz+d)^(−k)`, the Hecke sum needs the factor `N^(k−1)`; with the determinant-normalised slash it needs `N^(k/2−1)`. The parenthetical standard-Hecke convention is enough to interpret the experiments, but not a substitute for a definition when tracing constants through sources.

**Fix:** keep “exact finite verification; candidate general identity” until a full specialisation is written, and make subsequent results conditional on that identity. Alternatively supply the missing derivation. A short route to the hyperbolic coefficient is available through the character decomposition and Cohen–Strömberg's Γ₀(Q²) formula; see the repair calculation below. The exceptions in the current status paragraph do not license the unqualified “exists and is exact” and PROVED conclusions elsewhere.

### D3 — MAJOR: Prop 4.4(b) does not establish its advertised square-root obstruction as stated

**Locations:** `Z60_TRACE.md:11–14,183–190,233–244,249–250`.

The valid assertion in an empty elliptic window is

```
Tr−S = −(ε∞/2)(ES_k−TRIV_k).
```

This does not imply that the trace is large at every such point, nor whenever there is a balanced pair.

1. A balanced ES pair or TRIV pair alone does not bound the **difference** of the two weighted sums. Opposite-class contributions can cancel. The displayed additional hypothesis on `|ES_k−TRIV_k|` is essential and is dropped again in line 189 and the summaries.
2. The proposed comparison is with `√dim · τ(N) · N^((k−1)/2)`, but the argument discards τ(N). Under the displayed difference hypothesis, the lower-bound ratio is only `K^(1−k) ε∞/(2√dim τ(N))`, not `ε∞/(2√dim)`.
3. The equality controls `Tr−S`, whereas the bound being declared false controls Tr. Either exclude the scalar case or bound S.
4. `ε∞/(2√dim) ≍ √Q` assumes fixed k. Uniformly in weight its order is `√(Q/(k−1))` once away from the smallest exceptional case.
5. “One ES pair ... and only the trivial TRIV pairs” is not always sufficient for the numerical inequality as written. C=2, n=6, k=3 has N=49, ES₃=49, TRIV₃=2 and K=1 for its diagonal ES pair; 47 is not ≥49. Distinct-root ordered pairs avoid this particular subtraction error, but the theorem includes even n and diagonal pairs.

The unconditional headline is particularly misleading: for n=1 and Q≥8 the window is empty, ES=0, TRIV=2, S=0, and Tr=ε∞. At fixed odd k this is *smaller* than the proposed square-root scale as Q grows.

**Fix:** retain the exact identity and state a conditional lower bound with all factors and hypotheses. If the intended result is that a uniform bound over **all n and all levels**, at fixed k, is false, give an actual family. For example, Q=4C≥8 and `n=2Q−3` give

```
N=(Q−1)(2Q−1),   E=0,   S=0,
ES_k=2(Q−1)^(k−1),   TRIV_k=2,
Tr=−ε∞((Q−1)^(k−1)−1).
```

Here w=3, s=2 is the sole candidate and is not elliptic. Among divisors ≤√N the only possible ES divisor is Q−1; the only possible nontrivial TRIV divisor is Q+1, which would have to divide 6 and cannot. No square root of N can be ±1 modulo Q, so S=0. Since `τ(N)=Q^o(1)`, the ratio to the proposed square-root bound grows as `Q^(1/2−o(1))` for fixed k. This supplies the missing uniform counterexample, **conditional on the trace identity**, without claiming largeness everywhere. It does not refute such a bound on the Mordell-hard prime domain: this family has n≡5 (mod 8), outside that domain.

### D4 — MAJOR: the “route killed” verdict exceeds the proved certificate restrictions

**Locations:** `Z60_TRACE.md:150–152,160–173,198–200,216–217,223–236,243–250`.

Prop 4.2 is a correct rearrangement, explicitly recognised as a tautology. It is not a lower bound on the achievable slack of *every* spectral upper bound. Cor 4.3 proves a necessary condition for **B=D**, the worst-case Deligne bound. It does not show that better pointwise bounds cannot fire. Finite non-firing at C=2,3 and an independent-eigenvalue heuristic do not prove “worst-case inputs are useless beyond Γ(4)” as a universal statement either.

The Cauchy–Schwarz claim at lines 198–200 also needs a hypothesis. Its gap is

```
√(dim · Σ λ_f²) − Σ(−λ_f),
```

and firing only compares that gap with `(ε∞/2)ES`. Approximate constancy of eigenvalues follows only after proving this tolerance is small relative to the appropriate spectral norm. No such comparison is supplied. Cor 4.3's normalisation by the Deligne bound cannot simply be reused for an arbitrary second-moment bound.

“Only exact evaluation survives” and “the spectral side is not controllable at a single N” are not consequences of the stated propositions. The scoped failure of one uniform absolute bound in D3 also leaves open one-sided estimates, restricted arithmetic domains, removal of explicit geometric contributions, and estimates in other C-ranges.

**Fix:** replace the killed-route verdict by “no positivity mechanism obtained; Deligne imposes the displayed necessary alignment condition; a specified uniform absolute square-root bound fails.” Keep approximate independent evaluations as a possible escape, and label the Cauchy–Schwarz discussion Assessment unless a quantitative small-slack hypothesis is added. Say “near-total” only in the limit `(k−1)Q→∞`, not at every nonexceptional fixed level: the proved universal lower bound can be merely 0.4.

### D5 — MAJOR: F2/FRONTIER screens drop both a transport hypothesis and the threshold

**Locations:** `Z60_TRACE.md:212–224`, especially F2 line 213.

An argument producing some C need not produce an **even** C merely because it never explicitly invokes the words “C odd”. Restricting a quantified range, changing its density, or changing local level structure can invalidate an existence argument. A transport statement about the *whole proposed positivity argument* is needed, not just the observation that the identity exists at even levels.

Furthermore, the 12+2 R₈-zero primes lie below 2.33·10¹⁰, hence below the (MS) threshold 10¹⁷. As FRONTIER §4 explicitly explains, they refute an argument whose asserted range includes those primes, **not eventual C-even positivity or a statement beginning at 10¹⁷**. They are failures of one line of 8/p, not failures of 8/p itself.

F1's absence of a proved prime/square distinction and F3's absence of a prime-sensitive positivity input are useful negative findings, not a theorem excluding all future positivity arguments using this identity. “No positivity mechanism drawn from it passes F1–F3” should be “no mechanism supplied here establishes the needed discrimination.”

**Fix:** restore FRONTIER's transport and threshold qualifications verbatim in substance. The tied modulus being represented exactly is also only an encoding success, not a pass of the substantive B2 lower-tail screen.

### D6 — MAJOR: solutions/root pairs are not literally conjugacy classes; diagonal solutions are not split hyperbolic

**Locations:** `Z60_TRACE.md:8–10,58–61,123–127,228–230,239,246–248`.

The elementary dictionary identifies ordered divisor/root pairs with ordered (★) solutions. It does **not** give a bijection between those solutions and Γ(Q)-conjugacy classes of matrices. Integral lattice embeddings and level markings give multiplicities; exchanging roots also does not generally give a new matrix conjugacy class.

For example, C=1, n=5 gives roots u,B=1,2 and two ordered ES pairs, (3,7) and (7,3). Matrices γ with characteristic polynomial `(x−1)(x−2)` form one SL₂-class (the integral eigenspace projections split ℤ²), with SL₂ centraliser {±I}. Its corresponding Δ-class splits into **48/2=24 Γ(4)-classes**, not two. The cusp orbital calculation produces the weighted divisor sum, not an unweighted bijection to these classes.

There is also a boundary error for even n: C=1, n=2 has u=B=1, d=d′=3 and a genuine (★) solution, but w²−4s=0 and Γ=3I is scalar, not split hyperbolic under Lemma 1(iii)'s positive-discriminant definition. Non-scalar repeated-root matrices occur as well. The all-n theorem deliberately includes these cases.

**Fix:** consistently say “ordered positive integer root pairs (including repeated roots)” or “positive divisor-pair terms in the cusp contribution”. Restrict “split hyperbolic” to distinct roots and treat the repeated-root terms separately. Do not describe Theorem 2 as a literal count of positive conjugacy classes.

### D7 — MAJOR: the literature comparison understates prior higher-weight results

**Locations:** `Z60_TRACE.md:34–38,119–120`; `data/z60/trace/LIT_CHECK.md:170–205`.

“Those are weight-2 (even)” is false of the cited collection. Mertens §7.2 treats weight `2+2ν`; Kane–Pujahari Lemma 3.3 treats weight `2+2k`. LIT_CHECK itself records this. KPY Theorem 1.7 is indeed weight 2, but its Theorem 1.6 treats higher moments, including odd moments, with cusp-form corrections. The cached primary KPY text explicitly states this for every moment k≥1. Thus “all weights” or odd-weight sign separation cannot be advertised as a new general phenomenon against these references.

The narrow repository increment appears defensible: the principal-level specialisation with descended discriminant `4s−w²` and its explicit affine-line description is not the formula in GROWING_IDENTITIES §2 or y1_gamma8_trace. But GROWING_IDENTITIES Prop 2.1 already has the ±1 split-divisor term, parity sign, min-divisor weight, and odd-weight line-bundle explanation; Prop 2.2 already has the level/weight-versus-Deligne scale obstruction. y1_gamma8_trace already discusses class-function visibility versus the arithmetic extraction problem. The new specialisation should be credited as a refinement of these, not a first discovery that arithmetic solutions and elliptic terms inhabit one Hecke correspondence.

**Fix:** describe the prior progression identities as including higher moments/weights. Limit the new-to-repository claim to the explicit descended line formula and the precise necessary Deligne certificate inequality. Leave literature novelty unclaimed until a term-by-term comparison is made. “Presumably equivalent” in Cor 2.1 is appropriately tentative; it is not a verified reduction to KPY with M=16.

### D8 — MINOR: the Jacobi specialisation has the wrong rescaling and an inapplicable theorem citation

**Locations:** `Z60_TRACE.md:128–130`; `data/z60/trace/LIT_CHECK.md:104–128`.

For a series `F(τ,z)=Σ H(4s−w²)q^s ζ^w`, substituting `F(Qτ,−τ)` produces exponent `Qs−w=n`, not `Qn+1`. To produce the displayed generating series one needs the shape

```
q · F(Q²τ,−Qτ),
```

with the −12 coefficient normalisation, D=0 boundary contributions, and completion treated explicitly. The q factor is also the expected torsion-specialisation prefactor for α=−1/Q in the variable Q²τ.

EZ Theorem 2.1, as verified in LIT_CHECK, concerns convergent Jacobi–Eisenstein series of **even weight ≥4**, not this non-holomorphic weight-2 series. The report explicitly says that the weight-2 location in EZ is unverified. An Assessment label does not make the theorem support the wrong weight. “Non-holomorphic part ... exactly on the split points” also needs a calculation including the repeated-root boundary.

**Fix:** correct the rescaling and cite a verified weight-2 completion result, e.g. the Williams/Zagier source identified in LIT_CHECK, with its precise conventions. Retain “not worked out” until the projection/completion calculation is done.

### D9 — MINOR: w_* need not exist in the stated open interval

**Locations:** `Z60_TRACE.md:175–180,183`.

The at-most-one-elliptic-point result and its inequality chain are correct. But the representative of −n modulo 4C in `(-2C,2C)` does not exist when n≡2C modulo 4C. This occurs inside the stated range: C=1,n=2 is the endpoint example. The subsequent formulas using w_* are then undefined, even though the window is empty.

**Fix:** use a half-open interval and state that an endpoint representative is never elliptic under the hypothesis, or explicitly declare the candidate absent in this residue class.

### D10 — MINOR: two EVIDENCE numbers/scopes need correction

**Locations:** `Z60_TRACE.md:168–170,212`; `data/z60/trace/screen_C2_k3.tsv:row n=6561`, `screen_C2_k3_range.tsv:rows n=225,1296`.

* The C=3 median slack ratio is **66.24952741020795**, which rounds to **66.2**, not 66.3 at one decimal place.
* F1's “C=2 max 0.40 at squares” is the maximum over **all squares in n≤3000**, attained at the even square 1296 (exact ratio approximately 0.3973960845). Among the odd squares in that range the maximum is approximately 0.3326 at 225. The separately cited list of 49 odd squares extends to 99² and has maximum **0.6638 at 81²=6561**. Thus 0.40 is not the maximum of the screened odd squares described in that row. The quoted prime maximum 0.76 corresponds to the range file, not the list file.

**Fix:** give the sample and odd/all-square distinction explicitly. “Not distinguishable”/“no structural gap” is an Assessment, not a statistical conclusion established by comparing two maxima. All other displayed EVIDENCE-table counts, minima, firing counts, and trace ranges agree with the data at the shown precision; see below.

### D11 — MINOR: the certification tools do not fail on failed certification, and their exactness scope should be explicit

**Locations:** `scripts/z60_trace_check.py:19–32`, `z60_trace_c1_check.py:23–42`, `z60_trace_lemma1_check.py:27–36`, `z60_trace_screen.py:30–39`, `z60_trace_identity.py:7,24–25`.

The checkers print mismatch counts but return status zero even when nonzero; screen prints `id_ok=0` without failing. I deliberately supplied the main checker a C=1,k=2,n=1 row with T=1 instead of T=0: it printed `mismatches=1` and **exited 0**. A shell pipeline therefore reports success on a failed check. This did not contaminate the stored runs: their mismatch counts and rows check out.

`geom_pieces` uses floating-point square roots and an unexplained padding constant to bound an otherwise exact rational sum. The present small ranges are safe and were independently rechecked, but the implementation is not an all-size exact enumeration. TSV E/X/threshold fields are rounded to six significant digits; they are not certificates of exact rational values without recomputation. Finally, the Lemma 1 script checks the divisor dictionary and T1 only, **not** the weighted matrix-class assertion that fails in D1.

**Fix:** exit nonzero on mismatches, document the actually tested parts of Lemma 1, and use integer bounds. For the elliptic enumeration, `L=isqrt(4N−1)` and `−L≤Qw−2≤L`, followed by `w≡−n (mod Q)`, give a direct exact interval. Store exact rational TSV fields or explicitly label them display-only. Make the 2 GB PARI allocation configurable rather than an import side effect; keep resource limits on review runs.

### D12 — MINOR: small documentation/attribution inconsistencies

**Locations:** `Z60_TRACE.md:4–6,13–14,192–195,240–244`; `data/z60/trace/LIT_CHECK.md:58,86,198,203,259–261`.

* Tracked trace artifacts before this report total **1,251,444 bytes**, not <1 MB.
* The opening calls Prop 4.5 CONDITIONAL on Schinzel H; its actual heading says Assessment + CERTIFIED example and its text refers to Dickson-conditional results without stating a precise applicable theorem. Give one consistent label and an exact source proposition/hypothesis for infinite fixed-C failures. The finite examples alone establish no infinitude.
* “CERTIFIED for C≤5,k≤5” in the proposed FRONTIER paragraph can be read as a full parameter grid. The tested pairs are a sparse list, which should be stated or linked as such.
* In LIT_CHECK's KPY divisor interpretation, distinguish `d=(t−s)/2 | n`, with `t=d+n/d` and weight `d^(k+1)`, from `d=t−s | 4n`, with `t=(d+4n/d)/2` and weight `(d/2)^(k+1)`. The current sentence silently mixes these conventions. Cor 1.8's representative restriction `1≤m≤M` should also be preserved, or expressed as a statement about residue classes.
* The warning that Cohen's signs are “not A₁+A₂+A₃+A₄” must distinguish naming conventions: GROWING_IDENTITIES explicitly defines A₂ and A₃ as signed negative terms. Its plus-sign presentation is not itself a transcription error.
* LIT_CHECK line 58 must use the **projective** index in `(k−1)[Γ₁:Γ]/6`, or specify the bars. With Γ₁=SL₂ and Γ=Γ(4), the written SL₂-index reading incorrectly gives 16 for dim M₃+dim S₃, whose actual value is 7+1=8. Its Figure 3.4 dimension quotation also needs the restriction k≥3; substituting k=2 gives −1 for dim S₂(Γ(4)) rather than 0. The memo's own odd-k≥3 dimension formula does not make either mistake.

## What checks out mathematically

This section records affirmative checks to distinguish genuine defects from plausible but incorrect objections.

* **Lemma 1(i)–(ii):** `det(Qγ−I)=Q²s−Qw+1`, so det=N iff Qs−w=n; trace and discriminant transformations are correct and conjugation-equivariant.
* **Lemma 1(iii)–(iv):** a square discriminant has the parity of w², hence integer roots. Mixed signs force `(Qu−1)(QB−1)<0`; both positive or both nonpositive are the only cases. Repeated roots give `n=Qr²−2r`, even. The caveat is the distinction between repeated and strictly split roots (D6).
* **Lemma 1(v):** the citation to Z57_SYNTH Lemma A.1(b) is appropriate. With d=4uC−1, n≡−u modulo d and `(−u/d)=−1`; a square cannot have this symbol. The cited source actually excludes all squares, which is stronger than needed here.
* **Lemma 2's group theory:** normality and bi-invariance are correct; the index is 2μ, not μ, in SL₂. The individual centraliser argument is correct. Only the final use of Hurwitz weights fails (D1).
* **Spectral identification:** conjugating by A=diag(1,Q), as `AΓ(Q)A⁻¹`, gives `H=Γ₀(Q²)∩Γ₁(Q)`. The quotient Γ₀(Q²)/H is `(ℤ/Qℤ)×` via the lower-right entry. Its character decomposition gives exactly the stated spaces with χ(−1)=(−1)^k. Conjugation sends Δ to the negative of the displayed determinant-N set. Since N≡1 modulo Q, its positive correspondence gives the usual away-from-level T_N in each character component, after the usual character weighting/normalisation. Thus `T_Δ=(−1)^k ⊕T_N` is correct, not an extra factor of φ(Q).
* **Degree term:** the map `Γ(Q)\Δ → SL₂(ℤ)\M_N` is bijective. Surjectivity follows by lifting the inverse of a determinant-one reduction modulo Q; injectivity follows because two representatives congruent to −I can only differ on the left by a matrix congruent to I. The degree is σ(N).
* **Cor 2.1:** μ₁=24 and ε∞=6 give exactly the coefficients 24,3,8 and the scalar terms 2 and 4λ/3 displayed. For square N exactly one sign of √N is −1 modulo 4. The k=3 spectral trace is −a(N), so the sign of a(N)/3 is correct. The Gaussian-integer coefficient formula and the displayed five η-coefficients agree with an independent product expansion. If N is not a sum of two squares then both a(N) and the scalar term vanish, giving the stated special case. These deductions remain conditional on Theorem 2 until its proof is repaired; the finite independent checks are valid.
* **Prop 4.1:** both rearrangements, including the even-weight minus-TRIV term and the k=2 correction, are correct. TRIV≥2 for n≥1 because N>1.
* **Prop 4.2:** the slack equivalence is exact, conditional on the identity. It is a necessary-and-sufficient condition for the chosen bound's lower estimate to be positive, not an impossibility theorem about finding such a bound.
* **Dimension and Cor 4.3:** Γ(Q) is torsion-free with regular cusps. For odd k≥3, the dimension is `(k−1)μ/12−ε∞/2`. The six quoted dimensions 1,5,20,72,208,408 are correct. Since N is coprime to Q², the Hecke operators are normal; the standard adjoint relation makes T_N self-adjoint here because χ(N)=1. Their eigenvalues are real, and Deligne applies to every underlying newform. Oldform degeneracy copies have the same away-from-level eigenvalues, with multiplicity; they cause no exception. The two distinct divisors 1,N are not ES divisors, giving `ρ≤(τ(N)−2)/τ(N)<1`. The factor `6/((k−1)Q−6)` and the lower threshold 0.4 outside (k,Q)=(3,4) are correct. “Within o(1)” should be understood on the *normalised* eigenvalue scale.
* **Prop 4.4's at-most-one proof:** with two points, `Q≤w₂−w₁<4√s₂`. Writing σ=√s₂ and using w₂<2σ gives `Qσ²−2σ−n<0`, hence `σ<(1+√N)/Q`. Consequently `Q²<4(1+√N)`, i.e. `4C²<1+√N`, contradicting the hypothesis. For any individual elliptic point the same bound gives `|w|<(1+√N)/(2C)≤2C`. The equivalence `n≤4C³−2C ⇔ √N≤4C²−1` is correct. Only the undefined endpoint representative and the later largeness inferences need correction.
* **Bruhat identity, lines 201–203:** the seed has determinant 1. For translations with integers l,r, the diagonal entries are `Q−1+Ql`, `Q−1+Qr`; positivity means l,r≥0, and the upper-right entry is `Q−2+(Q−1)(l+r)+Qlr = Q(l+1)(r+1)−(l+1)−(r+1)`. This is the desired bijection. Ordinary Kloosterman residue sums forget the chosen lifts, but this alone is not a theorem excluding every trace formula with an archimedean test function.

### A concrete repair for the hyperbolic coefficient

Use the spectral character decomposition and Cohen–Strömberg's cusp-trace formula at level Q². Write `h=gcd(t,Q²/t)` for a divisor t of Q². Then h|Q. For ES/TRIV pairs, d,d′≡±1 modulo Q, so `h | d−d′` and `h | Q²/f_χ` for every character of conductor dividing Q. Thus all cusp divisors t are allowed. Conversely, the CRT cusp parameter y_t is ±1 modulo Q exactly when d and d′ are both that sign modulo Q: at each prime dividing Q, one of t and Q²/t contains the full prime-power part of Q, and dd′≡1 modulo Q determines the other root.

Parity-character orthogonality therefore gives

```
Σ_{χ mod Q, χ(−1)=(−1)^k} (−1)^k χ(y_t)
  = (φ(Q)/2)([d≡−1 (Q)] + (−1)^k[d≡1 (Q)]).
```

Moreover,

```
Σ_{t|Q²} φ(gcd(t,Q²/t)) = Q ∏_{p|Q}(1+1/p),
(φ(Q)/2) Q ∏_{p|Q}(1+1/p) = ε∞.
```

The original −1/2 prefactor gives precisely `−(ε∞/2)(ES_k+(−1)^k TRIV_k)`, including diagonal divisor pairs under the cited formula's convention. This is a possible replacement for “up to bookkeeping”, not a repair already present in the reviewed memo. The elliptic contribution still needs the orientation/cusp-trace conversion in D1–D2 to be written consistently.

## Numerical audit and reproducibility

All executions used `ulimit -v 4000000`, a timeout of at most 1800 seconds, Python through `uv run --with cypari2 python`, and sequential jobs (never more than two processes). No expensive unrestricted array computations were used. Temporary review scripts/results live outside the repository; only this report is committed.

### Fresh spectral and independent C=1 runs

```
ulimit -v 4000000
timeout 1800 uv run --with cypari2 python scripts/z60_trace_identity.py 3 5 40 > /tmp/z60-review-C3-k5.json
timeout 1800 uv run --with cypari2 python scripts/z60_trace_check.py < /tmp/z60-review-C3-k5.json
# C=3 k=5 dim=168 mu=576 rows=40 mismatches=0

timeout 300 uv run --with cypari2 python scripts/z60_trace_identity.py 7 3 2 > /tmp/z60-review-C7-k3.json
timeout 300 uv run --with cypari2 python scripts/z60_trace_check.py < /tmp/z60-review-C7-k3.json
# C=7 k=3 dim=1200 mu=8064 rows=2 mismatches=0

timeout 1800 uv run --with cypari2 python scripts/z60_trace_c1_check.py 50000
# n<= 50000: k=2 mismatches 0, k=3 mismatches 0

timeout 1800 uv run --with cypari2 python scripts/z60_trace_lemma1_check.py
# mismatches 0
```

Both fresh (C,k) pairs are absent from the committed data. C=7 also exercises non-real characters, unlike the Q=12 character family. The C=1 check does not use modular-form computations, but it still uses PARI for Hurwitz class numbers; “independent” should not be read as independent of that class-number engine. Separately, direct multiplication of `q∏(1−q^(4j))^6` agreed with the Gaussian-integer coefficient formula at every supported index through 401, starting `1,−6,9,10,−30`.

### Every committed JSON row

All ten JSON files were rerun through the supplied checker and independently recomputed geometrically, with **zero mismatches**. The independent pass used the integer trace interval described in D11, PARI's divisor list instead of the script's trial-divisor loop, and separate scalar/trace assembly. It still shares PARI's class-number function. It did not recompute every stored spectral trace from scratch; that was done for the two fresh parameter pairs above.

| File | C,k | dim | rows |
|---|---:|---:|---:|
| id_C1_k2.json | 1,2 | 0 | 150 |
| id_C1_k4.json | 1,4 | 3 | 150 |
| id_C1_k5.json | 1,5 | 5 | 150 |
| id_C2_k2.json | 2,2 | 5 | 80 |
| id_C2_k3.json | 2,3 | 20 | 100 |
| big_C2_k3.json | 2,3 | 20 | 1500 |
| id_C2_k4.json | 2,4 | 36 | 60 |
| id_C3_k3.json | 3,3 | 72 | 60 |
| id_C4_k3.json | 4,3 | 208 | 40 |
| id_C5_k3.json | 5,3 | 408 | 30 |

Total: **2320 JSON rows**. Claimed larger C=1,k=3 and C=3,k=3 coverage is supplied by the screen files, not separate missing JSON files.

### Every committed TSV row

All **23,702 rows** were independently recomputed. Every ES/TRIV value, displayed E, Tr, displayed X/threshold, firing bit, displayed normalised trace, type label, and identity flag matched. The rounding issue in D10 is in the memo's aggregate table, not the row data.

| File | rows | ES>0 | fires | minimum r (n) | median r | min/max Tr/D |
|---|---:|---:|---:|---|---:|---|
| screen_C1_k3.tsv | 20000 | 12229 | 137 | 0.6786248132 (12655) | 26.0123784262 | −0.9998957424 / 0.9999744901 |
| screen_C2_k3_range.tsv | 3000 | 990 | 0 | 3.8168352840 (701) | 96.1602690225 | −0.7696821055 / 0.7613228316 |
| screen_C3_k3_range.tsv | 600 | 109 | 0 | 6.7617536203 (491) | 66.2495274102 | −0.5200941831 / 0.4950725676 |
| screen_C2_k3.tsv | 102 | 21 | 0 | 3.8168352840 (701) | 77.7649025070 | −0.4908221543 / 0.6638000343 |

Odd-square counts are correctly 71,27,12 in the three range files, and 49 in the list file (3² through 99²). None fires. The four C=2 F4 rows have ES=0, firing=0 and traces respectively **46104, −39864, −31080, 419352** at n=409,577,5569,9601; the last normalised trace is **0.0682**, consistent with the memo's 0.068. The 14 global (★)-zero primes and 12+2 R₈-zero primes are inherited campaign results: their attribution and threshold were checked against FRONTIER, not re-enumerated to 10¹⁰ in this review.

### Source checks and limits

Read LIT_CHECK completely and checked the relevant cached primary passages in Popa arXiv:1408.4998 (Theorem 1, definition (1.5), Remark 3.2), Shimura's 1974 Acta text (Theorem 4.5 and its hypotheses), Mertens arXiv:1404.5491 (§7.2/Prop 7.2), and KPY arXiv:2405.14234 (Theorems 1.6/1.7 and Cor 1.8). EZ theorem scope was checked against LIT_CHECK and the quoted passage in arXiv:1710.10025, not a fresh reading of the EZ book. KPY's stated weight-2 formula and the vanishing classification agree with the quoted source once the residue representative convention is retained. The source report's warnings about Popa's space and EZ's weight are substantive, and the memo currently does not respect them.

## Recommended disposition

Keep the exact finite computations and the spectral identification. Repair D1–D2 before calling the general identity PROVED; retain Props 4.1–4.3 as consequences with the correct dependency label. Keep the at-most-one-point lemma after the endpoint fix, replace Prop 4.4(b) by a correctly quantified statement, and narrow the verdict/screens as in D3–D5. Credit the higher-weight literature and repository prior art. **Do not export the current proposed FRONTIER paragraph.**
