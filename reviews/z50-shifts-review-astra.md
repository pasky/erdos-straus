# Hostile cross-model review: z50 lane D / shifts

Reviewed: `EXSET_SHIFT_DIVISORS.md`, current round-1 draft, against the z48–z50 contexts, lane brief, `DISCOVERIES.md` (D)17–(D)31, and `EXCEPTIONAL_TUPLES.md` §4. Reviewer: Astra. **Erdős–Straus remains OPEN.**

## Overall verdict: MAJOR repairs required

The strongest clean parts are Lemma 2.1, the fixed-modulus asymptotic, the unrestricted-integer Janson-side estimate, and the conditional negative-association theorem. I did not break those core arguments. The proposed marginal-budget barrier has a real arithmetic ingredient and a valid elementary optimization behind it, but the document repeatedly applies it outside its defined class. In particular, it does **not** impose its precision requirement on conditional-ratio arguments or arbitrary refinements into subevents. Nor does it cap every theorem whose loss is *at most* a fixed constant. The level-coordinate extension has not been proved at the stated level of detail, and the progression version of Proposition 2.4 is literally false.

The character-polynomial reduction works for the 4ℤ line **as a statement about a periodic majorant's CRT mean**. It does not prove that character methods with genuinely non-CRT evaluation are barred. Several statements erase exactly this qualification present in the source proposition.

I found no fatal defect in the surviving fixed-shift/NA mathematics, and no proof of a new exceptional-set exponent beyond existing barriers. The main barrier theorem should not yet be advertised as PROVED for all three families with the current scope language.

## 1. Audit (§§1.1–1.3)

### 1.1 — SOUND

For n ≡ 5 (8), 2 divides n+3 and is −1 modulo 3. The word has t=1 and other endpoint (n+3)/2. For n ≡ 1 (8), n ≡ 2 (3), 6 divides n+7 and is −1 modulo 7. Both reductions are correct. The computation below independently reproduces zero failures for the v=3 marginal on n ≡ 5 (8).

### 1.2 — MINOR-REPAIR for mass/nontransfer; MAJOR for its claimed barrier coverage

* The inclusion of the **4ℤ line** in ℛ(A) is correct: v=4k and A ≡ −1 (v) imply k | (A+1)/4, so its class is −4k modulo A.
* With the explicitly stated **modulus cutoff** A≤X, the endpoint-class mass is indeed Θ(log²X). The lower bound already comes from Σ_{A≡3(4)} τ((A+1)/4)/A; the upper bound for both lines follows from Σ_{A≤X} τ(A+1)/A. This is a first-moment/class-mass statement, not a survival theorem or a proved general CRT cap of exponent 2/3. Keeping “natural exponent 2/3” as Assessment is correct.
* “Such a class is a U-class only when u²w | uvw” is false because labels can collide modulo M. Concrete example: M=15, (M+1)/4=4, (u,v,w)=(4,1,1). The label D=u²w=16 does not divide 4, but −4D≡−4 (15), an endpoint-4 U class. The integer divisibility criterion identifies a sufficient subfamily, not an iff criterion for residue-class membership. If the intended note subfamily imposes further size/coprimality restrictions, state them and prove the relevant noncollision statement instead.
* The 3/4 note supplies no automatic bound for E_U: U-solvability implies ES-solvability, so the exceptional-set inclusion goes in the wrong direction. This conclusion is sound, but not a proof that no reworking of its argument can bound E_U. There really are forced ℛ(M) hits at known U failures: n=105, M=47, A=12, D=9 gives 47 | 105+4·9. Similarly (n,M,D)=(2961,23,36) and (3985,19,25). These are better illustrations than the false label iff.
* A cap for the 4ℤ **subfamily does not cap the union with the odd line**. The document expressly leaves the odd-line membership unchecked, then concludes that any U method reaching the target must be non-CRT. That conclusion needs the missing membership proof, or must be weakened. A cap for a larger forced family passes to its subfamilies; the converse inference from one line to their union is invalid.
* “U is the same B=2 family as the ES₅ two-endpoint family” must not identify their survival laws: the cited `CONJECTURE_S_MODEL.md` proves one side of the ES₅ model law, with other sides conditional. Matching mass orders alone is not that theorem.

### A standard-input U bound omitted from the audit

I did not locate a published theorem using this campaign's name U. Nevertheless, the claim that the known landscape offers only log-power bounds for U overlooks an immediate **prime-endpoint sieve** consequence of standard inputs:

> Using Titchmarsh-divisor estimates (or their standard BV proof) and elementary Bonferroni, one obtains E_U(N) ≪ N exp(−c√log N).

