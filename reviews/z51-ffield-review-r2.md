# Hostile referee report, round 2: EXSET_FUNCTION_FIELD

## Scope and bottom line

**MAJOR revision required.** The headline Theorem 3.5 survives: for the specified monic analogue, the brief's fixed-degree Goal 1 really is false. Proposition 3.7(a), including the absolute exponent `1/16`, also survives. The new class-overlap proof can support Proposition 3.7(b), but the manuscript still contains a false assertion about *distinct words*, as opposed to distinct unordered classes. The fixed-q and transfer discussions contain additional substantive overclaims.

**Version boundary matters.** I initially read commit `134af22b`, with C2 labelled CONDITIONAL. During the review the author committed `98a86b72b5bb8bf364c08f5d20da060797ca1e24`, adding a purported proof. This report audits both versions, and its final mathematical findings refer to **98a86b72**. A further §3.9 appeared subsequently, initially uncommitted; by report completion HEAD had advanced to `e8bdecb221ab3d0d4cc9302c1f6786f44dd50432`. That later material is **outside this report's verdict**. Line references below refer to 98a86b72, before that insertion. Do not cite this report as approval of §3.9.

I changed no existing file and made no commit. All shell invocations used `ulimit -v 8000000`; executable commands were timeout-wrapped. Binaries and the downloaded citation were kept under `/tmp`. An independent proof-audit subagent checked §3.8; I reviewed its conclusions and checked the subsequently added C2 proof myself.

## 1. R1 repair checklist

| R1 issue | R2 status | Finding / remaining repair |
|---|---|---|
| Converse after (1.1) lacked proper degree bounds | SOUND | `1 ≤ deg A < n` now forces `deg v < n` and makes both constructed factors monic. |
| Lemma 1.1 and square obstruction | SOUND | Reciprocity and the argument prime-by-prime through a possibly nonsquarefree A remain valid. |
| U′ normalization and sufficient threshold | SOUND | Proper-degree bounds retained; `q > (n+1)²` is correctly only sufficient. |
| False non-nesting claim | SOUND | Corollary 1.6′ proves `ES₅,q ⇒ U_q`; the parity argument and swapping u,v are correct. Strictness at `(3,3)` is consistent with the counts. |
| Exact shape mass | SOUND | The formula with `k=floor((n−1)/2)` and all displayed small values are correct. Define k also in summary row 4. |
| Finite-flatness weight wording | SOUND | Leading coefficient contribution now has source weight zero. Filtered freeness and the top Jacobian argument work in every characteristic. |
| Unrestricted large-q limit | SOUND | Theorem 3.3 now states the per-characteristic limit and separates stable characteristic. The bounded-equation justification addresses uniformity in p. |
| Boundary specialization | SOUND | The henselian finite-étale explanation repairs the possible unramified-closure ambiguity. Constants inject into the regular generic-root residue field. |
| Every q / every union / trivial words | SOUND in theorem; MINOR in prose | Theorem 3.5 correctly excludes `(n,0,0)` and keeps the error/threshold. “Forest … empty” in §3.5 and “no word at all” in §4.1 still need “nontrivial.” |
| Corollary 3.5′ scaling | SOUND | Roots scale by `μ⁻¹`; adjoining the target splitting field preserves the boundary argument. |
| 29/144, Poisson limits, disjointness criterion | SOUND repairs; MAJOR new prose issues | 29/144 is conditional; the parity-asymptotic conjecture and Galois-closure branch-component criterion are corrected. New independence prose still overstates the computation; see §5 below. |
| Extinction / square defects | SOUND in §2; MINOR recurrence | §2 now restricts the evidence and supplies the corrected square-defect table. §4.1 again incorrectly says there are `3^floor(n/2)` squares for odd n. There are none. |
| Depth accounting | MINOR residual defects | The hypothetical budgets are now labelled Assessment, but “relative error,” “only if,” and the missing explicit `m_n ≍ n²` hypothesis need repair; §6 below. |
| Prime-family trimming | SOUND | The uniform mass lower bound, trimming, and final exponent check; §3 below. |
| Higher overlap moments | MAJOR literal defect; intended argument repairable | Bounded fibres really do reduce all fixed j to an overlapping-pair probability. That probability must concern distinct classes, not distinct ordered words; §4 below. |
| Numerical provenance | SOUND for inspected records | Missing `(7,4)` and `(11,3)` records are now present; `(163,3)` is corrected to 866671/4330747. Requested new reruns agree. |