Here is the argument, sufficiently explicit to distinguish it from a claim of new literature. For each prime ℓ≡3 (4), forbid the distinct residues −4d modulo ℓ, d | (ℓ+1)/4. Every such residue is a U certificate. Write ρ(ℓ)=τ((ℓ+1)/4). The shifted-prime divisor estimates give

    μ(z) := Σ_{ℓ≤z, ℓ≡3(4)} ρ(ℓ)/ℓ ≍ log z.

These are independent prime-local events in the CRT model. Truncate inclusion–exclusion at an even depth K=Cμ, with C a sufficiently large absolute constant. Its model expectation is at most exp(−cμ): the true product is ≤e^(−μ), and the next elementary-symmetric tail is ≤μ^(K+1)/(K+1)!. On the integer interval each selected intersection of residue classes has counting error O(1); the entire coefficient error is at most exp(O(K log z)), even using a crude polynomial bound for Σρ(ℓ). Set log z=c₁√log N with c₁ small. This error is N^δ for a fixed δ<1, and the desired estimate follows. Restricting to n≡1 (8) just adds the fixed modulus 8. No closure under scaling is needed.

This is the prime-local θ=1/2 implementation already anticipated in z50 CONTEXT §4(a), not a new campaign advance and not the θ=2/3 conjectural composite implementation. It should be acknowledged or explicitly excluded by “output of this lane's fixed-k argument.” In particular, do not conflate “Prop 4.1 proves only log powers” with “nothing with θ>0 is available for U.”

## 2. Single-shift mathematics

### Lemma 2.1 — SOUND

The frequent terms contain enough copies of each group element to realize its whole cyclic subgroup, and copies belonging to distinct residue values are disjoint. Thus all of H is realizable. There are fewer than |G|² terms outside H. In case (c), the representation of gs⁻¹ uses only frequent terms in H and cannot reuse the selected outside term s. This is precisely the point needed for the index-2 case; it is valid.

### Theorem 2.2 — SOUND

For fixed v, subgroup-supported integers have the claimed Wirsing asymptotics. Primes dividing v contribute only finitely many Euler factors. For the exceptional case of a subgroup of index at least 3, the bound on the number of outside prime factors, combined with y^{Ω_out−K}, gives x(log x)^(−δ)(log log x)^K. The Shiu constants can be chosen uniformly for 0<y≤1 because these weights are bounded by 1; the progression-prime harmonic estimates have constants depending on fixed v.

Distinct index-2 subgroups have index-4 intersection. Hence pairwise intersections are O_v(x/log^(3/4)x), while all higher-index remainder terms are o_v(x/√log x). First-order inclusion–exclusion yields exactly the sum of Landau constants asserted. The CRT criterion for −1 to be a nonsquare, and its application to the admissible endpoint moduli, are correct.

Important qualification: this theorem counts **unrestricted m≤x**. It does not identify the same constants for m=n+v on n≡1 (8), and it is not uniform for growing v. The later summary must preserve both distinctions.

### Theorem 2.3 — MINOR-REPAIR; main inequality SOUND

I checked the potentially dangerous analytic steps:

1. For z=κ/2∈[1/2,1), z^{Ω} meets Shiu's hypotheses. On a full dyadic block of scale D≥v², the modulus v≤D^(1/2) has a fixed-power margin inside the allowable range q<Y^(1−α), where the interval length Y is comparable to D. There is no large-modulus obstruction here. Handle the first/last partial blocks by enlargement to full dyadic blocks; a constant-factor change in the threshold is harmless.
2. On such a block, x/d and the logarithmic weight for the cofactor vary by bounded factors, including the last block where log(2x/d) is O(1). The convolution sum is bounded by a constant times J^(2z−1), J≈log x. Endpoint contributions are also bounded by this quantity for every fixed z>0. This remains valid when z<1/2, as used in Prop 2.5.
3. z^(−κL₂)(log x)^(2z−1) has exponent κ(1+log2−logκ)−1. Subtracting βlog2 at κ=β gives −Q(β), correctly.
4. The unrestricted moment Σκ^{Ω(m)}≪_κ x(log x)^(κ−1) is valid for fixed κ<2, e.g. by Selberg–Delange. **Ordinary Shiu cannot be cited directly for this moment when κ>1:** κ^{Ω(2^a)}=κ^a violates the condition f(n)≪_ε n^ε for every ε>0. Remove “or Shiu” or supply an appropriate prime-power decomposition. The valid Selberg–Delange alternative already repairs this proof.
5. The trivial reciprocal-divisor bound and the final all-large-v conclusion are sound. φ(v)≫v/log log v costs only a log-o(1) factor in the polylogarithmic range. For fixed 1<β<2, the remainder (1+log v)/v is smaller than log^(−Q(β)) when φ(v)≥log^(βlog2)x.

The claimed large-deviation exponent is an upper bound on hit probability, not a matching asymptotic. “Janson side” is terminology, not use of Janson's inequality.

### Proposition 2.4 — MAJOR as stated

The **unrestricted m≤x** floor is sound, with harmless adjustments of the BT cutoff constants and removal of the p≤v contribution. The progression extension is not proved by the stated argument and is literally false for its stated range of v:

    v=3, n≡1 (8): 2 | n+3 and 2≡−1 (3), so P(fail_3(n+3))=0.

If the intended restriction is v∈4ℤ∪(8ℤ+7), write it. Even then the proposed prime argument is invalid for the entire odd line: for example n+7 is always divisible by 8 and never a prime. The later 2^a·p argument is the appropriate replacement, not PNT for primes n+v. Do not quote the unrestricted prime proof as proving the progression cost bound.

### Proposition 2.5 — SOUND

Sathe–Selberg at k=⌊β′log log x⌋, fixed 0<β′<β<1, gives the stated logarithmic rate and the √L₂ factor. The large-divisor term is smaller by log^(−(β−β′)log2)x. For the small-divisor argument one needs to say that d<v²≤x^(1/2), so log(x/d) is comparable to log x; the displayed replacement of log(x/d) by log x is then valid despite the negative exponent. The residual ratio is O(√L₂(1+log v)/v)=o(1). Letting β′ approach β is legitimate in the usual logarithmic-exponent sense (or by a diagonal argument); no uniform Sathe–Selberg theorem up to a moving endpoint has been established or is needed.

### Conjecture 2.6 and the summary table — MINOR-REPAIR

The label CONJECTURE is appropriate. Theorem 2.2 for fixed v does **not** prove the proposed half-L₂ cap along growing v=(log x)^{βlog2+o(1)} for 0<β<0.1867. Say this explicitly instead of presenting the minimum with 1/2 as partly established throughout that range. The summary's hit→1 below the threshold uses the classical Erdős theorem, not Propositions 2.4–2.5; cite it in that row.

## 3. Dependence and correlation claims

### Theorem 3.1 — SOUND

The one-nonzero-coordinate proof of NA is correct, including the reduction for decreasing functions. Independent union preserves NA, and each failure indicator is a nonnegative decreasing function of a disjoint block of prime-power exponent coordinates. Induction on the number of blocks is valid.

The exact fibre in the theorem is right: condition on **all residues modulo p^{A_p} for p≤D_V**, not merely modulo p. The non-strict inequality matters: with shifts 4 and 7, D_V=3, and p=3 can divide both shifted integers. Primes p>D_V cannot do so. The prose “residues modulo the primes” should be replaced by “full capped prime-power coordinates.”

The preliminary divisibility m_v | n+v actually holds without the extra assumption v_p(n+v)≤A_p, because the valuation is capped by a minimum. That assumption is unnecessary, not harmful.

I independently enumerated the model with V={4,7}, prime caps 2³,3²,5²,7, total Q=12600, Q₀=72. All 72 fibres satisfied the asserted inequality.

### §3.1 Remark (3) — MINOR-REPAIR as a heuristic

The profile intuition can be made precise using the appropriate quadratic character associated with −v (after removing square factors), whose conductor divides admissible v. It is not true that (n/p)=+1 puts p in the kernel of **every** odd character modulo v. Example: v=8, p=3, n=1 gives (n/3)=1 and 3 | n+8, but χ_{−4}(3)=−1; the relevant character here is χ_{−8}. Identify the character being used.

The local-factor and k log log k estimates remain heuristic; they are not consequences of NA. NA conditional on full small-prime residues does not imply NA conditional only on a quadratic profile, nor does it imply that every successful interval method must condition on that profile.

### §3.3 correlation technology — MAJOR scope repair

The broad limitation that existing cited results do not supply the needed growing-shift, sufficiently precise law is credible. The stated universal reason is not:

* Nair–Tenenbaum applies to the relevant divisor-closed weights (its more general growth condition even allows A=B=1 here). Henriot makes discriminant dependence explicit, not arbitrary growing-degree dependence. But **neither the uniform e^{O(k)} loss nor the asserted product of the full marginal probabilities is a quoted theorem**. Local/discriminant factors and truncation cannot simply be assigned to a fixed C per coordinate. Call the proposed implementation an Assessment and exhibit an actual estimate before listing it as an instance of 𝔐_C.
* “Additive error” is not intrinsically inadequate. An error N^{1−δ} is much smaller than N exp(−(log N)^θ) for every fixed θ<1. Fixed-shift divisor correlations can have power-saving errors. What fails is the required growing number of shifts, the relevant functions/uniformity, and/or the available **size** of the error. State these separately. An o(N) with no rate, or N/log^B N for fixed B, is indeed insufficient at the desired density.
* Statements about MRT and Tao–Teräväinen need exact theorem citations and hypotheses (averaging, nonpretentiousness, boundedness). A sentence saying that they give an o(1) error for arbitrary fixed multiplicative functions suppresses the main hypotheses.

### (D)21 / Prop 4.3 and the χ-polynomial reduction — MAJOR as advertised; restricted reduction SOUND

For the 4ℤ line, define the finite periodic witness count

    r_{v,N}(n)=Σ_{d≤N+v, d≡−1(v)} 1[d | n+v].

For 1≤n≤N this equals r_v(n+v). If v≤N and P is nonnegative on nonnegative integer vectors, P(r_{v₁,N},…,r_{v_r,N}) is globally nonnegative and expands into a finite linear combination of intersections of witness classes. P(0)≥1 gives the required avoider majorization. For v_i∈4ℤ these are exactly classes covered by the source extension. Thus its CRT mean has the claimed lower bound (with cutoff 2N). **This reduction is valid.**

However:

1. r_v(n+v) itself is not periodic on all integers. The truncation and its interval-only equality must be explicit.
2. The extension as cited is for shifts 4D and moduli ≡3 (4). It does **not apply verbatim to the odd line**; for example v=7 has an allowed witness divisor d=6. A separate extension is needed. This appears repairable using a roughness lower bound that ignores 2: for v≡7 (8), no power of 2 is −1 modulo v, since (2/v)=+1 but (−1/v)=−1. Thus every witness has an odd prime factor q∤v. For a fixed set of admissible shifts, excluding their nonzero residues modulo odd q≤2N gives a product-density lower bound of the same exp(−O(r log log N)) form, also on n≡1 (8). Write that argument instead of citing an inapplicable proposition.
3. **A lower bound on Eν is not a lower bound on its exact sum on [1,N].** Prop 4.3's source explicitly scopes the obstruction to CRT-main-term evaluation. High-period polynomial majorants evaluated with non-CRT interval information are not barred by this reduction. This is precisely one of the campaign's open doors.
4. The statement that 1∗χ “pretends to be 1+χ” is not a standard pretentiousness assertion: 1∗χ is not 1-bounded, and 1+χ is not a multiplicative comparison function. For the principal character its mean is not the finite number L(1,χ), either. Character orthogonality is exact, but these heuristic remarks do not prove that every use of the twisted sums returns only CRT information.

Replace the categorical verdict “the χ-twist does not escape Prop 4.3 or §5” by the precise restricted verdict. The source document is considerably more careful than this draft about non-witness information, exact interval sums, and combining many fixed tuples.

## 4. Assembly

### Proposition 4.1 — MINOR-REPAIR; conclusion SOUND

For a fixed admissible collection of distinct linear shifts, the Nair–Tenenbaum Euler-product argument with y=1/2 gives the exponent −Σδ_i/2≤−k/4 as claimed. The subgroup multiplicities and the factors 2^{φ(v_i)²} are finite k-dependent constants.

There is an omitted hypothesis in the most directly cited formulation: ∏_{i≤k}(n+4i) has fixed prime divisors when k≥3 (already p=3). Do not insert it into a theorem assuming no fixed prime divisor without a reduction. A particularly simple repair is to take **v_i=4k!i** instead. For p≤k all roots coincide at 0, and for p>k there are fewer than p roots, so the product has no fixed prime divisor. All shifts remain admissible and fixed once k is fixed; the same proof goes through. Alternatively, use a precise version with small bad primes removed and explain it. Also take k=⌈4A⌉, not literally 4A when A is nonintegral.

This is routine, not new progress relative to the stronger prime-local sieve consequence described in §1 above.

### Assessment 4.2 — SOUND as an explicitly conditional implementation heuristic

If the implementation is restricted to k costly full-coordinate events seen only through z=N^{1/(Ck)}, then the arithmetic a≤(1−a)log2 gives a≤log2/(1+log2)=0.40938…. Correct algebra. It is not a theorem about Nair–Tenenbaum in growing dimension or all anatomy methods. The existing Assessment label and final qualification are essential; preserve them in the summary.

## 5. Three-family barrier