Thus “all repairs applied” is too categorical: the main R1 repairs are present, but some discarded wording reappears, and the new material creates further problems.

## 2. Theorem 3.5 / Corollary 3.5′ — SOUND

I specifically tried to break the conclusion “the brief's Goal 1 is false.” I found no counterexample or missing hypothesis that invalidates the repaired theorem.

1. The weighted degeneration is a purely transcendental base change of the original cover off `μ=0`.
2. At the generic point of `μ=0`, every factorization cover is finite étale. Its splitting algebra is therefore unramified as well, not merely at one selected place of a non-Galois extension.
3. The special splitting field is the generic degree-n polynomial's splitting field. Its constants are the base field, and its group is S_n.
4. The boundary n-cycle fixes no ordered partition with at least two nonempty blocks. All allowed shapes except `(n,0,0)` have this property.
5. Regularity and uniform bounded-complexity Chebotarev give a class density at least `1/∏ D_σ!`, with an `O_n(q^(−1/2))` density error. This produces a positive proportion only for sufficiently large q, exactly as now stated.
6. Adjoining the splitting field of f itself makes the same boundary element an n-cycle on f's roots. Its Frobenius class therefore also forces irreducibility.

The simultaneous prime/nontrivial-wordless claim is not contradicted by the small-q extinction data: the threshold and error are essential. The upper bound `q^(n/2)` for the number of squares is harmless when n is odd, provided it is not described as the exact odd-degree count.

**Exact repair:** preserve the theorem. Replace residual “empty forest/no word” language by “no nontrivial word.” Keep the normalization qualification: this refutes Goal 1 for U_q, not for every conceivable function-field ES analogue.

## 3. Proposition 3.7(a) — SOUND

### Exact Bonferroni

Group selected classes by their prime modulus A, with total probability x_A. Different classes at the same A are disjoint. For distinct primes whose total degree is at most n, the congruences are exactly independent for a uniformly random monic degree-n f. Thus the actual Bonferroni sums through order 2L equal `e_i(x)` when `2Lz ≤ n`.

Comparing the even truncation with the independent model gives

    P(avoid) ≤ ∏(1−x_A) + e_(2L+1)(x)
             ≤ exp(−μ_C) + μ_C^(2L+1)/(2L+1)!.

This argument does not require CRT at order `2L+1`: that last comparison is in the independent model. No hidden large-q hypothesis occurs here.

### Uniform RH mass lower bound

For fixed k, summing the progression error over all monic degree-k v costs at most

    C₀(k+1) q^(k+d/2)/d.

The chosen k₀ makes this at most `q^d/(4d)` after enlarging C₀ if necessary. The prime-count main term is at least `q^d/d − 2q^(d/2)/d`, because `Σ_(deg v=k) 1/Φ(v) ≥ 1`. Taking an absolute d₀ sufficiently large yields the claimed `q^d/(2d)` bound uniformly for `q ≥ 3`.

For large odd d, `k₀+1 ≥ d/4`, hence the degree-d mass is at least 1/8. **Odd degrees alone** therefore yield

    μ(z) ≥ z/16 − O(1)

with an absolute constant. The even-degree `1/16−o(1)` sentence is unnecessary; summing an unspecified o(1) would not by itself give an O(1) error, but the odd-degree argument avoids that issue completely.

### Trimming and the constant

If the full mass is below `z/16`, retain it all. Otherwise take a maximal subcollection below that target; its shortfall is at most `1/q`, the maximum single-class mass. This proves the claimed two-sided bound for μ_C.

With `z=floor(sqrt(n))` and `K=2L+1` the largest odd integer at most `n/z`, one has `K ≥ sqrt(n)−2` and `e μ_C/K ≤ 1/2` for sufficiently large n. Thus the remainder is at most `2^(−sqrt(n)+2)`, and the product is at most `C exp(−sqrt(n)/16)`. Increase C for the bounded remaining n.

**Exact repair:** none needed for the result. Simplify the mass proof by explicitly using odd degrees alone. The bound is genuinely uniform in q, including extension fields; the C enumeration only handles prime q, but the proof does not share that restriction.