### Lemma 5.0(a) — MAJOR: V/W essentially sound, T requires an actual proof

For V and W, the hit implication and Theorem 2.3 give the small-coordinate estimate. For a shifted interval use x=N+c, not x=N: the normalization costs at most 16 rather than literally 8 when c≤N. Large c can be disposed of separately. For V/W a hit with c≥3 entails c≤N+2 (indeed slightly stronger bounds are possible); then the trivial divisor estimate gives O(log N/c).

For T, **conditioning on m≡1 (c) is a nontrivial change of measure**, not an application of Theorem 2.3. Three missing points have to be supplied:

* The Ω>K term requires a progression moment

      (1/N) Σ_{n≤N} κ^{Ω(cn+1)} ≪ (c/φ(c)) (log N)^{κ−1+o(1)}

  uniformly in the required polylogarithmic range of c. The unrestricted moment in Theorem 2.3 gives an extra factor c, which destroys the claimed exponent. Ordinary Shiu for κ^{Ω} is unavailable for the reason above. Supply a standard progression Selberg–Delange bound with its uniformity, or a proof using a prime-power decomposition.
* One cannot simply apply reduced-class Shiu modulo **8c** to both factors. The mod-8 conditions on the factors are not fixed reduced classes; for odd c the product cn+1 is even. Work first modulo c, drop the n≡1 (8) restriction at a constant normalization cost, or explicitly split the 2-adic part.
* For d,e≥c², the two Shiu estimates plausibly give (c/φ(c)²)(log N)^f(κ), i.e. the expected extra c/φ(c). But the small-factor cases need their progression count and rounding terms, not just Σ1/d without explanation. Restricting the analytic proof to c≤log³N is enough for the barrier and makes these errors negligible. For larger c, use direct word counting, not an unproved uniform transfer to cn+1.

The all-c trivial estimate for T is easy independently: from n=cuw−u−w, c≥3, one gets n≥(c−2)uw, and hence at most O((N/c)log N) positive pairs (u,w), with the finitely small c absorbed. The endpoint restriction only reduces the count. This closes the large-coordinate range but not the missing polylogarithmic progression moment.

I expect a repair of the T bound to be possible. As written, its one-sentence proof is not a PROVED uniform theorem, and §§5.1–5.3 inherit this gap for the union of all three families.

### Lemma 5.0(b) — MINOR-REPAIR; witness mechanism works

The 2^a·p strategy is appropriate. Choosing one of the two n-mod-16 classes indeed permits a≤3. For T and c>64, neither factor of a factorization can be −1 modulo c if its prime-free factor is one of 1,2,4,8; this proves failure. Siegel–Walfisz in the resulting reduced prime progression, c≤log³N, then gives ≫N/log N witnesses. The finite script's condition p>2c ensures its prime class is reduced, which is necessary for promotion to an infinite prime progression.

There are two false arithmetic assertions to correct:

* 2^i≡−1 (c), i≤3, does **not** force c | 9: c=5, i=2 is a counterexample. The relevant c≥3 are 3,5,9, all already within the finite check.
* c>64 does **not** imply φ(c)≥32: φ(66)=20; φ(70)=φ(72)=φ(78)=φ(84)=φ(90)=24. These do not appear to destroy the witness argument, but the uniform BT subtraction must use a correct numerical threshold and account for the mod-8 compatibility. For even c only the a=0 divisor exclusion occurs; for odd c the mod-8 and mod-c conditions are coprime. This case split avoids an unjustified “four forbidden classes” subtraction.

The finite check correctly skips inadmissible V_c. I reran it successfully. Its claim is not “every c for V,” but every admissible V_c and every W_c,T_c in 3≤c≤64. State the domains consistently. Also handle W₁,W₂,T₁,T₂, or explicitly exclude them throughout the barrier definition; they are present in the union identity but absent from the floor theorem. These finitely many coordinates can be treated by elementary prime/2p witnesses and contribute only O(log log N), but this must not be left implicit in a max-over-all-c statement.

### Theorem 5.1 — MAJOR pending Lemma 5.0(a); optimization SOUND

Given valid uniform hit estimates and failure floors for the stated coordinate domains, the proof is correct. For each fixed C>1, h_c≥1−1/C forces c below log^{log2+ε}N; multiplying their number by O(log log N) gives log^{log2+o(1)}N. For the max cost over *all* c, add that above log³N the trivial hit estimate makes the cost O(1), and deal with c=1,2 if included.

The V-only version is already justified after the progression-floor repair. The extension to W is also straightforward. Do not label the three-family theorem unconditionally PROVED before supplying the T argument.

### Corollary 5.2 — MAJOR scope repair; formal implication SOUND

For the **literal definition** with a fixed C>1 multiplying every included unconditional marginal and with R≥0, the lower bound on the right-hand side follows immediately from Theorem 5.1. This is a genuine arithmetic budget theorem followed by a simple functional corollary, not a tautology in the strict logical sense: the nontrivial input is the quantitative marginal threshold/floor.

But its operational interpretation is overstated:

* A method with losses **at most C** need not output this formula with loss **exactly C** at every event. It can retain C_e=1+o(1) on cheap events. Increasing all those factors to C throws away precisely the information the method could exploit. The theorem bars formulas that actually pay a fixed loss, not all methods admitting a fixed upper bound for their losses.
* Conditional or fibrewise marginals need not be ≥ the unconditional marginals. Products/sums built from them are not in 𝔐_C.
* The claimed Nair–Tenenbaum/Henriot and Selberg examples have not been reduced to this exact form with a fixed absolute C. A growing-dimensional singular factor, or a weighted sum of conditional products, is not automatically an instance.
* No literal member of the exactly defined class escapes the budget, assuming the arithmetic lemmas. The escape is from the **claimed examples/scope**, not a counterexample to the elementary product inequality.

Thus this is potentially a useful barrier for a narrowly and honestly specified method class, not a theorem about all non-CRT shift methods. The binding fallback asks for a class strictly larger than previously barred classes; saying “not CRT-specific” does not prove that inclusion. Explain whether the new class is instead incomparable, and exhibit a meaningful non-CRT output genuinely covered.

### Theorem 5.3 — MAJOR scope/foundation repair; exponent algebra and table SOUND

Conditional on uniform versions of Lemma 5.0(a), the marginal-budget optimization is correct. The implication h>ε/(1+ε) and the integral/binning maximization of βlog2−Q(β)=f(β) are sound. For precision, make the uniformity on compact β ranges explicit (a finite mesh and monotonic cutoffs suffice), rather than substitute a moving β into a theorem stated only for fixed β.

The inequality ε/(1+ε)≥(log N)^(−a)/2 follows directly from monotonicity if ε≥(log N)^(−a); it is fine even for large ε. The maximum is attained at β_a because f′(β)=log(2/β)>0 for β<2.

Independently recomputed values:

| θ | β | Q(β) | βlog2 |
|---|---:|---:|---:|
| .70 | 1.0099578199 | .0000494153 | .7000494153 |
| .75 | 1.0873745411 | .0037105974 | .7537105974 |
| .80 | 1.1750792265 | .0145028528 | .8145028528 |
| .90 | 1.4018400146 | .0716814537 | .9716814537 |
| .99 | 1.8033618796 | .2599952024 | 1.2499952024 |

The table rounds correctly. The text proves at least log^{θ−o(1)}N **events** and a coordinate reaching log^{βlog2−o(1)}N; the summary conflates these when it says “over ≥log^.754 events.” A stronger event-number bound may be derivable by optimizing the largest k marginal costs, but it is not the stated equivalence/proof. Use the two quantities as stated, or prove the stronger assertion.

### Remark 5.4 and §5.4 — MAJOR for the asserted extensions

The observed failure of exact unconditional products is real. But the square-floor inference about the sum of costs requires R=0, or at least R=o(√N). With arbitrary R≥0 in the class definition, R alone can pay for every square and the stated necessary cost bound does not follow.

Most importantly, **delete the applications of Theorem 5.3 to methods explicitly declared “not covered”**:

1. A chain of conditional ratios can have conditional hit probabilities much larger than marginal ones. Nothing in Theorem 5.3 forces its per-step accuracy to be log^(−.0037)N, or forces conditioning on a quadratic profile. The general abstract countermechanism is disjoint hits: a hit of unconditional probability h has conditional probability h/(1−jh) after j disjoint hits have been excluded, eventually close to 1. A theorem about unconditional marginal costs does not control that phenomenon.
2. Refining one coordinate event into many divisor-window events destroys the “one coordinate used once” hypothesis and changes the marginal budget. Theorem 5.3 does not apply to these refinements without a new lemma. In particular, the number of subevents at a given coordinate is not bounded by the count of coordinates used in its proof.

These are not cosmetic qualifications: they are precisely the proposed open-door routes. The document cannot claim both that they are outside the theorem and that the theorem imposes its numerical precision requirement on them.

## 6. Computations and data audit

All review computations used `ulimit -v 8000000` and timeouts. No large factorization run or N=10⁸ census was repeated.

### Independently rerun