## 4. Proposition 3.7(b), C2, and the claimed reduction

### 4.1 Coprime part — SOUND

For a prime P of degree e and class weight `w_c=q^(−deg M_c)`, the estimate

    Σ_(P|M_c) w_c ≤ 2D² q^(−e)

is valid: within each ordered degree type, P dividing u or v costs `q^(−e)`; passing to unordered pairs can only decrease this upper bound. Consequently

    Σ_P (Σ_(P|M_c) w_c)² = O_D(1/q).

The pair-union bound in the product measure therefore bounds the noncoprime contribution to `e_j` by `O_(D,j)(1/q)`. Since the maximum class weight is at most `q^(−2)`, repeated indices also contribute o(1), so the coprime part tends to `μ_D^j/j!`.

**Exact repair:** distinguish the finite-q mass `μ_D(q)` from its limiting value. An equal-degree unordered type has mass `1/2 + 1/(2q^a)`, not exactly 1/2. Admit an unordered type if at least one orientation is U-admissible: `s` odd or `a` odd or `b` odd.

### 4.2 The bounded-fibre reduction — SOUND as an inequality

For every f the number of hit classes is at most the number of words, at most `B(n)=ΣD_σ`. A noncoprime compatible j-tuple contains an overlapping pair. Hence

    noncoprime contribution ≤ B(n)^j P(E₂)

really is a valid upper bound. It does not assume pairwise independence, and it does not omit a higher-cluster loss. B(n) depends only on fixed n, so a correct o(1) pair-probability estimate is sufficient.

### 4.3 The event E₂ is false as stated — MAJOR, with an explicit counterexample

At lines 418–424, E₂ means two **distinct small-modulus witness words** sharing a root of their moduli. Those words are ordered triples by Definition 1.2. C2's assertion `P(E₂) ≤ C(D)/q` is false.

Take `n=4, D=2`. For every monic quadratic t and distinct monic linear polynomials u,v, both

    (t,u,v) and (t,v,u)

are distinct U-witness words of shape `(2,1,1)` for the same f. Their moduli are the identical polynomial uv. There are `q²q(q−1)=q⁴−q³` such ordered triples. The degree of this finite flat word map is 12, so its image has at least `(q⁴−q³)/12` points. Therefore

    P(E₂) ≥ (1−1/q)/12,

which does not tend to zero. The initial CONDITIONAL version of C2 was thus a false hypothesis under its literal definition. The new PROVED version retains the same false probability consequence, even though its displayed class sum excludes the offending swaps.

**Exact repair:** throughout the reduction and C2, define

    E₂* = {f has two hit classes {u,v} ≠ {u′,v′}
           whose moduli have a common root}.

Replace E₂ by E₂*. This is a real statement correction, not a proof that the originally defined event is rare. It is not a counterexample to the intended `n^(2/3)` upper bound.

### 4.4 The newly added class-sum proof — SOUND after that distinction

I checked all three cases in commit 98a86b72, rather than treating its label as evidence.

* Nonsquarefree h: there are `O(q^(γ−1))` possibilities, and divisor splittings have bounded multiplicity depending only on D. Dropping compatibility is sufficient.
* Squarefree h, `γ<d′`: assigning its factors to u′ and v′ gives coprime pieces. The two residue conditions on the complementary monic factors have at most `max(1,q^(a′−γ))` and `max(1,q^(b′−γ))` solutions. The displayed exponent inequality follows in all four cases from `a′,b′≥1` and `γ≤a′+b′−1`.
* Divisibility case `γ=d′`: the four-piece factorization and cancellation modulo each piece are valid. They force one residue class for x and y. The second exponent inequality follows from `γ<a+b`. Equal products plus compatible residues force equal sums, hence the same unordered pair, already excluded.

These are upper counts; possible multiple representations of a pair do not invalidate them. Repeated factors in uv outside, or in excess of, the squarefree h also do not invalidate the congruence counts. Thus the **distinct-class** sum is `O_D(1/q)`, and a union bound gives `P(E₂*)=O_D(1/q)` when `2D≤n`.

The remaining optimization is valid: `μ_D ≫ D²`, also `μ_D ≪ D²`; choose `D=c₀n^(1/3)` with c₀ small and even Bonferroni depth of order `n/D`. Both the product and factorial remainder are `exp(−c n^(2/3))`. Small n can be accommodated by reducing c.