* Compiled `scripts/z50_shifts_joint.c` with `gcc -O2 ... -lm` and ran N=200000, V=40. On n≡1 (8), there are 25000 inputs; final failures are **224 squares and 42 nonsquares**, J(40)=.01064. On n≡5 (8), v=3 has exactly zero marginal failures, hence zero joint failures.
* Ran the C program at N=20000, V=40 and `uv run python scripts/z50_shifts_joint_brute.py 20000 40`. After removing comment lines, **all table rows match exactly**.
* Ran `uv run --with sympy python scripts/z50_shifts_floorcheck.py 64 200000`. Output: **`no witness found for: []`**. Inspection confirms that the retained witness has p>2c, so the reduced-class condition is not merely assumed.
* Enumerated the 12600-point CRT NA test described above: **zero violating fibres**.
* Recomputed the precision table and the arithmetic counterexamples above independently.

### §3.2 / §§6.2–6.4 — MINOR-REPAIR; principal counts SOUND

The four rows in §3.2 match `profile9_N1e8.txt` after rounding. The full joint table gives 5000 squares and 39 nonsquares at V=128, as claimed. The 5000-square floor relative to 12500000 inputs is .0004. At V=60 the ratio to the floor is 1.101, so “above V≈60 within 1.1” is a harmless approximation (true from V=63).

The nine-prime profile is **not the full vector of quadratic characters**: `z50_shifts_profile9.c` uses the binary indicator of being a nonresidue and merges 0 with +1. The five-prime version is ternary. Correct the §3.2 description; neither profile is the full small-prime-power fibre from Theorem 3.1. Consequently these numerical mixtures do not directly test that theorem.

The product/excess figures in the profile data really are conditioned on nonsquares; distinguish them from `z50_shifts_analyze.py`, which subtracts the square fraction without renormalizing and leaves the all-integer marginal product in place. The main table cites the appropriate profile data, so the published rounded numbers are not broken by this distinction.

The full N=10⁸ computation is a recorded census, not independently recertified in this review. The C/brute small-scale agreement and code inspection support its interpretation, not an independent certification of every large-run output.

### §6.1 — MINOR-REPAIR

The four fixed-modulus scaled failure ranges match the data (rounding endpoints loosely). However “P(hit_v)·v/log x≈0.8–0.9 for v≥2000” does not describe all four scales. Across the listed v≥2048, the actual ranges are:

| scale | min | max |
|---|---:|---:|
| 10⁸ | .367 | .628 |
| 10¹⁶ | .734 | .839 |
| 10²⁴ | .871 | 1.012 |
| 10³² | .869 | .934 |

Qualify it as a large-scale rough observation. The maximum binomial **standard error** at 20000 samples is .00354; ±.0035 is not a uniform confidence interval. The half-point in φ(v) also needs a defined interpolation/family rule: hit probability is not monotone in φ(v) across unrelated moduli. This does not invalidate the raw data, but the advertised four half-point exponents are not reproducible from a stated estimator.

## 7. Source checks and labels

I visited the following sources, not merely search snippets:

* Erdős–Hall, Cambridge article, DOI `10.1017/S0305004100052270`: the extract confirms the preceding Erdős theorem; its displayed image reads k<2^{(1−ε)log log x}, consistent with the claimed threshold. URL: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/proof-of-a-conjecture-about-the-distribution-of-divisors-of-integers-in-residue-classes/7065135EA6373562EFA28CD5AE61B490 . I did not read the full paywalled paper and do not certify a more detailed uniform formulation of its converse.
* Henriot, *Nair–Tenenbaum bounds uniform with respect to the discriminant*, https://arxiv.org/html/1102.1643v1 : the introduction states the Shiu range/growth hypotheses, the Nair–Tenenbaum no-fixed-prime-divisor hypothesis, and the dependence on degree/discriminant. These are the source of the analytic qualifications above.
* Wright, *A Shiu Theorem for Larger and Smoother Functions*, https://arxiv.org/html/2508.17217v1 , Theorem 1.1 restates classical Shiu with the same subpolynomial-growth and reduced-progression hypotheses. No result of this newer preprint is used as a proof input here.

A targeted search did not reveal a published U-named exceptional-set theorem or a post-2025 resolution relevant to this audit. That is not an exhaustive literature nonexistence claim. The prime-local θ=1/2 consequence should be included regardless of whether U was previously named.

Label repairs:

* Keep 2/3 and .409 as Assessments, not proved caps.
* Downgrade the T part of Lemma 5.0(a), and consequently the unrestricted three-family versions of 5.1–5.3, until the progression estimates are written.
* Keep the fixed-v law, the unrestricted hit bound, and Theorem 3.1 as proved mathematics with their actual domains.
* Remove blanket “χ-route barred,” “all constant-loss methods,” and “chains/refinements need this precision” conclusions.
* Corollary 5.2 is an immediate corollary of a marginal budget, not itself a mechanism for bounding E_U. The document is honest that it has no new θ>0 from the fixed-k shift argument, but its summary makes the barrier's novelty and reach look broader than demonstrated. Meeting the campaign fallback requires more than restating the cost profile and defining a class that pays the losses one wants to cap.

## Claim verdict table

| Claim | Verdict | One-line reason |
|---|---|---|
| §1.1 | SOUND | Both explicit divisors and congruence reductions are correct. |
| §1.2 mass / nontransfer | MINOR-REPAIR | Mass and exceptional-set direction correct; class-membership iff is false. |
| §1.2 whole-U CRT coverage | MAJOR | A cap for one line does not cap the unchecked union. |
| Lemma 2.1 | SOUND | Subproduct construction and index-2 case are valid. |
| Theorem 2.2 | SOUND | Fixed-v Wirsing, rare-outside-prime bound and intersections work. |
| Theorem 2.3 | MINOR-REPAIR | Bound works; ordinary Shiu does not handle κ^Ω for κ>1. |
| Proposition 2.4 | MAJOR | Progression assertion false at v=3; primes cannot witness the odd admissible line. |
| Proposition 2.5 | SOUND | Sathe–Selberg and both divisor ranges give the stated rate. |
| Conjecture 2.6 / summary | MINOR-REPAIR | Fixed-v half exponent is not a growing-v theorem. |
| Theorem 3.1 | SOUND | NA proof is correct with full capped prime-power fibres and p≤D. |
| §3.1 profile heuristic | MINOR-REPAIR | Specify the quadratic character; profile conditioning is weaker than the theorem's fibre. |
| §3.3 correlation survey | MAJOR | Missing hypotheses and unjustified C-lossy-product interpretation. |
| §3.3 χ reduction | MAJOR | Valid for periodic CRT means on the 4-line, not a ban on non-CRT character use. |
| Proposition 4.1 | MINOR-REPAIR | Fix the fixed-prime-divisor hypothesis; the log-power conclusion survives. |
| Assessment 4.2 | SOUND | .409 algebra is correct for the explicitly assumed implementation. |
| Lemma 5.0(a) | MAJOR | T progression moment and small-factor/range treatment are missing. |
| Lemma 5.0(b) | MINOR-REPAIR | Witness mechanism survives; two numerical claims and small-coordinate domains need fixes. |
| Theorem 5.1 | MAJOR | Sound budget conditional on repaired three-family inputs. |
| Corollary 5.2 | MAJOR | Literal formula cap works; loss-at-most-C and named-method coverage are overclaims. |
| Theorem 5.3 | MAJOR | Algebra/table correct; three-family foundation and outside-class applications are not. |
| Remark 5.4 / §5.4 | MAJOR | R can pay for squares; conditional ratios and refinements are not constrained by this theorem. |
| §3.2 / §§6.2–6.4 | MINOR-REPAIR | Small reruns and table values agree; describe the binary profile correctly. |
| §6.1 | MINOR-REPAIR | Fixed-v data agree; first-moment summary and error-bar/half-point descriptions need qualification. |

## Required repairs, in priority order

1. **Remove the false scope extensions:** conditional chains, refined subevents, arbitrary χ methods, and losses merely bounded above by C are not barred by 5.2/5.3.
2. **Prove the T-coordinate estimate properly**, including the uniform κ^Ω progression moment, reduced-class issue, and small-factor terms; otherwise restrict the proved barrier to V/W.
3. **Repair Proposition 2.4 and the floors:** restrict admissible endpoint domains, use 2^a·p on the odd line, fix c=5 and φ(66), and address coordinates 1,2.
4. **Restore precise CRT scope to the polynomial reduction**, explicitly truncate witness counts, and supply the odd-line extension if claimed.
5. **Correct the audit:** remove the residue-class iff, verify the odd-line forced-family inclusion before invoking full-U ledger caps, and acknowledge the standard prime-local θ=1/2 U bound.
6. **Make proof hypotheses/citations exact:** remove the invalid Shiu alternative for κ^Ω, fix the Nair–Tenenbaum fixed-prime-divisor issue, and distinguish fixed-k constants from hypothetical growing-k bounds.
7. **Fix labels and numerical prose:** distinguish event counts from coordinate reach, binary from ternary/full profiles, standard errors from confidence intervals, and low-scale data from the claimed first-moment trend.