**Conclusion:** after replacing E₂ with E₂*, Proposition 3.7(b) can legitimately remain PROVED in the revised version. In the initial version its CONDITIONAL label was honest about the missing proof, but its stated hypothesis was false.

### 4.5 C2 numerical check — MINOR normalization error

The script sums **unordered pairs of distinct classes**, whereas the lemma displays a sum over **ordered pairs**. I reproduced:

| q | classes | compatible unordered pairs | q times unordered sum |
|---|---:|---:|---:|
| 3 | 33 | 75 | 2.1852 |
| 7 | 371 | 2793 | 2.8251 |
| 11 | 1397 | 18535 | 3.0466 |

For the lemma's ordered sum, double the last column. The asymptotic estimate is unaffected.

**Exact repair:** label the numerical check “unordered-pair sum, half the displayed lemma sum,” or double the printed values.

## 5. §3.6 independence test — computation SOUND; interpretation MAJOR

Requested reruns reproduce the archive:

| q,n | genuine joint/product | with f+1 joint/product | selected mixed moment |
|---|---:|---:|---|
| 43,4 | 0.9990 | 0.9981 | 2.0021 versus 2 |
| 23,5 | 1.0982 | 1.1570 | 2.0866 versus 2; 4.1733 versus 4 |
| 11,6 | 1.7686 | 2.4274 | 4.3579 versus 4 |

There are nevertheless four problems.

1. **Evidence is not a convergence theorem.** “The defect decays like C(n)/q” and “so the compositum behaves like a direct product” are not certified by a few q. At n=4 the sign even changes. Write “the sampled defects are consistent with …”; retain independence/product-monodromy as a conjectural interpretation.
2. **The n=6 test is not precisely the U-class test.** The code includes `(s,a,b)=(2,2,2)`, which has no U-admissible orientation. Thus its six-class avoidance event is stronger than U-avoidance. This is not a faulty enumeration—the script says all genuine classes—but it is a scope mismatch if used as a direct U independence test. Exclude that class for a U-only table, or explicitly retain and label the broader test. At `(11,6)` its joint-with-f+1 probability is about .00400, whereas total U-failure probability from the engine is `12397/1771561 ≈ .006998`.
3. **W_c is not normalized as the Poisson variable.** The code adds both orientations for unequal degrees, giving mean 2; for equal degrees it counts ordered u,v, giving mean 1. The heuristic variables have means 1 and 1/2. Zero probabilities are unchanged, so the ratios remain valid. Explain that counts must be quotiented/renormalized before comparing distributions or moments to those Poisson means; the equal-factor diagonal produces a finite-q correction.
4. **The claimed modulus bound is false.** Lines 341–342 say the smaller of `tv−1` and `tu−1` has degree at most `(n+1)/2`. For shape `(3,1,1)`, n=5, both degrees are 4, not at most 3. Generally their minimum degree is `s+min(a,b)=(n+s−|a−b|)/2`. The alternative modulus uv has degree a+b, but is not one of those two divisors. State explicitly which parametrization is used and impose the actual total-degree condition. The accompanying irreducibility/dimension assertion needs a proof, not the numerical table. For overlapping moduli use `deg lcm`, not a sum of degrees, when deciding whether at most one f can occur.

**Exact repair:** keep the finite table CERTIFIED; move all asymptotic/product conclusions under EVIDENCE/CONJECTURE; fix the modulus calculation and class scope. The R1 branch-component repair itself is sound.

## 6. §3.7 depth rewrite — MINOR residual mathematical wording

The elementary identity `q^(n−1/2)=N^(1−1/(2n))` is correct, as is its inability by itself to resolve the even-degree square floor.

For the conditional budgets, write the hypothesis unambiguously as

    |δ_q(n)−ρ_n| ≤ E_n q^(−1/2),  ρ_n=exp(−m_n).

This is an **absolute error in density**, not an error relative to ρ_n. The displayed condition

    (log q)/2 − log E_n − m_n → +∞

is sufficient for that error bound to be o(ρ_n). It is not a necessary condition on the actual error, which might be far smaller than its upper bound. Replace “only if” by “is ensured if.” If “relative error” were intended literally, the `−m_n` term would not belong there.

Also explicitly assume `m_n ≍ n²` in the two illustrative cost models; it does not follow merely from writing `ρ_n=e^(−m_n)`. The least-q calculations then give the advertised exponents, subject also to the stable-characteristic threshold. They remain budget analogies, not impossibility theorems.

## 7. §4.1–4.2 numerics and FF-RLD-U

### 7.1 Numerical tables and irreducibles — SOUND for the audited entries

RLD reruns:

| n | z | nonsquare sifted | μ(z) | Mertens product | ratio |
|---|---:|---:|---:|---:|---:|
| 10 | 5 | 345 | 5.0247 | 4.094822e−3 | 1.4268 |
| 10 | 6 | 243 | 5.7709 | 1.934940e−3 | 2.1268 |
| 10 | 8 | 75 | 8.0608 | 1.947306e−4 | 6.5225 |
| 10 | 9 | 57 | 9.6051 | 4.152828e−5 | 23.2444 |
| 12 | 6 | 1348 | 5.7709 | 1.934940e−3 | 1.3109 |
| 12 | 8 | 328 | 8.0608 | 1.947306e−4 | 3.1695 |
| 12 | 11 | 70 | 11.9809 | 3.858570e−6 | 34.1363 |

All agree with Table 4.1. Inspection of the implementation confirms the prime sieve, the duplicate `v=1`/`v=A+1` correction, the degree minima, and square removal for these runs.

With `Z51_IRR=1`:

| q,n | irreducibles | irreducible U-failures | nonsquare U-failures |
|---|---:|---:|---:|
| 3,8 | 810 | 3 | 21 |
| 3,10 | 5880 | 0 | 12 |
| 3,14 | 341484 | 0 | 3 |
| 43,4 | 854238 | 62651 | 268277 |
| 23,5 | 1287264 | 11477 | 67137 |

The reported irreducible fractions .073341 and .008916 are correct. The irreducibility sieve exhausts all products with a factor of degree at most n/2; its counts also match the standard irreducible-polynomial formula. The mass and square controls pass in these reruns.

These are sample audits, not an independent recomputation of every archived entry. “No irreducible failure beyond n=8” must retain “in the tested q=3 range, through n=15”; the zeros at odd n follow from the total-failure data.

### 7.2 Conjecture and numerical consequence — MAJOR

Conjecture 4.1 is a clear conjectural upper bound and correctly removes squares. Set `z=floor(n/s)` explicitly; asymptotically `z<n` for fixed s>1. The finite ratio table supports plausibility, not the sentence “at fixed s the ratio stays O(1)” as an established asymptotic.

More importantly, the consequence with exponent

    1 − 1.03/(s log 3)

and threshold `s<1.87` does **not follow from Conjecture 4.1 alone**. It silently promotes a finite-data estimate for μ(z)/z to an asymptotic theorem. The text itself labels the fixed-q constant an Assessment. No proof of `μ(z)≥1.03z+o(z)` is supplied. The table even shows a changing odd/even increment pattern; it is not a derivation of a limiting coefficient.

**Exact repair:** write the valid implication in terms of μ:

    #non-square U-failures ≤ exp(C(3,s)) 3^n exp(−μ(floor(n/s))).

Under the additional proved or separately conjectured lower asymptotic `μ(z)≥κz+o(z)`, this yields exponent `1−κ/(s log 3)` and beats the square floor when `s<2κ/log 3`. Label the substitution κ=1.03 as numerical extrapolation unless a theorem is provided. The uniform `κ=1/16` lower bound is proved, but does not give the advertised below-square-floor range for s>1.

## 8. §4.3 rank/budget and the Sawin–Shusterman citation — MAJOR

### Citation: checked and correct, but narrower than the discussion

I visited and read Theorem 1.3 in arXiv:1808.04001v2, PDF page 3, and checked the journal metadata:

* https://arxiv.org/abs/1808.04001
* https://arxiv.org/pdf/1808.04001
* https://annals.math.princeton.edu/2022/196-2/p01

The journal reference is **Annals of Mathematics 196 (2022), 457–506**. Theorem 1.3 indeed assumes an odd p and `q>p²k²e²`, and proves k-point Chowla for distinct fixed polynomial shifts as degree grows. Thus `k<sqrt(q)/(pe)` is the correct range **of that theorem**. For q=p it supplies no positive k. It does not say that no shifts can ever be controlled at prime q; even k=1 has separate elementary cancellation. The paper describes a power saving inversely proportional to p, not a universal square-root error for its Chowla theorem. Its short-character-sum argument uses substantial geometric input beyond quoting one-variable Weil.

### Exact defects and repairs

1. **Missing nondegeneracy in the Weil formula.** The product must not be a constant times a square (with the usual nontrivial-character condition). As printed, take `P₁=P₂=T`: the sum is `q−1`, not at most `2sqrt(q)` for large q. Add the hypothesis and absolute-value notation.
2. **Counts are not indicators.** The trace of `φ_{σ*} Q̄_ℓ` is `W_σ(f)`, not `1_{W_σ(f)>0}` or `1_{W_σ(f)=0}`. Its generic rank is indeed D_σ. A product of these count traces has rank product D_σ, but a **joint avoidance indicator** is a different class function. No rank-product bound for that indicator follows without an explicit representation/expansion. Replace “U-event” by “witness-count trace,” and present a separate, genuinely justified complexity hypothesis for indicators.
3. **Rank alone does not bound all Betti numbers by rank times C^n.** Conductor, boundary geometry, and the actual sheaf matter. Even after middle-degree concentration, the coefficient is the relevant Betti number. Keep the proposed estimate explicitly hypothetical, with its geometric complexity conditions.
4. **The rank-one arithmetic contradicts “enough.”** At fixed q, `n log q/log n=o(n)`. This is not enough for the immediately preceding target `μ(z)≍n` events. Delete “— enough,” or change the target/cost model and justify it. Rank one itself also does not imply a loss of only O(1) per event.
5. **A sufficient range is not an upper bound on all methods.** Neither this citation nor the illustrative rank budget proves that all fixed-q geometric methods control only boundedly many shifts. Replace the universal claims in §4.3, §5.2, and summary row 11 by statements about these particular estimates/approaches.

The least-inert-prime observation is compatible with the standard RH bound and correctly concerns colour data, not witnesses. The fixed-q `exp(−sqrt(n)/16)` baseline is sound. “That is the strongest … this lane proves” should clearly refer to that baseline, not to the weaker polynomial bound in the immediately preceding bullet.

## 9. §5 transfer and the integer-exponent headline — MAJOR

### What really is proved

The same optimization powers appear: sqrt(n) for the prime family at every q, and n^(2/3) for U after taking q→∞ at fixed n, with the corrected class event in C2. This is a meaningful calibration. It is **not** a proof that these are optimal consequences of exact CRT, nor that all non-CRT methods are unavailable over the integers.

### Required repairs

* **Exact CRT is not EH.** For ordinary integers, counting all integers in one residue class modulo M is already `N/M+O(1)`, and CRT is an unconditional algebraic theorem. EH concerns averaged prime-distribution errors, not exact uniform distribution of all integers modulo every M≤N. The transfer-table row “stronger than EH / conjectural (EH)” conflates these statements. Replace it by the elementary integer congruence count, with accumulated endpoint errors under multiple-event summation; discuss prime-distribution conjectures separately if needed. Delete the equivalence arrows in “GRH ⇔ Weil” and “level-1 ⇔ exact CRT”: these are analogies, not equivalences.
* **Open is not impossible.** The fact that FF-RLD-U remains unproved here while RH and CRT hold does not prove that those inputs cannot imply it. §5.3(a) acknowledges this, but the categorical transfer verdict, summary row 12, and “best provable FF bound” revert to a stronger claim. Say “this manuscript derives no such implication; the stated estimates do not establish it.” Do not assert a mathematical non-implication or an optimality theorem.
* **The true density is not computed.** In the audited commit, `p_f(n)e^(−M_g(n))` and `exp(−Θ(n²))` remain heuristic/conjectural. Chebotarev expresses the density as a finite-group statistic; it does not prove big monodromy. Restore the conjectural qualification in the monodromy table row, the “gap is closed” paragraph, and summary row 8. Even a separate upper bound of order `exp(−c n²)` would not by itself prove a matching Θ statement.
* **No quotient has been constructed.** “CRT sees only the abelian quotient information of G_n” is a metaphor unless a map/quotient is actually supplied. Exact congruence counting is not automatically an abelian quotient of the word-cover monodromy group. Also S_n is nonabelian only for n≥3. Replace this with the precise contrast: CRT computes certain bounded-total-degree intersections, whereas Chebotarev describes the full joint Frobenius action.
* **No universal absence of integer nonabelian information.** Algebraic number fields and nonabelian Chebotarev exist over the integers. What is missing here is a corresponding family/cover and a usable estimate for this particular U problem. Qualify “has no integer counterpart” accordingly.
* **Chowla row overstates the cited error and the status.** The cited fixed-q theorem gives cancellation/power saving in its range, not the table's `sqrt(N)` error. Moreover “k=2 log-averaged only” is too sweeping: the cited paper itself notes the odd-k logarithmically averaged results. State the exact conjectural integer input being discussed, rather than identifying it with a theorem having different quantitative strength.
* **Poisson implication versus equivalence.** A quantitative counting bound `#exceptions≤N exp(−c(log N)²)` would force eventual absence. A qualitative Poisson heuristic does not itself do so, and full distributional independence is stronger than an empty exceptional set. Phrase §5.3(c) as a sufficient lower-tail hypothesis unless the precise referenced equivalence and its assumptions are stated.

## 10. Summary-table faithfulness

| Row | Verdict | Required change |
|---|---|---|
| 1–3 | SOUND | Preserve normalization and proper-degree qualifications. |
| 4 | MINOR | Define k in the summary. |
| 5 | SOUND | Implicitly restrict to admissible/nondegenerate shapes. |
| 6 | SOUND | The headline is supported; constants may be reduced when absorbing the error. |
| 7 | MINOR | “Sampled densities are consistent with” rather than certified limiting agreement/convergence. |
| 8 | MAJOR | PROVED applies to the CRT bounds, not the asserted “true exp(−Θ(n²))” or completed monodromy gap. Correct C2's event. Split labels within the row. |
| 9 | MINOR | Keep the budget qualifications; fix the sufficient-condition/error terminology. |
| 10 | MINOR | Restrict all zero-failure statements to tested degrees; O(1) ratio behavior is conjectural. |
| 11 | MAJOR | Restrict the Sawin–Shusterman range to that theorem; distinguish count traces from event indicators. |
| 12 | MAJOR | Replace a non-implication claim by the narrower conclusion that no implication is established here. |
| 13 | MINOR | Do not say all R1 repairs are complete without acknowledging the residual issues. |

## 11. Reproduction commands

Each command below was run with the memory limit; the larger runs were inspected beforehand. The largest requested arrays are tens of megabytes, not Cartesian products of all f with all words. The C2 Python check streams pairs (1397 classes at q=11,D=3), rather than allocating a pair matrix.

```sh
ulimit -v 8000000
timeout 30s gcc -O2 -o /tmp/r2rld scripts/z51_ffield_rld.c -lm
timeout 90s /tmp/r2rld 3 10
timeout 120s /tmp/r2rld 3 12

timeout 30s gcc -O2 -o /tmp/r2joint scripts/z51_ffield_joint.c
timeout 120s /tmp/r2joint 43 4
timeout 120s /tmp/r2joint 23 5
timeout 60s /tmp/r2joint 11 6

timeout 30s gcc -O2 -o /tmp/r2enum scripts/z51_ffield_enum.c
timeout 120s env Z51_IRR=1 /tmp/r2enum 3 8
timeout 120s env Z51_IRR=1 /tmp/r2enum 3 10
timeout 180s env Z51_IRR=1 /tmp/r2enum 3 14
timeout 120s env Z51_IRR=1 /tmp/r2enum 43 4
timeout 180s env Z51_IRR=1 /tmp/r2enum 23 5

timeout 90s uv run --no-project scripts/z51_ffield_c2check.py 3 3 7 11
```

## Overall verdict

**MAJOR.** The central positive-density theorem is sound, and both CRT exponent bounds are supportable after correcting the distinct-class event. I found an explicit false PROVED consequence in the current C2 wording, but it has a local repair and does not falsify Proposition 3.7(b)'s intended conclusion; I therefore do not classify the manuscript's central results as FATAL. The numerical reruns pass. Acceptance still requires fixing that event, the count-versus-indicator confusion, the unsupported fixed-q coefficient, and the transfer/summary overclaims. This verdict does not cover the subsequently added §3.9.
